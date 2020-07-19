def func(s):
    import numpy as np 
    import pandas as pd
    import os
    
    import nltk
    nltk.download('punkt')
    from nltk.corpus import wordnet as wn
    from nltk.tokenize import RegexpTokenizer
    
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    from pywsd.lesk import simple_lesk as sl
    nltk.download('stopwords')
    nltk.download('wordnet')
    print(s)
    sentences = nltk.sent_tokenize(s.lower())
    print(sentences)
    tt=""
    sentences2=[]
    for x in sentences:
        tokenizer = RegexpTokenizer('\w+')
        text2=tokenizer.tokenize(x)
       
        cnt=1
        for x2 in text2:
            if cnt==1:
                tt+=x2
                cnt=0
            else:
                tt+=" "+x2    
        sentences2.append(tt)
        tt=""
    stop_words = set(stopwords.words("english"))
    context_tab=[]
    for sentence in sentences2:
        words = nltk.word_tokenize(sentence)
        without_stop_words = [word for word in words if not word in stop_words]
        context_tab.append(without_stop_words)
    lemma=[]
    wl=WordNetLemmatizer()
    for x in context_tab:
        m2=[]
        for x2 in x:
            x3=wl.lemmatize(x2,wn.VERB)
            x3=wl.lemmatize(x3,wn.NOUN)
            x3=wl.lemmatize(x3,wn.ADJ)
            x3=wl.lemmatize(x3,wn.ADV)
            m2.append(x3)
        lemma.append(m2)
    li=[]
    d={}
    for i in lemma:
        for j in i:
            output = sl(s,j)
            d[j]=output.definition()
    return d


        