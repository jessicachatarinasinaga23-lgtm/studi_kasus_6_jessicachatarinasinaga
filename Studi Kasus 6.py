import json

FILE_PATH = "inventaris.json"

def baca_data():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:

        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
        return []
    except json.JSONDecodeError:
        
        return []

def tampilkan_data():
    data = baca_data()
    print("\n" + "="*50)
    print("DAFTAR INVENTARIS BARANG GUDANG")
    print("="*50)

    if not data:
        print("Belum ada data barang di dalam inventaris.")
    else:
        print(f"{'Kode':<8} | {'Nama Barang':<20} | {'Stok':<6} | {'Harga':<10}")
        print("-" * 50)
        for item in data:
            print(f"{item['kode_barang']:<8} | {item['nama_barang']:<20} | {item['stok']:<6} | Rp{item['harga']:,}")
    print("="*50)

def tambah_data():
    data = baca_data()
    print("\n TAMBAH BARANG BARU ")
    
    kode = input("Masukkan Kode Barang  : ").strip().upper()

    
    for item in data:
        if item['kode_barang'] == kode:
            print("Error: Kode barang sudah terdaftar!")
            return

    nama = input("Masukkan Nama Barang  : ").strip()
    
    try:
        stok = int(input("Masukkan Jumlah Stok  : "))
        harga = int(input("Masukkan Harga (Rp)   : "))
    except ValueError:
        print("Error: Stok dan Harga harus berupa angka!")
        return

    data_baru = {
        "kode_barang": kode,
        "nama_barang": nama,
        "stok": stok,
        "harga": harga
    }

    data.append(data_baru)
    
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Barang '{nama}' berhasil ditambahkan secara permanen!")

def main():
    
    while True:
        print("\n SISTEM MANAJEMEN INVENTARIS TOKO ")
        print("1. Tampilkan Seluruh Data Barang")
        print("2. Tambah Data Barang Baru")
        print("3. Keluar Program")
        
        pilihan = input("Pilih menu (1-3): ").strip()
        
        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan sistem inventaris. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()