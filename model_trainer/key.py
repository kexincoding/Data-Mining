#!/usr/bin/env python
#encoding: utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("../")
import util
import json
import re
import config


def get_key(key_path, to_file):

	key = key_path
	key_list=[]
	res = {} 
	a=0
 
	with open(key) as b:  
		key_list = b.read().split()  
		for element in key_list:  
			if element.isdigit():		
				a=element
				res[a] = {}		
			else:
				res[a] = element		

	print res
	print "dump..."
	json.dump(res, open(to_file, "w"), encoding="utf-8")

if __name__ == '__main__':
	get_key(
        os.path.join(config.DATASET_PATH, "AuthorKeywords.txt"),
        os.path.join(config.DATA_PATH, "key.json"))