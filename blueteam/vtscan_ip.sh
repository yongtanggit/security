#! /usr/bin/bash

## This program queries VT database for identifying malicious IP  from a IPs list file. 
## It determines whether the IPs are malicious by analysing the retrieved reports.     

# API key and file path
key=$(cat vt-key.txt)
file_path="ips.txt"

# VT API version v2
url="https://www.virustotal.com/vtapi/v2/ip-address/report?ip=$ip&apikey=$key"

# Process and analysing the reports
while read ip;
do	
	# Looping through the report in Json format. 
	result=$(curl -s "https://www.virustotal.com/vtapi/v2/ip-address/report?ip=$ip&apikey=$key" | jq | grep -E '"detected_urls' | tr ' ' '-') 
	# Analyse the data
	if [[ "$result" == '--"detected_urls":-[' ]]; then	
	   echo "$ip is flagged"
	else 
	   echo "$ip is good"
	fi
	# Avoid the VT api connect limit(4 times/minute) 
	sleep 15
done < "$file_path"





