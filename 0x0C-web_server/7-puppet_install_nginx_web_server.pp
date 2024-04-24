# a script that installs nginx using puppet

exec { 'update':
    command  =>  '/usr/bin/apt-get update',
}
package { 'nginx':
    ensure  => installed,
}

file_line { 'def':
    ensure =>  'present',
    path   =>  '/etc/nginx/sites-available/default',
    after  =>  'listen 80 default_server;',
    line   =>  'rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcx permanent;',
}

file { '/var/www/html/index.html':
    content  =>  'Hello World!',
}

service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}
