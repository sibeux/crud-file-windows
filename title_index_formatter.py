def formatter_title_index(list):
    for i in range(len(list)):
        print(f"\"{"{0:0=2d}".format(i+1)} --- {list[i]}\",")


def main():
    formatter_title_index([
     "BLADE",
"GET BACK",
"BLADE -Fate version-(TV size)",
"BLADE -Bond version-(TV size)"
    ])


if __name__ == "__main__":
    main()
