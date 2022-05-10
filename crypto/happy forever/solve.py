ct = [54, 108, 63, 41, 36, 37, 17, 31, 27, 12, 8, 118, 97, 101, 85, 3, 88, 9, 64, 64, 79, 186, 164, 160, 174, 149, 246, 249, 237, 189, 232, 131, 223, 146, 206, 305, 317, 291, 294, 286, 284, 374, 379, 358, 362, 367, 337, 270, 344, 328, 333, 332, 328, 439, 425, 405, 403, 400, 415, 469, 388, 399, 500, 500, 509, 424, 480, 488, 458, 608, 547, 553, 533, 512, 512, 515, 599, 588, 692, 738, 693, 640, 652, 675, 759, 763, 740, 736, 738, 750, 726, 732, 735, 724, 705, 714, 823, 876, 827, 800, 788, 796]
HAPPY_NUM = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446, 464, 469, 478, 487, 490, 496, 536, 556, 563, 565, 566, 608, 617, 622, 623, 632, 635, 637, 638, 644, 649, 653, 655, 656, 665, 671, 673, 680, 683, 694, 700, 709, 716, 736, 739, 748, 761, 763, 784, 790, 793, 802, 806, 818, 820, 833, 836, 847, 860, 863, 874, 881, 888, 899, 901, 904, 907, 910, 912, 913, 921, 923, 931, 932, 937, 940, 946, 964, 970, 973, 989, 998, 1000]

assert(len(ct) %2 == 0)

pt_hex = ''

for i,c in enumerate(ct):
    pt_hex += chr(c^(HAPPY_NUM[i]+i))

print(bytes.fromhex(pt_hex).decode()[::-1])
