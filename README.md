# UTS-Progjar

## How Code Works

### Server
1. **Inisialisasi Soket:**
    - Server menggunakan `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)` untuk membuat objek soket UDP. Ini menentukan bahwa server akan menggunakan protokol UDP untuk komunikasi.
2. **Menunggu Koneksi:**
    - Setelah membuat soket, server mengikatnya ke alamat localhost dengan port 12345 menggunakan `server_socket.bind(('localhost', 12345))`. Kemudian, server menunggu permintaan koneksi dari klien dengan memanggil `server_socket.recvfrom(1024)`. Ini memungkinkan server untuk menerima permintaan koneksi dari klien.
3. **Permainan Utama:**
    - Setelah koneksi berhasil dibuat, server memulai permainan dengan klien. Dalam loop utama:
      
        a. Server mengirimkan kata warna acak ke klien menggunakan fungsi `send_color`. Ini dipilih secara acak dari daftar warna yang telah ditentukan sebelumnya.
      
        b. Server menunggu jawaban dari klien. Jika waktu habis tanpa jawaban dari klien, server memberikan timeout dan mengakhiri permainan saat itu.
      
        c. Jika server menerima jawaban dari klien, itu memeriksa kebenaran jawaban menggunakan `check_answer`. Jika benar, server mengirimkan feedback "100: Jawaban benar!", jika tidak, mengirimkan feedback "0: Jawaban salah".
Server memberikan jeda selama 10 detik sebelum mengirimkan kata warna berikutnya.
### Client
### Fungsi Tambahan
