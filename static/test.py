import os
patha = '/opt/voyager/apps/myweb/static/uploadIMG/WOW'
for (dirpath,dirnames,filenames) in  os.walk(patha):
    for filename in filenames:
        print os.path.join(dirpath,filename)
