#coding=utf-8 

import urllib2
from sgmllib import SGMLParser

class MainPageAnalysis(SGMLParser):
    
    def reset(self):  
        self.data_url={}
        self.url = ''
        self.is_div = False
        self.is_a = False
        SGMLParser.reset(self)
    
    def start_div(self, attrs):
        for k, v in attrs:
            if k == 'class' and v == 'hd2 clearfix':
                self.is_div = True
                return

    def end_div(self):
        self.is_div = False

    def start_a(self, attrs):
        if self.is_div == True:
            self.is_a = True
            for k, v in attrs:
                if k == 'href':
                    self.url = v
                    return

    def end_a(self):
        self.is_a = False

    def handle_data(self,data):
        if self.is_a:
            self.data_url[data] = self.url


class SubPageAnalysis(SGMLParser):

    def reset(self):
        self.ghd = ''
        self.ghd_gbd = {}
        self.is_div_ghd = False
        self.is_h3_ghd = False
        self.is_a_ghd = False
        
        self.url_gbd = ''
        self.div_layer = 0
        self.is_div_gbd = False
        self.is_h5_gbd = False
        self.is_a_gbd = False
        
        SGMLParser.reset(self)
    
    def start_div(self, attrs):
        for k, v in attrs:
            if k == 'class' and v == 'ghd':
                self.is_div_ghd = True
            if k == 'class' and v == 'gbd':
                self.is_div_gbd = True
            
            if self.is_div_gbd == True:
                self.div_layer += 1

    def end_div(self):
        if self.is_div_ghd == True:
            self.is_div_ghd = False
        
        if self.is_div_gbd == True:
            self.div_layer -= 1
            if self.div_layer == 0:
                self.is_div_ghd = False
            
    def start_h3(self, attrs):
        if self.is_div_ghd == True:
            self.is_h3_ghd = True

    def end_h3(self):
        self.is_h3_ghd = False

    def start_h5(self, attrs):
        if self.is_div_gbd == True:
            self.is_h5_gbd = True

    def end_h5(self):
        self.is_h5_gbd = False

    def start_a(self,attrs):
        if self.is_div_ghd == True and self.is_h3_ghd == True:
            self.is_a_ghd = True
        if self.is_div_gbd == True and self.is_h5_gbd == True:
            self.is_a_gbd = True
            for k, v in attrs:
                if k == 'href':
                    self.url_gbd = v

    def end_a(self):
        if self.is_a_ghd == True:
            self.is_a_ghd = False
            self.is_h3_ghd = False
            return
        if self.is_a_gbd == True:
            self.is_a_gbd = False
            return

    def handle_data(self,data):
        if self.is_a_ghd == True:
            self.ghd = data
            self.ghd_gbd[data] = {}
        if self.is_a_gbd == True:
            self.ghd_gbd[self.ghd][data]= self.url_gbd

