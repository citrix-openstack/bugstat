# Summary

Fixed/Pending Ratio: 4 / 56

# nova  - `34`

Fixed/Pending ratio: 3 / 34

## storage/disk

 * `1030108` [maybe a xenserver bug][Detaching a volume from a XenAPI instance fails if it is in use](https://bugs.launchpad.net/nova/+bug/1030108)
 * `1015423` [ping it][xenapi ImageTooLarge exception leaves VDI around](https://bugs.launchpad.net/nova/+bug/1015423)
 * `962144` [xenapi resize fails on image with external ramdisk and kernel](https://bugs.launchpad.net/nova/+bug/962144)
 * `952816` [xenapi resize fails on Essex4 while using COW](https://bugs.launchpad.net/nova/+bug/952816)
 * `914484` [Boot from ISO is different in XS/KVM](https://bugs.launchpad.net/nova/+bug/914484)
 * `912684` [Xen instances:support for randomly-named and uncompressed images](https://bugs.launchpad.net/nova/+bug/912684)
 * `903445` [New xapi backend for Local Storage ISO SR](https://bugs.launchpad.net/nova/+bug/903445)

## new

 * `1152713` [keypair extension doesn't work with xenapi and agent](https://bugs.launchpad.net/nova/+bug/1152713)
 * `1152401` [xenapi:Detecting bad-volumes relies on 120 sec timeout](https://bugs.launchpad.net/nova/+bug/1152401)
 * `1152268` [XenAPI:Resize tempest test is failing (shrink problem)](https://bugs.launchpad.net/nova/+bug/1152268)
 * `1148614` [Reboot with bad volume fails ungracefully](https://bugs.launchpad.net/nova/+bug/1148614)

## migration

 * `1073306` [xenapi migrations don't apply security group filters](https://bugs.launchpad.net/nova/+bug/1073306)
 * `1073303` [xenapi finish_migration does not cleanup on failures](https://bugs.launchpad.net/nova/+bug/1073303)
 * `962097` [in xenapi migration plugin the vhd-util calls fail on kronos](https://bugs.launchpad.net/nova/+bug/962097)

## stale

 * `903282` [Instances spawned on XenServer cannot communicate](https://bugs.launchpad.net/nova/+bug/903282)
 * `902663` [dom0 management traffic is not allowed to flow across a VLAN](https://bugs.launchpad.net/nova/+bug/902663)
 * `747394` [XenServer port needs to clear out vm-data/networking before issuing resetnetwork command](https://bugs.launchpad.net/nova/+bug/747394)

## fixed

 * `1134493` [Add retry on upload_vhd in xapi glance plugin](https://bugs.launchpad.net/nova/+bug/1134493)
 * `1131588` [virt drivers' resume_state_on_host_boot don't handle migrating instances](https://bugs.launchpad.net/nova/+bug/1131588)
 * `1052085` [Raw disk key error 'root'](https://bugs.launchpad.net/nova/+bug/1052085)

## minor

 * `1074087` [Xen migration driver should use execvp](https://bugs.launchpad.net/nova/+bug/1074087)
 * `1024944` [XenServer:If file system is directly is on root device, auto_disk_configure does not work](https://bugs.launchpad.net/nova/+bug/1024944)
 * `813793` [Resize up from an instance with no local storage not handled properly in XenServer](https://bugs.launchpad.net/nova/+bug/813793)

## metrics

 * `1015190` [is it valid?][arch_filter tracebacks with xenapi](https://bugs.launchpad.net/nova/+bug/1015190)
 * `954913` [xenapi host refresh not dealing with exceptions well when updating host stats](https://bugs.launchpad.net/nova/+bug/954913)

## pools

 * `1026552` [is it valid?][XenAPI pool based migration should error when not shared storage](https://bugs.launchpad.net/nova/+bug/1026552)
 * `1026153` [is it valid?][Need to deal with XenAPI pool master election](https://bugs.launchpad.net/nova/+bug/1026153)

## missing implementation

 * `1100697` [libvirt should enable pae setting for Xen or KVM guest](https://bugs.launchpad.net/nova/+bug/1100697)
 * `1097980` [XenAPI should implement list_instance_uuids()](https://bugs.launchpad.net/nova/+bug/1097980)

## console

 * `1004175` [review][XenAPI text console support](https://bugs.launchpad.net/nova/+bug/1004175)

## instance spawn

 * `1061062` [Asynchronous errors can only be reported if instance is in ERROR](https://bugs.launchpad.net/nova/+bug/1061062)

## qabug

 * `1037516` [Over time XenAPI driver eventuall fills up Dom0 disk](https://bugs.launchpad.net/nova/+bug/1037516)

## networking

 * `1043886` [Firewall rules are not updated if you restart nova-compute](https://bugs.launchpad.net/nova/+bug/1043886)

## discussion

 * `816406` [Service stats needs to be unified across virt layer](https://bugs.launchpad.net/nova/+bug/816406)

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

# openstack-manuals  - `17`

Fixed/Pending ratio: 0 / 17

## new

 * `1106421` [grizzly:allow vm disk driver to be chosen per image](https://bugs.launchpad.net/openstack-manuals/+bug/1106421)
 * `1106405` [grizzly:xenapi:Add support for different image upload drivers](https://bugs.launchpad.net/openstack-manuals/+bug/1106405)
 * `1095506` [grizzly:add configdrive support for xenapi](https://bugs.launchpad.net/openstack-manuals/+bug/1095506)
 * `1026745` [Quantum docs should describe XenAPI setup](https://bugs.launchpad.net/openstack-manuals/+bug/1026745)
 * `1026742` [Add hints on troubleshooting XenAPI deployments](https://bugs.launchpad.net/openstack-manuals/+bug/1026742)
 * `1026693` [Need to document Nova-volume on XenAPI](https://bugs.launchpad.net/openstack-manuals/+bug/1026693)
 * `1026691` [Networking docs split for XenAPI and Libvirt too heavyweight](https://bugs.launchpad.net/openstack-manuals/+bug/1026691)
 * `1026689` [Need to better describe Network HA and XenAPI](https://bugs.launchpad.net/openstack-manuals/+bug/1026689)
 * `1026688` [XenAPI multi-nic](https://bugs.launchpad.net/openstack-manuals/+bug/1026688)
 * `1026683` [Document XenAPI boot-from-volume support](https://bugs.launchpad.net/openstack-manuals/+bug/1026683)
 * `1026682` [Document image creation and upload for XenAPI](https://bugs.launchpad.net/openstack-manuals/+bug/1026682)
 * `1026674` [Hypervisor flag descriptions are often KVM specific, need to include XenAPI](https://bugs.launchpad.net/openstack-manuals/+bug/1026674)
 * `1026671` [Expand "Post-Install Configuration" to include XenAPI](https://bugs.launchpad.net/openstack-manuals/+bug/1026671)
 * `1023417` [Need better example configuration for XenServer](https://bugs.launchpad.net/openstack-manuals/+bug/1023417)
 * `1022554` [Need docs for Xen in VLAN mode, not multi-host](https://bugs.launchpad.net/openstack-manuals/+bug/1022554)
 * `1021224` [XenServer install docs should not rely on DevStack](https://bugs.launchpad.net/openstack-manuals/+bug/1021224)

## storage/disk

 * `929062` [/images filling up on xenserver host](https://bugs.launchpad.net/openstack-manuals/+bug/929062)

