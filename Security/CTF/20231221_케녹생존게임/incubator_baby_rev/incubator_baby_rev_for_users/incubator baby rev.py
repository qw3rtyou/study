import random

def make_fake_flag() :
    flag = "KCTF{"
    flag += "X" * (1024 - 6)
    flag += "}"
    return flag

def reaplce_2_real_flag(flag):
    list_flag = [a for a in flag]
    flag = list_flag
    for i in range(len(flag)):
        if flag[i] == "X":
            flag[i] = hex(random.randint(0,15))[2:]
    return flag

def random_shuffle(flag) :
    random.seed(31208)
    for _ in range(75):
        random.shuffle(flag)

    return "".join(flag)

def random_unshuffle(shuffled_flag):
    random.seed(31208)
    actions = []
    
    # shuffle의 반대 과정을 구현하기 위해, 섞는 과정을 actions 리스트에 저장
    for _ in range(75):
        i, j = random.sample(range(len(shuffled_flag)), 2)
        actions.append((i, j))

    print("inside2")
    # actions 리스트에 저장한 섞는 과정을 역순으로 수행해서 unshuffle
    for i, j in reversed(actions):
        shuffled_flag[i], shuffled_flag[j] = shuffled_flag[j], shuffled_flag[i]
    print(shuffled_flag)


    return "".join(shuffled_flag)

if __name__ == "__main__" :
    # flag = make_fake_flag()
    # flag = reaplce_2_real_flag(flag)

    flag="KCTF{c17483b16861db889da1bccbdb9132ced5132ee254f29c0c7867c192cbc2fd6a398ec30526b4c1574bb1fca347e9b70993cfc3206397abdc8cfcb656a42186e6929a7edb26ea949f7ea275939308e9f251d1be70b67f0627bbc80689f986b449f3e8f26edc66f341f4bf5a14f1f0b88ebf03a0aaf2c73fc2a5b97e74644192e23718cb46fd24b703c0f1f9c72a41f3013b7f253d7687fc582be8d7ceabc9e55727536d9cfc64e8c7c9ade97c7ecc6f051a26bbd20dccc24f00657ed1a860721ae003260d578a1d19a949a273cfe63a6ca7d19d53e72a5e8b484e4f2d8dd42e38d14c9bcbafaa4f769eeec4c2db038f04f0690fffe30c9d2a8d26008f701ee9a020500dc2356ee0cd2d58231e6c3fa484dd739d7b226f4664919129b3578a3bc976d0d2413eb545a1b9ecdb4e67a718cd839b06dd03a388bdc53c83a7f7100cf8c838ec067ba9022113bdd82966fa4788b25ba61fd5e28b848cd42f96614d23b12682ec35c1d7ec0452ee2798737ae9dfa8cedeb64b2d38dda379be23cd20e21c0d0fc7468e03f7923501b80918e92ad2aa06b06a22b0cd27fa27179ccad449e69aee99c451792a5e2068a10155a5b36d7886c169116d3a47cbf0b54548e25633a273f779cc13968cbb09f54b0c81592423cedb6e953b7eb7534c9623dede369fb4276c0db3c4456dac83cb3ddd873779eb1d2f687e80c6b69427bf6b90}"
    print(flag)


    flag = [a for a in flag]
    flag = random_shuffle(flag)
    print(flag)




    flag = [a for a in flag]
    flag = random_unshuffle(flag)
    print(flag)