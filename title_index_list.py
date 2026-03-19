def formatter_title_index(list):
    for i in range(len(list)):
        print(f"\"{"{0:0=2d}".format(i+1)} --- {list[i]}\",")


def main():
    formatter_title_index([
     "Shakkotuenyou",
"Kyoui No Saiseisokudo Onika Nezuko",
"Koyama No Kousagi",
"Omoidashita Nezuko",
"Nakijyakuru Daki",
"Gyuutaraou No Shutsugen",
"Gyuutarou Sentou Kaishi",
"Hinatsuru No Kunai Kishikaisei No Itte",
"Uzui No Hakamairi",
"Daki Gekiha",
"Hinshi No Kisatsutai",
"Toubatumade Ato Ippo Hekirekiissen Shinsoku",
"Gyuutaou No Moukou Fumen No Kansei",
"Kecchaku Daki Gyuutarou Sen",
"Yukakuhoukai",
"Tatakai No Shuuen Nezuko No Honoo",
"Uzui No Gedoku",
"Nando Umarekawattemo",
"Daidanen",
"Zankyosanka -long intro version-"
    ])


if __name__ == "__main__":
    main()
