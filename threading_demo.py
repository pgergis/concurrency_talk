import random
from threading import Thread
import time

GLOBAL_MESSAGES = ["Hello from thread #", "Ahlan wa sahlan from thread #", "Salut from thread #", "Wazzaaap from thread #"]

def print_message(msg):
    print(msg)

def concurrent_sleep(identifier):
    message = GLOBAL_MESSAGES.pop()
    for _ in range(10):
        sleep_time = random.randint(0,4)
        print_message(message + f'{identifier}')
        time.sleep(sleep_time)

def main_threaded():
    for n in range(4):
        t = Thread(target=concurrent_socket_talk, args=(n,))
        t.start()

if __name__ == '__main__':
    main_threaded()
