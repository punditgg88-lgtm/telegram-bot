import base64

# Ganti dengan username bot kamu
BOT_USERNAME = "penyuka_lendir62bot"

def buat_link(deskripsi: str) -> str:
    # Encode teks ke base64 (URL safe, tanpa = di akhir biar lebih rapi)
    encoded = base64.urlsafe_b64encode(deskripsi.encode()).decode().rstrip("=")
    return f"https://t.me/{BOT_USERNAME}?start={encoded}"

if __name__ == "__main__":
    while True:
        teks = input("Masukkan deskripsi (atau ketik 'exit' untuk keluar): ")
        if teks.lower() == "exit":
            break
        link = buat_link(teks)
        print(f"✅ Link jadi: {link}\n")
