import yaml
from utils import *
from control_utils import *

class Meirentu:
    def __init__(self):
        self.root_net = 'https://meirentu.top'

        # 直接将各机构图片地址加载到内存中：
        with open('girls.yaml', 'r', encoding='utf-8') as f:
            self.ins_links = yaml.load(f, Loader=yaml.SafeLoader)

        # 将人物的各自链接加载到内查中：
        with open('models.yaml', 'r', encoding='utf-8') as f:
            self.models = yaml.load(f, Loader=yaml.SafeLoader)
        # 构建请求头：
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/110.0.0.0 Safari/537.36',
                        'Referer': ''}

    def institute_clawer(self):
        while True:
            # 选择机构爬取：
            ins_list = list(self.ins_links)
            print_page(self.ins_links, '机构链接')
            # 在此添加一个循环卡住代码：
            choice_list = set([str(n) for n in range(len(ins_list))])

            choice = str(input('请输入选择(q->退出, 序号->选择图包):'))
            if choice in choice_list:
                print("所选择选项为:", '【'+ins_list[int(choice)] +'】')
                ins_name = str(ins_list[int(choice)])
                ins_url = self.ins_links[ins_name]
                with Context(text='正在加载页面...', finish_text='加载完成!'):
                    all_ins_url = get_ins_page(root_url=self.root_net,
                                               ins_url=ins_url,
                                               headers=self.headers)
                # 统计页数，循环展示：
                current_page = 1
                current_ins_url = all_ins_url[current_page-1]
                self._contol_block(ins_or_person_name=ins_name, ins_or_person_url=current_ins_url,
                                   current_page=current_page, p_url=all_ins_url)
            elif choice == 'q':
                with Context(text="正在退出...", finish_text='退出成功!'):
                    time.sleep(2)
                time.sleep(1)
                break
            else:
                print('无效输入！请重新输入选择!')

    def person_clawer(self):
        while True:
            # 选择人爬取：
            person_list = list(self.models)
            print_page(self.models, '福利姬链接')
            # 在此添加一个控制选择的循环卡住代码：
            choice_list = set([str(n) for n in range(len(person_list))])

            choice = str(input('--请输入选择:'))
            if choice in choice_list:
                print("--所选择选项为:", '【'+person_list[int(choice)]+'】')
                person_name = str(person_list[int(choice)])
                person_url = self.models[person_name]
                with Context(text='--正在加载页面...', finish_text='--加载完成!'):
                    all_person_url = get_person_page(root_url=self.root_net,
                                                     person_url=person_url,
                                                     headers=self.headers)
                # 统计页数，循环展示：
                current_page = 1
                per_url = all_person_url[current_page - 1]

                self._contol_block(ins_or_person_url=per_url, ins_or_person_name=person_name,
                                   current_page=current_page, p_url=all_person_url)
            elif choice == 'q':
                with Context(text="--正在退出...", finish_text='--退出成功!'):
                    time.sleep(2)
                time.sleep(1)
                break
            else:
                print('--无效输入！请重新输入选择!')

    def _print_page(self, page_dict, current_page, total_pages):
        console = Console(width=107)
        # 传进来的参数是机构图页面的字典形式的数据结构
        # 格式为{图包名：图包连接}
        img_bag_name_list = list(page_dict)
        print('\n----图包页面内容:')
        console.rule('页面显示第'+str(current_page)+'/'+str(total_pages)+'页')
        for index, img_bag in enumerate(img_bag_name_list):
            if index % 2 == 0:
                if index == len(img_bag_name_list) - 1:
                    print(('【'+img_bag+'】').ljust(33, "-") + str(index))
                else:
                    print(('【'+img_bag+'】').ljust(33, "-") + str(index), end=" ")
            else:
                print(('【'+img_bag+'】').ljust(33, "-")+str(index))
        console.rule()

    def _claw_img_bag(self, img_bag_url, ins_name, bag_name):
        # 使用bs4获取当前页面图片的连接：
        with Context(text='----正在加载图包...', finish_text='----加载完成!'):
            img_bag_html = requests.get(url=img_bag_url, headers=self.headers).text
            img_list_fp = search_img(img_bag_html)
            # 先获取该图包有几页
            page_nums = bag_page_counting(img_bag_html)
        time.sleep(1)
        # 图片下载前先检查文件夹是否存在：
        with Context(text='----文件夹路径检查中...', finish_text='----检查完成!'):
            if not os.path.exists(path=os.path.join('Meirentu', ins_name)):
                os.mkdir(path=os.path.join('Meirentu', ins_name))
            # 再进一步检查是否存在
            if not os.path.exists(path=os.path.join('Meirentu', ins_name, bag_name)):
                os.mkdir(path=os.path.join('Meirentu', ins_name, bag_name))
            time.sleep(2)

        # 完成文件夹创建后即可开始下载图片：
        time.sleep(2)
        for p in range(1, page_nums+1):
            # 加载进度条：
            progress_bar(p, page_nums)
            if p == 0:
                time.sleep(1)
                continue
            img_page_url = img_bag_url[:-5] + '-' + str(p) + img_bag_url[-5:]
            if p == 1:
                for img_fp in img_list_fp:
                    download_img(img_fp, self.headers, img_page_url,
                                 os.path.join('Meirentu', ins_name, bag_name))
                    time.sleep(0)

            img_page_html = requests.get(url=img_page_url, headers=self.headers).text
            img_list = search_img(img_page_html)
            for img in img_list:
                download_img(img, self.headers, img_page_url,
                             os.path.join('Meirentu', ins_name, bag_name))
                time.sleep(0)

    def _contol_block(self, ins_or_person_url, ins_or_person_name, current_page, p_url):
        while True:
            # 加载当前的机构图页面：
            isBreak = False
            ins_page_dict, page_html = load_page(page_url=self.root_net+ins_or_person_url, headers=self.headers)
            ins_list = list(ins_page_dict)
            self._print_page(page_dict=ins_page_dict,
                             current_page=current_page,
                             total_pages=len(p_url))
            choice_range = set([str(n) for n in range(len(ins_page_dict))])
            while True:
                choice_for_img_bag = str(input('----请输入需要爬取的图包连接(q->退出, u->向上翻页, d->向下翻页):'))
                if choice_for_img_bag in choice_range:
                    # 开始爬取相应的图包：
                    img_bag_url = ins_page_dict.get(ins_list[int(choice_for_img_bag)])
                    self._claw_img_bag(img_bag_url=self.root_net+img_bag_url,
                                       ins_name=ins_or_person_name, bag_name=ins_list[int(choice_for_img_bag)])

                elif choice_for_img_bag == 'q':
                    print('----已选择退出...')
                    isBreak = True
                    break
                elif choice_for_img_bag == 'u' or choice_for_img_bag == 'd':
                    # 进行翻页操作：
                    if choice_for_img_bag == 'u':
                        if isTurnable(turn='u', current_page=current_page, total_page=len(p_url)):
                            ins_or_person_url = p_url[current_page-2]
                            current_page -= 1
                            break
                        else:
                            print('----当前已经是第一页!')
                    else:
                        if isTurnable(turn='d', current_page=current_page, total_page=len(p_url)):
                            ins_or_person_url = p_url[current_page]
                            current_page += 1
                            break
                        else:
                            print('----当前已经是最后一页!')
                else:
                    print('----无效输入!请重新输入选择!')
            if isBreak:
                print('----退出成功!返回上一级选择...')
                break
