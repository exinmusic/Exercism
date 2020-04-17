def is_isogram(string):
    used = []
    for char in string.upper().replace(" ","").replace("-",""):
        if char in used:
            return False
        else:
            used.append(char)
    return True