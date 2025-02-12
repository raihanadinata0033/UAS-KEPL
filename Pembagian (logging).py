import logging

# Konfigurasi dasar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def bagi(a, b):
    try:
        hasil = a / b
        logging.info(f'Pembagian berhasil: {a} / {b} = {hasil}')
        return hasil
    except ZeroDivisionError:
        logging.error('Terjadi kesalahan: Pembagian oleh nol tidak diperbolehkan')
        return None

# Contoh penggunaan
bagi(10, 2)
bagi(10, 0)