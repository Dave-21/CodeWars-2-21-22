def are_you_playing_banjo(name):
    if name[0].upper() == "R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print(are_you_playing_banjo("bick"))