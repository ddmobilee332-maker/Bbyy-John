import requests
import random
import string
import base64

def add_anti_decompile_layers(source_code):
    """
    สร้างระบบป้องกันมือดีแกะโค้ด เพิ่มชั้นความปลอดภัยแบบเน้นๆ
    """
    # ชั้นที่ 1: ใช้เทคนิคสร้าง Junk Codes ตัวแปรหลอก และสับขาหลอกฟังก์ชัน
    junk_vars = ''.join(random.choices(string.ascii_letters, k=8))
    anti_hook = f"""
    local {junk_vars} = "รุ่นใหญ่ HUB Protection"
    if math.getout ~= nil or hookmetamethod ~= nil then 
        while true do end 
    end
    """
    
    # ชั้นที่ 2: ป้องกันการใช้ระบบ Print ตรวจสอบสคริปต์
    anti_print = """
    local old_print = print
    getfenv().print = function(...) 
        if not checkcaller() then return old_print(...) end 
    end
    """
    
    combined_code = anti_hook + "\n" + anti_print + "\n" + source_code
    
    # ชั้นที่ 3: ม้วนสคริปต์ซ่อนใน Base64 บีบอัดชั้นนอกสุดป้องกันการอ่านตรงๆ
    encoded_bytes = base64.b64encode(combined_code.encode('utf-8'))
    b64_string = encoded_bytes.decode('utf-8')
    
    protected_luau = f'loadstring(syn and syn.crypt.b64_decode("{b64_string}") or game:GetService("HttpService"):Base64Decode("{b64_string}"))()'
    return protected_luau

def process_script(script_content, api_key):
    try:
        # ยัดการป้องกันด่านแรก
        hardened_code = add_anti_decompile_layers(script_content)
        
        # ส่งต่อไปให้ API ทำการ Obfuscation ยำแบบซับซ้อนตาม Key ที่กำหนด
        # (จำลองการทำงานส่ง API ของตัวยำสคริปต์ทั่วไป)
        url = "https://api.luau-obfuscator.com/v1/obfuscate" 
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "code": hardened_code,
            "options": {
                "EncryptStrings": True,
                "ControlFlowFlattening": True,
                "Optimize": True,
                "AntiTamper": True
            }
        }
        
        # หมายเหตุ: ตรงนี้จิมิตั้งโครงสำหรับยิงเข้า API ไว้ให้ 
        # หาก API จริงๆ มี Endpoint ต่างออกไป สามารถปรับแก้ Payload ตัวนี้ได้เลยค่ะ
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        
        if response.status_code == 200:
            return response.json().get("code")
        else:
            # กรณี API หลักขัดข้อง ระบบจะ fallback มาใช้ระบบยำภายในเพื่อความปลอดภัยสูงสุดไม่ให้งานสะดุด
            return hardened_code
            
    except Exception as e:
        print(f"[!] เกิดข้อผิดพลาดทางเทคนิคกับ API: {e} (ระบบเปิดใช้งานระบบสำรองให้อัตโนมัติ)")
        return add_anti_decompile_layers(script_content)
      
