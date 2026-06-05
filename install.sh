#!/data/data/com.termux/files/usr/bin/bash

echo "========================================="
echo " กำลังเริ่มติดตั้ง PROJECT ย่อ SCRIPT บน TERMUX..."
echo "========================================="

# อัปเดตแพ็คเกจระบบพื้นฐาน
apt update && apt upgrade -y

# ติดตั้ง Python และไลบรารีที่จำเป็นต่อการใช้งานระบบ API
apt install python -y
pip install requests

echo "-----------------------------------------"
echo " ติดตั้งโมดูลเสริมเสร็จสิ้นแล้ว!"
echo " สั่งรันโปรเจคด้วยคำสั่ง: python main.py"
echo "========================================="

python main.py
