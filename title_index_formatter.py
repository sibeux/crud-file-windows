def formatter_title_index(list):
    for i in range(len(list)):
        print(f"\"{"{0:0=2d}".format(i+1)} --- {list[i]}\",")

def main():
    formatter_title_index([
        "Metro Boomin, John Legend",
        "Metro Boomin, Future, Chris Brown",
        "Metro Boomin, Future, Don Toliver",
        "Metro Boomin, Travis Scott",
        "Metro Boomin, 21 Savage, Young Nudy",
        "Metro Boomin, Travis Scott, Young Thug",
        "Metro Boomin, Don Toliver",
        "Metro Boomin, Young Thug",
        "Metro Boomin, Future, Don Toliver",
        "Metro Boomin, The Weeknd, 21 Savage",
        "Metro Boomin, Travis Scott, 21 Savage",
        "Metro Boomin, 21 Savage, Mustafa",
        "Metro Boomin, Travis Scott, Future",
        "Metro Boomin, A$AP Rocky, Takeoff",
        "Metro Boomin, Gunna"

    ])

if __name__ == "__main__":
    main()
