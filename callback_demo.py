import random
import time

GLOBAL_MESSAGES = ["Hello from thread #", "Ahlan wa sahlan from thread #", "Salut from thread #", "Wazzaaap from thread #"]

# global containers used by event loop
waiting_to_sleep = [] # time, callback, argument tuple

def event_loop():
    while waiting_to_sleep:
        waiting_to_sleep.sort(key=lambda t: t[0])
        due_time, callback, args = waiting_to_sleep[0]
        if due_time < time.process_time():
            waiting_to_sleep.pop(0)
            callback(*args)

def upon_sleep(duration, callback, args):
    now = time.process_time()
    due = now + duration
    waiting_to_sleep.append((due, callback, args))

def print_message(msg):
    print(msg)

def concurrent_sleep(identifier):
    message = GLOBAL_MESSAGES.pop()
    def write(n):
        if n < 10:
            sleep_time = random.randint(0,4)
            print_message(message + f'{identifier}')
            upon_sleep(sleep_time, write, (n+1,))
    write(0)

def main_callback():
    for n in range(4):
        upon_sleep(0, concurrent_sleep, (n,))
    event_loop()

if __name__ == '__main__':
    main_callback()
