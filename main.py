from get_input import *
import table

def main():
    input = get_input("./test_cases/1.in")
    input += "$" # Example: (id+id)/id$

    stack = [0] # Initial state is 0
    word = ""
    index = 0

    while index < len(input):
        current_char = input[index]
        word += current_char

        if word in table.terminals:
            return
        else:
            index += 1
        

if __name__ == "__main__":
    main()