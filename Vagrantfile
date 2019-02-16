# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    $num_nodes = 1
    (1..$num_nodes).each do |i|
        config.vm.define "test-node#{i}" do |node|
            node.vm.box = "qzchenwl/centos"
            node.vm.synced_folder ".", "/vagrant", type: "virtualbox"
            node.vm.hostname = "test-node#{i}"
            ip = "10.0.3.#{i+100}"
            node.vm.network "private_network", ip: ip
            node.vm.provider "virtualbox" do |vb|
                vb.memory = "8192"
                vb.cpus = 2
                vb.name = "test-node#{i}"
            end

            node.vm.provision "shell", path: "scripts/bootstrap.sh", args: [ip]
        end
    end
end
