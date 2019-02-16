# -*- coding: utf-8 -*-

from wox import Wox,WoxAPI
import json
import webbrowser
# from pypinyin import Style, pinyin, load_phrases_dict

class TipsOpen(Wox):

    def query(self, query):
        results = []
        kw = query.split(" ")

        app = kw[0]
        word = ""
        if len(kw) >1 :
            word = kw[1]
        with open("config.json", "r", encoding="utf-8") as f1:
            data = ""
            a = json.load(f1, encoding="utf-8")
            if not app in a.keys():
                for key in a.keys():
                    if key.lower().find(app.lower()) != -1 or app == '':
                        config = {
                            "Title": "配置项(直接打开):" + key,
                            "SubTitle": "",
                            "IcoPath":"Images/app.ico",
                            "JsonRPCAction": {
                                "method": "openUrl",
                                "parameters": [key],
                                "dontHideAfterAction": False
                            }
                        }
                        if "ids" in a[key].keys():
                            config["Title"] = "配置项:" + key
                            config["JsonRPCAction"]['dontHideAfterAction'] = True
                        results.append(config)
                return results

            for x in a[app]['ids'].keys():
                # 首字母拼音搜索,字母和符号会原样保留,性能太差，后续有需要再优化
                # py = ""
                # if a[app]["needPy"]:
                #     for y in pinyin(x,style=Style.FIRST_LETTER):
                #         py += str(y[0])
                if word == '' or x.lower().find(word.lower()) != -1 :
                    desc = app
                    if "desc" in a[app].keys():
                        desc = a[app]['desc']
                    results.append({
                        "Title": "{}:{}".format(desc, x),
                        "SubTitle": "",
                        "IcoPath":"Images/app.ico",
                        "JsonRPCAction": {
                            "method": "openUrl",
                            "parameters": [app, x],
                            "dontHideAfterAction": False
                        }
                    })
            return results

    # 打开别名对应的页面
    def openUrl(self, app="", appid=""):
        if app == '':
            return

        with open("config.json", "r", encoding="utf-8") as f1:
            a = json.load(f1)
            if not app in a.keys():
                return "未找到相应的项目"

            url = a[app]['url']
            if not "ids" in a[app].keys():
                webbrowser.open(url)
                return
            app = a[app]['ids'][appid]
            url = url.replace("#id#", str(app))
            webbrowser.open(url)

if __name__ == "__main__":
    TipsOpen()