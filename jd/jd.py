# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/12/23 22:24'

import time
from  multiprocessing.dummy import Pool as ThreadPool
import sys
import requests
from lxml import etree  #数据解析库
import json

def get_response(url):
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    product_list = selector.xpath('//*[@id="J_goodsList"]/ul/li')
    for product in product_list:
        try:
            sku_id = product.xpath('@data-sku')[0]
            product_url = 'https://item.jd.com/{}.html'.format(str(sku_id))
            get_data(product_url)
        except Exception as e:
            print(e)


def get_data(product_url):
    '''
    获取商品的详情页
    :param url:
    :return:
    '''
    product_dict = {}
    html = requests.get(product_url,headers=headers)
    selector = etree.HTML(html.text)
    product_infos = selector.xpath('//ul[@class="parameter2 p-parameter-list"]')
    for product in product_infos:
        product_number = product.xpath('li[2]/@title')[0]
        product_prict = get_product_price(product_number)

        product_dict['商品名称'] = product.xpath('li[1]/@title')[0]
        product_dict['商品ID'] = product_number
        product_dict['商品产地'] = product.xpath('li[4]/@title')[0]
        product_dict['系统类型'] = product.xpath('li[5]/@title')[0]
        product_dict['商品价格'] = product_prict
    print(product_dict)


def get_product_price(sku):
    '''
    获取价格
    :param sku:
    :return:
    '''
    price_url ='https://p.3.cn/prices/mgets?&skuIds=J_{}'.format(str(sku))
    response = requests.get(price_url,headers=headers).content
    response_json = json.loads(response.decode())
    for info in response_json:
        return info.get('p')


def save(product_list):
    '''
    保存数据
    :param list:
    :return:
    '''
    # client = pymongo.MongoClient('localhost')
    # db = client['product_dict']
    # content = db['jd']
    # content.insert(product_list)


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }
    urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page={}&s=1&click=0'.format(page) for page in range(1,10)]
    pool = ThreadPool(10)
    start_time = time.time()
    pool.map(get_response,urls)
    pool.close()
    pool.join()
    end_time = time.time()
    print('用时{}秒'.format(str(end_time - start_time)))

