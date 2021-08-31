# Homework 6 - Heathrow 👩‍✈️🛫🌎☁️🌡️
Homework 5 practice on numpy and matplotlib

Data for this assignment comes from the the United Kingdom's weather agency known as the Met Office [metoffice.gov.uk](https://www.metoffice.gov.uk/). The exact dataset you will be using is recorded from a weather station at Heathrow Airport and stored in the [metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt](https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt) file.

## Part 1 - Instructions
This assignment is meant to ensure that you:
* Can manipulate real data with programmatic cleaning
* Understand `numpy`, and `matplotlib`
* Gain experience analyzing multidimensional arrays
* Implement and call user-defined functions
* Become familiar with the plotting functions

You will complete the functions in [hw6_heathrow.py](hw6_heathrow.py) to:

1. Define a function called `average` which accepts two parameters, adds them together, divdes them by two, and returns that result.

2. Define a function called `cToF` which accepts a Celcius parameter and returns its Fahrenheit conversion.

3. Define a function called `fToC` which accepts a Fahrenheit parameter and returns its Celcius conversion.

Then complete `main` function so that it:
1. Loads the text data skipping the first seven (7) rows, and only uses columns 0, 2, and 3 with a [numpy](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html) function.
2. Create a [plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html) of points using the year data as the domain and the average of the maximum and minimum as the range. You can convert the range to Fahrenheit if you prefer.
3. Plot a [regression line](https://www.kite.com/python/answers/how-to-plot-a-linear-regression-line-on-a-scatter-plot-in-python) to your figure.
4. Add a [title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html), [xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel), and [ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel) to your plot and customize your figure however you like.
5. [Save](https://www.kite.com/python/docs/matplotlib.pyplot.savefig) the figure and commit it to this repository. You can use any filetype you like (preference for svg and png).

This lab assignment assumes reading from a file. To ensure that GitHub can test and run your code, ***do not*** specify the entire path to the data file. The tester assumes no keyboard input.

## Part 2 - Reflection
Update the README to answer the following questions:

 1. Add the saved plot file here so it can be displayed in your README.md file.
  https://github.com/90812-Intro/hw6-heathrow-shwetachauras/blob/e7399d863b9e603433a0e052f36701ce29159a15/HW6_Graph.png
 
 2. What conclusion(s) can you draw from the graph you generated?
   The average temperature of Heathrow lies mostly in the range of 2.5 to 20 deg C. The average temperature very rarely goes above 20 deg C and even rarely falls      below 0 deg C. 
 
 3. How come your functions work on regular numbers as well as `np.ndarray`'s?
  Because unlike in lists, in np.ndarray's, '+' and '-' sign means addition and subtraction, respectively, of each elements of one ndarray with the corresponding element of another ndarray, provided the two ndarrays are of same dimensions. Also, ndarrays treat * and / with any integer or float as scalar multiplication and scalar division respectively. 
  e.g. 
    a1 = np.array([[1,2,3], [2,3,4]])
    a2 = np.array([[1,2,3], [2,3,5]])
    a = 2*a1+a2
    Now, a gets [[3,6,9], [[6,9,13]]
    
    Thus, the functions work on both regular numbers as well as np.ndarray's.
    
 4. Compare the functions `loadtxt` and `open`.
 Both the functions 'loadtxt' and 'open' are be used to load the data from a text file but 
 (i)'loadtxt' is for numpy to get the data in the form of class 'numpy.ndarray' while 'open' returns the file object in the form of '_io.TextIOWrapper' (a list of strings)
 
 (ii) 'loadtxt' only loads a data from a text file while 'open' is not just limited to text files.
 
 5. Explain the [`polyfit`]() function?
'polyfit' function is used to return coefficients of the polynomial that generate a curve to best fit the data. It fits a least squares polynomial for the given set of data (https://engineering.vanderbilt.edu/ge/es140/Otherlinks/MatlabTutorial/CurveFitting.php). 

e.g. In this case, to plot a regression line that would best represent the data, we need a polynomial of first degree (i.e. a straight line). So we use the function 'polyfit' and pass the parameters: x and y coordinates, and degree equal to 1, to get the coefficients of straight line (in this case slope and y-intercept). These are then used to plot the regression line on the plot.

 ---
 ## Running Tests Locally
 You do not have to wait for test results from GitHub because you can run tests on your own computer. The tester uses the program `pytest` which can be installed using the command `pip install -U pytest` (more info available at [https://docs.pytest.org](https://docs.pytest.org/en/stable/getting-started.html)). Use the following command to run `pytest`.

 ``` bash
 pytest
 ```
 ---
## Installing numpy
Use the following command to install numpy if you have not done so already. More documentation can be found on [numpy.org](https://numpy.org/install/).
``` bash
pip install numpy
```
