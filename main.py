# UTS Mini Project - Monitoring Kualitas Sinyal (SNR)
# Nama: Athifah Rahma
# NIM: 03041382631144
# Kelas: Teknik Elektro B Palembang
# Kelompok: B - Telekomunikasi

data_snr = [
    5, 8, 11, 14, 18, 22, 27, 9, 16, 24,
    12, 30, 7, 20, 15,
    0, 9.9, 10, 19.9, 20
]

def kualitas_sinyal(snr):
    """Mengembalikan kategori SNR: RENDAH (<10), BAIK (10 sampai <20),
    atau SANGAT BAIK (>=20)."""
    if snr < 10:
        return "RENDAH"
    elif snr < 20:
        return "BAIK"
    else:
        return "SANGAT BAIK"

def hitung_kategori(data):
    """Menghitung jumlah nilai pada masing-masing kategori SNR."""
    hasil = {"RENDAH": 0, "BAIK": 0, "SANGAT BAIK": 0}
    for snr in data:
        hasil[kualitas_sinyal(snr)] += 1
    return hasil

def rata_rata(data):
    """Menghitung rata-rata SNR; mengembalikan 0 jika data kosong."""
    if not data:
        return 0
    return sum(data) / len(data)

def main():
    print("MONITORING KUALITAS SINYAL (SNR)")
    print("-" * 42)
    print(f"Jumlah data       : {len(data_snr)}")
    print(f"Nilai minimum     : {min(data_snr):g} dB")
    print(f"Nilai maksimum    : {max(data_snr):g} dB")
    print("\nKategori setiap data:")
    for nomor, snr in enumerate(data_snr, start=1):
        print(f"{nomor:2}. {snr:g} dB -> {kualitas_sinyal(snr)}")
    print("\nRekap kategori:")
    for kategori, jumlah in hitung_kategori(data_snr).items():
        print(f"{kategori:13}: {jumlah} data")
    print(f"Rata-rata SNR    : {rata_rata(data_snr):.2f} dB")

if __name__ == "__main__":
    main()
