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