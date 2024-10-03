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
    def scene_play(self, obj: Scene, title: Text) -> Text:
        section_title = title
        return section_title


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
    sections: list[str] = ["0x00-同余", "0x01-乘法逆元", "0x02-欧拉函数", "0x03-费马小定理",
                           "0x04-欧几里得算法", "0x05-Wilson定理", "0x06-裴蜀定理", "0x07-中国剩余定理"]

    def title_opening(self, obj: Scene) -> Text:
        # 总开场
        icon = ImageMobject("./icon/manim.jpg").scale(0.5).shift([0, 3, 0])
        opening = Group(Text("本视频使用", font_size=100),
                        icon, Text("制作", font_size=100)).arrange(RIGHT)
        obj.play(FadeIn(opening), run_time=2)
        obj.wait(2)
        obj.play(FadeOut(opening), run_time=1)
        title = Text("密码学数论基础", font_size=100)
        obj.play(Write(title), run_time=2)
        obj.wait()
        return title

    def table_of_contents(self, obj: Scene) -> None:
        # 目录
        change_bottom_words(obj, "今天我们讲一些密码学数论基础知识")
        change_bottom_words(obj, "我们主要介绍以下知识点")
        change_bottom_words(obj, "同余、乘法逆元、欧拉函数、费马小定理、欧几里得算法", 0)
        cont = Text("CONTENTS", font_size=45).shift([0, 3, 0])
        obj.play(Write(cont), run_time=1)
        contents = VGroup(cont)
        for i in range(len(self.sections)):
            if i == 5:
                change_bottom_words(obj, "Willson定理、裴蜀定理及中国剩余定理", 0)
            pos = [-3 if i % 2 == 0 else 3, (2-i//2)-0.5, 0]
            t = Text(self.sections[i][5:], font=FONT["zh"], color="Red" if i in [
                0, 3, 4, 7] else "Blue").shift(pos)
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


class Equiv(S):
    def scene_play(self, obj: Scene, title: Text) -> Text:
        section_title = title
        # 同余的定义
        defination = Paragraph("两个或两个以上的整数，",
                               "除以一个整数m，如果",
                               "余数相同，那么这几个",
                               "整数对于除数m来说就",
                               "是同余的。",
                               #    alignment="left",
                               font=FONT["zh"],
                               font_size=50,
                               t2w={
                                   '同余': BOLD
                               },
                               t2c={
                                   '余数相同': BLUE,
                                   '同余': RED_A
                               })
        obj.play(Write(defination), run_time=4)
        obj.wait()
        defination.generate_target()
        defination.target.scale(24/50).to_corner(UR, buff=0.5)
        obj.play(MoveToTarget(defination), run_time=1)
        # 举个例子
        change_bottom_words(obj, "举个栗子")
        change_bottom_words(obj, "31和11除以10都余1")
        thirty_one = MathTex(r"31\div10=3\dots{1}", font_size=75).shift(UP)
        eleven = MathTex(r"11\div10=1\dots{1}", font_size=75)
        equations = VGroup(thirty_one, eleven).arrange(DOWN)
        obj.play(Write(equations), run_time=1.5)
        obj.wait()
        thirty_one[0][10].set_color(RED)
        eleven[0][10].set_color(RED)
        obj.wait()
        change_bottom_words(obj, "按照定义，我们说31和11在模10意义下同余")
        change_bottom_words(obj, "记作这个式子")
        equiv = Tex(r"$31\equiv 11\pmod {10}$", font_size=75).shift(
            DOWN*1.5).set_color(YELLOW)
        obj.play(Write(equiv))
        equations.add(equiv)
        obj.wait()
        obj.play(Unwrite(equations), run_time=1.5)
        obj.wait()
        obj.play(Unwrite(defination),  run_time=1.5)
        # 性质
        change_bottom_words(obj, "下面介绍同余的几个性质")
        # 1
        change_bottom_words(obj, "一、同余式与等式可以互相转化")
        line = Tex(r"$a\equiv b\pmod p\Leftrightarrow a=b+k\times p~~~a,b,p,k\in\mathbb{Z}$",
                   tex_template=TexTemplateLibrary.ctex, font_size=50)
        obj.play(Write(line))
        obj.wait(2)
        obj.play(Unwrite(line))
        # 2
        change_bottom_words(obj, "二、同余式具有传递性")
        line = Tex(r"$a\equiv b\pmod p,b\equiv c\pmod p\Rightarrow a\equiv c\pmod p$",
                   tex_template=TexTemplateLibrary.ctex, font_size=50)
        obj.play(Write(line))
        obj.wait(2)
        obj.play(Unwrite(line))
        # 3
        change_bottom_words(obj, "三、同余式乘法满足以下式子")
        line = Tex(r"$ab~mod~p=((a~mod~p)\times b)~mod~p$",
                   tex_template=TexTemplateLibrary.ctex, font_size=50)
        obj.play(Write(line))
        obj.wait(2)
        obj.play(Unwrite(line))
        # 4、5
        change_bottom_words(obj, "四、同余式两边同时加或乘相同的数，式子仍然成立")
        bg = Tex(r"若$a\equiv b\pmod p$",
                 tex_template=TexTemplateLibrary.ctex, font_size=50)
        obj.play(Write(bg))
        obj.wait()
        obj.play(bg.animate.to_corner(UR, buff=0.5), run_time=1)
        equation_block = BulletedList(r"$\forall c,~(a+c)\equiv(b+c)\pmod p$",
                                      r"$\forall c,~(a\times c)\equiv(b\times c)\pmod p$", tex_template=TexTemplateLibrary.ctex)
        obj.play(Write(equation_block), run_time=4)
        obj.wait(2)
        obj.play(Unwrite(equation_block), Unwrite(bg), run_time=1.5)
        # 6
        bg = Tex(r"若$a\equiv b\pmod p,~c\equiv d\pmod p$",
                 tex_template=TexTemplateLibrary.ctex, font_size=50)
        obj.play(Write(bg))
        change_bottom_words(obj, "五、若现在有数a,b,c,d,p满足上述条件")
        obj.wait()
        obj.play(bg.animate.to_corner(UR, buff=0.5), run_time=1)
        equation_block = BulletedList(r"$(a+c)\equiv(b+d)\pmod p$",
                                      r"$(a-c)\equiv(b-d)\pmod p$",
                                      r"$(a\times c)\equiv(b\times d)\pmod p$",
                                      r"$(a~/~c)\equiv(b~/~d)\pmod p$", tex_template=TexTemplateLibrary.ctex)
        change_bottom_words(obj, "则我们有如下式子")
        obj.play(Write(equation_block), run_time=4)
        obj.wait(4)
        obj.play(Unwrite(equation_block), Unwrite(bg), run_time=1.5)

        clear_bottom_words(obj)
        return section_title


class Invert(S):
    def scene_play(self, obj: Scene, title: Text) -> Text:
        section_title = title
        # 乘法逆元的定义
        defination = Paragraph("在模m算术中，若整数a",
                               "存在一个整数x，使得",
                               "ax=km+1，则称x是a在",
                               "模m下的乘法逆元。",
                               "",
                               "乘法逆元存在的条件是",
                               "a与m互质。",
                               #    alignment="left",
                               font=FONT["zh"],
                               font_size=50,
                               t2w={
                                   '乘法逆元': BOLD
                               },
                               t2c={
                                   'ax=km+1': BLUE,
                                   '乘法逆元': RED_A,
                                   "a与m互质": YELLOW,
                               })
        obj.play(Write(defination), run_time=4)
        obj.wait()
        defination.generate_target()
        defination.target.scale(24/50).to_corner(UR, buff=0.5)
        obj.play(MoveToTarget(defination), run_time=1)
        # 举个例子
        # inverse(5, 13) = 8
        change_bottom_words(obj, "举个栗子")
        change_bottom_words(obj, "因为")
        equation = MathTex(r"5\times8=40=3\times13+1",
                           font_size=75).shift(UP*0.5)
        refer = MathTex(r"a\times x~~~~=~~~k\times m+1", font_size=75)
        equations = VGroup(equation, refer).arrange(DOWN)
        obj.play(Write(equations), run_time=1.5)
        obj.wait()
        equation[0][2].set_color(RED_A)
        equation[0][4:6].set_color(YELLOW)
        equation[0][7].set_color(RED_A)
        equation[0][12].set_color(BLUE)
        refer[0][2].set_color(RED_A)
        refer[0][4].set_color(RED_A)
        refer[0][8].set_color(BLUE)
        obj.wait()
        change_bottom_words(obj, "按照定义，我们说8是5在模13下的乘法逆元")
        change_bottom_words(obj, "记作这个式子")
        invert = Tex(r"$8=5^{-1}\pmod{13}$",
                     font_size=75).shift(DOWN*1.5).set_color(YELLOW)
        obj.play(Write(invert))
        equations.add(invert)
        obj.wait()
        obj.play(Unwrite(equations), run_time=1.5)
        obj.wait()
        obj.play(Unwrite(defination),  run_time=1.5)
        clear_bottom_words(obj)
        # 逆元的作用
        change_bottom_words(obj, "乘法逆元常用作模下的除法")
        change_bottom_words(obj, "即在模下除以一个数就是乘上这个数的逆元")
        e1 = Tex(r"$a\times b\equiv c\pmod m$",
                 font_size=75).shift(UP)
        e2 = Tex(r"$a\equiv c\times b^{-1}\pmod m$",
                 font_size=75).next_to(e1, DOWN)
        obj.play(Write(e1))
        obj.wait()
        obj.play(Write(e2))
        obj.wait(2)
        obj.play(Unwrite(e1), Unwrite(e2), run_time=1.5)

        clear_bottom_words(obj)
        return section_title


class Euler(S):
    def scene_play(self, obj: Scene, title: Text) -> Text:
        section_title = title
        # 欧拉函数的定义
        line1 = Tex(r"$\mbox{欧拉函数}\phi(n)\mbox{表示的是}$",
                    tex_template=TexTemplateLibrary.ctex, font_size=50)
        line2 = Tex(r"$\mbox{小于或等于}n\mbox{且与}n\mbox{互质的}$",
                    tex_template=TexTemplateLibrary.ctex, font_size=50)
        line3 = Tex(r"$\mbox{正整数的个数。}$",
                    tex_template=TexTemplateLibrary.ctex, font_size=50)
        line1[0][0:4].set_color(RED_A)
        line2[0][-3:-1].set_color(BLUE)
        line3[0][:3].set_color(RED_A)
        defination = VGroup(line1, line2, line3).arrange(DOWN)
        obj.play(Write(defination), run_time=4)
        obj.wait()
        defination.generate_target()
        defination.target.scale(30/50).to_corner(UR, buff=0.5)
        obj.play(MoveToTarget(defination), run_time=1)
        change_bottom_words(obj, "那么，如何计算一个数的欧拉函数呢")
        phi = Tex(r"$\phi(n)=?$", font_size=150)
        obj.play(Write(phi))
        obj.wait(1.5)
        obj.play(Unwrite(phi))
        # phi(ab)=phi(a)phi(b)
        change_bottom_words(obj, "我们先来看这个式子")
        bg = Tex(r"$(a,b)=1$", font_size=100).shift(UP)
        phi_ab = Tex("$\phi(ab)=$", font_size=100).shift(LEFT*2+DOWN*0.2)
        res = Tex(r"$\phi(a)\phi(b)$", font_size=100).next_to(phi_ab, RIGHT)
        obj.play(Write(bg))
        obj.play(Write(phi_ab))
        change_bottom_words(obj, "当a，b互质的时候，根据乘法原理，我们易得")
        obj.play(Write(res))
        obj.wait(3)
        obj.play(Unwrite(bg), Unwrite(phi_ab), Unwrite(res), run_time=1.5)
        # 合数分析
        N1 = Tex(r"$n$", font_size=150).shift(LEFT*3.5)
        N2 = Tex(r"$=\prod_{i=1}{p_i}^{r_i}$",
                 font_size=150).next_to(N1, RIGHT)
        N = VGroup(N1, N2)
        change_bottom_words(obj, "对于任意一个正整数n")
        obj.play(Write(N1))
        change_bottom_words(obj, "我们可以先考虑其质因数分解")
        obj.play(Write(N2))
        change_bottom_words(obj, "因此我们需要先计算p的k次方的欧拉函数")
        obj.play(Unwrite(N), run_time=1.5)
        # 质数p
        change_bottom_words(obj, "对于素数p，我们能很轻松的计算其欧拉函数")
        tex_p = Tex(r"$p$", font_size=100).shift(LEFT+UP)
        res = Tex(r"$=p^1$", font_size=100).next_to(tex_p, RIGHT)
        p = VGroup(tex_p, res)
        phi_p = Tex(r"$\phi(p)=p-1$", font_size=100).next_to(p,
                                                             DOWN).set_color(YELLOW)
        obj.play(Write(tex_p))
        change_bottom_words(obj, "因为p的质因数只有p")
        obj.play(Write(res))
        change_bottom_words(obj, "根据定义很容易得到其欧拉函数等于p-1")
        obj.play(Write(phi_p))
        obj.play(Unwrite(p), Unwrite(phi_p), run_time=1.5)
        # p^k
        change_bottom_words(obj, "再考虑p的k次方")
        phi_pk = Tex(r"$\phi({p^k})$", font_size=100).shift(LEFT*2)
        res = Tex(r"$=p^k-p^{k-1}$", font_size=100).next_to(phi_pk, RIGHT)
        obj.play(Write(phi_pk))
        change_bottom_words(obj, "我们从反面思考，计算与其不互质的数的个数")
        phi_pk.generate_target()
        phi_pk.target.move_to([0, 3.5, 0]).scale(0.5)
        obj.play(MoveToTarget(phi_pk))
        change_bottom_words(obj, "现在问题转变成如何构造一个与p的k次方互质的数")
        goal = Tex(r"$(N,p)\neq1$", font_size=100)
        obj.play(Write(goal))
        obj.wait()
        goal[0][1].set_color(RED)
        change_bottom_words(obj, "考虑到可供选择的因数只有p")
        obj.play(Unwrite(goal))
        goal = Tex(r"$N=A\times p\le p^k$", font_size=100)
        obj.play(Write(goal))
        change_bottom_words(obj, "只需要找出p的k次方能容纳几个形如Ap的数")
        goal.generate_target()
        goal.target.move_to(UP*1.5)
        obj.play(MoveToTarget(goal))
        A_range = Tex(r"$A\in\{1,2,3\cdots p^{k-1}\}$", font_size=100)
        obj.play(Write(A_range))
        obj.play(Unwrite(goal))
        change_bottom_words(obj, "即p的k-1次方")
        A_range.generate_target()
        A_range.target = Tex(
            r"$A\in\{\underbrace{1,2,3\cdots p^{k-1}}_{p^{k-1}}\}$", font_size=100)
        obj.play(MoveToTarget(A_range))
        obj.wait(2)
        obj.play(Unwrite(A_range))
        change_bottom_words(obj, "因此易得")
        phi_pk.generate_target()
        phi_pk.target.move_to([-2, 0, 0]).scale(2)
        obj.play(MoveToTarget(phi_pk))
        obj.play(Write(res))
        obj.wait()
        obj.play(Unwrite(phi_pk), Unwrite(res), run_time=1.5)
        # n
        N = Tex(r"$n=\prod_{i=1}{p_i}^{r_i}$",
                font_size=50).move_to([0, 3.5, 0])
        phi_n = Tex(r"$\phi(n)$", font_size=150)
        obj.play(Write(phi_n), Write(N))
        change_bottom_words(obj, "这下我们可以解决求n的欧拉函数值的问题了")
        phi_n.generate_target()
        phi_n.target.move_to([-4, 0, 0]).scale(0.5)
        obj.play(MoveToTarget(phi_n))
        res = Tex(
            r"$=\prod_{i=1}(p_i-1)(p_i)^{r_i-1}$", font_size=75).next_to(phi_n, RIGHT)
        obj.play(Write(res))
        obj.wait(2)
        obj.play(Unwrite(N), Unwrite(phi_n), Unwrite(res), run_time=1.5)
        obj.play(Unwrite(defination), run_time=1.5)
        # 欧拉定理
        change_bottom_words(obj, "欧拉函数有一个非常重要的性质")
        euler_thoery = Tex(
            r"$a^{\phi(m)}\equiv1\pmod m$", font_size=100)
        bg = Text("(a, m) = 1", font=FONT['en'],
                  font_size=50).to_corner(UR, buff=0.5)
        obj.play(Write(euler_thoery), Write(bg))
        obj.wait()
        change_bottom_words(obj, "这个性质在后面学习RSA加解密的时候会用到")
        obj.play(Unwrite(euler_thoery), Unwrite(bg), run_time=1.5)

        clear_bottom_words(obj)
        return section_title


class Femmat(S):
    def scene_play(self, obj: Scene, title: Text) -> Text:
        section_title = title
        femmat = Tex(r"$a^{p-1}\equiv1\pmod p$", font_size=100)
        bg = Text("p为质数", font=FONT['zh'],
                  font_size=50).to_corner(UR, buff=0.5)
        obj.play(Write(femmat), Write(bg))
        change_bottom_words(obj, "费马小定理其实就是刚刚的欧拉定理的特例")
        femmat.generate_target()
        femmat.target.move_to([0, 2, 0])
        obj.play(MoveToTarget(femmat))
        euler = Tex(r"$a^{\phi(m)}\equiv1\pmod m$", font_size=100)
        obj.play(Write(euler))
        change_bottom_words(obj, "当m为质数时，欧拉函数值为m-1")
        euler.generate_target()
        euler.target = Tex(r"$a^{\phi(p)}\equiv1\pmod p$", font_size=100)
        obj.play(MoveToTarget(euler))
        obj.wait()
        euler.generate_target()
        euler.target = Tex(r"$a^{p-1}\equiv1\pmod p$", font_size=100)
        obj.play(MoveToTarget(euler))
        femmat.generate_target()
        femmat.target.move_to([0, 0, 0])
        obj.play(MoveToTarget(femmat))
        obj.play(Unwrite(femmat), Unwrite(euler), Unwrite(bg), run_time=1.5)

        clear_bottom_words(obj)
        return section_title


class Wilson(S):
    def scene_play(self, obj: Scene, title: Text) -> Text:
        section_title = title
        bg = Text("p是质数", font=FONT['zh'],
                  font_size=50).to_corner(UR, buff=0.5)
        willson = Tex(r"$(p-1)!\equiv-1\pmod p$", font_size=100)
        change_bottom_words(obj, "Wilson定理的一种表述为")
        obj.play(Write(willson), Write(bg))
        obj.wait()
        obj.play(Unwrite(willson), Unwrite(bg))
        change_bottom_words(obj, "换一种表述")
        another = Tex(r"$p$是素数当且仅当$(p-1)!+1$能被$p$整除",
                      tex_template=TexTemplateLibrary.ctex, font_size=50)
        obj.play(Write(another))
        obj.wait()
        obj.play(Unwrite(another), run_time=1.5)

        clear_bottom_words(obj)
        return section_title


class Euclid(S):
    def scene_play(self, obj: Scene, title: Text) -> Text:
        section_title = title
        # 欧几里得算法的定义
        bg = Tex(r"$a\le b$", font_size=50).to_corner(UR, buff=0.5)
        goal = Tex(r"$GCD(a,b)$", font_size=100)
        obj.play(Write(goal), Write(bg))
        change_bottom_words(obj, "计算两个非负整数a和b的最大公约数(GCD)的算法")
        change_bottom_words(obj, "我们可以使用这个递归公式来计算")
        goal.generate_target()
        goal.target.move_to([-2, 0, 0]).scale(0.75)
        res = Tex(r"$=GCD(b,a\%b)$", font_size=75).next_to(goal.target, RIGHT)
        obj.play(MoveToTarget(goal), Write(res))
        equation = VGroup(goal, res)
        change_bottom_words(obj, "当b=0时，a就是最大公约数")
        obj.play(Unwrite(equation), Unwrite(bg))
        # python代码
        euclid = Code(
            "Euclid.py",
            language="Python",
            tab_width=4,
            line_spacing=1,
            insert_line_no=False,
            background="window",
            style="github-dark",
            font="Monospace",
            font_size=24
        ).shift(RIGHT*0.5+UP*0.2)
        obj.play(FadeIn(euclid))
        change_bottom_words(obj, "欧几里得算法的Python实现")
        obj.wait()
        obj.play(FadeOut(euclid))
        # 模拟
        change_bottom_words(obj, "欧几里得算法模拟")
        a = 114
        b = 514
        title = Text("计算GCD(114, 514)", font=FONT['zh'], font_size=50)
        obj.play(Write(title))
        title.generate_target()
        title.target.to_corner(UR, buff=0.5)
        obj.wait()
        equation = Tex(r"$GCD(a,b)=GCD(b, a\%b)$", font_size=75).shift(DOWN*2)
        obj.play(MoveToTarget(title), Write(equation))
        obj.wait()
        t1 = Tex(f"$GCD({a},{b})$", font_size=75)
        equal = Tex(f"$=$", font_size=75)
        t2 = Tex(f"$GCD({b},{a}\%{b})$", font_size=75)
        lst = [t1, equal, t2]
        template = VGroup(*lst).arrange(RIGHT)
        obj.play(Write(template))
        while b != 0:
            a, b = b, a % b
            obj.wait()
            obj.play(FadeOut(template[0]), FadeOut(template[1]), template[2].animate(
                path_arc=-PI / 2).move_to(template[0]).shift(RIGHT*0.5))
            template[2].generate_target()
            template[2].target = Tex(
                f"$GCD({a},{b})$", font_size=75).move_to(template[0])
            obj.play(MoveToTarget(template[2]))
            lst = [template[2], equal, Tex(
                f"$GCD({b},{a}\%{b})$" if b != 0 else f"${a}$", font_size=75)]
            template = VGroup(*lst).arrange(RIGHT)
            obj.play(Write(lst[1]), Write(lst[2]))

        res = Tex(f"$GCD(114,514)={a}$", font_size=75)
        obj.play(Unwrite(template), Unwrite(equation), Unwrite(title))
        obj.play(Write(res))
        obj.wait()
        obj.play(Unwrite(res))

        clear_bottom_words(obj)
        return section_title


class ExtEuclid(S):
    def scene_play(self, obj: Scene, title: Text) -> Text:
        section_title = title
        # 裴蜀定理的定义
        goal1 = Tex(
            r"$\forall a,b\in\mathbb{Z},\exists x,y,s.t.$", font_size=100).shift(UP*0.5)
        goal2 = Tex(r"$ax+by=GCD(a,b)$", font_size=100).next_to(goal1, DOWN)
        obj.play(Write(goal1))
        change_bottom_words(obj, "对于任意两个整数a和b")
        change_bottom_words(obj, "它们的最大公约数可以表示为a和b的线性组合")
        obj.play(Write(goal2))
        change_bottom_words(obj, "即存在整数x和y，使得ax+by=GCD(a,b)")
        goal2[0][1].set_color(RED)
        goal2[0][4].set_color(BLUE)
        change_bottom_words(obj, "这里的x和y能够通过扩展欧几里得算法解出")
        obj.play(Unwrite(goal1), Unwrite(goal2))
        # python代码
        exteuclid = Code(
            "ExtEuclid.py",
            language="Python",
            tab_width=4,
            line_spacing=1,
            insert_line_no=False,
            background="window",
            style="github-dark",
            font="Monospace",
            font_size=18
        ).shift(RIGHT*0.5+UP*0.2)
        obj.play(FadeIn(exteuclid))
        change_bottom_words(obj, "扩展欧几里得算法的Python实现")
        obj.wait()
        obj.play(FadeOut(exteuclid))

        clear_bottom_words(obj)
        return section_title


class CRT(S):
    def scene_play(self, obj: Scene, title: Text) -> Text:
        section_title = title
        # CRT介绍
        bg = VGroup(Tex(r"$m_1,m_2,\dots,m_n$两两互素", tex_template=TexTemplateLibrary.ctex, font_size=50),
                    Tex(r"$\forall a_1,a_2,\dots,a_n$", tex_template=TexTemplateLibrary.ctex, font_size=50)).arrange(DOWN)
        obj.play(Write(bg), run_time=2)
        obj.wait()
        bg.generate_target()
        bg.target.scale(0.75).to_corner(UR, buff=0.5)
        obj.play(MoveToTarget(bg))
        e = Tex(
            r"$\left\{\begin{matrix}x\equiv a_1\pmod{m_1}\\ x\equiv a_2\pmod{m_2}\\\dots\\ x\equiv a_n\pmod{m_n}\end{matrix}\right.$", font_size=60)
        obj.play(Write(e))
        change_bottom_words(obj, "同余方程组存在整数解")
        e.generate_target()
        e.target.scale(0.75).move_to([0, 2, 0])
        obj.play(MoveToTarget(e))
        res = Tex(
            r"$x\equiv\sum_{i=1}^n a_i\times\frac{N}{m_i}\times[(\frac{N}{m_i})^{-1}]_{m_i}\pmod N$", font_size=70).shift(DOWN*0.5)
        r = Tex(r"$N=\prod_{i=1}^n m_i$", font_size=70).next_to(res, DOWN)
        obj.play(Write(res), Write(r))
        obj.wait(3)
        obj.play(Unwrite(bg), Unwrite(e), Unwrite(res), Unwrite(r))

        clear_bottom_words(obj)
        return section_title


class Final(Scene):
    def construct(self):
        cs = Cutscenes()
        scenes: list[S] = [Equiv(), Invert(), Euler(), Femmat(),
                           Euclid(), Wilson(), ExtEuclid(), CRT()]
        title = cs.title_opening(self)
        section_title = None
        for idx in range(len(scenes)):
            section_title = cs.section_opening(
                self, idx, title if section_title is None else section_title)
            section_title = scenes[idx].scene_play(self, section_title)
        cs.ending(self, section_title)
