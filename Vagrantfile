# -*- mode: ruby -*-
# vi: set ft=ruby :

fileToDisk = './tmp/large_disk.vdi'

Vagrant.configure("2") do |config|
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "addle/windows-server-2012-r2"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder ".", "C:\/Users\/vagrant\/Workplace\/rpa-draw"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = true

    # Customize the amount of memory on the VM:
    vb.memory = "1024"
    unless File.exist?(fileToDisk)
       vb.customize ['createhd', '--filename', fileToDisk, '--variant', 'Fixed', '--size', 1 * 1024]
    end
    vb.customize ['storageattach', :id,  '--storagectl', 'SATA', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', fileToDisk]
  end
end
