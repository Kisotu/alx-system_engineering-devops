# a script that installs nginx using puppet

package {'nginx':
     ensure => present,
}

file {'/var/www/html/index.nginx-debian.html':
     content => 'Hello World!',
}

file_line {'configure redirection':
     path  => 'etc/nginx/sites-available/default',
     after =>  'server_name _;',
     line  =>  "\n\tlocation /redirect_me {\n\t\treturn 301 https://youtu.be/dQw4w9WgXcQ;\n\t}\n",
}

exec {'run':
     command  => 'sudo service nginx restart',
     provider => shell,
}
