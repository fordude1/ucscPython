'''
Simple program that uses the subprocess module
to see if a website is available
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