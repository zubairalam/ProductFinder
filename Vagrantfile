VAGRANTFILE_API_VERSION = "2"
HOST_NAME = "productfinder"
CPU_EXEC_CAP = "75" 
MEMORY = "512"
TIMEOUT = 300

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.boot_timeout = TIMEOUT
  config.vm.hostname = HOST_NAME
  config.vm.graceful_halt_timeout = TIMEOUT  
  config.vm.network :private_network, ip: "10.7.7.7"
  config.vm.network "forwarded_port", guest:80, host:8080, auto_correct:true   # nginx
  config.vm.network "forwarded_port", guest:8000, host:8000, auto_correct:true # django
  config.vm.network "forwarded_port", guest:3000, host:3000, auto_correct:true # node
  config.vm.network "forwarded_port", guest:5432, host:5432, auto_correct:true # postgres
  config.vm.network "forwarded_port", guest:6379, host:6379, auto_correct:true # redis
  config.vm.network "forwarded_port", guest:9200, host:9200, auto_correct:true # elasticsearch

  config.vm.provider "virtualbox" do |v|
    v.name = HOST_NAME
    v.customize ["modifyvm", :id, "--memory", MEMORY]
    v.customize ["modifyvm", :id, "--cpuexecutioncap", CPU_EXEC_CAP]
    v.gui = false
  end

  config.vm.provision :puppet do |p|
  	p.manifests_path ="manifests"
  	p.manifest_file = "site.pp"
  	p.module_path = "modules"
  end

end
