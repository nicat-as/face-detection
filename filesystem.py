import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from clientftp import uploadFile

class MyHandler(FileSystemEventHandler):
    def on_created (self, event):
        print(event.src_path)
        time.sleep(2)
        uploadFile(event.src_path)


if __name__ == '__main__':
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path = 'output/', recursive = False)
    observer.start()
    
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    
        