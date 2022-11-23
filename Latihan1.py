kontak = {
    'Ari': '081267888',
    'Dina': '087677776'

}
# Print Kontak Ari
print("Kontak Ari", "\n=================")
for ari_nama, ari_nomor in kontak.items():
    print(ari_nama, ari_nomor)
    break

# Menambah Kontak Riko
kontak['Riko'] = '087654544'

# Mengubah Kontak Dina
kontak['Dina'] = '088999776'

# Menampilkan Semua Nama
print("\n|   Semua Nama  |", "\n|===============|")
for nama in kontak.keys():
    print("|", "    ", nama, "\t|")
print("\n")

# menampilkan Semua Nomor
print("\n|   Semua Nomor |", "\n|===============|")
for nomor in kontak.values():
    print("|", nomor, "\t|")
print("\n")

# Menampilkan Semua Kontak
print("| Nama\t| Nomor telpon\t|")
print("|=======================|")
for k_nama, k_nomor in kontak.items():
    print("|", k_nama, "\t|", k_nomor, "\t|")
