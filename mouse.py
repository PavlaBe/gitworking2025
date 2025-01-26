
def print_ascii_cat():
    import pdb
    pdb.set_trace()
    with open("mouse.txt") as f:
        for line in f.readlines():
            print(line)

def main():
    print_ascii_cat()

main()
