import numpy as np
import matplotlib.pyplot as plt 
import time

"""
This program loads the data of year and their corresponding minimum and maximum tempertaure at Heathrow (London Airport) from heathrowdata.txt file 
It calculates the average of minimum and maximum temperature for each corresponding year data and plots a graph of Average Temperature (in deg C) vs. Year
@Shweta Chaurasia
"""

def average(num1,num2):    #function to take two numbers as parameters and returns their average.
    return ((num1+num2)/2)

def cToF(cels):            #function to convert deg C to deg F
    return ((cels*9/5)+32)

def fToC (fahr):          #function to convert deg F to deg C
    return (5/9 * (fahr-32))

def main():

    txt_file_array = np.loadtxt("heathrowdata.txt", skiprows = 7, usecols = (0,2,3)).round(2) #loads data from the text file to get 0,2 and 3 column data skipping first 7 rows

    avg_temp_array = (average(txt_file_array[:,1], txt_file_array[:,2])) #gets the average of minimum and maximum temperature
     
    plt.plot(txt_file_array[:,0], avg_temp_array[:,], '*', color = 'purple', markersize = 4) # plotting a graph of points with 0 col of txt_file_array (year) as X-axis 
                                                                                              # and 0 col of avg_temp_array (avg temperature) as Y-axis
    
    m, b = np.polyfit(txt_file_array[:,0], avg_temp_array[:,], 1)    #calculates the coefficients i.e. the slope and y-intercept of the regression line

    plt.plot(txt_file_array[:,0], m * txt_file_array[:,0] + b, 'blue', linewidth = 2, ls = '-') #to plot the regression line on graph, (x, m * x + b)
    
    plt.title("Average Temperature vs. Year", fontdict={'fontsize': 'xx-large',             #to display and adjust the format of the graph's title
                                                        'fontweight': 'extra bold',
                                                        'color': 'brown',
                                                        'family': {'times new roman'},
                                                        'verticalalignment': 'baseline',
                                                        'horizontalalignment': 'center'}, 
              loc='center')

    plt.xlabel("Year", fontdict={'fontsize': 'x-large',                                     #to display and adjust the format of X-axis label
                                'fontweight': 'normal',
                                'color': 'blue',
                                'verticalalignment': 'top', 'family': {'arial'}})

    plt.ylabel("Average Temperature (degC)", fontdict={'fontsize': 'x-large',               #to display and adjust the format of Y-axis label
                                                'fontweight': 'normal',
                                                'color': 'blue',
                                                'verticalalignment': 'bottom',
                                                'horizontalalignment': 'center', 'family': {'arial'}})


    plt.show()     # displays the plotted graph
    


if __name__ == "__main__":
    main()
