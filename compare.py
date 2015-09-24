__author__ = 'liza55'

# coding: utf-8
import codecs, re
from collections import OrderedDict

# compare freeling and mystem morpho markup
arr_freel = []
arr_mystem = []
attrs = ['nom', 'gen', 'dat', 'acc', 'ins', 'loc', 'voc', 'sg', 'pl', 'f', 'm', 'n', 'm-f', 'anim', 'inan',
         'anom', 'distort', 'anum', 'abbr', 'indic', 'imper', 'inf', 'ger', 'praes', 'praet', '1p', '2p', '3p', 'pf', 'ipf',
         'inf', 'act', 'pass', 'tran', 'intr', 'brev', 'plen', 'supr', 'comp']

attrs = OrderedDict()
attrs['case'] = ['nom', 'gen', 'dat', 'acc', 'ins', 'loc', 'voc']
attrs['number'] = ['sg', 'pl']
attrs['gender'] = ['f', 'm', 'n', 'm-f']
attrs['mood'] = ['indic', 'imper', 'inf', 'ger']
attrs['tense'] = ['praes', 'praet']
attrs['person'] = ['1p', '2p', '3p']
attrs['finiteness'] = ['pf', 'ipf', 'inf']
attrs['voice'] = ['act', 'pass']
attrs['aform'] = ['brev', 'plen']
attrs['clevel'] = ['supr', 'comp']

#res = codecs.open('result.csv', 'w', 'utf-8')
attrs_line = u''
for attr in attrs.keys():
    for a in attrs[attr]:
        attrs_line += a + '\t' + a + '_match' + '\t'
print attrs_line
res.write('wordform\tlemma_gold\tlemma_freel\tmatch\tpos_gold\tpos_freel\tmatch\ttag_gold\ttag_freel\ttag_original\tmatch\t' + attrs_line[:-1] + '\n')
freel = codecs.open('corpus_freeling.xhtml', 'r', 'utf-8')
mystem = codecs.open('gold_corpus2.xhtml', 'r', 'utf-8')
for line in freel.readlines():
    if '<w>' in line:
        line = line.strip()
        try:
            freel_tag = line.split(';')[1]
        except:
            freel_tag = ''
        gr = re.findall('gr="([^"]*)"', line)[0]
        lex = re.findall('lex="([^"]*)"', line)[0]
        w = re.findall('</ana>([^<]*)</w>', line)[0]
        arr_freel.append((w, lex, gr, freel_tag))
for line in mystem.readlines():
    if '<w>' in line:
        gr = re.findall('gr="([^"]*)"', line)[0]
        lex = re.findall('lex="([^"]*)"', line)[0]
        w = re.findall('</ana>([^<]*)</w>', line)[0]
        arr_mystem.append((w, lex, gr))

