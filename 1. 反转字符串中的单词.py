# coding: utf-8

def reverStr(string):
    return " ".join([i[::-1] for i in string.split(" ")])

if __name__ == "__main__":
    string = "Let's take LeetCode contest"
    print reverStr(string)