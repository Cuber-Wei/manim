import inspect
from manim import *

FONT = {
    "en": "JetBrains Mono",
    "zh": "FangSong",
}
READ_SPEED = 8
TEX_TEMPLATE = TexTemplate()
TEX_TEMPLATE.add_to_preamble(r"\usepackage{color,xcolor}")
bottom_words = None


class S(Scene):
    idx = -1

    def scene_play(self, obj: Scene, title: Text) -> Text:
        section_title = title
        return section_title


def getScenes() -> list:
    ignore = ["S", "Scene", "Final", "Cutscenes"]
    module_name = __name__.split(".")[-1]
    all_classes = [member for _, member in inspect.getmembers(
        __import__(module_name)) if inspect.isclass(member)]
    tmp = [cls for cls in all_classes if cls.__module__ == module_name]
    scenes = [cls for cls in tmp if cls.__name__ not in ignore]
    scenes.sort(key=lambda x: x.idx)
    return scenes[1:]


def change_bottom_words(obj: Scene, text: str, wait_time: int = -1) -> None:
    global bottom_words
    new_words = Text(text, font_size=24, font="SimHei").shift([0, -3.5, 0])
    if bottom_words is None:
        obj.play(Write(new_words), run_time=1)
    else:
        obj.play(Transform(bottom_words, new_words,
                 replace_mobject_with_target_in_scene=True), run_time=1)
    bottom_words = new_words
    if wait_time > 0:
        obj.wait(wait_time)
    elif wait_time == -1:
        obj.wait(len(text)/READ_SPEED)


def clear_bottom_words(obj: Scene) -> None:
    global bottom_words
    if bottom_words is not None:
        obj.play(Unwrite(bottom_words), run_time=1)
        bottom_words = None


class Cutscenes(Scene):
    sections: list[str] = ["0xFF-背景引入", "0x00-加密",
                           "0x01-解密", "0x02-数学原理", "0x03-展望"]

    def title_opening(self, obj: Scene) -> Text:
        # 总开场
        icon = ImageMobject("./icon/manim.jpg").scale(0.5)
        opening = Group(Text("本视频使用", font_size=100),
                        icon, Text("制作", font_size=100)).arrange(RIGHT)
        obj.play(FadeIn(opening), run_time=2)
        obj.wait(2)
        obj.play(FadeOut(opening), run_time=1)
        title = Text("RSA加密算法", font_size=100)
        obj.play(Write(title), run_time=2)
        obj.wait()
        return title

    def table_of_contents(self, obj: Scene) -> None:
        # 目录
        change_bottom_words(obj, "今天来学习RSA加密算法")
        cont = Text("CONTENTS", font_size=45).shift([0, 3, 0])
        change_bottom_words(obj, "本视频主要分享以下内容")
        change_bottom_words(obj, "RSA加解密方式、背后的数学原理以及一些展望", 0)
        obj.play(Write(cont), run_time=1)
        contents = VGroup(cont)
        for i in range(len(self.sections)):
            pos = [-3 if i % 2 == 0 else 3, (2-i//2)-0.5, 0]
            t = Text(self.sections[i][5:], font=FONT["zh"], color="Red" if i in [
                0, 3, 4, 7, 8] else "Blue").shift(pos)
            contents.add(t)
            obj.play(Write(t), run_time=1)
        change_bottom_words(obj, "下面一起看看吧")
        clear_bottom_words(obj)
        obj.play(FadeOut(contents), run_time=1)

    def section_opening(self, obj: Scene, idx: int, prev_section_title: Text) -> Text:
        # 章节开场
        section_title = Text(self.sections[idx], font=FONT["zh"])
        if idx == 0:
            obj.play(Unwrite(prev_section_title), run_time=1)
            self.table_of_contents(obj)
            obj.play(Write(section_title), run_time=1)
        else:
            obj.play(prev_section_title.animate(run_time=1).move_to([0, 0, 0]),
                     Transform(prev_section_title, section_title, replace_mobject_with_target_in_scene=True))
        obj.wait()
        obj.play(section_title.animate(run_time=1).to_corner(UL, buff=0.5),
                 Transform(section_title, Text(self.sections[idx][5:], font=FONT["zh"]).to_corner(UL, buff=0.5)))
        return section_title

    def ending(self, obj: Scene, section_title: Text) -> None:
        # 结尾
        section_title.generate_target()
        section_title.target.move_to([0, 0, 0])
        obj.play(MoveToTarget(section_title))
        obj.play(FadeOut(section_title), run_time=2)
        obj.wait()
        end = Tex(
            r"$The~End$",
            tex_template=TexFontTemplates.french_cursive,
            font_size=144,
        )
        obj.play(Write(end), run_time=3)
        obj.wait()


class Final(Scene):
    def construct(self):
        cs = Cutscenes()
        title = cs.title_opening(self)
        scene_to_play: list[S] = [s() for s in getScenes()]
        section_title = None
        for idx in range(len(scene_to_play)):
            section_title = cs.section_opening(
                self, idx, title if section_title is None else section_title)
            section_title = scene_to_play[idx].scene_play(self, section_title)
        cs.ending(self, section_title)
        self.wait()
