# QChatGPT Plugin Emoticon v3
QChatGPT v3可用，基于在线api的表情包插件。

## 效果图
![示例图片](https://github.com/Pevernow/QChatGPT_Plugin_Emoticon_v3/assets/29888010/0b950881-3638-4bd6-8c28-52c91784eca1)


## API获取

使用的api目前是是免费的

前往https://www.alapi.cn/注册

在控制面板左侧——接口管理——更新Token密钥，点击Copy复制Token

## 配置插件

在本插件文件夹下main.py文件中找到这行，并替换成你获取到的token（不要弄丢引号）

```
self.token = 'YOURTOKEN'  # 请将这里的'YOUR_TOKEN'替换为你实际获取的token
```

## 配置GPT

你可以自行选择使用场景模式（我个人是没用）或直接通过QQ内对话命令GPT。
反正只要告诉GPT如何使用此功能就对了。

提示词举例：

```
你可以用文字方式发送表情包，用来表达你现在的心情，看法或者玩梗。
你只需要将代表表情包含义的简单中文短语写入两个英文引号直接即可。
例如
:开心:
表示发送一个开心的表情包。
```

## 关于Fork

本项目几乎重写了90%以上的代码了，约等于重头写起，就不用Fork了。

