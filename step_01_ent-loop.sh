#!/bin/bash



# loop through business files
for filename in ./BusinessMails/*.msg; do
    
        python entropie.py  -s 32 -b -m local  "$filename"   >> entfiles_raw_BE.csv
    
done

# loop through test files
for filename in ./test_data/*.msg; do
    
        python entropie.py  -s 32 -b -m local  "$filename"   >> entfiles_test_data.csv
    
done
