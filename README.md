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
      
         d. Server memberikan jeda selama 10 detik sebelum mengirimkan kata warna berikutnya.
### Client
1. **Inisialisasi Soket:**
    - Klien menggunakan `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)` untuk membuat objek soket UDP yang akan digunakan untuk komunikasi dengan server.
2. **Koneksi ke Server:**
    - Setelah membuat soket, klien mengirim permintaan koneksi ke server menggunakan `client_socket.sendto(b"Connect", ('localhost', 12345))`. Ini memulai komunikasi dengan server yang telah mengikat dirinya ke alamat dan port tertentu.
3. **Permainan dengan Server:**
    - Dalam loop utama:
      
        a. Klien menerima kata warna dari server menggunakan `client_socket.recvfrom(1024)`. Kata warna ini dalam bahasa Inggris.
      
        b. Klien menampilkan kata warna dalam bahasa Inggris kepada pengguna dan meminta jawaban dari pengguna dalam bahasa Indonesia.
      
        c. Jawaban dari pengguna dikirim kembali ke server menggunakan `client_socket.sendto(color_ind.encode(), ('localhost', 12345))`.
      
        d. Klien menerima feedback dari server, memprosesnya, dan menampilkan jumlah total poin.

### Fungsi Tambahan
1. **send_color:**
    - Fungsi ini digunakan oleh server untuk mengirimkan kata warna acak ke klien. Ini memilih warna secara acak dari daftar warna yang telah ditentukan sebelumnya.
2. **send_feedback:**
    - Fungsi ini digunakan oleh server untuk mengirimkan feedback ke klien setelah menerima jawaban dari klien. Feedback ini berisi informasi tentang kebenaran jawaban klien.
3. **check_answer:**
    - Fungsi ini digunakan oleh server untuk memeriksa kebenaran jawaban klien terhadap kata warna yang dikirimkan. Ini membandingkan jawaban klien dengan kata warna yang sebenarnya, mengabaikan perbedaan kapitalisasi.


## Screenshoot Cara Penggunaaan serta Contoh ketika Program Berjalan
