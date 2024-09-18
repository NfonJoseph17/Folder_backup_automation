import os
import shutil
import datetime
import schedule
import time

source_dir = "/Users/nfonjoseph/Desktop/images/Bridge you"
destination_dir = "/Users/nfonjoseph/Desktop/Documents/backups"

def copy_folder_to_dir(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"folder copied to {dest_dir}")
    except FileExistsError:
        print(f"Folder already exist in {dest}")


schedule.every().day.at("11:00").do(lambda: copy_folder_to_dir(source_dir, destination_dir))
while True:
    schedule.run_pending()
    time.sleep(60)