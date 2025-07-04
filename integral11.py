from manim import *
from MF_Tools import TransformByGlyphMap
from itertools import chain

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 2560
config.pixel_width = 1440

class Thumbnail(Scene):
    def construct(self):

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{physics}")

        integral = MathTex(r"\int_0^{\infty} \sin (x^2) \dd{x} \\ \\ \int_0^{\infty} \cos (x^2) \dd{x}",
            font_size=60, tex_template=temp)
        self.add(integral)

class Integral(Scene):
    def construct(self):

        # Initializing
        fontsize = 75
        delay = 0.6

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{physics}")

        # LaTeX
        raw_latex = [
            r"\int_0^{\infty} e^{ix^2}\dd{x}", # 0
            r"I = \int_0^{\infty} e^{ix^2}\dd{x}",
            r"\int_0^{\infty} \cos (x^2) \dd{x}",
            r"\int_0^{\infty} \sin (x^2) \dd{x}",
            r"I_1 = \int_0^{\infty} \cos (x^2) \dd{x}",
            r"I_2 = \int_0^{\infty} \sin (x^2) \dd{x}", # 5
            r"I_1 = \Re I",
            r"I_2 = \Im I",
            r"I = \frac 12 \int_0^{\infty} (x^2)^{-1/2}e^{ix^2} 2x\dd{x}",
            r"I = \frac 12 \int_0^{\infty} x^{-1/2}e^{ix} \dd{x}",
            r"I = \frac 12 \int_0^{\infty} x^{-1/2}e^{ix} \dd{x}", # 10
            r"J(s) = \int_0^{\infty} x^{-1/2}e^{-sx} \dd{x}",
            r"I = \frac 12 \lim_{\varepsilon \to 0^+} \hat{J} (-i + \varepsilon)",
            r"J(s) = s^{-1/2}\int_0^{\infty} (sx)^{-1/2}e^{-sx}s\dd{x}",
            r"J(s) = s^{-1/2}\int_0^{\infty} x^{-1/2}e^{-x}\dd{x}",
            r"J(s) = s^{-1/2}\Gamma \Big ( \frac 12 \Big )", # 15
            r"J(s) = \sqrt{\pi}s^{-1/2}",
            r"\frac 12 \lim_{\varepsilon \to 0^+} \hat{J} (-i + \varepsilon) = \frac 12 \lim_{\varepsilon \to 0^+} \sqrt{\pi}(-i + \varepsilon)^{-1/2}",
            r"I = \frac{\sqrt{\pi}}{2} \lim_{\varepsilon \to 0^+} (-i + \varepsilon)^{-1/2}",
            r"I = \frac{\sqrt{\pi}}{2} (-i)^{-1/2}",
            r"I = \frac{\sqrt{\pi}}{2} \left ( e^{-i\pi/2}\right )^{-1/2}", # 20
            r"I = \frac{\sqrt{\pi}}{2}e^{i\pi/4}",
            r"I = \frac{\sqrt{\pi}}{2} \left ( \frac{1}{\sqrt{2}} + \frac{i}{\sqrt{2}} \right )",
            r"I = \sqrt{\frac{\pi}{8}} + i\sqrt{\frac{\pi}{8}}",
            r"I_1 = \Re I",
            r"I_2 = \Im I", # 25
            r"I_1 = \sqrt{\frac{\pi}{8}}",
            r"I_2 = \sqrt{\frac{\pi}{8}}",
            r"I_1 = I_2 = \sqrt{\frac{\pi}{8}}",
            r"\int_0^{\infty} \cos (x^2) \dd{x} = \int_0^{\infty} \sin (x^2)\dd{x} = \sqrt{\frac{\pi}{8}}"
        ]

        latex = [MathTex(i, font_size=fontsize, tex_template=temp) for i in raw_latex]

        # Substitutions
        sub1 = MathTex(r"x^2 = x",
            font_size=fontsize*0.75, tex_template=temp).next_to(latex[8], DOWN*1.5)
        sub1_diff = MathTex(r"2x\dd{x} = \dd{x}",
            font_size=fontsize*0.75, tex_template=temp).next_to(sub1, DOWN)
        func1 = MathTex(r"J : \mathbb{R}^+ \to \mathbb{R}",
            font_size=fontsize*0.75, tex_template=temp, color=LIGHT_GREY).next_to(latex[11], UP*1.5)
        note1 = Tex(r"\text{$\hat{J}$ denotes an apt analytic continuation for $J$",
            font_size=fontsize*0.75, tex_template=temp, color=LIGHT_GREY)
        sub2 = MathTex(r"sx = x",
            font_size=fontsize*0.75, tex_template=temp).next_to(latex[13], DOWN*1.5)
        sub2_diff = MathTex(r"s\dd{x} = \dd{x}",
            font_size=fontsize*0.75, tex_template=temp).next_to(sub2, DOWN)
        note2 = MathTex(r"\Gamma : z \mapsto \int_0^{\infty} e^{-t}t^{z-1}\dd{t}",
            font_size=fontsize*0.75, tex_template=temp, color=LIGHT_GREY).next_to(latex[15], DOWN*1.5)

        # Mobject initialization
        for i in range(2, 8):
            if i % 2 == 0: latex[i].shift(UP*3)
            else: latex[i].shift(DOWN*3)
        latex[8].scale(0.8)
        latex[10].shift(UP*5)
        latex[11].scale(0.9)
        latex[12].next_to(latex[11], DOWN*2)
        note1.scale(0.7).next_to(latex[12], DOWN*1.5)
        latex[13].scale(0.7)
        latex[14].scale(0.8)
        latex[17].scale(0.55)
        latex[18].scale(0.95)
        for i in range(24, 28):
            if i % 2 == 0: latex[i].shift(UP*3)
            else: latex[i].shift(DOWN*3)
        latex[29].scale(0.6)

        # Coloring
        sub1[0][3].set_color(YELLOW)
        for i in [5, 6]: sub1_diff[0][i].set_color(YELLOW)
        for i in [8, 15, 16, 17]: latex[9][0][i].set_color(YELLOW)
        sub2[0][3].set_color(YELLOW)
        for i in [4, 5]: sub2_diff[0][i].set_color(YELLOW)
        for i in [13, 20, 21, 22]: latex[14][0][i].set_color(YELLOW)

        # Epilogue
        result_box = SurroundingRectangle(latex[29], color=YELLOW, buff=0.2)

        # Animation
        self.play(
            Write(latex[2]),
            Write(latex[3])
        )
        self.wait(delay)
        self.play(Write(latex[0]))
        self.play(
            TransformByGlyphMap(
                latex[2], latex[4],
                ([], [0, 1, 2])
            ),
            TransformByGlyphMap(
                latex[3], latex[5],
                ([], [0, 1, 2])
            ),
            TransformByGlyphMap(
                latex[0], latex[1],
                ([], [0, 1])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[4], latex[6],
                (list(range(3, 15)), [3, 4, 5])
            ),
            TransformByGlyphMap(
                latex[5], latex[7],
                (list(range(3, 15)), [3, 4, 5])
            )
        )
        self.wait(delay)
        self.play(
            FadeOut(latex[6]),
            FadeOut(latex[7])
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[1], latex[8],
                ([], list(chain([2, 3, 4], range(8, 16), [20, 21]))),
                ([9, 10], [22, 23])
            )
        )
        self.play(Write(sub1))
        self.play(Write(sub1_diff))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[8], latex[9],
                ([8, 9, 10, 11], [8]),
                ([18, 19], [15]),
                ([20, 21, 22, 23], [16, 17])
            ),
            FadeOut(sub1),
            FadeOut(sub1_diff)
        )
        self.wait(delay)
        self.play(latex[9].animate.shift(UP*5))
        self.play(
            TransformByGlyphMap(
                latex[9], latex[10],
                ([8], [8]),
                ([15], [15]),
                ([16], [16]),
                ([17], [17])
            )
        )
        self.play(
            Write(latex[11]),
            FadeIn(func1)
        )
        self.wait(delay)
        self.play(
            Write(latex[12]),
            FadeIn(note1)
        )
        self.wait(delay*2)
        self.play(
            latex[12].animate.shift(UP*7),
            note1.animate.shift(UP*7),
            FadeOut(func1),
            FadeOut(latex[10])
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[11], latex[13],
                ([], [5, 6, 7, 8, 9, 13, 14, 16, 25])
            )
        )
        self.wait(delay)
        self.play(Write(sub2))
        self.play(Write(sub2_diff))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[13], latex[14],
                ([13, 14, 15, 16], [13]),
                ([23, 24], [20]),
                ([25, 26, 27], [21, 22])
            ),
            FadeOut(sub2),
            FadeOut(sub2_diff)
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[14], latex[15],
                (list(range(10, 23)), list(range(10, 16)))
            ),
            FadeIn(note2)
        )
        self.wait(delay)
        self.play(FadeOut(note2))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[15], latex[16],
                (list(range(5, 10)), list(range(8, 13))),
                (list(range(10, 16)), [5, 6, 7])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[16], latex[17],
                ([], list(chain(range(11), range(19, 29)))),
                ([2], [13, 14, 15, 16]),
                ([8], [32, 33, 34, 35, 36, 37])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[17], latex[18],
                (list(range(18)), [0]),
                ([19, 29, 30, 31], [2, 3, 4])
            ),
            FadeOut(latex[12]),
            FadeOut(note1)
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[18], latex[19],
                (list(chain(range(7, 14), [17, 18])), [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[19], latex[20],
                ([8, 9], list(range(8, 14))),
                ([7], [7]),
                ([10], [14])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[20], latex[21],
                ([7, 14], []),
                (list(chain(range(9, 14), range(15, 19))), [8, 9, 10, 11])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[21], latex[22],
                ([7, 8, 9, 10, 11], list(range(7, 20)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[22], latex[23],
                ([7, 19], []),
                ([14], [8]),
                (list(chain(range(2, 7), range(8, 13), range(15, 19))), list(chain(range(2, 7), range(9, 14))))
            )
        )
        self.wait(delay)
        self.play(
            Write(latex[24]),
            Write(latex[25])
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[24], latex[26],
                ([3, 4, 5], [3, 4, 5, 6, 7])
            ),
            TransformByGlyphMap(
                latex[25], latex[27],
                ([3, 4, 5], [3, 4, 5, 6, 7])
            ),
            FadeOut(latex[23])
        )
        self.wait(delay)
        self.play(
            FadeOut(latex[26], shift=ORIGIN - latex[26].get_center()),
            FadeOut(latex[27], shift=ORIGIN - latex[27].get_center()),
            FadeIn(latex[28])
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[28], latex[29],
                ([0, 1], list(range(12))),
                ([3, 4], list(range(13, 25)))
            )
        )
        self.wait(delay)
        self.play(
            Create(result_box),
            ApplyWave(latex[29], amplitude=0.1, wavelength=0.2)
        )
        self.wait(delay*3)
