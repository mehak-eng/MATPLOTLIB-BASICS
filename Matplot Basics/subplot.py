# USE OF SUBPLOT
# USE OF SUBPLOTS

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import subplots


    #  CREATION OF SUBPLOT OF MANY DATASETS

# For showing 2 or more plot together ..one by one 

students = ["stu1" ,"stu2","stu3"]
marks = [33,34,39]

plt.subplot(121)
# they can written also plt.subplot(1,2,1)
plt.bar(students, marks)

plt.subplot(122)
plt.scatter(students , marks)

plt.show()

        # CREATION OF SUBPLOTS USING INDEX OF PLOTS

# to access the plot using index and assign the plot values 

food = ["chips" , "drink" ,"jelly" , "candy" ,"cookies"]
price = [120, 100, 75, 20,300]

# simply shows the the divison of plots how many rows and cols they have
fig , axes = plt.subplots(2 , 2 )

# to give the space from 1 plot to other use padding 
plt.tight_layout(pad=2.4)

axes[0,0].plot(food , price , 'r--')
axes[0,0].set_title("LINE PLOT")

axes[0,1].scatter(food , price)
axes[0,1].set_title("SCATTER PLOT")

axes[1,0].bar(food , price)
axes[1,0].set_title("BAR PLOT")

axes[1,1].hist(price,)
axes[1,1].set_title("HISTOGRAM")

plt.show()

