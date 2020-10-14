# user limit hotfix
exec {'fix-userlimit':
  path    => '/bin/',
  command => 'sed -i s/holberton/foo/ /etc/security/limits.conf',
}
