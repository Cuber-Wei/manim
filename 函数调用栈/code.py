import numpy as np
from manim import *


class Stack(Scene):
    def construct(self):
        # 构建栈空间
        rectangle5 = Rectangle(height=0.5, width=4,)  # 创建一个矩形
        rectangle6 = Rectangle(height=0.5, width=4,).next_to(
            rectangle5, DOWN, buff=0)  # 创建一个矩形
        rectangle7 = Rectangle(height=0.5, width=4,).next_to(
            rectangle6, DOWN, buff=0)  # 创建一个矩形
        rectangle8 = Rectangle(height=0.5, width=4,).next_to(
            rectangle7, DOWN, buff=0)  # 创建一个矩形
        rectangle9 = Rectangle(height=0.5, width=4,).next_to(
            rectangle8, DOWN, buff=0)  # 创建一个矩形
        rectangle10 = Rectangle(height=0.5, width=4,).next_to(
            rectangle9, DOWN, buff=0)  # 创建一个矩形
        rectangle4 = Rectangle(height=0.5, width=4,).next_to(
            rectangle5, UP, buff=0)  # 创建一个矩形
        rectangle3 = Rectangle(height=0.5, width=4,).next_to(
            rectangle4, UP, buff=0)  # 创建一个矩形
        rectangle2 = Rectangle(height=0.5, width=4,).next_to(
            rectangle3, UP, buff=0)  # 创建一个矩形
        rectangle1 = Rectangle(height=0.5, width=4,).next_to(
            rectangle2, UP, buff=0)  # 创建一个矩形
        rectangle0 = Rectangle(height=0.5, width=4,).next_to(
            rectangle1, UP, buff=0)  # 创建一个矩形

        rectangle_group = VGroup(rectangle0, rectangle1, rectangle2, rectangle3, rectangle4, rectangle5,
                                 rectangle6, rectangle7, rectangle8, rectangle9, rectangle10)
        self.add(rectangle_group)  # 放置
        # 栈空间文本
        caller_bp1 = Text("调用者父函数bp", color=BLUE,
                          font_size=20).shift(0.5 * UP * 5)
        local_var1 = Text("局部变量", color=BLUE, font_size=20).shift(0.5 * UP * 4)
        ret_value1 = Text("返回值", color=BLUE, font_size=20).shift(0.5 * UP * 3)
        para1 = Text("参数", color=BLUE, font_size=20).shift(0.5 * UP * 2)

        stack = Text('栈底', font_size=30).next_to(rectangle0, UP)
        text = VGroup(caller_bp1, local_var1, ret_value1, para1, stack)
        self.play(Create(text))
        # 栈指针
        rbp_arrow = Arrow(np.array([-4, 2.5, 0]),
                          np.array([-2, 2.5, 0]))  # 代表rbp的箭头
        rbp_text = Text('RBP', font_size=20).next_to(
            rbp_arrow, LEFT)  # rbp箭头文本
        rsp_arrow = Arrow(np.array([-4, 1, 0]),
                          np.array([-2, 1, 0]),)  # 代表rsp的箭头
        rsp_text = Text('RSP', font_size=20).next_to(
            rsp_arrow, LEFT)  # rsp箭头文本
        rip = Text("RIP->指令1", font_size=30).to_corner(DL)
        rbp = VGroup(rbp_arrow, rbp_text)
        rsp = VGroup(rsp_arrow, rsp_text)
        # 描述性文本
        right_up = Text("高地址", font_size=30).to_corner(UR, buff=1)
        right_down = Text("低地址", font_size=30).to_corner(DR, buff=1)
        down_arrow = Arrow(np.array([5.5, 2.5, 0]),
                           np.array([5.5, -2.5, 0]))  # 地址描述中的下箭头
        addr_dsb = VGroup(right_up, down_arrow, right_down)
        describe_text = Text('入栈',
                             font_size=20).to_corner(UL, buff=0.5)
        self.play(Create(rbp), Create(addr_dsb), Create(rsp), Create(rip))
        self.play(Create(describe_text))
        self.wait(2)

        new_text = Text('Command: call [子函数]\n[ push rip\njmp\t]\n(rsp--\n rsp = *rip\n rip++ )',
                        font_size=20).to_corner(UL, buff=0.5)
        self.play(Transform(describe_text, new_text))
        self.wait(2)
        ret_addr = Text("返回地址", color=YELLOW, font_size=20).shift(0.5 * UP)
        new_rip = Text("RIP->指令2", font_size=30).to_corner(DL)
        self.play(
            Create(ret_addr),
            Transform(rip, new_rip),
            MoveAlongPath(
                rsp, Line(np.array([-3.5, 1, 0]), np.array([-3.45, 0.5, 0])))
        )
        self.wait(2)

        new_text = Text('Command: push rbp\nmov rbp,rsp\n(rsp--, rsp = *rbp, rbp = rsp)',
                        font_size=20).to_corner(UL, buff=0.5)
        self.play(Transform(describe_text, new_text))
        self.wait(2)
        caller_bp2 = Text("调用者函数bp", color=YELLOW,
                          font_size=20).shift(0.5 * DOWN * 0)
        self.play(
            Create(caller_bp2),
            MoveAlongPath(
                rsp, Line(np.array([-3.5, 0.5, 0]), np.array([-3.45, -0.1, 0]))),
            MoveAlongPath(
                rbp, Line(np.array([-3.5, 2.5, 0]), np.array([-3.45, 0.1, 0])))
        )
        self.wait(2)

        new_text = Text('Command: mov *par',
                        font_size=20).to_corner(UL, buff=0.5)
        self.play(Transform(describe_text, new_text))
        self.wait(2)
        local_var2 = Text("局部变量", color=YELLOW,
                          font_size=20).shift(0.5 * DOWN * 1)
        ret_value2 = Text("返回值", color=YELLOW,
                          font_size=20).shift(0.5 * DOWN * 2)
        para2 = Text("参数", color=YELLOW, font_size=20).shift(0.5 * DOWN * 3)
        stack_in = VGroup(local_var2, ret_value2, para2)
        self.play(
            Create(stack_in),
            MoveAlongPath(
                rsp, Line(np.array([-3.5, -0.1, 0]), np.array([-3.45, -1.5, 0])))
        )
        self.wait(2)

        new_text = Text('出栈', font_size=20).to_corner(UL, buff=0.5)
        self.play(Transform(describe_text, new_text))
        self.wait(2)

        new_text = Text('Command: mov rsp,rbp\n(rsp = rbp)',
                        font_size=20).to_corner(UL, buff=0.5)
        self.play(Transform(describe_text, new_text))
        self.wait(2)
        self.play(
            MoveAlongPath(
                rsp, Line(np.array([-3.45, -1.5, 0]), np.array([-3.45, -0.1, 0]))),
            FadeOut(stack_in)
        )
        self.wait(2)

        new_text = Text('Command: pop rbp\n(rbp = *rbp, rsp++)',
                        font_size=20).to_corner(UL, buff=0.5)
        self.play(Transform(describe_text, new_text))
        self.wait(2)
        self.play(
            MoveAlongPath(
                rbp, Line(np.array([-3.45, 0.1, 0]), np.array([-3.5, 2.5, 0]))),
            MoveAlongPath(
                rsp, Line(np.array([-3.45, 0, 0]), np.array([-3.45, 0.5, 0]))),
            FadeOut(caller_bp2)
        )
        self.wait(2)

        new_text = Text('Command: ret\n[ pop rip\nadd rsp,0x8 ]\n(rip = rsp, rsp++)',
                        font_size=20).to_corner(UL, buff=0.5)
        self.play(Transform(describe_text, new_text))
        self.wait(2)
        new_rip = Text("RIP->指令1", font_size=30).to_corner(DL)
        self.play(
            Transform(rip, new_rip),
            MoveAlongPath(
                rsp, Line(np.array([-3.45, 0.5, 0]), np.array([-3.5, 1, 0]))),
            FadeOut(ret_addr)
        )
        self.wait(2)
        '''
        new_text = Text('Command: push rbp',
                        font_size=20).to_corner(UL, buff=0)
        self.play(Transform(describe_text, new_text))
        self.play(MoveAlongPath(
            rbp, Line(np.array([-3.5, 2.5, 0]), np.array([-3.45, -1.5, 0]))))
        '''
