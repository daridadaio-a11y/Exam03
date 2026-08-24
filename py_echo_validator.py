# def echo_validator(text: str) -> bool:
#     clean = [char.lower() for char in text if char.isalpha()]
#     if not clean:
#         return False
#     return clean == clean[::-1]



def echo_validator(text: str) -> bool:
    clean = ""
    for char in text:
        if char.isalpha():
            clean += char.lower()
    if not clean:
        return False
    return clean == clean[::-1]