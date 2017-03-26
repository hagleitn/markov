import sys
import re
import random

markov_dict = {}

for fs in sys.argv[2:]:
    with open(fs, 'rU') as ls:
        cur = None
        for line in ls:
            ws = re.findall(r"[\w']+|[.,!?;]", line);
            for w in ws:
                if w.isupper() and len(w) > 1:
                    continue
                if (cur != None):
                    if not cur in markov_dict:
                        markov_dict[cur] = {}
                    if w in markov_dict[cur]:
                        markov_dict[cur][w] += 1
                    else:
                        markov_dict[cur][w] = 1
                cur = w

for k in markov_dict:
    sum = 0
    for l in markov_dict[k]:
        sum += markov_dict[k][l]
    for l in markov_dict[k]:
        markov_dict[k][l] /= float(sum)

cur = '.'
first = True
min_words = int(sys.argv[1])
i = 0

while i < min_words or cur != '.':
    r = random.random()
    sum = 0
    found = False
    for k in markov_dict[cur]:
        sum += markov_dict[cur][k]
        # print cur, k, r, sum
        if r <= sum:
            if (len(k) != 1 or k.isalpha()) and not first:
                sys.stdout.write(' ')
            sys.stdout.write(k)
            sys.stdout.flush()
            # print 'picked', k
            cur = k
            first = False
            found = True
            break
    if not found:
        cur = "."
    i += 1
print
