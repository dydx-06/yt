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

        integral = MathTex(r"\int_0^{\infty} e^{-x^2} \ln x\dd{x}",
            font_size=80, tex_template=temp)
        self.add(integral)

class Integral(Scene):
    def construct(self):

        # Initializing
        fontsize = 80
        delay = 0.6

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{physics}")

        # LaTeX Mobjects
        raw_latex = [
            r"\int_0^{\infty} e^{-x^2} \ln x \dd{x}", # 0
            r"I = \int_0^{\infty} e^{-x^2} \ln x \dd{x}",
            r"I(s) = \int_0^{\infty} x^se^{-x^2} \dd{x}",
            r"\dv{s} I(s) = \dv{s} \int_0^{\infty} x^se^{-x^2} \dd{x}",
            r"\dv{s} I(s) = \int_0^{\infty} \pdv{s} \left ( x^s e^{-x^2}\right ) \dd{x}",
            r"\dv{s} I(s) = \int_0^{\infty} x^s\ln(x)e^{-x^2} \dd{x}", # 5
            r"\dv{s} I(s) \eval_{s = 0} = \int_0^{\infty} x^0\ln(x)e^{-x^2} \dd{x}",
            r"I'(0) = I",
            r"I(s) = \int_0^{\infty} x^se^{-x^2} \dd{x}",
            r"\int_0^{\infty} x^se^{-x^2} \dd{x}",
            r"\frac 12 \int_0^{\infty} (x^2)^{(s - 1)/2}e^{-x^2} \cdot 2x\dd{x}", # 10
            r"\frac 12 \int_0^{\infty} x^{(s - 1)/2}e^{-x} \dd{x}",
            r"\frac 12 \int_0^{\infty} x^{(s - 1)/2}e^{-x} \dd{x}",
            r"\frac 12 \, \Gamma \left ( \frac{s + 1}{2} \right )",
            r"I(s) = \frac 12 \, \Gamma \left ( \frac{s + 1}{2} \right )",
            r"I'(0) = \frac 12 \, \Gamma' \left ( \frac{0 + 1}{2} \right )", # 15
            r"I = \frac 12 \, \Gamma' \left ( \frac 12 \right )",
            r"\frac 12 \, \Gamma' \left ( \frac 12 \right ) = \frac 12 \, \Gamma \left ( \frac 12 \right ) \psi \left ( \frac 12 \right )",
            r"\frac{\sqrt{\pi}}{4} \, \psi \left ( \frac 12 \right )",
            r"\frac{\sqrt{\pi}}{4} \left ( -\gamma + \sum_{k = 1}^{\infty} \frac 1k - \frac{1}{k - 1/2} \right )",
            r"\frac{\sqrt{\pi}}{4} \left ( - \gamma + \sum_{k = 1}^{\infty} \frac 1k - \frac{2}{2k - 1} \right )", # 20
            r"\frac{\sqrt{\pi}}{4} \left ( - \gamma + 2\sum_{k = 1}^{\infty} \frac 1{2k} - \frac 1{2k - 1} \right )",
            r"\frac{\sqrt{\pi}}{4} \left ( - \gamma + 2\sum_{k = 1}^{\infty} \frac{(-1)^k}{k} \right )",
            r"\frac{\sqrt{\pi}}{4} \left ( - \gamma - 2\ln 2 \right )",
            r"-\frac{\sqrt{\pi}}{4} \left ( \gamma + 2\ln 2 \right )",
            r"\int_0^{\infty} e^{-x^2} \ln x \dd{x} = -\frac{\sqrt{\pi}}{4} \left ( \gamma + 2\ln 2 \right )" # 25
        ]

        latex = [MathTex(i, font_size=fontsize, tex_template=temp) for i in raw_latex]

        # Notes and substitutions
        note1 = MathTex(r"I : \mathbb{R}^+ \cup \{ 0 \} \to \mathbb R",
                        font_size=0.75*fontsize, color=LIGHT_GREY, tex_template=temp).next_to(latex[1], 2*UP)
        sub1 = MathTex(r"x^2 = x",
                       font_size=0.75*fontsize, tex_template=temp).next_to(latex[10], 2*DOWN)
        diff1 = MathTex(r"2x\dd{x} = \dd{x}",
                        font_size=0.75*fontsize, tex_template=temp).next_to(sub1, DOWN)
        note2 = MathTex(r"\Gamma (z) = \int_0^{\infty} e^{-t}t^{z - 1} \dd{t}",
                        font_size=0.75*fontsize, color=LIGHT_GREY, tex_template=temp).next_to(latex[13], 2*DOWN)
        note3 = MathTex(r"(1) \; \psi (z) = \dv{z} \ln \Gamma (z) \text{ for $z > 0$}",
                        font_size=0.75*fontsize, color=LIGHT_GREY, tex_template=temp).next_to(latex[17], 2*DOWN)
        note4_1 = MathTex(r"\psi (1 + z) = -\gamma + \sum_{k = 1}^{\infty} \frac 1k - \frac{1}{k + z}",
                        font_size=0.75*fontsize, color=LIGHT_GREY, tex_template=temp).next_to(latex[19], 2*DOWN)
        note4_2 = MathTex(r"\text{(2) $\gamma$ denotes the Euler-Mascheroni constant}",
                        font_size=0.75*fontsize, color=LIGHT_GREY, tex_template=temp).next_to(note4_1, DOWN)

        # Mobject initialization
        for i in [3, 4, 5]: latex[i].scale(0.75)
        latex[6].scale(0.65)
        latex[10].scale(0.75)
        latex[17].scale(0.75)
        note3.scale(0.8)
        latex[19].scale(0.70)
        note4_1.scale(0.70)
        note4_2.scale(0.65)
        for i in [20, 21, 22]: latex[i].scale(0.70)
        latex[25].scale(0.60)

        latex[6][0][20].set_color(YELLOW)
        sub1[0][3].set_color(YELLOW)
        for i in [5, 6]: diff1[0][i].set_color(YELLOW)
        for i in [6, 16, 17, 18]: latex[11][0][i].set_color(YELLOW)
        for i in [3, 12]: latex[15][0][i].set_color(YELLOW)

        # Epilogue
        result_box = SurroundingRectangle(latex[25], color=YELLOW, buff=0.2)

        # Animation
        self.play(Write(latex[0]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[0], latex[1],
                ([], [0, 1])
            )
        )
        self.wait(delay)
        self.play(FadeOut(latex[1]))
        self.play(Write(latex[2]), FadeIn(note1))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[2], latex[3],
                ([], [0, 1, 2, 3, 9, 10, 11, 12])
            ),
            FadeOut(note1)
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[3], latex[4],
                ([9, 11], [12, 14]),
                ([10, 12], [13, 15]),
                ([], [16, 23])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[4], latex[5],
                (list(range(12, 24)), list(range(12, 23)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[5], latex[6],
                ([], list(range(8, 15))),
                ([13], [20])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[6], latex[7],
                (list(range(15)), [0, 1, 2, 3, 4]),
                (list(range(16, 32)), [6])
            )
        )
        self.wait(delay)
        self.play(FadeOut(latex[7]))
        self.play(Write(latex[8]))
        self.play(
            TransformByGlyphMap(
                latex[8], latex[9],
                ([0, 1, 2, 3, 4], [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[9], latex[10],
                ([], [0, 1, 2, 21, 22]),
                ([], [6, 9]),
                ([], [8, 10, 12, 13, 14, 15, 16, 23]),
                ([4], [11])
            )
        )
        self.play(Write(sub1))
        self.play(Write(diff1))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[10], latex[11],
                ([6, 8, 9, 20, 21, 22, 23], [])
            ),
            FadeOut(sub1), FadeOut(diff1)
        )
        self.play(
            TransformByGlyphMap(
                latex[11], latex[12],
                ([6], [6]),
                ([16], [16]),
                ([17, 18], [17, 18])
            )
        )
        self.play(
            TransformByGlyphMap(
                latex[12], latex[13],
                (list(range(3, 19)), list(range(3, 11)))
            ),
            FadeIn(note2)
        )
        self.play(
            TransformByGlyphMap(
                latex[13], latex[14],
                ([], [0, 1, 2, 3, 4])
            ),
            FadeOut(note2)
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[14], latex[15],
                ([2], [3]),
                ([10], [12]),
                ([], [1, 10])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[15], latex[16],
                ([1, 2, 3, 4, 12, 13], [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[16], latex[17],
                ([0, 1], []),
                ([1], [10]),
                (list(range(2, 12)), list(range(10))),
                ([], list(range(11, 26)))
            ),
            FadeIn(note3)
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[17], latex[18],
                (list(range(11)), []),
                (list(chain([11], range(14, 20))), [0, 1, 2]),
                ([12, 13], [3, 4])
            ),
            FadeOut(note3)
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[18], latex[19],
                (list(range(5, 11)), list(range(5, 26)))
            ),
            FadeIn(note4_1), FadeIn(note4_2)
        )
        self.wait(delay)
        self.play(FadeOut(note4_1), FadeOut(note4_2))
        self.play(
            TransformByGlyphMap(
                latex[19], latex[20],
                ([18], [18]),
                ([], [20]),
                ([23, 24], [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[20], latex[21],
                ([18], [20, 9]),
                ([], [17])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[21], latex[22],
                (list(range(15, 26)), list(range(15, 22)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[22], latex[23],
                (list(range(8, 22)), [8, 9, 10, 11, 12]),
                ([5, 22], [5, 13])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[23], latex[24],
                ([6, 8], [0]),
                ([], [8])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[24], latex[25],
                ([], list(range(13)))
            )
        )
        self.play(
            Create(result_box),
            ApplyWave(latex[25], amplitude=0.1, wavelength=0.2)
        )
        self.wait(3*delay)
