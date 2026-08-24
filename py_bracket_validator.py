# def bracket_validator(s: str) -> bool:
#     dict = {")": "(", "]": "[", "}": "{"}
#     check = []
#     for char in s:
#         if char in dict.values():
#             check.append(char)
#         elif char in dict.keys():
#             if not check or check.pop() != dict[char]:
#                 return False
#     return not check

def bracket_validator(s: str) -> bool:
    dict = {")": "(", "]": "[", "}": "{"}
    new_list = []
    for char in s:
        if char in dict.values():
            new_list.append(char)
        elif char in dict.keys():
            if not new_list or new_list.pop() != dict[char]:
                return False
    return not new_list



if __name__ == "__main__":
    print(bracket_validator("()"))
    print(bracket_validator("()[]{}"))
    print(bracket_validator("(]"))
    print(bracket_validator("([)]"))
    print(bracket_validator("{[]}"))
    print(bracket_validator("hello(world)"))
    print(bracket_validator("(((()))"))
    print(bracket_validator(""))