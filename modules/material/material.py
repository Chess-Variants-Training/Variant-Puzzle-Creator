def piece_values(variant):
    if variant == "Atomic":
        return [3.32, 4.78, 6.14, 9.57, 19.04]
    elif variant == "Horde":
        return [3.70, 7.08, 7.36, 13.41, 27.77]
    elif variant == "Racing Kings":
        return [0, 7.20, 9.04, 12.65, 21.98]
    elif variant == "Three-check":
        return [1.81, 6.91, 8.29, 12.22, 22.74]
    elif variant == "King of the Hill":
        return [1, 3, 3, 5, 9]
    elif variant == "Antichess":
        return [-137, -130, -322, -496, -187]
    else:
        return None
