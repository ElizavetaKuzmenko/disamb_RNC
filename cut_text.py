# coding: utf-8
__author__ = 'liza'

import codecs, re
f = codecs.open('freel7.csv', 'r', 'utf-8').readlines()
words1 = []
words2 = []
m_st = codecs.open('gold_corpus2.xhtml', 'r', 'utf-8').readlines()
puncts = u'.,:;?!()"\''
for line in f:
    if line.strip() != '':
        word = line.split()[0]
        if word not in puncts:
            words1.append(word)
for line in m_st:
    word = re.findall('</ana>([^<]*)</w>', line, flags = re.U|re.DOTALL)
    if word != []:
        words2.append(word[0])
print len(words1), len(words2)
print words1[0], words2[0]
print words1[-1], words2[-1]


#    if line == u'':
#        t.write(sentence + '\n')
#        sentence = u''
#    else:
#        sentence += line.split()[0] + ' '
#t.close()
