"""STOPWATCH. Disclaimer: gets problems in Windows, WinError 10093"""

import time
import sys
import select

class Stopwatch:
    def __init__(self):
        self.startTime = None
        self.elapsedTime = 0
        self.isRunning = False

    def startWatch(self):
        if not self.isRunning:
            self.startTime = time.time()
            self.isRunning = True
            print("\nThe stopwatch just started running ...!\n")
    
    def stopWatch(self):
        if self.isRunning:
            self.elapsedTime = time.time() - self.startTime
            self.isRunning = False
            print("\nThe stopwatch just stopped running. Please reset it, keep running it or exit.\n\n")

    def resetWatch(self):
        self.elapsedTime = 0
        self.isRunning = False
        print("\nNow the stopwatch just got resetted to zero.\n\n")

    def logWatchTime(self):
        totalTime = self.elapsedTime
        if self.isRunning:
            totalTime += time.time() - self.startTime
        print(f"Time: {totalTime:.2f} seconds")

watch = Stopwatch()

while True:
    command = input("\nPlease enter one of the following commands:\nStart\nStop\nReset\nQuit\n\n>")
    if command == "Start":
        watch.startWatch()
    elif command == "Stop":
        watch.stopWatch()
    elif command == "Reset":
        watch.resetWatch()
    elif command == "Quit":
        break
    else:
        print("\nThe command you typed down is invalid, please try again.\n\n")

    while watch.isRunning:
        #sys.stdin Monitors if the user is typing down in keyboard
        #select.select: accesses the systems standard inputs and outputs streams
        #first index: look for any pending keyboard action that will always return a tuple
        if sys.stdin in select.select([sys.stdin],[],[],0)[0]:
            break
        watch.logWatchTime()
        #sleep for 1 second
        time.sleep(1)

#uncomment and add the following commented block into the file "sys.py"
"""
if sys.platform == 'win32':
    # windows does not support select() for anything except sockets
    # https://docs.python.org/3.7/library/select.html
     output+= os.read(fd, block_size)
else:
    # this does NOT work on windows... and it may not work on other systems... in that case, put more things to use the original code above
    inputready,outputready,exceptready = select.select([fd],[],[])
    for i in inputready:
        if i == fd:
            output += os.read(fd, block_size)
"""
