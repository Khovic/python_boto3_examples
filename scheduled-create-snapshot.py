import schedule
import create_snapshots

schedule.every(5).minutes.do(create_snapshots.create_snapshots('created-by', 'python-script'))

while True:
    schedule.run_pending()
