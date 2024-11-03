import datetime

# Opening a file in write mode
with open("security_log.txt", "w") as file:
    file.write("Log Entry 1: Security tool initialized.\n")
    file.write("Log Entry 2: Scanning started.\n")
    file.write("Log Entry 3: Scan complete.\n")
    file.close()

def logActivity(activity):
    timestamp = datetime.datetime.now()
    with open("security_log.txt", "a") as file:
        file.write(f"{timestamp} - {activity}")
        file.close()

def displayActivity():
    with open("security_log.txt" , "r") as file:
        contents = file.read()
        print("contents are :", contents)

logActivity("Log Entry 4: Report generated.")
displayActivity()