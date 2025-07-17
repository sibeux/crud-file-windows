def formatter_title_index(list):
    for i in range(len(list)):
        print(f"\"{"{0:0=2d}".format(i+1)} --- {list[i]}\",")


def main():
    formatter_title_index([
     "Will He Shoemaker?",
"Shrine and Dash",
"Miguel's Got an Axe to Find",
"The Strum of Destiny",
"It's All Relative",
"Crossing the Marigold Bridge",
"Dept. of Family Reunions",
"The Skeleton Key to Escape",
"The Newbie Skeleton Walk",
"Adiós Chicharrón",
"Plaza de la Cruz",
"Family Doubtings",
"Taking Sides",
"Fiesta Espectacular",
"Fiesta con de la Cruz",
"I Have a Great-Great-Grandson",
"A Blessing and a Fessing",
"Somos Familia",
"Reunión Familiar de Rivera",
"A Family Dysfunction",
"Grabbing a Photo Opportunity",
"For Whom the Bell Tolls",
"One Year Later",
"Coco - Día de los Muertos Suite"
    ])


if __name__ == "__main__":
    main()
