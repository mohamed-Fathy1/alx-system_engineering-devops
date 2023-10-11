#  install and configure an Nginx server using Puppet instead of Bash.

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/error/error_40x.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}

$hostname = $facts['networking']['hostname']

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

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
