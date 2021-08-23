import time

import bcrypt


def find_passwd(alphabet_list, digest):
    count = 0
    for x in alphabet_list:
        for y in alphabet_list:
            passwd = f'{x}{y}'.encode()
            count += 1
            if bcrypt.checkpw(passwd, digest):
                return (passwd, count)
            else:
                print("wrong pw:", passwd)
                continue


def count_combination1():
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']

    result = []
    for x in alphabet_list:
        for y in alphabet_list:
            result.append(f'{x}{y}'.encode())

    return result


def count_combination2():
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']

    result = []
    for x in alphabet_list:
        for y in alphabet_list:
            for z in alphabet_list:
                result.append(f'{x}{y}{z}'.encode())

    return result



if __name__ == "__main__":
    result1 = count_combination1()
    result2 = count_combination2()

    print("1:", len(result1))
    print("2:", len(result2))



    # alphabet_list = ['p', 'a']
    # user_info_list = [("ntp33", b"$2b$12$aGViT/W21sbGrZY42BvaYezRizJBPWxjDsBBJtGbI0RJ8ngVX7TsS")]
    # for user_info in user_info_list:
    #     start = time.time()
    #     result = find_passwd(alphabet_list, user_info[1])
    #     passwd = result[0].decode()
    #     guesses = result[1]
    #     end = time.time()
    #     print("---------------------")
    #     print("plssss:", end - start)
    #     print("user:", user_info[0])
    #     print("passwd:", passwd)
    #     print("guesses:", guesses)
    #     print("---------------------")
