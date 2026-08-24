def pattern_tracker(text: str) -> int:
    count = 0
    num = "0123456789"
    for i in range(len(text) - 1):
        pair = text[i] + text[i + 1]
        if pair in num:
            count += 1
    return count

if __name__ == "__main__":
    print(pattern_tracker("123"))
    print(pattern_tracker("12a34"))
    print(pattern_tracker("01234567"))
    print(pattern_tracker("abc"))
