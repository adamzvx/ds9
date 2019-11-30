# INI FILE UNTUK FUNGSI / FUNCTION

def add(a,b):
	return a+b

def intersect(kata1, kata2):
	hasil =[]
	for i in kata1:
		if i in kata2:
			hasil.append(i)
	return hasil

kata1 = input('masukkan kata pertama : ')
kata2 = input('masukkan kata kedua : ')
hasilPotong = intersect(kata1,kata2)
print('\n\n')
for i in hasilPotong:
	print('huruf ', i ,' ada dalam kata ',kata2)

