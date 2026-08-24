# def cryptic_sorter(strings: list[str]) -> list[str]:
#     def sort_key(s):
#         return (len(s), s.lower(), sum(1 for char in s if char.lower() in "aeiou"))
#     result = strings[:]
#     for i in range(len(result)):
#         for j in range(len(result) - i - 1):
#             if sort_key(result[j]) > sort_key(result[j + 1]):
#                 result[j], result[j + 1] = result[j + 1], result[j]
#     return result


def cryptic_sorter(strings: list[str]) -> list[str]:
    def sort_key2(s):
        counter = 0
        for char in s:
            if char.lower() in "aeiou":
                counter += 1
        return (len(s), s.lower(), counter)
    result = strings[:]
    for i in range(len(result)):
        for j in range(len(result) - i - 1):
            if sort_key2(result[j]) > sort_key2(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

if __name__ == "__main__":
    print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
