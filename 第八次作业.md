#第八次作业

标签（空格分隔）： 未分类

---

#the nonliear oscillation
###Abstract
######We consider a special type oscillation model. I first will analyze when the function will truly have a period as its parameter varys. Then build a computation method to find the periods of the function. Then to analyze the relation between the amplitude and the period of particular parameter.
###Basic principle
######the oscillation model ODE is :
######![此处输入图片的描述][1]
######the parameter is a, when a equals to one, it is simply the harmonic oscillation equation. While when it didn't equal to unity, the oscillation is nonlinear. We only analyze the integer parameter here. 
######To see the properties of this function more clearly: 
######http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2x%7D%7Bdt%5E2%7D%3D%5Cfrac%7Bdv%7D%7Bdt%7D%3D%5Cfrac%7Bdv%7D%7Bdx%7D%5Cfrac%7Bdx%7D%7Bdt%7D%3D%5Cfrac%7Bvdv%7D%7Bdx%7D%3D-kx%5Ea
######then do the integration separately,we get:
######http://latex.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7B2%7D%28v%5E2-v_%7B0%7D%5E2%29%3D%5Cfrac%7Bkx_%7B0%7D%5E%7Ba&plus;1%7D-kx%5E%7Ba&plus;1%7D%7D%7Ba&plus;1%7D
######the x0 and v0 is the initial location and speed. Then we let:
######![此处输入图片的描述][2]
######Then we see if the a is odd, then a+1 is even which means, with a definite speed the displacement of x have a boundary on both side:![此处输入图片的描述][3]
######here the speed v is definite. We say that only the displacement can't be infinite, can the period exists. they have a amplitude which only relevant to the initial conditions,![此处输入图片的描述][4]
######also the slope(speed)of the function is symmetry on the ![此处输入图片的描述][5]
######then at the same x, there are two speed with same quantity but different direction, which cooresponding to the two sides of the amplitude. 
######Consequently, we have full reason to believe that the odd number a equation will all have a period.
######On the contrary, for the even number a, there is no confinement on the displacement, so it can reach to infinity as long as the speed also reaches to infinity. ![此处输入图片的描述][6]
######Although you can say that just like the y=tan(x), they may be have some asymptotic lines but are also period function. While it seems impossible here.
######During our analyzation above, we can now build a function to explain the period:![此处输入图片的描述][7]
###the computation result
######first is the diagram of the function for different parameter:(1,3,5,7,9,11)
######![此处输入图片的描述][8]
######the initial conditions of these function is the same：（x0=1.0,v0=0)
######we can say the odd number equation truly exists period,and the period is proportional to the parameter.
######To see this we not only use the above period equation to calculate the period but also let the program to point out the periods from the first graph.Then we get
######![此处输入图片的描述][9]
####there exists a misleading the line between the spots doesn't represent the truly relation line,the only function of it is to point out which spots is corresponding to period equation results and which are others. This is very important.
######the relation between the amplitude and the period for different parameter.
######![此处输入图片的描述][10]
######(the low order)
######![此处输入图片的描述][11]
######(the upper order)
######we can say first like our conscious,the linear order function show that its periods is not relevant to the amplitude. However, unlike the linear equation, the other order all show a decreasing trend as their periods increase. And the larger the parameter is the faster the periods tend to zero.
######![此处输入图片的描述][12]
######![此处输入图片的描述][13]
######we say in the first graph that there exists a point where the periods for three equation is same,(x0=1.16,v0=0), the second graph depicts this properity,we can say it is truly this way.
######![此处输入图片的描述][14]
######this graph's initial condition is (x0=2,v0=0),we can say like the previous relation between amplitude and periods. Under this condition, the period of the nonlinear function is less than the linear term.
######also at the beginning the period for nonlinear equation is larger than than linear equation. but at some point the two is in the same and after that the nonlinear equation is less than the linear equation.
###[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp19.py)
###Reference
######Computational Physics, Nicholas J. Giordano & Hisao Nakanishi
######《Python基础教程》

  [1]: http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2x%7D%7Bdt%5E2%7D=-kx%5Ea
  [2]: http://latex.codecogs.com/gif.latex?v_%7B0%7D%5E2&plus;%5Cfrac%7Bkx_%7B0%7D%5E%7Ba&plus;1%7D%7D%7Ba&plus;1%7D=A=%5Cfrac%7Bkx%5E%7Ba&plus;1%7D%7D%7Ba&plus;1%7D&plus;v%5E2=Bx%5E%7Ba&plus;1%7D&plus;v%5E2
  [3]: http://latex.codecogs.com/gif.latex?%28-%28%5Cfrac%7BA-v%5E2%7D%7BB%7D%29%5E%7B%5Cfrac%7B1%7D%7Ba&plus;1%7D%7D,%28%5Cfrac%7BA-v%5E2%7D%7BB%7D%29%5E%7B%5Cfrac%7B1%7D%7Ba&plus;1%7D%7D%29
  [4]: http://latex.codecogs.com/gif.latex?%28-%28%5Cfrac%7BA%7D%7BB%7D%29%5E%7B%5Cfrac%7B1%7D%7Ba&plus;1%7D%7D,%28%5Cfrac%7BA%7D%7BB%7D%29%5E%7B%5Cfrac%7B1%7D%7Ba&plus;1%7D%7D%29
  [5]: http://latex.codecogs.com/gif.latex?%5Cpm%20x
  [6]: http://latex.codecogs.com/gif.latex?v_%7B0%7D%5E2&plus;%5Cfrac%7Bkx_%7B0%7D%5E%7Ba&plus;1%7D%7D%7Ba&plus;1%7D=A=%5Cfrac%7Bkx%5E%7Ba&plus;1%7D%7D%7Ba&plus;1%7D&plus;v%5E2=Bx%5E%7Ba&plus;1%7D&plus;v%5E2
  [7]: http://latex.codecogs.com/gif.latex?%5Cfrac%7BT%7D%7B2%7D=%20%5Cint_%7Bm%7D%5E%7B-m%7D%5Cfrac%7Bdx%7D%7B%5Csqrt%7BA-Bx%5E%7Ba&plus;1%7D%7D%7D,%20%28m=%28%5Cfrac%7BA%7D%7BB%7D%29%5E%7B%5Cfrac%7B1%7D%7Ba&plus;1%7D%7D%29
  [8]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/trajectory%20oscillation.png
  [9]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/period%20via%20order.png
  [10]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/new%20periods_amp%28low%29.png
  [11]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/new%20period_amp%28upper%29.png
  [12]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/new%20period_amp.png
  [13]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/oscillation_time.png
  [14]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/oscillation_time2.png
