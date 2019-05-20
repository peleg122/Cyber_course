import hashlib

outer_dictionary = {}
inner_dictionary = {}
ans_to_find = ['dcddb75469b4b4875094e14561e573d8', '3cdf5666859f6906c283a1058cd5b9a7', '1c53056c382c3048dec245445d5a6196', '195479f4d1ac291efa44fb760bf5767e']


def creating():
    create_dict = open("dict.csv", "w")
    for i in range(0, 100000):
        word = '{:>5}'.format(str(i).zfill(5))
        result = hashlib.md5(word.encode())
        md5_word = result.hexdigest()
        outer_dictionary[word] = md5_word
        result_inner = hashlib.md5(md5_word.encode())
        inner_md5_word = result_inner.hexdigest()
        inner_dictionary[md5_word] = inner_md5_word
        create_dict.write(word)
        create_dict.write(";")
        create_dict.write(md5_word)
        create_dict.write(";")
        create_dict.write(inner_md5_word)
        if not i == 99999:
            create_dict.write('\n')


creating()


def decrypt():
    for i in range(0, 4):
        for x in outer_dictionary:
            inner_val = inner_dictionary[outer_dictionary[x]]
            if ans_to_find[i] == outer_dictionary[x]:
                print x+';'+'0'
            if ans_to_find[i] == inner_val:
                print x+';'+'1'


decrypt()
