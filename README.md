# Wox.Plugin.AliasOpen
一个Wox插件，可以方便地打开搜索配置文件类的网址

个人使用需要编辑插件内的config.json文件：
```
{
  "gamersky": {    // 插件输入的一级关键字，一般为简单的缩写便于快速输入
    "url": "http://www.gamersky.com/#id#",  // 插件对应的Url地址，  #id#为模板变量 需要替换
    "desc": "游民星空", // 网址描述
    "ids": {  // 二级分类， 用于二级搜索
      "趣味": "ent/qw/",    // key用来展示及搜索， value替换url内的#id#模板
      "壁纸": "ent/wp/"
    }
  },
  // 这里是不需要二级分类的配置写法
  "bili": {
  	"url": "https://space.bilibili.com/9052944/",
  	"desc": "哔哩哔哩动画"
  }
}
```
