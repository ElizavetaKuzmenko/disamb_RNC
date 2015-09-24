# coding: utf-8

__author__ = 'liza'

import codecs, re
f = codecs.open('gold_corpus.csv', 'r', 'utf-8').readlines()
m_st = codecs.open('test_corpus.xhtml', 'r', 'utf-8').readlines()
m = codecs.open('gold_corpus2.xhtml', 'w', 'utf-8')
m.write(''.join(m_st[33164:377607]))
m.close()
#m_st = [line.strip() for line in m_st if '<w>' in line]

#for l in range(len(1, m_st)):
#    w_prev = re.findall('</ana>([^<]*)</w>', m_st[l - 1], flags = re.U|re.DOTALL)[0].replace(u'`', '')
#    w_now = re.findall('</ana>([^<]*)</w>', m_st[l], flags = re.U|re.DOTALL)[0].replace(u'`', '')
#    w_