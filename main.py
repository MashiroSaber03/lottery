from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("repeater", "Your Name", "一个带开关的复读机插件(群组/私聊隔离)", "1.0.0", "repo url")
class RepeaterPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.repeater_enabled = {}  # 使用字典存储每个会话的开关状态

    @filter.command("repeat_on")
    async def repeat_on(self, event: AstrMessageEvent):
        """开启复读模式"""
        self.repeater_enabled[event.session_id] = True
        yield event.plain_result("复读模式已开启")

    @filter.command("repeat_off")
    async def repeat_off(self, event: AstrMessageEvent):
        """关闭复读模式"""
        self.repeater_enabled[event.session_id] = False
        yield event.plain_result("复读模式已关闭")

    @filter.command("repeat_status")
    async def repeat_status(self, event: AstrMessageEvent):
        """查看复读模式状态"""
        status = self.repeater_enabled.get(event.session_id, False)  # 获取当前会话状态, 默认为False
        status_text = "开启" if status else "关闭"
        yield event.plain_result(f"当前复读模式: {status_text}")

    @filter.message()
    async def repeat_message(self, event: AstrMessageEvent):
        """复读收到的消息（受开关控制）"""
        if event.is_from_self():
            return

        # 检查当前会话的复读模式是否开启。 如果session_id 不在字典中，get方法返回默认值False
        if self.repeater_enabled.get(event.session_id, False):
            message_str = event.message_str
            if message_str:
                yield event.result(event.message_obj.message)
