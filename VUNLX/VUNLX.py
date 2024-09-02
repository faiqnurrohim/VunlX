import socket
import os
import sys

# Fungsi untuk membersihkan tampilan terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menampilkan header dengan tampilan custom
def show_header():
    print(r"""
██    ██ ██    ██ ██      ███    ██ ██   ██ 
██    ██ ██    ██ ██      ████   ██ ██  ██  
██    ██ ██    ██ ██      ██ ██  ██ █████   
██    ██ ██    ██ ██      ██  ██ ██ ██  ██  
 ██████   ██████  ███████ ██   ████ ██   ██ 
    """)
    print("Cybersecurity Tool\n")

# Fungsi untuk menampilkan menu dan mendapatkan pilihan pengguna
def show_menu():
    print("1. Port Scanner")
    print("2. Vulnerability Checker")
    print("3. Service Enumerator")
    print("4. Exit\n")
    choice = input("Pilih fitur yang ingin Anda gunakan (1-4): ")
    return choice

# Fungsi untuk melakukan port scanning
def port_scanner(target):
    print(f"Memindai target: {target}")
    for port in range(1, 1025):  # Memindai port 1-1024
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} terbuka")
        sock.close()

# Fungsi untuk memeriksa kerentanan pada port yang terbuka
def vulnerability_checker(target):
    # Dummy implementation
    print(f"Memeriksa kerentanan pada target: {target}")
    vulnerable_ports = [21, 22, 80]
    for port in vulnerable_ports:
        print(f"Port {port} pada {target} mungkin rentan!")

# Fungsi untuk enumerasi layanan pada port yang terbuka
def service_enumerator(target):
    print(f"Enumerasi layanan pada target: {target}")
    for port in range(1, 1025):  # Memindai port 1-1024
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                banner = sock.recv(1024).decode('utf-8').strip()
                print(f"Port {port} menjalankan layanan: {banner}")
            except:
                print(f"Port {port} terbuka tetapi layanan tidak dapat diidentifikasi")
        sock.close()

# Fungsi untuk menampilkan pilihan setelah fitur selesai digunakan
def post_action_menu():
    print("\n1. Kembali ke Menu Utama")
    print("2. Exit\n")
    choice = input("Pilih aksi selanjutnya (1-2): ")
    return choice

# Main program loop
def main():
    while True:
        clear_screen()
        show_header()
        choice = show_menu()
        
        if choice == '1':
            target = input("Masukkan IP address target: ")
            clear_screen()
            port_scanner(target)
        elif choice == '2':
            target = input("Masukkan IP address target: ")
            clear_screen()
            vulnerability_checker(target)
        elif choice == '3':
            target = input("Masukkan IP address target: ")
            clear_screen()
            service_enumerator(target)
        elif choice == '4':
            print("Terima kasih telah menggunakan VulnXplorer!")
            break  # Keluar dari loop untuk mengakhiri program
        else:
            print("Pilihan tidak valid, coba lagi.")
        
        post_action = post_action_menu()
        if post_action == '2':
            print("Terima kasih telah menggunakan VulnXplorer!")
            break

if __name__ == "__main__":
    main()