"""
Number of Vaccinations


Using the same vaccinations dataset, which includes the number of times people got the flu vaccine.
The dataset contains the following numbers:
never: 5
once: 8
twice: 4
3 times: 3

Calculate and output the variance.
Declare a list with the data and use a loop to calculate the value.
We will soon learn about easier ways to calculate the variance and other summary statistics using Python. For now, use Python code to calculate the result using the corresponding equation.
"""

vac = [0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3]

mean = sum(vac)/len(vac)

var = sum((i - mean) ** 2 for i in vac)/len(vac)

print(var)