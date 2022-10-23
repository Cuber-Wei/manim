from manim import *


class Opening(Scene):
    def construct(self):
        # 背景介绍
        title = Text("背景引入:", font_size=40).shift(UP * 2.5 + LEFT * 5.5)
        back_text = Text(
            "\t假设Alice想通过一个不可靠的媒体接收Bob的一条私人消息, \n\nBob可以用下面的方式产生一组公钥和私钥.",
            t2c={"不可靠": RED, "Alice": PINK, "Bob": BLUE, "公钥": GREEN, "私钥": RED}, font_size=30)
        back_ground = VGroup(title, back_text)
        self.play(Create(back_ground), run_time=4)
        self.wait(2)
        # RSA加密 文本呈现
        rsa_text = Text("RSA 加密", font_size=80, t2c={"RSA": DARK_BLUE})
        self.play(FadeOut(back_ground))
        self.play(Create(rsa_text), run_time=2)
        self.wait(2)
        # 开场白结束，隐去文字
        self.play(FadeOut(rsa_text))
        self.wait(2)


class Encode(Scene):
    def construct(self):
        title = Text("加密", font_size=50)
        self.play(Create(title))
        self.wait()
        new_title = Text("加密字符串'RSA_Encode'(388769841948688842187877)",
                         font_size=30).to_corner(UL, buff=0.7)
        self.play(Transform(title, new_title))

        rectangle = Rectangle(height=4, width=3).to_corner(DR, buff=0.5)
        explain_text = Text(
            '名词解释:',
            t2c={"名词解释": YELLOW},
            font_size=20).shift(RIGHT * 4.5)
        corner_explain = VGroup(rectangle, explain_text)

        step = Text("1. 随意选择两个大的质数p和q, (p不等于q), 计算N = pq.", t2c={
            "大的质数": GREEN, "(p不等于q)": RED}, font_size=35).shift(UP * 2)
        explain = Text("Example:", font_size=20).shift(LEFT * 5 + UP)
        example = Text("p = 1,145,141\nq = 1,145,143\nN = 1,311,350,200,163", t2c={
                       "p": BLUE_B, "q": BLUE_B, "N": BLUE_B, "1,145,141": YELLOW, "1,145,143": YELLOW, "1,311,350,200,163": YELLOW}, font_size=40).shift(LEFT * 2)
        self.play(Create(step), run_time=3)
        self.play(Create(explain), Create(example), Create(corner_explain))
        self.wait(4)

        new_step = Text("2. 根据欧拉函数, 求得r = φ(N) = φ(p) * φ(q) = (p-1)(q-1).",
                        t2c={"欧拉函数": GREEN}, font_size=35).shift(UP * 2)
        new_example = Text("p = 1,145,141\nq = 1,145,143\nN = 1,311,350,200,163\nr = 1,311,347,909,880",
                           t2c={"p": BLUE_B, "q": BLUE_B, "N": BLUE_B, "r": BLUE_B, "1,145,141": YELLOW,
                                "1,145,143": YELLOW, "1,311,350,200,163": YELLOW, "1,311,347,909,880": YELLOW},
                           font_size=40).shift(LEFT * 2 + DOWN * 0.3)
        new_explain_text = Text(
            '名词解释:\n\n欧拉函数\n\n\t在数论里, 对正整\n数n,欧拉函数是小于n的\n正整数中与n互质的数\n的数目.\n\n记作 φ(N)\n特别的, 对于质数N,\nφ(N) = N - 1',
            t2c={"名词解释": YELLOW, "欧拉函数": GREEN},
            font_size=20).shift(RIGHT * 5.15 + DOWN * 1.15)
        self.play(Transform(step, new_step))
        self.play(Transform(explain_text, new_explain_text))
        self.wait(3)
        self.play(Transform(example, new_example))
        self.wait(4)

        new_step = Text("3. 选择一个小于r的整数e, 保证e与r互质.\n并选择一个e关于r的模反元素d.",
                        t2c={"模反元素": GREEN}, font_size=35).shift(UP * 2 + LEFT)
        new_explain_text = Text(
            '名词解释:\n\n模反元素\n\n\t如果两个正整数a\n和n 互质, 那么一定可\n以找到整数b , 使得\n a * b - 1 被n 整除,\n或者说a * b 被 n除的\n余数是1. 这时, b就叫做\na的"模反元素".',
            t2c={"名词解释": YELLOW, "模反元素": GREEN},
            font_size=20).shift(RIGHT * 5.15 + DOWN * 1.15)
        new_example = Text("p = 1,145,141\nq = 1,145,143\nN = 1,311,350,200,163\nr = 1,311,347,909,880\ne = 1,138,480,027,699\nd = 11,451,499",
                           t2c={"p": BLUE_B, "q": BLUE_B, "N": BLUE_B, "r": BLUE_B, "e": BLUE_B, "d": BLUE_B, "1,145,141": YELLOW,
                                "1,145,143": YELLOW, "1,311,350,200,163": YELLOW, "1,311,347,909,880": YELLOW, "1,138,480,027,699": YELLOW, "11,451,499": YELLOW}, font_size=40).shift(LEFT * 2 + DOWN)
        self.play(Transform(step, new_step))
        self.play(Transform(explain_text, new_explain_text))
        self.wait(2)
        self.play(Transform(example, new_example))
        self.wait(4)

        new_step = Text("其中(N, e)是公钥, (N, d)是私钥.",
                        t2c={"公钥": GREEN, "私钥": RED}, font_size=35).shift(UP * 2 + LEFT * 2)
        new_example = Text("p = 1,145,141\nq = 1,145,143\nN = 1,311,350,200,163\nr = 1,311,347,909,880\ne = 1,138,480,027,699\nd = 11,451,499\n公钥 : (1,311,350,200,163 , 1,138,480,027,699)\n私钥 : (1,311,350,200,163 , 11,451,499)",
                           t2c={"p": BLUE_B, "q": BLUE_B, "N": BLUE_B, "r": BLUE_B, "e": BLUE_B, "d": BLUE_B, "公钥": GRAY, "私钥": RED, "1,145,141": YELLOW,
                                "1,145,143": YELLOW, "1,311,350,200,163": YELLOW, "1,311,347,909,880": YELLOW, "1,138,480,027,699": YELLOW, "11,451,499": YELLOW},
                           font_size=30).shift(LEFT * 2 + DOWN * 1.5)

        self.play(Transform(step, new_step))
        self.play(FadeOut(corner_explain))
        self.wait(2)
        self.play(Transform(example, new_example))
        self.wait(2)

        new_exp_text = Tex("$m^{e}\\equiv c\\pmod{n} $")
        text = Text("\n其中\nm : 明文\nc : 密文",
                    t2c={"m": BLUE_B, "c": BLUE_B, "明文": YELLOW, "密文": YELLOW},
                    font_size=35).next_to(new_exp_text, DOWN, buff=0.2)
        new_explain_text = VGroup(new_exp_text, text).shift(
            RIGHT * 4.5)
        self.play(Create(new_explain_text))
        self.wait(1)
        self.play(FadeOut(step, example, explain, title))

        self.play(MoveAlongPath(new_explain_text, Line(RIGHT * 4.5, UP * 2)))
        final = Text(
            "明文 : 'RSA_Encode'(388769841913504470099045)\n密文 : b'M\\xb7\\xc6\\xba\\x1a'(333795736090)",
            t2c={"明文": BLUE_B, "密文": BLUE_B, "RSA_Encode": YELLOW, "M\\xb7\\xc6\\xba\\x1a": YELLOW,
                 "388769841913504470099045": GREEN, "333795736090": GREEN},
            font_size=40).shift(DOWN)
        self.play(Create(final))
        self.wait(2)
        self.play(FadeOut(final, new_explain_text))
        self.wait(2)


