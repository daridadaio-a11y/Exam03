def string_sculptor(text: str) -> str:
    count = 0
    new_str = []
    for char in text:
        if char.isalpha():
            if count % 2 == 0:
                char = char.lower()
                new_str.append(char)
            else:
                char = char.upper()
                new_str.append(char)
            count += 1
        elif char == " ":
            count = 0
            new_str.append(char)
        else:
            new_str.append(char)
    return "".join(new_str)