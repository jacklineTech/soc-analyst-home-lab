#!/usr/bin/env python3

import re
import sys
from collections import Counter
from pathlib import Path

log_file = Path(
    sys.argv[1] if len(sys.argv) > 1
    else "evidence/sample-logs/sample-auth.log"
)

threshold = 3

if not log_file.is_file():
    print(f"ERROR: Log file not found: {log_file}")
    sys.exit(1)

failed_counts = Counter()
failed_then_success = set()
successful_count = 0

with log_file.open("r", encoding="utf-8") as file:
    for line in file:
        match = re.search(
            r"\bfrom\s+(\d{1,3}(?:\.\d{1,3}){3})\b",
            line
        )

        if "Failed password" in line and match:
            failed_counts[match.group(1)] += 1

        elif "Accepted password" in line:
            successful_count += 1

            if match:
                ip = match.group(1)
                if failed_counts[ip] >= threshold:
                    failed_then_success.add(ip)

print("HOME SOC LAB - AUTHENTICATION LOG ANALYSIS")
print("=" * 44)
print(f"Log file: {log_file}")
print(f"Failed login events analysed: {sum(failed_counts.values())}")
print(f"Successful login events in sample: {successful_count}")
print(f"Detection threshold: {threshold} failed logins per IP")
print()

if not failed_counts:
    print("No failed-login events with identifiable source IPs found.")

for ip, count in failed_counts.most_common():
    print(f"Source IP: {ip} | Failed logins: {count}")

    if count >= threshold:
        print(f"ALERT: Repeated failed logins from {ip}")
        print("Suggested action: Review surrounding events and verify context.")
    else:
        print("No alert: Count is below the configured threshold.")

    if ip in failed_then_success:
        print(f"ALERT: Failed logins followed by a successful login from {ip}")
        print("Suggested action: Investigate the account, source IP, and login timeline.")

print()
print("NOTE: This is fictional training data.")
print("An alert indicates a pattern for investigation, not proof of compromise.")
