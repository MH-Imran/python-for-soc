# count_ips.py
# Simple script to count how many times each IP appears in a log file

from collections import Counter

def count_ips(log_file):
    with open(log_file, 'r') as f:
        lines = f.readlines()

    ip_list = []

    for line in lines:
        parts = line.split()
        for item in parts:
            if item.count('.') == 3:  # simple check for IPv4
                ip_list.append(item)

    ip_count = Counter(ip_list)

    for ip, count in ip_count.most_common():
        print(f"{ip}: {count} times")

# Example usage:
# count_ips('sample_log.txt')
