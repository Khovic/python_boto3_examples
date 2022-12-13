import schedule
import create_snapshots
import time

schedule.every(5).minutes.do(create_snapshots.create_snapshots('created-by', 'python-script'))

time.sleep(120)
schedule.run_pending()
