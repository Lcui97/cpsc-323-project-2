def get_input(filename):
    with open(filename, "r") as file:
        value = file.read()
        
        # Remove all whitespace
        value = value.replace(" ", "").replace("\t", "").replace("\n", "")
        return value