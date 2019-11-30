import numpy as np
height =np.round(np.random.normal(1.75,0.2,5000),2)
print(height)
print(len(height))
weight =np.round(np.random.normal(60.32,15,5000),2)
print(weight)
print(len(weight))

npCity = np.column_stack((height,weight))
print(npCity)

print('Rata-rata tinggi badan',np.mean(npCity[:,0]))
print('Nilai Tengah tinggi badan',np.median(npCity[:,0]))
print('Std Deviasi tinggi badan',np.std(npCity[:,0]))