import numpy as np

height = [1.75, 1.6, 1.5, 1.7, 1.81]
weight = [66.4, 65.4, 70.4, 70, 66] 
# a =np.array([1, 2, 3])
npheight = np.array(height)
npweight = np.array(weight)
print(npheight)
print(npweight)
bmi = npweight/npheight ** 2
print('bmi...' , bmi)
print(bmi[bmi > 24])
print(bmi)