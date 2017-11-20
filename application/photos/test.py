import psutil
import os

#pid = os.system("ps -ef|grep appName|grep -v grep|awk '{print $2}'")
pid = os.popen("ps -ef|grep appName|grep -v grep|awk '{print $2}'").readlines()
print pid
