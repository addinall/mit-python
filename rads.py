# rads.py
# vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#
# Mark Addinall - Sept 2015
# MIT Computer Science - Python
#
# RADIATION EXPOSURE  (25 points possible)
# "Radioactive decay" is the process by which an unstable atom loses 
# energy and emits ionizing particles - what is commonly refered to 
# as radiation. Exposure to radiation can be dangerous and is very 
# important to measure to ensure that one is not exposed to too 
# terribly much of it.
#
# The radioactivity of a material decreases over time, as the material 
# decays. A radioactive decay curve describes this decay. The x-axis 
# measures time, and the y-axis measures the amount of activity produced 
# by the radioactive sample. 'Activity' is defined as the rate at which 
# the nuclei within the sample undergo transititions - put simply, this 
# measures how much radiation is emitted at any one point in time. 
# The measurement of activity is called the Becquerel (Bq).
#
# Now here's the problem we'd like to solve. Let's say Sarina has 
# moved into a new apartment. Unbeknownst to her, there is a sample 
# of Cobalt-60 inside one of the walls of the apartment. Initially 
# that sample had 10 MBq of activity, but she moves in after the sample 
# has been there for 5 years. She lives in the apartment for 6 years, 
# then leaves. How much radiation was she exposed to?
#
# We can actually figure this out using the radioactive decay curve. 
# What we want to know is her total radiation exposure from year 5 to year 11. 
#
# We have learned a technique that can help us here - approximation. 
# Let's use an approximation algorithm to estimate the area under 
# the ha;f life curve. We'll do so by first splitting up the area into 
# equally-sized rectangles (in this case, six of them, one rectangle per year):
#
# Once we've done that, we can figure out the area of each rectangle 
# pretty easily. Recall that the area of a rectangle is found by 
# multiplying the height of the rectangle by its width. The height of this rectangle:
# is the value of the curve at 5.0. If the curve is described by 
# a function, f, we can obtain the value of the curve by asking for f(5.0).
#
# f(5.0) = 5.181
#
# The width of the rectangle is 1.0. So the area of this single rectangle 
# is 1.0*5.181 = 5.181. To approximate how much radiation Sarina was 
# exposed to, we next calculate the area of each successive rectangle 
# and then sum up the areas of each rectangle to get the total. 
# When we do this, we find that Sarina was exposed to nearly 23 MBq of 
# radiation.
#

def f(x):

    '''
        This function describes the half-life decay profile of 
        Cobalt-60 '''

    import math
    return 10 * math.e **(math.log(0.5)/5.27 * x)



def radiationExposure(start, stop, step):
   
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
    the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
    between start and stop times.  '''

    testing = True                              # for me to debug!

    # OK, what we are doing here is using the Riemann Integral
    # to calculate the radiation dose received as a function
    # of the area under the curve of the half-life decay of
    # the isotope as described in the function f()

    exposure    = 0
    periods     = int((stop - start) / step)    # step gives us the widths of our
                                                # rectangles under the curve,
                                                # thinner the rectangles, greater 
                                                # the accuracy
                                                # of the approximation of the integral
    for x in range(periods):
        exposure += f(start + x * step) * step

    if testing:
        print("f(start)    == " + str(f(start)))
        print("f(stop)     == " + str(f(stop)))
        print("step        == " + str(step))
        print("periods     == " + str(periods))
        print("exposure    == " + str(exposure))

    return exposure

    print("--------------------------------------")

# Test as per MIT supplied test cases

print radiationExposure(0, 5, 1)
# 39.10318784326239

print radiationExposure(5, 11, 1)
# 22.94241041057671

print radiationExposure(0, 11, 1)
# 62.0455982538

print radiationExposure(40, 100, 1.5)
# 0.434612356115

'''ma
CORRECT
Function call: radiationExposure(0, 5, 1)
Cobalt-60.Half-life: 5.27 years. Initial Activity: 10 MBq.
Find total exposure from years 0 - 5.
Output:
39.10318784326239

Function call: radiationExposure(5, 11, 1)
Cobalt-60.Half-life: 5.27 years. Initial Activity: 10 MBq.
Find total exposure from years 5 - 11.
Output:
22.94241041057671

Function call: radiationExposure(12, 16, 1)
Cobalt-60.Half-life: 5.27 years. Initial Activity: 10 MBq.
Find total exposure from years 12 - 16.
Output:
6.848645835538622

Function call: radiationExposure(0, 4, 0.25)
Radium-224.Half-life: 3.66 days. Initial Activity: 400 MBq.
Find total exposure from days 0 - 4.
Output:
1148.6783342153556

Function call: radiationExposure(5, 10, 0.25)
Radium-224.Half-life: 3.66 days. Initial Activity: 400 MBq.
Find total exposure from days 5 - 10.
Output:
513.4662018628549
'''
