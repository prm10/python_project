#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'prm14'
import pandas as pd
import os
import shutil
import cPickle
import config
import re


def save_pd_to_csv(df, file_name, header=True):
	df.to_csv(file_name, sep=',', index=False, encoding='utf8', header=header)
	print('%d lines have been saved to %s' % (len(df), file_name))


def load_pd_from_csv(file_name, header=0):
	return pd.read_csv(file_name, header=header, sep=',', encoding='utf8')


# 删除目录以及目录下的文件，再重新生成该目录
def delete_then_create_dir(dir_name):
	if os.path.exists(dir_name):
		shutil.rmtree(dir_name)
		print('remove directory: ' + dir_name)
	if not os.path.exists(dir_name):
		os.makedirs(dir_name)
		print('create directory: ' + dir_name)


def write_pickle(variable_name, variable):
	data_dir = os.path.join(config.data_dir, 'pickle')
	if not os.path.exists(data_dir):
		os.mkdir(data_dir)
	with open(os.path.join(data_dir, variable_name), 'w') as f:
		cPickle.dump(variable, f)


def read_pickle(variable_name):
	data_dir = os.path.join(config.data_dir, 'pickle')
	with open(os.path.join(data_dir, variable_name), 'r') as f:
		return cPickle.load(f)


def get_readable_txt(text):
	# 把换行加的'-'去掉
	text = re.sub('(\w)-\n(\w)', '\g<1>\g<2>', text)
	# 去除pdf换行造成的换行符
	text = re.sub('([\S| ])\n([\S| ])', '\g<1> \g<2>', text)
	# 多个空格合并为一个
	text = re.sub(' +', ' ', text)
	return text


# for word count
def get_word_txt(text):
	# 将非英文符号替换为'|'
	# text = re.sub('[^A-Za-z_\n-]', '|', text)
	text = re.sub('[^A-Za-z_-]', '|', text)
	# # 将多个'|'合并为一个
	# text = re.sub('\|{2,}', '|', text)
	# 将'|-|g|u||d|-|-|'替换为'|'
	text = re.sub('(\|)(.?\|)+', '\g<1>', text)
	# 将多个'\n'合并为一个
	# text = re.sub('\n{2,}', '\n', text)
	# 首尾去除'|'
	text = re.sub('^\|', '', text)
	text = re.sub('\|$', '', text)
	return text


# for read
def get_word_txt_backup(text):
	# 将非英文符号替换为'|'
	text = re.sub('[^A-Za-z_\n-]', '|', text)
	# # 将多个'|'合并为一个
	# text = re.sub('\|{2,}', '|', text)
	# 将'|-|g|u||d|-|-|'替换为'|'
	text = re.sub('(\|)(.?\|)+', '\g<1>', text)
	# 将多个'\n'合并为一个
	text = re.sub('\n{2,}', '\n', text)
	return text
