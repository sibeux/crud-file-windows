import os
import re
import invalid_char as inv_char

# Daftar nama file baru tanpa nomor urut dan waktu
new_names = [
"Lunar Eclipse",
"YUKAI",
"BYAKUGUN",
"Lunar Eclipse TV Edit",
"Lunar Eclipse Off Vocal",

]

# Direktori tempat file berada
# r"..." digunakan di depan string untuk memastikan Python tidak memperlakukan backslash sebagai karakter escape saat membaca string asli.
# r untuk raw string, agar backslash tidak dianggap sebagai escape character
# f untuk f-string, agar bisa menggunakan variabel di dalam string
folder = "Witch Watch ED2 Theme Tsuki to Watashi no Kakurenbo"
directory1 = rf"C:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\{folder}\flac"
# directory1 = rf"C:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\{folder}\2"
# directory1 = r"C:\Users\Nasrul Wahabi\Downloads\Video\1. Welcome To The Course!"

directory = directory1.replace("\\", "\\\\")

# Fungsi untuk mengekstrak nomor urut dari nama file
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

# Fungsi untuk membersihkan nama file dari karakter yang tidak diperbolehkan dengan pengganti karakter yang mirip
def sanitize_filename(filename):
    # Ganti setiap karakter yang tidak diperbolehkan dengan pengganti yang sesuai
    for invalid_char, replacement in inv_char.replacement.items():
        filename = filename.replace(invalid_char, replacement)

    return filename

# Fungsi untuk mengganti list new_names dengan list index
def append_index_name(length):
    global new_names
    list_index = []
    for x in range(1,length+1):
        list_index.append(f"{"{0:0=2d}".format(x)}")
    new_names = list_index.copy()

# Mendapatkan daftar semua file di direktori yang ditentukan
files = os.listdir(directory)

# Mengurutkan file berdasarkan nomor urut di nama file
sorted_files = sorted(files, key=natural_sort_key)

# Isi new_names dengan index
append_index_name(len(sorted_files))

# Pastikan jumlah file sesuai dengan jumlah nama baru
if len(sorted_files) != len(new_names):
    raise ValueError("Jumlah file tidak sesuai dengan jumlah nama baru.")

# Mengubah nama file
for old_name, new_name in zip(sorted_files, new_names):
    old_path = os.path.join(directory, old_name)
    _, ext = os.path.splitext(old_name)
    # Sanitasi nama baru
    sanitized_new_name = sanitize_filename(new_name)
    new_name_with_ext = f"{sanitized_new_name}{ext}"
    new_path = os.path.join(directory, new_name_with_ext)
    os.rename(old_path, new_path)
    print(f"Renamed '{old_name}' to '{new_name_with_ext}'")
