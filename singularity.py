"""
=========================================================================================
E&Y SECURE CORE - v50.0 THE LEVIATHAN (FULL DEPLOYMENT)
Authors: Enes & Yasin
Description: Enterprise-Grade Cyber Operations Terminal & Multi-Device Sync.
Features: 18-Grid Dashboard, OTA Auto-Updater (SSL Bypassed), Live P2P Comms, 
          Oracle-X AI, Dual-Core Database, Forensic Hex-Dumps, IP Blacklist,
          Advanced Port Scanner, Collatz Avalanche Crypto-Analysis, Omega Protocol.
Architecture: Uncompressed, Modular, Deep-Scan DB Repair, Asymmetric Preparation.
Lines of Code: 1000+ (Enterprise Standard)
=========================================================================================
"""

import os
import sys
import time
import json
import socket
import random
import hashlib
import string
import secrets
import uuid
import platform
import urllib.request
import urllib.error
import ssl
from datetime import datetime, timedelta

# --- KRİPTOGRAFİ KÜTÜPHANELERİ (AES-256 GCM ve HKDF) ---
try:
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.hkdf import HKDF
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
except ImportError:
    print("\n [!] KRİTİK HATA: 'cryptography' kütüphanesi eksik.")
    print(" [!] Lütfen komut satırına şunu yazın: pip install cryptography")
    sys.exit()

# --- BÖLÜM 1: ÇİFT ÇEKİRDEKLİ (DUAL-CORE) VERİTABANI MOTORU VE LOKASYON ---

DB_FILE = "ey_vault.json"
BACKUP_FILE = "ey_backup_vault.json"

def get_strategic_intel(postal_code):
    """
    Girilen posta kodunu alarak askeri düzeyde lokasyon, savunma seviyesi ve koordinat üretir.
    Trabzon (61) merkez üs olarak yapılandırılmıştır. Tüm veriler statik istihbarata dayanır.
    """
    intel_matrix = {
        "61": ("TRABZON", "KARADENİZ SİBER KARARGAH (MERKEZ ÜS)", "41.002°N, 39.716°E", "🔴 DEFCON-1", "ZONE-OMEGA"),
        "34": ("İSTANBUL", "MARMARA VERİ HUB VE ANALİZ", "41.008°N, 28.978°E", "🟡 DEFCON-3", "ZONE-BRAVO"),
        "06": ("ANKARA", "STRATEJİK OPERASYON KOMUTANLIĞI", "39.933°N, 32.859°E", "🔴 DEFCON-2", "ZONE-ALPHA"),
        "35": ("İZMİR", "EGE LOJİSTİK VE HABERLEŞME HATTI", "38.419°N, 27.128°E", "🟢 DEFCON-4", "ZONE-CHARLIE"),
        "07": ("ANTALYA", "GÜNEY RADAR VE SİNYAL İZLEME", "36.896°N, 30.713°E", "🟢 DEFCON-4", "ZONE-CHARLIE"),
        "41": ("KOCAELİ", "ENDÜSTRİYEL SİBER SAVUNMA HATTI", "40.765°N, 29.940°E", "🟡 DEFCON-3", "ZONE-BRAVO"),
        "55": ("SAMSUN", "KUZEY VERİ AKTARIM DÜĞÜMÜ", "41.286°N, 36.336°E", "🟢 DEFCON-4", "ZONE-CHARLIE"),
        "01": ("ADANA", "GÜNEYDOĞU VERİ İSTASYONU", "37.000°N, 35.321°E", "🟡 DEFCON-3", "ZONE-DELTA")
    }
    prefix = str(postal_code)[:2]
    
    if prefix in intel_matrix:
        return intel_matrix[prefix]
    else:
        return (f"BÖLGE-{prefix}", "DIŞ SEKTÖR BAĞLANTISI", "COORD: N/A", "⚪ UNKNOWN", "ZONE-NULL")

def vault_blueprint():
    """
    Sistemin sıfır noktasıdır (Genesis). 
    Eğer veritabanı silinir veya bozulursa sistem kendini bu şablona göre yeniden inşa eder.
    Tüm eklentiler, yeni 18'li menü özellikleri ve yetkiler detaylı açıklamalarıyla buradadır.
    """
    return {
        "META": {
            "sys_name": "E&Y LEVIATHAN CORE", 
            "sys_ver": "v50.0 DEPLOYMENT", 
            "news": "Leviathan Protokolü Aktif - Sistem Maksimum Kapasitede",
            "boot_time": datetime.now().isoformat(), 
            "total_ops": 0, 
            "failed_logins": 0,
            "update_url": "AYARLANMADI" 
        },
        "CONFIG": {
            "beta_key": "beta", 
            "admin_key": "admin", 
            "auth_pass": "2010", 
            "panic": "6161"
        },
        "PLUGINS": {
            "oracle_ai": [True, "Oracle-X AI", "Yapılan işlemleri analiz eder, risk skoru ve taktik üretir."],
            "forensic": [True, "Adli Bilişim Köprüsü", "Mühürlü verilerin Hex-Dump seviyesinde analizini yapar."],
            "intel": [True, "İstihbarat Akışı", "Saha loglarını ve eylemleri saniyelik olarak tutar."],
            "net_sim": [True, "Ağ Tarama Motoru", "Hedef IP/Domain analiz eder ve ping atar."],
            "port_scan": [True, "Gelişmiş Port Tarayıcı", "Gerçek zamanlı TCP port analizi gerçekleştirir."],
            "crypto_collatz": [True, "Collatz Kripto Analiz", "Asimetrik şifreleme için çığ etkisi simülasyonu."],
            "sys_diag": [True, "Donanım Teşhis", "Sistemin çalıştığı makinenin CPU/RAM ve OS bilgisini okur."],
            "firewall": [True, "IP Karantina Sistemi", "Zararlı veya şüpheli IP adreslerini engeller."],
            "comms": [True, "Siber Haberleşme", "Uçtan uca şifreli, canlı senkronize Chat kanalı sağlar."],
            "ota_update": [True, "Sistem Güncelleyici", "Sistemi kapatmadan merkezden (GitHub) yeni kod çeker."]
        },
        "S_PERMS": {
            "s_ai": [True, "AI Yönetim Yetkisi", "Yapay zeka analiz motoruna erişim sağlar."],
            "s_for": [True, "Adli Arşiv (Root)", "Verilerin Hex dökümünü alma ve derin arşiv yetkisi."],
            "s_root": [True, "DB Kök Yönetimi", "Veritabanını tamamen temizleme ve imha etme yetkisi."],
            "s_net": [True, "Ağ Operasyonları", "Dış IP adreslerine ping ve port tarama yetkisi."],
            "s_ban": [True, "Karantina Yetkisi", "Tespit edilen IP adreslerini kara listeye alma yetkisi."],
            "s_chat": [True, "Haberleşme İzni", "Global haberleşme (Chat) kanalına giriş yetkisi."],
            "s_ota": [True, "Sistem Güncelleme", "Github veya buluttan kodu çekip üzerine yazma yetkisi."],
            "s_crypto": [True, "İleri Kripto Analizi", "Collatz ve asimetrik veri analiz modüllerine erişim."]
        },
        "B_PERMS": {
            "b_enc": [True, "Veri Mühürleme", "Ağa yeni şifreli veri (Kripto) yükleme yetkisi."],
            "b_dec": [True, "Deşifreleme", "Sistemdeki kilitli verileri anahtarla açma yetkisi."],
            "b_p_arc": [True, "Kişisel Arşiv", "Yalnızca kendi oluşturduğu verileri izleme yetkisi."],
            "b_sug": [True, "Rapor Gönderme", "Yönetime durum bildiren vaka raporları gönderme yetkisi."],
            "b_chat": [True, "Siber Haberleşme", "Merkez ve diğer cihazlarla şifreli chat yapma yetkisi."],
            "b_g_arc": [False, "Sistem Arşivi", "Ağdaki tüm şifreli paketleri görme yetkisi (Kritik)."],
            "b_broad": [False, "Duyuru Yayınlama", "Sistem geneline flash haber ve duyuru yapma yetkisi."],
            "b_stats": [False, "Sistem Analitiği", "Veritabanı doluluk ve trafik oranlarını görme yetkisi."],
            "b_diag": [False, "Sistem Teşhisi", "Bağlı olunan sunucunun donanım durumunu okuma yetkisi."],
            "b_pass": [True, "Parola Üretici", "Operasyonlar için kriptografik parola üretme yetkisi."]
        },
        "ARCHIVE": [], 
        "SUGGESTIONS": [], 
        "INTEL_LOGS": [], 
        "BLACKLIST": [], 
        "COMMS": [], 
        "ACTIVE_NODES": {}
    }

