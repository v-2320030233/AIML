#from matplotlib import pyplot as plt
#plt.plot([1,2,3],[2,3,2])
#plt.show()

"""x = [5,2,7]
y = [2,16,4]
plt.plot(x,y)
plt.title('dikkumalina caale_G')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()"""

import matplotlib.pyplot as plt
population_age = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55]
bins = [0,10,20,30,40,50]
plt.hist(population_age, bins, histtype='barstacked', rwidth=0.8, color='violet')


plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.title('Histogram',color= 'cyan')
plt.show()