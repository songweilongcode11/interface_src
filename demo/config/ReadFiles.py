import queue
phone = 13265899708
tel_phone = [str(phone+i) for i in range(100)]
print(tel_phone)
telqueue = queue.Queue()
for i in telqueue:
    telqueue.put_nowait(i)
    print(telqueue)