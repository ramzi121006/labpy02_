angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator aritmatika (+, -, *, /): ")

if operator == '+':
    hasil = angka1 + angka2
elif operator == '-':
    hasil = angka1 - angka2
elif operator == '*':
    hasil = angka1 * angka2
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error: Pembagian dengan nol tidak diperbolehkan"
else:
    hasil = "Error: Operator tidak valid!"

print("Hasil: ", hasil)