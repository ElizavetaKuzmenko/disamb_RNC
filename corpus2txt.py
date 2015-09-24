#coding: utf-8
__author__ = 'liza55'

#from lxml import etree
import re, codecs

# exctracts pure text from our test corpus in html
text = u''
new = codecs.open(u'test_corpus.txt', 'w', 'utf-8')
corpus = codecs.open(u'test_corpus.xhtml', 'r', 'utf-8')
i = 0
for line in corpus.readlines():
    text = u''
    i += 1
    word = re.findall('</ana>([^<]*)</w>', line, flags = re.U|re.DOTALL)
    if word != []:
        word = word[0].replace(u'`', u'')
        text += word
    punct = re.findall('</w>([^\n<]*)', line, flags = re.U|re.DOTALL)
    if punct != []:
        if u'«' not in punct[0]:
            punct = punct[0].replace(u' ', u'')
            text += punct + u' '
        else:
            text += punct[0]
    #new.write(text)
    new.write(text.replace('\n', '').replace('\r', '') + '\n')
new.close()
