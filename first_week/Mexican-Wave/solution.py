def wave(people):    
    wave_list = [people[:i] + people[i].upper() + people[i + 1:]
               for i in range(len(people)) if people[i] != ' ']
    return wave_list
