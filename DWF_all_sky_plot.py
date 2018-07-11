import numpy as np
import matplotlib.pyplot as plt
import ephem 
import math

#--- RA and DEC must be values Ra=[0, 360] Dec=[-90,90] 
#--- org is the origin is the origin of the plot, 0 or a multiple of 30 degrees
#--- give figure a title 
#--- project types hammer, mollweide, aitoff or lambert 



##---------------- to plot just one data set ----------------------### 
def plot_mwd(RA, Dec, title, projection, marker_color):
    x = np.remainder(RA+360-0,360) # shift RA values
    ind = x>180
    x[ind] -=360    # scale conversion to [-180, 180]
    x=x    # reverse the scale: East to the left
    #tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
    #tick_labels = np.remainder(tick_labels+360+0,360)
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111, projection= projection)
    #ax.scatter(x,Dec, color = marker_color , marker = 'D', zorder = +999) # when already in radians 
    ax.scatter(np.radians(x),np.radians(Dec), color = marker_color , marker = 'D', zorder = +999)  # convert degrees to radians
    #ax.set_xticklabels(tick_labels)     # we add the scale on the x axis
    ax.set_title(title)
    ax.title.set_fontsize(15)
    ax.set_xlabel("RA")
    ax.xaxis.label.set_fontsize(12)
    ax.set_ylabel("Dec")
    ax.yaxis.label.set_fontsize(12)
    ax.grid(True)
    plt.savefig(title + 'pdf')
    #plt.show()
    
##----------------- to plot several fields and gal plane --------#### 
def plot_all( RA_plane, DEC_plane, marker_color_plane, Lplane, RA_1, Dec_1, marker_color1, L1,  RA_2, Dec_2, marker_color2 , L2,  RA_3, Dec_3, marker_color3, L3, RA_4, Dec_4, marker_color4 , L4, RA_5,Dec_5, marker_color5 , L5, RA_6, Dec_6, marker_color6, L6,  RA_7,Dec_7, marker_color7, L7 , org=0, title='Mollweide projection', projection='mollweide' ):
    
    xp = np.remainder(RA_plane+360-0,360) # shift RA values
    indp = xp>180
    xp[indp] -=360    # scale conversion to [-180, 180]
    xp=-xp   # reverse the scale: East to the left
    
    x1 = np.remainder(RA_1+360-0,360) # shift RA va
    
    ind1 = x1>180
    x1[ind1] -=360    # scale conversion to [-180, 18
    x1=x1   # reverse the scale: East to the left
    
    x2 = np.remainder(RA_2+360-0,360) # shift RA value
    ind2 = x2>180
    x2[ind2] -=360	 # scale conversion to [-180, 180]
    x2=x2   # reverse the scale: East to the left
    
    x3 = np.remainder(RA_3+360-0,360) # shift RA value
    ind3 = x3>180
    x3[ind3] -=360	 # scale conversion to [-180, 180]
    x3=x3   # reverse the scale: East to the left   
    
    x4 = np.remainder(RA_4+360-0,360) # shift RA value
    ind4 = x4>180
    x4[ind4] -=360	 # scale conversion to [-180, 180]
    x4=x4   # reverse the scale: East to the left 
    
    x5 = np.remainder(RA_5+360-0,360) # shift RA value
    ind5 = x5>180
    x5[ind5] -=360	 # scale conversion to [-180, 180]
    x5=x5   # reverse the scale: East to the left
    
    x6 = np.remainder(RA_6+360-0,360) # shift RA value
    ind6 = x6>180
    x6[ind6] -=360	 # scale conversion to [-180, 180]
    x6=x6   # reverse the scale: East to the left

    x7 = np.remainder(RA_7+360-0,360) # shift RA value
    ind7 = x7>180
    x7[ind7] -=360	 # scale conversion to [-180, 180]
    x7=x7   # reverse the scale: East to the left   
    
    
    #tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
    #tick_labels = np.remainder(tick_labels+360+0,360)
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111, projection=projection)
    ax.grid(True, zorder = -999)
    
    
    #ax.plot(xcp, dec_cp, 'g--', label= 'Celestial Equator', zorder = +999)
    ax.plot(np.radians(xp),np.radians(DEC_plane), 'k.', markersize=0.8, label= Lplane, zorder = +999)
    #ax.scatter(xcp,dec_cp, color = '', marker = '.', label= 'Celestial Equator', zorder = +999) #
    #ax.scatter(np.radians(xp),np.radians(DEC_plane), color = 'r', marker = '.', label= Lplane, zorder = +1)  # convert degrees to radians
    ax.scatter(np.radians(x1),np.radians(Dec_1), color = marker_color1 , marker = '*', label= L1, zorder = +999)  # convert degrees to radians
    ax.scatter(np.radians(x2),np.radians(Dec_2), color = marker_color2 , marker = '*', label=L2, zorder = +999)  # convert degrees to radians   
    ax.scatter(np.radians(x3),np.radians(Dec_3), color = marker_color3 , marker = '*', label=L3, zorder = +999)  # convert degrees to radians 
    ax.scatter(np.radians(x4),np.radians(Dec_4), color = marker_color4 , marker = '*', label=L4, zorder = +999)  # convert degrees to radians 
    ax.scatter(np.radians(x5),np.radians(Dec_5), color = marker_color5 , marker = '*', label=L5, zorder = +999)  # convert degrees to radians 
    ax.scatter(np.radians(x6),np.radians(Dec_6), color = marker_color6 , marker = '*', label=L6, zorder = +999)  # convert degrees to radians 
    ax.scatter(np.radians(x7),np.radians(Dec_7), color = marker_color7 , marker = '*', label=L7, zorder = +999)  # convert degrees to radians 
    
    #ax.set_xticklabels(tick_labels)     # we add the scale on the x axis
    ax.set_title("DWF Fields")
    ax.title.set_fontsize(15)
    ax.set_xlabel("RA")
    ax.xaxis.label.set_fontsize(12)
    ax.set_ylabel("Dec")
    ax.yaxis.label.set_fontsize(12)
    #ax.tick_params(axis='x', colors='white')
    
    ax.legend(bbox_to_anchor=(.95, .25), loc=2, borderaxespad=0. ,fontsize = 'x-small')
    plt.show()
    #plt.savefig("DWF_ALL_fig.pdf")
    #plt.savefig('colorchanged_allsky.png', transparent=True)

