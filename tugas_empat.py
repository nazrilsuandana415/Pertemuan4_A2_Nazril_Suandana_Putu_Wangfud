#menghitung huruf vokal
teks = str(input())

jumlah_a = teks.count("a")
jumlah_i = teks.count("i")
jumlah_u = teks.count("u")
jumlah_e = teks.count("e")
jumlah_o = teks.count("o")
jumlah_A = teks.count("A")
jumlah_I = teks.count("I")
jumlah_U = teks.count("U")
jumlah_E = teks.count("E")
jumlah_O = teks.count("O")

total_vokal =(jumlah_a+jumlah_i+jumlah_u+jumlah_e+jumlah_o+jumlah_A+jumlah_I+jumlah_U+jumlah_E+jumlah_O)

print(total_vokal)