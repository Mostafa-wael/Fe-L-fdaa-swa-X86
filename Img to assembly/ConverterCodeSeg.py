from PIL import Image
filename = 'Msgtail.png'
im = Image.open(filename)
width, height = im.size
pixels = list(im.getdata())
px = pixels
if '.png' in filename:
    px = []
    for elm in pixels:
        px.append(elm[:-1])
C = []

# Used pallete: https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/VGA_palette_with_black_borders.svg/1200px-VGA_palette_with_black_borders.svg.png
# This pallete is the default 256 colors in the Tasm/Masm Extension for VS code, Note that the original asm86 only supported the first 16 colors
# So make sure while drawing your art to pick (via color picker) from this palette, btw: Krita(~30mb) is a great and easy app for creating pixel art:
# How to set up Krita for pixel art(5 mins): https://www.youtube.com/watch?v=aaRzNTCanIQ
# Nice Pixel art tutorials playlist (each video is 5~15 mins): https://www.youtube.com/playlist?list=PLmac3HPrav-9UWt-ahViIZxpyQxJ2wPSH

    # It is okay tho to use black(0) as escaping since there are other codes for the same color like 16, 248..255.
    # if it is .png with some pixels having 0 in alpha channel (making them tranparent: use black(0) as escaping color)
D = {

    (0, 0, 170): 1,
    (0, 170, 0): 2,
    (0, 170, 170): 3,
    (170, 0, 0): 4,
    (170, 0, 170): 5,
    (170, 85, 0): 6,
    (170, 170, 170): 7,
    (85, 85, 85): 8,
    (85, 85, 255): 9,
    (85, 255, 85): 10,
    (85, 255, 255): 11,
    (255, 85, 85): 12,
    (255, 85, 255): 13,
    (255, 255, 85): 14,
    (255, 255, 255): 15,
    (0, 0, 0): 16,
    (16, 16, 16): 17,
    (32, 32, 32): 18,
    (53, 53, 53): 19,
    (69, 69, 69): 20,
    (85, 85, 85): 21,
    (101, 101, 101): 22,
    (117, 117, 117): 23,
    (138, 138, 138): 24,
    (154, 154, 154): 25,
    (170, 170, 170): 26,
    (186, 186, 186): 27,
    (202, 202, 202): 28,
    (223, 223, 223): 29,
    (239, 239, 239): 30,
    (255, 255, 255): 31,
    (0, 0, 255): 32,
    (65, 0, 255): 33,
    (130, 0, 255): 34,
    (190, 0, 255): 35,
    (255, 0, 255): 36,
    (255, 0, 190): 37,
    (255, 0, 130): 38,
    (255, 0, 65): 39,
    (255, 0, 0): 40,
    (255, 65, 0): 41,
    (255, 130, 0): 42,
    (255, 190, 0): 43,
    (255, 255, 0): 44,
    (190, 255, 0): 45,
    (130, 255, 0): 46,
    (65, 255, 0): 47,
    (0, 255, 0): 48,
    (0, 255, 65): 49,
    (0, 255, 130): 50,
    (0, 255, 190): 51,
    (0, 255, 255): 52,
    (0, 190, 255): 53,
    (0, 130, 255): 54,
    (0, 65, 255): 55,
    (130, 130, 255): 56,
    (158, 130, 255): 57,
    (190, 130, 255): 58,
    (223, 130, 255): 59,
    (255, 130, 255): 60,
    (255, 130, 223): 61,
    (255, 130, 190): 62,
    (255, 130, 158): 63,
    (255, 130, 130): 64,
    (255, 158, 130): 65,
    (255, 190, 130): 66,
    (255, 223, 130): 67,
    (255, 255, 130): 68,
    (223, 255, 130): 69,
    (190, 255, 130): 70,
    (158, 255, 130): 71,
    (130, 255, 130): 72,
    (130, 255, 158): 73,
    (130, 255, 190): 74,
    (130, 255, 223): 75,
    (130, 255, 255): 76,
    (130, 223, 255): 77,
    (130, 190, 255): 78,
    (130, 158, 255): 79,
    (186, 186, 255): 80,
    (202, 186, 255): 81,
    (223, 186, 255): 82,
    (239, 186, 255): 83,
    (255, 186, 255): 84,
    (255, 186, 239): 85,
    (255, 186, 223): 86,
    (255, 186, 202): 87,
    (255, 186, 186): 88,
    (255, 202, 186): 89,
    (255, 223, 186): 90,
    (255, 239, 186): 91,
    (255, 255, 186): 92,
    (239, 255, 186): 93,
    (223, 255, 186): 94,
    (202, 255, 186): 95,
    (186, 255, 186): 96,
    (186, 255, 202): 97,
    (186, 255, 223): 98,
    (186, 255, 239): 99,
    (186, 255, 255): 100,
    (186, 239, 255): 101,
    (186, 223, 255): 102,
    (186, 202, 255): 103,
    (0, 0, 113): 104,
    (28, 0, 113): 105,
    (57, 0, 113): 106,
    (85, 0, 113): 107,
    (113, 0, 113): 108,
    (113, 0, 85): 109,
    (113, 0, 57): 110,
    (113, 0, 28): 111,
    (113, 0, 0): 112,
    (113, 28, 0): 113,
    (113, 57, 0): 114,
    (113, 85, 0): 115,
    (113, 113, 0): 116,
    (85, 113, 0): 117,
    (57, 113, 0): 118,
    (28, 113, 0): 119,
    (0, 113, 0): 120,
    (0, 113, 28): 121,
    (0, 113, 57): 122,
    (0, 113, 85): 123,
    (0, 113, 113): 124,
    (0, 85, 113): 125,
    (0, 57, 113): 126,
    (0, 28, 113): 127,
    (57, 57, 113): 128,
    (69, 57, 113): 129,
    (85, 57, 113): 130,
    (97, 57, 113): 131,
    (113, 57, 113): 132,
    (113, 57, 97): 133,
    (113, 57, 85): 134,
    (113, 57, 69): 135,
    (113, 57, 57): 136,
    (113, 69, 57): 137,
    (113, 85, 57): 138,
    (113, 97, 57): 139,
    (113, 113, 57): 140,
    (97, 113, 57): 141,
    (85, 113, 57): 142,
    (69, 113, 57): 143,
    (57, 113, 57): 144,
    (57, 113, 69): 145,
    (57, 113, 85): 146,
    (57, 113, 97): 147,
    (57, 113, 113): 148,
    (57, 97, 113): 149,
    (57, 85, 113): 150,
    (57, 69, 113): 151,
    (81, 81, 113): 152,
    (89, 81, 113): 153,
    (97, 81, 113): 154,
    (105, 81, 113): 155,
    (113, 81, 113): 156,
    (113, 81, 105): 157,
    (113, 81, 97): 158,
    (113, 81, 89): 159,
    (113, 81, 81): 160,
    (113, 89, 81): 161,
    (113, 97, 81): 162,
    (113, 105, 81): 163,
    (113, 113, 81): 164,
    (105, 113, 81): 165,
    (97, 113, 81): 166,
    (89, 113, 81): 167,
    (81, 113, 81): 168,
    (81, 113, 89): 169,
    (81, 113, 97): 170,
    (81, 113, 105): 171,
    (81, 113, 113): 172,
    (81, 105, 113): 173,
    (81, 97, 113): 174,
    (81, 89, 113): 175,
    (0, 0, 65): 176,
    (16, 0, 65): 177,
    (32, 0, 65): 178,
    (49, 0, 65): 179,
    (65, 0, 65): 180,
    (65, 0, 49): 181,
    (65, 0, 32): 182,
    (65, 0, 16): 183,
    (65, 0, 0): 184,
    (65, 16, 0): 185,
    (65, 32, 0): 186,
    (65, 49, 0): 187,
    (65, 65, 0): 188,
    (49, 65, 0): 189,
    (32, 65, 0): 190,
    (16, 65, 0): 191,
    (0, 65, 0): 192,
    (0, 65, 16): 193,
    (0, 65, 32): 194,
    (0, 65, 49): 195,
    (0, 65, 65): 196,
    (0, 49, 65): 197,
    (0, 32, 65): 198,
    (0, 16, 65): 199,
    (32, 32, 65): 200,
    (40, 32, 65): 201,
    (49, 32, 65): 202,
    (57, 32, 65): 203,
    (65, 32, 65): 204,
    (65, 32, 57): 205,
    (65, 32, 49): 206,
    (65, 32, 40): 207,
    (65, 32, 32): 208,
    (65, 40, 32): 209,
    (65, 49, 32): 210,
    (65, 57, 32): 211,
    (65, 65, 32): 212,
    (57, 65, 32): 213,
    (49, 65, 32): 214,
    (40, 65, 32): 215,
    (32, 65, 32): 216,
    (32, 65, 40): 217,
    (32, 65, 49): 218,
    (32, 65, 57): 219,
    (32, 65, 65): 220,
    (32, 57, 65): 221,
    (32, 49, 65): 222,
    (32, 40, 65): 223,
    (45, 45, 65): 224,
    (49, 45, 65): 225,
    (53, 45, 65): 226,
    (61, 45, 65): 227,
    (65, 45, 65): 228,
    (65, 45, 61): 229,
    (65, 45, 53): 230,
    (65, 45, 49): 231,
    (65, 45, 45): 232,
    (65, 49, 45): 233,
    (65, 53, 45): 234,
    (65, 61, 45): 235,
    (65, 65, 45): 236,
    (61, 65, 45): 237,
    (53, 65, 45): 238,
    (49, 65, 45): 239,
    (45, 65, 45): 240,
    (45, 65, 49): 241,
    (45, 65, 53): 242,
    (45, 65, 61): 243,
    (45, 65, 65): 244,
    (45, 61, 65): 245,
    (45, 53, 65): 246,
    (45, 49, 65): 247
}

for c,i in enumerate(px):
    if '.png' in filename and pixels[c][3] == 0:
        C.append(0)
    elif i in D.keys():
        C.append(D[i])
    else:
        MIN = (255, 255, 255)
        MINK = (255, 255, 255)
        for k in D.keys():
            if abs(k[0] - i[0]) + abs(k[1] - i[1]) + abs(k[2] - i[2]) < MIN[0] + MIN[1] + MIN[2]:
                MIN = (abs(k[0] - i[0]), abs(k[1] - i[1]), abs(k[2] - i[2]))
                MINK = k
        C.append(D[MINK])


#print(px)

# Reverse array if -in assembly- you are drawing from width & height down to 0 & 0 (reversed iteration)
# else remove the line below
C = [str(ele) for ele in reversed(C)]


StrC = "img DB "

# Split the array into multiple lines cause it will be too long for one line for the tasm/masm.
for i in range(len(C)):
    if i % 40 == 39:
        StrC = StrC + str(C[i]) + " " + "\n DB "
    else:
        StrC = StrC + str(C[i]) + ", "

StrC = StrC[:-2]
output = open("ImageResult.txt", "a")
output.write(StrC)
output.close()
print("imgW equ", width)
print("imgH equ", height)
print(StrC)