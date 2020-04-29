import time

print('Star:', time.ctime())

time.sleep(2)
print('End: ', time.ctime())


seconds = 4
while seconds != 0:
    print(f'Voce tem {seconds} para responder...')
    time.sleep(1)
    seconds -= 1
print('Time over...')