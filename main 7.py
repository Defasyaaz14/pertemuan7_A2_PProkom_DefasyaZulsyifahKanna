def ganti_vokal(teks, pengganti):
    huruf_vokal = "aeiouAEIOU"
    teks_baru = ""
    for huruf in teks:
        if huruf in huruf_vokal:
            teks_baru += pengganti
        else:
            teks_baru += huruf
    return teks_baru

# Input dari pengguna
teks_input = input("Masukkan teks: ")
pengganti_input = input("Masukkan huruf pengganti: ")

# Panggil fungsi untuk mengganti huruf vokal
teks_hasil = ganti_vokal(teks_input, pengganti_input)

# Tampilkan hasil
print("Teks setelah penggantian huruf vokal:")
print(teks_hasil)
