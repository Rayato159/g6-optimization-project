## :pencil: Final Project - Black Box Optimization problem [Group 6]

### Lecturer:
Dr. Atthaphon Ariyarit

### Members:  
1. Ruangyot Nanchiang B6116736 (Coding)
2. Sahassawat Rattanamongkolkul B6113056 (Tester)
3. Kamonlaphat Sitthitharanon B6130268 (Validation & Documentation)

### Infomation:
All algorithms and solutions code is in the [src](https://github.com/Rayato159/G6-Optimization-Exam/tree/main/src) folder. Include some class we wrote for comfortable to used in another file.

### Deal with black box:
At first. We don’t know what our black box contains. The first thing we have to do is put a value in an input file and run the black box file to get output. But that method seems like slowly because we only can put one value and run the black box file one at a time.  


As the following problem. We write a shell script [exam_1_script.sh](https://github.com/Rayato159/G6-Optimization-Exam/blob/main/src/exam_1_script.sh) and [exam_2_script.sh](https://github.com/Rayato159/G6-Optimization-Exam/blob/main/src/exam_2_script.sh) (.sh file) to solve that problem. The shell script will input a value, run the black box function to get output, and write output values into the new output files autonomously.  

### Find the graph from output:
Now, We already have output files containing some input and value of the function from the input. The next thing we have to do is plot the graph to evaluate and find some spot where the minimum value is.

### Exam No.1
Exam 1 is quite simple. Just need to visualize some output from executing a file to evaluate where the minimum point is.

![fig1](https://github.com/Rayato159/G6-Optimization-Exam/blob/main/graph/exam_1_graph.png)

Finally, We connect Python to 6.exe (Here the code to connect black box function to out Python in real time [CrackBox.py](https://github.com/Rayato159/G6-Optimization-Exam/blob/main/src/CrackBox.py).) to get the real time output. We know the range of x where the lowest point is placed, so we choose **"Newton method"** for optimize the problem which use 3 iterations to solve.

***Code:*** [exam_1_solution.py](https://github.com/Rayato159/G6-Optimization-Exam/blob/main/src/exam_1_solution.py)

***Output:***
```shell
Iter	xi	fx	ea
1	4.8210	-1.8753	1.4726
2	4.8153	-1.9937	0.1179
3	4.8153	-1.9946	0.0007
Answer is 4.8153 and the minimum value is -1.9946
```
***Answer: The minimum value is -1.9946 at x = 4.8153.***  
***Iterations: 3**  

### Exam No.2
Now the real things begin. In this part, we do the same as previous. Thus, plot the graph at first to visualize where the minimum point is.

![fig2](https://github.com/Rayato159/G6-Optimization-Exam/blob/main/graph/exam_2_3D_plot.png)

After visualizing this function we got a big problem because we can't define where the minimum point is.  
Therefore, let's try again with a contour plot.

![fig3](https://github.com/Rayato159/G6-Optimization-Exam/blob/main/graph/exam_2_contour.png)

This problem can't use calculus optimization to deal with. Because we don’t even know where the global minimum point is. Therefore, we turn to an **"Evolutionary algorithm"** to find the best solution and deal with this problem.  

#### Into the "Genetic Algorithm":

The Genetic Algorithm (GA) is a method for solving constrained and unconstrained optimization problems based on Charles Darwin's theory of natural selection, which mimics biological evolution.    

These methods are randomized search algorithms that have been developed in an effort to imitate the mechanics of natural selection and natural genetics. Genetic algorithms operate on string structures, like biological structures, which are evolving in time according to the rule of survival of the fittest by using a randomized yet structured information exchange. The first string structure has the fittest information, which will be used for the new string, call generations. The main characteristics of a genetic algorithm are as follow :  

  1. The genetic algorithm works with the coding of the parameter set only, not the parameters themselves.
  2. The genetic algorithm initiates its search from a population of points, not a single point
  3. The genetic algorithm uses payoff information, not derivatives.    

To describe the process of the genetic algorithm starts with a random generation of the initial population. Following with the selection, crossover, and mutation e preceded until the generation reaches maximum.    

    • Selection
The selection of parents to produce successive generations plays a crucial role in this method. The goal allows the fittest individuals to be more often selected to reproduce. 

    • Crossover
The crossover step is an important operator of the genetic algorithm. It is responsible for the structure recombination and the convergence speed of the GA, and it is applied with a high probability of around 0.6-0.9. After the selected operation, simple crossover proceeds. The main objective of crossover is to reorganize the information of two different individuals and produce a new one.

    • Mutation 
The mutation is a background operator, which produces a spontaneous change in various chromosomes. In an artificial genetic system, the mutation operator protects against some irrecoverable loss. It is an occasional random alteration of the value in the string position. The mutation is needed because even though reproduction and crossover effectively search and recombine extent notions, occasionally, they may lose some potentially useful genetic material.    

####  Flow chart of out "Genetic Algorithm":
***Code:*** [Genetic_Algorithm.py](https://github.com/Rayato159/G6-Optimization-Exam/blob/main/src/Genetic_Algorithm.py) and [exam_2_Solution.py](https://github.com/Rayato159/G6-Optimization-Exam/blob/main/src/exam_2_Solution.py)

![flowchart](https://github.com/Rayato159/G6-Optimization-Exam/blob/main/graph/Genetic%20Algorithm.svg)

#### Continue with exam no.2
The result of the genetic algorithm as follows.

![fig4](https://github.com/Rayato159/G6-Optimization-Exam/blob/main/graph/Genetic_plot.png)

Then, the genetic algorithm can find the minimum of this function.    

***Output:***
```shell
Execution time: 2761.4247014522552

Final solution (Convergence): [0. 1. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
Encode_x1 (Convergence): [1. 0. 0. 0. 0. 0. 0. 0.]
Encode_x2 (Convergence): [0. 1. 0. 0. 0. 0. 0. 0.]

Final solution (Best): [0. 1. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
Encode_x1 (Best): [1. 0. 0. 0. 0. 0. 0. 0.]
Encode_x2 (Best): [0. 1. 0. 0. 0. 0. 0. 0.]


Final obj value (Convergence) 3.01541
Decode_x1 (Convergence): 0.00784
Decode_x2 (Convergence): -0.99608

Final Obj value (Best): 3.01541
Decode_x1 (Best): 0.00784
Decode_x2 (Best): -0.99608
```
***Answer: The minimum value is 3.01541 at x1 = 0.0078, x2 = -0.99608.***  
***Time execute: 2761.42 sec (46 min)***  
***Time complexity: O(100 population * 25 generation) = O(2500)***  
