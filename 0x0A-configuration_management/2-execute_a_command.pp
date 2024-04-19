# creates a manifest that kills a process

exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
