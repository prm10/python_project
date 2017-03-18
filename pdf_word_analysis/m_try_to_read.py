#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'prm14'


from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice



def read_pdf(fp):
	# 创建一个PDF文档解析器对象
	parser = PDFParser(fp)
	# 创建一个PDF文档对象存储文档结构
	# 提供密码初始化，没有就不用传该参数
	document = PDFDocument(parser, password='')
	# 检查文件是否允许文本提取
	if not document.is_extractable:
		raise PDFTextExtractionNotAllowed
	# 创建一个PDF资源管理器对象来存储共享资源
	resource_manager = PDFResourceManager()
	# 创建一个pdf设备对象
	device = PDFDevice(resource_manager)
	# 创建一个PDF解析器对象
	interpreter = PDFPageInterpreter(resource_manager, device)
	# 处理文档当中的每个页面
	for page in PDFPage.create_pages(document):
		interpreter.process_page(page)


file_name = 'one.pdf'
with open(file_name, 'rb') as f:
	outputString = read_pdf(f)
	print(outputString)
