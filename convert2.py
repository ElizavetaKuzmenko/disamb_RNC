__author__ = 'liza'
# coding: utf-8

import codecs, re

# converts freeling-like markup into mystem-like one
res_f = codecs.open('corpus_freeling.xhtml', 'w', 'utf-8')
res_f.write(u'<?xml version="1.0" encoding="utf-8"?><html><head></head><body>')
#w_template = u'<w><ana lex="гостиница" gr="S,f,inan=pl,nom"></ana>Гост`иницы</w>'

# determine the POS by the first letter of the annotation
pos_dic = {u'A': u'A', u'D': u'ADV', u'P': u'ADV-PRO',
           u'Y': u'A-NUM', u'R': u'A-PRO',
           u'M': u'null', u'C': u'CONJ', u'J': u'INTJ', u'Z': u'NUM',
           u'T': u'PART', u'B': u'PR', u'N': u'S', u'E': u'S-PRO',
           u'V': u'V', u'Q': u'V'}

# here the attributes of every POS are described
attrDict = {
    "N": ['taggerProp', 'case', 'number', 'gender', 'animation',   'addNounInfo',  'others',  'abuse'],
    "Y": ['case',   'number',  'gender', 'animation'],
    "R": ['case',   'number',  'gender', 'animation',   'others'],
    "V": ['mood',   'number',  'gender', 'tense',   'person',  'finiteness',  'voice',  'status',  'others',  'abuse'],
    "F": ['case',   'number',  'gender', 'tense',   'aform',  'finiteness',  'voice',  'status',  'others', 'abuse'],
    "D": ['clevel',   'others',  'abuse'],
    "P": ['others'],
    "E": ['case',   'number',  'gender', 'animation',     'person',   'others'],
    "B": ['others'],
    "T": ['others'],
    "Z": ['case',   'number',  'gender', 'animation', 'others'],
    "J": ['others',  'abuse'],
    "C": ['others'],
    "M": ['others'],
    "A": ['case',   'number',  'gender', 'animation', 'aform',   'clevel',  'others',  'abuse'],
            }

# and here the values of the attributes
props = {
    'case': {'N': 'nom', 'G': 'gen', 'D': 'dat', 'F': 'acc', 'C': 'ins', 'O': 'loc', 'P': 'gen2', 'L': 'loc2', 'V': 'voc'},
    'number': {'S': 'sg', 'P': 'pl'},
    'gender': {'F': 'f', 'M': 'm', 'A': 'n', 'C': 'm-f'},
    'animation': {'A': 'anim', 'I': 'inan'},
    'others': {'D': 'anom', 'V': 'distort', 'I': 'anum', 'B': 'abbr'},
    'abuse': {'H': 'obsc'},
    'mood': {'D': 'indic', 'M': 'imper', 'I': 'inf', 'G': 'ger'},
    'tense': {'P': 'praese', 'F': 'praes', 'S': 'praet'},
    'person': {'1': '1p', '2': '2p', '3': '3p'},
    'finiteness': {'F': 'pf', 'N': 'ipf', 'I': 'inf'},
    'voice': {'A': 'act', 'S': 'pass'},
    'status': {'M': 'tran', 'A': 'intr'},
    'aform': {'S': 'brev', 'F': 'plen'},
    'clevel': {'E': 'supr', 'C': 'comp'}
}

res = codecs.open('freel7.csv', 'r', 'utf-8')
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
            word = u'<w><ana lex="" gr=""></ana>' + w + u'</w>' + '\n'
            res_f.write(word*(l + 1))
        continue
    if '[?' in gr:
        word = u'<w><ana lex="None" gr="NONLEX"></ana>None</w>;None'
        res_f.write(word + '\n')
        continue
    if pos == 'NUM' and '_' in w:
        l = w.count('_')
        word = u'<w><ana lex="" gr=""></ana>' + w + u'</w>' + '\n'
        res_f.write(word*(l + 1))
        continue
    if gr[0] == 'Q':
        attrs = 'V'
    else:
        attrs = gr[0]
    pr = attrDict[attrs]
    ana = u''
    person = u''
    gr = gr.replace('P1', '1').replace('P2', '2').replace('P3', '3')
    for prop in range(len(gr[1:])):
        attrib = u''
        if gr[1:][prop] == '0':
            continue
        #if gr[1:][prop] == 'P':
        #    person = 'P'
        #if gr[1:][prop] in '123' and person != u'':
        #    person += gr[1:][prop]
        try:
            means = pr[prop]
        except IndexError:
            continue
        if means == 'taggerProp' or means == 'addNounInfo':
            continue
        if person != u'':
            attrib = person
        else:
            attrib = gr[1:][prop]
        try:
            ms = props[means][attrib]
        except KeyError:
            continue
        ana += ms + ','
    if ana != u'':
        ana = ',' + ana[:-1]
    word = u'<w><ana lex="' + lex + u'" gr="' + pos + ana + u'"></ana>' + w + u'</w>' + u';' + gr
    res_f.write(word + '\n')
res_f.write(u'</body></html>')
res_f.close()
