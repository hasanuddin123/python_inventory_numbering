nomor_awal = 1
nomor_akhir = 24
masuk_1 = [1,3,4]

aktif = ([ int(a) for a in masuk_1 ])
aktif
Out[6]: [1, 3, 4]

range_nomor_kapasitas = ([ jj for jj in range(nomor_awal, nomor_akhir + 1) ])
range_nomor_kapasitas
Out[8]: 
[1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19,
 20,
 21,
 22,
 23,
 24]

hasil = list(set(range_nomor_kapasitas).difference(set(aktif)))
hasil
Out[10]: [2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