## ----------- non-projected fields on sqaure plot -----------------# 

def plot_all_NP(ra_cp, dec_cp, RA_plane, DEC_plane, marker_color_plane, Lplane, RA_1, Dec_1, marker_color1, L1,  RA_2, Dec_2, marker_color2 , L2,  RA_3, Dec_3, marker_color3, L3, RA_4, Dec_4, marker_color4 , L4, RA_5,Dec_5, marker_color5 , L5, RA_6, Dec_6, marker_color6, L6,  RA_7,Dec_7, marker_color7, L7 , org=0, title='Mollweide projection', projection='mollweide'):
	
    
    #ra_cp=-ra_cp   # reverse the scale: East to the left
    
    xp = np.remainder(RA_plane+360-0,360) # shift RA values
    indp = xp>180
    xp[indp] -=360    # scale conversion to [-180, 180]
    xp=-xp   # reverse the scale: East to the left
    
    x1 = np.remainder(RA_1+360-0,360) # shift RA va
    
    ind1 = x1>180
    x1[ind1] -=360    # scale conversion to [-180, 18
    x1=x1   # reverse the scale: East to the left
    
    x2 = np.remainder(RA_2+360-0,360) # shift RA value
    ind2 = x2>180
    x2[ind2] -=360	 # scale conversion to [-180, 180]
    x2=x2   # reverse the scale: East to the left
    
    x3 = np.remainder(RA_3+360-0,360) # shift RA value
    ind3 = x3>180
    x3[ind3] -=360	 # scale conversion to [-180, 180]
    x3=x3   # reverse the scale: East to the left   
    
    x4 = np.remainder(RA_4+360-0,360) # shift RA value
    ind4 = x4>180
    x4[ind4] -=360	 # scale conversion to [-180, 180]
    x4=x4   # reverse the scale: East to the left 
    
    x5 = np.remainder(RA_5+360-0,360) # shift RA value
    ind5 = x5>180
    x5[ind5] -=360	 # scale conversion to [-180, 180]
    x5=x5   # reverse the scale: East to the left
    
    x6 = np.remainder(RA_6+360-0,360) # shift RA value
    ind6 = x6>180
    x6[ind6] -=360	 # scale conversion to [-180, 180]
    x6=x6   # reverse the scale: East to the left

    x7 = np.remainder(RA_7+360-0,360) # shift RA value
    ind7 = x7>180
    x7[ind7] -=360	 # scale conversion to [-180, 180]
    x7=x7   # reverse the scale: East to the left   

   #tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
    #tick_labels = np.remainder(tick_labels+360+0,360)
    #fig = plt.figure(figsize=(10, 5))
    
    #fig.grid(True, zorder = -999)
    
    
    plt.plot(ra_cp, dec_cp, 'g--', label= 'Celestial Equator', zorder = +999)
    plt.scatter(xp, DEC_plane , color = 'k-', marker = '.',  label= Lplane, zorder = +999)
    #ax.scatter(xcp,dec_cp, color = '', marker = '.', label= 'Celestial Equator', zorder = +999) #
    #ax.scatter(np.radians(xp),np.radians(DEC_plane), color = 'r', marker = '.', label= Lplane, zorder = +1)  # convert degrees to radians
    plt.scatter(x1,Dec_1, color = marker_color1 , marker = '*', label= L1, zorder = +999)  # convert degrees to radians
    plt.scatter(x2,Dec_2, color = marker_color2 , marker = '*', label=L2, zorder = +999)  # convert degrees to radians   
    plt.scatter(x3,Dec_3, color = marker_color3 , marker = '*', label=L3, zorder = +999)  # convert degrees to radians 
    plt.scatter(x4,Dec_4, color = marker_color4 , marker = '*', label=L4, zorder = +999)  # convert degrees to radians 
    plt.scatter(x5,Dec_5, color = marker_color5 , marker = '*', label=L5, zorder = +999)  # convert degrees to radians 
    plt.scatter(x6,Dec_6, color = marker_color6 , marker = '*', label=L6, zorder = +999)  # convert degrees to radians 
    plt.scatter(x7,Dec_7, color = marker_color7 , marker = '*', label=L7, zorder = +999)  # convert degrees to radians 
    
    #ax.set_xticklabels(tick_labels)     # we add the scale on the x axis
    plt.title("DWF Fields")
    #plt.title.set_fontsize(15)
    plt.xlabel("RAJ2000 (degrees)")
    #plt.xaxis.label.set_fontsize(12)
    plt.ylabel("DecJ2000 (Degrees)")
    #plt.yaxis.label.set_fontsize(12)
    #plt.tick_params(axis='x', colors='white')
    
    plt.legend(bbox_to_anchor=(0.01, .99), loc=2, borderaxespad=0. ,fontsize = 'x-small')
    plt.show()
    #plt.savefig("DWF_ALL_fig_noprojection.pdf")
    #plt.savefig('.png', transparent=True)




