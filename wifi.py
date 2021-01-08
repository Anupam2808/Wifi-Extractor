import os
i=input ("Enter The Drive . Please Type In Capital ")
if i== "H":
    os.system('cmd /c "netsh wlan export profile folder = H: key=clear"')
if i== "G":
    os.system('cmd /c "netsh wlan export profile folder = G: key=clear"')
if i == "F":
    os.system('cmd /c "netsh wlan export profile folder = F: key=clear"')
if i == "E":
    os.system('cmd /c "netsh wlan export profile folder = E: key=clear"')
    
