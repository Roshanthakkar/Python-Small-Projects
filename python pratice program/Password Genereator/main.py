import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)  this is comment becasue funtion to you get what should be return
    s2 = string.ascii_uppercase
    # print(s2)  this is comment becasue funtion to you get what should be return
    s3 = string.digits
    # print(s3)  this is comment becasue funtion to you get what should be return
    s4 = string.punctuation
    # print(s4)  this is comment becasue funtion to you get what should be return
    plen = int(input("Enter password length\n")) #Todo1: Handle Gibberish
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    # random.shuffle(s) shuffle means randomly in list 1 to 4 using divide 
    # print(s)
    print("Your password is: ")
    print("".join(random.sample(s, plen))) # s is object for use to store random list in 1 to 4
    # print("".join(s[0:plen]))

