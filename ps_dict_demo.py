from collections import OrderedDict

print '\n\n'
print '1 -------------  print dict  ----------------------'

info = {
    'host' : 'ws1',
    'domain' : 'rootcap.in',
    'desc' : 'web server',
    'apps' : 'apache httpd',
    'version' : 2.2,

}

print info


print '\n\n'
print '2 ---------  add and delete  --------------------------'
info = {
    'host' : 'ws1',
    'domain' : 'rootcap.in',
    'desc' : 'web server',
    'apps' : 'apache httpd',
    'version' : 2.2,

}

item = 'version'
if item in info:
    info[item] = 3.6   # update dict

info['arch'] = 'x86_64' # add an element in dict

value = info.pop('desc') # delete an element in dict
print value
print

del info['domain'], info['version'] # alternate way to delete


print info



print '\n\n'
print '3 -------------  Dict lookup  ----------------------'


info = {
    'host' : 'ws1',
    'domain' : 'rootcap.in',
    'desc' : 'web server',
    'apps' : 'apache httpd',
    'version' : 2.2,

}

print info['host']
print info['desc']
print info['apps']
#print info['app']  # this will throw an exception as 'app' is not found
print info.get('apps')
print info.get('app')  # graceful way for key not found
print info.get('app', 'default-key') # you can set the default value



print '\n\n'
print '4 -------------  Dict iterate  ----------------------'

info = {
    'host' : 'ws1',
    'domain' : 'rootcap.in',
    'desc' : 'web server',
    'apps' : 'apache httpd',
    'version' : 2.2,

}

for i in info:
    print i, '->' , info[i]


print

for k, v in info.items():   # better way than the above
    print k, ':' , v



print '\n\n'
print '5 -------------  print keys, values and items  ----------------------'

info = {
    'host' : 'ws1',
    'domain' : 'rootcap.in',
    'desc' : 'web server',
    'apps' : 'apache httpd',
    'version' : 2.2,

}

print info.keys()
print
print info.values()
print
print info.items()



print '\n\n'
print '5 -------------  ordered dictionary  ----------------------'

od = OrderedDict()
od['lang'] = 'perl'
od['author'] = 'wall'
od['release'] = 'green parrot'

for k, v in od.items():
    print k, ':', v