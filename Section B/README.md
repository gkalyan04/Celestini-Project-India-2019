### Section B

A) 
(1) The classification accuracy for the respective kernels are as follows.

     1. Linear Kernel
	With the linear kernel of the SVM the accuracy obtained .
	[1.         0.95238095 	0.9047619  	1.         0.94444444]
            These are the 5 -cross validation accuracy list obtained 
	    
     2.	Radial Basis Function
	[1.         0.95238095  	0.9047619  	1.         0.94444444]
	The accuracy list obtained was basically the same as linear.

     3.	Polynomial kernel
	[0.95454545 	0.95238095 	0.85714286 	0.84210526 	0.94444444]

     4. Sigmoid Kernel
	
	[0.86363636 	0.61904762 	0.80952381 	0.78947368 	0.83333333]

(2) 
We also trained a Neural Network with one hidden layer of 50 neurons and 7 neurons in the output layer.
     
We trained it for 15 epochs the cost started at  1.4595953  and the minimum cost was 0.03888691.
  
The accuracy started at 0.5049505 and ended up being 1.0000. 

<pre>
The precision score for every label depends upon the kernel which is being used like 

for linear kernel       
precision score : <br>
[1.     1.      1.     1.    1.     1.     1.]

And for sigmoid kernel
precision score : <br>
[1.     0.82608696          1.0        1.0     0.     0.42105263      0.75]

And for polynomial kernel
precision score : <br>
[1.     1.      1.     1.    1.     1     . 0.90909091]
</pre>

************************************************************************************************************* 
 
B)

The Model trained on SVM algorithm gave different type of performances on different kernels , 
Although the data size was very less but one thing that we can infer is accuracies on different kernels .
The Model performed the best on linear as well as rbf kernel giving as high as accuracy of 100 on some folds of cross validation. It performed the worst on sigmoid kernel , the precision scores were also a bit low for sigmoid kernel .
Conclusion :
Linear as well as rbf kernel for SVM proved to be the best for the zoo problem.

The model was also trained on the neural networks with one hidden layer of 50 neurons 
We trained it for 15 epochs, there was significant decrease of loss as described above and the model gave as high as accuracy of 99% after 15 epochs .
 
In the given problem both SVM(for linear or rbf kernel) and NN performed well as the precision and accuracy was on higher side for both.

*************************************************************************************************************

C)


The ROC curve for the SVM is as follows:
The curve shows the recall precisions relation for every class in the give problem statement


This for the sigmoid kernel 
<img src="https://github.com/piyush-98/Cesltine_TEST/blob/master/Section%20B/plot3.png">

This is for the linear,rbf kernel
<img src="https://github.com/piyush-98/Cesltine_TEST/blob/master/Section%20B/plot4.png">
