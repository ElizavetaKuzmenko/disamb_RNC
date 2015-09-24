__author__ = 'liza55'
# coding: utf-8

import codecs, re

# converts freeling-like markup into mystem-like one
res_f = codecs.open('test_freel.xhtml', 'w', 'utf-8')
res_f.write(u'<?xml version="1.0" encoding="utf-8"?><html><head></head><body>')
#w_template = u'<w><ana lex="гостиница" gr="S,f,inan=pl,nom"></ana>Гост`иницы</w>'
pos_dic = {u'A': u'A', u'D': u'ADV', u'P': u'ADV-PRO',
           u'Y': u'A-NUM', u'R': u'A-PRO',
           u'M': u'null', u'C': u'CONJ', u'J': u'INTJ', u'Z': u'NUM',
           u'T': u'PART', u'B': u'PR', u'N': u'S', u'E': u'S-PRO',
           u'V': u'V', u'Q': u'V'}
#attrDict = {
#    "N": [taggerProp, case,   number,  gender  , animation ,   addNounInfo  ,  others  ,  abuse],
#    "Y": [case  ,   number  ,  gender , animation],
#    "R": [case  ,   number  ,  gender  , animation ,   others],
#    "V": [mood  ,   number  ,  gender  , tense     ,   person ,  finiteness  ,  voice  ,  status  ,  others   ,  abuse],
#    "F": [case  ,   number  ,  gender  , tense     ,   aform  ,  finiteness  ,  voice  ,  status  ,  others   ,  abuse],
#    "D": [clevel,   others  ,  abuse],
#    "P": [others],
#    "R": [case  ,   number  ,  gender  , animation ,   others],
#    "E": [case  ,   number  ,  gender  , animation ,     person,   others],
#    "B": [others],
#    "T": [others],
#    "Z": [case  ,   number  ,  gender  , animation , others],
#    "J": [others,  abuse],
#    "C": [others],
#    "M": [others],
#    "A": [case  ,   number  ,  gender  , animation , aform   ,   clevel  ,  others,  abuse],
#            }
res = codecs.open('test_freel.txt', 'r', 'utf-8')
dic = codecs.open('dict_freel.csv', 'r', 'utf-8')
dic_gr = []
for line in dic.readlines():
    line = line.strip()
    freel, translate, ms, position = line.split('\t')
    dic_gr.append({freel: (position, ms)})
for line in res.readlines():
    line = line.strip()
    try:
        w, lex, gr, prob = line.split(' ')
        #print line.split(' '), w
    except ValueError:
        continue
    try:
        pos = pos_dic[gr[0]]
    except KeyError:
        if '_' in w:
            l = w.count('_')
            print w, l + 1
            word = u'<w><ana lex="" gr=""></ana>' + w + u'</w>' + '\n'
            res_f.write(word*(l + 1))
        continue
    if pos == 'NUM' and '_' in w:
        l = w.count('_')
        print w, l + 1
        word = u'<w><ana lex="" gr=""></ana>' + w + u'</w>' + '\n'
        res_f.write(word*(l + 1))
        continue
    ana = u''
    for x in range(len(gr)):
        for el in dic_gr:
            if el.keys()[0] == gr[x]:
                if str(x + 1) in el[gr[x]][0]:
                    if (x + 1 == 2 and pos == 'S'):

                        continue
                    else:
                        if (el[gr[x]][1] == 'fut' and pos == 'S') or (pos == 'S' and el[gr[x]][1] == 'anim' and x + 1 == 5) or ((el[gr[x]][1] == 'gen2' or el[gr[x]][1] == 'dat' or el[gr[x]][1] == 'loc' or el[gr[x]][1] == 'pl' or el[gr[x]][1] == 'f' or el[gr[x]][1] == 'm') and (pos == 'V' or pos == 'S-PRO' or pos == 'ADV' or pos == 'A')):
                            pass
                        else:
                            ana += el[gr[x]][1] + ','
                            continue
    if ana != u'':
        ana = ',' + ana[:-1]
    word = u'<w><ana lex="' + lex + u'" gr="' + pos + ana + u'"></ana>' + w + u'</w>'
    res_f.write(word + '\n')
res_f.write(u'</body></html>')
res_f.close()