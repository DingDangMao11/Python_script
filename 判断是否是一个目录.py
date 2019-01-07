import os

dir = "/var/www/html/"
if os.path.isdir(dir):
      print(' %s is a dir' % dir)
else:
      print(' %s not is a dir' % dir)
