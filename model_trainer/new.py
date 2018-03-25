#!/usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("../")
import config
import json
import util


def Journal_Conference(PaperAuthor_PATH, Paper_PATH, Journal_PATH, Conference_PATH, to_file):

    data = util.read_dict_from_csv(PaperAuthor_PATH)
    for item in data:
        PaperId = item["PaperId"]
        AuthorId = item["AuthorId"]
		dict_authors_Journal_Conference= {}
		if  AuthorId not in dict_authors_Journal_Conference:
            dict_authors_Journal_Conference[AuthorId] = []

		data1 = util.read_dict_from_csv(Paper_PATH)
		for paperId in data1:
			用paperId找到Journal_Conference的ID
        for
			用Journal_Conference的ID找到Journal_Conference的具体名称


        dict_paperId_to_authors[AuthorId].append(具体名称)
        

    json.dump(dict_authors_Journal_Conference, open(to_file, "w"), encoding="utf-8")

if __name__ == '__main__':
    load_paperIdAuthorId_to_name_and_affiliation(config.PAPERAUTHOR_FILE, config.DATASET_PATH + "/paperIdAuthorId_to_name_and_affiliation.json")


