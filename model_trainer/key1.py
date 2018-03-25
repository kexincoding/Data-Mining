#!/usr/bin/env python
#encoding: utf-8
import os
import sys
import pandas as pd
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("../")
import util
import json
from collections import Counter
import config

#获取每个作者的top k个发表论文的journal或者conference
def get_top_k_key(Authorkeywords_PATH, k, to_file):

    data_authors = util.read_dict_from_csv(Authorkeywords_PATH)
    
    dict_authors_to_key= {}
    for item in data_authors:
        AuthorId = item["AuthorId"]
        key = item["keyword1"]
	if  AuthorId not in dict_authors_to_JC:
			dict_authors_to_JC[AuthorId] = []
		dict_authors_to_JC[AuthorId].append(key)
        key = item["keyword2"]
	if  AuthorId not in dict_authors_to_JC:
			dict_authors_to_JC[AuthorId] = []
		dict_authors_to_JC[AuthorId].append(key)
        key = item["keyword3"]
	if key is not None:
		if  AuthorId not in dict_authors_to_JC:
			dict_authors_to_JC[AuthorId] = []
		dict_authors_to_JC[AuthorId].append(key)
        key = item["keyword4"]
	if key is not None:
		if  AuthorId not in dict_authors_to_JC:
			dict_authors_to_JC[AuthorId] = []
		dict_authors_to_JC[AuthorId].append(key)        
	key = item["keyword5"]
	if key is not None:
		if  AuthorId not in dict_authors_to_JC:
			dict_authors_to_JC[AuthorId] = []
		dict_authors_to_JC[AuthorId].append(key)
	key = item["keyword6"]
	if key is not None:
		if  AuthorId not in dict_authors_to_JC:
			dict_authors_to_JC[AuthorId] = []
		dict_authors_to_JC[AuthorId].append(key)
	key = item["keyword7"]
	if key is not None:
		if AuthorId not in dict_authors_to_JC:
			dict_authors_to_JC[AuthorId] = []
		dict_authors_to_JC[AuthorId].append(key)
	key = item["keyword8"]
	if key is not None:
		if  AuthorId not in dict_authors_to_JC:
			dict_authors_to_JC[AuthorId] = []
		dict_authors_to_JC[AuthorId].append(key)
	key = item["keyword9"]
	if key is not None:
		if  AuthorId not in dict_authors_to_JC:
			dict_authors_to_JC[AuthorId] = []
		dict_authors_to_JC[AuthorId].append(key)
	key = item["keyword10"]
	if key is not None:
		if  AuthorId not in dict_authors_to_JC:
			dict_authors_to_JC[AuthorId] = []
		dict_authors_to_JC[AuthorId].append(key)


    dict_authors_to_key11={}
    for AuthorId in dict_authors_to_key:
        key11 = dict_authors_to_key[AuthorId]
        n = len(key11)
        for i in range(n):
            for j in range(i+1, n):
                if key11[i] not in dict_authors_to_key11:
                    dict_authors_to_key11[key11[i]] = Counter()
                if key11[j] not in dict_authors_to_key11:
                    dict_authors_to_key11[key11[j]] = Counter()
                dict_authors_to_key11[key11[i]][key11[j]] += 1
                dict_authors_to_key11[key11[j]][key11[i]] += 1
    
    print "get top k..."
    
    res = {}
    for AuthorId in dict_authors_to_key11:
        res[AuthorId] = {}
        for keyId, freq in dict_authors_to_key11[AuthorId].most_common(k):
            res[AuthorId][keyId] = freq
    print res
    
    print "dump..."
    
    json.dump(res, open(to_file, "w"), encoding="utf-8")

    #json.dump(dict_authors_Journal_Conference, open(to_file, "w"), encoding="utf-8")


if __name__ == '__main__':
    k = 10
    get_top_k_key(
        os.path.join(config.DATASET_PATH, "AuthorKeywords2.csv"),
        k,
        os.path.join(config.DATA_PATH, "AuthorKeywords2.json"))

