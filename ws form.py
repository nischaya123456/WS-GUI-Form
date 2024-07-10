import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("สมัครสมาชิก")
root.geometry("380x720")

title_label = tk.Label(root, text="สมัครสมาชิก", font=("Helvetica", 13), bg="yellow", width=45).pack()

personal_info_frame = ttk.LabelFrame(root, text="ข้อมูลส่วนตัว")
personal_info_frame.pack(pady=10, padx=10, fill="x")

# Title
ttk.Label(personal_info_frame, text="คำนำหน้า:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
title = ttk.Combobox(personal_info_frame, values=["นาย", "นาง", "นางสาว"]).grid(row=0, column=1, padx=5, pady=5)

# First
ttk.Label(personal_info_frame, text="ชื่อ:").grid(row=1, column=0, padx=4, pady=4, sticky="e")
first_name = ttk.Entry(personal_info_frame).grid(row=1, column=1, padx=4, pady=4)

# Last
ttk.Label(personal_info_frame, text="นามสกุล:").grid(row=2, column=0, padx=4, pady=4, sticky="e")
last_name = ttk.Entry(personal_info_frame).grid(row=2, column=1, padx=4, pady=4)

# Date
ttk.Label(personal_info_frame, text="วัน/เดือน/ปี:").grid(row=3, column=0, padx=4, pady=4, sticky="e")
dob = ttk.Entry(personal_info_frame).grid(row=3, column=1, padx=4, pady=4)

# Gender
ttk.Label(personal_info_frame, text="เพศ:").grid(row=4, column=0, padx=4, pady=4, sticky="e")
gender_frame = ttk.Frame(personal_info_frame)
gender_frame.grid(row=4, column=1, padx=4, pady=4)
gender = tk.StringVar()
ttk.Radiobutton(gender_frame, text="ชาย", variable=gender, value="ชาย").pack(side="left")
ttk.Radiobutton(gender_frame, text="หญิง", variable=gender, value="หญิง").pack(side="left")
ttk.Radiobutton(gender_frame, text="ไม่ระบุ", variable=gender, value="ไม่ระบุ").pack(side="left")

# Address
ttk.Label(personal_info_frame, text="หมายเลขโทรศัพท์:").grid(row=5, column=0, padx=4, pady=4, sticky="e")
address = ttk.Entry(personal_info_frame).grid(row=5, column=1, padx=4, pady=4)

# Phone Number
ttk.Label(personal_info_frame, text="ที่อยู่:").grid(row=6, column=0, padx=4, pady=4, sticky="e")
phone = ttk.Entry(personal_info_frame).grid(row=6, column=1, padx=4, pady=4)

ttk.Label(personal_info_frame, text="อำเภอ:").grid(row=7, column=0, padx=4, pady=4, sticky="e")
description = ttk.Entry(personal_info_frame).grid(row=7, column=1, padx=4, pady=4)

ttk.Label(personal_info_frame, text="จังหวัด:").grid(row=8, column=0, padx=4, pady=4, sticky="e")
id_card = ttk.Entry(personal_info_frame).grid(row=8, column=1, padx=4, pady=4)

# Password
ttk.Label(personal_info_frame, text="รหัสไปรษณีย์:").grid(row=9, column=0, padx=4, pady=4, sticky="e")
password = ttk.Entry(personal_info_frame, show="*").grid(row=9, column=1, padx=4, pady=4)

# Hobbies
hobbies_frame = ttk.LabelFrame(root, text="งานอดิเรก")
hobbies_frame.pack(pady=9, padx=9, fill="x")
hobbies = []
hobby_list = ["อ่านหนังสือ", "เล่นเกม", "ดูหนัง", "ฟังเพลง", "ปลูกต้นไม้", "ท่องเที่ยว" ,"อื่นๆ..."]
for idx, hobby in enumerate(hobby_list):
    var = tk.BooleanVar()
    ttk.Checkbutton(hobbies_frame, text=hobby, variable=var).grid(row=idx//4, column=idx%4, padx=4, pady=4, sticky="w")
    hobbies.append(var)

# User Frame
user_info_frame = ttk.LabelFrame(root, text="ข้อมูลผู้ใช้")
user_info_frame.pack(pady=9, padx=9, fill="x")

# Username
ttk.Label(user_info_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
username = ttk.Entry(user_info_frame)
username.grid(row=0, column=1, padx=5, pady=5)

# Password
ttk.Label(user_info_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
user_password = ttk.Entry(user_info_frame, show="*")
user_password.grid(row=1, column=1, padx=5, pady=5)

# Button
button_frame = ttk.Frame(root)
button_frame.pack(pady=20)
ttk.Button(button_frame, text="สมัครสมาชิก").pack(side="left", padx=10)
ttk.Button(button_frame, text="ยกเลิกสมัคร").pack(side="right", padx=10)

root.mainloop()
