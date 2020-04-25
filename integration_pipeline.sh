#!/bin/bash
echo "######################################"
echo "Starting Normalization and Comparison"
echo "######################################"
# loop through business files
#rm /home/nodejs/df-privacy-checker_tools/DF-privacy-checker/pipe_entfiles_raw_BE.csv
for filename in /home/nodejs/df-privacy-checker_tools/DF-privacy_aware_file_checker/directory/*.msg; do

echo "$filename"
echo python /home/nodejs/df-privacy-checker_tools/DF-privacy-checker/entropie.py  -s 32 -b -m local  "$filename"
          python /home/nodejs/df-privacy-checker_tools/DF-privacy-checker/entropie.py  -s 32 -b -m local  "$filename"   >> /home/nodejs/df-privacy-checker_tools/DF-privacy-checker/pipe_entfiles_raw_BE.csv


done




# echo 'bGludXhoaW50LmNvbQo=' | base64 --decode
file=$(echo -n $1 | base64 --decode)
#file=$(echo -n $1)
echo $0

# loop through test files
rm /home/nodejs/df-privacy-checker_tools/DF-privacy-checker/pipe_entfiles_test_data.csv
# for filename in ./test_data/*.msg; do

echo python /home/nodejs/df-privacy-checker_tools/DF-privacy-checker/entropie.py  -s 32 -b -m local "/home/nodejs/df-privacy-checker_tools/DF-privacy_aware_file_checker/uploads/$file"
python /home/nodejs/df-privacy-checker_tools/DF-privacy-checker/entropie.py  -s 32 -b -m local "/home/nodejs/df-privacy-checker_tools/DF-privacy_aware_file_checker/uploads/$file"   >> /home/nodejs/df-privacy-checker_tools/DF-privacy-checker/pipe_entfiles_test_data.csv

# done


rm pipe_entfiles_raw_BE_transformed.csv

rm pipe_entfiles_test_data_transformed.csv

rm heatmap_file_comparison.csv

cd /home/nodejs/df-privacy-checker_tools/DF-privacy-checker/

#python /home/nodejs/df-privacy-checker_tools/DF-privacy-checker/integration_pipeline_transform_and_compare.py >> "./../DF-privacy_aware_file_checker/results/entropy_cosine_compare/output_$(echo -n $1 | base64 --decode)_final.csv"
python /home/nodejs/df-privacy-checker_tools/DF-privacy-checker/integration_pipeline_transform_and_compare.py >> "./../DF-privacy_aware_file_checker/results/differentiator/output_$(echo -n $1 | base64 --decode)_final.csv"

