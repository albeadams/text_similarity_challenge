import re, sys

contractions = { 
"ain't": "am not / are not / is not / has not / have not",
"aren't": "are not / am not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he had / he would",
"he'd've": "he would have",
"he'll": "he shall / he will",
"he'll've": "he shall have / he will have",
"he's": "he has / he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how has / how is / how does",
"I'd": "I had / I would",
"I'd've": "I would have",
"I'll": "I shall / I will",
"I'll've": "I shall have / I will have",
"I'm": "I am",
"I've": "I have",
"isn't": "is not",
"it'd": "it had / it would",
"it'd've": "it would have",
"it'll": "it shall / it will",
"it'll've": "it shall have / it will have",
"it's": "it has / it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she had / she would",
"she'd've": "she would have",
"she'll": "she shall / she will",
"she'll've": "she shall have / she will have",
"she's": "she has / she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as / so is",
"that'd": "that would / that had",
"that'd've": "that would have",
"that's": "that has / that is",
"there'd": "there had / there would",
"there'd've": "there would have",
"there's": "there has / there is",
"they'd": "they had / they would",
"they'd've": "they would have",
"they'll": "they shall / they will",
"they'll've": "they shall have / they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we had / we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what shall / what will",
"what'll've": "what shall have / what will have",
"what're": "what are",
"what's": "what has / what is",
"what've": "what have",
"when's": "when has / when is",
"when've": "when have",
"where'd": "where did",
"where's": "where has / where is",
"where've": "where have",
"who'll": "who shall / who will",
"who'll've": "who shall have / who will have",
"who's": "who has / who is",
"who've": "who have",
"why's": "why has / why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you had / you would",
"you'd've": "you would have",
"you'll": "you shall / you will",
"you'll've": "you shall have / you will have",
"you're": "you are",
"you've": "you have"
}


s1 = """The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."""

s2 = """The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."""

s3 = """We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."""

s4 = """more sample"""

s5 = """another sample"""

phrases = [s1,s2,s3,s4,s5]

def remove_punctuation_lowercase(phrases):
    p = []
    for phrase in phrases:
        #https://stackoverflow.com/questions/29930287/python-removing-punctuation-from-unicode-string-except-apostrophe
        p.append(re.sub(r"[^\w\d'\s]+",'',phrase).lower())
    return p

def count_frequency_words(phrases):
    c = []
    for phrase in phrases:
        split = set(list(phrase.split()))
        c.append({x:phrase.count(x) for x in split})
    return c

def get_all_words(p):
    words = p[0].split() + p[1].split()
    return set(words)


def get_whole(contract):
    ncontract = []
    if contract in contractions.keys():
        csplit = contractions[contract].split('/')
        ncontract = [x.strip() for x in csplit]
    return ncontract


def replace(p1, p2):
    s = p1.split()
    c1 = [x for x in s if bool(re.search("'", x))]
    for c in c1:
        nc = get_whole(c)
        for opt in nc:
            if opt in p2:
                p1 = p1.replace(c, opt)
            else:
                p1 = p1.replace(c, nc[0]) # default to first choice
    return p1
        
def replace_contractions(p):
    x, y = replace(p[0], p[1]), replace(p[1], p[0])
    return x, y


def sum_to_stop(num):
    sum = 0
    for i in range(2, num+1):
        sum = sum+i
    return sum

def shifting_window(p, verbose=False):
    s1 = p[0].split()
    s2 = p[1].split()
    m = p[0] if len(s1) > len(s2) else p[1]
    n = p[0] if len(s1) <= len(s2) else p[1]
    m = m.split()
    stop = 3
    div = sum_to_stop(stop)
    final_count = 0
    total_count = 0
    k = 0
    for i in range(2,stop+1): #shifting window
        count = 0
        total_count = 0
        for j in range(0,len(m[:-i])+1):
            gram = ' '.join(m[j:j+i])
            if gram in n:
                count += 1
            total_count += 1
        final_count += (count/total_count)*((stop-k)/div)
        k = k + 1
    return final_count

def process(phrase1, phrase2, verbose=False):
    p1, p2 = remove_punctuation_lowercase([phrase1, phrase2])
    p1, p2 = replace_contractions([p1, p2])
    freq1, freq2 = count_frequency_words([p1,p2])
    words = get_all_words([p1,p2])
    p1v = [1 if x in p1 else 0 for x in words]
    p2v = [1 if x in p2 else 0 for x in words]
    matches = [1 for idx,val in enumerate(words) if p1v[idx]==p2v[idx]]
    nonmatches = [1 for idx,val in enumerate(words) if p1v[idx]!=p2v[idx]]
    word_matches = len(matches)/(len(words))
    window_matches = shifting_window([p1,p2], verbose)
    return word_matches*.75 + window_matches*.25



def main(argv):
    try:
        a = int(argv[0])
        b = int(argv[1])
        print(process(phrases[a-1], phrases[b-1]))
    except ValueError:
        if len(argv) != 2:
            print('Only supply 2 args, either strings or in set [1,2,3]')
            return
        print(process(str(argv[0]), str(argv[1])))

if __name__ == "__main__":
    main(sys.argv[1:])