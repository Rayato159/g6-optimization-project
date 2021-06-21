#! /bin/bash

#Initial X_1 X_2
X_1=$(echo "scale=1; -2.0" | bc)
X_2=$(echo "scale=1; -2.0" | bc)

#Step 0.1
STEP=$(echo "scale=1; 0.1" | bc)

I=1
J=1
LINE=1
OUT=""

#Ouput file
FILE="../result/output2.txt"
touch $FILE

#Let's generate output!!!
while [ $I -lt 42 ]
	do

	while [ $J -lt 41 ]
		do

		rm input2.txt
		touch "input2.txt"

		echo "$X_1 $X_2" >> "input2.txt"
		
		echo $(wine 2-6.exe)

		while read -r CURRENT_LINE
			do
				OUT="$CURRENT_LINE"
		done < "./output2.txt"
		
		echo "$X_1 $X_2 $OUT" >> $FILE

		X_2=$(echo "scale=1; $X_2+$STEP" | bc)
		((J++))

	done
	J=0

	X_1=$(echo "scale=1; $X_1+$STEP" | bc)
	X_2=$(echo "scale=1; -2.0" | bc)

	((I++))
done
