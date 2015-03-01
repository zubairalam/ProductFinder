class bootstrap {
	# scope variables
	$packages = ["curl", "g++", "git", "make", "wget"]

	# useful for pillow and xml support		
	$libs = ["libjpeg8-dev", "libtiff4-dev", "zlib1g-dev", "libfreetype6-dev",
			 "liblcms2-dev", "libwebp-dev", "tcl8.5-dev", "tk8.5-dev",
			 "libffi-dev", "libxml2-dev", "libxslt1-dev"
	]

	# let's rock!
	package { $packages: }
	package { $libs:
      require => Package[$packages]
    }
}