

# Do the same thing on each file

files=("venus.csv" "mars.csv" "jupiter.csv" "saturn.csv" "sun.csv")

for f in "${!files[@]}"
do

	cat ${files[$f]} > ${files[$f]}_original.csv

	sed -i 's/Rx//g' ${files[$f]}

	sed -i 's/:/ /g' ${files[$f]}

	sed -i 's/,//g' ${files[$f]}

	awk '{print $1 "," $2 "," $3 "," $4 "," $5 "," $6 "," $9}' ${files[$f]} > tmp.csv

	echo 'start month,start day,start year,start hour,start minute,ampm,label' | cat - tmp.csv > ${files[$f]}

	rm tmp.csv

	months=("Jan" "Feb" "Mar" "Apr" "May" "June" "July" "Aug" "Sep" "Oct" "Nov" "Dec")
	itr=1

	for i in "${!months[@]}"
	do
		sed -i 's/'${months[$i]}'/'${itr}'/g' ${files[$f]}
		itr=$((itr+1))
	done

done



##
