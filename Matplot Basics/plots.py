# CREATION OF DIFFERENT TYPES OF PLOT USING MATPLOTLIB
# LINE PLOT
# BAR PLOT
# SCATTER PLOT
# HISTOGRAM

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








 