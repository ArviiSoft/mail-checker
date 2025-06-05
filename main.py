import re
import os
import time
from datetime import datetime
import dns.resolver
import whois

DISPOSABLE_DOMAINS = [
    "mailinator.com", "10minutemail.com", "tempmail.org", "guerrillamail.com",
    "yopmail.com", "trashmail.com", "getnada.com", "fakeinbox.com",
    "dispostable.com", "moakt.com", "temp-mail.org", "maildrop.cc",
    "mytemp.email", "throwawaymail.com", "mailcatch.com", "spambox.me", "tempmail100.com", "temp-mail.io", "mailnesia.com", "mail-temporaire.com", "spambog.com",
    "spambog.de", "spambog.com.br", "spambog.ru", "spambog.eu", "spambog.fr",
]

def yasal_uyari():
    print("#############################################")
    print("      YASAL UYARI - LEGAL DISCLAIMER         ")
    print("#############################################\n")
    print("Bu araç sadece eğitim ve bilgilendirme amaçlıdır.")
    print("E-Posta sahibinin rızası olmadan bilgi toplamak YASAL DEĞİLDİR.")
    print("Geliştirici (Alkan - ArviS), bu aracın kötüye kullanımından sorumlu değildir.")

    input("\nDevam etmek için ENTER tuşuna bas...")

def email_gecerli_mi(email):
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(regex, email) is not None

def mx_kaydi_var_mi(email):
    try:
        domain = email.split("@")[1]
        mx_kayitlari = dns.resolver.resolve(domain, "MX")
        return True if mx_kayitlari else False
    except Exception:
        return False

def whois_bilgisi_al(domain):
    try:
        w = whois.whois(domain)
        return {
            "domain_name": w.domain_name,
            "registrar": w.registrar,
            "creation_date": w.creation_date,
            "expiration_date": w.expiration_date
        }
    except Exception:
        return {
            "domain_name": "Bilinmiyor.",
            "registrar": "Bilinmiyor.",
            "creation_date": "Bilinmiyor.",
            "expiration_date": "Bilinmiyor."
        }

def disposable_mi(email):
    domain = email.split("@")[1].lower()
    return domain in DISPOSABLE_DOMAINS

def kaydet(email, gecerli, mx_var, whois_info, disposable):
    klasor = "Output"
    os.makedirs(klasor, exist_ok=True)
    dosya_adi = os.path.join(klasor, f"{email.replace('@', '_at_')}.txt")
    
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write(f"Tarih: {datetime.now()}\n")
        f.write(f"E-Posta: {email}\n")
        f.write(f"Geçerli mi?: {'EVET' if gecerli else 'HAYIR'}\n")
        f.write(f"MX Kaydı Var mı?: {'EVET' if mx_var else 'HAYIR'}\n")
        f.write(f"Disposable mı?: {'EVET' if disposable else 'HAYIR'}\n\n")

        f.write("WHOIS Bilgileri:\n")
        f.write(f"Domain: {whois_info['domain_name']}\n")
        f.write(f"Registrar: {whois_info['registrar']}\n")
        f.write(f"Oluşturulma Tarihi: {whois_info['creation_date']}\n")
        f.write(f"Bitiş Tarihi: {whois_info['expiration_date']}\n")

    print(f"\nSonuç(lar) Kaydedildi: {dosya_adi}")

def main():
    yasal_uyari()
    os.system("cls" if os.name == "nt" else "clear")

    print("Mail Checker Tooluna Hoş Geldin\n")
    email = input("Kontrol edilecek E-Posta adresini gir \n> ")

    if not email:
        print("E-Posta adresi boş olamaz.")
        return

    gecerli = email_gecerli_mi(email)
    print("\nE-Posta geçerlilik kontrolü yapılıyor...")
    time.sleep(1)
    print(f"E-Posta geçerli mi?: {'EVET' if gecerli else 'HAYIR'}")

    print("\nMX kaydı kontrol ediliyor...")
    mx_var = mx_kaydi_var_mi(email)
    time.sleep(1)
    print(f"MX kaydı mevcut mu?: {'EVET' if mx_var else 'HAYIR'}")

    domain = email.split("@")[1]
    print("\nWHOIS bilgileri alınıyor...")
    whois_info = whois_bilgisi_al(domain)
    time.sleep(1)
    print(f"WHOIS bilgileri alındı.")

    print("\nDisposable kontrolü yapılıyor...")
    disposable = disposable_mi(email)
    time.sleep(1)
    print(f"Geçici E-Posta mı?: {'EVET' if disposable else 'HAYIR'}")

    kaydet(email, gecerli, mx_var, whois_info, disposable)

if __name__ == "__main__":
    main()