###-----LOAD IN DWF FIELDS-------### 

ra_deg, dec_deg = np.loadtxt('/Users/swebb/Documents/DWF/sky_plots/DWF_fields_degree.txt', unpack = True, usecols=(3,4), skiprows=1)
field = np.genfromtxt('/Users/swebb/Documents/DWF/sky_plots/DWF_fields_degree.txt', unpack = True, skip_header=1, usecols=(0), dtype=np.str)
run = np.genfromtxt('/Users/swebb/Documents/DWF/sky_plots/DWF_fields_degree.txt', unpack = True, skip_header=1, usecols=(5), dtype=np.str)


data = {}

data["RA"] = ra_deg
data["DEC"] = dec_deg
data["field"] = field
data["run"] = run

jan2015_idx = np.where(data["run"] == "Jan2015")[0]

field_jan2015 = data["field"][jan2015_idx]
RA_jan2015 = data["RA"][jan2015_idx]
DEC_jan2015 = data["DEC"][jan2015_idx]
run_jan2015 = data["run"][jan2015_idx]

jan2015 = {}
jan2015["RA"]= RA_jan2015
jan2015["DEC"]= DEC_jan2015
jan2015["field"]= field_jan2015
jan2015["run"]= run_jan2015

#print(jan2015)


feb2015_idx = np.where(data["run"] == "Feb2015")[0]

field_feb2015 = data["field"][feb2015_idx]
RA_feb2015 = data["RA"][feb2015_idx]
DEC_feb2015 = data["DEC"][feb2015_idx]
run_feb2015 = data["run"][feb2015_idx]

feb2015 = {}
feb2015["RA"]= RA_feb2015
feb2015["DEC"]= DEC_feb2015
feb2015["field"]= field_feb2015
feb2015["run"]= run_feb2015


dec2015_idx = np.where(data["run"] == "Dec2015")[0]

field_dec2015 = data["field"][dec2015_idx]
RA_dec2015 = data["RA"][dec2015_idx]
DEC_dec2015 = data["DEC"][dec2015_idx]
run_dec2015 = data["run"][dec2015_idx]

