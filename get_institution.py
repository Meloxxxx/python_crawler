import re
from bs4 import BeautifulSoup
import requests
import yaml

girls_diction = {'周于希': ['/model/周于希.html'], '鱼子酱': ['/model/鱼子酱.html'], '绮里嘉': ['/model/绮里嘉.html', '/model/Carina梦绮.html'],
                 '熊小诺': ['/model/熊小诺.html'], '王馨瑶': ['/model/王馨瑶.html'], '婠婠么': ['/model/婠婠么.html'],
                 '程程程': ['/model/程程程.html'], '小果冻儿': ['/model/小果冻儿.html'], '林星阑': ['/model/林星阑.html'],
                 '玥儿玥': ['/model/玥儿玥.html'], '唐琪儿': ['/model/唐琪儿.html'], '林子欣': ['/model/林子欣.html'],
                 '韩静安': ['/model/韩静安.html'], '杨晨晨': ['/model/杨晨晨.html'], '绯月樱': ['/model/绯月樱.html'],
                 '梦心玥': ['/model/梦心玥.html', '/model/梦心月.html'], '尹甜甜': ['/model/尹甜甜.html'], '豆瓣酱': ['/model/豆瓣酱.html'],
                 '陆萱萱': ['/model/陆萱萱.html'], '林子遥': ['/model/林子遥.html'], '赵小米': ['/model/赵小米.html'],
                 '阿朱': ['/model/就是阿朱啊.html'], '林乐一': ['/model/林乐一.html'], '言沫': ['/model/言沫.html'],
                 '郑颖姗': ['/model/郑颖姗.html'], '尹菲': ['/model/尹菲.html', '/model/顾奈奈酱.html', '/model/顾奈奈.html'],
                 '利世': ['/model/利世.html', '/model/抖娘利世.html'],
                 '李可可': ['/model/李可可.html'], '一颗甜蛋黄': ['/model/一颗甜蛋黄.html'], '朱可儿': ['/model/朱可儿.html'],
                 '徐莉芝': ['/model/徐莉芝.html', '/model/芝芝Booty.html'], '甜仔': ['/model/甜仔.html'],
                 '唐安琪': ['/model/唐安琪.html'], '王雨纯': ['/model/王雨纯.html'], '张思允': ['/model/张思允.html'],
                 '冯木木': ['/model/冯木木.html']}


with open('models.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(girls_diction, f, allow_unicode=True)