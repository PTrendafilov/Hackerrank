s = input()
midday = s[len(s) - 2:len(s)]
s = s[0:len(s) - 2]
s=s.split(':')
h = int(s[0])
m = s[1]
s = s[2]
if h < 12 and midday == "PM":
    h += 12
if h >= 12 and midday == "AM":
    h -= 12
if h<10:
    print(f'0{h}:{m}:{s}')
else:
    print(f'{h}:{m}:{s}')
