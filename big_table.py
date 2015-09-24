# coding: utf-8
__author__ = 'liza'

# making a big table for machine learning

import codecs
from collections import OrderedDict

freel = codecs.open('freeling_diff.csv', 'r', 'utf-8').readlines()
pym = codecs.open('diff_pymorphy4.csv', 'r', 'cp1251').readlines()
#tr = codecs.open('TREE_TAGGER.csv', 'r', 'utf-8').readlines()

#big_lemma = codecs.open('lemma_taggers_part.csv', 'w', 'utf-8')
#big_pos = codecs.open('pos_taggers_part.csv', 'w', 'utf-8')
big_tag = codecs.open('tag_taggers_part.csv', 'w', 'utf-8')

POSs = ['A', 'ADV', 'ADV-PRO', 'A-NUM', 'A-PRO', 'null', 'CONJ', 'INTJ', 'NUM', 'PART', 'PR', 'S', 'S-PRO', 'V']

first_line = 'wordform\tright1\tright2\t'

for POS in POSs:
    first_line += POS + '1\t' + POS + '2\t' #+ POS + '3\t'
first_line += 'equaltag12\t'

attrs = OrderedDict()
attrs['case'] = ['nom', 'gen', 'dat', 'acc', 'ins', 'loc', 'voc']
attrs['number'] = ['sg', 'pl']
attrs['gender'] = ['f', 'm', 'n', 'm-f']
attrs['mood'] = ['indic', 'imper', 'inf1', 'ger']
attrs['tense'] = ['praes', 'praet']
attrs['person'] = ['1p', '2p', '3p']
attrs['finiteness'] = ['pf', 'ipf', 'inf2']
attrs['voice'] = ['act', 'pass']
attrs['aform'] = ['brev', 'plen']
attrs['clevel'] = ['supr', 'comp']
for attr in attrs.keys():
    for a in attrs[attr]:
        first_line += a + '1\t' + a + '2\t'
#print len(first_line.split('\t'))

#big_lemma.write(first_line + '\n')
big_tag.write(first_line + 'trr' + '\n')
#big_tag.write(first_line + 'trrr' + '\n')

for l in range(1, len(freel[:5000])):
    print l
    line_f = freel[l].strip()
    line_p = pym[l].strip()

    wf, lemma_g, lemma_f, match_lemma, pos_g, pos_f, match_pos, tag_gold, tag_f, tag_orig, match_tag, nom, nom_match, \
    gen, gen_match, dat, dat_match, acc, acc_match, ins, ins_match, loc, loc_match, voc, voc_match, sg, sg_match, pl, \
    pl_match, f, f_match, m, m_match, n, n_match, mf, mf_match, indic, indic_match, imper, imper_match, inf1, \
    inf1_match, ger, ger_match, praes, praes_match, praet, praet_match, p1, p1_match, p2, p2_match, p3, p3_match, pf, \
    pf_match, ipf, ipf_match, inf2, inf2_match, act, act_match, passive, pass_match, brev, brev_match, plen, plen_match, \
    supr, supr_match, comp, comp_match = line_f.split('\t')

    wf_p, lemma_g_p, lemma_p, match_lemma_p, pos_g_p, pos_p, match_pos_p, tag_gold_p, tag_p, tag_orig_p, match_tag_p, \
    nom_p, nom_match_p, gen_p, gen_match_p, dat_p, dat_match_p, acc_p, acc_match_p, ins_p, ins_match_p, loc_p, \
    loc_match_p, gen2, gen2_match, loc2, loc2_match, voc_p, voc_match_p, sg_p, sg_match_p, pl_p, pl_match_p, f_p, f_match_p, m_p, m_match_p, n_p, n_match_p, \
    mf_p, mf_match_p, anim, anim_match, inan, inan_match, anom, anom_match, distort, distort_match, anum, anum_match, abbr, abbr_match, indic_p, indic_match_p, imper_p, imper_match_p, inf1_p, inf1_match_p, ger_p, ger_match_p, praes_p, \
    praes_match_p, praet_p, praet_match_p, p1_p, p1_match_p, p2_p, p2_match_p, p3_p, p3_match_p, pf_p, \
    pf_match_p, ipf_p, ipf_match_p, inf2_p, inf2_match_p, act_p, act_match_p, passive_p, pass_match_p, tran, tran_match, intr, intr_match, brev_p, \
    brev_match_p, plen_p, plen_match_p, supr_p, supr_match_p, comp_p, comp_match_p = line_p.split(';')

    line = wf + '\t'
    #print match_tag, match_tag_p
    if match_tag == '1':
        line += '1\t'
    else:
        line += '0\t'
    if match_tag_p == '1':
        line += '1\t'
    else:
        line += '0\t'
    #print line

    for POS in POSs:
        if pos_f == POS and pos_p == POS:
            line += '1\t1\t'
        elif pos_f == POS and pos_p != POS:
            line += '1\t0\t'
        elif pos_f != POS and pos_p == POS:
            line += '0\t1\t'
        elif pos_f != POS and pos_p != POS:
            line += '0\t0\t'
    if pos_f == pos_p:
        line += '1\t'
    else:
        line += '0\t'

    for a in range(11, len(freel[l].split('\t')), 2):
        if freel[l].split('\t')[a] == '1':
            line += '1\t'
        else:
            line += '0\t'
        if pym[l].split(';')[a] == '1':
            line += '1\t'
        else:
            line += '0\t'
    #big_lemma.write(line + '\n')
    big_tag.write(line + '\n')
    #print len(line.split('\t')), len(first_line.split('\t'))
    #big_tag.write(line + '\n')
#big_lemma.close()
big_tag.close()
#big_tag.close()