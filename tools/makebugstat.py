import launchpadlib
import sys

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
    def __init__(self, lptask):
        self.web_link = lptask.web_link
        self.title = lptask.title
        self.lptask = lptask
        self.number = int(self.web_link.split('/')[-1])

    @property
    def category(self):
        return categories[self.number]

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


class TaskList(object):
    def __init__(self, prj_name, taskgen):
        self.tasks = [task for task in sorted(taskgen, key=lambda x: x.number, reverse=True) if task.relevant]
        self.prj_name = prj_name

    def print_statistics(self):
        fixed_tasks = [task for task in self.tasks if task.fixed]
        print "Fixed/Pending ratio:", len(fixed_tasks), '/', len(self.tasks)

    def printout(self):
        if not self.tasks:
            return

        print "#", prj_name
        self.print_statistics()
        for category, tasks in self.tasks_by_category():
            if not tasks:
                continue
            print "##", category
            for task in tasks:
                task.printout()

    def tasks_by_category(self):
        result = dict((cat, []) for cat in set(categories.values()))
        for task in self.tasks:
            result[task.category].append(task)

        for category, tasks in sorted(result.items(), key=lambda x: len(x[1]), reverse=True):
            yield category, tasks


def tasks(prj_name, keywords):
    prj = launchpad.projects[prj_name]
    for task in prj.searchTasks(search_text='xenapi'):
        yield Task(task)


for prj_name in ['nova', 'cinder', 'quantum', 'glance']:
    tasklist = TaskList(prj_name, tasks(prj_name, ['xen', 'xcp', 'xapi']))
    tasklist.printout()