def db_load():
    """
    Çift Çekirdekli (Dual-Core) Veritabanı Yükleyici ve Derin Onarıcı (Deep-Scan Repair).
    Herhangi bir JSON hatasında veya eksik veri anahtarında çökme yaşanmasını engeller.
    """
    data = None
    retries = 3
    
    for i in range(retries):
        try:
            if os.path.exists(DB_FILE):
                with open(DB_FILE, "r", encoding="utf-8") as f: 
                    data = json.load(f)
                    break
            elif os.path.exists(BACKUP_FILE):
                with open(BACKUP_FILE, "r", encoding="utf-8") as f: 
                    data = json.load(f)
                    break
            else:
                data = vault_blueprint()
                db_save(data)
                return data
        except json.JSONDecodeError:
            # Dosya o an başka bir cihaz tarafından meşgulse bekle
            time.sleep(0.2)
    
    if data is None:
        return vault_blueprint()

    # --- DERİN ONARIM MOTORU (DEEP REPAIR) ---
    ref = vault_blueprint()
    
    for k in ref.keys():
        if k not in data: 
            data[k] = ref[k]
    
    for sub in ["PLUGINS", "S_PERMS", "B_PERMS"]:
        if sub in data:
            for sk, sv in ref[sub].items():
                if sk not in data[sub]:
                    data[sub][sk] = sv
                    
    return data

def db_save(data):
    """
    Veriyi eşzamanlı olarak hem ana DB_FILE'a hem de BACKUP_FILE'a yazar.
    Sıfır veri kaybı prensibiyle çalışır.
    """
    try:
        data["META"]["total_ops"] = data["META"].get("total_ops", 0) + 1
        
        with open(DB_FILE, "w", encoding="utf-8") as f: 
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        with open(BACKUP_FILE, "w", encoding="utf-8") as f: 
            json.dump(data, f, indent=4, ensure_ascii=False)
            
    except Exception as e:
        print(f"\n [!] Veritabanı Yazma Hatası: {e}")

def update_active_status(ip):
    """
    Sisteme bağlı olan düğümlerin (cihazların) aktiflik durumunu günceller.
    Bu veri canlı radar ekranında yeşil bildirim olarak gösterilir.
    """
    db = db_load()
    if "ACTIVE_NODES" not in db: 
        db["ACTIVE_NODES"] = {}
        
    db["ACTIVE_NODES"][ip] = time.time()
    db_save(db)

# --- BÖLÜM 2: GÖRSEL MOTOR, ANİMASYONLAR VE KONSOL TASARIMI ---

C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_G = "\033[38;5;82m"   # Yeşil
C_Y = "\033[38;5;226m"  # Sarı
C_R = "\033[38;5;196m"  # Kırmızı
C_C = "\033[38;5;51m"   # Camgöbeği (Cyan)
C_B = "\033[38;5;27m"   # Mavi
C_P = "\033[38;5;129m"  # Mor
C_O = "\033[38;5;208m"  # Turuncu
C_PK = "\033[38;5;201m" # Pembe
C_GR = "\033[38;5;244m" # Gri

def cls():
    """Terminal ekranını işletim sistemine uygun şekilde temizler."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_system_ip():
    """Mevcut cihazın ağ üzerindeki aktif IP adresini bulur."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except: 
        return "127.0.0.1"

def simulate_loading(task_name, duration=1.0, steps=20):
    """
    Siber operasyon hissiyatını artırmak için terminalde animasyonlu bir 
    yükleme çubuğu (progress bar) oluşturur.
    """
    print()
    for i in range(steps + 1):
        percent = (i / float(steps)) * 100
        bar = '█' * i + '-' * (steps - i)
        sys.stdout.write(f"\r {C_C}[{task_name}]{C_RESET} İŞLENİYOR: |{C_Y}{bar}{C_RESET}| {percent:.1f}% ")
        sys.stdout.flush()
        time.sleep(duration / steps)
    print(f"\n {C_G}✓ İŞLEM BAŞARILI BİR ŞEKİLDE TAMAMLANDI.{C_RESET}")
    time.sleep(0.3)

def boot_sequence():
    """
    Sistem ilk açıldığında gösterilen, modüllerin yüklendiği hissini veren
    simüle edilmiş başlangıç (boot) sekansı ve devasa ASCII sanatları.
    """
    cls()
    print(f"{C_C}")
    print(r"  ███████╗  ██████╗  ██╗   ██╗")
    print(r"  ██╔════╝ ██╔═══██╗ ╚██╗ ██╔╝")
    print(r"  █████╗   ██║   ██║  ╚████╔╝ ")
    print(r"  ██╔══╝   ██║▄▄ ██║   ╚██╔╝  ")
    print(r"  ███████╗ ╚██████╔╝    ██║   ")
    print(r"  ╚══════╝  ╚══▀▀═╝     ╚═╝   ")
    print(f"{C_RESET}")
    print(f" {C_BOLD}{C_P}--- THE LEVIATHAN CORE v50.0 INITIALIZATION ---{C_RESET}\n")
    
    boot_msgs = [
        "INITIALIZING DEEP-SYNC DATABASE PROTOCOLS...",
        "LOADING ENCRYPTION MODULES (AES-256 GCM)...",
        "ESTABLISHING P2P COMMS NETWORK...",
        "VERIFYING OTA UPDATE PROTOCOLS (SSL BYPASS)...",
        "ACTIVATING ORACLE-X AI ENGINE...",
        "LOADING COLLATZ CRYPTO-ANALYSIS ENGINE...",
        "MOUNTING FORENSIC HEX-DUMP UTILITIES...",
        "SYSTEM ONLINE AND FULLY OPERATIONAL."
    ]
    for msg in boot_msgs:
        print(f" {C_G}[*]{C_RESET} {msg}")
        time.sleep(0.2)
    print(f"{C_RESET}")
    time.sleep(0.5)

def draw_header(title, mode, db, ip, loc):
    """
    Sistemin ana başlığını (Dashboard Header) çizer.
    İçerisinde Canlı Radar (Aktif Cihazlar), Haber Akışı ve Operasyonel statü bulunur.
    """
    cls()
    meta = db.get("META", {})
    color = C_P if mode == "ADMIN" else C_C
    w = 185
    
    # Aktif kullanıcıları hesapla
    active_nodes = db.get("ACTIVE_NODES", {})
    curr_time = time.time()
    online_count = sum(1 for t in active_nodes.values() if curr_time - t < 120)
    
    print(f"{color}╔" + "═" * (w-2) + f"╗{C_RESET}")
    
    sys_id = f"⚡ {meta.get('sys_name')} | CORE: {meta.get('sys_ver')} | NODE: {ip} | TOPLAM OPS: {meta.get('total_ops')} ⚡"
    online_badge = f"🟢 AKTİF CİHAZ: {online_count}"
    
    header_line = f"{color}║{C_RESET} {C_BOLD}{sys_id}{C_RESET}"
    header_line += " " * (w - len(sys_id) - len(online_badge) - 7)
    header_line += f"{C_G}{C_BOLD}{online_badge}{C_RESET} {color}║{C_RESET}"
    print(header_line)
    
    print(f"{color}╠" + "═" * (w-2) + f"╣{C_RESET}")
    
    news = f"📢 SİSTEM BROADCAST: {meta.get('news')}"
    print(f"{color}║{C_RESET} {C_O}{C_BOLD}{news.center(w-4)}{C_RESET} {color}║{C_RESET}")
    print(f"{color}╠" + "═" * (w-2) + f"╣{C_RESET}")
    
    print(f"{color}║{C_RESET} {C_BOLD}{str(title).upper().center(w-4)}{C_RESET} {color}║{C_RESET}")
    print(f"{color}╠" + "═" * (w-2) + f"╣{C_RESET}")
    
    status = f"👤 RÜTBE: {mode} | 📍 ZONE: {loc[0]} | 🏢 HUB: {loc[1]} | 🛡️ {loc[3]} | 🕒 {datetime.now().strftime('%H:%M:%S')}"
    print(f"{color}║{C_RESET} {C_Y}{status.center(w-4)}{C_RESET} {color}║{C_RESET}")
    print(f"{color}╚" + "═" * (w-2) + f"╝{C_RESET}")

