# # Bofore semophore
# import threading
# import time
# import random

# buffer = []
# BUFFER_SIZE = 100

# def producer():
#     global buffer
#     for i in range(5):
#         if len(buffer) + 2 <= BUFFER_SIZE:
#             print(f"Producer adding pair at size {len(buffer)}")
#             buffer.append("P1")
#             buffer.append("P2")
#         else:
#             print("Producer found buffer full")
#         time.sleep(random.random())

# def consumer():
#     global buffer
#     for i in range(5):
#         if len(buffer) >= 2:
#             buffer.pop()
#             buffer.pop()
#             print(f"Consumer removed pair, size now {len(buffer)}")
#         else:
#             print("ERROR: Consumer found buffer empty!")
#         time.sleep(random.random())

# threads = []

# for i in range(3):
#     threads.append(threading.Thread(target=producer))

# threads.append(threading.Thread(target=consumer))

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()

# print("Final buffer size:", len(buffer))


# After semaphore
import threading
import time
import random

buffer = []
BUFFER_SIZE = 100

mutex = threading.Semaphore(1)
empty = threading.Semaphore(50)  # 50 pairs
full = threading.Semaphore(0)

def producer():
    global buffer
    for i in range(5):
        empty.acquire()
        mutex.acquire()

        print(f"Producer placing pair at {len(buffer)}")
        buffer.append("P1")
        buffer.append("P2")

        mutex.release()
        full.release()

        time.sleep(random.random())

def consumer():
    global buffer
    for i in range(5):
        full.acquire()
        mutex.acquire()

        buffer.pop()
        buffer.pop()
        print(f"Consumer removed pair, size now {len(buffer)}")

        mutex.release()
        empty.release()

        time.sleep(random.random())

threads = []

for i in range(3):
    threads.append(threading.Thread(target=producer))

threads.append(threading.Thread(target=consumer))

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Final buffer size:", len(buffer))