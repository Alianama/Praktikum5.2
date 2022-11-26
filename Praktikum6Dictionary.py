print("Program Input Nilai")
print("=============================================")


while True : 
    menu = input("\n[ (T)ambah, (U)bah, (H)apus, (L)ihat, (C)ari ? ] = ")



    while menu == 'T':
        siswa = {
            'nim' : 'n',
            'nama' : 'a', 
            'uts' : 'b', 
            'uas' : 'c', 
            'tugas' : 'd'
            }

        siswa ['nim'] = input("Masukan Nim\t\t= ")
        siswa ['nama'] = input("Masukan Nama\t\t= ")
        siswa ['uts'] = input("Masukan Nilai UTS\t= ")
        siswa ['uas'] = input("Masukan Nilai UAS\t= ")
        siswa ['tugas'] = input("Masukan Nilai Tugas\t= ")

        
        break
    while menu == 'L':
        print("NIM\t\t= ", siswa['nim'])
        print("Nama\t\t= ", siswa['nama'])
        print("Nilai UTS\t= ", siswa['uts'])
        print("Nilai UAS\t= ", siswa['uas'])
        print("Nilai Tugas\t= ", siswa['tugas'])
        break