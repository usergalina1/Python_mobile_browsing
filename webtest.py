import subprocess
from time import sleep


def executeadbcommand(adb_command):
    subprocess.Popen(adb_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
    sleep(1)


def gotowebsite(website):
    adb_command = 'adb shell am start -n com.android.chrome/com.google.android.apps.chrome.Main -d ' + website
    executeadbcommand(adb_command)
    print(website)
    # time spent on web page
    sleep(30)


def generatewebusage(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    count = 0
    for website in lines:
        count += 1
        gotowebsite(website)
        if (count % 10 == 0):
            closeopentabs()


def closeopentabs():
    # Pixel 3a/12 device
    executeadbcommand('adb shell input tap 905 165')  # tab button
    executeadbcommand('adb shell input tap 1020 170')  # more options
    executeadbcommand('adb shell input tap 720 425')  # close all tabs text


def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts


if __name__ == '__main__':

    from sys import argv

    myargs = getopts(argv)
    if '-f' in myargs:
        print("Proccessing " + myargs['-f'] + "\n")
        filename = myargs['-f']
        generatewebusage(filename)
        closeopentabs()

# how to call from command prompt
# python webtest.py -f websites.txt
