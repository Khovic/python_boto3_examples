import schedule
import create_snapshots

while True:
    schedule.every(5).minutes.do(create_snapshots.create_snapshots('created-by', 'python-script'))