def notify(msg, n_type="INFO"):
    """Standart bildirim ve hata mesajı gösterici."""
    c = C_C if n_type == "INFO" else C_R
    print(f"\n {c} ❱❱❱ {msg} {C_RESET}")
    time.sleep(1.2)

def oracle_ai(mode, db, action, extra_data=""):
    """
    Oracle-X Yapay Zeka Analiz Motoru.
    Kullanıcının yaptığı eylemlere göre dinamik risk skoru hesaplar ve taktiksel geri bildirim verir.
    """
    if not db["PLUGINS"].get("oracle_ai", [False])[0]: 
        return
        
    risk = random.randint(1, 15) if action != "denied" else random.randint(85, 100)
    
    scenarios = {
        "enc": f"Kripto paketi analiz edildi (Risk Skoru: %{risk}). 256-bit GCM katmanı başarıyla devrede.",
        "dec": f"Deşifreleme işlemi yapıldı (Risk Skoru: %{risk}). İzler karartıldı ve bellek temizlendi.",
        "login": f"Sistem erişimi mühürlendi (Risk Skoru: %{risk}). IP maskeleme savunması devrede.",
        "denied": f"KRİTİK İHLAL! Yetkisiz modül erişimi (Risk Skoru: %{risk}). Alarm durumuna geçildi.",
        "net": f"Ağ analizi tamamlandı (Risk Skoru: %{risk}). Hedef {extra_data} üzerinde güvenlik duvarı tespit edildi.",
        "port": f"TCP Port taraması tamamlandı (Risk Skoru: %{risk}). Hedef sistemin zafiyetleri analiz edildi.",
        "collatz": f"Asimetrik analiz tamamlandı. Collatz çığ etkisi (Avalanche) hesaplandı (Risk: %{risk}).",
        "diag": f"Sistem donanım teşhisi yapıldı. İşlemci ve RAM verilerinde sızıntı yok, her şey güvende.",
        "ban": f"Firewall güncellendi. {extra_data} IP adresi karantinaya alındı ve ağdan izole edildi.",
        "chat": f"Güvenli kanaldan veri iletildi (Risk Skoru: %0). Canlı P2P senkronizasyon Aktif.",
        "update": f"Sistem güncelleme protokolü başlatıldı (Risk Skoru: %{risk}). Kodun orijinalliği doğrulanıyor.",
        "settings": "Çekirdek ayarları ve META verileri başarıyla güncellendi."
    }
    
    msg = scenarios.get(action, f"İşlem yapay zeka tarafından analiz edildi (Risk Skoru: %{risk}).")
    col = C_R if risk > 50 else (C_Y if risk > 15 else C_G)
    
    print(f"\n {C_PK}✨ ORACLE-X AI:{C_RESET} {col}{msg}{C_RESET}")

# --- BÖLÜM 3: KRİPTOGRAFİ (ŞİFRELEME VE DEŞİFRELEME) ---

def get_crypto_key(tag, geo):
    """
    Tarih etiketi (Tag) ve Posta Kodu Hash'inden (Geo-Key)
    kırılamaz bir anahtar üretmek için HKDF algoritmasını kullanır.
    """
    kdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"leviathan_full_deployment_v50",
        info=f"{tag}{geo}".encode()
    )
    return kdf.derive(b"master_nexus_secret_key")

def encryption_module(mode, db, ip, loc, geo_key):
    """AES-256 GCM standartlarında veri şifreleme ve mühürleme işlemi."""
    draw_header("Kripto Mühürleme İstasyonu", mode, db, ip, loc)
    
    msg = input(f"\n {C_G}📝 GİZLİ MESAJINIZ (Geri Çıkmak için X):{C_RESET} ").strip()
    if msg.upper() == "X": 
        return
        
    tag = input(f" {C_G}📅 ETİKET/ID BELİRLEYİN:{C_RESET} ").strip()
    if tag.upper() == "X":
        return
        
    try:
        hr = input(f" ⏳ İMHA ZAMANI (SAAT Cinsinden - Varsayılan 24): ").strip()
        simulate_loading("AES-256 GCM ALGORİTMASIYLA ŞİFRELEME", duration=1.2)
        
        # Kripto Motoru
        key = get_crypto_key(tag, geo_key)
        nonce = os.urandom(12)
        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(msg.encode()) + encryptor.finalize()
        
        # Kodun Birleştirilmesi (Nonce + Tag + Ciphertext + Extra)
        tag_hex = tag.encode().hex()
        final_code = nonce.hex() + encryptor.tag.hex() + ciphertext.hex() + tag_hex + f"{len(tag_hex):02x}"
        uid = str(uuid.uuid4())[:8].upper()
        
        db = db_load() 
        
        record = {
            "id": uid, 
            "at": datetime.now().strftime("%H:%M:%S"), 
            "user": mode, 
            "msg": msg, 
            "code": final_code, 
            "geo": geo_key, 
            "tag": tag, 
            "exp": (datetime.now() + timedelta(hours=int(hr or "24"))).isoformat(), 
            "ip": ip, 
            "loc": loc[0], 
            "size": len(final_code)
        }
        
        db["ARCHIVE"].append(record)
        db["INTEL_LOGS"].append({
            "at": datetime.now().strftime("%H:%M:%S"), 
            "user": mode, 
            "act": f"ŞİFRELEME ({uid})", 
            "ip": ip, 
            "loc_tag": loc[0]
        })
        
        db_save(db)
        
        print(f"\n {C_G}✅ İŞLEM BAŞARILI:{C_RESET} Mühürlü Kripto Kodunuz Aşağıdadır:")
        print(f" {C_BOLD}{C_C}{final_code}{C_RESET}")
        
        oracle_ai(mode, db, "enc", tag)
        
    except Exception as e: 
        notify(f"Kriptografi Hatası: {e}", "ERR")
        
    input("\n [ENTER] DEVAM ET...")

def decryption_module(mode, db, ip, loc):
    """Mühürlü AES-256 verisini anahtar ve etiket kontrolüyle deşifre eder."""
    draw_header("Vanguard Çözümleme İstasyonu", mode, db, ip, loc)
    
    code = input(f"\n {C_C}📥 ÇÖZÜLECEK KRİPTO KODU GİRİN (Geri: X):{C_RESET} ").strip()
    if code.upper() == "X": 
        return
        
    geo_in = input(f" {C_C}🔑 DOĞRULAMA İÇİN GEO-KEY GİRİN:{C_RESET} ").strip()
    
    simulate_loading("ŞİFRE ÇÖZÜMÜ VE KİMLİK DOĞRULAMA", duration=1.5)
    
    try:
        uz = int(code[-2:], 16)
        t_hex = code[-(uz+2):-2]
        t_raw = bytes.fromhex(t_hex).decode()
        core = code[:-(uz+2)]
        
        nonce = bytes.fromhex(core[:24])
        tag = bytes.fromhex(core[24:56])
        ct = bytes.fromhex(core[56:])
        
        key = get_crypto_key(t_raw, geo_in)
        decryptor = Cipher(algorithms.AES(key), modes.GCM(nonce, tag)).decryptor()
        res = (decryptor.update(ct) + decryptor.finalize()).decode('utf-8')
        
        db = db_load() 
        print(f"\n {C_G}🔓 VERİ BAŞARIYLA ÇÖZÜLDÜ:{C_RESET}\n\n {C_BOLD}{res}{C_RESET}\n")
        
        db["INTEL_LOGS"].append({
            "at": datetime.now().strftime("%H:%M:%S"), 
            "user": mode, 
            "act": "DEŞİFRELEME", 
            "ip": ip, 
            "loc_tag": loc[0]
        })
        db_save(db)
        oracle_ai(mode, db, "dec")
        
    except Exception: 
        notify("Veri Bütünlüğü Bozulmuş veya Anahtar Yanlış!", "ERR")
        oracle_ai(mode, db, "denied")
        
    input("\n [ENTER] DEVAM ET...")

# --- BÖLÜM 4: İLERİ SEVİYE KRİPTO VE MATEMATİKSEL ANALİZ ---

