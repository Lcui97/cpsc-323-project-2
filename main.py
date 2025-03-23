from get_input import *
import table

def main():
    input = get_input("./test_cases/10.in")

    stack = []
    word = ""
    while True:
        for char in input:
            word += char
            if word in table.terminals:
                stack.append(word)
                word = ""

                # now check the grammar

            else:
                continue

        

if __name__ == "__main__":
    main()