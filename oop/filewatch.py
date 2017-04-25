import sys
import os
import argparse
import time


class FileWatcher:
    def __init__(self, path_of_file_to_watch):
        self.path = path_of_file_to_watch
        self.subscribers = set()

    def watch(self):
        self.file_size_stored = os.stat(args.file).st_size
        print(f'''Monitoring "{args.file}" file.
            Original files size is {self.file_size_stored} bytes''')
        while True:
            try:
                time.sleep(1)
                self.check_file()
            except KeyboardInterrupt:
                print('\nDone')
                break
            except:
                print(f'Unhandled error: {sys.exc_info()[0]}')

    def check_file(self):
        file_size_current = os.stat(args.file).st_size
        if file_size_current != self.file_size_stored:
            self.dispatch(file_size_current)
            self.file_size_stored = file_size_current

    def register(self, who):
        self.subscribers.add(who)

    def dispatch(self, file_size):
        for subscriber in self.subscribers:
            subscriber.update(file_size)

    def unregister(self, who):
        self.subscribers.discard(who)


class FileObserver:
    def __init__(self, name):
        self.name = name

    def update(self, file_size):
        print(f'{self.name} noticed that the file is now {file_size} bytes')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file',
                        help='file path to be monitored')
    args = parser.parse_args()

    pub = FileWatcher(args.file)

    bob = FileObserver('Bob')
    stacy = FileObserver('Stacy')
    john = FileObserver('John')

    pub.register(bob)
    pub.register(stacy)
    pub.register(john)

    pub.watch()
