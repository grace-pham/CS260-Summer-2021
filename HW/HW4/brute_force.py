import time

import bcrypt


def brute_force(alphabet_list, digest):
    count = 0
    for x in alphabet_list:
        for y in alphabet_list:
            passwd = f'{x}{y}'.encode()
            count += 1
            if bcrypt.checkpw(passwd, digest):
                return (passwd, count)
            else:
                continue


if __name__ == "__main__":
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    user_info_list = [("ntp33", b"$2b$12$aGViT/W21sbGrZY42BvaYezRizJBPWxjDsBBJtGbI0RJ8ngVX7TsS"),
                      ("kms677", b"$2b$12$KxAkoCk/NuTrL47MiGbFb.KJ5fe6z9qYd12GRdbdIrg2J9jkaVnaK"),
                      ("bmh324", b"$2b$12$BNDMm8akBdlvUDx9jZUri.aD04xCokRfLlxbnHU7VNr8fBpHeUdDy"),]
    for user_info in user_info_list:
        start = time.time()
        result = brute_force(alphabet_list, user_info[1])
        end = time.time()
        passwd = result[0].decode()
        guesses = result[1]
        print("---------------------")
        print("Student ID:", user_info[0])
        print("Password:", passwd)
        print("Number of guesses:", guesses)
        print("Time taken to hack:", end - start)
