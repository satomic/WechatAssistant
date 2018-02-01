这个MD格式的文本其实是包含格式的，当前先不管格式了。有时间再弄吧

requirements:
    python3.5
    pip install wxpy

get start:
    python3原生执行
        python3 main.py nickname (这里的nickname是可以任意指定的，并不一定要是微信名，但是这个值会跟微信登录信息绑定)
    windows: 点击windows_start.bat
    linux:   点击linux_start.sh

启动起来如下画面

![avatar](https://raw.githubusercontent.com/satomic/WechatAssistant/master/started.png)

=======================================
原始：
1. 目标用户的搜索与收集
	1.1 自动拉好友入群（自动后台摇朋友？？）
	1.2 群发消息
	1.3 群内文件的快速查找……分类？？？
	1.4 好友申请设置时间自动通过

2. 朋友圈/公众号  简易编辑界面，争取一条龙服务，操作更简便

3. 友情提醒操作流程？？？

4. 自动对话/聊天

=============================
整理：
1. 好友请求时
    1) 自动同意请求
    2) 发送问候信息，以及基本的操作模式
        操作模式：
            * 专业咨询模式，根据tree结构匹配用户请求
            * 自由模式，由图灵机器人自动回复

2. 保留字
    1) “帮助”
    2) “模式切换”

3. 每个人的数据独立存储
    数据存储的方式

4. 脚本操作
    接收特定指令，可以由python执行

5. python3下的log系统（完成）
    基础能力

6. license系统




