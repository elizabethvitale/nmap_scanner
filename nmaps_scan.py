import os
import subprocess
from xml.dom import minidom

dir = os.getcwd()
dir = dir + '/scan.xml'
ip_addresses = ["192.168.0.1"]
def searchData():
    scanned = minidom.parse(dir)
    openedports = scanned.getElementsByTagName('port')
    
    print('Open Ports for TCP')
    for port in openedports:
        process = ''
        state = ''
        data = port.childNodes
        for objects in data:
            try:
                process = objects.attributes['name'].value
            except:
                state = objects.attributes['state'].value    
        if((process == 'unknown') or (process == '')):
            process = 'Service origin is unknown!'
        print('PORT', f'{port.attributes["portid"].value:6}', 'STATE:', f'{state:10}', 'SERVICE:', process)

for address in ip_addresses:        
#subprocess.call(['nmap','-p-', '-oX',dir, '192.168.0.1'])
    cmd = "nmap -p- -oX " + dir + " " + address + "  > text.txt"
    os.system(cmd) #using system so the inital nmap call does not show 
    searchData()
    os.system("rm -rf text.txt")
