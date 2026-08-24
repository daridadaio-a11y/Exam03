def hidenp(small: str, big: str) -> bool:
    i = 0
    if not small:
        return True
    for char in big:
        if small[i] == char:
            i += 1
            if i == len(small):
                return True
    return False