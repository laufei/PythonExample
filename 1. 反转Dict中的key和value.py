# coding: utf-8

d = {'a': 1, 'b': 2, 'c': 3}
def revert_dict(source):
    return {v: k for k, v in d.items()}
    # return dict((v, k) for k, v in d.items())
if __name__ == "__main__":
    print revert_dict(d)