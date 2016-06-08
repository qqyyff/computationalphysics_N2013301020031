# the fourteenth homework

标签（空格分隔）： wave

---

###Abstract
######To solve the ideal wave equation(one dimension) ![此处输入图片的描述][1], then set the different initial conditions to the whole string vary via time. Then choose one pointer on the string to observe its vibration via time. Finally, add some damp influence of the string's stiffness into the equation to make the model more realistic.
###the fundamental principle
###### ![此处输入图片的描述][2],to solve these equation we need to discrete the partial differential into the interation equation. We set the time t as ![此处输入图片的描述][3], then divide the whole string into N parts and use i to represent ith parts. then we will get:[此处输入图片的描述][4]the r in this equation is[此处输入图片的描述][5]. In order to match the variation of propagation of wave, we set the r=1.
######then we set the point at the 0.05 length away from edge to see its vibration. then we do FFT to it signal and get its power spectrum. In this situation, we set the c=300m/s, the string is 2m and  ![此处输入图片的描述][6]so that we can determine ![此处输入图片的描述][7]. We have set two different conditions, one is Guassian wave packet,the other is that string is plucked at the middle.
######to make the situation more approach to reality, we add the damp into the ideal wave equation. ![此处输入图片的描述][8]which the ![此处输入图片的描述][9]is the dimensionless stiffness parameter. then with the similar procedure, we obtain the iteration equation. ![此处输入图片的描述][10]then we set the different stineffness parameter to observe the more realistic condition to different instrument.
###the numerical result
######we set a Guassian in the middle of the string and from top to bottom is the time sequence.
#####![此处输入图片的描述][11]
######the vibration of a point near the edge.
######![此处输入图片的描述][12]
######we then set two Guassian on the string with the same amplitude. 
#####![此处输入图片的描述][13]
######the vibration of a point near the edge.
#####![此处输入图片的描述][14]
######different amplitude
#####![此处输入图片的描述][15]
######then we study the real intial condition(a pluck at 0.5)
######![此处输入图片的描述][16]
######compare two condition of the vibration of a point near the edge.
#####![此处输入图片的描述][17]
######then we study the power spectrum of two conditions 
#####![此处输入图片的描述][18]
#####to see the real stirng with damp
![此处输入图片的描述][19]
######the stiffness parameter is different, one is 0.000001,one is 0.00002
######compare the ideal vibration with the damp one
####![此处输入图片的描述][20]
######we discover the different kind of real instrument's power spectrum.
######![此处输入图片的描述][21]
###the code
######[code1](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp48.py)
######[code2](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp49.py)
######[code3](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp51.py)
######[code4](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp52.py)
###Reference
######Computational Physics, Nicholas J. Giordano & Hisao Nakanishi
######《Python基础教程》


  [1]: http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2y%7D%7B%5Cpartial%7Bt%5E2%7D%7D=c%5E2%7B%7D%5Cfrac%7B%5Cpartial%5E2y%7D%7B%5Cpartial%7Bx%5E2%7D%7D
  [2]: http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2y%7D%7B%5Cpartial%7Bt%5E2%7D%7D=c%5E2%7B%7D%5Cfrac%7B%5Cpartial%5E2y%7D%7B%5Cpartial%7Bx%5E2%7D%7D
  [3]: http://latex.codecogs.com/gif.latex?t_%7Bn%7D=n%5CDelta%20t
  [4]: http://latex.codecogs.com/gif.latex?y%28i,n&plus;1%29=2%5B1-r%5E2%5Dy%28i,n%29-y%28i,n-1%29&plus;r%5E2%5By%28i&plus;1,n%29&plus;y%28i-1,n%29%7D
  [5]: http://latex.codecogs.com/gif.latex?r=c%5CDelta%20t/%5CDelta%20x
  [6]: http://latex.codecogs.com/gif.latex?%5CDelta%20x=0.01m
  [7]: http://latex.codecogs.com/gif.latex?%5CDelta%20t=%5CDelta%20x/%28rc%29
  [8]: http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2y%7D%7B%5Cpartial%7Bt%5E2%7D%7D=c%5E2%7B%5Cfrac%7B%5Cpartial%5E2y%7D%7B%5Cpartial%7Bx%5E2%7D%7D-%5Cepsilon%20L%5E2%20%5Cfrac%7B%5Cpartial%5E4y%7D%7B%5Cpartial%7Bx%5E4%7D%7D%7D
  [9]: http://latex.codecogs.com/gif.latex?%5Cepsilon
  [10]: http://latex.codecogs.com/gif.latex?y%28i,n&plus;1%29=2%5B2-2r%5E2-6%5Cepsilon%20M%5E2%5Dy%28i,n%29-y%28i,n-1%29&plus;r%5E2%5B1&plus;4%5Cepsilon%20M%5E2%5D%5By%28i&plus;1,n%29&plus;y%28i-1,n%29%7D-2r%5E2%20%5Cepsilon%20M%5E2%5By%28i&plus;2,n%29&plus;y%28i-2,n%29%5D
  [11]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/wave%20propagation.png
  [12]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/guassian%20vibration.png
  [13]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/two%20summit.png
  [14]: ######the%20vibration%20of%20a%20point%20near%20the%20edge.
  [15]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/two%20summitd.png
  [16]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/straight%20line1.png
  [17]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/vibration%20of%20two%20kinds.png
  [18]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/real%20real.png
  [19]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/vibration%20damp.png
  [20]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/vibration%20damp2.png
  [21]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/power%20spectrum%20C.png