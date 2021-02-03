import re

##Do you count punctuation or only words? - as it is specified that punctuation can ##hamper the accuracy of the similarity so it is visible in the below code that #punctutaion is eradicated from the samples
##Which words should matter in the similarity comparison? - the word that is taken out ##after removing punctuation and stop words 
##Do you care about the ordering of words? - ordering of data is good for analysis but ##if we follow the approach of changing the following in metrics or array it does not ##matter as the code is designed in such a way
##What metric do you use to assign a numerical value to the similarity? - array are used ##to create the metrics
##What type of data structures should be used? (Hint: Dictionaries and lists are ##particularly helpful data structures that can be leveraged to calculate the similarity ##of two pieces of text.) - mainly dictionary and lists are used

def string_similarity(sentence_pr, sentence_dr):

## stop words are introduced so that correct similarity can happen between the samples 
## amongst the words on which real emphasis should be kept
    stop_words=["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","dont","should","now","the","if","ll"]

## as we cannot use nltk.word tokenize so we have used re function 
## and split function to tokenize the word as per the requirements
    
    words1 = re.sub("[^\w]"," ", sentence1).split(" ")
    words2 = re.sub("[^\w]"," ", sentence2).split(" ")
    words3 = re.sub("[^\w]"," ", sentence3).split(" ")

## empty arrays to store the key value pair created below as a vector as per their occurences
    
    l1 = []
    l2 = []
    l3 = []

## to remove the stopwords present in the outcome produced as removing the stopwords increase the accuracy 
## between the similarity of list produced by the sample

    sen1_l = [word.lower() for word in words1 if word not in stop_words]
    sen2_l = [word.lower() for word in words2 if word not in stop_words]
    sen3_l = [word.lower() for word in words3 if word not in stop_words]

## following if else condtion is kept to see what 2 sample or 
## text accuracy is being tested processing happens according to that only
## this test shows the similarity betweent the text1 sample and text2 sample
## similarity between sample1 and sample2:  0.7937507937511906
##################COSINE SIMILARITY##################################################################

    if (sentence_pr == sentence1 and sentence_dr == sentence2):
        rvector_1_2 = set(sen1_l).union(set(sen2_l))
        for w in rvector_1_2:
            if w in sen1_l:l1.append(1)
            else:l1.append(0)
            if w in sen2_l:l2.append(1)
            else:l2.append(0)

        c = 0

        for i in range(len(rvector_1_2)):
            c += l1[i]*l2[i]
        cosine_1_2 = c /float((sum(l1)*sum(l2))**0.5)
        print("similarity between sample1 and sample2: ", cosine_1_2)
    
## this test shows the similarity betweent the text1 sample and text3 sample 
## similarity between sample1 and sample3:  0.1935483870967742
##################COSINE SIMILARITY##################################################################
    
    elif(sentence_pr == sentence1 and sentence_dr == sentence3):
        rvector_1_3 = set(sen1_l).union(set(sen3_l))
        for w in rvector_1_3:
            if w in sen1_l:l1.append(1)
            else:l1.append(0)
            if w in sen3_l:l3.append(1)
            else:l3.append(0)

        c = 0

        for i in range(len(rvector_1_3)):
            c += l1[i]*l3[i]
        cosine_1_3 = c /float((sum(l1)*sum(l3))**0.5)
        print("similarity between sample1 and sample3: ", cosine_1_3)

## this test shows the similarity betweent the text2 sample and text3 sample 
## similarity between sample1 and sample3:  0.15875015875023812
##################COSINE SIMILARITY##################################################################
    
    elif(sentence_pr == sentence2 and sentence_dr == sentence3):
        rvector_2_3 = set(sen2_l).union(set(sen3_l))
        for w in rvector_2_3:
            if w in sen2_l:l2.append(1)
            else:l2.append(0)
            if w in sen3_l:l3.append(1)
            else:l3.append(0)

        c = 0

        for i in range(len(rvector_2_3)):
            c += l2[i]*l3[i]
        cosine_2_3 = c /float((sum(l2)*sum(l3))**0.5)
        print("similarity between sample2 and sample3: ", cosine_2_3)


sentence1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
sentence2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
sentence3 = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."
print(string_similarity(sentence1,sentence2))
print(string_similarity(sentence1,sentence3))
print(string_similarity(sentence2,sentence3))


## output for the similarity of text using cosine similarity
##similarity between sample1 and sample2:  0.7937507937511906
##similarity between sample1 and sample3:  0.1935483870967742
##similarity between sample2 and sample3:  0.15875015875023812







    
    
