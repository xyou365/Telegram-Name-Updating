# Telegram-Name-Updating

Update (first/last/user) name of Telegram user every 10 seconds. 

参考文档：<a href="https://telethon.readthedocs.io/en/stable/">Telethon</a>

lastname实时更新效果：<a href="https://t.me/CodyDoby">Cody</a>

## 0. 准备

运行环境：VPS，python3，python3-pip

创建应用：<a href="https://my.telegram.org/">https://my.telegram.org/</a>。只要填App title和Short name即可。获得api_id和api_hash。

## 1. 在VPS上安装 telethon

<code>pip3 install telethon</code>

## 2. 下载并运行Demo脚本</strong>（第一次发布scipt，写的不好不要拍死我）

<code>wget https://raw.githubusercontent.com/xyou365/Telegram-Name-Updating/master/tg_username_update.py</code>

<code>python3 tg_username_update.py</code>

## 3. api认证和用户登陆

第根据提示输入api_id和api_hash。接着输入手机号和验证码，如果账号开启了二次验，证根据提示再输入二次验证的密码。最后看到 It works! 表明成功了。 默认的是每10秒钟按照一定概率更新一次lastname到特定模式。

欢迎<a href="https://www.gfan.loan/we-are-google-fans/">加入我们</a>。
