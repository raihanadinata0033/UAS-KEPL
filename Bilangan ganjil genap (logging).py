import logging

# Konfigurasi dasar logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def cek_angka(n):
    if n % 2 == 0:
        logging.info(f'Angka {n} adalah bilangan genap')
    else:
        logging.warning(f'Angka {n} adalah bilangan ganjil')

def hitung_pangkat(x, y):
    try:
        hasil = x ** y
        logging.debug(f'Menghitung {x} pangkat {y}: {hasil}')
        return hasil
    except Exception as e:
        logging.error(f'Terjadi kesalahan: {e}')
        return None

# Contoh penggunaan
cek_angka(10)
cek_angka(7)
hitung_pangkat(2, 3)
hitung_pangkat(5, 2)