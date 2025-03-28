def formatter_title_index(list):
    for i in range(len(list)):
        print(f"\"{"{0:0=2d}".format(i+1)} --- {list[i]}\",")

def main():
    formatter_title_index([
"\"Hotel Tasokare\" Theme",
"Tasokare (TV size Ver.)",
"Wandering Reasoning",
"Waltz of Neko",
"Neko is Skipping.",
"Bouncing Night",
"Change Your Mood",
"Black Stone",
"The Guest is Come",
"Ethnic Corridor",
"Hotel Manager",
"Walk, Don't Run",
"Dialogue & Theme",
"To ho ho",
"Dash! Dash! Dash!",
"Tasokare Papillon Corridor (Game Ver.)",
"The Ogawa Strut",
"Fade",
"Day Dream",
"Day Dream (Piano Version)",
"From 'The Nutcracker' Suite Op.71a",
"Warmhearted Place",
"Illusion of Empty",
"Suspicious",
"Dark Skies",
"Pathetic",
"Anonymous Sign",
"An Outsider in the Hotel",
"Revolution",
"Composition of Confrontation",
"Evil Breath",
"Fatal Wound",
"Gateway",
"Twilight (TV Size Ver.)",
"Valse No.7 cis-moll Op.64-2",
"The Ogawa Strut (Atori Solo)"

    ])

if __name__ == "__main__":
    main()
