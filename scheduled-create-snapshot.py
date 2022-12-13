import schedule
from create_snapshots import create_snapshots
import time

schedule.every(5).minutes.do(create_snapshots('created-by', 'python-script'))

while True:
    schedule.run_pending()
