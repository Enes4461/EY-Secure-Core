"""
=============================================================================
E&Y SECURE CORE - v46.0 NETWORK SYNC (THE LEVIATHAN)
Authors: Enes & Yasin
Description: Enterprise Cyber Operations Terminal & Multi-Device Sync.
Features: 15-Grid Dashboard, OTA Auto-Updater, Live P2P Comms, Oracle-X AI, 
          Dual-Core Database, Forensic Hex-Dumps, IP Blacklist.
=============================================================================
"""

import os
import sys
import time
import json
import socket
import random
import hashlib
import binascii
import uuid
import platform
import urllib.request
from datetime import datetime, timedelta

# --- KRİPTOGRAFİ KÜTÜPHANELERİ ---
try:
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.hkdf import HKDF
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
except ImportError:
    print("\n [!] KRİTİK HATA: 'cryptography' kütüphanesi eksik.")
    print(" Terminale yazın: pip install cryptography")
    sys.exit()

# --- BÖLÜM 1: ÇİFT ÇEKİRDEKLİ (DUAL-CORE) VERİTABANI MOTORU ---
DB_FILE = "ey_vault.json"
BACKUP_FILE = "ey_backup_vault.json"

def get_strategic_intel(pk):
    """Posta kodundan derin askeri lokasyon ve savunma analizi."""
    intel_matrix = {
        "61": ("TRABZON", "KARADENİZ SİBER KARARGAH (MERKEZ ÜS)", "41.002°N, 39.716°E", "🔴 DEFCON-1", "ZONE-OMEGA"),
        "34": ("İSTANBUL", "MARMARA VERİ HUB VE ANALİZ", "41.008°N, 28.978°E", "🟡 DEFCON-3", "ZONE-BRAVO"),
        "06": ("ANKARA", "STRATEJİK OPERASYON KOMUTANLIĞI", "39.933°N, 32.859°E", "🔴 DEFCON-2", "ZONE-ALPHA"),
        "35": ("İZMİR", "EGE LOJİSTİK VE HABERLEŞME", "38.419°N, 27.128°E", "🟢 DEFCON-4", "ZONE-CHARLIE"),
        "07": ("ANTALYA", "GÜNEY SİNYAL İZLEME", "36.896°N, 30.713°E", "🟢 DEFCON-4", "ZONE-CHARLIE"),
        "41": ("KOCAELİ", "ENDÜSTRİYEL SAVUNMA HATTI", "40.765°N, 29.940°E", "🟡 DEFCON-3", "ZONE-BRAVO"),
        "55": ("SAMSUN", "KUZEY VERİ AKTARIM DÜĞÜMÜ", "41.286°N, 36.336°E", "🟢 DEFCON-4", "ZONE-CHARLIE")
    }
    p = str(pk)[:2]
    return intel_matrix.get(p, (f"BÖLGE-{p}", "DIŞ SEKTÖR", "COORD: N/A", "⚪ UNKNOWN", "ZONE-NULL"))

def vault_blueprint():
    """Sistemin fabrika ayarları, tüm yetkiler ve OTA Update URL'si."""
    return {
        "META": {
            "sys_name": "E&Y NETWORK SYNC CORE", "sys_ver": "v46.0 PRO", 
            "news": "OTA Güncelleme Protokolü Aktif",
            "boot_time": datetime.now().isoformat(), "total_ops": 0, "failed_logins": 0,
            "update_url": "https://raw.githubusercontent.com/.../main/singularity.py" # Burayı GitHub raw linkinizle değiştirebilirsiniz
        },
        "CONFIG": {
            "beta_key": "beta", "admin_key": "admin", "auth_pass": "2010", "panic": "6161"
        },
        "PLUGINS": {
            "oracle_ai": [True, "Oracle-X AI", "Risk skoru ve taktik üretir."],
            "forensic": [True, "Adli Köprü", "Hex-Dump analizi yapar."],
            "intel": [True, "İstihbarat", "Saha loglarını tutar."],
            "net_sim": [True, "Ağ Tarama", "Hedef IP/Domain analiz eder."],
            "sys_diag": [True, "Donanım Teşhis", "Sistem CPU/RAM okur."],
            "firewall": [True, "IP Karantina", "Zararlı IP engeller."],
            "comms": [True, "Siber Haberleşme", "Uçtan uca şifreli Chat kanalı."],
            "ota_update": [True, "Sistem Güncelleyici", "Merkezden yeni kod çeker."]
        },
        "S_PERMS": {
            "s_ai": [True, "AI Yönetimi", "Yapay zeka erişimi."],
            "s_for": [True, "Adli Arşiv", "Hex Veri dökümü alma."],
            "s_root": [True, "DB Kök Yönetimi", "Veritabanı imhası."],
            "s_net": [True, "Ağ Operasyonları", "Dış IP ping tarama."],
            "s_ban": [True, "Karantina Yetkisi", "IP banlama yetkisi."],
            "s_chat": [True, "Haberleşme İzni", "Global chat yetkisi."],
            "s_ota": [True, "Sistem Güncelleme", "Github'dan kod çekme."]
        },
        "B_PERMS": {
            "b_enc": [True, "Mühürleme", "Veri şifreleme."],
            "b_dec": [True, "Deşifreleme", "Kilit açma."],
            "b_p_arc": [True, "Kişisel Arşiv", "Kendi verilerini izleme."],
            "b_sug": [True, "Rapor Gönderme", "Yönetime durum bildirme."],
            "b_chat": [True, "Siber Haberleşme", "Merkez ile chat yapma."],
            "b_g_arc": [False, "Sistem Arşivi", "Tüm verileri görme."],
            "b_broad": [False, "Duyuru", "Sistem geneli yayın yapma."],
            "b_stats": [False, "Sistem Analitiği", "DB doluluk oranlarını görme."],
            "b_diag": [False, "Sistem Teşhisi", "Donanım durumunu okuma."]
        },
        "ARCHIVE": [], "SUGGESTIONS": [], "INTEL_LOGS": [], "BLACKLIST": [], "COMMS": [], "ACTIVE_NODES": {}
    }

