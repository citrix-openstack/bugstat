# Summary

Fixed/Pending Ratio: 3 / 65

# nova  - `50`

Fixed/Pending ratio: 2 / 50

## new

 * `1516765` [xenapi:volume_utils._parse_volume_info can leak connection password via StorageError](https://bugs.launchpad.net/nova/+bug/1516765)
 * `1516721` [XenAPI:Race condition in test_get_console_output_with_unlimited_size](https://bugs.launchpad.net/nova/+bug/1516721)
 * `1515672` [XenServer attach second Cinder volume failed](https://bugs.launchpad.net/nova/+bug/1515672)
 * `1512955` [Race condition in nova/neutron when booting instance with xen driver](https://bugs.launchpad.net/nova/+bug/1512955)
 * `1507424` [Hypervisor type of xen should be XenServer](https://bugs.launchpad.net/nova/+bug/1507424)
 * `1502929` [XenServer 6.5 fails to attach to Cinder volumes](https://bugs.launchpad.net/nova/+bug/1502929)
 * `1492034` [nova network FlatDHCP (kilo) on XenServer 6.5  ebtables rules](https://bugs.launchpad.net/nova/+bug/1492034)
 * `1490238` [Configdrive fails to properly display within Windows Guest (Xenapi)](https://bugs.launchpad.net/nova/+bug/1490238)
 * `1488753` [ephemeral and root device filesystems should be labeled](https://bugs.launchpad.net/nova/+bug/1488753)
 * `1482403` [bdm for swap created with no regard for previous](https://bugs.launchpad.net/nova/+bug/1482403)
 * `1481705` [xenapi:xen tools scripts needs to be tested](https://bugs.launchpad.net/nova/+bug/1481705)
 * `1481689` [xenapi:cached images should be cleaned up by time](https://bugs.launchpad.net/nova/+bug/1481689)
 * `1477684` [Instance recreate is not supported](https://bugs.launchpad.net/nova/+bug/1477684)
 * `1468762` [lxc hypervisor does not support PCI devices](https://bugs.launchpad.net/nova/+bug/1468762)
 * `1461642` [libvirt-xen:Race between nova and a Xen script for updating the iptables](https://bugs.launchpad.net/nova/+bug/1461642)
 * `1450465` [vif name too long when libvirt driver trying to create XEN HVM domain](https://bugs.launchpad.net/nova/+bug/1450465)
 * `1445443` [volume access I/O error with libvirt-xen and iscsi](https://bugs.launchpad.net/nova/+bug/1445443)
 * `1443898` [TestVolumeBootPattern.test_volume_boot_pattern fail with libvirt-xen](https://bugs.launchpad.net/nova/+bug/1443898)
 * `1422342` [xenapi:soft reboot should attempt hard reboot on failure](https://bugs.launchpad.net/nova/+bug/1422342)
 * `1414529` [eval being used in session.py](https://bugs.launchpad.net/nova/+bug/1414529)
 * `1413475` [cannot get aggregate metadata information when nova-compute starts using xen](https://bugs.launchpad.net/nova/+bug/1413475)
 * `1383899` [xenapi auto disk config uses wrong size value when booting from volume](https://bugs.launchpad.net/nova/+bug/1383899)
 * `1374001` [Xenserver glance plugin uses unsafe SSL connection](https://bugs.launchpad.net/nova/+bug/1374001)
 * `1368073` [[Security-NIST]SimpleDH in nova/virt/xenapi/agent.py does not fit the NIST](https://bugs.launchpad.net/nova/+bug/1368073)
 * `1326156` [VHD image overhead (xenserver) not large enough](https://bugs.launchpad.net/nova/+bug/1326156)
 * `1323722` [libvirt Xen have to use "file" disk driver in the case of compute node doesn't support blktap.](https://bugs.launchpad.net/nova/+bug/1323722)
 * `1318544` [XenServer - Nova-Compute StorageError Waiting for device](https://bugs.launchpad.net/nova/+bug/1318544)
 * `1309580` [xenserver driver raises NotImplementedError for reset_network](https://bugs.launchpad.net/nova/+bug/1309580)
 * `1302831` [hacking/flake8 skips most xenapi plugins](https://bugs.launchpad.net/nova/+bug/1302831)
 * `1294587` [Old style Images with vhd files tarred along with a folder are not handled in nova xen plugin](https://bugs.launchpad.net/nova/+bug/1294587)
 * `1290455` [libvirt inject_data assumes instance with kernel_id doesn't contain a partition table](https://bugs.launchpad.net/nova/+bug/1290455)
 * `1275875` [Virt drivers should use standard image properties](https://bugs.launchpad.net/nova/+bug/1275875)
 * `1253571` [libivrt+xen does not support copy on write images](https://bugs.launchpad.net/nova/+bug/1253571)
 * `1245560` [vcpu_weight in flavor-create API is not validated](https://bugs.launchpad.net/nova/+bug/1245560)
 * `1224587` [xenapi:secgroups are not in place for a short duration after live-migration](https://bugs.launchpad.net/nova/+bug/1224587)
 * `1223396` [Rescue does not provide access to ephemeral disk](https://bugs.launchpad.net/nova/+bug/1223396)
 * `1220621` [xenapi:network bridge not created on hypervisor](https://bugs.launchpad.net/nova/+bug/1220621)
 * `1218528` [openvswitch-nova in XenServer doesn't work with bonding](https://bugs.launchpad.net/nova/+bug/1218528)
 * `1215928` [xenapi:image size calculation ignores container_format](https://bugs.launchpad.net/nova/+bug/1215928)
 * `1204165` [xenapi:vm_utils.ensure_free_mem does not take into account overheads](https://bugs.launchpad.net/nova/+bug/1204165)
 * `1201863` [XenAPI Resize Fails with Migration Error:Failed to transfer vhd to new host](https://bugs.launchpad.net/nova/+bug/1201863)
 * `1187330` [nova-compute does not respect reserved memory for dom0 when using libvirt/XEN](https://bugs.launchpad.net/nova/+bug/1187330)
 * `1177005` [XenAPI driver not reporting progress in notifications](https://bugs.launchpad.net/nova/+bug/1177005)
 * `1169769` [start guests on host reboot](https://bugs.launchpad.net/nova/+bug/1169769)
 * `1161471` [xenapi:guest kernel not cleaned up](https://bugs.launchpad.net/nova/+bug/1161471)

## fixed

 * `1503423` [Build failures:device_id assigned as int instead of expected string](https://bugs.launchpad.net/nova/+bug/1503423)
 * `1481693` [xenapi:xentool - cache destroy script is broken](https://bugs.launchpad.net/nova/+bug/1481693)

## storage/disk

 * `912684` [XenAPI instances:support for randomly-named and uncompressed images](https://bugs.launchpad.net/nova/+bug/912684)

## pools

 * `1026552` [is it valid?][XenAPI pool based migration should error when not shared storage](https://bugs.launchpad.net/nova/+bug/1026552)

## discussion

 * `816406` [Service stats needs to be unified across virt layer](https://bugs.launchpad.net/nova/+bug/816406)

# cinder  - `1`

Fixed/Pending ratio: 0 / 1

## new

 * `1480968` [Instance freezes after attaching a cinder volume on XenServer 6.5](https://bugs.launchpad.net/cinder/+bug/1480968)

# quantum  - `8`

Fixed/Pending ratio: 0 / 8

## new

 * `1495423` [Cannot get dom0's ovsdb monitor result](https://bugs.launchpad.net/neutron/+bug/1495423)
 * `1493662` [Xen ovs-agent-plugin polling manager is reported as not active](https://bugs.launchpad.net/neutron/+bug/1493662)
 * `1362301` [neutron.plugins.openvswitch.agent.ovs_neutron_agent fails to configure bridges](https://bugs.launchpad.net/neutron/+bug/1362301)
 * `1328524` [to determine ovs version are not using rootwrap](https://bugs.launchpad.net/neutron/+bug/1328524)
 * `1269805` [XenServer 6.2 OVS problem](https://bugs.launchpad.net/neutron/+bug/1269805)
 * `1268955` [OVS agent updates the wrong port when using Xen + Neutron with HVM or PVHVM](https://bugs.launchpad.net/neutron/+bug/1268955)
 * `1264505` [XenServer:OVS agent fail to start on slave host](https://bugs.launchpad.net/neutron/+bug/1264505)
 * `1245809` [Security groups cannot be used with XenAPI + OVS plugin](https://bugs.launchpad.net/neutron/+bug/1245809)

# glance  - `1`

Fixed/Pending ratio: 0 / 1

## new

 * `1412394` [schema-image.json should contain the hypervisor specific parameters](https://bugs.launchpad.net/glance/+bug/1412394)

# openstack-manuals  - `5`

Fixed/Pending ratio: 1 / 5

## new

 * `1403100` [XenAPI:Re-document boot from ISO](https://bugs.launchpad.net/openstack-manuals/+bug/1403100)
 * `1363437` [xenapi:Attach original local disks during rescue](https://bugs.launchpad.net/openstack-manuals/+bug/1363437)
 * `1254969` [xenapi:move session into new client module](https://bugs.launchpad.net/openstack-manuals/+bug/1254969)
 * `1212687` [xenapi:through-dev raw-tgz image upload to glance](https://bugs.launchpad.net/openstack-manuals/+bug/1212687)

## fixed

 * `1492118` [OVS-agent:Introduce Ryu based OpenFlow implementation](https://bugs.launchpad.net/openstack-manuals/+bug/1492118)

