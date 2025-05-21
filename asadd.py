import requests
import os
import random
import json
import datetime
from urllib.parse import unquote, quote, urlparse, unquote


def generate_random_duration():
    # Durasi dalam detik, antara 30 detik dan 5 menit (300 detik)
    duration_seconds = random.randint(30, 300)
    minutes = duration_seconds // 60
    seconds = duration_seconds % 60
    return f"{minutes:02}:{seconds:02}"


def escape_sql_string(value):
    # Escape single quotes by doubling them
    return value.replace("'", "''")


def escape_ampersand(url):
    # Mengencode ampersand menjadi %26
    if "&" in url:
        return url.replace("&", "%26")
    if " " in url:
        return url.replace(" ", "%20")
    else:
        return url


def escape_url(url):
    # Mengencode karakter khusus lainnya menggunakan urllib
    return quote(url, safe=":/")


def get_artist_from_title(title, list_title_artist):
    """Fungsi untuk mencocokkan judul dan menemukan artis yang sesuai."""
    for item in list_title_artist:
        # Pisahkan berdasarkan ' --- '
        song_title, artist = item.split(' --- ')
        if title.lower() == song_title.lower():  # Cocokkan tanpa memperhatikan huruf besar/kecil
            return artist
    return ""  # Return empty string jika tidak ditemukan


def fetch_github_files(repo_url):
    # Ekstrak informasi pemilik, repository, dan path folder dari URL
    parts = repo_url.split("/")
    owner = parts[3]
    repo = parts[4]
    folder_path = "/".join(parts[7:])
    music_path = []

    # Daftar pasangan nama lagu dan artis
    list_title_artist = []

    cover_link = ""
    category = ""
    artist = ""
    album = ''

    is_dynamic_artist = False
    disc = 0

    folder_api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{folder_path}"
    folder_response = requests.get(folder_api_url)

    if folder_response.status_code == 200:
        files = folder_response.json()
        for file in files:
            if file["type"] == "dir":
                file_name_without_ext = os.path.splitext(file["name"])[0]
                if file_name_without_ext == "flac":
                    music_path.append(file["path"])
                if file_name_without_ext.isdigit():
                    music_path.append(file["path"])
            if file['name'] == '.here.txt':
                response = requests.get(file["download_url"])
                text_content = json.loads(response.text)
                category = text_content["category"]
                album = text_content["title"]
                artist = text_content["author"]
                if text_content['disc'] != '0':
                    is_dynamic_artist = True
                    disc = int(text_content['disc']) - 1
                    for i in range(disc+1):
                        list_title_artist.append(
                            text_content[str(i+1)]
                        )
                elif text_content['1'] != []:
                  is_dynamic_artist = True
                  list_title_artist.append(text_content["1"])
            if file['type'] == 'file':
                if os.path.splitext(file["name"])[1] == '.jpg' or os.path.splitext(file["name"])[1] == '.png' or os.path.splitext(file["name"])[1] == '.jpeg':
                    cover_link = file["download_url"]

    # Starting timestamp for date_added
    base_time = datetime.datetime.now().replace(microsecond=0)

    # Base SQL INSERT statement template
    insert_statement_template = "INSERT INTO music (id_music, category, link_gdrive, title, artist, album, time, cover, favorite, date_added) VALUES \n"
    playlist_insert_statement_template = "INSERT INTO `playlist` (`uid`, `name`, `image`, `type`, `author`, `pin`, `date_pin`, `date`, `editable`) VALUES \n"

    # Parameters for the static fields
    # 1 = IndoPride
    # 2 = 日本の歌
    # 3 = Jowo Mletre
    # 4 = Worldwide
    favorite = "0"

    # Collecting each row of values
    values = []
    playlist_value = []

    for x in range(disc+1):
        # Buat URL API untuk folder
        api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{music_path[x]}"

        # Lakukan request ke API GitHub
        response = requests.get(api_url)

        if response.status_code == 200:
            files = response.json()
            index = 0
            album_disc = f"{album} Disc {x+1}"
            album_name = ''
            if disc > 0:
              album_name = album_disc
            else:
              album_name = album
            for file in files:
                if file["type"] == "file":
                    # Hapus ekstensi file untuk menampilkan nama file tanpa ekstensi
                    file_name_without_ext = os.path.splitext(file["name"])[0]

                    # cari artist berdasarkan nama file
                    if is_dynamic_artist:
                        artist = get_artist_from_title(
                            file_name_without_ext, list_title_artist[x])

                    date_added = base_time + datetime.timedelta(seconds=index)
                    date_added_str = date_added.strftime("%Y-%m-%d %H:%M:%S")

                    index += 1

                    duration = generate_random_duration()

                    # Escape special characters in the values
                    artist = escape_sql_string(artist)
                    album = escape_sql_string(album)

                    # mendapatkan link github yang bisa di-stream
                    download_music_link = file['download_url']
                    # mendapatkan link file yang versi encode
                    name_file_link_html = file['html_url']
                    # mengambil nama file dan ekstensi dari link html
                    name_link_encoded = name_file_link_html.split('/')[-1]
                    # memasukkan ke dalam link stream dengan nama file encode
                    music_link = download_music_link.rsplit(
                        '/', 1)[0] + '/' + name_link_encoded

                    # Encode ampersand
                    music_link = escape_ampersand(music_link)
                    # Encode other special characters
                    music_link = escape_url(music_link)
                    # Unquote untuk menghapus encoding berlebih
                    music_link = unquote(music_link)

                    cover_link = escape_sql_string(cover_link)
                    cover_link = cover_link.replace(
                        "https://github.com/",
                        "https://raw.githubusercontent.com/"
                    ).replace(
                        "/blob/",
                        "/refs/heads/"
                    )
                    date_added_str = escape_sql_string(date_added_str)

                    values.append(
                        f"(NULL, '{category}', '{music_link}', '{file_name_without_ext}', '{artist}', '{album_name}', '{duration}', '{cover_link}', '{favorite}', '{date_added_str}')"
                    )
                    if x == 0 and index == 1:
                      playlist_value.append(
                          f"(NULL, '{album}', '{cover_link}', 'album', '{artist}', 'false', NULL, NOW(), 'false')"
                      )
        else:
            print("Error:", response.status_code, response.json())

    # Joining all values into the final SQL INSERT statement
    insert_statement = insert_statement_template + \
        ",\n".join(values) + ";"
    playlist_insert_statement = playlist_insert_statement_template + \
        ",\n".join(playlist_value) + ";"
    print(insert_statement)
    print(playlist_insert_statement)


# Contoh penggunaan dengan URL yang kamu berikan
repo_url = "https://github.com/cybeat-music/ninkoro-ost/tree/main/ninkoro-ost"

fetch_github_files(repo_url)
