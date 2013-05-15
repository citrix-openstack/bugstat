# Summary

Fixed/Pending Ratio: 10 / 58

# nova  - `39`

Fixed/Pending ratio: 10 / 39

## new

 * `1178639` [xenapi spawn clean up vdi logic needs work](https://bugs.launchpad.net/nova/+bug/1178639)
 * `1178223` [xenapi:checking agent by default is confusing](https://bugs.launchpad.net/nova/+bug/1178223)
 * `1177993` [poll_rebooting_instances hits DB directly  in Xen/VMware virt drivers](https://bugs.launchpad.net/nova/+bug/1177993)
 * `1177005` [Xen driver not reporting progress in notifications](https://bugs.launchpad.net/nova/+bug/1177005)
 * `1175383` [Default 'tiny' instance_type has wrong root_gb](https://bugs.launchpad.net/nova/+bug/1175383)
 * `1169769` [start guests on host reboot](https://bugs.launchpad.net/nova/+bug/1169769)
 * `1162973` [XCP resource pool - unable to migrate instances](https://bugs.launchpad.net/nova/+bug/1162973)
 * `1161619` [Can't create nova aggregate on Xen](https://bugs.launchpad.net/nova/+bug/1161619)
 * `1161471` [xenapi:guest kernel not cleaned up](https://bugs.launchpad.net/nova/+bug/1161471)
 * `1155113` [xenapi:ImageTooLarge for instances with 0 disk size](https://bugs.launchpad.net/nova/+bug/1155113)
 * `1155066` [xenapi:resize to size too small for disk fails badly](https://bugs.launchpad.net/nova/+bug/1155066)
 * `1152401` [xenapi:Detecting bad-volumes relies on 120 sec timeout](https://bugs.launchpad.net/nova/+bug/1152401)
 * `1152268` [XenAPI:Resize tempest test is failing (shrink problem)](https://bugs.launchpad.net/nova/+bug/1152268)

## fixed

 * `1170237` [cannot reboot instances when in rescue mode](https://bugs.launchpad.net/nova/+bug/1170237)
 * `1167515` [xenapi:_connect_volume exception handler not eventlet safe](https://bugs.launchpad.net/nova/+bug/1167515)
 * `1162029` [xenapi:nova_instance_uuid not set for root image](https://bugs.launchpad.net/nova/+bug/1162029)
 * `1160323` [Cannot block migrate in xenapi with iSCSI cinder volumes attached](https://bugs.launchpad.net/nova/+bug/1160323)
 * `1158603` [xenapi's check_can_live_migrate_destination should not return None](https://bugs.launchpad.net/nova/+bug/1158603)
 * `1157695` [xenapi:RPM parted dependency](https://bugs.launchpad.net/nova/+bug/1157695)
 * `1157389` [xenapi:console for rescue vm is broken](https://bugs.launchpad.net/nova/+bug/1157389)
 * `1157211` [XenAPI depends on /sys/hypervisor/uuid - not readable across reboot](https://bugs.launchpad.net/nova/+bug/1157211)
 * `1154731` [xenserver boot from iso broken](https://bugs.launchpad.net/nova/+bug/1154731)
 * `1015423` [ping it][xenapi ImageTooLarge exception leaves VDI around](https://bugs.launchpad.net/nova/+bug/1015423)

## storage/disk

 * `1030108` [maybe a xenserver bug][Detaching a volume from a XenAPI instance fails if it is in use](https://bugs.launchpad.net/nova/+bug/1030108)
 * `914484` [Boot from ISO is different in XS/KVM](https://bugs.launchpad.net/nova/+bug/914484)
 * `912684` [Xen instances:support for randomly-named and uncompressed images](https://bugs.launchpad.net/nova/+bug/912684)

## metrics

 * `1015190` [is it valid?][arch_filter tracebacks with xenapi](https://bugs.launchpad.net/nova/+bug/1015190)
 * `954913` [xenapi host refresh not dealing with exceptions well when updating host stats](https://bugs.launchpad.net/nova/+bug/954913)

## migration

 * `1073306` [xenapi migrations don't apply security group filters](https://bugs.launchpad.net/nova/+bug/1073306)
 * `1073303` [xenapi finish_migration does not cleanup on failures](https://bugs.launchpad.net/nova/+bug/1073303)

## minor

 * `1074087` [XenApi migration driver should use execvp](https://bugs.launchpad.net/nova/+bug/1074087)
 * `1024944` [XenServer:If file system is directly is on root device, auto_disk_configure does not work](https://bugs.launchpad.net/nova/+bug/1024944)

## console

 * `1004175` [review][XenAPI text console support](https://bugs.launchpad.net/nova/+bug/1004175)

## instance spawn

 * `1061062` [Asynchronous errors can only be reported if instance is in ERROR](https://bugs.launchpad.net/nova/+bug/1061062)

## networking

 * `1043886` [Firewall rules are not updated if you restart nova-compute](https://bugs.launchpad.net/nova/+bug/1043886)

## pools

 * `1026552` [is it valid?][XenAPI pool based migration should error when not shared storage](https://bugs.launchpad.net/nova/+bug/1026552)

## stale

 * `747394` [XenServer port needs to clear out vm-data/networking before issuing resetnetwork command](https://bugs.launchpad.net/nova/+bug/747394)

## discussion

 * `816406` [Service stats needs to be unified across virt layer](https://bugs.launchpad.net/nova/+bug/816406)

## missing implementation

 * `1100697` [libvirt should enable pae setting for Xen or KVM guest](https://bugs.launchpad.net/nova/+bug/1100697)

# cinder  - `0`

No bugs found

# quantum  - `2`

Fixed/Pending ratio: 0 / 2

## new

 * `1005616` [Windows instances may not get correct port configuration as set by quantum](https://bugs.launchpad.net/quantum/+bug/1005616)
 * `994831` [ovs_quantum_plugin incompatibility with python 2.4](https://bugs.launchpad.net/quantum/+bug/994831)

# glance  - `1`

Fixed/Pending ratio: 0 / 1

## new

 * `1055399` [windows image upload on xen host results in sr scan failure](https://bugs.launchpad.net/glance/+bug/1055399)

# openstack-manuals  - `16`

Fixed/Pending ratio: 0 / 16

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

