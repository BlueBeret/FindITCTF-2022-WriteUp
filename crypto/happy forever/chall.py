# from secret import HAPPY_NUM, FLAG
# import base64

# reverse flag kemudian dijadiin hex
# FLAGenc = FLAG[::-1].encode().hex()

# m ^ happy_num+i
# ciphertext = [(ord(c)^(HAPPY_NUM[i]+i)) for i,c in enumerate(FLAGenc)]

# print(f"ciphertext = {ciphertext}")
ciphertext = [54, 108, 63, 41, 36, 37, 17, 31, 27, 12, 8, 118, 97, 101, 85, 3, 88, 9, 64, 64, 79, 186, 164, 160, 174, 149, 246, 249, 237, 189, 232, 131, 223, 146, 206, 305, 317, 291, 294, 286, 284, 374, 379, 358, 362, 367, 337, 270, 344, 328, 333, 332, 328, 439, 425, 405, 403, 400, 415, 469, 388, 399, 500, 500, 509, 424, 480, 488, 458, 608, 547, 553, 533, 512, 512, 515, 599, 588, 692, 738, 693, 640, 652, 675, 759, 763, 740, 736, 738, 750, 726, 732, 735, 724, 705, 714, 823, 876, 827, 800, 788, 796]

assert(len(ciphertext) %2 == 0)

FLAG = 'FindITCTF{'

x = FLAG[::-1].encode().hex()
c_ = ciphertext[-20::1]
for i,c in enumerate(x):
    print(ord(c)^c_[i] -i)