# coding: utf8

from logbook import Logger, StreamHandler, FileHandler
import sys

StreamHandler(sys.stdout).push_application()
FileHandler('app.log').push_application()  # 会覆盖上一个Handler

# log = Logger('Logbook')
# log.info('Hello, World!')
# log.error('it is err')

def print_all(text):
    print(text)



if __name__ == '__main__':
    print('Let us play  python')