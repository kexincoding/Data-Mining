#!/usr/bin/env python
#encoding: utf-8
import sys
from authorIdPaperId import AuthorIdPaperId
import util
import config
import pyprind


def prepare_author_keywords(aid_pid_path, paper_path):
    aid_pid = util.read_dict_from_csv(aid_pid_path)
    paper = util.read_dict_from_csv(paper_path)
    print 'finish loading csv file'
    max_aid, max_pid = 0, 0
    for item in aid_pid:
        max_aid = max(max_aid, int(item["AuthorId"]) )
        max_pid = max(max_pid, int(item['PaperId']))
    for item in paper:
        max_pid = max(max_pid, int(item["Id"]))
    print 'max_aid',max_aid,'max_pid',max_pid

    paper_indexd_list = range(max_pid+1)
    for item in paper:
        paper_indexd_list[int(item["Id"])] = item
    del paper

    keywords = [[]]*(max_aid+1)
    bar = pyprind.ProgPercent(len(aid_pid))
    for item in aid_pid:
        bar.update()
        aid = int(item['AuthorId'])
        pid = int(item['PaperId'])
        if pid != paper_indexd_list[pid]:
            kw = paper_indexd_list[pid]["Keyword"]
            if kw:
                keywords[aid].append(kw)

    author_keywords = []
    for index,item in enumerate(keywords):
        dic = {}
        if item:
            dic["AuthorId"] = str(index)
            dic["Keywords"] = " ".join(item)
            author_keywords.append(dic)

    del keywords
    write_dict_to_csv(['AuthorId', 'Keywords'], author_keywords, config.AUTHOR_KEYWORDS_FILE)
    print 'finish writing author_keywords csv in',config.AUTHOR_KEYWORES_FILE


if __name__=='__main__':
    prepare_author_keywords(config.PAPERAUTHOR_FILE, config.PAPER_FILE)