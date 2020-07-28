# -*- coding: utf-8 -*-

"""
==================================================
   File Name：     base.py
   email:         songdongdong@weidian.com
   Author :       songdongdong
   date：          2020/7/24 14:38
   Description :  
==================================================
"""

import os

from util import write_corpus, text_generator ,parse_text

path = "/Users/songdongdong/workSpace/datas/new_finds/"
kenlm_dir = "/Users/songdongdong/kenlm/build/bin/"
text = "ds_vdian_search_new_query_report_di_0716"
raw_file = path + text  # 原始文本

#模型文件
arpa_file = path + text + '.arpa'
bin_file = path + text + ".bin"

#文件保存
corpus_file = path + text + '.corpus'  # 语料保存的文件名 ,这也是需要经过预处理的文本
vocab_file = path + text + '.chars'  # 字符集保存的文件名
ngram_file = path + text + '.ngrams'  # ngram集保存的文件名
output_file = path + text + '.vocab'  # 最后导出的词表文件名

#
# # 文本预处理，
# write_corpus(text_generator(raw_file), corpus_file)
#
# # 训练模型
# os.system(
#     kenlm_dir + "lmplz -o 4 < " + corpus_file + ">" + arpa_file)
#
# # 压缩模型
# os.system(
#     kenlm_dir + "build_binary -s  " + arpa_file + " " + bin_file)

#count_ngrams
#利用kenlm的count_ngrams计算n-grams
# order = 4  # n-gram
# memory = 0.5 # 内存占有
# done = os.system(
#         kenlm_dir+'count_ngrams -o %s --memory=%d%% --write_vocab_list %s <%s >%s'
#         % (order, memory * 100, vocab_file, corpus_file, ngram_file)
#     )


#3.1 model.score函数
import kenlm
model = kenlm.Model(bin_file)
print(model.score('this is a sentence .', bos = True, eos = True))
# 其中， 每个句子通过语言模型都会得到一个概率(0-1),然后对概率值取log得到分数(-\propto ,0],
# 得分值越接近于0越好。 score函数输出的是对数概率，即log10(p('微 信'))，其中字符串可以是gbk，也可以是utf-8
# bos=False, eos=False意思是不自动添加句首和句末标记符,得分值越接近于0越好。
# 一般都要对计算的概率值做log变换，不然连乘值太小了，在程序里会出现 inf 值。

#该模块，可以用来测试词条与句子的通顺度：,注意这里需要空格分割下：
text = '再 心 每 天也 不 会 担 个 大 油 饼 到 了 下  午 顶 着 一 了 '
print(model.score(text, bos=True, eos=True))


#3.2  model.full_scores函数
#score是full_scores是精简版，full_scores会返回： (prob, ngram length, oov) 包括：概率，ngram长度，是否为oov
# Show scores and n-gram matches
sentence = '盘点不怕被税的海淘网站❗️海淘向来便宜又保真，比旗舰店、专柜和代购好太多！'
words = ['<s>'] + parse_text(sentence).split() + ['</s>']
print(words)
for i, (prob, length, oov) in enumerate(model.full_scores(sentence)):
    print('{0} {1}: {2}'.format('prob:  ',prob, ' length :   ' ,length, ' '.join(words[i+2-length:i+2])))
    if oov:
        print('\t"{0}" is an OOV'.format(words[i+1]))


# Find out-of-vocabulary words
for w in words:
    if not w in model:
        print('"{0}" is an OOV'.format(w))



#3.3 kenlm.State()状态转移概率
'''
状态的累加
score defaults to bos = True and eos = True.  
Here we'll check without the endof sentence marker.  
'''
#Stateful query
state = kenlm.State()
state2 = kenlm.State()
#Use <s> as context.  If you don't want <s>, use model.NullContextWrite(state).
model.BeginSentenceWrite(state)

accum = 0.0
accum += model.BaseScore(state, "海", state2)
print(accum)
accum += model.BaseScore(state2, "淘", state)
print(accum)
accum += model.BaseScore(state, "</s>", state2)
print(accum)
#这个实验可以看到：state2的状态概率与score的概率差不多，该模块还有很多可以深挖，NSP任务等等。

