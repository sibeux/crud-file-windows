import os
import re
import invalid_char as inv_char

# Daftar nama file baru tanpa nomor urut dan waktu
new_names = [
    "Unnamed Memory a Nameless Fairytale",
"Peaceful Days ~The King's Rest~",
"Peaceful Days ~The Witch's Grace~",
"A Friendly Smile",
"Enveloped by Night",
"The Chaotic Pair",
"The Blue Tower Rising in the Wasteland",
"An Unpleasant Wind",
"Crawling Hostility",
"The Crossroads",
"Malice Lurking in the Shadows",
"A Serpent Glares from Afar",
"A Veiled Presence",
"Whispers Along the Spine",
"An Irredeemable Dream of the Past",
"Arms That Should Have Been Warm",
"An Unreadable Opponent",
"At the End of Longing",
"Dreaming of Happiness",
"Loving You, Just as You Are",
"Tangled Wish",
"Blessing and Curse",
"One Who Lurks in the Shadows of History",
"Age of Witches",
"A Pure White Flash",
"For the Day We Must Confront",
"Freezing Air",
"Endless Madness",
"An Eternal Wish",
"The Spark of War",
"A Confused Battlefield",
"Let's Win with Ease",
"Clash with a Threat",
"For What I'd Trade the World to Hold Again",
"Awakening Passion",
"Nesting in Human Hearts",
"A Whirlpool of Hatred",
"One Who Knows All That Was Lost",
"The Hollow Monarch",
"Perfectly Similar, Yet Unstable",
"An Enigmatic Smile",
"In the Corner of Daily Life",
"Clan of Proud Pillagers",
"A God Who Spreads Madness",
"Pleasure Bathed in Moonlight",
"Ruler of Demons",
"At the End of an Act",
"Conversation Between Two",
"Interlude",
"Here Lies Glory",
"Under Tension",
"Offense and Defense",
"Like a Child",
"Guided by a Wish",
"Swelling Anguish",
"Where Longing Leads",
"Footsteps in the Shadows",
"The Evil One",
"Beautiful Forces",
"Sealed Memories",
"The Artifact: Eleterria",
"Distorted Smile",
"Cursed Power",
"Standing on the Frontlines",
"A Love That Never Fades",
"As the Heart Falls Silent",
"The Change the World Seeks",
"Defying Fate",
"Straight to My Beloved",
"Unnamed Memory ~Toward a New History~",
"Then, Let Us Fall in Love Again",
"The Great Magical Nation: Tuldarr",
"Blessing of Light",
"Yume Ato",
]

# Direktori tempat file berada
# r"..." digunakan di depan string untuk memastikan Python tidak memperlakukan backslash sebagai karakter escape saat membaca string asli.
# r untuk raw string, agar backslash tidak dianggap sebagai escape character
# f untuk f-string, agar bisa menggunakan variabel di dalam string
folder = "Unnamed Memory OST"
directory1 = rf"C:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\{folder}\flac"
# directory1 = rf"C:\Users\Nasrul Wahabi\Downloads\Music\{folder}\2"
# directory1 = r"C:\Users\Nasrul Wahabi\Downloads\Music\KNY Orchestra Concert S3\2"

directory = directory1.replace("\\", "\\\\")

# Fungsi untuk mengekstrak nomor urut dari nama file


def extract_number(filename):
    match = re.match(r'(\d+)', filename)
    return int(match.group(1)) if match else float('inf')

# Fungsi untuk membersihkan nama file dari karakter yang tidak diperbolehkan dengan pengganti karakter yang mirip

def sanitize_filename(filename):
    # Ganti setiap karakter yang tidak diperbolehkan dengan pengganti yang sesuai
    for invalid_char, replacement in inv_char.replacement.items():
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
