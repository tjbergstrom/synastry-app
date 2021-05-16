

cat node.csv > node_original.csv

# Replace slashes with commas
tr -s '[/]' ',' < node.csv > tmp.csv

# Replacece blank spaces with commas
tr -s '[:blank:]' ',' < tmp.csv > node.csv

# Delete last column
awk '!($8="")' node.csv > tmp.csv

# Trim trailing white spaces after deleting last column
awk '{$1=$1};1' tmp.csv > node.csv

# Remove unwanted columns, seperate remaining columns with comma

awk -F "," '{print $1,$2,$3,$5,$6,$7,$8}' node.csv > tmp.csv

awk '{print $1 "," $2 "," $3 "," $4 "," $5 "," $6 "," $7}' tmp.csv > node.csv

# Add a header

echo 'start year,start month,start day,end year,end month,end day,label' | cat - node.csv > tmp.csv

mv tmp.csv node.csv



##