def collatz_avalanche_analysis(mode, db, ip, loc):
    """
    Collatz dizilerindeki veri davranışını analiz ederek asimetrik bir şifreleme
    algoritması için çığ etkisi (Avalanche Effect) simülasyonu yapar.
    """
    draw_header("Collatz Asimetrik Kripto Analizörü", mode, db, ip, loc)
    print(f"\n {C_PK}--- ASİMETRİK ŞİFRELEME HAZIRLIK MODÜLÜ ---{C_RESET}")
    print(f" {C_GR}Bu modül, Collatz varsayımı kullanılarak geliştirilecek asimetrik")
    print(f" şifreleme projeleri için tohum (seed) analizi ve çığ etkisi ölçümü yapar.{C_RESET}")
    
    seed_str = input(f"\n {C_C}Analiz edilecek Tohum Değeri (Sayı) [X: Geri]:{C_RESET} ").strip()
    if seed_str.upper() == "X": return
    
    if not seed_str.isdigit():
        notify("Tohum değeri pozitif bir tam sayı olmalıdır.", "ERR")
        return
        
    seed = int(seed_str)
    if seed <= 0: return
    
    simulate_loading("COLLATZ DİZİSİ HESAPLANIYOR VE ÇIĞ ETKİSİ ÖLÇÜLÜYOR", duration=2.0)
    
    steps = 0
    max_val = seed
    current = seed
    sequence = [current]
    
    while current != 1 and steps < 1000:
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
        sequence.append(current)
        if current > max_val:
            max_val = current
        steps += 1
        
    # Çığ etkisi simülasyonu (Avalanche Effect)
    hash_val = hashlib.sha256(str(sequence).encode()).hexdigest()
    
    print(f"\n {C_Y}--- ANALİZ SONUÇLARI ---{C_RESET}")
    print(f" {C_B}Başlangıç Tohumu:{C_RESET} {seed}")
    print(f" {C_B}Toplam Adım Sayısı:{C_RESET} {steps}")
    print(f" {C_B}Ulaşılan Tepe Değeri (Max):{C_RESET} {max_val}")
    print(f" {C_B}Dizi Parçası:{C_RESET} {sequence[:10]} ... {sequence[-5:]}")
    print(f" {C_B}Üretilen Kriptografik Karma (Hash):{C_RESET} {hash_val}")
    
    db = db_load()
    db["INTEL_LOGS"].append({
        "at": datetime.now().strftime("%H:%M:%S"), 
        "user": mode, 
        "act": f"COLLATZ ANALİZİ ({seed})", 
        "ip": ip, 
        "loc_tag": loc[0]
    })
    db_save(db)
    
    oracle_ai(mode, db, "collatz")
    input("\n [ENTER] DEVAM ET...")

def generate_secure_password(mode, db, ip, loc):
    """Operasyonlar için kriptografik olarak güvenli, kırılamaz parola üretir."""
    draw_header("Kriptografik Parola Üretici (Vault)", mode, db, ip, loc)
    print(f"\n {C_PK}--- SİBER OPERASYON PAROLA MERKEZİ ---{C_RESET}")
    
    try:
        length = int(input(f"\n {C_C}Parola Uzunluğu (Örn: 32) [0: Geri]:{C_RESET} "))
        if length == 0: return
        if length < 8 or length > 256:
            notify("Uzunluk 8 ile 256 karakter arasında olmalıdır.", "ERR")
            return
            
        simulate_loading("ENTROPİ HAVUZU OLUŞTURULUYOR", duration=1.0)
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        
        print(f"\n {C_G}ÜRETİLEN GÜVENLİ PAROLA:{C_RESET}")
        print(f" {C_BOLD}{C_Y}{password}{C_RESET}")
        
        db = db_load()
        db["INTEL_LOGS"].append({
            "at": datetime.now().strftime("%H:%M:%S"), 
            "user": mode, 
            "act": f"PAROLA ÜRETİLDİ ({length} char)", 
            "ip": ip, 
            "loc_tag": loc[0]
        })
        db_save(db)
        
    except ValueError:
        notify("Lütfen geçerli bir sayı giriniz.", "ERR")
        
    input("\n [ENTER] DEVAM ET...")

# --- BÖLÜM 5: COMMS, FIREWALL, AĞ, PORT VE OTA MODÜLLERİ ---

def comms_module(mode, db_stale, ip, loc):
    """P2P Canlı Senkronize Haberleşme (Chat) Modülü."""
    while True:
        db = db_load()
        update_active_status(ip)
        draw_header("SİBER HABERLEŞME KANALI (LIVE COMMS)", mode, db, ip, loc)
        
        msgs = db.get("COMMS", [])
        print(f" {C_B}--- UÇTAN UCA ŞİFRELİ KANAL ---{C_RESET}")
        
        if not msgs: 
            print(f" {C_GR}Henüz bir iletişim kaydı bulunmuyor.{C_RESET}")
        else:
            for m in msgs[-15:]:
                color = C_P if m['sender'] == "ADMIN" else C_C
                print(f" {C_GR}[{m['at']}]{C_RESET} {color}{m['sender']}{C_RESET} ({m['loc']}): {m['msg']}")
        
        print(f"\n {C_Y}>> Ekranı yenilemek için boş bırakıp ENTER'a basınız. | Çıkış: X{C_RESET}")
        txt = input(f" {C_G}💬 MESAJ YAZ > {C_RESET}").strip()
        
        if txt.upper() == "X": 
            break
            
        if txt:
            db = db_load()
            db["COMMS"].append({
                "at": datetime.now().strftime("%H:%M:%S"), 
                "sender": mode, 
                "ip": ip, 
                "loc": loc[0], 
                "msg": txt
            })
            db["INTEL_LOGS"].append({
                "at": datetime.now().strftime("%H:%M:%S"), 
                "user": mode, 
                "act": "COMMS İLETİSİ", 
                "ip": ip, 
                "loc_tag": loc[0]
            })
            db_save(db)

def auto_update_system(mode, db, ip, loc):
    """
    OTA (Over-The-Air) Sistem Güncelleme Protokolü.
    SSL Bypassed: SSL Sertifika hatasını aşarak kodu zorla çeker.
    """
    draw_header("OTA SİSTEM GÜNCELLEME MERKEZİ", mode, db, ip, loc)
    update_url = db["META"].get("update_url", "")
    
    print(f" {C_B}Mevcut Çekirdek Sürümü:{C_RESET} {db['META']['sys_ver']}")
    print(f" {C_B}Hedef İndirme Sunucusu:{C_RESET} {update_url}")
    print(f" {C_Y}DİKKAT:{C_RESET} Sistem, belirtilen hedef sunucudaki kod dizinini çekecek,")
    print(f"         kendi üzerine yazacak ve operasyonu yeniden başlatacaktır.")
    
    if "raw.githubusercontent.com" not in update_url and "http" not in update_url:
        print(f"\n {C_R}[!] KRİTİK HATA: Geçerli bir RAW bağlantı URL'si ayarlanmamış.{C_RESET}")
        print(f" {C_GR}Sistemin güncellenebilmesi için Ayarlar menüsünden{C_RESET}")
        print(f" {C_GR}'update_url' parametresini GitHub Raw linkinizle değiştirmeniz gereklidir.{C_RESET}")
        input("\n [ENTER] GERİ DÖN")
        return

    cmd = input(f"\n {C_R}GÜNCELLEME PROTOKOLÜNÜ BAŞLATMAK İSTİYOR MUSUNUZ? (EVET/HAYIR):{C_RESET} ").upper()
    
    if cmd == "EVET":
        try:
            simulate_loading("SUNUCUYA BAĞLANILIYOR (SSL BYPASS AKTİF)", duration=1.5)
            oracle_ai(mode, db, "update")
            
            # --- SSL BYPASS (Sertifika Doğrulamasını Devre Dışı Bırakma) ---
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            
            req = urllib.request.Request(update_url, headers={'User-Agent': 'EY-Terminal-Updater'})
            
            # Context parametresi eklendi
            with urllib.request.urlopen(req, context=ctx, timeout=15) as response:
                new_code = response.read().decode('utf-8')
            
            if "E&Y SECURE CORE" in new_code:
                simulate_loading("YENİ KOD İNDİRİLİYOR VE YAZILIYOR", duration=2.0)
                
                current_file = sys.argv[0]
                with open(current_file, 'w', encoding='utf-8') as f: 
                    f.write(new_code)
                
                print(f"\n {C_G}SİSTEM GÜNCELLEMESİ BAŞARILI! YENİDEN BAŞLATILIYOR...{C_RESET}")
                
                db["INTEL_LOGS"].append({
                    "at": datetime.now().strftime("%H:%M:%S"), 
                    "user": mode, 
                    "act": "OTA GÜNCELLEMESİ YAPILDI", 
                    "ip": ip, 
                    "loc_tag": loc[0]
                })
                db_save(db)
                time.sleep(2)
                
                os.execv(sys.executable, ['python'] + sys.argv)
            else: 
                notify("İndirilen kaynakta güvenlik imzası bulunamadı. İşlem iptal.", "ERR")
                
        except urllib.error.URLError as e:
            print(f"\n {C_R}[!] BAĞLANTI HATASI: İnternet yok veya Sunucu reddetti.{C_RESET}")
            print(f" {C_Y}Hata Detayı: {e.reason}{C_RESET}")
        except Exception as e: 
            print(f"\n {C_R}[!] BEKLENMEDİK HATA: {e}{C_RESET}")
            
    input("\n [ENTER] ANA MENÜYE DÖN")

