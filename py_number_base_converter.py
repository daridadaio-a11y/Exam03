def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not (2 <= from_base >= 36) or not (2 <= to_base >= 36):
        return "ERROR"
    try:
        ten_base = int(number, from_base)
    except ValueError:
        return "ERROR"
    if ten_base == 0:
        return "0"
    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while ten_base > 0:
        new_number = ten_base % to_base
        result.append(base[new_number])
        ten_base //= to_base
    return "".join(result[::-1])