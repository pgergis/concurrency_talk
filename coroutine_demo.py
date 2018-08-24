import time
import random

GLOBAL_MESSAGES = ["Hello from thread #", "Ahlan wa sahlan from thread #", "Salut from thread #", "Wazzaaap from thread #"]

# global containers used by event loop
waiting_to_sleep = []

def event_loop():
    while waiting_to_sleep:
        waiting_to_sleep.sort(key=lambda t: t[0])
        due_time, coroutine = waiting_to_sleep[0]
        if due_time < time.process_time():
            waiting_to_sleep.pop(0)
            try:
                reason, data = next(coroutine)
                if reason == 'sleep':
                    next_time = time.process_time() + data
                    waiting_to_sleep.append((next_time, coroutine))
            except StopIteration:
                pass

def print_message(msg):
    print(msg)

def concurrent_sleep(identifier):
    message = GLOBAL_MESSAGES.pop()
    for _ in range(0, 10):
        sleep_time = random.randint(0,4)
        print_message(message + f'{identifier}')
        yield 'sleep', sleep_time

def main_coroutine():
    for n in range(4):
        waiting_to_sleep.append((0, concurrent_sleep(n)))
    event_loop()

if __name__ == '__main__':
    main_coroutine()
