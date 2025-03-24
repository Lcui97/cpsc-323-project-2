from get_tokens import *
import table

def main():
    input = get_tokens("./test_cases/1.in")
    input.append("$")
    print(input)

    stack = [0]
    index = 0
    
    while True:
        current_state = stack[-1]
        current_token = input[index]

        action = table.table[current_state][table.valid_tokens.index(current_token)]
        print(action)
        break
        
    
        

if __name__ == "__main__":
    main()