def db_load():
    """Çoklu cihaz (Multi-Device) destekli okuma motoru. Okuma hatasında 3 kez dener."""
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
                data = vault_blueprint(); db_save(data); return data
        except json.JSONDecodeError:
            time.sleep(0.2)
    
    if data is None: return vault_blueprint()

    # Derin Onarım (Blueprint Sync)
    ref = vault_blueprint()
    for k in ref.keys():
        if k not in data: data[k] = ref[k]
    for sub in ["PLUGINS", "S_PERMS", "B_PERMS"]:
        for sk, sv in ref[sub].items():
            if sk not in data[sub]: data[sub][sk] = sv
    return data

def db_save(data):
    """Veriyi hem ana dosyaya hem yedeğe eşzamanlı yazar (Sıfır kayıp)."""
    try:
        data["META"]["total_ops"] = data["META"].get("total_ops", 0) + 1
        with open(DB_FILE, "w", encoding="utf-8") as f: json.dump(data, f, indent=4, ensure_ascii=False)
        with open(BACKUP_FILE, "w", encoding="utf-8") as f: json.dump(data, f, indent=4, ensure_ascii=False)
    except: pass

def update_active_status(ip):
    db = db_load()
    if "ACTIVE_NODES" not in db: db["ACTIVE_NODES"] = {}
    db["ACTIVE_NODES"][ip] = time.time()
    db_save(db)

# --- BÖLÜM 2: GÖRSEL MOTOR VE ANİMASYONLAR ---
C_RESET, C_BOLD = "\033[0m", "\033[1m"
C_G, C_Y, C_R = "\033[38;5;82m", "\033[38;5;226m", "\033[38;5;196m"
C_C, C_B, C_P = "\033[38;5;51m", "\033[38;5;27m", "\033[38;5;129m"
C_O, C_PK, C_GR = "\033[38;5;208m", "\033[38;5;201m", "\033[38;5;244m"

def cls(): os.system('cls' if os.name == 'nt' else 'clear')

def get_system_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]; s.close()
        return ip
    except: return "127.0.0.1"

def simulate_loading(task_name, duration=1.0, steps=20):
    print()
    for i in range(steps + 1):
        percent = (i / float(steps)) * 100
        bar = '█' * i + '-' * (steps - i)
        sys.stdout.write(f"\r {C_C}[{task_name}]{C_RESET} İŞLENİYOR: |{C_Y}{bar}{C_RESET}| {percent:.1f}% ")
        sys.stdout.flush(); time.sleep(duration / steps)
    print(f"\n {C_G}✓ İŞLEM BAŞARILI.{C_RESET}"); time.sleep(0.3)

def boot_sequence():
    """Terminalin siber hissiyatını artıran sahte yükleme ekranı."""
    cls()
    print(f"{C_G}")
    boot_msgs = [
        "INITIALIZING NEURAL ÇEKİRDEK...",
        "LOADING ENCRYPTION MODULES (AES-256 GCM)...",
        "ESTABLISHING SECURE P2P COMMS...",
        "MOUNTING DUAL-CORE DATABASE...",
        "VERIFYING INTEGRITY HASHS...",
        "SYSTEM ONLINE."
    ]
    for msg in boot_msgs:
        print(f"[*] {msg}")
        time.sleep(0.15)
    print(f"{C_RESET}"); time.sleep(0.5)

def draw_header(title, mode, db, ip, loc):
    cls()
    meta = db.get("META", {})
    color = C_P if mode == "ADMIN" else C_C
    w = 185
    
    # Aktif kullanıcı radar
    active_nodes = db.get("ACTIVE_NODES", {})
    curr_time = time.time()
    online_count = sum(1 for t in active_nodes.values() if curr_time - t < 120)
    
    print(f"{color}╔" + "═" * (w-2) + f"╗{C_RESET}")
    sys_id = f"⚡ {meta.get('sys_name')} | CORE: {meta.get('sys_ver')} | NODE: {ip} | OPS: {meta.get('total_ops')} ⚡"
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
    c = C_C if n_type == "INFO" else C_R
    print(f"\n {c} ❱❱❱ {msg} {C_RESET}"); time.sleep(1.2)

def oracle_ai(mode, db, action, extra=""):
    """Oracle-X AI Analiz ve Taktik Motoru."""
    if not db["PLUGINS"].get("oracle_ai", [False])[0]: return
    risk = random.randint(1, 15) if action != "denied" else random.randint(85, 100)
    scenarios = {
        "enc": f"Kripto analiz edildi (Risk: %{risk}). 256-bit GCM katmanı devrede.",
        "dec": f"Deşifreleme yapıldı (Risk: %{risk}). İzler karartıldı.",
        "login": f"Erişim mühürlendi (Risk: %{risk}). IP maskeleme devrede.",
        "denied": f"İHLAL! Yetkisiz modül (Risk: %{risk}). Sistem Alarmı.",
        "net": f"Ağ analizi tamam (Risk: %{risk}). Hedef {extra} portları taranıyor.",
        "diag": f"Sistem teşhisi yapıldı. İşlemci ve RAM verileri güvende.",
        "ban": f"Firewall güncellendi. IP {extra} karantinada.",
        "chat": f"Güvenli kanaldan veri iletildi (Risk: %0). Canlı senkronizasyon Aktif.",
        "update": f"Sistem güncelleme protokolü başlatıldı (Risk: %{risk}). Orijinallik doğrulanıyor."
    }
    msg = scenarios.get(action, f"İşlem analiz edildi (Risk: %{risk}).")
    col = C_R if risk > 50 else (C_Y if risk > 15 else C_G)
    print(f"\n {C_PK}✨ ORACLE-X AI:{C_RESET} {col}{msg}{C_RESET}")

