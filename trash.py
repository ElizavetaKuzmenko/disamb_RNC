import codecs,re
__author__ = 'liza55'

# ah, nothing
f = codecs.open('text.txt', 'r', 'utf-8').read()
f = re.sub('\\s', ' ', f, flags = re.U|re.DOTALL)
t = codecs.open('new_text.txt', 'w', 'utf-8')
t.write(f)
t.close()