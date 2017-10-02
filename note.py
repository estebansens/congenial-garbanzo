import winsound

print("Binary Representation of sound")

print("Enter the duration of each note (in ms)?")
print("e.g. 200")
rate = int(input(">"))

print("Enter a 5-bit binary note")
print("Or more than one note separated by spaces")

print("Notes:")
print("00000 = no sound")
print("00001 = Low C")
print("00010 = D")
print("00011 = E")
print("00100 = F")
print("00101 = G")
print("00110 = A")
print("00111 = B")
print("01000 = High C")
print("10000 = C Sharp")
print("10001 = D Sharp")
print("10010 = E Sharp")
print("10011 = F Sharp")
print("10100 = G Sharp")

print("e.g: ")
print("00101 00101 00101 00010 00011 00011 00010 00000 00111 00111 00110 00110 00101")
soundBinary = input(">")

for note in soundBinary.split():

    if note == "00000":          #rest
        freq = 37
    elif note == "00001":        #low c
        freq = 262
    elif note == "00010":        #d
        freq = 294
    elif note == "00011":        #e
        freq = 330
    elif note == "00100":        #f
        freq = 349
    elif note == "00101":        #g
        freq = 392
    elif note == "00110":        #a
        freq = 440
    elif note == "00111":        #b
        freq = 494
    elif note == "01000":        #high c
        freq = 523
    elif note == "10001":        #c sharp
        freq = 277
    elif note == "10010":        #d sharp
        freq = 311
    elif note == "10011":        # f sharp
        freq = 370
    elif note == "10100":        #g sharp
        freq = 415
    winsound.Beep(freq, rate)
