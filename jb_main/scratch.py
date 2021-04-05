from datetime import datetime, timedelta
import time


now = datetime.now()



later = datetime.now()

diff = timedelta(now, later)

time.sleep(15)

print(diff)

time.sleep(15)

print(diff)

