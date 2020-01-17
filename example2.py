import os
import subprocess
from xml.dom import minidom

dir = os.getcwd()
dir = dir + '/scan.xml'

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

        
subprocess.call(['nmap','-p-', '-oX', dir, '192.168.0.1'])
searchData()

