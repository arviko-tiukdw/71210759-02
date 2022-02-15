#Arviko Praditya 71210759
print("Menghitung Uang Gaji")
#Memasukkan
gaji_perjam = int(input("Masukkan Gaji Perjam Yang Anda Inginkan : "))
jam_kerja = int(input("Masukkan Jam Kerja yang Rencana Anda Lakukan selama 1 minggu : "))
#Gaji Bersih
pendapatan_1 = gaji_perjam * jam_kerja
print("Gaji Bersih Anda Sebelum di Potong Pajak : ",pendapatan_1)
#Pajak Selama Bekerja
pendapatan_2 = pendapatan_1*0.14
print("Gaji Anda Setelah di Potong Pajak : ",pendapatan_2)
#Uang untuk baju dan aksesoris
uang_baju = pendapatan_2 - (pendapatan_2*0.1)
print("Gaji Anda Setelah membeli baju dan aksesoris : ",uang_baju)
#Uang untuk membayar alat tulis
uang_atk = uang_baju - (uang_baju*0.01)
print("Gaji Anda Setelah membeli alat tulis : ",uang_atk)
#Uang untuk disedekahkan
uang_sedekah = uang_atk - (uang_atk*0.25)
print("Gaji Anda Setelah memberikan sedekah : ",uang_sedekah)
#Sedekah Untuk Yatim
uang_yatim = uang_sedekah - (uang_sedekah*0.3)
print("Uang yang akan diterima anak yatim : ",uang_yatim)
#Sedekah Untuk Dhuafa
uang_dhuafa = uang_sedekah-uang_yatim
print("Uang yang akan diterima anak dhuafa : ",uang_dhuafa)