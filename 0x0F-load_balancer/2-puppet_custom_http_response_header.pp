#  install and configure an Nginx server using Puppet instead of Bash.

exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => '/usr/bin/test -e /var/lib/apt/periodic/update-success-stamp',
}

package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

exec { '/usr/sbin/ufw allow \'Nginx HTTP\'':
  path    => '/usr/sbin',
  unless  => '/usr/sbin/ufw status | grep "Nginx HTTP" | grep "ALLOW"',
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/error/error_40x.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}

exec { 'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart Nginx'],
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => Package['nginx'],
  subscribe => File['/etc/nginx/sites-available/default'],
}