class Decode(Scene):
    def construct(self):
        title = Text("解密[已知公钥和私钥(N, e, d)]", font_size=50)
        self.play(Create(title))
        self.wait()
        new_title = Text("解密字符串b'M\\xb7\\xc6\\xba\\x1a'(333795736090)",
                         font_size=30).to_corner(UL, buff=0.7)
        self.play(Transform(title, new_title))

        rectangle = Rectangle(height=4, width=3).to_corner(DR, buff=0.5)
        explain_text = Text(
            '名词解释:',
            t2c={"名词解释": YELLOW},
            font_size=20).shift(RIGHT * 4.5)
        corner_explain = VGroup(rectangle, explain_text)

        step = Text("1. 分解N, 得到p, q.", t2c={
            "N": GREEN, "p": RED, "q": RED}, font_size=35).shift(UP * 2)
        explain = Text("Example:", font_size=20).shift(LEFT * 5 + UP)
        example = Text("N = 1,311,350,200,163\np = 1,145,141\nq = 1,145,143", t2c={
                       "p": BLUE_B, "q": BLUE_B, "N": BLUE_B, "1,145,141": YELLOW, "1,145,143": YELLOW, "1,311,350,200,163": YELLOW}, font_size=40).shift(LEFT * 2)
        self.play(Create(step), run_time=3)
        self.play(Create(explain), Create(example), Create(corner_explain))
        self.wait(4)

        exp1 = Text("由加密过程知", font_size=30).shift(UP * 1.5)
        process1 = Tex(
            "$c^{d}\\equiv m\\pmod{n}$ ··· (1)").shift(UP * 1)
        process2 = Tex("$m^{e}\\equiv c\\pmod{n}$ ··· (2)").shift(UP * 0.5)
        exp2 = Text("将式(2)代入式(1), 可得", font_size=30)
        process3 = Tex("$m^{ed}\\equiv m \\pmod{n} $",).shift(DOWN * 0.75)
        process3.color = RED
        self.play(FadeOut(corner_explain, step,
                  explain, example), FadeIn(exp1))
        self.wait()
        self.play(Write(process1))
        self.wait()
        self.play(Write(process2))
        self.wait()
        self.play(Write(exp2))
        self.wait()
        self.play(Write(process3))
        self.wait(3)
        self.play(FadeOut(exp1, exp2, process1, process2),
                  MoveAlongPath(process3, Line(
                      DOWN * 0.75, RIGHT * 5 + UP * 3)),
                  FadeIn(corner_explain, step, explain, example))

        new_step = Text("2. 根据费马小定理,求出\ned ≡ 1 (mod φ(N))", t2c={
                        "费马小定理": GREEN}, font_size=35).shift(UP * 2)
        new_explain_text = Text(
            "名词解释:\n\t费马小定理是数\n论中的一个重要定理:\n如果p是一个质数,而整\n数a不是p的倍数,则有",
            t2c={"名词解释": YELLOW},
            font_size=20).shift(RIGHT * 5.15 + DOWN)
        alg = Tex(
            "$a^{p-1}\\equiv 1\\pmod{p}$.").next_to(new_explain_text, DOWN, buff=0.3)
        alg.font_size = 30
        self.play(Transform(step, new_step), Transform(
            explain_text, new_explain_text), Write(alg))
        self.wait(4)

        new_step = Text("3. 可知e,d对于φ(N)互为逆元\n带入加密算法即可得出明文m.",
                        font_size=35).shift(UP * 2)
        self.play(Transform(step, new_step), FadeOut(
            alg, corner_explain, process3))
        self.wait(4)

        new_process0 = Tex("$m^{e}\\equiv c\\pmod{n}$").shift(UP * 2)
        new_process0.font_size = 50
        new_process0.color = LIGHT_BROWN
        new_process1 = Tex("$c^{d}\\equiv m\\pmod{n}$").next_to(
            new_process0, DOWN, buff=0.2)
        new_process1.font_size = 50
        new_process1.color = LIGHT_BROWN
        new_process2 = Tex("$m^{ed}\\equiv m \\pmod{n}$").next_to(
            new_process1, DOWN, buff=0.2)
        new_process2.font_size = 50
        new_process2.color = LIGHT_BROWN
        new_process3 = Tex(
            "$ed\\equiv 1\\pmod{\\varphi \\left ( N \\right )}$").next_to(new_process2, DOWN, buff=0.2)
        new_process3.font_size = 50
        new_process3.color = LIGHT_BROWN
        algi = VGroup(new_process0, new_process1, new_process2, new_process3)
        result = Text(
            "密文 : b'M\\xb7\\xc6\\xba\\x1a'(333795736090)\n明文 : 'RSA_Encode'(388769841913504470099045)",
            t2c={"明文": BLUE_B, "密文": BLUE_B, "RSA_Encode": YELLOW, "M\\xb7\\xc6\\xba\\x1a": YELLOW,
                 "388769841913504470099045": GREEN, "333795736090": GREEN},
            font_size=40).shift(DOWN)
        self.play(FadeOut(step, explain, example),
                  FadeIn(result, algi))
        self.wait(3)
        self.play(FadeOut(result, algi, title))
        self.wait(2)


