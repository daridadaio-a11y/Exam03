# def inter(s1: str, s2: str) -> str:
#     new_str = ""
#     for char in s1:
#         for char_s2 in s2:
#             if char == char_s2:
#                 if not char in new_str:
#                     new_str += char
#     return new_str


def inter(s1: str, s2: str) -> str:
    clean = []
    for char in s1:
        if char in s2 and char not in clean:
            clean.append(char)
    return "".join(clean)

if __name__ == "__main__":
    print(inter("hello", "world"))
    print(inter("banana", "band"))
    print(inter("abcabc", "bc"))
    print(inter("abc", "xyz"))
    print(inter("", "abc"))