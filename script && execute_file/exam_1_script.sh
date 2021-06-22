#! /bin/bash

#Initial X
X=$(echo "scale=1; -2.70" | bc)

#Step 0.1
STEP=$(echo "scale=1; 0.01" | bc)

I=1
OUT=""

#Output file
FILE="../result/output1_new.txt"
touch $FILE

rm input1.txt
touch "input1.txt" #Let's generate output!!!

while [ $I -lt 1024 ]
do
        echo "$X" > "input1.txt"
        echo $(wine 6.exe)

        while read -r CURRENT_LINE
                do
                        OUT="$CURRENT_LINE"
        done < "./output1.txt"

        echo "$X $OUT" >> $FILE

        X=$(echo "scale=2; $X+$STEP" |bc)
        ((I++))
done