class Real(Scene):
    def construct(self):
        title = Text("  刚刚是一个较为简单的例子, \n现实中, 常见的加密长这样:", font_size=50)
        self.play(Write(title), run_time=3)
        self.wait(2)

        real_py = Code(
            "real.py",
            tab_width=4,
            background="window",
            insert_line_no=False,
            font="XHei NF",
            font_size=20
        )
        new_title = Text("加密 'RSA_encode' 的相关参数",
                         font_size=30).next_to(real_py, UP)
        self.play(Transform(title, new_title), Write(real_py))
        self.wait(2)
        self.play(FadeOut(title, real_py), run_time=3)
        self.wait(2)
        text = Text("近现代的加密算法大多立足于\n大数分解的极大困难度.\n\t\t\tRSA亦如此", font_size=50)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
        self.wait()
        bye = Text("感谢观看！\nThanks!", font_size=50)
        self.play(Write(bye), run_time=5)
        self.wait(3)


class Test(Scene):
    def construct(self):
        new_process0 = Tex("$m^{e}\\equiv c\\pmod{n}$").shift(UP * 2)
        new_process0.font_size = 50
        new_process0.color = YELLOW
        new_process1 = Tex("$c^{d}\\equiv m\\pmod{n}$").next_to(
            new_process0, DOWN, buff=0.2)
        new_process1.font_size = 50
        new_process1.color = YELLOW
        new_process2 = Tex("$m^{ed}\\equiv m \\pmod{n}$").next_to(
            new_process1, DOWN, buff=0.2)
        new_process2.font_size = 50
        new_process2.color = YELLOW
        new_process3 = Tex(
            "$ed\\equiv 1\\pmod{\\varphi \\left ( N \\right )}$").next_to(new_process2, DOWN, buff=0.2)
        new_process3.font_size = 50
        new_process3.color = YELLOW
        algi = VGroup(new_process0, new_process1, new_process2, new_process3)
        self.add(algi)


