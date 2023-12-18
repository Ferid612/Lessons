from datetime import datetime
import time 




time_1 = datetime.now()

for a in range(5):
    time.sleep(1)
    print(a)
    
time_2 = datetime.now()

difference = time_2 - time_1

print(difference.total_seconds())