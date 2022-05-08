with open('./forensic/dingin/chall.txt', 'r') as f:
    raw = f.read()
    m = ""
    for i in raw:
        if (i == 'a'):
            m += "0"
        elif (i == 'b'):
            m += "1"
    print(m)
    for i in range(0, len(m), 8):
        print(chr(int(m[i:i+8], 2)), end='')
    print()
