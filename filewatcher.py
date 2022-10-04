import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class Handler(FileSystemEventHandler):
    def on_created(self,dir_location):      #overriding the on_created() method to our needs
        print("file created")               #action pending

dir_location = 'test_dir'  #customisable
observer = Observer()
event_handler = Handler()
observer.schedule(event_handler,dir_location,recursive = True)      #recursively observing the directory for changes
observer.start()

try:
    while(True):
        time.sleep(10)      #maintaining a 10 second gap between observations
except KeyboardInterrupt:
    observer.stop()         #to manually stop the observer

observer.join()