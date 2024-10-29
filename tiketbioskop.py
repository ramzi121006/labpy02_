tipe_tiket = input("Masukkan tipe tiket (reguler/VIP): ").lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()
harga_tiket = 50000 if tipe_tiket == "reguler" else 100000
diskon = 0.2 if status_member == "ya" else 0
total_harga = harga_tiket * (1 - diskon)
print("Total harga yang harus dibayar: Rp", int(total_harga))
   
