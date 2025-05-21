# generate palindrome code ai
def generate_index(n):
    for i in range(1, n+1):
        print(f"\"{"{0:0=2d}".format(i)}\"", end=",\n")


def main():
    generate_index(19)


if __name__ == "__main__":
    main()
