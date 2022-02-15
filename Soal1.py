#Arviko Praditya 71210759

print("Sistem Menghitung Berat Badan Ideal/BMI")
#Memasukkan Nilai BMI dan Tinggi(dalam meter)
bmi = int(input("Masukkan BMI Anda : "))
tinggi_badan = float(input("Masukkan Tinggi Badan Anda (dalam meter) : ",))
#Menghitung tinggi badan dalam kuadrat dan menghitung berat badan dengan menggunakan bmi dan tinggi badan dalam kuadrat
tinggi_badan_2 = tinggi_badan**2
berat_badan = bmi * tinggi_badan_2
print("Berat Badan Anda Adalah", berat_badan)
#Menghitung berat badan maksimal dan minimal
berat_min = 18.5 * tinggi_badan_2
berat_max = 25 * tinggi_badan_2
#Menghitung berat badan jika BMI tidak masuk kedalam BMI yang Ideal
if bmi < 18.5:
    berat_minimal = berat_min-berat_badan
    print("Berat Badan Ideal Anda Harus", berat_badan+berat_minimal)
elif bmi > 25:
    berat_maksimal = berat_badan-berat_max
    print("Berat Badan Ideal Anda Harus", berat_badan-berat_maksimal)
else:
    print("Berat Anda Sudah Ideal")







