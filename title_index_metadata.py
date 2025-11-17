import os
from mutagen.id3 import ID3, TPE1, TIT2, TALB  # type: ignore
from mutagen.flac import FLAC
from mutagen.mp4 import MP4

# Ganti dengan path direktori yang sesuai
folder = "41-TV Anime Rent-A-Girlfriend 1st Season Original Soundtrack"
directory1 = rf"C:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\{folder}\flac"
# directory1 = rf"C:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\{folder}\2"

directory_path = directory1.replace("\\", "\\\\")

def get_mp3_metadata(file_path):
    try:
        tags = ID3(file_path)
        author = tags.get("TPE1", None)
        title = tags.get("TIT2", None)
        album = tags.get("TALB", None)

        # Ambil nama file tanpa ekstensi
        file_name_without_ext = os.path.splitext(os.path.basename(file_path))[0]

        print(f"File: {file_name_without_ext}")
        # print(f"Title: {title.text[0] if title else 'Unknown'}")
        print(f"Author: {author.text[0] if author else 'Unknown'}")
        # print(f"Album: {album.text[0] if album else 'Unknown'}")
    except Exception as e:
        print(f"Error reading metadata for {file_path}: {e}")


def get_flac_metadata(file_path, type):
    try:
        if type == "flac":
            audio = FLAC(file_path)
            artist = audio.get("artist", ["Unknown"])[0]
            title = audio.get("title", ["Unknown"])[0]
            album = audio.get("album", ["Unknown"])[0]
        elif type == "alac":
            """Mengambil metadata dari file ALAC (.m4a) menggunakan Mutagen."""
            # Gunakan kelas MP4 untuk file M4A (tempat ALAC disimpan)
            audio = MP4(file_path)
            # Tags MP4 menggunakan kunci khusus seperti '©art' (artist), '©nam' (title), '©alb' (album)
            # Nilai tag berupa list, jadi kita ambil elemen pertamanya ([0])
            artist = audio.get("©ART", ["Unknown"])[0]  # Artist
            title = audio.get("©nam", ["Unknown"])[0]  # Title
            album = audio.get("©alb", ["Unknown"])[0]  # Album

        # Ambil nama file tanpa ekstensi
        file_name_without_ext = os.path.splitext(os.path.basename(file_path))[0]
        
        if '"' in title:
            title = title.replace('\"', '\\"')
        print(f"\"{file_name_without_ext} --- {title if title else 'Unknown'}\",")
    except Exception as e:
        print(f"Error reading metadata for {file_path}: {e}")

# List semua file di direktori
files = os.listdir(directory_path)

# Filter hanya file (bukan direktori)
files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]

for file_name in files:
    file_path = os.path.join(directory_path, file_name)

    if file_name.lower().endswith(".mp3"):
        get_mp3_metadata(file_path)
    elif file_name.lower().endswith(".flac"):
        get_flac_metadata(file_path, "flac")
    elif file_name.lower().endswith(".m4a"):
        get_flac_metadata(file_path, "alac")