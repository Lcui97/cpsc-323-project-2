from get_tokens import *
from data import *

def main():
    input = get_tokens("./test_cases/1.in")

    if not input:
        return

    input.append("$")
    print(input)

    stack = [0]
    index = 0

    print(f"Beginning Stack: {stack}")

    while True:
        current_state = stack[-1]
        current_token = input[index]
        print(f"Current token: {current_token}")

        action = table[current_state][table_column.index(current_token)]
        print(f"Action: {action}")

        if action.startswith('S'):
            state_to_shift = int(action[1:])
            stack.append(current_token)
            stack.append(state_to_shift)
            index += 1
            print(f"Shifted Stack: {stack}")

        elif action.startswith('R'):
            # Reduce. 
            break

        elif action == "Acc":
            # Accept. We output CST.
            break
            
        break # Remove this if necessary.
        
    
        

if __name__ == "__main__":
    main()