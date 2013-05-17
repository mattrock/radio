import sys, os
#prev_sys_path = list(sys.path)

#import site 
#site.addsitedir('/usr/local/tgenv/rock/lib/python2.7/site-packages')

#new_sys_path = []
#for item in list(sys.path):
#    if item not in prev_sys_path:
#        new_sys_path.append(item)
#        sys.path.remove(item)
#sys.path[:0] = new_sys_path 

#sys.path.append('/usr/local/tgenv/rock/lib/python2.7/site-packages')

os.environ['PYTHON_EGG_CACHE'] = '/usr/local/tgenv/rock/radio/python-eggs'

from paste.deploy import loadapp
application = loadapp('config:/usr/local/tgenv/rock/radio/production.ini')

