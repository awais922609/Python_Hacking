import json


    #Counting failed attempts
def numberOfFailedAttempts(data):
    count = 0
    for entry in data:
        if entry['status'] == "failed":
            count += 1
    print (f"\n Number of failed attempts : {count}")

with open("./security_log.json" , "r") as file:
    data = json.load(file)
    for entry in data:
        print(f"Timestamp: {entry['timestamp']}  - Username: {entry['username']} - IP Address: {entry['ip_address']} - Status: {entry['status']} ")
    
    numberOfFailedAttempts(data)

    #Printing failed logins

    for entry in data:
        if entry['status'] == "failed":
            
            print("\n Printing failed Enteries")
            print(f"Timestamp: {entry['timestamp']}  - Username: {entry['username']} - IP Address: {entry['ip_address']} - Status: {entry['status']} ")

