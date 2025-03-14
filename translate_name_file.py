import os
import re

# Daftar nama file baru tanpa nomor urut dan waktu
new_names = [
    "The Rose of Versailles",
    "Ma Vie en Rose",
    "Enchanting Masquerade",
    "Our King and Queen",
    "Soul to Soul",
    "Resonance of Love",
    "Nowhere Heart",
    "Believe in My Way",
    "Never Surrender",
    "Return to Nothing",
    "Ravine",
    "Child of Mars",
    "Anger and Pain",
    "Before Dawn Comes",
    "Libération",
    "The Rose of Versailles (Movie Edit)",
    "Ma Vie en Rose (Movie Edit)",
    "Enchanting Masquerade (Movie Edit)",
    "Soul to Soul (Movie Edit)",
    "Resonance of Love (Movie Edit)",
    "Nowhere Heart (Movie Edit)",
    "Never Surrender (Movie Edit)",
    "Ravine (Movie Edit)",
    "Child of Mars (Movie Edit)",
    "Before Dawn Comes (Movie Edit)"

]

# Direktori tempat file berada
# r"..." digunakan di depan string untuk memastikan Python tidak memperlakukan backslash sebagai karakter escape saat membaca string asli.
# r untuk raw string, agar backslash tidak dianggap sebagai escape character
# f untuk f-string, agar bisa menggunakan variabel di dalam string
folder = "Song Collection from The Rose of Versailles"
directory1 = rf"C:\Users\Nasrul Wahabi\Downloads\Music\{folder}\flac"

directory = directory1.replace("\\", "\\\\")

# Fungsi untuk mengekstrak nomor urut dari nama file
def extract_number(filename):
    match = re.match(r'(\d+)', filename)
    return int(match.group(1)) if match else float('inf')

# Fungsi untuk membersihkan nama file dari karakter yang tidak diperbolehkan dengan pengganti karakter yang mirip
def sanitize_filename(filename):
    # Peta pengganti karakter
    replacements = {
        "'": '’',
        '"': '”',
        '<': '‹',
        '>': '›',
        ':': '⁚',
        '꞉': '⁚',
        '∶': '⁚',
        '/': '⁄',
        '\\': '⁄',
        '|': '―',
        '?': '⁇',
        '？': '⁇',
        '*': '⁕',
        ';': '⁏',
    }
    
    # Ganti setiap karakter yang tidak diperbolehkan dengan pengganti yang sesuai
    for invalid_char, replacement in replacements.items():
        filename = filename.replace(invalid_char, replacement)
    
    return filename

# Mendapatkan daftar semua file di direktori yang ditentukan
files = os.listdir(directory)

# Mengurutkan file berdasarkan nomor urut di nama file
sorted_files = sorted(files, key=extract_number)

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
