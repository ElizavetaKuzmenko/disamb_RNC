import csv

data_freel = []
frequency_pos = {}
with open('diff_pymorphy4.csv', 'r', encoding='cp1251') as f:
    reader = csv.reader(f, delimiter=';')
    header = next(reader, None)
    header[3] = 'match_lemma'
    header[6] = 'match_pos'
    header[10] = 'match_tag'

    for row in reader:
        data_freel.append(dict(zip(header[:11], row[:11])))  # make a dict of feature : value

for word in data_freel:
    pos = word['pos_pymorphy']
    if pos in frequency_pos.keys():
        if word['match_pos'] != '':
            frequency_pos[pos][0] += int(word['match_pos'])
        if word['match_lemma'] != '':
            frequency_pos[pos][1] += int(word['match_lemma'])
        frequency_pos[pos][2] += 1
    else:
        frequency_pos[pos] = [0, 0, 0]

for pos in frequency_pos:
    print(pos, 1 - frequency_pos[pos][0]/frequency_pos[pos][2], 1 - frequency_pos[pos][1]/frequency_pos[pos][2])