#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'prm14'
import utils
import os
from gensim import corpora, models


def extract_word(file_path):
	with open(file_path, 'r') as f:
		text = f.read()
		text = utils.get_word_txt(text)
		word_list = [w for w in text.split('|') if len(w) > 1]
		return word_list


def cal_tf_idf(train_set):
	# word_list = list(set([(word, 1) for literature in train_set for word in literature]))
	dic = corpora.Dictionary(train_set)
	corpus = [dic.doc2bow(text) for text in train_set]
	tf_idf = models.TfidfModel(corpus)
	corpus_tf_idf = tf_idf[corpus]
	word_tf_idf = [(word_id, value) for literature in corpus_tf_idf for word_id, value in literature]
	# word_tf_idf = tf_idf[word_list]
	# word_tf_idf = [(word, tf_idf[word]) for word in word_list]
	word_tf_idf.sort(key=lambda x: x[1], reverse=True)
	word_tf_idf2 = list()
	word_set = set()
	for word_id, value in word_tf_idf:
		if word_id not in word_set:
			word_set.add(word_id)
			word_tf_idf2.append((dic[word_id], value,))
	return word_tf_idf2


def save_result(result, file_path):
	with open(file_path, 'w') as f:
		f.write('\n'.join([str(line) for line in result]))


def run(in_dir, out_file):
	word_dict = dict()
	literature_word_list = list()
	for file_name in os.listdir(in_dir):
		file_path = os.path.join(in_dir, file_name)
		word_list = extract_word(file_path)
		literature_word_list.append(word_list)
		for word in word_list:
			word_dict.setdefault(word, 0)
			word_dict[word] += 1
	# 按词频降序排列
	word_order = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
	save_result(word_order, out_file + '_count.txt')
	word_tf_idf = cal_tf_idf(literature_word_list)
	save_result(word_tf_idf, out_file + '_tf_idf.txt')
	for item in word_tf_idf[:100]:
		print(item)


if __name__ == '__main__':
	in_dir = 'clean'
	out_file = 'result'
	run(in_dir, out_file)
