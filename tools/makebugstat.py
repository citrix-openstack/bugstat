import launchpadlib
import sys
import os

from launchpadlib.launchpad import Launchpad


cachedir = sys.argv[1]

launchpad = Launchpad.login_anonymously('just testing', 'production', cachedir)


STORAGE = 'storage/disk'
DISCUSSION = 'discussion'
METRICS = 'metrics'
CONSOLE = 'console'
POOLS = 'pools'
QABUG = 'qabug'
NETWORKING = 'networking'
SPAWN = 'instance spawn'
MIGRATION = 'migration'
MISSINGIMPLEMENTATION = 'missing implementation'
FIXED = 'fixed'
NONXEN = 'non-xen'
NEW = 'new'

categories = {
    816406: DISCUSSION,
    929062: STORAGE,
    952816: STORAGE,
    954913: METRICS,
    962097: MIGRATION,
    962144: STORAGE,
    1004175: CONSOLE,
    1015190: METRICS,
    1015423: STORAGE,
    1026153: POOLS,
    1026552: POOLS,
    1030108: STORAGE,
    1037516: QABUG,
    1043886: NETWORKING,
    1061062: SPAWN,
    1073303: MIGRATION,
    1073306: MIGRATION,
    1097980: MISSINGIMPLEMENTATION,
    1098382: FIXED,
    1100866: FIXED,
    1101229: FIXED,
    1104967: NONXEN,
}

REVIEW = 'review'
ISITVALID = 'is it valid?'
PINGIT = 'ping it'
XSBUG = 'maybe a xenserver bug'

ACTIONS = {
    1004175: REVIEW,
    1015190: ISITVALID,
    1015423: PINGIT,
    1026153: ISITVALID,
    1026552: ISITVALID,
    1030108: XSBUG,
}


def to_key_value(obj):
    for attrname in dir(obj):
        if not attrname.startswith('_'):
            attr = getattr(obj, attrname)
            if not callable(attr):
                yield (attrname, attr)

def to_dict(obj):
    return dict(to_key_value(obj))


class Task(object):
    def __init__(self, web_link, title):
        self.web_link = web_link
        self.title = ":".join(item.strip(' "') for item in title.split(':')[1:])
        self.number = int(self.web_link.split('/')[-1])

    @property
    def category(self):
        return categories.get(self.number, NEW)

    @property
    def relevant(self):
        return NONXEN != self.category

    @property
    def actions(self):
        actions = ACTIONS.get(self.number, "")
        if actions:
            if isinstance(actions, str):
                actions = [actions]
            return "[" + ", ".join(actions) + "]"
        return ""

    def printout(self):
        print " * %s[%s](%s)" % (self.actions, self.title, self.web_link)

    @property
    def fixed(self):
        return self.category == FIXED

    def save(self):
        with open(os.path.join("tasks", str(self.number)), "wb") as f:
            f.write(repr(dict(web_link=self.web_link, title=self.title)))


class TaskList(object):
    def __init__(self, prj_name, taskgen):
        self.tasks = [task for task in sorted(taskgen, key=lambda x: x.number, reverse=True) if task.relevant]
        self.prj_name = prj_name

    def print_statistics(self):
        print ""
        fixed_tasks = [task for task in self.tasks if task.fixed]
        print "Fixed/Pending ratio:", len(fixed_tasks), '/', len(self.tasks)
        print ""

    def printout(self):
        print "#", self.prj_name, " - ", len(self.tasks)
        if not self.tasks:
            print ""
            print "No bugs found"
            print ""
            return

        self.print_statistics()
        for category, tasks in self.tasks_by_category():
            if not tasks:
                continue
            print "##", category
            print ""
            for task in tasks:
                task.printout()
            print ""

    def tasks_by_category(self):
        result = dict((cat, []) for cat in set(categories.values() + [NEW]))
        for task in self.tasks:
            result[task.category].append(task)

        for category, tasks in sorted(result.items(), key=lambda x: len(x[1]), reverse=True):
            yield category, tasks


def search_task_by_text_or_tag(prj_name, keywords, tags, task_db):
    prj = launchpad.projects[prj_name]

    for keyword in keywords:
        for lptask in prj.searchTasks(search_text=keyword):
            task = Task(lptask.web_link, lptask.title)

            if task.number not in task_db:
                task_db[task.number] = task
                task.save()
                yield task

    for tag in tags:
        for lptask in prj.searchTasks(tags=tag):
            task = Task(lptask.web_link, lptask.title)

            if task.number not in task_db:
                task_db[task.number] = task
                task.save()
                yield task


def main():
    task_db = dict()
    tasklists = []

    for prj_name in ['nova', 'cinder', 'quantum', 'glance']:
        tasklists.append(
            TaskList(prj_name, search_task_by_text_or_tag(prj_name, ['xenserver', 'xenapi', 'xen', 'xcp', 'xapi'], ['xenserver'], task_db)))

    print "# Summary"
    print ""
    print "Fixed/Pending Ratio:", len([t for t in task_db.values() if t.fixed]), "/", len(task_db)
    print ""

    for tasklist in tasklists:
        tasklist.printout()


if __name__ == "__main__":
    main()
