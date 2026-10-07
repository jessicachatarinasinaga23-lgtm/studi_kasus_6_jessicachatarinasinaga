# studi_kasus_6_jessicachatarinasinaga
**Nama : Jessica Chatarina Sinaga <br>
NIM :  26090611016 <br>
Kelas : A** <br>
<br>
PENJELASAN MENGENAI FUNGSI DAN KEGUNAAN BAGIAN-BAGIAN KODE<br>
<br>
**Penjelasan bagian file Inventaris.json**<br>
<br>
<img width="549" height="640" alt="Cuplikan layar 2026-10-07 235208" src="https://github.com/user-attachments/assets/012e58c6-8ec2-4ac1-9e7a-d905736d8874" /> <br>
File _inventaris.json_ tersebut bertindak sebagai database lokal berformat JSON yang menyimpan seluruh riwayat data barang dalam bentuk terstruktur, terdapat tiga struktur dalam file inventaris.json yaitu, Array;Berfungsi menampung kumpulan (banyak) data barang sekaligus dalam satu file, Dictionary;Setiap pasangan kurung kurawal mewakili satu unit data barang, dan Pasangan Key-Value adalah konsep dasar penyimpanan data di mana setiap informasi disimpan dalam bentuk nama label (key) dan isinya (value). <br>
<br>
**Penjelasan bagian utama program**<br>
<br>
<img width="458" height="83" alt="Cuplikan layar 2026-10-07 232319" src="https://github.com/user-attachments/assets/65fd6309-ab59-45d9-9ec1-539fb1332e12" /> <br>
import json berfungsi untuk mengolah data berformat JSON (membaca, membuat, dan menyimpan file .json).<br>

FILE_PATH = "inventaris.json" akan menyimpan nama/jalur file target ke dalam variabel konstan. Tujuannya adalah mempermudah jika suatu saat nama file penyimpanan ingin diubah. <br>
<br>
<img width="733" height="302" alt="Cuplikan layar 2026-10-07 232326" src="https://github.com/user-attachments/assets/be86db66-5633-49a6-9aa7-568fc67c667a" /> <br>
Fungsi ini bertugas membaca data dari file JSON dan mengembalikannya dalam bentuk list<br>

try ... except untuk menangani error agar program tidak crash jika terjadi masalah pada file. <br>

open(FILE_PATH, "r", ...) & json.load(f) akan membaca file inventaris.json dan mengonversi format JSON menjadi struktur data. <br>

except FileNotFoundError Jika file inventaris.json belum ada, program secara otomatis membuat file baru berisi list kosong ([]). br>

except json.JSONDecodeError Jika file JSON rusak atau kosong (tidak berformat valid), fungsi akan mengembalikan list kosong ([]) agar program tetap berjalan aman. <br>
<br>
<img width="1264" height="348" alt="Cuplikan layar 2026-10-07 232345" src="https://github.com/user-attachments/assets/5582ee0e-fb71-40bb-a1fd-46d5d721e546" /> <br>
Fungsi ini bertugas menampilkan seluruh daftar barang ke layar dalam bentuk tabel yang rapi. <br>

data = baca_data() untuk mengambil data barang terbaru dari file.<br>

if not data berfungsi memeriksa apakah inventaris kosong. Jika ya, pesan pemberitahuan akan ditampilkan.<br>

Format :<8}, :<20} untuk menata rata kiri kolom tabel dengan lebar karakter tertentu agar tampilan rapi dan sejajar.<br>

Rp{item['harga']:,} umtuk mengformat angka harga dengan pemisah ribuan (koma).<br>
<br>
<img width="780" height="819" alt="Cuplikan layar 2026-10-07 232406" src="https://github.com/user-attachments/assets/c4f12019-8059-4abf-8073-e3826bcce687" /> <br>
Fungsi ini bertugas menerima masukan barang baru dari pengguna, memvalidasinya, lalu menyimpannya ke file JSON.<br>

.strip().upper() untuk menghapus spasi berlebih di awal/akhir input dan mengubah kode barang menjadi huruf kapital semua (misal: "brg1" menjadi "BRG1").<br>

Pemeriksaan Duplikasi (for item in data:) kegunaannya adalah memastikan tidak ada kode barang yang sama di dalam database.<br>

