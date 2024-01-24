import time
seconds=1
while True:
    print("Hello")
    time.sleep(seconds)
    seconds+=1
    if(seconds==4):
        print("ENd of loop")
        break
