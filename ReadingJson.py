import json

with open("./security_log.json" , "r") as file:
    data = json.load(file)
    # print(data)

    for entry in data:
        print(f"Timestamp: {entry['timestamp']}  - Username: {entry['username']} - IP Address: {entry['ip_address']} - Status: {entry['status']} ")

    #Printing failed logins

    for entry in data:
        if entry['status'] == "failed":
            
            print("\n Printing failed Enteries")
            print(f"Timestamp: {entry['timestamp']}  - Username: {entry['username']} - IP Address: {entry['ip_address']} - Status: {entry['status']} ")


