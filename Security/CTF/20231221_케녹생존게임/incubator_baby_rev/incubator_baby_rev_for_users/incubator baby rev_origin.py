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

def random_shuffle(flag,seed) :
    random.seed(seed)
    rand = random.randint(70,90)
    print(rand)
    for _ in range(rand):
        random.seed(seed)
        random.shuffle(flag)

    return flag
        

if __name__ == "__main__" :
    # print("[+] yeonwoo is shuffling flag ^-^")
    # flag = make_fake_flag()
    # flag = reaplce_2_real_flag(flag)

    # with open("real_flag.txt","w") as f :
    #     f.write(''.join(flag))
    #     f.close()

    # flag = random_shuffle(flag,31208)

    test=[a for a in range(1024)]
    test = random_shuffle(test,31208)
    print(test)

    with open("shuffled_flag.txt","w") as f :
        f.writelines(flag)
        f.close()

    print("[+] done! can you find the real flag? ^-^")