#!/usr/bin/env python

import yaml
import os
from random import randint as rnd

def randelt(lst):
    return lst[rnd(0, len(lst)-1)]

y = yaml.load(open('ff.yml', 'r'))
facts = y['facts']

rf = randelt(facts)

with open('index.html', 'w') as f:
    f.write('<html>\n\t<p>\n\t\t%s\n\t</p>\n</html>\n' % rf)

os.system('git add index.html')
os.system('git commit -m "rf"')
os.system('git push')
