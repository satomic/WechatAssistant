requirements:
----------------
```
    python3.5
    pip install wxpy
```
get start:
----------------
* python3原生执行
    * python3 main.py nickname  注：这里的nickname是可以任意指定的，并不一定要是微信名，但是这个值会跟微信登录信息绑定)
* windows: 双击 windows_start.bat
* linux:   双击 linux_start.sh

启动画面
----------------
![avatar](https://raw.githubusercontent.com/satomic/WechatAssistant/master/started.png)

---

原始idea
----------------
* 目标用户的搜索与收集
    * 自动拉好友入群（自动后台摇朋友？？）
    * 群发消息
    * 群内文件的快速查找……分类？？？
    * 好友申请设置时间自动通过
* 朋友圈/公众号  简易编辑界面，争取一条龙服务，操作更简便

* 友情提醒操作流程？？？

* 自动对话/聊天

---


整理后
----------------

* 好友请求时
    * 自动同意请求
    * 发送问候信息，以及基本的操作模式
        * 操作模式：
            * 专业咨询模式，根据tree结构匹配用户请求
            * 自由模式，由图灵机器人自动回复
* 保留字
    * “帮助”
    * “模式切换”
* 每个人的数据独立存储
    * 数据存储的方式: 根据用户启动时输入的nickname绑定信息，在pkls文件夹中创建nickname为名字的文件夹。用来存储于用户相关的pkl数据。可以使用户不用每次都扫码登录。
      
* 脚本操作
    * 接收特定指令，可以由python执行
* python3下的log系统（完成）
    * 基础能力
* unittest framework
    * 支持加载全局testcase
    * 结构与代码结构保持一致
* license系统
* exe打包 pyinstaller
* 外部特殊功能加载


bug
---
* 单独跑testcase报错，加载class失败问题
* 单独跑testcase，明明python interpretor选择的是3.5版本，却依旧是调用2.7版本




