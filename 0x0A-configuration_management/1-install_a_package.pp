#!/usr/bin/puppet

# Update pip3
exec { 'update_pip':
  command     => 'pip3 install --upgrade pip',
  path        => ['/usr/local/bin', '/usr/bin'],
  refreshonly => true,
}

# Install Flask version 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Exec['update_pip'],
}

# Notify that the catalog has been applied
notify { 'Catalog_applied':
  message => 'Applied catalog for installing Flask 2.1.0',
}

