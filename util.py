# -*- coding: utf-8 -*-

"""
==================================================
   File Name：     util.py
   email:         songdongdong@weidian.com
   Author :       songdongdong
   date：          2020/7/24 16:59
   Description :  
==================================================
"""

import logging
import glob
import re
logging.basicConfig(level=logging.INFO, format=u'%(asctime)s - %(levelname)s - %(message)s')


class Progress:
    """显示进度，自己简单封装，比tqdm更可控一些
    iterator: 可迭代的对象；
    period: 显示进度的周期；
    steps: iterator可迭代的总步数，相当于len(iterator)
    """

    def __init__(self, iterator, period=1, steps=None, desc=None):
        self.iterator = iterator
        self.period = period
        if hasattr(iterator, '__len__'):  # hasattr() 函数用于判断对象是否包含对应的属性。
            self.steps = len(iterator)
        else:
            self.steps = steps
        self.desc = desc
        if self.steps:
            self._format_ = u' %s/%s  passed' % ('%s', self.steps)
        else:
            self._format_ = u'%s passed'
        if self.desc:
            self._format_ = self.desc + ' - ' + self._format_
        self.logger = logging.getLogger()

    def __iter__(self):  # 从这里返回的是一个迭代器对象
        for i, j in enumerate(self.iterator):
            if (i + 1) % self.period == 0:
                self.logger.info(self._format_ % (i + 1))
            yield j


def text_generator(text):

    #txts = glob.glob('/Users/songdongdong/workSpace/datas/THUCNews/*/*.txt') #返回匹配到的所有文件
    text = glob.glob(text) #返回匹配到的所有文件
    # with open (path+"ds_vdian_search_new_query_report_di_0716","r",encoding="utf-8") as file:
    #     text = file.readlines()
    txts = text[:10000]

    for txt in txts:
        with open(txt,"r",encoding="utf-8") as file:
            lines  = file.readlines()
            for line in lines:
                d = line.replace(u'\u3000', ' ').strip()
                yield d
        # d = open(txt, encoding='utf-8').read()
        # d = d.replace(u'\u3000', ' ').strip()
        # print(re.sub(u'[^\u4e00-\u9fa50-9a-zA-Z ]+', '\n', d))
        # yield re.sub(u'[^\u4e00-\u9fa50-9a-zA-Z ]+', '\n', d) # 抽取所有的文字，并以\n分割段落


def write_corpus(generater, filename):
    """:q：将语料写到文件中，词与词(字与字)之间用空格隔开
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for s in Progress(generater, 10000, desc=u'exporting corpus'):
            s = ' '.join(s.strip()) + '\n'
            f.write(s)


def parse_text(text):
    return ' '.join(list(text))