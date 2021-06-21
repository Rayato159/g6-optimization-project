#! /bin/bash

#Initial X
X=$(echo "scale=1; -2.7" | bc)

#Step 0.1
STEP=$(echo "scale=1; 0.1" | bc)

I=1
OUT=""

#Output file
FILE="../result/output1.txt"
touch $FILE

#Let's generate output!!!
while [ $I -lt 107 ]
do	
	rm input1.txt
	touch "input1.txt"

	echo "$X" >> "input1.txt"
	echo $(wine 6.exe)
	
	while read -r CURRENT_LINE
		do
		       	OUT="$CURRENT_LINE"
        done < "./output1.txt"
	
	echo "$X $OUT" >> $FILE

	X=$(echo "scale=1; $X+$STEP" |bc)
	((I++))
done
