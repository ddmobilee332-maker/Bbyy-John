import os
import sys
import json
from logo import show_logo
from obfuscator import process_script
from uploader import upload_to_github

# สเปคค่าคงที่
API_KEY = "Abf18cbe-30e1-949b-f742-cad8bfd77d6d00"
GITHUB_REPO = "ddmobilee332-maker/Byy-John"
TEMP_CODE_FILE = ".current_code.txt"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def main_menu():
    current_script = ""
    clear_screen()
    print("=== PROJECT ย่อ SCRIPT BY RUENYAI HUB ===")
    print("กรุณาใส่คำสั่งเริ่มต้นเพื่อทำงาน...")
    
    while True:
        cmd = input("\n[Termux]:~# ").strip()
        
        if cmd == "oop":
            clear_screen()
            show_logo()
            print("\n[ระบบ]: เข้าสู่หน้าหลักเรียบร้อยแล้ว (พร้อมรับคำสั่งถัดไป)")
            
        elif cmd == "oopp":
            print("\n[ระบบ]: กรุณาวางโค้ด Roblox Script ของคุณที่นี่ (กด Ctrl+D หรือ Ctrl+Z แล้ว Enter เมื่อวางเสร็จ):")
            try:
                lines = sys.stdin.read()
                if lines.strip():
                    current_script = lines
                    with open(TEMP_CODE_FILE, "w", encoding="utf-8") as f:
                        f.write(current_script)
                    print("\n[ระบบ]: บันทึกโค้ดเข้าสู่ระบบชั่วคราวสำเร็จ!")
                else:
                    print("\n[คำเตือน]: ไม่พบโค้ดที่คุณวาง กรุณาลองใหม่")
            except Exception as e:
                print(f"\n[ข้อผิดพลาด]: {e}")
                
        elif cmd == "oopp2":
            if not os.path.exists(TEMP_CODE_FILE) or current_script == "":
                print("\n[ระบบตรวจสอบ]: ❌ ตอนนี้ไม่มีโค้ดอยู่ในระบบ! กรุณาใส่โค้ดด้วยคำสั่ง 'oopp' ก่อน")
                continue
                
            print("\n[ระบบตรวจสอบ]:  พบโค้ดพร้อมทำรายการ")
            confirm = input("คุณต้องการจะย่อโค้ดนี้ใช่หรือไม่? (y/n): ").strip().lower()
            
            if confirm == 'y':
                print("\n[1/2] กำลังส่งโค้ดไปยำผ่าน API และลงระบบป้องกันแบบหนาพิเศษ...")
                obfuscated_code = process_script(current_script, API_KEY)
                
                if obfuscated_code:
                    print("[2/2] กำลังนำโค้ดที่ย่อเสร็จแล้วไปยัดลง GitHub...")
                    raw_url = upload_to_github(obfuscated_code, GITHUB_REPO)
                    
                    if raw_url:
                        clear_screen()
                        show_logo()
                        print("\n" + "="*60)
                        print("🎉 ย่อสคริปต์และป้องกันการแกะสำเร็จเรียบร้อย! 🎉")
                        print("="*60)
                        print(f'\nloadstring(game:HttpGet("{raw_url}"))()')
                        print("\n" + "="*60)
                        # เคลียร์ค่าหลังเสร็จงาน
                        if os.path.exists(TEMP_CODE_FILE):
                            os.remove(TEMP_CODE_FILE)
                        current_script = ""
                    else:
                        print("\n[ล้มเหลว]: เกิดข้อผิดพลาดในขั้นตอนอัปโหลดขึ้น GitHub")
                else:
                    print("\n[ล้มเหลว]: การทำ Obfuscate ผ่าน API ไม่สำเร็จ")
            else:
                print("\n[ระบบ]: ยกเลิกการย่อโค้ด")
                
        elif cmd == "exit":
            print("ปิดการทำงานโปรเจค ย่อ script. สวัสดีค่ะ!")
            break
        else:
            print(f"[ข้อผิดพลาด]: ไม่รู้จักคำสั่ง '{cmd}' (คำสั่งที่ใช้งานได้: oop, oopp, oopp2)")

if __name__ == "__main__":
    main_menu()
                  
