#!/usr/bin/puppet

# Using Puppet to install Flask from pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Exec['update_pip'], # Ensure that pip is up-to-date before installing
}

# Exec resource to update pip3
exec { 'update_pip':
  command     => 'pip3 install --upgrade pip',
  path        => ['/usr/local/bin', '/usr/bin'],
  refreshonly => true,
}

