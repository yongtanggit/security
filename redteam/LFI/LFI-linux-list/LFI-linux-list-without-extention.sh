#! /bin/bash

## I wrote this code to remove files' extentions in a LFI Linux list, which needs for LFI fuzzing.  
## See my walkthrough on "symfonos 4" for more details.

# Remove any pre-existing output file
rm 'LFI-linux-list-without-extention.txt' 2>/dev/null 

input='LFI-linux-list.txt'

while IFS= read -r line
do 
	filename_e=$(basename "$line")
	filename="${filename_e%.*}"
	echo $line | sed -e "s/$filename_e/$filename/" >> 'LFI-linux-list-without-extention.txt'
done < "$input"

# Add files such as /.bash_config back the new list  
grep "/\." LFI-linux-list.txt >> 'LFI-linux-list-without-extention.txt'  