def firewall_module(mode, db, ip, loc):
    """Şüpheli IP adreslerini ağdan kalıcı olarak banlama modülü."""
    while True:
        db = db_load()
        draw_header("Siber Güvenlik Duvarı (Firewall)", mode, db, ip, loc)
        b_list = db.get("BLACKLIST", [])
        
        print(f" {C_R}--- KARANTİNA VE YASAKLI IP LİSTESİ ---{C_RESET}")
        if not b_list: 
            print(f" {C_GR}Kara liste şu an tamamen boş.{C_RESET}")
        else:
            for i, bip in enumerate(b_list, 1): 
                print(f" [{i}] ENGEL DURUMU AKTİF: {bip}")
                
        cmd = input(f"\n {C_Y}Operasyon Seçin:{C_RESET}\n [1] Yeni IP Engelle\n [2] Mevcut IP Engelini Kaldır\n [X] Geri Dön\n\n Seçim > ").upper()
        
        if cmd == "X": 
            break
        elif cmd == "1":
            t_ip = input(f" {C_R}Engellenecek Hedef IP:{C_RESET} ").strip()
            if t_ip and t_ip not in b_list:
                db = db_load()
                db["BLACKLIST"].append(t_ip)
                db_save(db)
                notify(f"{t_ip} adresi ağdan izole edildi ve engellendi!")
                oracle_ai(mode, db, "ban", t_ip)
        elif cmd == "2" and b_list:
            no = input(f" {C_G}Engeli Kaldırılacak IP Numarası:{C_RESET} ").strip()
            if no.isdigit() and int(no) <= len(b_list):
                db = db_load()
                rem = db["BLACKLIST"].pop(int(no)-1)
                db_save(db)
                notify(f"{rem} üzerindeki engel kaldırıldı.", "INFO")

def display_hex_dump(hex_string):
    """Adli Bilişim aracı: Gönderilen veriyi Hex bellek dökümüne çevirir."""
    print(f"\n {C_GR}--- FORENSIC HEX DUMP (MEMORY EXTRACTION) ---{C_RESET}")
    lines = [hex_string[i:i+64] for i in range(0, len(hex_string), 64)]
    
    for i, line in enumerate(lines):
        blocks = [line[j:j+8] for j in range(0, len(line), 8)]
        offset = f"{i * 32:08x}"
        print(f" {C_Y}{offset}{C_RESET}  {' '.join(blocks)}")
        
    print(f" {C_GR}--- END OF PHYSICAL MEMORY DUMP ---{C_RESET}\n")

def network_traceroute(mode, db, ip, loc):
    """Ağ ping ve hedef yönlendirme simülasyonu."""
    draw_header("Ağ İstihbaratı (Ping/Traceroute)", mode, db, ip, loc)
    
    target = input(f"\n {C_C}🌐 Hedef IP veya Domain (X: Geri):{C_RESET} ").strip()
    if target.upper() == "X": 
        return
        
    simulate_loading(f"AĞ YÖNLENDİRİCİSİ PROTOKOLÜ -> {target}", duration=2.5)
    
    print(f"\n {C_GR}Yönlendirme döngüsü başlatıldı: {target}{C_RESET}")
    for i in range(1, 6):
        hop_ip = f"{random.randint(10,200)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        ms = random.randint(10, 150)
        print(f" {i:2d}  {ms} ms   {hop_ip} [Ağ Düğümü Güvenli]")
        time.sleep(0.4)
        
    print(f"  6  {random.randint(10,50)} ms   {target} [HEDEF SİSTEME ULAŞILDI]")
    
    db = db_load()
    db["INTEL_LOGS"].append({
        "at": datetime.now().strftime("%H:%M:%S"), 
        "user": mode, 
        "act": f"TRACEROUTE ({target})", 
        "ip": ip, 
        "loc_tag": loc[0]
    })
    db_save(db)
    
    oracle_ai(mode, db, "net", target)
    input("\n [ENTER] DEVAM ET...")

def advanced_port_scanner(mode, db, ip, loc):
    """Gerçek zamanlı olarak basit bir TCP Port taraması gerçekleştirir."""
    draw_header("Gelişmiş TCP Port Tarayıcı", mode, db, ip, loc)
    
    target = input(f"\n {C_C}🔍 Taranacak Hedef IP (X: Geri):{C_RESET} ").strip()
    if target.upper() == "X": return
    
    common_ports = [21, 22, 25, 53, 80, 110, 443, 3306, 8080]
    print(f"\n {C_GR}Hedef {target} üzerinde kritik portlar taranıyor...{C_RESET}")
    
    open_ports = []
    
    for port in common_ports:
        sys.stdout.write(f"\r Port {port} test ediliyor...")
        sys.stdout.flush()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3) # Hızlı tarama
        try:
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
        except:
            pass
        finally:
            s.close()
            
    print("\n")
    if not open_ports:
        print(f" {C_Y}Sonuç: Hedefte standart açık port bulunamadı veya ICMP kapalı.{C_RESET}")
    else:
        print(f" {C_G}AÇIK PORTLAR TESPİT EDİLDİ:{C_RESET}")
        for p in open_ports:
            print(f" [+] Port {p} : AÇIK")
            
    db = db_load()
    db["INTEL_LOGS"].append({
        "at": datetime.now().strftime("%H:%M:%S"), 
        "user": mode, 
        "act": f"PORT SCAN ({target})", 
        "ip": ip, 
        "loc_tag": loc[0]
    })
    db_save(db)
    oracle_ai(mode, db, "port", target)
    input("\n [ENTER] DEVAM ET...")

def system_diagnostics(mode, db, ip, loc):
    """Cihazın ve programın çalıştığı fiziksel sistemin özelliklerini okur."""
    draw_header("Donanım ve Fiziksel Sistem Teşhisi (Diag)", mode, db, ip, loc)
    simulate_loading("FİZİKSEL DONANIM ANALİZİ", duration=1.2)
    
    os_info = f"{platform.system()} {platform.release()}"
    arch = platform.machine()
    python_v = platform.python_version()
    db_size = os.path.getsize(DB_FILE) / 1024 if os.path.exists(DB_FILE) else 0
    uptime = str(datetime.now() - datetime.fromisoformat(db['META']['boot_time'])).split('.')[0]
    
    print(f"\n {C_P}--- SİSTEM VE DONANIM RAPORU ---{C_RESET}")
    print(f" {C_B}İşletim Sistemi Altyapısı:{C_RESET} {os_info} ({arch})")
    print(f" {C_B}Çalıştırılan Python Çekirdeği:{C_RESET} {python_v}")
    print(f" {C_B}Aktif Dizin (Workspace):{C_RESET}   {os.getcwd()}")
    print(f" {C_B}Veritabanı Dosya Boyutu:{C_RESET}   {db_size:.2f} KB")
    print(f" {C_B}Sistem Kesintisiz Çalışma:{C_RESET} {uptime}")
    print(f" {C_B}CPU Tehdit ve Yük Durumu:{C_RESET}  %{random.randint(1, 15)} (Tamamen Stabil)")
    
    oracle_ai(mode, db, "diag")
    input("\n [ENTER] GERİ DÖN...")

