# the twelfth homework

标签（空格分隔）： 未分类
##the three body problem

###_Abstract_
######when we rise the object we deal with in a gravitational problem from two to three even more. We will find quickly that the current problem can not generally be solved analytically. this is the famous three body problem. As a result we begin to do it numerically.
###the basic principle
######We only deal with the sun-jupiter-earth model and make it by two steps. first ,let the sun fixed,only care about the motion of the sun and jupiter, the initial conditions we use is based on the real situation. First the orbit is the same with the real situation: set the sun at the origin, the earth be 1AU, the jupiter 5.2AU. The initial speed is based on the equation ![此处输入图片的描述][1]
######the e is the ellipticality.
######Then to make the chaotic phenomenon obvious, we let the mass of jupiter increase and will say the orbit of earth gradually changed.
######Second, we begin to add the motion of sun to our consideration. then we the origin be the mass center of this problem(the location of origin will be different, if we change the mass of the jupiter.). At this time we set the initial speed of the sun to make the speed of the mass center to zero. Like the previous situation, we alter the mass of the jupiter to say the change. 
######We also considered the influence of jupiter on the motion of the asteriod in different radius. We measure the effect by the eccentricity of the asteriod's orbit, the larger the eccentircity finally is ,the larger the effect is. 
###the numerical result
######![此处输入图片的描述][2]
###[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp35.py)
######we can say when the mass of jupiter become large the chaotic phenomenon appears.
######then we add the motion of the sun and then solely study the motion of the earth.
######![此处输入图片的描述][3]
######![此处输入图片的描述][4]
######![此处输入图片的描述][5]
###[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp36.py)
######the situaition of the earth motion know is rather complex. We only pick some particular initial conditions here.(all these satisfy make the totally momentum to zero)
######the effect on the asteriod
######![此处输入图片的描述][6]
######![此处输入图片的描述][7]
###[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp41.py)
######to say exactly the true orbit of the asteriod in some radius(to determine whether the previous is meaningful)
######![此处输入图片的描述][8]
######the same situation on the textbook
######![此处输入图片的描述][9]
###[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp42.py)
###Reference
######Computational Physics, Nicholas J. Giordano & Hisao Nakanishi

######《Python基础教程》


  [1]: http://latex.codecogs.com/gif.latex?v=%5Csqrt%7B%5Cfrac%7BGM_%7BS%7D%281-e%29%7D%7Ba%281&plus;e%29%7D%7D
  [2]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/MJjupiter.png
  [3]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/400MJjupiter.png
  [4]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/245MJjupiter.png
  [5]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/265MJjupiter.png
  [6]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/asteriod1.png
  [7]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/asteriod2.png
  [8]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/asteriod3.png
  [9]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/asteriod4.png