class SubSubPageAnalysis(SGMLParser):

    def reset(self):
        self.year_info = {}
        self.year_list = []
        self.key = ''
        self.key_count = 0
        self.key_value = []
        self.div_year = False
        self.a_year = False
        self.div_detail_layer = 0
        self.div_detail_true_count = 0
        self.div_detail = False
        self.span_key = False
        self.span_value = False
        
        SGMLParser.reset(self)

    def start_div(self, attrs):
        for k, v in attrs:
            if k == 'class' and v == 'year_type':
                self.div_year = True
            if k == 'class' and (v == 'detailinfo' or v == 'price'):
                self.div_detail = True
                self.div_detail_true_count += 1
            if self.div_detail == True:
                self.div_detail_layer += 1

    def end_div(self):
        if self.div_year == True:
            self.div_year = False
            return
        if self.div_detail == True:
            self.div_detail_layer -= 1
            if self.div_detail_layer == 0:
                self.div_detail = False

    def start_a(self,attrs):
        if self.div_year == True:
            for k, v in attrs:
                if k == 'class' and v == 'select_ctr':
                    self.a_year = False
                    return
            self.a_year = True

    def end_a(self):
        self.a_year = False
    
    def start_span(self, attrs):
        if self.div_detail == False:
            return
        for k, v in attrs:
            if k == 'class' and v == 'key':
                self.span_key = True
                self.key_count = 1
            if k == 'class' and v == 'value':
                self.span_value = True

    def end_span(self):
        self.span_key = False
        self.span_value = False

    def handle_data(self,data):
        if self.a_year == True:
            #print data
            self.year_list.append(data)
            self.year_info[data] = []
        if self.span_key == True:
            self.key = data.strip()
        if self.span_value == True:
            #self.key_value.append(self.key + data.strip())
            data_strs = data.strip().split('\t')
            data_str = ''
            for item in data_strs:
                data_str += item.strip()
            if self.key_count != 1:
                self.year_info[self.year_list[(self.div_detail_true_count+1)/2-1]].append(data_str.strip())
            else:
                self.year_info[self.year_list[(self.div_detail_true_count+1)/2-1]].append(',' + self.key + data_str.strip())
                self.key_count = 0

        if self.div_detail_true_count > 0 and self.div_detail_true_count % 2 == 0 and self.div_detail == False:
            temp = self.key_value
            #self.year_info[self.year_list[self.div_detail_true_count/2-1]] = temp
            #self.key_value.clear()
            
            
        
        
def get_page_content():

    car_info = {}

    
    URL = 'http://product.auto.163.com/'
    #main_page_analysis
    main_page_URL = 'http://product.auto.163.com/brand/'
    request = urllib2.Request(main_page_URL)
    response = urllib2.urlopen(request)
 
    main_page = response.read()
    main_page_analysis = MainPageAnalysis()
    main_page_analysis.feed(main_page)

    #print main_page_analysis.data_url

    for k, v in main_page_analysis.data_url.items():
        print k
        sub_URL = URL + v
        request = urllib2.Request(sub_URL)
        response = urllib2.urlopen(request)
     
        sub_page = response.read()
        sub_page_analysis = SubPageAnalysis()
        sub_page_analysis.feed(sub_page)

        car_info[k] = sub_page_analysis.ghd_gbd
        #print sub1_page_analysis.ghd_gbd

    flag = False
    print 'write car_infomation'
    fo = open('car_infomation_by_kkun', 'wb')
    for k1, v1 in car_info.items():
        if k1 == 'M':
            flag = True
        if k1 == 'T':
            flag = False
        if flag == False:
            continue
        for k2, v2 in v1.items():
            for k3, v3 in v2.items():
                print k1, k2, k3
                sub_sub_URL = URL + v3
                request = urllib2.Request(sub_sub_URL)
                response = urllib2.urlopen(request)
             
                sub_sub_page = response.read()
                sub_sub_page_analysis = SubSubPageAnalysis()
                sub_sub_page_analysis.feed(sub_sub_page)

                for k_s, v_s in sub_sub_page_analysis.year_info.items():
                    fo.write(str(k1)+','+str(k2)+','+str(k3)+','+str(k_s))
                    for item in v_s:
                        fo.write(str(item).replace(' ', ''))
                    fo.write('\n')
                    fo.flush()
    fo.close()
    
                


if __name__ == '__main__':
    get_page_content()

    '''
    sub_sub_page_URL = 'http://product.auto.163.com/series/1953.html#CX001'
    request = urllib2.Request(sub_sub_page_URL)
    response = urllib2.urlopen(request)
 
    sub_sub_page = response.read()
    sub_sub_page_analysis = SubSubPageAnalysis()
    sub_sub_page_analysis.feed(sub_sub_page)

    #print sub_sub_page_analysis.year_info
    fo = open('subsub', 'wb')
    for k, v in sub_sub_page_analysis.year_info.items():
        fo.write(str(k))
        for item in v:
            fo.write(str(item).replace(' ', ''))
        fo.write('\n')
    fo.close()
    '''
    
