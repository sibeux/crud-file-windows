def formatter_title_index(list):
    for i in range(len(list)):
        print(f"\"{"{0:0=2d}".format(i+1)} --- {list[i]}\",")


def main():
    formatter_title_index([
        "Medoree Hantengu, Ozomashii Sakebi / Zohakuten Toujou",
        "Medoree Rifujin e no Ikari / Zohakuten to no Mondou",
        "Haganezuka, Kyoui no Shuuchuuryoku",
        "Medoree Tokitou, Usureyuku Ishiki no Naka de / Kotetsu ni Semaru Kyoui / Kasumi no Kokyuu Ni no Kata Yaegasumi",
        "Medoree Ani to Futari Gurashi / Oni no Shuugeki ~ Hageshii Ikari / Yuichirou no Ikari ~ Mugen no Mu",
        "Medoree Kasumi no Kokyuu Go no Kata Kasumigumo no Umi / Gyokko to no Zessen ~ Gekitou / Kanzennaru Utsukushiki Sugata ~ Shi no Fuchi no Kaiko / Kasumi no Kokyuu Shichi no Kata Oboro / Gyokko no Saigo / Tokitou wo Tsutsumikomu Kazoku ~ Tokage to no Gekitou",
        "Medoree Tsukiyo ni Maioriru Kanroji / Watashi Okotteru kara! / Kanroji no Nichirintou / Kanroji tai Zohakuten",
        "Itsuwari no Watashi",
        "Medoree Minna Watashi ga Mamoru kara ne / Kanroji, Azekata no Hatsugen",
        "Onigui",
        "Hantengu to no Koubou ~ Tanjirou-tachi no Souryokusen",
        "Medoree Ningen no Hokyuu / Todokerareta Katana / Enbu Issen",
        "Kare wa Dare Toki・Asaborake",
        "Kamado Nezuko no Uta -full ver.-",
        "Medoree Kanki no Kibutsuji / Kibutsuji, Karada no Ihen",
        "Medoree Yokattaaaa ~ Tamayo no Tegami / Kansha no Miokuri",
        "Koikogare",
        "Kizuna no Kiseki",
        "Zankyou Sanka"

    ])


if __name__ == "__main__":
    main()
