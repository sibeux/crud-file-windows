import os
from mutagen.id3 import ID3, TPE1, TIT2, TALB  # type: ignore
from mutagen.flac import FLAC
from mutagen.mp4 import MP4


def get_mp3_metadata(file_path):
    try:
        tags = ID3(file_path)
        artist = tags.get("TPE1", None)
        title = tags.get("TIT2", None)
        album = tags.get("TALB", None)

        # Ambil nama file tanpa ekstensi
        file_name_without_ext = os.path.splitext(
            os.path.basename(file_path))[0]

        artist = ', '.join(artist)

        bul = True
        # bul = False

        if bul:
            artist = artist.replace("鳴潮", "Wuthering Waves")

        print(f"\"{file_name_without_ext} --- {artist if artist else ''}\",")

        # print(f"File: {file_name_without_ext}")
        # print(f"Title: {title.text[0] if title else 'Unknown'}")
        # print(f"Author: {author.text[0] if author else 'Unknown'}")
        # print(f"Album: {album.text[0] if album else 'Unknown'}")
    except Exception as e:
        print(f"Error reading metadata for {file_path}: {e}")


def get_flac_metadata(file_path, type):
    try:
        if type == "flac":
            audio = FLAC(file_path)
            artist = audio.get("artist", None)
            # title = audio.get("title", None)
            # album = audio.get("album", None)
        elif type == "alac":
            audio = MP4(file_path)
            artist = audio.get("\xa9ART", None)
            # title = audio.get("\xa9nam", None)
            # album = audio.get("\xa9alb", None)

        # Ambil nama file tanpa ekstensi
        file_name_without_ext = os.path.splitext(
            os.path.basename(file_path))[0]

        artist = ', '.join(artist)

        bul = True
        # bul = False

        if bul:
            artist = artist.replace("土屋俊輔", "Shunsuke Tsuchiya")
            artist = artist.replace("光田康典", "Yasunori Mitsuda")
            artist = artist.replace("辻 陽", "Yo Tsuji")
            artist = artist.replace("りぶ", "RIB")
            artist = artist.replace("吉澤嘉代子", "Yoshizawa Kayoko")
            artist = artist.replace("林ゆうき", "Yuki Hayashi")
            artist = artist.replace("妹S", "ImoutoS")
            artist = artist.replace("堤 博明", "Hiroaki Tsutsumi")
            artist = artist.replace("神前 暁", "Satoru Kosaki")
            artist = artist.replace("桶狭間ありさ", "Alisa Okehazama")
            artist = artist.replace("加藤達也", "Tatsuya Kato")
            artist = artist.replace("竹中だいち", "Daichi Takenaka")
            artist = artist.replace("内田ましろ", "Mashiro Uchida")
            artist = artist.replace("アオイエマ。", "Aoiema.")
            artist = artist.replace("大原ゆい子", "Yuiko Ōhara")
            artist = artist.replace("ケビン・ペンキン", "Kevin Penkin")
            artist = artist.replace("橋本由香利", "Yukari Hashimoto")
            artist = artist.replace("ヴォイド教信徒たち", "Void Cult Followers")
            artist = artist.replace("照井順政", "Yoshimasa Terui")
            artist = artist.replace("立山秋航", "Akiyuki Tateyama")
            artist = artist.replace("葛西竜之介", "Ryuunosuke Kasai")
            artist = artist.replace("純情のアフィリア", "Junjo no Afilia")
            artist = artist.replace("アフィリア・サーガ", "Afilia Saga")
            artist = artist.replace("イースト", "East")
            artist = artist.replace(
                "メメルン(CV.鈴木みのり)", "Memmeln (CV: Minori Suzuki)")
            artist = artist.replace(
                "超実在イグジスト(CV.宮野真守)", "Choujitsuzai Exister (CV: Mamoru Miyano)")
            artist = artist.replace(
                "本場切絵(CV:白石晴香)", "Kirie Motoba (CV: Haruka Shiraishi)")
            artist = artist.replace(
                "橘・シルフィンフォード(CV:古川由利奈)", "Sylphynford Tachibana (CV: Yurina Furukawa)")
            artist = artist.replace(
                "海老名菜々(CV:影山灯)", "Nana Ebina (CV: Akari Kageyama)")
            artist = artist.replace(
                "土間うまる(CV:田中あいみ)", "Umaru Doma (CV: Aimi Tanaka)")
            artist = artist.replace(
                "金子このみ(CV: 東城日沙子)", "Kaneko Konomi (CV: Tojo Hisako)")

        print(f"\"{file_name_without_ext} --- {artist if artist else ''}\",")
        # print(f"Title: {title[0] if title else 'Unknown'}")
        # print(f"Album: {album[0] if album else 'Unknown'}")
        # print(f"Artist: {artist[0] if artist else 'Unknown'}")
    except Exception as e:
        print(f"Error reading metadata for {file_path}: {e}")


# Ganti dengan path direktori yang sesuai
folder = "Sukimakaze"
directory_path = rf"C:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\{folder}\flac"
directory_path = r"C:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\Radiance Aflame\3"

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
