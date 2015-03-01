class redis {
	# scope variables
    $packages = ["redis-server"]

	# let's rock!
	package { $packages:
      require => Class["bootstrap"],
    }
}

