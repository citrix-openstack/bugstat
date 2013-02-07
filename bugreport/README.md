# nova

Fixed/Pending ratio: 1 / 11

## new

 * [libvirt should enable pae setting for Xen or KVM guest](https://bugs.launchpad.net/nova/+bug/1100697)
 * [nova command of host-descrbe should display vg disk size in xen hypervisor when libvirt_images_type is lvm](https://bugs.launchpad.net/nova/+bug/1098116)
 * [Xen migration driver should use execvp](https://bugs.launchpad.net/nova/+bug/1074087)
 * [Raw disk key error 'root'](https://bugs.launchpad.net/nova/+bug/1052085)
 * [Need more efficient implementation of get_num_instances() and instance_exists() in Xen and VMWare virt drivers](https://bugs.launchpad.net/nova/+bug/934279)
 * [Boot from ISO is different in XS/KVM](https://bugs.launchpad.net/nova/+bug/914484)
 * [Xen instances:support for randomly-named and uncompressed images](https://bugs.launchpad.net/nova/+bug/912684)
 * [New xapi backend for Local Storage ISO SR](https://bugs.launchpad.net/nova/+bug/903445)
 * [dom0 management traffic is not allowed to flow across a VLAN](https://bugs.launchpad.net/nova/+bug/902663)

## storage/disk

 * [maybe a xenserver bug][Detaching a volume from a XenAPI instance fails if XenAPI thinks it is in use](https://bugs.launchpad.net/nova/+bug/1030108)

## fixed

 * [[xen] create/update metadata during boot can put instance into ERROR](https://bugs.launchpad.net/nova/+bug/1100866)

# cinder

No bugs found

# quantum

Fixed/Pending ratio: 0 / 2

## new

 * [ovs_quantum_plugin incompatibility with python 2.4](https://bugs.launchpad.net/quantum/+bug/994831)
 * [ovs_quantum_agent.py crashes on Citrix XCP because of old python version (2.4)](https://bugs.launchpad.net/quantum/+bug/994774)

# glance

Fixed/Pending ratio: 0 / 1

## new

 * [windows image upload on xen host results in sr scan failure](https://bugs.launchpad.net/glance/+bug/1055399)

