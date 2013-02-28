# Summary

Fixed/Pending Ratio: 2 / 40

# nova  - `34`

Fixed/Pending ratio: 1 / 34

## new

 * `1024944` [XenServer:If file system is directly is on root device, auto_disk_configure does not work](https://bugs.launchpad.net/nova/+bug/1024944)
 * `934279` [Need more efficient implementation of get_num_instances() and instance_exists() in Xen and VMWare virt drivers](https://bugs.launchpad.net/nova/+bug/934279)
 * `914484` [Boot from ISO is different in XS/KVM](https://bugs.launchpad.net/nova/+bug/914484)
 * `912684` [Xen instances:support for randomly-named and uncompressed images](https://bugs.launchpad.net/nova/+bug/912684)
 * `903445` [New xapi backend for Local Storage ISO SR](https://bugs.launchpad.net/nova/+bug/903445)
 * `903282` [Instances spawned on XenServer cannot communicate](https://bugs.launchpad.net/nova/+bug/903282)
 * `902663` [dom0 management traffic is not allowed to flow across a VLAN](https://bugs.launchpad.net/nova/+bug/902663)
 * `813793` [Resize up from an instance with no local storage not handled properly in XenServer](https://bugs.launchpad.net/nova/+bug/813793)
 * `747394` [XenServer port needs to clear out vm-data/networking before issuing resetnetwork command](https://bugs.launchpad.net/nova/+bug/747394)

## storage/disk

 * `1134493` [Add retry on upload_vhd in xapi glance plugin](https://bugs.launchpad.net/nova/+bug/1134493)
 * `1103158` [XenServer not cleaning up SM locks](https://bugs.launchpad.net/nova/+bug/1103158)
 * `1030108` [maybe a xenserver bug][Detaching a volume from a XenAPI instance fails if XenAPI thinks it is in use](https://bugs.launchpad.net/nova/+bug/1030108)
 * `1015423` [ping it][xenapi ImageTooLarge exception leaves VDI around](https://bugs.launchpad.net/nova/+bug/1015423)
 * `962144` [xenapi resize fails on image with external ramdisk and kernel](https://bugs.launchpad.net/nova/+bug/962144)
 * `952816` [xenapi resize fails on Essex4 while using COW](https://bugs.launchpad.net/nova/+bug/952816)
 * `929062` [/images filling up on xenserver host](https://bugs.launchpad.net/nova/+bug/929062)

## migration

 * `1135465` [block live migration is broken:InstanceNotFound](https://bugs.launchpad.net/nova/+bug/1135465)
 * `1131588` [virt drivers' resume_state_on_host_boot don't handle migrating instances](https://bugs.launchpad.net/nova/+bug/1131588)
 * `1073306` [xenapi migrations don't apply security group filters](https://bugs.launchpad.net/nova/+bug/1073306)
 * `1073303` [xenapi finish_migration does not cleanup on failures](https://bugs.launchpad.net/nova/+bug/1073303)
 * `962097` [in xenapi migration plugin the vhd-util calls fail on kronos](https://bugs.launchpad.net/nova/+bug/962097)

## metrics

 * `1015190` [is it valid?][arch_filter tracebacks with xenapi](https://bugs.launchpad.net/nova/+bug/1015190)
 * `954913` [xenapi host refresh not dealing with exceptions well when updating host stats](https://bugs.launchpad.net/nova/+bug/954913)

## missing implementation

 * `1100697` [libvirt should enable pae setting for Xen or KVM guest](https://bugs.launchpad.net/nova/+bug/1100697)
 * `1097980` [XenAPI should implement list_instance_uuids()](https://bugs.launchpad.net/nova/+bug/1097980)

## pools

 * `1026552` [is it valid?][XenAPI pool based migration should error when not shared storage](https://bugs.launchpad.net/nova/+bug/1026552)
 * `1026153` [is it valid?][Need to deal with XenAPI pool master election](https://bugs.launchpad.net/nova/+bug/1026153)

## networking

 * `1043886` [Firewall rules are not updated if you restart nova-compute](https://bugs.launchpad.net/nova/+bug/1043886)

## console

 * `1004175` [review][XenAPI text console support](https://bugs.launchpad.net/nova/+bug/1004175)

## discussion

 * `816406` [Service stats needs to be unified across virt layer](https://bugs.launchpad.net/nova/+bug/816406)

## fixed

 * `1052085` [Raw disk key error 'root'](https://bugs.launchpad.net/nova/+bug/1052085)

## qabug

 * `1037516` [Over time XenAPI driver eventuall fills up Dom0 disk](https://bugs.launchpad.net/nova/+bug/1037516)

## instance spawn

 * `1061062` [Asynchronous errors can only be reported if instance is in ERROR](https://bugs.launchpad.net/nova/+bug/1061062)

## minor

 * `1074087` [Xen migration driver should use execvp](https://bugs.launchpad.net/nova/+bug/1074087)

# cinder  - `1`

Fixed/Pending ratio: 1 / 1

## fixed

 * `1131291` [XenAPINFS:Volume always uploaded as vhd/ovf](https://bugs.launchpad.net/cinder/+bug/1131291)

# quantum  - `3`

Fixed/Pending ratio: 0 / 3

## new

 * `1005616` [Windows instances may not get correct port configuration as set by quantum](https://bugs.launchpad.net/quantum/+bug/1005616)
 * `994831` [ovs_quantum_plugin incompatibility with python 2.4](https://bugs.launchpad.net/quantum/+bug/994831)
 * `994774` [ovs_quantum_agent.py crashes on Citrix XCP because of old python version (2.4)](https://bugs.launchpad.net/quantum/+bug/994774)

# glance  - `1`

Fixed/Pending ratio: 0 / 1

## new

 * `1055399` [windows image upload on xen host results in sr scan failure](https://bugs.launchpad.net/glance/+bug/1055399)

