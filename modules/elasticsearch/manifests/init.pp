
class elasticsearch {
	# scope variables
    $packages = ["openjdk-7-jre-headless"]
	$version = "elasticsearch-1.0.1.deb"
	$url = "https://download.elasticsearch.org/elasticsearch/elasticsearch/$version"

	# let's rock!
	package { $packages:
      require => Class["bootstrap"],
    }

	exec { "download-$version":
		command => "wget $url",
		require => Package[$packages],
	}

	exec { "install-$version":
		command => "sudo dpkg -i $version && rm -rf $version",
		require => Exec["download-$version"],
	}
}

