# Random systems
---
#####作者：强雨，学号:2013301020031，班级：13级弘毅班
##Abstract
######Since the random systems can not be determined or predicted by the initial conditions, in order to  have a rough understanding on the random systems such as diffusion processes, we explore various kinds of random walk model, and investigate some properties of them which can be meaningful in some random systems as well.
##Introduction
######We mainly consider the random walk model in one and two dimensions with some different approaches. We have mainly calculated the main square distance varies with time. In the self-avoiding walk we also investigate the standard deviation of the square distance varies with time. After that we set up a partial differential equation diffusion model and compare it with the previous random walk model. Finally, consider the entropy varies with time by random walk approach in the cream in coffee problem.
###random walk in one dimension 
######random walk means the walk direction is totally deterimined by probability, we set up a random number seed to generate a random number in the section between 0 and 1 and to let the particle's probability for move left and right be same, if the number bigger than 0.5 then right ,otherwise, left.  Here we convey the model into two ways, one is step length fixed as one which means in any step the change of the particle's location can only be one. The other is step length unfixed. In this case, we transform the random number in section [0,1] to the section [-1,1] and set the result as the step length. 
######![此处输入图片的描述][1]
######this is two samples for step length fixed approach. Honestly,each this kind of line is unique, once we repeat the program the result can be very different with this one. 
######![此处输入图片的描述][2]
######this is two samples for step length unfixed approach. the x increasing speed is smaller than the previous one.
######then we consider the average of square distance vaies with time. Since we have built a list to store the location of one particle in different time, all we have to do now is produce a large number of random moving particles(repeat the previous process many times) and average the final results.due to the equation ![此处输入图片的描述][3], we will investigate the D value of two different approaches.
######![此处输入图片的描述][4]
######this is the line for step length fixed approach, there are two kinds of spots in the diagram. The green one is the average for 20000 times and the orange one is the average for 2000 times. we can say some fluctuation on the orange spots but dispear when the average sample become large. the fitting line is y=1.004*x-0.0337.So the D value is 0.502
######![此处输入图片的描述][5]
######this is the line for step length unfixed approach, it is obvious that the distance increasing speed is smaller than the previous one and the D value is approximately 0.1677. 
######[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp53.py)
######[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp54.py)
###self-avoiding walk
######To investigate the shape of the  macromolecule it is line-shaped,but can not intersect which means in one location can only be occupied once. We only investigate the two dimension SAW. In this case,we devise the SAW model, that is the path of the random walk particle will not pass the location which it has passed before. To accomplish this target, we must scan the location of the previous steps to see whether it has occupied the four location adjacent to the present particle location. if some has been taken up,the particle now can not pass them.
######there are two methods to achieve this goal: one is simulation the other is enumeration. Simulation is first produce many random walk path step by step and if it has been self-intersect, then abandon them, so the rest can be all SAW path. Enumeration is the method to list the possible SAW path step by step.  
######simulation approach,we finally get more than 200 SAW path in step 50, and get their average square distance. Due to the relation:![此处输入图片的描述][6] we exam the exact value of the v.
######![此处输入图片的描述][7]
######we do a log-log fit to the equation ![此处输入图片的描述][8],and get that v value is :0.94462. There are some deviation for this results and the result on textbook, the value I get is larger than the textbook, I think this leads to the v value become larger than its standard value 0.75. However, I check my program and don't find some problem and the value doesn't change when I increase the number of average sample. 
######[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp55.py)
######enumeration approach, we use the previous scanning principle step by step to get the all possible path of SAW. Due the large number of calculation, we only do ten step. And our result perfectly agree with the list on the textbook. Since the average square distance has the relation:![此处输入图片的描述][9]
######![此处输入图片的描述][10]
######this is the results by averaging all possible SAW path step by step
######![此处输入图片的描述][11]
######we can say the number of possible SAW path increase rapidly versus time and that is the reason for I only do 11 steps.
######due to this relation:![此处输入图片的描述][12]:
######![此处输入图片的描述][13]
######the equation of the fitting line is y=1.666/n+0.9654, So the v value is 0.833
######[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp56.py)
### partial differential model
######by analyzing the iteration of particle moving probability, we derive :![此处输入图片的描述][14] Then by discreting, we get :![此处输入图片的描述][15]
###### We set an sharp Guassian in the center as a initial  conditions, then we can see the time evolution.
######![此处输入图片的描述][16]
######This time, we set the D value as 1.0.
######[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp57.py)
######Now we set all particle at the center at the beginning, then let them do random walk in one dimension, after some steps we can say the result is somehow similar to the previous one, which means random walk model is feasible to deal with  diffusion problem.
######![此处输入图片的描述][17]
######the time step for every one subplot is the same with the previous Guassian one. And we can see they are somehow adjacent.
######[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp58.py)
###cream in coffee problem.
###### we consider it as two dimension random walk problem. First we set a number of particle in the center of the whole area which is shaped as a square. Then let them do random walk to up,down,left and right four direction. The only limit is once they are reach the edge of the area they can not pass it. Then we observe the whole random particle picture in different time.  
######![此处输入图片的描述][18]
######this time, we consider an area of 128*128, and only the center area (16,16) has been occupied by the particle initially. the time sequence for eight subplot is not even. they are (0,10,100,500,1000,2000,4000,8000)
######[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp59.py)
######Now its time for us to derive some useful information from this seemingly disordered system. The entropy, to deal with this we have applied a different sumulation method with the above one.
######First, we set one particle at the center of the area and let it do the random walk step by step. Each step we will do 5000 times which means there are 5000 particles in the center of the area. Then we add the times of being occupied for every point in this area in 5000 times, so we derive the probability for each state(point) and then use the equation:![此处输入图片的描述][19](the sum is over all point in the area)we get the result.
######![此处输入图片的描述][20]
######we have done 640 steps this time, and the entropy is increase as the time goes on just like we expect.
######[the code](https://github.com/qqyyff/computationalphysics_N2013301020031/blob/master/cp60.py)
###conclusion 
######By exploring several kinds of random walk model,we can say that it is a good approximation for many random system to some extent. It reveals the essence of this kind system in some way. However, to derive the real situation, we can not omit the interaction between the particles. Once we add this factor in into the simulation, there is no doubt that the result will appeal to reality, but just like the SAWs, the calculation will become severely large as the time step increase. 
###Reference
######Computational Physics, Nicholas J. Giordano & Hisao Nakanishi
######《Python基础教程》


  [1]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/random%20walk%20in%20one%20dimesion%20f1.png
  [2]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/random%20walk%20in%20one%20dimension%20uf2.png
  [3]: http://latex.codecogs.com/gif.latex?%3Cx%5E2%3E=2Dt
  [4]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/random%20in%20one%20dimesion%20f.png
  [5]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/random%20walk%20in%20one%20dimension%20uf.png
  [6]: http://latex.codecogs.com/gif.latex?%3Cr%5E2%3E=At%5E%7B2%5Cnu%7D
  [7]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/SAW%20simulation%201.88924281.png
  [8]: http://latex.codecogs.com/gif.latex?%3Cr%5E2%3E=At%5E%7B2%5Cnu%7D
  [9]: http://latex.codecogs.com/gif.latex?%5Cfrac%7B%3Cr_%7Bn&plus;1%7D%5E2%3E%7D%7B%3Cr_%7Bn%7D%5E2%3E%7D%5Csim%201&plus;%5Cfrac%7B2%5Cnu%7D%7Bn%7D
  [10]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/SAW3.png
  [11]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/SAW5.png
  [12]: http://latex.codecogs.com/gif.latex?%5Cfrac%7B%3Cr_%7Bn&plus;1%7D%5E2%3E%7D%7B%3Cr_%7Bn%7D%5E2%3E%7D%5Csim%201&plus;%5Cfrac%7B2%5Cnu%7D%7Bn%7D
  [13]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/random%20fitting.png
  [14]: http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5Crho%7D%7B%5Cpartial%7Bt%7D%20%7D=D%5Cfrac%7B%5Cpartial%5E2%5Crho%7D%7B%5Cpartial%7Bx%5E2%7D%20%7D
  [15]: http://latex.codecogs.com/gif.latex?%5Crho%28i,n&plus;1%29=%5Crho%28i,n%29&plus;%5Cfrac%7BD%5CDelta%7Bt%7D%7D%7B%5CDelta%7Bx%5E2%7D%7D%28%5Crho%28i&plus;1,n1%29&plus;%5Crho%28i-1,n%29-2%5Crho%28i,n%29%29
  [16]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/diffusion1.png
  [17]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/diffusion2.png
  [18]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/diffusion5.png
  [19]: http://latex.codecogs.com/gif.latex?S=-%5Csum%20_%7Bi%7DP_%7Bi%7DlnP_%7Bi%7D
  [20]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/random%20entropy.png