import time
import _thread as thread
def loap1():
    print('Start  loop 1 at:',time.ctime())
    time.sleep(4)
    print('End loop 1 at:',time.ctime())

def loap2():
    print('Start  loop 2 at:',time.ctime())
    time.sleep(2)
    print('End loop 2 at:',time.ctime())

def main():
    print('Starting at',time.ctime())
    thread.start_new_thread(loap1, ())

    thread.start_new_thread(loap2, ())
    print('all done at',time.ctime())
if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
