import random
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register

@register("lottery", "Your Name", "一个简单的抓阄插件", "1.0.0", "repo url")
class LotteryPlugin(Star):
    @filter.command("抓阄")
    async def lottery(self, event: AstrMessageEvent):
        '''从提供的名字中随机抽取一个'''
        # 获取用户输入的名字字符串（去除/抓阄指令部分）
        message_str = event.message_str.strip("/抓阄").strip()
        
        # 检查输入的名字是否为空
        if not message_str:
            yield event.plain_result("请提供至少一个名字，用逗号分隔。")
            return

        # 将输入的名字按逗号分隔，去除多余空格
        names = [name.strip() for name in message_str.split(",")]

        # 检查是否至少有两个名字
        if len(names) < 2:
            yield event.plain_result("请至少提供两个名字进行抓阄。")
            return

        # 随机选择一个名字
        selected_name = random.choice(names)

        # 返回结果
        yield event.plain_result(f"抓阄结果是：{selected_name}")
