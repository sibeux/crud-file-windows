import os

# Ganti dengan path direktori yang sesuai
directory_path = r"C:\Users\Nasrul Wahabi\Downloads\Music\Summer Lights\flac"

# Loop melalui semua file di direktori
for filename in os.listdir(directory_path):
    old_file_path = os.path.join(directory_path, filename)

    # Hanya proses file, bukan direktori
    if os.path.isfile(old_file_path):
        new_filename = filename.replace(".flac", " (feat. isui).flac")

        # Hasilkan path baru
        new_file_path = os.path.join(directory_path, new_filename)

        # Rename file
        os.rename(old_file_path, new_file_path)
        print(f"File {filename}-----→{new_filename}")
