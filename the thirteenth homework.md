# the thirteenth homework

标签（空格分隔）： 未分类

---_electrical field and partial differential equation_

###the abstract
######First introduce the different method to  deal with the Laplace equation numerically, and then to calculate the electrical field in different boundary conditions. 
###the fundamental principle
######To solve the Laplace equation: ![此处输入图片的描述][1]. We use the idea similar to the ODE, to transform the continous differential to discrete iteration.  
######![此处输入图片的描述][2]
######![此处输入图片的描述][3]
######then tranform all the three differential operator we get 
######![此处输入图片的描述][4]
######At that case, we can use the iteration to solve the problem. First set the initial boundary condition and interate it step by step until and change before and after the iterate is much small, which means the whole system approaches steady.
######there are two methods mentioned on the book.
######first is the Jacobi method,which the six value on the left hand of the equaiton are all old value(the result of the last value).and the second is the Guass-Seidel method(the point before the current point in iteration use the newest interation result, while others use the old value)
######To make the problem simple we only deal with the two dimensional problem here.  
######the square-square problem: two square, one is in the center of the other the V on the inner square is constant(+1), the V on the edge of outer square is also constant(-1). Then try to solve the potential in the middle area between two squares. 
######then the two flats problem, since in the numerical method we can not deal with a problem with infinite spatial volume. Then we consider two flats with different electrical potential in a square area and potential on the edge of the area is constant. In this problem, we compare two different method: Jacobi and SOR. 
######We first plot the relation the fluctuation after every iteration step and iteration times, then the relationship of step length and covergence speed.
###the numerical result
######![此处输入图片的描述][5] divided into 96
######[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp37.py)
######![此处输入图片的描述][6] divided into 48
######[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp43.py)
######![此处输入图片的描述][7] we set the initial potential on the edge to be 0.5 and 1.0 on the center.
######[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp44.py)
######![此处输入图片的描述][8] we set the shape of the center to be circle.
######[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp45.py)
######![此处输入图片的描述][9] we set the shape of the edge to be circle.
######we first consider the two flats with the same potential :
######![此处输入图片的描述][10]
######then with opposite potential
######![此处输入图片的描述][11]
######the previous results are drawn out by the Jacobi method then we deal the same problem with the SOR method
######![此处输入图片的描述][12]
######we can see the result at the low iteration time (such as 10) are not very steady.
######![此处输入图片的描述][13]
###[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp46.py)
######it is easy to see the convergent speed of Jacobi method approximately proportionate the square of step length, while of the SOR  is proportaionate to the step length.
######![此处输入图片的描述][14]
###[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp47.py)
######we can see as the iteration times increase, the SOR convergent more faster, but it has some fluctation during the whole process. 
###Reference
######Computational Physics, Nicholas J. Giordano & Hisao Nakanishi

######《Python基础教程》


  [1]: http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%7BV%7D%7D%7B%5Cpartial%7Bx%7D%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%7BV%7D%7D%7B%5Cpartial%7By%7D%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%7BV%7D%7D%7B%5Cpartial%7Bz%7D%5E2%7D=0
  [2]: http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%7BV%7D%7D%7B%5Cpartial%7Bx%7D%5E2%7D=%5Cfrac%7B1%7D%7B%5CDelta%20%7Bx%7D%7D%5B%5Cfrac%7BV%28i&plus;1,j,k%29-V%28i,j,k%29%7D%7B%5CDelta%20%7Bx%7D%7D-%5Cfrac%7BV%28i,j,k%29-V%28i-1,j,k%29%7D%7B%5CDelta%20%7Bx%7D%7D%5D
  [3]: http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%7BV%7D%7D%7B%5Cpartial%7Bx%7D%5E2%7D=%5Cfrac%7BV%28i&plus;1,j,k%29&plus;V%28i-1,j,k%29-2V%28i,j,k%29%7D%7B%5CDelta%20%7Bx%7D%5E2%7D
  [4]: http://latex.codecogs.com/gif.latex?%5Cfrac%7BV%28i&plus;1,j,k%29&plus;V%28i-1,j,k%29&plus;V%28i,j&plus;1,k%29&plus;V%28i,j-1,k%29&plus;V%28i&plus;1,j,k%29&plus;V%28i,j,k&plus;1%29%7D%7B6%7D=V%28i,j,k%29
  [5]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/square%20field2.png
  [6]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/square%20field3.png
  [7]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/square%20field4.png
  [8]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/square%28circle%20inner%29%20field.png
  [9]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/square%28circle%20outer%29%20field.png
  [10]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/two%20flat1.png
  [11]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/two%20flat%20field.png
  [12]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/two%20flat%20field%28SOR%29.png
  [13]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/iteration%20times%20via%20L.png
  [14]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/covergence%20of%20two%20method.png