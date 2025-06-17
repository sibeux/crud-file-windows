import os
import re
import invalid_char as inv_char

# Ganti dengan path direktori yang sesuai
# r"..." digunakan di depan string untuk memastikan Python tidak memperlakukan backslash sebagai karakter escape saat membaca string asli.
# r untuk raw string, agar backslash tidak dianggap sebagai escape character
# f untuk f-string, agar bisa menggunakan variabel di dalam string
folder = "Unnamed Memory OST"
directory_path = rf"C:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\{folder}\flac"
# directory_path = r"C:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\Radiance Aflame\3"

# List semua file di direktori
files = os.listdir(directory_path)

# Filter hanya file (bukan direktori)
files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]

# List untuk menyimpan file yang mengandung karakter petik
files_with_single_quote = []
files_with_double_quote = []
files_with_symbols = []

# Regular expression untuk mendeteksi simbol selain huruf dan angka
symbol_pattern = re.compile(r'[^a-zA-Z0-9.\-_ ]')

# Cek setiap file dan ganti karakter petik dengan backtick
for file_name in files:
    new_file_name = file_name
    for invalid_char, replacement in inv_char.replacement.items():
        new_file_name = new_file_name.replace(invalid_char, replacement)
        if invalid_char in file_name:
            files_with_single_quote.append(file_name)
    if symbol_pattern.search(file_name):
        files_with_symbols.append(file_name)

    # Rename file jika ada perubahan
    if new_file_name != file_name:
        os.rename(
            os.path.join(directory_path, file_name),
            os.path.join(directory_path, new_file_name)
        )
        print(f"Renamed: {file_name} -> {new_file_name}")

# Cetak hasil
if files_with_single_quote:
    print("\nFile yang mengandung karakter petik tunggal:")
    for file_name in files_with_single_quote:
        print(f"- {os.path.join(directory_path, file_name)}")

if files_with_double_quote:
    print("\nFile yang mengandung karakter petik ganda:")
    for file_name in files_with_double_quote:
        print(f"- {os.path.join(directory_path, file_name)}")

if files_with_symbols:
    print("\nFile yang mengandung simbol selain huruf dan angka:")
    for file_name in files_with_symbols:
        print(f"- {os.path.join(directory_path, file_name)}")

if not files_with_single_quote and not files_with_double_quote:
    print("Tidak ada file yang mengandung karakter petik tunggal atau ganda.")