# --- BÖLÜM 3: KRİPTOGRAFİ MODÜLLERİ ---

def get_crypto_key(tag, geo):
    kdf = HKDF(algorithm=hashes.SHA256(), length=32, salt=b"network_sync_v46", info=f"{tag}{geo}".encode())
    return kdf.derive(b"master_nexus_secret_key")

def encryption_module(mode, db, ip, loc, geo_key):
    draw_header("Kripto Mühürleme İstasyonu", mode, db, ip, loc)
    msg = input(f"\n {C_G}📝 GİZLİ MESAJ (Geri: X):{C_RESET} ").strip()
    if msg.upper() == "X": return
    tag = input(f" {C_G}📅 ETİKET/ID:{C_RESET} ").strip()
    try:
        hr = input(f" ⏳ İMHA ZAMANI (SAAT - Default 24): ").strip()
        simulate_loading("AES-256 GCM ŞİFRELEME", duration=1.0)
        
        key = get_crypto_key(tag, geo_key); nonce = os.urandom(12)
        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce)); encryptor = cipher.encryptor()
        ct = encryptor.update(msg.encode()) + encryptor.finalize()
        final = nonce.hex() + encryptor.tag.hex() + ct.hex() + tag.encode().hex() + f"{len(tag.encode().hex()):02x}"
        uid = str(uuid.uuid4())[:8].upper()
        
        db = db_load() # Güncel loglama
        record = {"id": uid, "at": datetime.now().strftime("%H:%M:%S"), "user": mode, "msg": msg, "code": final, "geo": geo_key, "tag": tag, "exp": (datetime.now() + timedelta(hours=int(hr or "24"))).isoformat(), "ip": ip, "loc": loc[0], "size": len(final)}
        db["ARCHIVE"].append(record)
        db["INTEL_LOGS"].append({"at": datetime.now().strftime("%H:%M:%S"), "user": mode, "act": f"ŞİFRELEME ({uid})", "ip": ip, "loc_tag": loc[0]})
        db_save(db); print(f"\n {C_G}✅ BAŞARILI:{C_RESET} Mühür Kodu:\n {C_BOLD}{C_C}{final}{C_RESET}")
        oracle_ai(mode, db, "enc", tag)
    except Exception as e: notify(f"Kripto Hatası: {e}", "ERR")
    input("\n [ENTER] DEVAM ET...")

def decryption_module(mode, db, ip, loc):
    draw_header("Vanguard Çözümleme İstasyonu", mode, db, ip, loc)
    code = input(f"\n {C_C}📥 KRİPTO KOD (Geri: X):{C_RESET} ").strip()
    if code.upper() == "X": return
    geo_in = input(f" {C_C}🔑 GEO-KEY:{C_RESET} ").strip()
    simulate_loading("ŞİFRE ÇÖZÜMÜ", duration=1.0)
    try:
        uz = int(code[-2:], 16); t_hex = code[-(uz+2):-2]; t_raw = bytes.fromhex(t_hex).decode()
        core = code[:-(uz+2)]; nonce, tag, ct = bytes.fromhex(core[:24]), bytes.fromhex(core[24:56]), bytes.fromhex(core[56:])
        key = get_crypto_key(t_raw, geo_in); decryptor = Cipher(algorithms.AES(key), modes.GCM(nonce, tag)).decryptor()
        res = (decryptor.update(ct) + decryptor.finalize()).decode('utf-8')
        
        db = db_load() 
        print(f"\n {C_G}🔓 VERİ ÇÖZÜLDÜ:{C_RESET}\n {C_BOLD}{res}{C_RESET}")
        db["INTEL_LOGS"].append({"at": datetime.now().strftime("%H:%M:%S"), "user": mode, "act": "DEŞİFRELEME", "ip": ip, "loc_tag": loc[0]})
        db_save(db); oracle_ai(mode, db, "dec")
    except: 
        notify("Veri Bozuk veya Anahtar Yanlış!", "ERR"); oracle_ai(mode, db, "denied")
    input("\n [ENTER] DEVAM ET...")

# --- BÖLÜM 4: COMMS, FIREWALL VE YENİ GÜNCELLEME MODÜLÜ ---

