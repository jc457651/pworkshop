__author__ = 'jc457651'
a_string = input("TEXT:")
word_list = a_string.split()
count_word_dict = {}
for word  in word_list:
    count_word_dict [word] = word_list.count(word)
for key in count_word_dict:
    print("{}: {}".format(key,count_word_dict[key]))
