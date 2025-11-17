import os
import re

new_names = []

input_path = str(input("Place your path here: "))
input_path = input_path.replace("\"", "")
directory = rf"{input_path}"

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def append_index_name(length):
    global new_names
    list_index = []
    for x in range(1, length+1):
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
    new_name_with_ext = f"{new_name}{ext}"
    new_path = os.path.join(directory, new_name_with_ext)
    os.rename(old_path, new_path)
    print(f"Renamed '{old_name}' to '{new_name_with_ext}'")
print("done")