class Final(Scene):
    def construct(self):
        # 背景介绍
        title = Text("背景引入:", font_size=40).shift(UP * 2.5 + LEFT * 5.5)
        back_text = Text(
            "\t假设Alice想通过一个不可靠的媒体接收Bob的一条私人消息, \n\nBob可以用下面的方式产生一组公钥和私钥.",
            t2c={"不可靠": RED, "Alice": PINK, "Bob": BLUE, "公钥": GREEN, "私钥": RED}, font_size=30)
        back_ground = VGroup(title, back_text)
        self.play(Create(back_ground), run_time=4)
        self.wait(2)
        # RSA加密 文本呈现
        rsa_text = Text("RSA 加密", font_size=80, t2c={"RSA": DARK_BLUE})
        self.play(FadeOut(back_ground))
        self.play(Create(rsa_text), run_time=2)
        self.wait(2)
        # 开场白结束，隐去文字
        self.play(FadeOut(rsa_text))
        self.wait()

        title = Text("加密", font_size=50)
        self.play(Create(title))
        self.wait()
        new_title = Text("加密字符串'RSA_Encode'(388769841948688842187877)",
                         font_size=30).to_corner(UL, buff=0.7)
        self.play(Transform(title, new_title))

        rectangle = Rectangle(height=4, width=3).to_corner(DR, buff=0.5)
        explain_text = Text(
            '名词解释:',
            t2c={"名词解释": YELLOW},
            font_size=20).shift(RIGHT * 4.5)
        corner_explain = VGroup(rectangle, explain_text)

        step = Text("1. 随意选择两个大的质数p和q, (p不等于q), 计算N = pq.", t2c={
            "大的质数": GREEN, "(p不等于q)": RED}, font_size=35).shift(UP * 2)
        explain = Text("Example:", font_size=20).shift(LEFT * 5 + UP)
        example = Text("p = 1,145,141\nq = 1,145,143\nN = 1,311,350,200,163", t2c={
                       "p": BLUE_B, "q": BLUE_B, "N": BLUE_B, "1,145,141": YELLOW, "1,145,143": YELLOW, "1,311,350,200,163": YELLOW}, font_size=40).shift(LEFT * 2)
        self.play(Create(step), run_time=3)
        self.play(Create(explain), Create(example), Create(corner_explain))
        self.wait(4)

        new_step = Text("2. 根据欧拉函数, 求得r = φ(N) = φ(p) * φ(q) = (p-1)(q-1).",
                        t2c={"欧拉函数": GREEN}, font_size=35).shift(UP * 2)
        new_example = Text("p = 1,145,141\nq = 1,145,143\nN = 1,311,350,200,163\nr = 1,311,347,909,880",
                           t2c={"p": BLUE_B, "q": BLUE_B, "N": BLUE_B, "r": BLUE_B, "1,145,141": YELLOW,
                                "1,145,143": YELLOW, "1,311,350,200,163": YELLOW, "1,311,347,909,880": YELLOW},
                           font_size=40).shift(LEFT * 2 + DOWN * 0.3)
        new_explain_text = Text(
            '名词解释:\n\n欧拉函数\n\n\t在数论里, 对正整\n数n,欧拉函数是小于n的\n正整数中与n互质的数\n的数目.\n\n记作 φ(N)\n特别的, 对于质数N,\nφ(N) = N - 1',
            t2c={"名词解释": YELLOW, "欧拉函数": GREEN},
            font_size=20).shift(RIGHT * 5.15 + DOWN * 1.15)
        self.play(Transform(step, new_step))
        self.play(Transform(explain_text, new_explain_text))
        self.wait(3)
        self.play(Transform(example, new_example))
        self.wait(4)

        new_step = Text("3. 选择一个小于r的整数e, 保证e与r互质.\n并选择一个e关于r的模反元素d.",
                        t2c={"模反元素": GREEN}, font_size=35).shift(UP * 2 + LEFT)
        new_explain_text = Text(
            '名词解释:\n\n模反元素\n\n\t如果两个正整数a\n和n 互质, 那么一定可\n以找到整数b , 使得\n a * b - 1 被n 整除,\n或者说a * b 被 n除的\n余数是1. 这时, b就叫做\na的"模反元素".',
            t2c={"名词解释": YELLOW, "模反元素": GREEN},
            font_size=20).shift(RIGHT * 5.15 + DOWN * 1.15)
        new_example = Text("p = 1,145,141\nq = 1,145,143\nN = 1,311,350,200,163\nr = 1,311,347,909,880\ne = 1,138,480,027,699\nd = 11,451,499",
                           t2c={"p": BLUE_B, "q": BLUE_B, "N": BLUE_B, "r": BLUE_B, "e": BLUE_B, "d": BLUE_B, "1,145,141": YELLOW,
                                "1,145,143": YELLOW, "1,311,350,200,163": YELLOW, "1,311,347,909,880": YELLOW, "1,138,480,027,699": YELLOW, "11,451,499": YELLOW}, font_size=40).shift(LEFT * 2 + DOWN)
        self.play(Transform(step, new_step))
        self.play(Transform(explain_text, new_explain_text))
        self.wait(2)
        self.play(Transform(example, new_example))
        self.wait(4)

        new_step = Text("其中(N, e)是公钥, (N, d)是私钥.",
                        t2c={"公钥": GREEN, "私钥": RED}, font_size=35).shift(UP * 2 + LEFT * 2)
        new_example = Text("p = 1,145,141\nq = 1,145,143\nN = 1,311,350,200,163\nr = 1,311,347,909,880\ne = 1,138,480,027,699\nd = 11,451,499\n公钥 : (1,311,350,200,163 , 1,138,480,027,699)\n私钥 : (1,311,350,200,163 , 11,451,499)",
                           t2c={"p": BLUE_B, "q": BLUE_B, "N": BLUE_B, "r": BLUE_B, "e": BLUE_B, "d": BLUE_B, "公钥": GRAY, "私钥": RED, "1,145,141": YELLOW,
                                "1,145,143": YELLOW, "1,311,350,200,163": YELLOW, "1,311,347,909,880": YELLOW, "1,138,480,027,699": YELLOW, "11,451,499": YELLOW},
                           font_size=30).shift(LEFT * 2 + DOWN * 1.5)

        self.play(Transform(step, new_step))
        self.play(FadeOut(corner_explain))
        self.wait(2)
        self.play(Transform(example, new_example))
        self.wait(2)

        new_exp_text = Tex("$m^{e}\\equiv c\\pmod{n} $")
        text = Text("\n其中\nm : 明文\nc : 密文",
                    t2c={"m": BLUE_B, "c": BLUE_B, "明文": YELLOW, "密文": YELLOW},
                    font_size=35).next_to(new_exp_text, DOWN, buff=0.2)
        new_explain_text = VGroup(new_exp_text, text).shift(
            RIGHT * 4.5)
        self.play(Create(new_explain_text))
        self.wait(1)
        self.play(FadeOut(step, example, explain, title))

        self.play(MoveAlongPath(new_explain_text, Line(RIGHT * 4.5, UP * 2)))
        final = Text(
            "明文 : 'RSA_Encode'(388769841913504470099045)\n密文 : b'M\\xb7\\xc6\\xba\\x1a'(333795736090)",
            t2c={"明文": BLUE_B, "密文": BLUE_B, "RSA_Encode": YELLOW, "M\\xb7\\xc6\\xba\\x1a": YELLOW,
                 "388769841913504470099045": GREEN, "333795736090": GREEN},
            font_size=40).shift(DOWN)
        self.play(Create(final))
        self.wait(2)
        self.play(FadeOut(final, new_explain_text))
        self.wait(2)

        title = Text("解密[已知公钥和私钥(N, e, d)]", font_size=50)
        self.play(Create(title))
        self.wait()
        new_title = Text("解密字符串b'M\\xb7\\xc6\\xba\\x1a'(333795736090)",
                         font_size=30).to_corner(UL, buff=0.7)
        self.play(Transform(title, new_title))

        rectangle = Rectangle(height=4, width=3).to_corner(DR, buff=0.5)
        explain_text = Text(
            '名词解释:',
            t2c={"名词解释": YELLOW},
            font_size=20).shift(RIGHT * 4.5)
        corner_explain = VGroup(rectangle, explain_text)

        step = Text("1. 分解N, 得到p, q.", t2c={
            "N": GREEN, "p": RED, "q": RED}, font_size=35).shift(UP * 2)
        explain = Text("Example:", font_size=20).shift(LEFT * 5 + UP)
        example = Text("N = 1,311,350,200,163\np = 1,145,141\nq = 1,145,143", t2c={
                       "p": BLUE_B, "q": BLUE_B, "N": BLUE_B, "1,145,141": YELLOW, "1,145,143": YELLOW, "1,311,350,200,163": YELLOW}, font_size=40).shift(LEFT * 2)
        self.play(Create(step), run_time=3)
        self.play(Create(explain), Create(example), Create(corner_explain))
        self.wait(4)

        exp1 = Text("由加密过程知", font_size=30).shift(UP * 1.5)
        process1 = Tex(
            "$c^{d}\\equiv m\\pmod{n}$ ··· (1)").shift(UP * 1)
        process2 = Tex("$m^{e}\\equiv c\\pmod{n}$ ··· (2)").shift(UP * 0.5)
        exp2 = Text("将式(2)代入式(1), 可得", font_size=30)
        process3 = Tex("$m^{ed}\\equiv m \\pmod{n} $",).shift(DOWN * 0.75)
        process3.color = RED
        self.play(FadeOut(corner_explain, step,
                  explain, example), FadeIn(exp1))
        self.wait()
        self.play(Write(process1))
        self.wait()
        self.play(Write(process2))
        self.wait()
        self.play(Write(exp2))
        self.wait()
        self.play(Write(process3))
        self.wait(3)
        self.play(FadeOut(exp1, exp2, process1, process2),
                  MoveAlongPath(process3, Line(
                      DOWN * 0.75, RIGHT * 5 + UP * 3)),
                  FadeIn(corner_explain, step, explain, example))

        new_step = Text("2. 根据费马小定理,求出\ned ≡ 1 (mod φ(N))", t2c={
                        "费马小定理": GREEN}, font_size=35).shift(UP * 2)
        new_explain_text = Text(
            "名词解释:\n\t费马小定理是数\n论中的一个重要定理:\n如果p是一个质数,而整\n数a不是p的倍数,则有",
            t2c={"名词解释": YELLOW},
            font_size=20).shift(RIGHT * 5.15 + DOWN)
        alg = Tex(
            "$a^{p-1}\\equiv 1\\pmod{p}$.").next_to(new_explain_text, DOWN, buff=0.3)
        alg.font_size = 30
        self.play(Transform(step, new_step), Transform(
            explain_text, new_explain_text), Write(alg))
        self.wait(4)

        new_step = Text("3. 可知e,d对于φ(N)互为逆元\n带入加密算法即可得出明文m.",
                        font_size=35).shift(UP * 2)
        self.play(Transform(step, new_step), FadeOut(
            alg, corner_explain, process3))
        self.wait(4)

        new_process0 = Tex("$m^{e}\\equiv c\\pmod{n}$").shift(UP * 2)
        new_process0.font_size = 50
        new_process0.color = LIGHT_BROWN
        new_process1 = Tex("$c^{d}\\equiv m\\pmod{n}$").next_to(
            new_process0, DOWN, buff=0.2)
        new_process1.font_size = 50
        new_process1.color = LIGHT_BROWN
        new_process2 = Tex("$m^{ed}\\equiv m \\pmod{n}$").next_to(
            new_process1, DOWN, buff=0.2)
        new_process2.font_size = 50
        new_process2.color = LIGHT_BROWN
        new_process3 = Tex(
            "$ed\\equiv 1\\pmod{\\varphi \\left ( N \\right )}$").next_to(new_process2, DOWN, buff=0.2)
        new_process3.font_size = 50
        new_process3.color = LIGHT_BROWN
        algi = VGroup(new_process0, new_process1, new_process2, new_process3)
        result = Text(
            "密文 : b'M\\xb7\\xc6\\xba\\x1a'(333795736090)\n明文 : 'RSA_Encode'(388769841913504470099045)",
            t2c={"明文": BLUE_B, "密文": BLUE_B, "RSA_Encode": YELLOW, "M\\xb7\\xc6\\xba\\x1a": YELLOW,
                 "388769841913504470099045": GREEN, "333795736090": GREEN},
            font_size=40).shift(DOWN)
        self.play(FadeOut(step, explain, example),
                  FadeIn(result, algi))
        self.wait(3)
        self.play(FadeOut(result, algi, title))
        self.wait(2)

        title = Text("  刚刚是一个较为简单的例子, \n现实中, 常见的加密长这样:", font_size=50)
        self.play(Write(title), run_time=3)
        self.wait(2)

        real_py = Code(
            "real.py",
            tab_width=4,
            background="window",
            insert_line_no=False,
            font="XHei NF",
            font_size=20
        )
        new_title = Text("加密 'RSA_encode' 的相关参数",
                         font_size=30).next_to(real_py, UP)
        self.play(Transform(title, new_title), Write(real_py))
        self.wait(2)
        self.play(FadeOut(title, real_py), run_time=3)
        self.wait(2)
        text = Text("近现代的加密算法大多立足于\n大数分解的极大困难度.\n\t\t\tRSA亦如此", font_size=50)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
        self.wait()
        bye = Text("感谢观看！\nThanks!", font_size=50)
        self.play(Write(bye), run_time=5)
        self.wait(3)
