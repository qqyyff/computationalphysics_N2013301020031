#the eleventh homework


###_Abstract_
######Use principally the Newton's gravitation law to study the solar system. We focus on the three problems,first,simulating the two body locomotion problem; second, investigating the inverse-square force law precisely and see the variation change with the ellipticity; third, using the general relativity adjust the force law and then study the mercury precession, see the variation of eccentricity versus precession angular speed.
###the fundamental principle
###### the classical gravitation model is simply decompose the force on X,Y directions. 
######![此处输入图片的描述][1]![此处输入图片的描述][2]
######in order to study the two body problem, we simply let the previous fixed object be free. The key ideas there is to set the correct initial conditions.we let the initial speed perpendicular to the line cross two objects and let the mass ratio of two objects be different.
###### Bying doing some slightly change on the order of the r:![此处输入图片的描述][3]![此处输入图片的描述][4] 
######we can say the precession of the ellipse orbit. we will say that the change of the ellipticity can be achieved by adjust the initial speed, different speed correspond to be differernt.and say under the different ellipticity ,the rotation speed of the whole ellipse orbit is different.
###### Under the adjustment of the general relativity, the force law becomes:  ![此处输入图片的描述][5]Thus by the Kepler second law and conservation of energy, we can build a relation between the eccentricity and the initial speed( we choose the initial location at the perihelion).![此处输入图片的描述][6], Then we can change the initial speed to change the eccentricity.
###the numerical result
######the two body problem:
######![此处输入图片的描述][7]
######the final situation represent the speed exceed the escape velocity. the first and third situations equals to the mass center with novanishing speed.
######the stability of the orbit with slight change in the force law.
######![此处输入图片的描述][8]
######![此处输入图片的描述][9]（the initial speed is 0.9 previous situation) 
######![此处输入图片的描述][10]（the initial speed is 0.8 previous situation) 
######the precession versus time
######![此处输入图片的描述][11]
######![此处输入图片的描述][12]
######![此处输入图片的描述][13]
######![此处输入图片的描述][14]


######the precession speed versus the eccentricity. there is some problem occur in the range of 0.8 of eccentricity,the trajectory becomes a line and when i do simulation in the e=0.7988, i find sometimes the results is normally some rotated elliptical trajectory and sometimes it is the straight line. 
######the x-axis is the eccentricity,Y-axis is the precession![此处输入图片的描述][15]
######![此处输入图片的描述][16]
######![此处输入图片的描述][17]
######we can see when the eccentricity bigger than 0.65. the unstability occurs. we then do some more precise simulation.
######![此处输入图片的描述][18]
######it even have more detailed structure:
######![此处输入图片的描述][19]
######![此处输入图片的描述][20]
######then we study the trajectory to say whether these instability is true.
######![此处输入图片的描述][21]
######![此处输入图片的描述][22]
######![此处输入图片的描述][23]
######we can say at e=0.7979731,the precession speed vanishes.
###the code
######[problem1](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp29.py)
######[problem2(1)](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp31.py)
######[problem2(2)](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp32.py)
######[problem2(3)](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp33.py)
######[problem3](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp34.py)
##Reference
######《Python基础教程》(第二版）[挪]Magnus Lie Hetland著



  


  [1]: http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdx%7D%7Bdt%7D=v_%7Bx%7D,%5Cfrac%7Bdv_%7Bx%7D%7D%7Bdt%7D=-%5Cfrac%7B4%7B%5Cpi%5E2%7Dx%7D%7Br%5E3%7D
  [2]: http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdy%7D%7Bdt%7D=v_%7By%7D,%5Cfrac%7Bdv_%7By%7D%7D%7Bdt%7D=-%5Cfrac%7B4%7B%5Cpi%5E2%7Dy%7D%7Br%5E3%7D
  [3]: http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdx%7D%7Bdt%7D=v_%7Bx%7D,%5Cfrac%7Bdv_%7Bx%7D%7D%7Bdt%7D=-%5Cfrac%7B4%7B%5Cpi%5E2%7Dx%7D%7Br%5E%7B2&plus;%5Cbeta%7D%7D
  [4]: http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdy%7D%7Bdt%7D=v_%7By%7D,%5Cfrac%7Bdv_%7By%7D%7D%7Bdt%7D=-%5Cfrac%7B4%7B%5Cpi%5E2%7Dy%7D%7Br%5E%7B2&plus;%5Cbeta%7D%7D
  [5]: http://latex.codecogs.com/gif.latex?F_%7BG%7D=-%5Cfrac%7BGM_%7BS%7DM_%7BM%7D%7D%7Br%5E2%7D%281&plus;%5Cfrac%7B%5Calpha%7D%7Br%5E2%7D%29
  [6]: http://latex.codecogs.com/gif.latex?v_%7B1%7D=%5Csqrt%7B%5Cfrac%7BGM_%7BS%7D%281-e%29%7D%7Ba%281&plus;e%29%7D%7D
  [7]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/two%20body%20gravitation.png
  [8]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/precession%20mercury.png
  [9]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/precession%20a%200.9.png
  [10]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/precession%20a%200.8.png
  [11]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/precession%20mercury2.png
  [12]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/precession%20theta_time.png
  [13]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/precession%20w_a.png
  [14]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/precession%20mercury1.png
  [15]: http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D
  [16]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/eccentricity%20speed.png
  [17]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/eccentricity%20truth.png
  [18]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/eccentricity%20truth2.png
  [19]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/eccentricity%20truth3.png
  [20]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/eccentricity%20truth4.png
  [21]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/eccentricity.png
  [22]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/eccentricity3.png
  [23]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/eccentricity8.png