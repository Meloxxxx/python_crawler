import os
from bs4 import BeautifulSoup
import requests
from rich.console import Console

def load_page(page_url, headers):

    def img_bag_analysis(html):
        bs = BeautifulSoup(html, 'lxml')
        bag_list = bs.find_all(name='li', attrs={'class': 'i_list list_n2'})
        bags_dict = dict()
        for item in bag_list:
            img_href = item.find(name='a').get('href')
            img_text = item.find(name='div', attrs={'class': 'meta-title'}).text.split(' ')[0]
            bags_dict[img_text] = img_href
        return bags_dict

    page_content = requests.get(url=page_url, headers=headers).text
    return img_bag_analysis(page_content), page_content

def get_ins_page(root_url, ins_url, headers):
    html = requests.get(url=root_url+ins_url, headers=headers).text
    bs = BeautifulSoup(html, 'lxml')
    page_analysis = bs.find_all(name='div', attrs={'class': 'page'})[0]
    # 获取当前页面页码：
    current_page = page_analysis.find(name='a', attrs={'class': 'current'}).text
    # 所有页面的url连接列表：
    p_url = []
    for p in page_analysis.find_all(name='a'):
        p_url.append(p.get('href'))
    # 把所有页面装载好之后，判断能否进行翻页操作
    return p_url

def get_person_page(root_url, person_url, headers):
    # 所传进来的person_url是一个url列表
    all_urls = []
    for single_url in person_url:
        html = requests.get(url=root_url+single_url, headers=headers).text
        bs = BeautifulSoup(html, 'lxml')
        page_analysis = bs.find_all(name='div', attrs={'class': 'page'})
        if len(page_analysis) != 0:
            page_analysis = page_analysis[0]
            # 获取所有页面的url链接
            for p in page_analysis.find_all(name='a'):
                all_urls.append(p.get('href'))
        else:
            all_urls.append(single_url)
    return all_urls

def search_img(html):
    bs = BeautifulSoup(html, 'lxml')
    imgs_list = bs.find(name='div', attrs={'class': 'content_left'})
    imgs_list = [img.get('src') for img in imgs_list.find_all(name='img')]
    return imgs_list

def download_img(img_url, headers, current_url, path):
    headers['Referer'] = current_url
    # 请求图片：
    img_binary = requests.get(url=img_url, headers=headers).content
    # 截取图片的名称：
    img_name = img_url.split('/')[-1]
    # 写入存储图片：
    with open(os.path.join(path, img_name), 'wb') as f:
        f.write(img_binary)

def bag_page_counting(html):
    bs = BeautifulSoup(html, 'lxml')
    p = bs.find(name='div', attrs={'class': 'page'})
    page_list = [page.get('href') for page in p.find_all(name='a')]
    page_nums = len(set(page_list))
    return page_nums

def progress_bar(index, length):
    scale = length
    moving_bar = '=' * index
    total_bar = '-' * (scale - index)
    percentage = (index / scale) * 100.0
    state = '爬取中...' if index != scale else '爬取完成！'
    print("\r{:^3.0f}% [{} > {}] {state}".format(percentage,
                                                 moving_bar,
                                                 total_bar,
                                                 state=state), end=' ')
    if index == scale: print("\n\n")

def print_page(content_links, hints):
    def isSingle(index):
        if index < 10:
            return ' '+str(index)
        else:
            return str(index)
    # 所传输的参数content_links为字典类型数据结构：
    console = Console(width=90)
    console.rule(hints)
    for index, key in enumerate(content_links.keys()):
        # 长度补全：
        new_key = ('【'+key+'】').ljust(12, "－")
        if index % 3 == 0 or index % 3 == 1:
            if index == len(content_links) - 1:
                print(new_key, isSingle(index))
            else:
                print(new_key, isSingle(index), end="  |  ")
        else:
            print(new_key, isSingle(index))
    console.rule()

def isTurnable(turn, current_page, total_page):
    if turn == 'u':
        if current_page > 1:
            return True
        else:
            return False
    else:
        if current_page < total_page:
            return True
        else:
            return False

