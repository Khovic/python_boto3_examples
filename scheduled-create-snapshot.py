import schedule
import create_snapshots
import time

#schedule.every(5).minutes.do(create_snapshots.create_snapshots('created-by', 'python-script'))

def print_poo():
    print('poopoo')

schedule.every(1).minutes.do(print_poo)
while True:
    schedule.run_pending()
