def humor(a, b, c):
    if (a - b > 0) and (b - c <= 0):
        return(":)")
    elif (a - b < 0) and (b - c < 0) and (c - b >= b - a):
        return(":)")
    elif (a - b > 0) and (b - c > 0) and (c - b < b - a):
        return(":)")
    elif (a == b) and (b - c < 0):
        return(":)")
    else:
        return(":(")