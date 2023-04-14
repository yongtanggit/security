#! /bin/bash

## DATA Processing From a CVS file with AWK




## create a file path for IPs input ##
file_path='code/test-data/ips.txt'
full_file_path="$HOME/$file_path"

## check file path ##
if ! [[ -f "$full_file_path" ]]; then
   echo "$full_file_path not exit"
   exit
fi
## create a function to connet a ssh server and
## provide connection result for analysis
## three "-o" options are set to avoid interactive shell and shorten timeout time. 
ssh_test () {
	ssh   -vvv -o PasswordAuthentication=no -o StrictHostKeyChecking=no -o ConnectTimeout=5 "$line" 2>&1
}

while read -r line
do
  if ssh_test | grep -q 'Connection timed out'; then
     echo "Connection timed out"
  elif ssh_test | grep -q 'cbc'; then 
	echo "$line "
  fi
done < "$full_file_path"




