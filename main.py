from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register

@register("repeater", "Your Name", "一个简单的复读机插件", "1.0.0", "repo url")
class RepeaterPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.enabled = True  # 设置插件启用状态，True 表示启用，False 表示禁用

    @filter.command("repeat")
    async def repeat(self, event: AstrMessageEvent):
        '''这是一个复读机指令'''
        if not self.enabled:
            return  # 如果插件被禁用，直接返回，不执行后续代码

        user_name = event.get_sender_name()
        message_str = event.message_str  # 获取消息的纯文本内容
        yield event.plain_result(f"{user_name} 说: {message_str}")

    @filter.command("toggle")
    async def toggle(self, event: AstrMessageEvent):
        '''切换复读机插件的启用状态'''
        self.enabled = not self.enabled
        status = "启用" if self.enabled else "禁用"
        yield event.plain_result(f"复读机插件已{status}。")
