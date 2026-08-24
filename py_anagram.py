def anagram(s1: str, s2: str) -> bool:
    low_s1 = s1.lower()
    low_s2 = s2.lower()
    no_s1 = low_s1.replace(" ", "")
    no_s2 = low_s2.replace(" ", "")
    sort_s1 = sorted(no_s1)
    sort_s2 = sorted(no_s2)
    return sort_s1 == sort_s2