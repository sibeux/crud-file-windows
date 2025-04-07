def formatter_title_index(list):
    for i in range(len(list)):
        print(f"\"{"{0:0=2d}".format(i+1)} --- {list[i]}\",")

def main():
    formatter_title_index([
        "Kakushinteki☆Metamarufo~Ze!",
        "Sisters Wink",
        "Fever Natsu Vacation!",
        "Yuusha Umaru no Karei naru Seikatsu",
        "Beautiful Days",
        "sweet sweet everytime sweet",
        "Soida Bane",
        "My Precious",
        "Toto Fantasia",
        "T.S.F in Nippon!",
        "Shupatto No.1",
        "Dreamy Friends",
        "Fuwari Wata-ame Oishiku nare",
        "Happy Nightmare ~Imoutotachi no Kyouen~",
        "X'mas Decoration",
        "Hidamari Days",
        "Paradise☆Syndro~me!"

    ])

if __name__ == "__main__":
    main()
