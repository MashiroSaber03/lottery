from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register

@register("repeater", "mash", "一个带开关的复读插件", "1.0.0", "repo url")
class EchoPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.echo_enabled = False  # 默认关闭复读模式

    @filter.command("echobot")
    async def echobot(self, event: AstrMessageEvent):
        '''切换复读模式'''
        self.echo_enabled = not self.echo_enabled
        status = "开启" if self.echo_enabled else "关闭"
        yield event.plain_result(f"复读模式已{status}。")

    @filter.command("echo")
    async def echo(self, event: AstrMessageEvent, message: str):
        '''复读指令'''
        if self.echo_enabled:
            yield event.plain_result(f"你说：{message}")
        else:
            yield event.plain_result("复读模式已关闭，无法复读。")