try ... except ValueError untuk memvalidasi agar input untuk stok dan harga benar-benar berupa angka bulat (int). Jika diisi teks/simbol, input ditolak.<br>

data_baru = { ... } untuk membungkus data barang ke dalam bentuk dictionary.<br.

json.dump(data, f, indent=4) untuk menyimpan kembali seluruh data yang telah diperbarui ke file inventaris.json dengan format identasi 4 spasi agar mudah dibaca. <br>
<br>
<img width="967" height="538" alt="Cuplikan layar 2026-10-07 232415" src="https://github.com/user-attachments/assets/b5ae02f9-759e-4c80-9b34-42b27cf147e5" /> <br>
while True untuk melakukan pengulangan tanpa henti (infinite loop) agar menu terus tampil setelah pengguna selesai menjalankan suatu aksi.<br>

if-elif-else berfungsi untuk menjalankan fungsi yang sesuai dengan nomor menu yang dipilih pengguna (1, 2, atau 3).<br>

break akan menghentikan perulangan while dan keluar dari program saat pengguna memilih menu nomor 3.<br>

terakhir if __name__ == "__main__" untuk Mmemastikan fungsi main() hanya akan dijalankan jika file Python ini dieksekusi secara langsung, bukan saat diimpor sebagai modul oleh file lain.<br>
<br>
**Hasil/Output** <br>
<br>
<img width="676" height="660" alt="Cuplikan layar 2026-10-08 042337" src="https://github.com/user-attachments/assets/9870eea1-f789-4e35-b2cf-ac4e63e06da8" /> <br>
Ini adalah kondisi awal dari file inventaris.json sebelum ditambahkan barang baru. <br>
<img width="651" height="438" alt="Cuplikan layar 2026-10-08 042513" src="https://github.com/user-attachments/assets/c4fd787f-aad7-44f2-a447-5ca4cf116685" /> <br>
Jika kita memilih "1" pada pilihan menu, kita akan ditunjukkan data yang sama dengan data yang sudah ada di dalam Inventaris.json<br>
<img width="709" height="362" alt="Cuplikan layar 2026-10-08 042807" src="https://github.com/user-attachments/assets/4ae56e79-7458-4230-a32a-99407940baa8" /> <br>
Ketika kita memilih "2" pada pilihan menu, kita akan diminta memasukkan kode barang, nama, stok, dan juga harga barang, dan jika sudah, data baru akan ditambahkan pada Inventaris.json secara permanen.<br>
<img width="535" height="788" alt="Cuplikan layar 2026-10-08 043032" src="https://github.com/user-attachments/assets/e495ae1d-5166-444f-873f-e0a654459dc1" /> <br>
Ini adalah kondisi Inventaris.json ketika data baru ditambahkan.<br>
<img width="718" height="200" alt="Cuplikan layar 2026-10-08 043252" src="https://github.com/user-attachments/assets/15534ced-bb38-4276-b16e-02328dffd9ea" /> <br>
Dan jika kita memilih "3" pada menu, maka program telah selesai untuk digunakan.<br>
<br>
<img width="693" height="471" alt="Cuplikan layar 2026-10-08 043755" src="https://github.com/user-attachments/assets/3776b74d-b929-46f5-9d56-512045ea0240" /> <br>
Namun, walaupun program dimulai kembali, data dari program sebelumnya yaitu "Tepung 1kg" masih tetap ada di dalam data dan tersimpan permanen di dalam Inventaris.json.<br>
<br>
Bukti bahwa data baru tetap tersimpan meskipun program dijalankan kembali.<br>
<br>
<img width="1920" height="1080" alt="Screenshot (134)" src="https://github.com/user-attachments/assets/c598abd8-73c8-4064-96dc-279882a8cb4d" /> <br>
<img width="1920" height="1080" alt="Screenshot (135)" src="https://github.com/user-attachments/assets/65f14019-34a3-4ec8-83f6-1648b837551f" /> <br>
Walaupun telah selesai menggunakan kode program dengan menu "3" atau menu keluar, ketika kita memulai kembali, data baru yaitu "Tepung 1kg" masih tersimpan dan akan ikut ditampilkan ketika memilih menu "1" pada program yang baru dijalankan.

