import subprocess
import time
import os
BLUE = '34m'
message = 'WARNING THIS PROGRAM MUST BE USED WITH SUDO OTHER WISE MAC ADDRESS WONT CHANGE!!!!!!!!'


def display_colored_text(color, text):
    colored_text = f"\033[{color}{text}\033[00m"
    return colored_text
print(display_colored_text(BLUE, message))

Interface = input('[+] Which interface do you want to change: ')
mac = input('[+] What would you like your new mac address to be? PS: Make sure it has 12 digits every two digits must have a ":" in between: ')
subprocess.call('ifconfig '+str(Interface)+' down',shell=True)
subprocess.call('ifconfig '+str(Interface)+' hw ether '+str(mac)+'' ,shell=True)
subprocess.call('ifconfig '+str(Interface)+' up',shell=True)
print('[+] \033[5;37;40m Your MAC Address is being changed WARNING:If you changed your wireless adapters mac address your wifi will be turned off but will be brought back in 5 to 6 seconds so dont be alarmed it is normal \033[0;37;40m\n')
time.sleep(6)
os.system('clear')
print('[+] \033[5;37;40m YOUR MAC ADDRESS HAS SUCCESSFULLY CHANGED TAKE A LOOK \033[0;37;40m\n')
subprocess.call('ifconfig '+str(Interface)+'', shell=True)

