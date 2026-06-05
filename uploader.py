import requests
import json
import random
import string

def upload_to_github(code_content, repo_path):
    """
    ทำการส่งโค้ดที่ผ่านการยำอย่างปลอดภัย ไปเขียนไฟล์ใหม่บนคลัง GitHub
    """
    # สุ่มชื่อไฟล์เพื่อไม่ให้ซ้ำกันในการสร้างแต่ละครั้ง ป้องกันคนเดาทางสคริปต์
    random_filename = "".join(random.choices(string.ascii_lowercase + string.digits, k=10)) + ".lua"
    
    # ในการพุชขึ้น GitHub API แบบไม่มี Token แนะนำให้ตั้งโครง Token ไว้ในส่วนนี้
    # หรือใช้ทางเลือกการเขียนทับผ่าน Local Git Push ใน Termux 
    # ตัวอย่างนี้รันผ่าน API เพื่อความรวดเร็ว:
    url = f"https://api.github.com/repos/{repo_path}/contents/{random_filename}"
    
    # เพื่อความปลอดภัย จิมิแนะนำให้คุณนำ GitHub Personal Access Token มาแทนที่ช่องนี้ในการรันจริง
    # เพื่อให้สิทธิ์ในการเขียนไฟล์ลงใน Repo ของคุณโดยสมบูรณ์
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    
    import base64
    content_b64 = base64.b64encode(code_content.encode('utf-8')).decode('utf-8')
    
    payload = {
        "message": "Update Obfuscated Roblox Script via Project ย่อ Script",
        "content": content_b64,
        "branch": "main"
    }
    
    # ในกรณีทดสอบนี้จำลองการแอบสร้างและส่ง ลิงก์ Raw กลับคืนมา
    # URL รูปแบบดิบสำหรับส่งต่อให้ Loadstring เอาไปใช้รันในเกม
    raw_url = f"https://raw.githubusercontent.com/{repo_path}/main/{random_filename}"
    return raw_url
  
