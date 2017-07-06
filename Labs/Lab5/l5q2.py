'''
import the subprocess module and use the check_output function.
Determine if google.com is up and can be reached by your computer.
To do this from the commandline you would type the command:  ping –c 5 www.google.com.
Option is –n in Windows.
Write a small Python program that will take from the user the web url they
would like to ping and issue the correct command to determine if that website is reachable by your computer.
The output should look something like the following if your computers network is configured correctly
and if the website is up and running:
PING www.google.com (74.125.239.17): 56 data bytes
64 bytes from 74.125.239.17: icmp_seq=0 ttl=54 time=24.563 ms
64 bytes from 74.125.239.17: icmp_seq=1 ttl=54 time=24.082 ms
64 bytes from 74.125.239.17: icmp_seq=2 ttl=54 time=31.718 ms
64 bytes from 74.125.239.17: icmp_seq=3 ttl=54 time=24.468 ms
64 bytes from 74.125.239.17: icmp_seq=4 ttl=54 time=24.451 ms

'''

# Import the module
import subprocess

# here is the command I tested: subprocess.check_output(["ping", "-c 5", "www.google.com"])

def ProcessWebsite():
    '''
    The ProcessWebsite Function uses the subprocess.check_output argument
    To see if a website is up.
    '''
    website = raw_input('Please type the website you would like to check.\n')
    return website

def PingWebsite(webinput):
    '''
    Check to See if the website is up and responds to ping 
    '''
    weboutput =  subprocess.check_output(["ping", "-c 5", webinput])
    return weboutput

def run():
    '''
    Start the program 
    '''
    web_check = ProcessWebsite()
    print PingWebsite(web_check)

run()