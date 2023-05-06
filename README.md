# ArknightsStoryConverter
将PRTS上的剧情数据转换为可读性更强的纯文本数据
附赠一个简易gui

用于打印可读文本
###原始数据示例
```
{{剧情模拟器|图片数据={{Widget:Data_Image}}|角色数据={{Widget:Data_Char}}|音频数据={{Widget:Data_Audio}}|文本数据=
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=true, fit_mode="BLACK_MASK", deny_auto_switch_scene=true)] 初始引导
[PlayMusic(key="$babel_loop", volume=0.8, delay=0.2)]
[name=""]   哦，是你。
[Dialog]
[Image(image="bg_0_babel", fadetime=1, block=true)]
[ImageTween(image="bg_0_babel", tiled=true, xScaleTo=1.05, yScaleTo=1.05, duration=3, block=false)]
[ImageTween(image="bg_0_babel", tiled=true, xScaleTo=1.5, yScaleTo=1.5, duration=75, block=false)]
[name=""]   离我们上一次见面，已经过去了很久。
[name=""]   这段时间里......你一直徘徊在悬崖的边缘。
[Dialog]
[Delay(time=1.3)]
[name=""]   你可能已经忘记了你的身份，但你还记得那个名字，这就够了。
[Dialog]
[name=""]   ——好了，别在这里逗留太久。
[name=""]   毕竟，你既不是我的客人，也不应该出现在这里。
[name=""]   她需要你。
```
