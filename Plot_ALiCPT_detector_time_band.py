import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

nd_per_module_ali = 1712*4
nd_per_module_bicep = 2560
yield_ali_min = 12/24.*0.5
yield_ali_max = 16/24.*0.5
yield_bicep = 0.5


# begin year is 2016
year_begin = 2016
dt_ali_min_list = []
dt_ali_max_list = []
dt_bicep_list = []
dt_ali1_min_list = []
dt_ali1_max_list = []
dt_bicep3_list = []
year_list = []
dt_bicep=0
dt_ali_min=0
dt_ali_max=0
dt_ali1_min=0
dt_ali1_max=0
dt_bicep3=0
for year in range(2017,2035):
	#year = year_begin+nyear-1
	if year<2019:
		nd_bicep = nd_per_module_bicep
	elif year==2019:
		nd_bicep = 2*nd_per_module_bicep
	else:
		nd_bicep = 4*nd_per_module_bicep
	dt_bicep = dt_bicep+nd_bicep*yield_bicep
	print(year)
	print(nd_bicep)
	dt_bicep_list.append(dt_bicep)
	dt_bicep3 = dt_bicep3+nd_per_module_bicep*yield_bicep
	dt_bicep3_list.append(dt_bicep3)
	if year>=2020:
		dt_ali1_min = dt_ali1_min+nd_per_module_ali*yield_ali_min
		dt_ali1_max = dt_ali1_max+nd_per_module_ali*yield_ali_max
		dt_ali1_min_list.append(dt_ali1_min)
		dt_ali1_max_list.append(dt_ali1_max)
	if year>=2020 and year<=2023:
		nd_ali = nd_per_module_ali*(year-2019)
		print(nd_ali)
		dt_ali_min = dt_ali_min+nd_ali*yield_ali_min
		dt_ali_min_list.append(dt_ali_min)
		dt_ali_max = dt_ali_max+nd_ali*yield_ali_max
		dt_ali_max_list.append(dt_ali_max)
	elif year>2023:
		nd_ali = nd_per_module_ali*4
		dt_ali_min = dt_ali_min+nd_ali*yield_ali_min
		dt_ali_min_list.append(dt_ali_min)
		dt_ali_max = dt_ali_max+nd_ali*yield_ali_max
		dt_ali_max_list.append(dt_ali_max)
		print(nd_ali)
		
	year_list.append(year)

dt_ali_min_array = np.array(dt_ali_min_list)
dt_ali_max_array = np.array(dt_ali_max_list)
dt_bicep_array = np.array(dt_bicep_list)
dt_ali1_min_array = np.array(dt_ali1_min_list)
dt_ali1_max_array = np.array(dt_ali1_max_list)
dt_bicep3_array = np.array(dt_bicep3_list)
year_array = np.array(year_list)
#print(year_array)
#print(dt_ali_array)
#print(dt_bicep_array)


fig,ax = plt.subplots(1,1)
#plt.plot(year_array[3:],dt_ali_array,label='AliCPT')
ax.fill_between(year_array[3:],dt_ali_min_array,dt_ali_max_array,facecolor='blue',label='AliCPT',alpha=0.7)
ax.fill_between(year_array[3:],dt_ali1_min_array,dt_ali1_max_array,facecolor='red',label='AliCPT1',alpha=0.7)
BICEP = plt.plot(year_array,dt_bicep_array,label='BICEP3+BICEP Array',lw=4,color='red',ls='--')
#plt.plot(year_array[3:],dt_ali1_array,label='AliCPT1')
BICEP3 = plt.plot(year_array,dt_bicep3_array,label='BICEP3',lw=4,color='blue',ls='--')
plt.xlim(2016,2030)
plt.ylim(0,60000)
p1 = Rectangle((0, 0), 1, 1, fc="blue",alpha=0.7)
p2 = Rectangle((0, 0), 1, 1, fc="red",alpha=0.7)

plt.legend([p1, p2, BICEP[0], BICEP3[0]], ['AliCPT-1+AliCPT-2', 'AliCPT-1','BICEP3+BICEP Array','BICEP3'],loc='upper left')
plt.xlabel('Year')
plt.ylabel('Detector Year')
#plt.legend(loc='upper left')
#plt.show()
plt.savefig('Detector_Year.png',dpi=200)
