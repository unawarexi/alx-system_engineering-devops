# increase nginx limit
exec { 'increase-limit':
  command => 'sed -i "s/15/8192/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'grep -q "15" /etc/default/nginx',
}

# restart nginx
exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin',
  require => Exec['increase-limit'],
}
