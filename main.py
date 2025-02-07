from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register

@register("repeater", "Your Name", "一个简单的复读机插件", "1.0.0", "repo url")
class RepeaterPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.enabled = False  # 插件默认禁用

    @filter.command("repeat")
    async def repeat(self, event: AstrMessageEvent):
        '''切换复读机的启用/禁用状态'''
        if not self.enabled:
            self.enabled = True
            yield event.plain_result("复读机插件已启用。现在我将复读您的消息。")
        else:
            self.enabled = False
            yield event.plain_result("复读机插件已禁用。")

    @filter.event(AstrMessageEvent)
    async def on_message(self, event: AstrMessageEvent):
        '''如果复读功能启用，复读用户消息'''
        if self.enabled:
            message_str = event.message_str
            user_name = event.get_sender_name()
            yield event.plain_result(f"{user_name} 说: {message_str}")