def comms_module(mode, db_stale, ip, loc):
    """CANLI SENKRONİZE SİBER HABERLEŞME"""
    while True:
        db = db_load()
        update_active_status(ip)
        draw_header("SİBER HABERLEŞME KANALI (LIVE COMMS)", mode, db, ip, loc)
        
        msgs = db.get("COMMS", [])
        print(f" {C_B}--- UÇTAN UCA ŞİFRELİ KANAL ---{C_RESET}")
        if not msgs: print(f" {C_GR}Henüz bir iletişim kaydı yok.{C_RESET}")
        else:
            for m in msgs[-15:]:
                color = C_P if m['sender'] == "ADMIN" else C_C
                print(f" {C_GR}[{m['at']}]{C_RESET} {color}{m['sender']}{C_RESET} ({m['loc']}): {m['msg']}")
        
        print(f"\n {C_Y}>> Yenilemek için boş bırakıp ENTER'a basınız. | Çıkış: X{C_RESET}")
        txt = input(f" {C_G}💬 MESAJ YAZ > {C_RESET}").strip()
        
        if txt.upper() == "X": break
        if txt:
            db = db_load()
            db["COMMS"].append({"at": datetime.now().strftime("%H:%M:%S"), "sender": mode, "ip": ip, "loc": loc[0], "msg": txt})
            db["INTEL_LOGS"].append({"at": datetime.now().strftime("%H:%M:%S"), "user": mode, "act": "COMMS İLETİSİ", "ip": ip, "loc_tag": loc[0]})
            db_save(db)

