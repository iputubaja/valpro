
print ('==========================')
print ('GAJI KARYAWAN STMIK A.YANI')
print ('==========================')

print('Gaji dalam waktu sehari')
n = int(input('Masukan Jumlah Karyawan yang ingin di hitung gajinya: '))
print()
for i in range (1,n+1) :
	nama = str(input('Masukan Nama :'))
	jam = int(input('Masukan Jumlah Jam :'))
	
	#jika jam kerja lebih dari 24 jam maka akan masuk kedalam jam lembur
	if jam >= 24 :
		lembur = jam - 24
		upah = 24 * 20000 + lembur * 25000
	else :
		upah = jam*20000
	print (upah)
	
print('-----------------------')
print('Gaji dalam waktu 7 hari')
n = int(input('Masukan Jumlah Karyawan yang ingin di hitung gajinya: '))
print()
for i in range (1,n+1) :
	nama = str(input('Masukan Nama :'))
	jam = int(input('Masukan Jumlah Jam :'))
	
	#jika jam kerja lebih dari 168 jam maka akan masuk kedalam jam lembur
	if jam >= 168 :
		lembur = jam - 168
		upah = 168 * 20000 + lembur * 25000
	else :
		upah = jam*20000
	print (upah)
	
print('-----------------------')	
print('Gaji dalam waktu 21 hari')
n = int(input('Masukan Jumlah Karyawan yang ingin di hitung gajinya: '))
print()
for i in range (1,n+1) :
	nama = str(input('Masukan Nama :'))
	jam = int(input('Masukan Jumlah Jam :'))
	
	#jika jam kerja lebih dari 504 jam maka akan masuk kedalam jam lembur
	if jam >= 504 :
		lembur = jam - 504
		upah = 504 * 20000 + lembur * 25000
	else :
		upah = jam*20000
	print (upah)
	
print('-----------------------')
print('Gaji dalam waktu 30 hari')
n = int(input('Masukan Jumlah Karyawan yang ingin di hitung gajinya: '))
print()
for i in range (1,n+1) :
	nama = str(input('Masukan Nama :'))
	jam = int(input('Masukan Jumlah Jam :'))
	
	#jika jam kerja lebih dari 720 jam maka akan masuk kedalam jam lembur
	if jam >= 720 :
		lembur = jam - 720
		upah = 720 * 20000 + lembur * 25000
	else :
		upah = jam*20000
	print (upah)