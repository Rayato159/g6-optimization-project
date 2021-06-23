## :pencil: Final Project - Black Box Optimization problem [Group 6]

### Lecturer:
Dr. Atthaphon Ariyarit

### Members:  
1. Ruangyot Nanchiang B6116736
2. Sahassawat Rattanamongkolkul B6113056
3. Kamonlaphat Sitthitharanon B6130268

### Deal with black box:
At first. We don’t know what our black box contains. The first thing we have to do is put a value in an input file and run the black box file to get output. But that method seems like slowly because we only can put one value and run the black box file one at a time.  


As the following problem. We write a [shell script](https://github.com/Rayato159/G6-Optimization-Exam/tree/main/script%20%26%26%20execute_file) (.sh file) to solve that problem. The shell script will input a value, run the black box function to get output, and write output values into the new output files autonomously.  

### Find the graph from output:
Now, We already have output files with containing all input and value of the function from the input. The next thing we have to do is plot the graph to evaluate and find some spot where the minimum value is.

### Exam No.1
First of all, we use shell script to get outputs from 6.exe

Second, plot the graph from outputs that we get from first step.

![Figure_1](https://user-images.githubusercontent.com/85036863/123076115-06fbe180-d443-11eb-94f4-35cc316cf8c8.png)

Third, we connect Python to 6.exe to get the real time output. We know the range of x where the lowest point is placed, so we choose Newton method for optimize the problem which use 3 iterations to solve.

Finally,

```python
lowest point of this problem is -1.9946  at x = 4.8153 
```
