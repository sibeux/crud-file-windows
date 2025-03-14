import os
import re

# Daftar nama file baru tanpa nomor urut dan waktu
new_names = [
    "Former Glory (Katsute no Eiga)",
    "Half-Belief, Half-Doubt (Hanshin Hangi)",
    "A Genius Thought (Tensaiteki Kousatsu)",
    "State of Emergency (Hijou Jitai)",
    "Conspiracies, Lies and Rumors (Inbou to Uso to Uwasa)",
    "Self-Centered (Hitoriyogari)",
    "Black Magic (Kuro Majutsu)",
    "Thistle and Marcille (Thistle to Marcille)",
    "Mad Magician (Kyouran no Majutsushi)",
    "In a Limited Amount of Time (Kagirareta Toki no Naka de)",
    "Hostility (Tekii)",
    "Confused Schemes (Konmeishita Sakubou)",
    "Weird Creature (Kimyou na Ikimono)",
    "The Truth That was Told (Tsugerareta Jitsujou)",
    "Concerns (Kigakari)",
    "Adventurers' Trust (Boukenshatachi no Shinrai)",
    "Nightmares (Nightmare)",
    "Weakness (Suijaku)",
    "Surprise Attack (Kishuu)",
    "A Dizzying Attack and Defense (Memagurushii Koubou)",
    "Canary Squad (Canary-tai)",
    "Monsters Dancing to Illusions (Gensou ni Odorasareshi Mamonotachi)",
    "Scattered in a Desperate Situation (Zettai Zetsumei no Sanji)",
    "The End of the Dungeon (Meikyuu no Gyoumatsu)",
    "Cruel Bargaining (Kokuhaku na Kakehiki)",
    "The Ultimate Deliciousness (Oishisa no Kiwami)",
    "Slapstick Struggle (Dotabata Funtou)",
    "Bright Dining Table (Akarui Shokutaku)",
    "Eastern Covert Unit (Touhou Onmitsu Butai)",
    "Chimera Falin (Chimera Falin)",
    "Ruthless World (Reikoku na Sekai)",
    "Gentle Conversation (Yasashiki Katarai)",
    "Resonance of the Heart (Kokoro no Kyoumei)",
    "Doubts of a Certain Past (Aru Kako no Ginen)",
    "Peaceful Village of Melini (Heiwa na Mura Merini)",
    "Upbringing (Oitachi)",
    "A Futile Argument (Munashiki Iiarasoi)",
    "Fleeting Life (Hakanai Seimei)",

]

# Direktori tempat file berada
# r"..." digunakan di depan string untuk memastikan Python tidak memperlakukan backslash sebagai karakter escape saat membaca string asli.
# r untuk raw string, agar backslash tidak dianggap sebagai escape character
# f untuk f-string, agar bisa menggunakan variabel di dalam string
folder = "Song Collection from The Rose of Versailles"
directory1 = rf"C:\Users\Nasrul Wahabi\Downloads\Music\{folder}\flac"
# directory1 = r"C:\Users\Nasrul Wahabi\Downloads\Music\Dungeon Meshi OST\Disc 2"

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
