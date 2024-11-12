import schedule
import time
import zipfile
import datetime
import os


def logArchive():
    logsdirectory ="logs"
    archive_name = f"Logs Backup {datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"


    with zipfile.ZipFile(archive_name , "w") as archive:
        for root,dirs,files in os.walk(logsdirectory):
            for file in files:
                file_path = os.path.join(root,file)
                archive.write(file_path, os.path.relpath(file_path, logsdirectory))

    print(f"Logs archived to {archive_name}")

schedule.every().day.at("02:00").do(logArchive)

while True:
    schedule.run_pending()
    time.sleep(60)