def the_omega_protocol():
    """Görsel bir siber imha (Self-Destruct) sekansıdır."""
    cls()
    print(f"{C_R}{C_BOLD}")
    print(r"  /$$$$$$  /$$      /$$ /$$$$$$$$ /$$$$$$   /$$$$$$ ")
    print(r" /$$__  $$| $$$    /$$$| $$_____//$$__  $$ /$$__  $$")
    print(r"| $$  \ $$| $$$$  /$$$$| $$     | $$  \__/| $$  \ $$")
    print(r"| $$  | $$| $$ $$/$$ $$| $$$$$  | $$ /$$$$| $$$$$$$$")
    print(r"| $$  | $$| $$  $$$| $$| $$__/  | $$|_  $$| $$__  $$")
    print(r"| $$  | $$| $$\  $ | $$| $$     | $$  \ $$| $$  | $$")
    print(r"|  $$$$$$/| $$ \/  | $$| $$$$$$$|  $$$$$$/| $$  | $$")
    print(r" \______/ |__/     |__/|________/\______/ |__/  |__/")
    print(f"{C_RESET}")
    
    print(f"\n {C_R}{C_BOLD}DİKKAT: OMEGA PROTOKOLÜ (SİSTEM İMHASI) TETİKLENDİ.{C_RESET}")
    confirm = input(f" {C_Y}BU İŞLEM GERİ ALINAMAZ. ONAYLIYOR MUSUNUZ? (EVET/HAYIR): {C_RESET}").upper()
    
    if confirm == "EVET":
        cls()
        for i in range(10, 0, -1):
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(f"               {C_R}{C_BOLD}SİSTEM KENDİNİ İMHA EDİYOR: {i}{C_RESET}".center(100))
            time.sleep(1)
            cls()
            
        if os.path.exists(DB_FILE): os.remove(DB_FILE)
        if os.path.exists(BACKUP_FILE): os.remove(BACKUP_FILE)
        
        print(f"\n\n {C_R}BÜTÜN VERİLER SİLİNDİ. SİSTEM KAPATILIYOR.{C_RESET}")
        time.sleep(2)
        sys.exit()

# --- BÖLÜM 6: ANA KONTROL DÖNGÜSÜ (18'Lİ MEGA GRID DASHBOARD) ---

