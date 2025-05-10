# CREATION OF DIFFERENT TYPES OF PLOT USING MATPLOTLIB
# LINE PLOT
# BAR PLOT
# SCATTER PLOT
# HISTOGRAM
# CREATION OF DIFFERENT TYPES OF PLOT USING MATPLOTLIB
# LINE PLOT
# BAR PLOT
# SCATTER PLOT
# HISTOGRAM
# BOX PLOT

import pandas as pd
import matplotlib.pyplot as plt
                              

#                                                         #LINE PLOT
#         # PLOT USING NORMAL DATA
#                  # METHOD 1
# plt.plot([1,2,3,4] ,[2,3,4,6] ,'r--') 
# plt.plot([8,4,5,6,] ,[2,3,4,6] ,'g^') 
# plt.plot([11,22,33,44] ,[1,2,3,4] ,'bo') 
# plt.plot([11,22,33,44] ,[1,2,3,4] ,'ys') 

# # line plot has PARAMETERS of (color(red , green  , blue ,  yellow) and shape(triangle , dot , line , star , square) )
# # [1,2,3,4] ,[2,3,4] x and y must have same first dimension

# # give name to the data set use label
# plt.xlabel("SET A")
# plt.ylabel("SET B")

# # suptitle will give the heading to plot
# plt.suptitle("LINE PLOT OF A AND B")
# plt.show()

#                  # METHOD 2
# x = [90, 91, 33]
# y = [11 ,22 ,33]
# plt.plot(x,y)
# plt.xlabel("SET A")
# plt.ylabel("SET B")
# plt.suptitle("LINE PLOT OF A AND B")
# plt.show()

# # # # simple charts work with all color and shapes to show and show() func will enable to see on screen , plot will make the plot of data sets 
                            
#         # PLOT USING CSV DATA

# # for using csv file .. first read it through pandas and then implement matplotlib func
# air = pd.read_csv("air.csv")
# titanic = pd.read_csv("titanic.csv")

# plt.plot(air["station_london"] , air["station_paris"] , 'g^' )
# plt.show()


#                                                          #BAR PLOT
#       # PLOT USING NORMAL DATA
# plt.bar([11,22,33] , [99,88,77] ,color='r', width=3 )
# plt.show()
# # # bar plot has parameters of color , width , alignment , height , aplha value ( to smooth the colors of bars)

#       # PLOT USING CSV DATA
# plt.bar(titanic["Survived"] , titanic["Age"])
# plt.show()


#                                                         #  SCATTER PLOT
# plt.scatter([90,91,92,93] , [30,31,32,33] , marker="*")
# plt.show()
# # # scatter plot has PARAMETERS of markers(include style i.e star , triangle etc , edge color)



#                                                        # HISTOGRAM 
# plt.hist([1,2,1], density=True , histtype='stepfilled',color='red')
# plt.show()
# # # we will specify some of parameterslike(histogram type (stack , stepfilled,bar , barstack) ,density and which you have to given , orientation , alignment etc)


                                                         #BOXPLOT
# plt.boxplot([11,22,33] , [44,66,77])
# plt.show()


#                                                         # PIE CHART
# c = ['r' , 'y' , 'g' ,'b']
# plt.pie([10,20,30,40,50], colors=c ,labels=["ten" , "twenty" , "thirty" , "forty" ," fifty"])
# plt.show()
# # pie chart has PARAMETERS OF lables , color , radius , counterclock ,    startangle)
import pandas as pd
import matplotlib.pyplot as plt
                              

        #LINE PLOT
                           # PLOT USING NORMAL DATA
# # [1,2,3,4] ,[2,3,4] x and y must have same first dimension
# plt.plot([1,2,3,4] ,[2,3,4,6] ,'r--') 
# plt.plot([8,4,5,6,] ,[2,3,4,6] ,'g^') 
# plt.plot([11,22,33,44] ,[1,2,3,4] ,'bo') 
# plt.xlabel("SET A")
# plt.ylabel("SET B")
# # label will name the data-set
# plt.suptitle("LINE PLOT OF A AND B")
# # # suptitle will give the heading to plot
# plt.show()
# # simple charts work with all color and shapes to show and show() func will enable to see on screen , plot will make the plot of data sets 
                            
                            # PLOT USING CSV DATA

air = pd.read_csv("air.csv")
titanic = pd.read_csv("titanic.csv")

# plt.plot(air["station_london"] , air["station_paris"] , 'gs')
# plt.show()

#         #BAR PLOT
#                            # PLOT USING NORMAL DATA
# plt.bar([11,22,33] , [99,88,77] , align='center')
# plt.show()
# # bar plot doesnot use any parameters of color and shape but can use other parameters like alignment 

#                               # PLOT USING CSV DATA
plt.bar(titanic["Survived"] , titanic["Age"])
plt.show()
#         # SCATTER PLOT
#                             # PLOT USING NORMAL DATA
# plt.scatter([90,91,92,93] , [30,31,32,33])
# plt.show()
# # scatter plot doesnot use any parameters of color and shape

#         # HISTOGRAM 
# plt.hist([1,2,1], density=True , histtype='stepfilled',color='red')
# plt.show()
# # we will specify some of parameterslike(histogram type (stack , stepfilled,bar , barstack) ,density and which you have to given)








 
