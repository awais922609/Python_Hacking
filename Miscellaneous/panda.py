import pandas as pd

df_json = pd.read_json("./security_log.json")

print(df_json)

#Printing failed data 

failed_attemps = df_json[df_json["status"] == "failed"]
print (failed_attemps)

failed_groups = df_json[df_json["status"] == "failed"].groupby("username").size()
print(failed_groups)

#Top 3 IP Addresses
top_failed_ips = df_json[df_json["status"] == "failed"]["ip_address"].value_counts().head(3)
print("Top 3 IP addresses with failed attempts:\n", top_failed_ips)

#Timebase Filter Function
def filter_by_date(df, start, end):
    # Converting 'timestamp' column to datetime format
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Filtering by date range
    filtered_df = df[(df["timestamp"] >= start) & (df["timestamp"] <= end)]
    return filtered_df

# Example usage
start_date = "2024-10-29"
end_date = "2024-10-30"
filtered_attempts = filter_by_date(df_json, start_date, end_date)
print("Login attempts within date range:\n", filtered_attempts)
