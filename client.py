#program klien 
import socket

def main():
    # Inisialisasi soket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Kirim permintaan koneksi ke server
    client_socket.sendto(b"Connect", ('localhost', 12345))

    total_points = 0  # Inisialisasi jumlah total poin

    while True:
        # Terima kata warna dari server
        recv_data, _ = client_socket.recvfrom(1024)
        color_eng = recv_data.decode()

        # Tampilkan kata warna
        print("\nKata warna dalam bahasa Inggris:", color_eng)

        # Beri jawaban dalam bahasa Indonesia
        color_ind = input("Masukkan kata warna dalam bahasa Indonesia: ")

        # Kirim jawaban ke server
        client_socket.sendto(color_ind.encode(), ('localhost', 12345))

        # Terima feedback dari server
        feedback_data, _ = client_socket.recvfrom(1024)
        feedback_info = feedback_data.decode().split(":")
        feedback = feedback_info[0]
        if len(feedback_info) > 1:
            message = feedback_info[1]
        else:
            message = "Pesan feedback tidak valid."

        # Tampilkan feedback
        print(message)
        print("Jumlah poin:", feedback)

        # Update jumlah total poin jika feedback dapat diubah menjadi integer
        try:
            total_points += int(feedback)
        except ValueError:
            print("Nilai feedback tidak valid")

        # Tampilkan jumlah total poin saat ini
        print("Jumlah total poin saat ini:", total_points)

if __name__ == "__main__":
    main()