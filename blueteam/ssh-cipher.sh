#! /bin/bash

input='ips.txt' 


while read -r line
do
  output=$(ssh -T -o PasswordAuthentication=no -o StrictHostKeyChecking=no "$line")
  echo $output 
  
#| grep  -q 'cbc';
   #then 
	#echo "$line: "
#fi
done < "$input"




