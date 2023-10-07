Vagrant.configure("2") do |config|
  # Define the web server and load balancer boxes
  config.vm.define "65087-web-01" do |web1|
    web1.vm.box = "ubuntu/focal64"
    web1.vm.hostname = "65087-web-01"
    web1.vm.network "private_network", type: "static", ip: "192.168.56.11"
  end

  config.vm.define "65087-web-02" do |web2|
    web2.vm.box = "ubuntu/focal64"
    web2.vm.hostname = "65087-web-02"
    web2.vm.network "private_network", type: "static", ip: "192.168.56.12"
  end

  config.vm.define "65087-lb-01" do |lb|
    lb.vm.box = "ubuntu/focal64"
    lb.vm.hostname = "65087-lb-01"
    lb.vm.network "private_network", type: "static", ip: "192.168.56.13"
  end
end

