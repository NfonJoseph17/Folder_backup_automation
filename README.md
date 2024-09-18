# Folder_backup_automation
This Python script automatically copies a folder to a backup location at a scheduled time every day. It uses the shutil library to copy the folder and schedule to trigger the backup at a specified time.

Features

	•	Automatically backs up a folder to a new directory every day.
	•	Each backup is saved in a new folder named with the current date.
	•	Uses Python’s schedule module to run the backup task at a specified time.

Requirements

	•	Python 3.x
	•	schedule module

Setup Instructions

1. Install Required Python Libraries

You need to install the schedule module if it’s not already installed. You can do this using pip:
pip install schedule

2. Modify Source and Destination Paths
   Before running the script, modify the source and destination directories to your desired paths:
   source_dir = "/path/to/your/source/folder"
   destination_dir = "/path/to/your/destination/folder"
3. Set the Backup Time

The script is currently set to back up the folder every day at 11:00 AM:
schedule.every().day.at("11:00").do(lambda: copy_folder_to_dir(source_dir, destination_dir))
You can modify the time by changing "11:00" to the desired time in 24-hour format (e.g., "15:30" for 3:30 PM).

4. Running the Script

To start the backup process, simply run the script:
python backup_script.py

The script will:

	•	Copy the folder from the source directory to the destination directory.
	•	Create a new folder in the destination with the current date as the name.
	•	Schedule itself to run every day at the specified time.
