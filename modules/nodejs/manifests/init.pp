class nodejs {
    # scope variables
    $packages = ["nodejs"]
    $npm_packages = ["stylus", "yuglify", "coffee-script"]

    exec {"add-nodejs-repo":
      command => "sudo add-apt-repository -y ppa:chris-lea/node.js",
      require => Class["python"],
    }

    # fix for running update again!
    exec { "update-2":
      command => "sudo apt-get update",
      require => Exec["add-nodejs-repo"],
    }

    package { $packages:
      require => Exec["update-2"],
    }

    define install_npm_packages {
          exec { "installing node package $name":
                command => "sudo npm install -g $name",
                require => Package[$nodejs::packages],
          }
    }
    install_npm_packages { $npm_packages: }
}