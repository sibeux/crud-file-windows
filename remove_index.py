import os
import re
import invalid_char as inv_char

# Ganti dengan path direktori yang sesuai
# r"..." digunakan di depan string untuk memastikan Python tidak memperlakukan backslash sebagai karakter escape saat membaca string asli.
# r untuk raw string, agar backslash tidak dianggap sebagai escape character
# f untuk f-string, agar bisa menggunakan variabel di dalam string
folder = "Heart"
directory_path = rf"C:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\{folder}\flac"
# directory_path = rf"C:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\{folder}\2"

pattern = re.compile(r"^\d{2}\. ")  # contoh: "01. "
# pattern = re.compile(r"^\d{2} - ") # contoh: "01 - "
# pattern = re.compile(r"^\d{2}-") # contoh: "01-"
# pattern = re.compile(r"^\d{2}_") # contoh: "01_"
# pattern = re.compile(r"^\d{2}\.") # contoh: "01."
# pattern = re.compile(r"^\d{2} ")  # contoh: "01 "
# pattern = re.compile(r"^\d{1}\. ") # contoh: "1. "
# pattern = re.compile(r"^\d{1} - ") # contoh: "1 - "
# pattern = re.compile(r"^\d{1}\.\d{2} ")  # contoh: "1.01 "
# pattern = re.compile(r"^\d{2}\.\d{2} ")  # contoh: "10.01 "
# pattern = re.compile(r"^\d{1}\.\d{2}. ") # contoh: "1.01. "
# pattern = re.compile(r"^\d{1}\-\d{2} – ") # contoh: "1-16 – "
# pattern = re.compile(r"^\d{1}\-\d{2} ") # contoh: "1-16 "
# pattern = re.compile(r"^\(\d{2}\) ") # contoh: "(01) "
# pattern = re.compile(r"- ") # contoh: "- "
# pattern = re.compile(r" ") # contoh: " "

# *** custom pattern *** #
# kalau ada tanda kurung, harus di-escape dengan backslash = r"Taiji Koga \(Piano\) - "
# pattern = re.compile(r"\[Artemis\] ")
# pattern = re.compile(r"Mr.Kitty - ")


def sanitize_filename(filename):
    # Ganti setiap karakter yang tidak diperbolehkan dengan pengganti yang sesuai
    for invalid_char, replacement in inv_char.replacement.items():
        filename = filename.replace(invalid_char, replacement)

    return filename


# Loop melalui semua file di direktori
for filename in os.listdir(directory_path):
    old_file_path = os.path.join(directory_path, filename)

    # Hanya proses file, bukan direktori
    if os.path.isfile(old_file_path):
        # Cek apakah filename dimulai dengan pola yang ingin dihapus
        new_filename = pattern.sub("", filename)

        # Untuk menghapus kata di belakang
        # new_filename = filename.replace(" [Japanese ver.]", "")

        # Untuk menambah kata di belakang
        # new_filename = filename.replace(".flac", " [Japanese ver.].flac")

        # Hasilkan path baru
        new_file_path = os.path.join(directory_path, new_filename)

        # Rename file
        os.rename(old_file_path, new_file_path)
        new_filename = sanitize_filename(new_filename)
        print(f"File {filename}-----→{new_filename}")
