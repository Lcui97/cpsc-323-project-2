import data

# Gets input string and converts it into an array of tokens
def get_tokens(filename):
    with open(filename, "r") as file:
        input = file.read()
        input = input.replace(" ", "").replace("\t", "").replace("\n", "")
        
        tokens = []
        current_token = ""

        for char in input:
            current_token += char
            if current_token in data.valid_tokens:
                tokens.append(current_token)
                current_token = ""

        return tokens