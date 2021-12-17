def timeConversion(s):
    split = s.split(':')
    print(split)
    if "AM" in split[2]:
        time = int(split[0]) + 12

    if time == 24:
        time = 00

    new_time = split[1:] + time




s = "07:05:45PM"
timeConversion(s)