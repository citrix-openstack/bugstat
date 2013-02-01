# nova
Fixed/Pending ratio: 3 / 21

## storage/disk

 * [maybe a xenserver bug][Bug #1030108 in OpenStack Compute (nova): "Detaching a volume from a XenAPI instance fails if XenAPI thinks it is in use"](https://bugs.launchpad.net/nova/+bug/1030108)
 * [ping it][Bug #1015423 in OpenStack Compute (nova): "xenapi ImageTooLarge exception leaves VDI around"](https://bugs.launchpad.net/nova/+bug/1015423)
 * [Bug #962144 in OpenStack Compute (nova): "xenapi resize fails on image with external ramdisk and kernel"](https://bugs.launchpad.net/nova/+bug/962144)
 * [Bug #952816 in OpenStack Compute (nova): "xenapi resize fails on Essex4 while using COW"](https://bugs.launchpad.net/nova/+bug/952816)
 * [Bug #929062 in OpenStack Compute (nova): "/images filling up on xenserver host"](https://bugs.launchpad.net/nova/+bug/929062)

## migration

 * [Bug #1073306 in OpenStack Compute (nova): "xenapi migrations don't apply security group filters"](https://bugs.launchpad.net/nova/+bug/1073306)
 * [Bug #1073303 in OpenStack Compute (nova): "xenapi finish_migration does not cleanup on failures"](https://bugs.launchpad.net/nova/+bug/1073303)
 * [Bug #962097 in OpenStack Compute (nova): "in xenapi migration plugin the vhd-util calls fail on kronos"](https://bugs.launchpad.net/nova/+bug/962097)

## fixed

 * [Bug #1101229 in OpenStack Compute (nova): "xenapi: error on volume detach StorageError: Unable to find SR from VBD"](https://bugs.launchpad.net/nova/+bug/1101229)
 * [Bug #1100866 in OpenStack Compute (nova): "[xen] create/update metadata during boot can put instance into ERROR"](https://bugs.launchpad.net/nova/+bug/1100866)
 * [Bug #1098382 in OpenStack Compute (nova): "xenapi get_all_bw_counters accesses instance as object"](https://bugs.launchpad.net/nova/+bug/1098382)

## metrics

 * [is it valid?][Bug #1015190 in OpenStack Compute (nova): "arch_filter tracebacks with xenapi"](https://bugs.launchpad.net/nova/+bug/1015190)
 * [Bug #954913 in OpenStack Compute (nova): "xenapi host refresh not dealing with exceptions well when updating host stats"](https://bugs.launchpad.net/nova/+bug/954913)

## pools

 * [is it valid?][Bug #1026552 in OpenStack Compute (nova): "XenAPI pool based migration should error when not shared storage"](https://bugs.launchpad.net/nova/+bug/1026552)
 * [is it valid?][Bug #1026153 in OpenStack Compute (nova): "Need to deal with XenAPI pool master election"](https://bugs.launchpad.net/nova/+bug/1026153)

## console

 * [review][Bug #1004175 in OpenStack Compute (nova): "XenAPI text console support"](https://bugs.launchpad.net/nova/+bug/1004175)

## discussion

 * [Bug #816406 in OpenStack Compute (nova): "Service stats needs to be unified across virt layer"](https://bugs.launchpad.net/nova/+bug/816406)

## networking

 * [Bug #1043886 in OpenStack Compute (nova): "Firewall rules are not updated if you restart nova-compute"](https://bugs.launchpad.net/nova/+bug/1043886)

## qabug

 * [Bug #1037516 in OpenStack Compute (nova): "Over time XenAPI driver eventuall fills up Dom0 disk"](https://bugs.launchpad.net/nova/+bug/1037516)

## instance spawn

 * [Bug #1061062 in OpenStack Compute (nova): "Asynchronous errors can only be reported if instance is in ERROR"](https://bugs.launchpad.net/nova/+bug/1061062)

## missing implementation

 * [Bug #1097980 in OpenStack Compute (nova): "XenAPI should implement list_instance_uuids()"](https://bugs.launchpad.net/nova/+bug/1097980)
