from pkg.plugin.context import register, handler, BasePlugin, APIHost, EventContext
from pkg.plugin.events import NormalMessageResponded
from mirai import Image, MessageChain
import random
import httpx
import logging
import re


# 注册插件
@register(name="emoticon", description="在线智能表情包插件", version="1.0", author="Pevernow")
class HelloPlugin(BasePlugin):

    def __init__(self, host: APIHost):
        self.token = 'YOUR_TOKEN'  # 请将这里的'YOUR_TOKEN'替换为你实际获取的token
        self.logger = logging.getLogger(__name__)

    # 当收到GPT接口回复时触发
    @handler(NormalMessageResponded)
    async def normal_message_responded(self, ctx: EventContext, **kwargs):
        response_text = ctx.event.response_text

        # 更宽松的正则表达式，支持多语言字符
        EMOTICON_PATTERN = re.compile(r':(.{1,10}):')

        ma = EMOTICON_PATTERN.search(response_text)
        if ma:
            emotion = ma.group()[1:-1]
            self.logger.info(emotion)

            # 使用API获取表情包
            url = await self.get_random_emoticon(emotion)
            if url:
                await ctx.event.query.adapter.reply_message(ctx.event.query.message_event,MessageChain([Image(url=url)]),False)
            else:
                self.logger.warning('没有找到相关表情包')

            #无论如何都要删掉表情包转义符，即使没有找到
            ctx.add_return("reply", [response_text.replace(ma.group(), '')])

    # 使用API获取随机表情包
    async def get_random_emoticon(self, keyword):
        url = 'https://v2.alapi.cn/api/doutu'
        params = {
            'token': self.token,
            'keyword': keyword,
            'page': 1,  # 默认从第一页开始
            'type': 7,  # 表情包来源
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()

        data = response.json()['data']
        if data:
            random_emoticon = random.choice(data)
            return random_emoticon
        else:
            return None

    # 插件卸载时触发
    def __del__(self):
        pass
