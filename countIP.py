import re
from collections import Counter
import csv

# Path to the log file
log_file_path = "access.log"

# Regex pattern to extract IP addresses (typical format)
ip_pattern = re.compile(r'^(\d{1,3}(?:\.\d{1,3}){3})')

# Counter to store frequency of each IP
ip_counter = Counter()

# Read and parse the log file
with open(log_file_path, 'r') as file:
    for line in file:
        match = ip_pattern.match(line)
        if match:
            ip = match.group(1)
            ip_counter[ip] += 1

# Display top 5 IPs
print("Top 5 IPs by request count:")
for ip, count in ip_counter.most_common(5):
    print(f"{ip}: {count} requests")

# Save all IP counts to a CSV file
csv_file_path = "ip_request_counts.csv"
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP Address", "Request Count"])
    for ip, count in ip_counter.items():
        writer.writerow([ip, count])

print(f"\nSaved {len(ip_counter)} IP entries to '{csv_file_path}'")
