for word in ['a','b','c','d','e','ef']:
	print(word,'\n')


# SUMM
sum =0
for i in [1,2,3,4]:
	sum = sum +i
	print(sum)


prod = 1
for i in [1,2,3,4]: prod*=i 
print(prod)


teks = 'rubah besar'
kalimat =('makan','siang','bersama')
for i in teks:
	print(i , end=' ')

for i in kalimat:
	print(i,end='...')
print('\n')
kor =[(1,2), (3,4), (5,6)]
for (x,y) in kor:
	print(x,y)