import time

def MyFunction():
    print("Main function executed.")

main_interval_min = 1
message_interval_sec = 10

while True:
    MyFunction()
    time.sleep(message_interval_sec)
    while cnt > 0:
        print("Program sleeping ... ")
        cnt = cnt - message_interval_sec
        time.sleep(message_interval_sec)
