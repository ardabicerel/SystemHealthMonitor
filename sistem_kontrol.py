import psutil
import os
import subprocess
import time

try:
    while True:

        KIRMIZI = "\033[91m"
        NORMAL = "\033[0m"


        bellek = psutil.virtual_memory()
        disk_c = psutil.disk_usage("C:")
        disk_d = psutil.disk_usage("D:")
        cpu_usage = psutil.cpu_percent(interval=10)
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

        bos_bellek = bellek.available / (1024 ** 3)

        toplam_disk_c = disk_c.total / (1024 ** 3)
        bos_disk_c = disk_c.free / (1024 ** 3)

        toplam_disk_d = disk_d.total / (1024 ** 3)
        bos_disk_d = disk_d.free / (1024 ** 3)

        if bellek.percent > 90:
            bellek_mesaji = f"{KIRMIZI}!!! KRITIK BELLEK KULLANIMI: %{bellek.percent}{NORMAL}"
        else:
            bellek_mesaji = f"Bellek Kullanımı: %{bellek.percent}"

        if cpu_usage > 80:
            cpu_mesaji = f"{KIRMIZI}!!! YUKSEK CPU KULLANIMI: %{cpu_usage}{NORMAL}"
        else:
            cpu_mesaji = f"CPU Kullanımı: %{cpu_usage}"

        try:
            disk_e = psutil.disk_usage("E:")
            toplam_disk_e = f"{disk_e.total / (1024**3):.2f} GB"
        except:
            toplam_disk_e = "Disk Takılı Değil"

        print("----------------------------------\n")
        
        print(bellek_mesaji)
        print(f"Boş Bellek: {bos_bellek:.2f} GB\n")

        print(f"Toplam Disk(C): {toplam_disk_c:.2f} GB")
        print(f"Boş Disk(C): {bos_disk_c:.2f} GB\n")

        print(f"Toplam Disk(D): {toplam_disk_d:.2f} GB")
        print(f"Boş Disk(D): {bos_disk_d:.2f} GB\n")

        print(f"Toplam Disk(E): {toplam_disk_e}\n")

        print(cpu_mesaji, end="\n")
        print("----------------------------------")

        try:
            with open("system_logs.txt", "a", encoding="utf-8") as dosya:
                dosya.write(f"Zaman: {time.ctime()} | CPU: %{cpu_usage} | RAM Kullanımı: %{bellek.percent:.2f}\n")
        except:
            print("Log dosyasına yazılamadı!")

except KeyboardInterrupt:
    print("\nProgram kullanıcı tarafından durduruldu.")