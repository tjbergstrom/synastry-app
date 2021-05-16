

cat venus.csv > venus_original.csv

sed -i 's/Rx//g' venus.csv

sed -i 's/:/ /g' venus.csv

sed -i 's/,//g' venus.csv

awk '{print $1 "," $2 "," $3 "," $4 "," $5 "," $6 "," $9}' venus.csv > tmp.csv

echo 'start month,start day,start year,start hour,start minute,ampm,label' | cat - tmp.csv > venus.csv

rm tmp.csv

months=("Jan" "Feb" "Mar" "Apr" "May" "June" "July" "Aug" "Sep" "Oct" "Nov" "Dec")
itr=1

# Repace month names with numbers

for i in "${!months[@]}"
do
	sed -i 's/'${months[$i]}'/'${itr}'/g' venus.csv
	itr=$((itr+1))
done



##
