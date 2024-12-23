print("*****Constants in SciPy********") 

# Import the constants module once
from scipy import constants 

# Print the value of pi
print(constants.pi)

print("*****Constant Units*********")

# Print the list of attributes in the constants module
print(dir(constants))

# Time constants:
print(constants.minute)      # 60.0 seconds
print(constants.hour)        # 3600.0 seconds
print(constants.day)         # 86400.0 seconds
print(constants.week)        # 604800.0 seconds
print(constants.year)        # 31536000.0 seconds
print(constants.Julian_year) # 31557600.0 seconds
