import os

f =open("teks.txt","r")
print(f.read())
print(f.readline())

for x in f:
	print(x)

print(f.close())

f2=open("teks2.txt","a")
f2.write("\n isi dari teks 2")
f2.close()
f2=open("teks2.txt","r")
print(f2.read())

# write overwrite
f2=open('teks2.txt','w')
f2.write('isssi jadi 0 \n')
f2.close()

f2= open('teks2.txt','r')
print(f2.read())

# menghapus file
if os.path.exists('teks3.txt'):
	os.remove('teks3.txt')
#membuat file
f3 = open('teks3.txt','x')
f3 = open('teks3.txt','w')
