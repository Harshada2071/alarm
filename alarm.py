from datetime import datetime
import time
alarm_time = input("enter alarm time (HH:MMAM/PM):")
while True:
    current_time = datetime.now().strftime("%I:%M %p")
    print(current_time)

    if  current_time == alarm_time:
        print("wake up! alarm ringing...")

        break
    time.sleep(1)
