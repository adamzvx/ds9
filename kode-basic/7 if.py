umur = input('masukkan umur anda : ')
if int(umur)* 365 > 20000:
	print('umur anda telah cukup tua')
elif int(umur)*365 > 10000:
	print('masih banyak waktu untuk berubah')
else:
	print('ayo mulai kamu bisa')

umur2 = input('masukkan umur hero :')
umur2 = int(umur2)*365

if umur2 >=9490:
	print('welcome Jedi Master, go to Master Yoda')
elif umur2 >=8395 and umur2<9490:
	print('Still Jedi Knight')
else:
	print('Still Young Padawan')