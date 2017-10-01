import csv
import random

def build_prefs(file):
    prefs = {}
    with open(file) as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            key = row[-1]
            if key in prefs:
                prefs[key] += 1
            else:
                prefs[key] = 1
    return prefs

def rank_prefs(p):
    p_sorted = sorted(p, key = p.get, reverse=True)
    return p_sorted

def build_themes(file):
    themes = {}
    with open(file) as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            keys = row[1].split(' ')
            for k in keys:
                temp = themes.get(k, [])
                temp.append((row[0], row[2]))
                themes[k] = temp
    return themes

def build_imgs(p, pk, t, r, n):
    imgs = {}
    for i in xrange(n):
        pref = pk[i]
        for j in xrange(p[pref]):
            if pref in r:
                theme = random.choice(r[pref])
                if theme in t:
                    name, link = random.choice(t[theme])
                    imgs[name] = link
    return imgs
        
if __name__ == '__main__':
    p = build_prefs('data.csv')
    pkeys = rank_prefs(p)
    t = build_themes('sdata.csv')
    r = {'Restaurant':['Food'], 'Wine':['Drinks'], 'Hiking': ['Mountain', 'Outdoor']}
    i = build_imgs(p, pkeys, t, r, 4)
    for j in xrange(1, 11):
        print("#"+ str(j) + " preference: " + str(pkeys[j]))
    for k in i:
        print(k, i[k])
