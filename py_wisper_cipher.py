def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            code = (ord(char) - base + shift) % 26 + base
            result += chr(code)
        else:
            result += char
    return result