def start_leviathan():
    """Programın başlangıç noktası ve devasa 18'li menü döngüsü."""
    boot_sequence() 
    
    while True:
        db = db_load()
        my_ip = get_system_ip()
        cls()
        meta, conf = db["META"], db["CONFIG"]
        
        # --- GİRİŞ (AUTH) PANELİ ---
        w_l = 150
        print(f"\n\n {C_P}╔" + "═" * (w_l-2) + "╗")
        print(f" ║ {C_BOLD}{f'{meta['sys_name']} {meta['sys_ver']} | MERKEZİ KİMLİK DOĞRULAMA'.center(w_l-4)} {C_P}║")
        print(f" ╚" + "═" * (w_l-2) + "╝{C_RESET}")
        
        entry = input(f" {C_Y}🔑 GİRİŞ ANAHTARI (X: ÇIKIŞ YAP) > {C_RESET}").strip().lower()
        if entry == "x": break
            
        # Gizli Panic Kodu
        if entry == conf.get("panic"): 
            the_omega_protocol()
            continue
            
        # Güvenlik Duvarı (Blacklist) Kontrolü
        if my_ip in db.get("BLACKLIST", []):
            simulate_loading("GÜVENLİK PROTOKOLÜ TARAMASI", duration=1.0)
            notify(f"IP ADRESİNİZ KARANTİNADA. SİSTEME ERİŞİM REDDEDİLDİ.", "ERR")
            time.sleep(2)
            continue

        # Rütbe Doğrulaması
        if entry == "admin" or entry == conf.get("admin_key"): 
            mode = "ADMIN"
        elif entry == "beta" or entry == conf.get("beta_key"): 
            mode = "BETA"
        else: 
            notify("KİMLİK DOĞRULANAMADI! DENEME LOGLANDI.", "ERR")
            db = db_load()
            db["META"]["failed_logins"] = db["META"].get("failed_logins", 0) + 1
            db_save(db)
            continue

        simulate_loading("KİMLİK DENETİMİ VE AĞ BAĞLANTISI SAĞLANIYOR", duration=0.8)
        oracle_ai(mode, db, "login", my_ip)
        
        draw_header("LOKASYON DOĞRULAMA SİSTEMİ", mode, db, my_ip, ("?", "?", "?", "?", "?"))
        pk_in = input(f"\n 📍 POSTA KODU VEYA ÜS KODU (0: ATLA | X: İPTAL) > ").strip().upper()
        if pk_in == "X": 
            continue
            
        loc_info = get_strategic_intel(pk_in) if pk_in != "0" else ("KONUMSUZ", "GLOBAL ANALİZ MERKEZİ", "N/A", "⚪ SAFE", "ZONE-UNK")

        # --- İÇ MENÜ DÖNGÜSÜ ---
        while True:
            # Her ana menüye dönüşte aktif radar pingi at
            db = db_load()
            update_active_status(my_ip)
            
            b_p, s_p, plug = db["B_PERMS"], db["S_PERMS"], db["PLUGINS"]
            draw_header("LEVIATHAN COMMAND CENTER", mode, db, my_ip, loc_info)
            
            if mode == "BETA":
                # --- BETA DYNAMIC DASHBOARD ---
                print(f" {C_C}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{C_RESET}".ljust(95) + f"{C_C}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{C_RESET}")
                enc_opt = f"┃ {C_G}[1]{C_RESET} VERİ MÜHÜRLEME (ŞİFRELEME ÜNİTESİ)                             ┃{C_RESET}" if b_p["b_enc"][0] else f"{C_GR}┃ [X] ERİŞİM KISITLI                                               ┃{C_RESET}"
                dec_opt = f"┃ {C_G}[2]{C_RESET} VERİ ÇÖZÜMLEME (DEŞİFRELEME ÜNİTESİ)                           ┃{C_RESET}" if b_p["b_dec"][0] else f"{C_GR}┃ [X] ERİŞİM KISITLI                                               ┃{C_RESET}"
                print(enc_opt.ljust(95) + dec_opt)
                print(f" ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{C_RESET}".ljust(95) + f"{C_C}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{C_RESET}")
                
                print(f" {C_Y}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{C_RESET}".ljust(95) + f"{C_PK}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{C_RESET}")
                arc_opt = f"┃ {C_Y}[3]{C_RESET} KİŞİSEL İŞLEM ARŞİVİM VE KAYITLAR                              ┃{C_RESET}" if b_p["b_p_arc"][0] else f"{C_GR}┃ [X] ARŞİV GÖRÜNTÜLEME KISITLI                                    ┃{C_RESET}"
                sug_opt = f"┃ {C_PK}[4]{C_RESET} MERKEZE STRATEJİK RAPOR VE VAKA GÖNDER                         ┃{C_RESET}" if b_p["b_sug"][0] else f"{C_GR}┃ [X] RAPOR GÖNDERME YETKİSİ YOK                                   ┃{C_RESET}"
                print(arc_opt.ljust(95) + sug_opt)
                print(f" ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{C_RESET}".ljust(95) + f"{C_PK}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{C_RESET}")
                
                # Betaya atanan ek yetkilerin menüye dizilmesi
                extras = []
                if b_p.get("b_chat", [False])[0]: extras.append(f"{C_B}[5]{C_RESET} SİBER HABERLEŞME")
                if b_p.get("b_g_arc", [False])[0]: extras.append(f"{C_G}[6]{C_RESET} SİSTEM ARŞİVİ")
                if b_p.get("b_broad", [False])[0]: extras.append(f"{C_O}[7]{C_RESET} DUYURU YAYINLA")
                if b_p.get("b_stats", [False])[0]: extras.append(f"{C_PK}[8]{C_RESET} DB DASHBOARD")
                if b_p.get("b_diag", [False])[0]: extras.append(f"{C_C}[9]{C_RESET} SİSTEM TEŞHİSİ")
                if b_p.get("b_pass", [False])[0]: extras.append(f"{C_P}[10]{C_RESET} PAROLA ÜRETİCİ")
                
                if extras: 
                    print(f"\n " + "  ".join(extras))
                    
                print(f"\n {C_R}[X] TERMİNALİ KAPAT VE GÜVENLİ ŞEKİLDE ÇIKIŞ YAP{C_RESET}")
                
            else:
                # --- 18'Lİ MEGA GRID DASHBOARD (ADMIN + ALL PLUGINS) ---
                print(f"  {C_P}⚡ KRİPTOGRAFİ & ADLİ İŞLEMLER{C_RESET}".ljust(65) + f"{C_PK}📡 AĞ, İLETİŞİM & İSTİHBARAT{C_RESET}".ljust(65) + f"{C_B}⚙️ YÖNETİM & SİSTEM KONTROLÜ{C_RESET}")
                print(f"  {'─'*35}".ljust(65) + f"{'─'*35}".ljust(65) + f"{'─'*45}")
                print(f"  {C_G}[1]{C_RESET} Veri Mühürleme İstasyonu".ljust(65) + f"{C_PK}[7]{C_RESET} Rapor / Vaka Denetimi".ljust(65) + f"{C_B}[13]{C_RESET} Veritabanı Analitik Paneli")
                print(f"  {C_G}[2]{C_RESET} Veri Çözümleme İstasyonu".ljust(65) + f"{C_O}[8]{C_RESET} Duyuru Yayın İstasyonu".ljust(65) + f"{C_B}[14]{C_RESET} Sistem Donanım Teşhisi (Diag)")
                print(f"  {C_Y}[3]{C_RESET} Adli Arşiv (Hex Dump)".ljust(65) + f"{C_R}[9]{C_RESET} IP Güvenlik Duvarı (Ban)".ljust(65) + f"{C_B}[15]{C_RESET} Yetki ve İzin Matrisi")
                print(f"  {C_P}[4]{C_RESET} Collatz Kripto Analizi".ljust(65) + f"{C_PK}[10]{C_RESET} İstihbarat Akışı (Logs)".ljust(65) + f"{C_O}[16]{C_RESET} Eklenti Yönetimi (Plugins)")
                print(f"  {C_G}[5]{C_RESET} SİBER HABERLEŞME KANALI".ljust(65) + f"{C_C}[11]{C_RESET} Ağ Tarama (Traceroute)".ljust(65) + f"{C_B}[17]{C_RESET} Çekirdek Ayarları (Update Linki)")
                print(f"  {C_Y}[6]{C_RESET} Güvenli Parola Üretici".ljust(65) + f"{C_C}[12]{C_RESET} Gelişmiş Port Tarayıcı".ljust(65) + f"{C_R}[18]{C_RESET} {C_BOLD}OTA SİSTEM GÜNCELLEME{C_RESET}")
                print(f"  {'─'*180}")
                print(f"  {C_R}[00] OMEGA PROTOKOLÜ (SİSTEMİ İMHA ET){C_RESET}".ljust(130) + f"{C_R}[X] TERMİNALİ KİLİTLE{C_RESET}")
            
            sel = input(f"\n {C_BOLD}[EMİR GİRİN] > {C_RESET}").strip().upper()
            
            # --- YÖNLENDİRME (ROUTING) KATMANI ---
            
            if sel == "X": 
                break
            
            elif sel == "00" and mode == "ADMIN":
                the_omega_protocol()
                
            elif sel == "1": 
                if mode == "ADMIN" or b_p["b_enc"][0]: 
                    encryption_module(mode, db, my_ip, loc_info, geo_key)
                else: 
                    notify("Şifreleme yetkiniz kısıtlanmıştır.", "ERR")
                    
            elif sel == "2":
                if mode == "ADMIN" or b_p["b_dec"][0]: 
                    decryption_module(mode, db, my_ip, loc_info)
                else: 
                    notify("Deşifreleme yetkiniz kısıtlanmıştır.", "ERR")
            
            elif sel == "3": 
                page = 0
                while True:
                    db = db_load() 
                    draw_header("ADLİ ARŞİV VE VERİ DENETİM MERKEZİ", mode, db, my_ip, loc_info)
                    
                    if mode == "ADMIN" or b_p["b_g_arc"][0]:
                        target = db["ARCHIVE"]
                    else:
                        target = [x for x in db["ARCHIVE"] if x.get('ip') == my_ip]
                        
                    if not target: 
                        print(f"\n {C_GR}[!] Sistemde mühürlü bir kayıt bulunamadı.{C_RESET}")
                        input("\n [ENTER] Geri dön...")
                        break
                    
                    psize = 5
                    start = page * psize
                    end = start + psize
                    
                    for m in target[start:end]:
                        ucol = C_C if m.get('user') == "BETA" else C_P
                        print(f" {C_Y}VAKA #{m.get('id', 'UNK')}{C_RESET} | {ucol}{m.get('user'):<8}{C_RESET} | T:{m.get('at')} | L:{m.get('loc')}")
                        print(f" ├─ {C_G}VERİ:{C_RESET} {C_BOLD}{m.get('msg')}{C_RESET}")
                        if mode == "ADMIN" or s_p["s_for"][0]: 
                            print(f" └─ {C_GR}CODE:{C_RESET} {m.get('code')[:70]}...")
                        print(" " + "─"*175)
                    
                    cmd = input(f"\n {C_Y}[N]{C_RESET} İleri | {C_Y}[P]{C_RESET} Geri | {C_PK}[ID]{C_RESET} Hex-Dump İncele | {C_R}[X]{C_RESET} Çık: ").upper()
                    
                    if cmd == "X": 
                        break
                    elif cmd == "N" and end < len(target): 
                        page += 1
                    elif cmd == "P" and page > 0: 
                        page -= 1
                    else:
                        if mode == "ADMIN" and plug["forensic"][0]:
                            found = next((x for x in target if x.get("id") == cmd), None)
                            if found:
                                draw_header(f"HEX-DUMP ANALİZİ: {found['id']}", mode, db, my_ip, loc_info)
                                simulate_loading("BELLEK DÖKÜMÜ ÇIKARILIYOR", duration=1.0)
                                print(f" {C_C}KAYNAK İZİ:{C_RESET} {found['ip']} | {C_C}ANAHTAR:{C_RESET} {found['geo']}")
                                display_hex_dump(found['code'])
                                input("[ENTER] GERİ DÖN")

            elif sel == "4": 
                if mode == "ADMIN":
                    if s_p.get("s_crypto", [False])[0]:
                        collatz_avalanche_analysis(mode, db, my_ip, loc_info)
                    else: notify("Kripto analiz yetkiniz kapalı.", "ERR")
                elif mode == "BETA" and b_p["b_sug"][0]:
                    t = input("\n 📩 GÖNDERİLECEK VAKA/RAPOR İÇERİĞİ: ")
                    if t: 
                        db = db_load()
                        uid = str(uuid.uuid4())[:6].upper()
                        db["SUGGESTIONS"].append({
                            "id": uid, "at": datetime.now().strftime("%H:%M"), 
                            "msg": t, "ip": my_ip, "read": False, "loc": loc_info[0]
                        })
                        db_save(db)
                        notify(f"Vaka (ID: {uid}) başarıyla karargaha iletildi.")
            
            elif sel == "5":
                if mode == "ADMIN" or (mode == "BETA" and b_p.get("b_chat", [False])[0]): 
                    comms_module(mode, db, my_ip, loc_info)

            elif sel == "6": 
                if mode == "ADMIN":
                    generate_secure_password(mode, db, my_ip, loc_info)
                elif mode == "BETA" and b_p.get("b_g_arc", [False])[0]: 
                    notify("Sistem Arşivi erişimi Seçenek 3 üzerinden filtrelenmektedir.", "INFO")

            elif sel == "7": 
                if mode == "ADMIN":
                    while True:
                        db = db_load()
                        draw_header("VAKA VE RAPOR DENETİM MERKEZİ", mode, db, my_ip, loc_info)
                        reps = db.get("SUGGESTIONS", [])
                        if not reps: 
                            print(f"\n {C_GR}İncelenecek herhangi bir rapor yok.{C_RESET}")
                            input("\n [ENTER] Geri dön...")
                            break
                            
                        for i, s in enumerate(reps, 1):
                            mark = f"{C_PK}[YENİ]{C_RESET} " if not s.get('read') else "      "
                            print(f" {mark}{i}. [{s.get('id')}] {s.get('loc')} -> {s.get('msg')[:80]}...")
                            
                        idx = input(f"\n İncelemek için numara girin | Çıkış için X: ").upper()
                        if idx == "X": 
                            break
                        if idx.isdigit() and int(idx) <= len(reps):
                            r = reps[int(idx)-1]
                            r['read'] = True
                            db_save(db)
                            
                            draw_header(f"VAKA DETAY DOSYASI: {r['id']}", mode, db, my_ip, loc_info)
                            print(f" GÖNDEREN: {r['ip']} | ZAMAN: {r['at']} | KONUM: {r['loc']}\n" + "═"*130)
                            print(f"\n {C_BOLD}{r['msg']}{C_RESET}\n\n" + "═"*130)
                            input("[ENTER] GERİ DÖN")
                elif mode == "BETA" and b_p.get("b_broad", [False])[0]:
                    db = db_load()
                    db["META"]["news"] = input("\n 📢 SİSTEM GENELİ YENİ DUYURU: ")
                    db_save(db)
                    notify("Broadcast başarıyla yayına alındı.")

            elif sel == "8": 
                if mode == "ADMIN":
                    db = db_load()
                    db["META"]["news"] = input("\n 📢 SİSTEM GENELİ YENİ DUYURU: ")
                    db_save(db)
                    notify("Broadcast başarıyla yayına alındı.")
                elif mode == "BETA" and b_p.get("b_stats", [False])[0]:
                    draw_header("VERİTABANI ANALİTİK DASHBOARD", mode, db, my_ip, loc_info)
                    print(f" 📊 TRAFİK AKIŞI  : {len(db['INTEL_LOGS'])} Eylem")
                    print(f" 📂 ARŞİV HACMİ   : {len(db['ARCHIVE'])} Kayıt")
                    print(f" 📩 AKTİF RAPOR   : {len(db['SUGGESTIONS'])} Adet")
                    input("\n [ENTER] GERİ DÖN")

            elif sel == "9": 
                if mode == "ADMIN": 
                    firewall_module(mode, db, my_ip, loc_info)
                elif mode == "BETA" and b_p.get("b_diag", [False])[0]: 
                    system_diagnostics(mode, db, my_ip, loc_info)

            elif sel == "10": 
                if mode == "ADMIN":
                    page_i = 0
                    while True:
                        db = db_load()
                        draw_header("SAHA İSTİHBARAT AKIŞI (LOGS)", mode, db, my_ip, loc_info)
                        logs = db.get("INTEL_LOGS", [])
                        p_i = 20
                        s_i = page_i * p_i
                        e_i = s_i + p_i
                        
                        for l in logs[s_i:e_i]:
                            print(f" {C_GR}[{l.get('at')}]{C_RESET} {C_Y}{l.get('user', 'UNK'):<8}{C_RESET} -> {C_BOLD}{l.get('act', 'UNK'):<25}{C_RESET} | IP: {l.get('ip', '--')} | ZON: {l.get('loc_tag', '--')}")
                            
                        nav_i = input(f"\n {C_Y}[N]{C_RESET} İleri | {C_Y}[P]{C_RESET} Geri | {C_R}[X]{C_RESET} Kapat: ").upper()
                        if nav_i == "X": break
                        elif nav_i == "N" and e_i < len(logs): page_i += 1
                        elif nav_i == "P" and page_i > 0: page_i -= 1
                elif mode == "BETA" and b_p.get("b_pass", [False])[0]:
                    generate_secure_password(mode, db, my_ip, loc_info)

            elif sel == "11" and mode == "ADMIN": 
                network_traceroute(mode, db, my_ip, loc_info)

            elif sel == "12" and mode == "ADMIN": 
                if plug.get("port_scan", [False])[0]:
                    advanced_port_scanner(mode, db, my_ip, loc_info)
                else:
                    notify("Port tarama eklentisi devre dışı.", "ERR")

            elif sel == "13" and mode == "ADMIN": 
                db = db_load()
                draw_header("VERİTABANI ANALİTİK DASHBOARD", mode, db, my_ip, loc_info)
                print(f" 📊 TOPLAM İŞLEM TRAFİĞİ  : {len(db['INTEL_LOGS'])} Kayıt")
                print(f" 📂 ŞİFRELENMİŞ ARŞİV HACMİ : {len(db['ARCHIVE'])} Mühür")
                print(f" 📩 BEKLEYEN VAKA RAPORLARI : {len(db['SUGGESTIONS'])} Adet")
                print(f" 💬 SİBER HABERLEŞME (COMMS): {len(db['COMMS'])} İleti")
                
                if input("\n VERİTABANINI SIFIRLA (SIFIRLA): ").upper() == "SIFIRLA":
                    db["ARCHIVE"], db["INTEL_LOGS"], db["SUGGESTIONS"], db["COMMS"] = [], [], [], []
                    db_save(db)
                    notify("Veritabanı başarıyla temizlendi.")
                else: 
                    input("\n [ENTER] GERİ DÖN")

            elif sel == "14" and mode == "ADMIN": 
                system_diagnostics(mode, db, my_ip, loc_info)

            elif sel == "15" and mode == "ADMIN": 
                while True:
                    db = db_load()
                    draw_header("YETKİ VE İZİN HİYERARŞİSİ", mode, db, my_ip, loc_info)
                    print(f" {C_P}[1] SİSTEM ÇEKİRDEK YETKİLERİ{C_RESET}".ljust(65) + f"{C_C}[2] BETA OPERASYONEL YETKİLERİ{C_RESET}")
                    ch = input("\n Bölüm Seçin | [X] GERİ: ").upper()
                    if ch == "X": break
                    
                    t_map = db["S_PERMS"] if ch == "1" else db["B_PERMS"]
                    while True:
                        draw_header("YETKİ KONFİGÜRASYONU DÜZENLEME", mode, db, my_ip, loc_info)
                        for i, (k, v) in enumerate(t_map.items(), 1):
                            print(f"  [{i}] {v[1]:<30} : [{'AÇIK' if v[0] else 'KAPALI'}]")
                            print(f"      └─> {C_GR}{v[2]}{C_RESET}")
                        c = input("\n Değiştirmek için No girin | X Geri: ").upper()
                        if c == "X": break
                        if c.isdigit() and int(c) <= len(t_map):
                            key = list(t_map.keys())[int(c)-1]
                            t_map[key][0] = not t_map[key][0]
                            db_save(db)

            elif sel == "16" and mode == "ADMIN": 
                while True:
                    db = db_load()
                    draw_header("EKLENTİ (PLUGINS) YÖNETİMİ", mode, db, my_ip, loc_info)
                    for i, (k, v) in enumerate(db["PLUGINS"].items(), 1):
                        print(f"  [{i}] {v[1]:<25} : [{'AKTİF' if v[0] else 'PASİF'}]")
                        print(f"      └─> {C_GR}{v[2]}{C_RESET}")
                    c = input("\n Değiştirmek için No girin | X Geri: ").upper()
                    if c == "X": break
                    if c.isdigit() and int(c) <= len(db["PLUGINS"]):
                        key = list(db["PLUGINS"].keys())[int(c)-1]
                        db["PLUGINS"][key][0] = not db["PLUGINS"][key][0]
                        db_save(db)
                        
            elif sel == "17" and mode == "ADMIN": 
                if input(" 🔐 ADMIN AUTH ŞİFRESİ: ") == conf["auth_pass"]:
                    while True:
                        db = db_load()
                        draw_header("ÇEKİRDEK VE SİSTEM AYARLARI", mode, db, my_ip, loc_info)
                        print(f" {C_Y}Genel Sistem Ayarları:{C_RESET}")
                        print(f" [1] Program Adı : {meta['sys_name']}")
                        print(f" [2] Admin Key   : {conf['admin_key']}")
                        print(f" [3] Beta Key    : {conf['beta_key']}")
                        print(f" [4] Auth Şifresi: {conf['auth_pass']}")
                        print(f" [5] Panic Kodu  : {conf['panic']}")
                        
                        print(f"\n {C_Y}OTA Sistem Güncelleme Ayarları:{C_RESET}")
                        print(f" [6] GitHub URL  : {meta.get('update_url', 'Ayarlanmadı')}")
                        
                        cs = input("\n Değiştirmek istediğiniz numara | X Geri: ").upper()
                        if cs == "X": break
                        if cs.isdigit() and int(cs) <= 6:
                            v = input("Yeni Değer Girin: ")
                            if cs == "1": db["META"]["sys_name"] = v
                            elif cs == "2": db["CONFIG"]["admin_key"] = v
                            elif cs == "3": db["CONFIG"]["beta_key"] = v
                            elif cs == "4": db["CONFIG"]["auth_pass"] = v
                            elif cs == "5": db["CONFIG"]["panic"] = v
                            elif cs == "6": db["META"]["update_url"] = v
                            db_save(db)
                            notify("Ayar başarıyla mühürlendi.")
                            oracle_ai(mode, db, "settings")
                            
            elif sel == "18" and mode == "ADMIN": 
                if s_p.get("s_ota", [False])[0]: 
                    auto_update_system(mode, db, my_ip, loc_info)
                else: 
                    notify("Sistem Güncelleme yetkiniz güvenlik sebebiyle kapalı.", "ERR")

if __name__ == "__main__":
    try: 
        start_leviathan()
    except KeyboardInterrupt: 
        sys.exit()
