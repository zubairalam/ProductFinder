ProductFinder
====================

:Authors:
   Zubair

:Version: 1.0

:Description:
    Find and Compare Products.

:License:
    Creative Commons (CC) License 3.0

****

Hardware Requirements
---------------------

- Your PC/laptop has a processor which is **64-bit capable (Intel Core 2 Duo+)**.
- Your PC/laptop has a minimum of **1GB RAM memory**.
- Your PC/laptop has broadband/internet access of at least **2Mbps+**.

Software Requirements
---------------------

- Your PC/laptop has a copy of **Windows, Linux or Mac OSX** operating system installed.
- Install the latest version of git_.
- Install the latest version of virtualbox_.
- Install the latest `virtualbox extensions pack`_.
- Install the latest vagrant_.


Running the Project
-------------------

After successfully cloning the repository, launch "Terminal/Console" and run the following commands:

    1. **vagrant up**  (Approx. 5-20 minutes based on internet connectivity)
    2. **vagrant ssh** 


Inside the guest virtual machine:

    1. **workon project**      (Activates the Python Virtualenv for "project")
    2. **cd /vagrant/project** (Project folder)
    3. **./reload**            (Starts the Django Server)

The project is now running!

Viewing the Project
-------------------

On the host machine, open your favourite internet browser and navigate to:

    - **http://127.0.0.1:8000** or **http://localhost:8000**


Logging into Admin Mode
-----------------------

On the host machine, open your favourite internet browser and navigate to:

    - **http://127.0.0.1:8000/admin/** or **http://localhost:8000/admin/**
    - username: **vagrant**
    - password: **vagrant**


Commands Shortcuts for Project
------------------------------

The following command shortcutes are available:
    
    - **./run**     (runserver)
    - **./migrate** (migrate + runserver)    
    - **./reload**  (destroy data + syncdb + load fixtures + migrate + runserver)
    

Installing PIP Requirements
---------------------------

On the guest virtual machine, if you need to install 3rd party libraries/extensions:

    1. **workon project** (This activates the "project" virtualenv)
    2. **pip install <package>==<version>** (e.g pip install django==1.6.2)
    3. Add the <package>==<version> line in any suitable file found in the "project/requirements/" folder.


Vagrant Commands
----------------

Inside the **host** machine:

    - **vagrant up**      (starts the guest virtual machine)
    - **vagrant ssh**     (ssh login into the guest virtual machine environment)
    - **vagrant halt**    (shuts down the guest virtual machine)
    - **vagrant destroy** (deletes the guest virtual machine)
    - **vagrant reload**  (restarts the guest virtual machine)

    
Inside the **guest** virtual machine:

    - **exit**            (exits the guest machine terminal back into host machine)



.. _git: http://git-scm.com/
.. _rsync: http://rsync.samba.org/
.. _vagrant: http://www.vagrantup.com/downloads.html
.. _virtualbox: http://www.virtualbox.org/wiki/Downloads
.. _virtualbox extensions pack: http://www.virtualbox.org/wiki/Downloads
.. _PyCharm: http://www.jetbrains.com/pycharm/download/
