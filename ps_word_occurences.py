from pprint import pprint as pp

# get word counts
def get_word_occurences(txt_file):



    words_dict = {}
    count = 1

    for line in open(txt_file):
        for word in line.rstrip().split(':'):
            #if words_dict.get(word) == None:
            #    words_dict[word] = count
            #else:
                words_dict[word] = words_dict.get(word, 0) + 1;
    pp(words_dict)
    return words_dict


# group by word occurences
def get_word_by_occurences(word_count):
    group_by = dict()

    for word, count in word_count.items():
        if count not in group_by:
            group_by[count] = list()

        group_by[count].append(word)
    return group_by




wc = get_word_occurences('resources/data1.txt')
grp = get_word_by_occurences(wc)
pp(grp)