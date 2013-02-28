# Summary

Fixed/Pending Ratio: 1 / 40

# nova  - `34`

Fixed/Pending ratio: 0 / 34

## new

 * [block live migration is broken:InstanceNotFound](https://bugs.launchpad.net/nova/+bug/1135465)
 * [Add retry on upload_vhd in xapi glance plugin](https://bugs.launchpad.net/nova/+bug/1134493)
 * [virt drivers' resume_state_on_host_boot don't handle migrating instances](https://bugs.launchpad.net/nova/+bug/1131588)
 * [XenServer not cleaning up SM locks](https://bugs.launchpad.net/nova/+bug/1103158)
 * [libvirt should enable pae setting for Xen or KVM guest](https://bugs.launchpad.net/nova/+bug/1100697)
 * [Xen migration driver should use execvp](https://bugs.launchpad.net/nova/+bug/1074087)
 * [Raw disk key error 'root'](https://bugs.launchpad.net/nova/+bug/1052085)
 * [XenServer:If file system is directly is on root device, auto_disk_configure does not work](https://bugs.launchpad.net/nova/+bug/1024944)
 * [Need more efficient implementation of get_num_instances() and instance_exists() in Xen and VMWare virt drivers](https://bugs.launchpad.net/nova/+bug/934279)
 * [Boot from ISO is different in XS/KVM](https://bugs.launchpad.net/nova/+bug/914484)
 * [Xen instances:support for randomly-named and uncompressed images](https://bugs.launchpad.net/nova/+bug/912684)
 * [New xapi backend for Local Storage ISO SR](https://bugs.launchpad.net/nova/+bug/903445)
 * [Instances spawned on XenServer cannot communicate](https://bugs.launchpad.net/nova/+bug/903282)
 * [dom0 management traffic is not allowed to flow across a VLAN](https://bugs.launchpad.net/nova/+bug/902663)
 * [Resize up from an instance with no local storage not handled properly in XenServer](https://bugs.launchpad.net/nova/+bug/813793)
 * [XenServer port needs to clear out vm-data/networking before issuing resetnetwork command](https://bugs.launchpad.net/nova/+bug/747394)

## storage/disk

 * [maybe a xenserver bug][Detaching a volume from a XenAPI instance fails if XenAPI thinks it is in use](https://bugs.launchpad.net/nova/+bug/1030108)
 * [ping it][xenapi ImageTooLarge exception leaves VDI around](https://bugs.launchpad.net/nova/+bug/1015423)
 * [xenapi resize fails on image with external ramdisk and kernel](https://bugs.launchpad.net/nova/+bug/962144)
 * [xenapi resize fails on Essex4 while using COW](https://bugs.launchpad.net/nova/+bug/952816)
 * [/images filling up on xenserver host](https://bugs.launchpad.net/nova/+bug/929062)

## migration

 * [xenapi migrations don't apply security group filters](https://bugs.launchpad.net/nova/+bug/1073306)
 * [xenapi finish_migration does not cleanup on failures](https://bugs.launchpad.net/nova/+bug/1073303)
 * [in xenapi migration plugin the vhd-util calls fail on kronos](https://bugs.launchpad.net/nova/+bug/962097)

## metrics

 * [is it valid?][arch_filter tracebacks with xenapi](https://bugs.launchpad.net/nova/+bug/1015190)
 * [xenapi host refresh not dealing with exceptions well when updating host stats](https://bugs.launchpad.net/nova/+bug/954913)

## pools

 * [is it valid?][XenAPI pool based migration should error when not shared storage](https://bugs.launchpad.net/nova/+bug/1026552)
 * [is it valid?][Need to deal with XenAPI pool master election](https://bugs.launchpad.net/nova/+bug/1026153)

## networking

 * [Firewall rules are not updated if you restart nova-compute](https://bugs.launchpad.net/nova/+bug/1043886)

## console

 * [review][XenAPI text console support](https://bugs.launchpad.net/nova/+bug/1004175)

## discussion

 * [Service stats needs to be unified across virt layer](https://bugs.launchpad.net/nova/+bug/816406)

## qabug

 * [Over time XenAPI driver eventuall fills up Dom0 disk](https://bugs.launchpad.net/nova/+bug/1037516)

## instance spawn

 * [Asynchronous errors can only be reported if instance is in ERROR](https://bugs.launchpad.net/nova/+bug/1061062)

## missing implementation

 * [XenAPI should implement list_instance_uuids()](https://bugs.launchpad.net/nova/+bug/1097980)

# cinder  - `1`

Fixed/Pending ratio: 1 / 1

## fixed

 * [XenAPINFS:Volume always uploaded as vhd/ovf](https://bugs.launchpad.net/cinder/+bug/1131291)

# quantum  - `3`

Fixed/Pending ratio: 0 / 3

## new

 * [Windows instances may not get correct port configuration as set by quantum](https://bugs.launchpad.net/quantum/+bug/1005616)
 * [ovs_quantum_plugin incompatibility with python 2.4](https://bugs.launchpad.net/quantum/+bug/994831)
 * [ovs_quantum_agent.py crashes on Citrix XCP because of old python version (2.4)](https://bugs.launchpad.net/quantum/+bug/994774)

# glance  - `1`

Fixed/Pending ratio: 0 / 1

## new

 * [windows image upload on xen host results in sr scan failure](https://bugs.launchpad.net/glance/+bug/1055399)

