#  install and configure an Nginx server using Puppet instead of Bash.

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

$nginx_file = "
server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
"

file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => $nginx_file,
}

exec { 'execute-command':
    command => '/usr/sbin/service nginx restart',
}