dec2015 = {}
dec2015["RA"]= RA_dec2015
dec2015["DEC"]= DEC_dec2015
dec2015["field"]= field_dec2015
dec2015["run"]= run_dec2015



jul2016_idx = np.where(data["run"] == "Jul2016")[0]

field_jul2016 = data["field"][jul2016_idx]
RA_jul2016= data["RA"][jul2016_idx]
DEC_jul2016 = data["DEC"][jul2016_idx]
run_jul2016 = data["run"][jul2016_idx]

jul2016 = {}
jul2016["RA"]= RA_jul2016
jul2016["DEC"]= DEC_jul2016
jul2016["field"]= field_jul2016
jul2016["run"]= run_jul2016


feb2017_idx = np.where(data["run"] == "Feb2017")[0]

field_feb2017 = data["field"][feb2017_idx]
RA_feb2017= data["RA"][feb2017_idx]
DEC_feb2017 = data["DEC"][feb2017_idx]
run_feb2017 = data["run"][feb2017_idx]

feb2017= {}
feb2017["RA"]= RA_feb2017
feb2017["DEC"]= DEC_feb2017
feb2017["field"]= field_feb2017
feb2017["run"]= run_feb2017





feb2018_idx = np.where(data["run"] == "Feb2018")[0]

field_feb2018 = data["field"][feb2018_idx]
RA_feb2018= data["RA"][feb2018_idx]
DEC_feb2018 = data["DEC"][feb2018_idx]
run_feb2018 = data["run"][feb2018_idx]

feb2018= {}
feb2018["RA"]= RA_feb2018
feb2018["DEC"]= DEC_feb2018
feb2018["field"]= field_feb2018
feb2018["run"]= run_feb2018





jun2018_idx = np.where(data["run"] == "Jun2018")[0]

field_jun2018 = data["field"][jun2018_idx]
RA_jun2018= data["RA"][jun2018_idx]
DEC_jun2018 = data["DEC"][jun2018_idx]
run_jun2018 = data["run"][jun2018_idx]

jun2018= {}
jun2018["RA"]= RA_jun2018
jun2018["DEC"]= DEC_jun2018
jun2018["field"]= field_jun2018
jun2018["run"]= run_jun2018





lon_array = np.arange(0,360)
lat = 0.
eq_array = np.zeros((360,2))
for lon in lon_array:
    ga = ephem.Galactic(np.radians(lon), np.radians(lat))
    eq = ephem.Equatorial(ga)
    eq_array[lon] = np.degrees(eq.get())
RA = eq_array[:,0]
DEC = eq_array[:,1]




#print(jan2015)

#def plot_mwd(RA,Dec,org=0,title='Mollweide projection', projection='mollweide', marker_color = 'k'):

#plot_mwd(jan2015["RA"], jan2015["DEC"], 'Jan 2015 Run', 'hammer',  'forestgreen') 
#plot_mwd(feb2015["RA"], feb2015["DEC"], 'Feb 2015 Run', 'hammer', 'lightskyblue') 

#plot_mwd(dec2015["RA"], dec2015["DEC"], 'Dec 2015 Run', 'hammer', 'darkorange') 
#plot_mwd(jul2016["RA"], jul2016["DEC"], 'Jul 2016 Run', 'hammer', 'darkred') 
#plot_mwd(feb2017["RA"], feb2017["DEC"], 'Feb 2017 Run', 'hammer', 'blueviolet') 
#plot_mwd(feb2018["RA"], feb2018["DEC"], 'Feb 2018 Run', 'hammer', 'r') 
#plot_mwd(jun2018["RA"], jun2018["DEC"], 'Jun 2018 Run', 'hammer', 'salmon') 

#plot_mwd(longitude2, latitude2, 'GAL PLANE', 'hammer', 'k') 
plot_all(  RA, DEC, 'k', 'Galatic Plane', jan2015["RA"], jan2015["DEC"],  'forestgreen', 'Jan 2015',  feb2015["RA"], feb2015["DEC"],  'lightskyblue', 'Feb 2015',   dec2015["RA"], dec2015["DEC"],  'darkorange',  'Dec 2015', jul2016["RA"], jul2016["DEC"],  'darkred', 'Jul 2016',  feb2017["RA"], feb2017["DEC"],  'blueviolet', 'Feb 2017', feb2018["RA"], feb2018["DEC"], 'r',  'Feb 2018', jun2018["RA"], jun2018["DEC"],  'salmon', 'Jun 2018',  org=0, title= 'DWF fields', projection='aitoff' ) 

