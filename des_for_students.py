LB32_MASK = 0x00000001
LB64_MASK = 0x0000000000000001
L64_MASK = 0x00000000ffffffff
H64_MASK = 0xffffffff00000000

# Initial Permutation Table
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Inverse Initial Permutation Table
PI = [
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
]

# Expansion table
E = [
    32,  1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# Post P-Box permutation
P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

# The S-Box tables
S = [
    # S1
    [
        14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
    ],
    # S2
    [
        15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
    ],
    # S3
    [
        10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
    ],
    # S4
    [
        7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
    ],
    # S5
    [
        2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
    ],
    # S6
    [
        12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
    ],
    # S7
    [
        4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
    ],
    # S8
    [
        13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
    ]
]

# Permuted Choice 1 Table
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# Permuted Choice 2 Table
PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Iteration Shift Array
iteration_shift = [
    # 1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
    1,  1,  2,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  2,  1
]


# Initial permutation
#输入为 16 进制数， 输出为 10 进制数
def initial_permutaion(block):
    init_perm_res = 0
    # TODO
    intblock = int(block)
    for i in range(len(IP)):
        iblock = (intblock >> (len(IP)-IP[i])) & LB64_MASK
        init_perm_res += iblock << (len(IP) - i - 1)
    init_perm_res = int(init_perm_res)
    return init_perm_res

# key schedule function
# 输入为 16 进制数， 输出为 10 进制数组成的列表
def key_schedule(key):
    Round_key = [0] * 16
    # TODO 
    key = int(key)
    ckey = 0
    for i in range(len(PC1)):
        ikey = (key >> (64 - PC1[i])) & 0x1
        ckey += ikey << (len(PC1) - i - 1) & 0xffffffffffffff
    
    keyl = (ckey >> 28) & 0xfffffff
    keyr = ckey & 0xfffffff
    for n in range(16):
        for i in range(iteration_shift[n]):
            keyl = ((keyl << 1) | (keyl >> 27)) & 0xFFFFFFF
            keyr = ((keyr << 1) | (keyr >> 27)) & 0xFFFFFFF
        nkey = 0
        nkeybits = ((keyl << 28) | keyr) & 0xffffffffffffff
        for i in range(len(PC2)):
            inkey = (nkeybits >> (56 - PC2[i])) & 0x1
            nkey += (inkey << (len(PC2) - i - 1)) & 0xffffffffffffff
        Round_key[n] = nkey
    
    return Round_key


def f(R0, K, roundn):
    f_function_res = 0
    # TODO
    R = R0 & L64_MASK
    L = ((R0 & H64_MASK) >> 32) & L64_MASK
    # expansion P-box
    Rbits = R
    for i in range(len(E)):
        ibits = (Rbits >> (32 - E[i])) & LB32_MASK
        f_function_res += ibits << (47 - i) & 0xffffffffffff
    # XOR K
    f_function_res = (f_function_res ^ K)
    # S BOX
    s = f_function_res & 0xffffffffffff
    f_function_res = 0
    f_mask = 0x3f
    for i in range(8):
        fcache = (s >> 6*(7 - i)) & f_mask
        j = int((fcache & 0x20) >> 5) * 2 + int(fcache & 0x01)
        k = int((fcache & 0x1e) >> 1) & 0x0f
        f_function_res += S[i][16 * j + k]  << ((7 - i)* 4) & 0xffffffff
    # straight P BOX
    fbits = int(f_function_res)
    f_function_res = 0
    for i in range(len(P)):
        ibits = fbits >> (32 - P[i]) & LB32_MASK
        f_function_res += ibits << (len(P) - i - 1)
    # Mixer
    R_out = (L ^ f_function_res) & 0xffffffff
    L_out = R
    if roundn == 15:
        R_out, L_out = L_out, R_out
    return (L_out << 32) | R_out & 0xFFFFFFFFFFFFFFFF

def inverse_initial_permutation(block):
    # Inverse initial permutation
    inv_init_perm_res = 0
    # TODO
    for i in range(len(PI)):
        iblock = (block >> (len(PI) - PI[i])) & LB64_MASK
        inv_init_perm_res += iblock << (len(PI) - i - 1)
    inv_init_perm_res = hex(inv_init_perm_res)
    return inv_init_perm_res

# Des Encryption
def des_encrypt(plain, key):
    # TODO
    
    # round key generation
    Round_key = key_schedule(key)
    # Initial permutation
    init_perm_res = initial_permutaion(plain)
    # 16 ROUND Feistel
    R = init_perm_res
    for i in range(16):
        R = f(R, Round_key[i], i)
    # inverse_initial_permutation
    inv_init_perm_res = inverse_initial_permutation(R)
    return inv_init_perm_res

# Des Decryption
def des_decrypt(plain, key):
    # TODO
    
    # round key generation
    Round_key = key_schedule(key)
    
    Round_key.reverse()
    # Initial permutation
    plain = int(plain, 16)
    init_perm_res = initial_permutaion(plain)
    # 16 ROUND Feistel
    R = init_perm_res
    for i in range(16):
        R = f(R, Round_key[i], i)
    # inverse_initial_permutation
    inv_init_perm_res = inverse_initial_permutation(R)
    return inv_init_perm_res


def test1():
    plain = 0x0123456789ABCDEF
    key   = 0xFEDCBA9876543210
      
    cipher = des_encrypt(plain, key)
    print(f"Encrypted: {cipher:016}")

    decrypted = des_decrypt(cipher, key)
    print(f'Decrypted: {decrypted:016}')

def test2():
    plain = 0x0123456789ABCDEF
    key   = 0x1111111111111111
  
    cipher = des_encrypt(plain, key)
    print(f"Encrypted: {cipher:016}")

    decrypted = des_decrypt(cipher, key)
    print(f'Decrypted: {decrypted:016}')

if __name__ != '__main__':
    test1()
    test2()

print(hex(0x56082007 ^ 0x04000000 ^ 0x80682de0))