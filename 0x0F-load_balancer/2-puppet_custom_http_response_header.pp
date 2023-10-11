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
}

file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
}

file { '/var/www/error/error_40x.html':
    ensure  => file,
    content => 'Ceci n\'est pas une page',
}

$hostname = $::hostname

$nginx_config = "
server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html index.htm;

    location / {
        add_header X-Served-By ${hostname};
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /error_40x.html;
    location = /error_40x.html {
        root /var/www/error;
        internal;
    }
}"

file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => $nginx_config,
}

service { 'nginx':
    ensure    => 'running',
    enable    => true,
    require   => Package['nginx'],
    subscribe => File['/etc/nginx/sites-available/default'],
}
