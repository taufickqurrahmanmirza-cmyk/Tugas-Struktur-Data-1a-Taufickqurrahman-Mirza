data_mahasiswa = {
    "12550111074": "Reysa Priatna",
    "12550111081": "Taufickqurrahman Mirza",
    "12550111122": "M. Rafiq Alghifari",
    "12550111125": "M. Yahya Abiyu"
}

nim = "12550111081"

if nim in data_mahasiswa:
    print("\nHasil pencarian:")
    print("NIM:", nim)
    print("Nama:", data_mahasiswa[nim])
else:
    print("\nData mahasiswa tidak ditemukan.")
