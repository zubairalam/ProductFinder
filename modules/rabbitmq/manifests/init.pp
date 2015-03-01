class rabbitmq {
	# scope variables
    $packages = ["rabbitmq-server"]

	# let's rock!
	package { $packages:
      require => Class["bootstrap"],
    }
}

