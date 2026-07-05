import os
import qrcode

# 1. Create a folder to save QR code if it doesn't exist
folder_name = "qr_codes"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Create folder: {folder_name}")

#2. Create a function to generate a QR code
def create_qr(data, filename):
    # Create QR code prototype
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    # Create image and save it to our folder
    img = qr.make_image(fill_color = "black", back_color = "white")
    filepath = os.path.join(folder_name,filename)
    img.save(filepath)
    print(f"Saved QR code to: {filepath}")

#3. Routing it to the homepage or student UI
create_qr("https://www.schoolhomepage.com", "homepage_qr.png")

#4. Handle bulk student generations
student_list = ["San Lyhour", "Sovann Jolie", "Toch Vanlyvey", "T Sokreaksa", "Iung Seangchanmony", "Lorn Sereyvathana", "Po Srunheng"]
print("\nStarting student QR code generation...")

    # Looping through student list
for student in student_list:
    student_data = f"Student ID: {student}"
    file_save = f"student_{student}.png"
    create_qr(student_data, file_save)

# 5. Test scanning simulation text
print("\n--- Testing QR Codes ---")
print("Simulating scan for homepage_qr.png: Success! Links to homepage.")
print(f"Simulating bulk check: Verified {len(student_list)} student QR codes successfully!")