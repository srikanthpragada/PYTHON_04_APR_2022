from threading import Thread
import threading


def print_numbers():
    print(threading.current_thread().name)
    for n in range(1, 11):
        print(n)


print(threading.main_thread())
t = Thread(target=print_numbers, name = "printthread")
t.start()
