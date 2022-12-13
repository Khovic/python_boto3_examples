import schedule
import create-snapshots

schedule.every(5).minutes.do(create-snapshots.create_snapshots('created-by', 'python-script'))