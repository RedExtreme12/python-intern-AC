def find_short(s):
    l = len((sorted(s.split(' '), key=len))[0])
    
    return l