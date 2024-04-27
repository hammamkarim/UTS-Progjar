# program server
import socket
import random
import time

# List warna dalam bahasa Inggris dan Indonesia
colors_eng = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white', 'gold', 'cyan', 'magenta', 'olive', 'maroon']
colors_ind = ['merah', 'biru', 'hijau', 'kuning', 'jingga', 'ungu', 'pink', 'coklat', 'hitam', 'putih', 'emas', 'cyan', 'magenta', 'zaitun', 'marun']

# Fungsi untuk mengirimkan kata warna acak ke semua klien
def send_color(sock, addr):
    color_index = random.randint(0, len(colors_eng) - 1)
    color_eng = colors_eng[color_index]
    color_ind = colors_ind[color_index]
    message = color_eng.encode()
    sock.sendto(message, addr)
    return color_ind

# Fungsi untuk mengirimkan nilai feedback ke klien
def send_feedback(sock, addr, feedback):
    message = feedback.encode()
    sock.sendto(message, addr)  # Mengirimkan sebagai byte

# Fungsi untuk mengecek jawaban klien
def check_answer(recv_color, correct_color):
    return recv_color.lower() == correct_color.lower()

# Fungsi utama
def main():
    # Inisialisasi soket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))

    print("Server menunggu koneksi...")

    while True:
        # Terima permintaan klien
        data, addr = server_socket.recvfrom(1024)
        print("Berhasil tersambung ke", addr)

        # Mulai permainan
        while True:
            # Kirim kata warna acak ke klien
            correct_color = send_color(server_socket, addr)
            print("Mengirim kata warna:", correct_color)

            # Set timeout untuk menerima jawaban dari klien
            server_socket.settimeout(5)
            try:
                # Terima jawaban dari klien
                recv_data, _ = server_socket.recvfrom(1024)
                recv_color = recv_data.decode()

                # Periksa jawaban klien
                if check_answer(recv_color, correct_color):
                    send_feedback(server_socket, addr, '100:Jawaban benar!')
                else:
                    send_feedback(server_socket, addr, '0:Jawaban salah!')

            except socket.timeout:
                print("Waktu habis, tidak ada jawaban dari klien.")
                break

            # Beri jeda 10 detik sebelum mengirim kata warna berikutnya
            time.sleep(10)

if __name__ == "__main__":
    main()



