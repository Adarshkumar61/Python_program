import threading
import time

def frame(): 
    while True:
        print('Frame capturing...🤖')
        time.sleep(1)
        
def motor():
    while True:
        print('Motor is running...🚗')
        time.sleep(0.5)

t1 = threading.Thread(target=frame, daemon=True)
t2 = threading.Thread(target=motor, daemon=True)
t1.start()
t2.start()
input('Press Enter to stop...\n')
print('Stopping threads and exiting.')