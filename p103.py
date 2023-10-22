import sys
import time
import random
import os
import shutil
from watchdog.observers import FileSystemEventHandler
from watchdog.events import Observer

source='Users/agam/Downloads'

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print('already created')
    def on_deleted(self, event):
        print('already deleted')
    def on_modified(self, event):
        print('already changed')
    def on_moved(self, event):
        print('moved elsewhere or renamed')

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, source, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print('stopped')
    observer.stop()