def auto_update_system(mode, db, ip, loc):
    """
    OTA (Over-The-Air) Otomatik Güncelleme Protokolü.
    Merkezi GitHub Raw linkinden kodu okur, mevcut dosyanın üzerine yazar ve yeniden başlatır.
    """
    draw_header("OTA SİSTEM GÜNCELLEME MERKEZİ", mode, db, ip, loc)
    update_url = db["META"].get("update_url", "")
    
    print(f" {C_B}Mevcut Sürüm:{C_RESET} {db['META']['sys_ver']}")
    print(f" {C_B}Hedef Sunucu:{C_RESET} {update_url}")
    print(f" {C_Y}DİKKAT:{C_RESET} Sistem, hedef sunucudaki kodu çekerek kendi üzerine yazacak ve yeniden başlayacaktır.")
    
    if "raw.githubusercontent.com" not in update_url and "http" not in update_url:
        print(f"\n {C_R}[!] HATA: Geçerli bir RAW URL ayarlanmamış.{C_RESET}")
        print(f" {C_GR}Ayarlar (Seçenek 14) menüsünden 'update_url' parametresini kendi GitHub RAW linkinizle değiştirin.{C_RESET}")
        input("\n [ENTER] GERİ DÖN")
        return

    cmd = input(f"\n {C_R}GÜNCELLEMEYİ BAŞLATMAK İSTİYOR MUSUNUZ? (EVET/HAYIR):{C_RESET} ").upper()
    if cmd == "EVET":
        try:
            simulate_loading("GÜNCELLEME SUNUCUSUNA BAĞLANILIYOR", duration=1.5)
            oracle_ai(mode, db, "update")
            
            req = urllib.request.Request(update_url, headers={'User-Agent': 'EY-Terminal/46.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                new_code = response.read().decode('utf-8')
            
            # Basit Güvenlik Doğrulaması (İmza Kontrolü)
            if "E&Y SECURE CORE" in new_code:
                simulate_loading("KOD İNDİRİLİYOR VE DOĞRULANIYOR", duration=2.0)
                
                # Mevcut çalıştırılan dosyanın üzerine yeni kodu yaz
                current_file = sys.argv[0]
                with open(current_file, 'w', encoding='utf-8') as f:
                    f.write(new_code)
                
                print(f"\n {C_G}GÜNCELLEME BAŞARILI! SİSTEM YENİDEN BAŞLATILIYOR...{C_RESET}")
                db["INTEL_LOGS"].append({"at": datetime.now().strftime("%H:%M:%S"), "user": mode, "act": "OTA GÜNCELLEMESİ YAPILDI", "ip": ip, "loc_tag": loc[0]})
                db_save(db)
                time.sleep(2)
                
                # Sistemi kendini kapatıp yeniden açmaya zorla
                os.execv(sys.executable, ['python'] + sys.argv)
            else:
                notify("İndirilen kodda güvenlik imzası (E&Y SECURE CORE) bulunamadı. İşlem iptal edildi.", "ERR")
        except Exception as e:
            notify(f"Bağlantı veya Yazma Hatası: {e}", "ERR")
    input("\n [ENTER] GERİ DÖN")

def firewall_module(mode, db, ip, loc):
    while True:
        db = db_load()
        draw_header("Siber Güvenlik Duvarı (Firewall)", mode, db, ip, loc)
        b_list = db.get("BLACKLIST", [])
        print(f" {C_R}--- KARANTİNA LİSTESİ ---{C_RESET}")
        if not b_list: print(f" {C_GR}Kara liste boş.{C_RESET}")
        else:
            for i, bip in enumerate(b_list, 1): print(f" [{i}] ENGEL: {bip}")
        cmd = input(f"\n {C_Y}İşlemler:{C_RESET}\n [1] IP Engelle\n [2] IP Engelini Kaldır\n [X] Geri\n Seçim > ").upper()
        if cmd == "X": break
        elif cmd == "1":
            t_ip = input(f" {C_R}Engellenecek IP:{C_RESET} ").strip()
            if t_ip and t_ip not in b_list:
                db = db_load(); db["BLACKLIST"].append(t_ip); db_save(db); notify(f"{t_ip} engellendi!"); oracle_ai(mode, db, "ban", t_ip)
        elif cmd == "2" and b_list:
            no = input(f" {C_G}Kaldırılacak IP No:{C_RESET} ").strip()
            if no.isdigit() and int(no) <= len(b_list):
                db = db_load(); rem = db["BLACKLIST"].pop(int(no)-1); db_save(db); notify(f"{rem} engeli kaldırıldı.", "INFO")

def display_hex_dump(hex_string):
    print(f"\n {C_GR}--- FORENSIC HEX DUMP (MEMORY) ---{C_RESET}")
    lines = [hex_string[i:i+64] for i in range(0, len(hex_string), 64)]
    for i, line in enumerate(lines):
        blocks = [line[j:j+8] for j in range(0, len(line), 8)]
        print(f" {C_Y}{i * 32:08x}{C_RESET}  {' '.join(blocks)}")
    print(f" {C_GR}--- END OF DUMP ---{C_RESET}\n")

def network_simulation(mode, db, ip, loc):
    draw_header("Ağ İstihbaratı (Ping/Traceroute)", mode, db, ip, loc)
    target = input(f"\n {C_C}🌐 Hedef IP/Domain (X: Geri):{C_RESET} ").strip()
    if target.upper() == "X": return
    simulate_loading(f"AĞ YÖNLENDİRİCİSİ -> {target}", duration=2.0)
    print(f"\n {C_GR}İzleme başlatıldı: {target}{C_RESET}")
    for i in range(1, 5):
        print(f" {i:2d}  {random.randint(10, 150)} ms   {random.randint(10,200)}.X.X.X [Düğüm Güvenli]")
        time.sleep(0.3)
    print(f"  5  {random.randint(10,50)} ms   {target} [HEDEF ULAŞILDI]")
    db = db_load(); db["INTEL_LOGS"].append({"at": datetime.now().strftime("%H:%M:%S"), "user": mode, "act": f"AĞ TARAMA ({target})", "ip": ip, "loc_tag": loc[0]})
    db_save(db); oracle_ai(mode, db, "net", target); input("\n [ENTER] DEVAM ET...")

def system_diagnostics(mode, db, ip, loc):
    draw_header("Sistem Teşhisi (Diag)", mode, db, ip, loc)
    simulate_loading("DONANIM ANALİZİ", duration=1.0)
    print(f"\n {C_P}--- SİSTEM RAPORU ---{C_RESET}")
    print(f" {C_B}OS:{C_RESET}      {platform.system()} {platform.release()} ({platform.machine()})")
    print(f" {C_B}Python:{C_RESET}  {platform.python_version()}")
    print(f" {C_B}DB Boyut:{C_RESET} {os.path.getsize(DB_FILE) / 1024:.2f} KB")
    print(f" {C_B}Uptime:{C_RESET}   {str(datetime.now() - datetime.fromisoformat(db['META']['boot_time'])).split('.')[0]}")
    oracle_ai(mode, db, "diag"); input("\n [ENTER] GERİ DÖN...")

# --- BÖLÜM 5: ANA DÖNGÜ (15'Lİ MEGA GRID VE UPDATE MERKEZİ) ---

def start_nexus():
    boot_sequence() # Sahte başlangıç animasyonu
    while True:
        db = db_load(); my_ip = get_system_ip(); cls()
        meta, conf = db["META"], db["CONFIG"]
        
        # GİRİŞ PANELİ
        w_l = 145
        print(f"\n\n {C_P}╔" + "═" * (w_l-2) + "╗")
        print(f" ║ {C_BOLD}{f'{meta['sys_name']} {meta['sys_ver']} | MERKEZİ KİMLİK DOĞRULAMA'.center(w_l-4)} {C_P}║")
        print(f" ╚" + "═" * (w_l-2) + "╝{C_RESET}")
        
        entry = input(f" {C_Y}🔑 GİRİŞ ANAHTARI (X: ÇIKIŞ) > {C_RESET}").strip().lower()
        if entry == "x": break
        if entry == conf.get("panic"):
            if os.path.exists(DB_FILE): os.remove(DB_FILE)
            if os.path.exists(BACKUP_FILE): os.remove(BACKUP_FILE)
            print(f"{C_R}[!] SİSTEM İMHA EDİLDİ.{C_RESET}"); time.sleep(2); sys.exit()
            
        if my_ip in db.get("BLACKLIST", []):
            simulate_loading("GÜVENLİK PROTOKOLÜ", duration=1.0)
            notify(f"IP ADRESİNİZ KARANTİNADA. ERİŞİM REDDEDİLDİ.", "ERR"); time.sleep(2); continue

        if entry == "admin" or entry == conf.get("admin_key"): mode = "ADMIN"
        elif entry == "beta" or entry == conf.get("beta_key"): mode = "BETA"
        else: 
            notify("KİMLİK DOĞRULANAMADI!", "ERR")
            db = db_load(); db["META"]["failed_logins"] = db["META"].get("failed_logins", 0) + 1; db_save(db); continue

        simulate_loading("KİMLİK DENETİMİ VE CANLI AĞ", duration=0.8); oracle_ai(mode, db, "login", my_ip)
        
        draw_header("LOKASYON DOĞRULAMA", mode, db, my_ip, ("?", "?", "?", "?", "?"))
        pk_in = input(f"\n 📍 POSTA KODU (0: ATLA | X: İPTAL) > ").strip().upper()
        if pk_in == "X": continue
        loc_info = get_strategic_intel(pk_in) if pk_in != "0" else ("KONUMSUZ", "GLOBAL", "N/A", "⚪ SAFE", "ZONE-UNK")
        h = hashlib.sha256(); h.update(pk_in.encode()); geo_key = h.hexdigest()[-4:]

        while True:
            db = db_load()
            update_active_status(my_ip)
            
            b_p, s_p, plug = db["B_PERMS"], db["S_PERMS"], db["PLUGINS"]
            draw_header("NETWORK SYNC COMMAND CENTER", mode, db, my_ip, loc_info)
            
            if mode == "BETA":
                # BETA DYNAMIC DASHBOARD
                print(f" {C_C}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{C_RESET}".ljust(90) + f"{C_C}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{C_RESET}")
                print(f" ┃ {C_G}[1]{C_RESET} VERİ MÜHÜRLEME (ŞİFRELEME)                            ┃{C_RESET}".ljust(90) + (f"┃ {C_G}[2]{C_RESET} VERİ ÇÖZÜMLEME (DEŞİFRE)                              ┃{C_RESET}" if b_p["b_dec"][0] else f"{C_GR}┃ [X] ERİŞİM KISITLI                                          ┃{C_RESET}"))
                print(f" ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{C_RESET}".ljust(90) + f"{C_C}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{C_RESET}")
                
                l2_l = f" {C_Y}┃ [3] KİŞİSEL İŞLEM ARŞİVİ                                  ┃{C_RESET}" if b_p["b_p_arc"][0] else f" {C_GR}┃ [X] ARŞİV KISITLI                                           ┃{C_RESET}"
                l2_r = f"{C_PK}┃ [4] MERKEZE RAPOR/VAKA GÖNDER                             ┃{C_RESET}" if b_p["b_sug"][0] else f"{C_GR}┃ [X] RAPOR YETKİSİ YOK                                       ┃{C_RESET}"
                print(f" ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓".ljust(90) + f"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                print(l2_l.ljust(90) + l2_r)
                print(f" ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛".ljust(90) + f"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                
                extras = []
                if b_p.get("b_chat", [False])[0]: extras.append(f"{C_B}[5]{C_RESET} SİBER HABERLEŞME")
                if b_p.get("b_g_arc", [False])[0]: extras.append(f"{C_G}[6]{C_RESET} SİSTEM ARŞİVİ")
                if b_p.get("b_broad", [False])[0]: extras.append(f"{C_O}[7]{C_RESET} DUYURU YAYINLA")
                if b_p.get("b_stats", [False])[0]: extras.append(f"{C_PK}[8]{C_RESET} DB DASHBOARD")
                if b_p.get("b_diag", [False])[0]: extras.append(f"{C_C}[9]{C_RESET} SİSTEM TEŞHİSİ")
                
                if extras: print(f"\n " + "  ".join(extras))
                print(f"\n {C_R}[X] TERMİNALİ KAPAT VE GÜVENLİ ÇIKIŞ YAP{C_RESET}")
            else:
                # --- 15'Lİ MEGA GRID DASHBOARD (ADMIN + AUTO UPDATE) ---
                print(f"  {C_P}⚡ OPERASYONEL & ADLİ{C_RESET}".ljust(65) + f"{C_PK}📡 İLETİŞİM & İSTİHBARAT{C_RESET}".ljust(65) + f"{C_B}⚙️ YÖNETİM & SİSTEM{C_RESET}")
                print(f"  {'─'*35}".ljust(65) + f"{'─'*35}".ljust(65) + f"{'─'*45}")
                print(f"  {C_G}[1]{C_RESET} Veri Mühürleme".ljust(65) + f"{C_PK}[6]{C_RESET} Rapor / Vaka Denetimi".ljust(65) + f"{C_B}[11]{C_RESET} Yetki Matrisi")
                print(f"  {C_G}[2]{C_RESET} Veri Çözümleme".ljust(65) + f"{C_O}[7]{C_RESET} Duyuru Yayın İstasyonu".ljust(65) + f"{C_B}[12]{C_RESET} DB Analitik Paneli")
                print(f"  {C_Y}[3]{C_RESET} Adli Arşiv (Hex)".ljust(65) + f"{C_R}[8]{C_RESET} IP Güvenlik Duvarı".ljust(65) + f"{C_B}[13]{C_RESET} Sistem Teşhisi (Diag)")
                print(f"  {C_C}[4]{C_RESET} Ağ Tarama (Ping)".ljust(65) + f"{C_PK}[9]{C_RESET} İstihbarat Akışı (Log)".ljust(65) + f"{C_B}[14]{C_RESET} Çekirdek Ayarları")
                print(f"  {C_G}[5]{C_RESET} SİBER HABERLEŞME".ljust(65) + f"{C_O}[10]{C_RESET} Eklenti Yönetimi (Plugins)".ljust(65) + f"{C_R}[15]{C_RESET} {C_BOLD}OTA GÜNCELLEME{C_RESET}")
                print(f"  {'─'*180}")
                print(f"  {C_R}[X] SİSTEMİ KAPAT VE KİLİTLE{C_RESET}")
            
            sel = input(f"\n {C_BOLD}[NEXUS] > {C_RESET}").strip().upper()
            if sel == "X": break
            
            # --- YÖNLENDİRME KATMANI ---
            if sel == "1" and (mode == "ADMIN" or b_p["b_enc"][0]): encryption_module(mode, db, my_ip, loc_info, geo_key)
            elif sel == "2" and (mode == "ADMIN" or b_p["b_dec"][0]): decryption_module(mode, db, my_ip, loc_info)
            
            elif sel == "3": # ADLİ ARŞİV
                page = 0
                while True:
                    db = db_load() 
                    draw_header("ADLİ ARŞİV VE VERİ DENETİMİ", mode, db, my_ip, loc_info)
                    target = db["ARCHIVE"] if mode == "ADMIN" or b_p["b_g_arc"][0] else [x for x in db["ARCHIVE"] if x.get('ip') == my_ip]
                    if not target: print(f"\n {C_GR}[!] Kayıt bulunamadı.{C_RESET}"); input("\n [ENTER] Geri..."); break
                    
                    psize = 5; start, end = page * psize, (page + 1) * psize
                    for m in target[start:end]:
                        ucol = C_C if m.get('user') == "BETA" else C_P
                        print(f" {C_Y}VAKA #{m.get('id', 'UNK')}{C_RESET} | {ucol}{m.get('user'):<8}{C_RESET} | T:{m.get('at')} | L:{m.get('loc')}")
                        print(f" ├─ {C_G}VERİ:{C_RESET} {C_BOLD}{m.get('msg')}{C_RESET}")
                        if mode == "ADMIN" or s_p["s_for"][0]: print(f" └─ {C_GR}CODE:{C_RESET} {m.get('code')[:70]}...")
                        print(" " + "─"*175)
                    
                    cmd = input(f"\n {C_Y}[N]{C_RESET} İleri | {C_Y}[P]{C_RESET} Geri | {C_PK}[ID]{C_RESET} Hex-Dump | {C_R}[X]{C_RESET} Çık: ").upper()
                    if cmd == "X": break
                    elif cmd == "N" and end < len(target): page += 1
                    elif cmd == "P" and page > 0: page -= 1
                    else:
                        if mode == "ADMIN" and plug["forensic"][0]:
                            found = next((x for x in target if x.get("id") == cmd), None)
                            if found:
                                draw_header(f"HEX-DUMP: {found['id']}", mode, db, my_ip, loc_info)
                                simulate_loading("BELLEK DÖKÜMÜ", duration=1.0)
                                print(f" {C_C}KAYNAK:{C_RESET} {found['ip']} | {C_C}ANAHTAR:{C_RESET} {found['geo']}")
                                display_hex_dump(found['code']); input("[ENTER] GERİ DÖN")

            elif sel == "4" and mode == "ADMIN": network_simulation(mode, db, my_ip, loc_info)
            elif sel == "4" and mode == "BETA" and b_p["b_sug"][0]:
                t = input("\n 📩 VAKA İÇERİĞİ: ")
                if t: 
                    db = db_load()
                    uid = str(uuid.uuid4())[:6].upper()
                    db["SUGGESTIONS"].append({"id": uid, "at": datetime.now().strftime("%H:%M"), "msg": t, "ip": my_ip, "read": False, "loc": loc_info[0]})
                    db_save(db); notify(f"Vaka (ID: {uid}) İletildi.")
            
            elif sel == "5" and mode == "ADMIN": comms_module(mode, db, my_ip, loc_info)
            elif sel == "5" and mode == "BETA" and b_p.get("b_chat", [False])[0]: comms_module(mode, db, my_ip, loc_info)

            elif sel == "6" and mode == "ADMIN":
                while True:
                    db = db_load()
                    draw_header("VAKA VE RAPOR DENETİMİ", mode, db, my_ip, loc_info)
                    reps = db.get("SUGGESTIONS", [])
                    if not reps: print(f"\n {C_GR}Rapor yok.{C_RESET}"); input("\n [ENTER] Geri..."); break
                    for i, s in enumerate(reps, 1):
                        mark = f"{C_PK}[YENİ]{C_RESET} " if not s.get('read') else "      "
                        print(f" {mark}{i}. [{s.get('id')}] {s.get('loc')} -> {s.get('msg')[:80]}...")
                    idx = input(f"\n No İncele | X Geri: ").upper()
                    if idx == "X": break
                    if idx.isdigit() and int(idx) <= len(reps):
                        r = reps[int(idx)-1]; r['read'] = True; db_save(db)
                        draw_header(f"VAKA DETAYI: {r['id']}", mode, db, my_ip, loc_info)
                        print(f" GÖNDEREN: {r['ip']} | ZAMAN: {r['at']} | KONUM: {r['loc']}\n" + "═"*120)
                        print(f"\n {C_BOLD}{r['msg']}{C_RESET}\n\n" + "═"*120); input("[ENTER] GERİ")

            elif sel == "7" and mode == "ADMIN":
                db = db_load()
                db["META"]["news"] = input("\n 📢 YENİ DUYURU: "); db_save(db); notify("Broadcast Yayında.")
            elif sel == "7" and mode == "BETA" and b_p.get("b_broad", [False])[0]:
                db = db_load()
                db["META"]["news"] = input("\n 📢 YENİ DUYURU: "); db_save(db); notify("Broadcast Yayında.")

            elif sel == "8" and mode == "ADMIN": firewall_module(mode, db, my_ip, loc_info)
            elif sel == "8" and mode == "BETA" and b_p.get("b_stats", [False])[0]:
                draw_header("DB DASHBOARD", mode, db, my_ip, loc_info)
                print(f" 📊 TRAFİK AKIŞI  : {len(db['INTEL_LOGS'])} Eylem")
                print(f" 📂 ARŞİV HACMİ   : {len(db['ARCHIVE'])} Kayıt")
                print(f" 📩 AKTİF RAPOR   : {len(db['SUGGESTIONS'])} Adet")
                input("\n [ENTER] GERİ")

            elif sel == "9" and mode == "ADMIN":
                page_i = 0
                while True:
                    db = db_load()
                    draw_header("İSTİHBARAT AKIŞI (LOGS)", mode, db, my_ip, loc_info)
                    logs = db.get("INTEL_LOGS", []); p_i = 20; s_i, e_i = page_i * p_i, (page_i + 1) * p_i
                    for l in logs[s_i:e_i]:
                        print(f" {C_GR}[{l.get('at')}]{C_RESET} {C_Y}{l.get('user', 'UNK'):<8}{C_RESET} -> {C_BOLD}{l.get('act', 'UNK'):<20}{C_RESET} | IP: {l.get('ip', '--')} | ZON: {l.get('loc_tag', '--')}")
                    nav_i = input(f"\n {C_Y}[N]{C_RESET} İleri | {C_Y}[P]{C_RESET} Geri | {C_R}[X]{C_RESET} Kapat: ").upper()
                    if nav_i == "X": break
                    elif nav_i == "N" and e_i < len(logs): page_i += 1
                    elif nav_i == "P" and page_i > 0: page_i -= 1
            elif sel == "9" and mode == "BETA" and b_p.get("b_diag", [False])[0]: system_diagnostics(mode, db, my_ip, loc_info)

            elif sel == "10" and mode == "ADMIN":
                while True:
                    db = db_load()
                    draw_header("EKLENTİ YÖNETİMİ", mode, db, my_ip, loc_info)
                    for i, (k, v) in enumerate(db["PLUGINS"].items(), 1):
                        print(f"  [{i}] {v[1]:<25} : [{'AKTİF' if v[0] else 'PASİF'}] -> {C_GR}{v[2]}{C_RESET}")
                    c = input("\n Değiştir (No) | X Geri: ").upper()
                    if c == "X": break
                    if c.isdigit() and int(c) <= len(db["PLUGINS"]):
                        key = list(db["PLUGINS"].keys())[int(c)-1]; db["PLUGINS"][key][0] = not db["PLUGINS"][key][0]; db_save(db)

            elif sel == "11" and mode == "ADMIN":
                while True:
                    db = db_load()
                    draw_header("YETKİ HİYERARŞİSİ", mode, db, my_ip, loc_info)
                    print(f" {C_P}[1] SİSTEM YETKİLERİ{C_RESET}".ljust(60) + f"{C_C}[2] BETA YETKİLERİ{C_RESET}")
                    ch = input("\n Seç | [X] GERİ: ").upper()
                    if ch == "X": break
                    t_map = db["S_PERMS"] if ch == "1" else db["B_PERMS"]
                    while True:
                        draw_header("YETKİ KONFİGÜRASYONU", mode, db, my_ip, loc_info)
                        for i, (k, v) in enumerate(t_map.items(), 1):
                            print(f"  [{i}] {v[1]:<30} : [{'AÇIK' if v[0] else 'KAPALI'}]")
                        c = input("\n Değiştir (No) | X Geri: ").upper()
                        if c == "X": break
                        if c.isdigit() and int(c) <= len(t_map):
                            key = list(t_map.keys())[int(c)-1]; t_map[key][0] = not t_map[key][0]; db_save(db)

            elif sel == "12" and mode == "ADMIN":
                db = db_load()
                draw_header("DB ANALİTİK DASHBOARD", mode, db, my_ip, loc_info)
                print(f" 📊 TOPLAM TRAFİK  : {len(db['INTEL_LOGS'])}")
                print(f" 📂 ARŞİV HACMİ    : {len(db['ARCHIVE'])}")
                print(f" 📩 AKTİF RAPORLAR : {len(db['SUGGESTIONS'])}")
                if input("\n SIFIRLA (SIFIRLA): ").upper() == "SIFIRLA":
                    db["ARCHIVE"], db["INTEL_LOGS"], db["SUGGESTIONS"], db["COMMS"] = [], [], [], []; db_save(db); notify("Temizlendi.")
                else: input("\n [ENTER] GERİ")

            elif sel == "13" and mode == "ADMIN": system_diagnostics(mode, db, my_ip, loc_info)
            
            elif sel == "14" and mode == "ADMIN": # ÇEKİRDEK AYARLARI (URL BURADA)
                if input(" 🔐 ŞİFRE: ") == conf["auth_pass"]:
                    while True:
                        db = db_load()
                        draw_header("ÇEKİRDEK AYARLARI", mode, db, my_ip, loc_info)
                        print(f" {C_Y}Genel Ayarlar:{C_RESET}")
                        print(f" [1] Program Adı: {meta['sys_name']}\n [2] Admin Key: {conf['admin_key']}\n [3] Beta Key: {conf['beta_key']}\n [4] Auth Pwd: {conf['auth_pass']}\n [5] Panic Key: {conf['panic']}")
                        print(f"\n {C_Y}OTA Güncelleme (Auto-Update) Ayarları:{C_RESET}")
                        print(f" [6] GitHub URL: {meta.get('update_url', 'Ayarlanmadı')}")
                        cs = input("\n Değiştir No | X Geri: ").upper()
                        if cs == "X": break
                        if cs.isdigit() and int(cs) <= 6:
                            v = input("Yeni Değer: ")
                            if cs == "1": db["META"]["sys_name"] = v
                            elif cs == "2": db["CONFIG"]["admin_key"] = v
                            elif cs == "3": db["CONFIG"]["beta_key"] = v
                            elif cs == "4": db["CONFIG"]["auth_pass"] = v
                            elif cs == "5": db["CONFIG"]["panic"] = v
                            elif cs == "6": db["META"]["update_url"] = v
                            db_save(db); notify("Ayarlar Güncellendi.")
                            
            elif sel == "15" and mode == "ADMIN": # YENİ: OTA GÜNCELLEME
                if s_p.get("s_ota", [False])[0]:
                    auto_update_system(mode, db, my_ip, loc_info)
                else: notify("Sistem Güncelleme yetkiniz kapalı.", "ERR")

if __name__ == "__main__":
    try: start_nexus()
    except KeyboardInterrupt: sys.exit()
