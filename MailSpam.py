import smtplib
import time

def spam_attack(sender_email, password, target_email, message_body, count=10):
    try:
        # SMTP sunucusuna bağlan
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        # Spam e-postalarını gönder
        for i in range(count):
            subject = "SPAM MAIL"
            body = f"{message_body} - Spam mail number {i+1}"
            message = f"Subject: {subject}\n\n{body}"
            
            # E-posta gönder
            server.sendmail(sender_email, target_email, message)
            print(f"Spam mail {i+1} gönderildi.")
            time.sleep(1)  # 1 saniye bekle
        
        server.quit()
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def main():
    # Sade giriş ekranı
    print("**************************")
    print("     HACKLAB ATTACKER    ")
    print("**************************")

    # Kullanıcı bilgilerini al
    sender_email = input("Gmail Adresinizi Girin: ")
    password = input("Gmail Şifrenizi Girin: ")
    target_email = input("Saldırılacak Gmail Adresini Girin: ")
    message_body = input("Spam e-posta için mesajınızı yazın: ")

    # Alınan bilgileri ekranda göster
    print("\nBilgileriniz:")
    print("---------------")
    print(f"Gmail Adresiniz: {sender_email}")
    print(f"Gmail Şifreniz: {password}")
    print(f"Saldırılacak Adres: {target_email}")
    print(f"Mesajınız: {message_body}")
    print("---------------\n")

    # Kullanıcı onayı
    confirm = input("Emin misiniz? (Evet/Hayır): ")
    if confirm.lower() != 'evet':
        print("İşlem iptal edildi.")
        return

    print("SPAM attack başlatılıyor...")
    time.sleep(2)

    # Spam e-posta gönderme işlemi
    spam_attack(sender_email, password, target_email, message_body, count=10)
    
    print("Saldırı tamamlandı. Teşekkürler!")

if __name__ == "__main__":
    main()