n = 0
for x in range(len(arr_freel[:302327])):
    w_mystem = arr_mystem[x][1].replace(u'`', u'').lower()
    #print w_mystem
    #if arr_freel[x][1] != w_mystem:
    #    print arr_freel[x][1], w_mystem, arr_freel[x][0], arr_mystem[x][0]
    #    n += 1
    #    print n
    gr_freel = arr_freel[x][2].replace(',inan', '').replace(',anim', '').replace(',intr', '').replace(',tran', '')
    # BAD!!!
    gr_freel = gr_freel.replace(',act', '').replace(',pass', '')
    gr_freel = gr_freel.split(u',')
    gr_mystem1 = arr_mystem[x][2].replace('comp2', 'comp').replace(',inan', '').replace(',anim', '').replace('dat2', 'dat').replace('gen2', 'gen').replace('acc2', 'acc').replace('loc2', 'loc').replace('adnum', 'gen').replace(',intr', '').replace(',tran', '').replace('imper2', 'imper')
    gr_mystem1 = gr_mystem1.replace(',famn', '').replace(',patrn', '').replace(',zoon', '').replace(',persn', '').replace(',anom', '').replace(',distort', '').replace('=distort', '').replace(',ciph', '').replace(',init', '').replace(',abbr', '').replace(',0', '')
    # BAD!!!
    gr_mystem1 = gr_mystem1.replace(',act', '').replace(',med', '').replace(',pass', '')
    gr_mystem1 = gr_mystem1.split(u',')
    gr_mystem = []
    for i in gr_mystem1:
        if '=' in i:
            grs = i.split('=')
            gr_mystem += grs
        else:
            gr_mystem.append(i)
    if gr_freel[0] == gr_mystem[0]:
        diff_POS = 'Yes'
    else:
        diff_POS = 'No'
    if w_mystem == arr_freel[x][1]:
        diff_lemma = 'Yes'
    else:
        print w_mystem, arr_freel[x][1]
        print x
        diff_lemma = 'No'
    if set(gr_freel) != set(gr_mystem):
    #if gr_freel[0] != gr_mystem[0]:
        if 'A-NUM' in gr_mystem and ('A-NUM' in gr_freel or 'NUM' in gr_freel):
            diff_tag = 'Yes'
        elif 'NUM' in gr_freel and 'ciph' in gr_mystem:
            diff_tag = 'Yes'
        elif 'PARENTH' in gr_mystem and 'ADV' in gr_freel:
            diff_tag = 'Yes'
        elif 'ADV-PRO' in gr_mystem and 'PRO' in gr_freel:
            diff_tag = 'Yes'
        elif 'PRAEDIC-PRO' in gr_mystem and 'PRAEDIC' in gr_freel:
            diff_tag = 'Yes'
        elif 'dat2' in gr_mystem and 'dat' in gr_freel:
            diff_tag = 'Yes'
        elif 'acc2' in gr_mystem and 'acc' in gr_freel:
            diff_tag = 'Yes'
        elif 'loc2' in gr_mystem and 'loc' in gr_freel:
            diff_tag = 'Yes'
        elif (('inan' in gr_freel or 'anim' in gr_freel) and ('inan' not in gr_mystem or 'anim' not in gr_mystem)) or (('inan' in gr_mystem or 'anim' in gr_mystem) and ('inan' not in gr_freel or 'anim' not in gr_freel)):
            diff_tag = 'Yes'
        elif ('1p' in gr_mystem or '2p' in gr_mystem or '3p' in gr_mystem) and ('1p' not in gr_freel or '2p' not in gr_freel or '3p' not in gr_freel):
            diff_tag = 'Yes'
        else:
            diff_tag = 'No'
    else:
        diff_tag = 'Yes'
        #print arr_mystem[x][0], arr_mystem[x][1], gr_mystem[0], gr_freel[0], arr_freel[3]
    r = arr_mystem[x][0] + '\t' + arr_mystem[x][1] + '\t' + arr_freel[x][1] + '\t' + diff_lemma + '\t' + gr_mystem[0] + '\t' + gr_freel[0] + '\t' + diff_POS + '\t' + ','.join(gr_mystem) + '\t' + ','.join(gr_freel) + '\t' + arr_freel[x][3] + '\t' + diff_tag + '\t'
    for attr in attrs.keys():
        if len(set(attrs[attr]) & set(gr_mystem)) > 0:
            for v in attrs[attr]:
                if v in gr_freel and v in gr_mystem:
                    r += 'Yes\tYes\t'
                elif v in gr_freel and v not in gr_mystem:
                    r += 'Yes\tNo\t'
                elif v not in gr_freel and v in gr_mystem:
                    r += 'No\tNo\t'
                elif v not in gr_freel and v not in gr_mystem:
                    r += 'No\tYes\t'
        else:
            for v in attrs[attr]:
                r += 'NA\tNA\t'

    r = r[:-1] + '\n'
    #res.write(r)
            #res.write(arr_freel[x][0] + '\t' + arr_freel[x][1] + '\t' + ','.join(gr_freel) + '\t' + w_mystem + '\t' + arr_mystem[x][0] + '\t' + ','.join(gr_mystem) + '\n')
            #print arr_freel[x][1], gr_freel, arr_freel[x][0], w_mystem, gr_mystem, arr_mystem[x][0]
            #n += 1
#res.close()
        #n = 0
        #len_gr = len(gr_freel)
        #for y in gr_freel:
        #    if y in gr_mystem:
        #        n +=1
        #if n >= len_gr - 3:
        #print gr_freel, arr_freel[x][1], arr_freel[x][0], gr_mystem, arr_mystem[x][1], arr_mystem[x][0]
#print float(n)/len(arr_freel)

#for x in range(2000):
            #print arr_freel[x][2], arr_mystem[x][2]
