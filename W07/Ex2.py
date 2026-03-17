# # before semaphore
# import threading
# import time
# import random

# def p1():
#     print("H", end="")
#     time.sleep(random.random())
#     print("E", end="")

# def p2():
#     print("L", end="")

# def p3():
#     print("O", end="")

# threads = [
#     threading.Thread(target=p1),
#     threading.Thread(target=p2),
#     threading.Thread(target=p3)
# ]

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()

# print()


# After semaphore
import threading

a = threading.Semaphore(1)
b = threading.Semaphore(0)
c = threading.Semaphore(0)

def p1():
    a.acquire()
    print("H", end="")
    print("E", end="")
    b.release()

def p2():
    b.acquire()
    print("L", end="")
    c.release()

def p3():
    c.acquire()
    print("L", end="")
    print("O")

t1 = threading.Thread(target=p1)
t2 = threading.Thread(target=p2)
t3 = threading.Thread(target=p3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()