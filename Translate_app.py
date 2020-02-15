# coding = "utf-8
import requests
import json


# query_str = sys.argv[1]
class YouDaoTranslate:
    def __init__(self):
        self.keep_active = True
        self.acture_mod = False
        self.language_code_dict = {"1": "ZH_CN2EN", "2": "ZH_CN2JA", "3": "ZH_CN2KR", "4": "ZH_CN2FR",
                                   "5": "ZH_CN2RU", "6": "ZH_CN2SP",
                                   "7": "EN2ZH_CN", "8": "JA2ZH_CN", "9": "KR2ZH_CN", "10": "FR2ZH_CN",
                                   "11": "RU2ZH_CN", "12": "SP2ZH_CN"}
        self.language_code_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        print("输入“帮助”或者“help”了解更多信息")

    # 获取帮助信息
    def get_help_msg(self):
        print("1.输入“切换翻译模式” --> 重新选择翻译模式")
        print("2.输入“翻转翻译” --> 切换翻译的源和目标语言")
        print("3.输入“结束”或者“exit” --> “退出翻译”")

    # 选择翻译模式
    def start(self):
        self.language_code = input("请选择翻译模式：1-> 中英； 2-> 中日； 3-> 中韩； 4-> 中法； 5-> 中俄； 6-> 中西；"
                                   "7-> 英中； 8-> 日中； 9-> 韩中； 10-> 俄中； 11-> 西中 ：")
        # 输入正确的翻译方式
        if self.language_code in self.language_code_list:
            print("language_code = ", self.language_code_dict[self.language_code])
            self.type = self.language_code_dict[self.language_code]
            self.acture_mod = True
            # 获取实际翻译类型索引
            self.real_code_index = list(self.language_code_dict.keys()).index(self.language_code)
        # 输入的不是正确的翻译模式
        else:
            self.type = self.language_code
            # 查看帮助
            if self.type == "help" or self.type == "帮助":
                self.get_help_msg()
            elif self.type == "结束" or self.type == "exit":
                print("退出翻译！", self.type)
                exit()
            else:
                print("输入有误，请重新输入！")
            # 进入死循环，除非输入正确的翻译模式或者退出翻译
            while (self.acture_mod == False):
                code = input("请选择翻译模式：1-> 中英； 2-> 中日； 3-> 中韩； 4-> 中法； 5-> 中俄； 6-> 中西；"
                             "7-> 英中； 8-> 日中； 9-> 韩中； 10-> 俄中； 11-> 西中 ：")
                # 得到正确的翻译模式
                if code in self.language_code_list:
                    self.type = self.language_code_dict[code]
                    self.acture_mod = True
                # 退出翻译
                elif code == "结束" or code == "exit":
                    self.acture_mod = True
                    print("退出翻译！", code)
                    exit()
                # 继续循环
                else:
                    print("输入有误,清重新输入")

    # 翻译过程处理
    def process(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36"}
        post_data = {
            'i': self.trans_content,
            # 'type': 'AUTO',
            'type': self.type,
            # 'from': 'zh',
            # 'to': 'en',
            'smartresult': 'dict',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME'
        }
        post_url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        r = requests.post(post_url, data=post_data, headers=headers)
        dict_ret = json.loads(r.content.decode())
        ret = dict_ret["translateResult"][0][0]["tgt"]
        print("翻译结果为：", ret)

    # 翻转翻译类型
    def reverse_trans(self):
        if self.real_code_index < 6:
            self.real_code_index = self.real_code_index + 6
        else:
            self.real_code_index = self.real_code_index - 6
        self.type = self.language_code_dict[self.language_code_list[self.real_code_index]]
        print("翻转后的翻译模式为：", self.type)

    def run(self):
        while self.keep_active:
            self.trans_content = input("请输入要翻译的内容：")
            # 判断输入的内容
            if self.trans_content == "帮助" or self.trans_content == "help":
                # 获取帮助信息
                self.get_help_msg()
            elif self.trans_content == "结束" or self.trans_content == "exit":
                # 退出翻译
                self.keep_active = False
                print("退出翻译！", self.trans_content)
                exit
            elif self.trans_content == "切换翻译模式":
                # 切换翻译模式
                self.start()
            elif self.trans_content == "翻转翻译":
                # 翻转翻译模式
                self.reverse_trans()
            else:
                # 开始翻译
                self.process()


if __name__ == '__main__':
    #    str = sys.argv[1]
    translate = YouDaoTranslate()
    translate.start()
    translate.run()
