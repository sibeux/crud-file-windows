def formatter_title_index(list):
    for i in range(len(list)):
        print(f"\"{"{0:0=2d}".format(i+1)} --- {list[i]}\",")

def main():
    formatter_title_index([
        "Zohakuten Appears",
        "Haganezuka, Incredible Concentration",
        "Tokito, In Fading Consciousness",
        "Yuichiro's Rage ~ 'Mu' Stands for 'Infinity'",
        "Mist Breathing Fifth Form: Sea of Clouds and Haze",
        "Verbal Battle with Gyokko ~ Fierce Fight",
        "Mist Breathing Seventh Form: Obscuring Clouds",
        "The Family That Embraces Tokito ~ Fierce Battle with the Snake-dragon",
        "Kanroji Swoops Down Upon a Moonlit Night",
        "Because I'm Angry!",
        "Kanroji vs. Zohakuten",
        "A Place Where I Can Be Me",
        "I'm Going to Protect You All",
        "Dancing Flash",
        "Daybreak and First Light",
        "Song of Nezuko Kamado -Full Ver.-",
        "Joyful Kibutsuji",
        "Thank Goodness ~ Tamayo's Letter",
        "A Thankful Farewell"

    ])

if __name__ == "__main__":
    main()
