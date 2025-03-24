import table

# Gets input string and converts it into an array of tokens
def get_tokens(filename):
    with open(filename, "r") as file:
        input = file.read()
        input = input.replace(" ", "").replace("\t", "").replace("\n", "")
        
        tokens = []
        current_token = ""

        for char in input:
            if char in table.valid_tokens:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(char)
            else:
                current_token += char

        if current_token:
            tokens.append(current_token)

        return tokens