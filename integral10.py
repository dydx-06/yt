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

        integral = MathTex(r"\int_0^{\infty} \ln \left ( \frac{e^x + 1}{e^x - 1}\right ) \dd{x}",
            font_size=80, tex_template=temp)
        self.add(integral)

class Integral(Scene):
    def construct(self):

        # Initializing
        fontsize = 75
        delay = 0.6

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{physics}")

        # LateX
        raw_latex = [
            r"\int_0^{\infty} \ln \left ( \frac{e^x + 1}{e^x - 1}\right ) \dd{x}", # 0
            r"\int_0^{\infty} \ln \left ( \frac{1 + e^{-x}}{1 - e^{-x}} \right ) \dd{x}",
            r"-\int_0^{\infty} \frac{1}{e^{-x}} \ln \left ( \frac{1 + e^{-x}}{1 - e^{-x}} \right ) (-e^{-x})\dd{x}",
            r"-\int_1^0 \frac 1x \ln \left ( \frac{1 + x}{1 - x} \right ) \dd{x}",
            r"\int_0^1 \frac 1x \ln \left ( \frac{1 + x}{1 - x} \right ) \dd{x}",
            r"\int_1^{\infty} \frac{x + 1}{x - 1} \ln (x) \cdot \frac{2}{(x + 1)^2} \dd{x}", # 5
            r"2\int_1^{\infty} \frac{\ln (x)}{x^2 - 1} \dd{x}",
            r"2\int_1^{\infty} \frac{\ln (1/x)}{1 - (1/x)^2} \left ( - \frac 1{x^2} \right ) \dd{x}",
            r"2\int_1^0 \frac{\ln (x)}{1 - x^2} \dd{x}",
            r"-2\int_0^1 \frac{\ln (x)}{1 - x^2} \dd{x}",
            r"-2\int_0^1 \ln (x) \sum_{k=0}^{\infty} (x^2)^k \dd{x}", # 10
            r"-2\sum_{k=0}^{\infty} \int_0^1 x^{2k}\ln (x) \dd{x}",
            r"-2\sum_{k = 0}^{\infty} \left \{ \frac{x^{2k+1}}{2k + 1} \ln (x) \eval_0^1 - \frac{1}{2k + 1} \int_0^1 x^{2k} \dd{x}\right \}",
            r"-2\sum_{k = 0}^{\infty} \left \{ 0 -\frac{1}{(2k + 1)^2}\right \}",
            r"2\sum_{k=0}^{\infty} \frac{1}{(2k + 1)^2}",
            r"2\sum_{k=1}^{\infty} \frac{1}{k^2} - 2\sum_{k=1}^{\infty} \frac{1}{(2k)^2}", # 15
            r"2\sum_{k=1}^{\infty} \frac 1{k^2} - \frac 12 \sum_{k=1}^{\infty} \frac 1{k^2}",
            r"\frac 32 \sum_{k=1}^{\infty} \frac 1{k^2}",
            r"\frac 32 \cdot \frac{\pi^2}{6}",
            r"\frac{\pi^2}{4}",
            r"\int_0^{\infty} \ln \left ( \frac{e^x + 1}{e^x - 1} \right ) \dd{x} = \frac{\pi^2}{4}" # 20
        ]

        latex = [MathTex(i, font_size=fontsize, tex_template=temp) for i in raw_latex]

        # Substitutions and notes
        sub1 = MathTex(r"e^{-x} = x",
            font_size=0.70*fontsize, tex_template=temp).next_to(latex[2], 1.5*DOWN)
        sub1_diff = MathTex(r"-e^{-x} \dd{x} = \dd{x}",
            font_size=0.70*fontsize, tex_template=temp).next_to(sub1, DOWN)
        sub2_1 = MathTex(r"\frac{1 + x}{1 - x} = x",
            font_size=0.70*fontsize, tex_template=temp).next_to(latex[4], 1.5*DOWN)
        sub2_2 = MathTex(r"\frac{x - 1}{x + 1} = x",
            font_size=0.70*fontsize, tex_template=temp).next_to(latex[4], 1.5*DOWN)
        sub2_diff = MathTex(r"\frac{2}{(x + 1)^2}\dd{x} = \dd{x}",
            font_size=0.70*fontsize, tex_template=temp).next_to(sub2_2, DOWN)
        sub3 = MathTex(r"\frac 1x = x",
            font_size=0.70*fontsize, tex_template=temp).next_to(latex[7], 1.5*DOWN)
        sub3_diff = MathTex(r"- \frac 1{x^2} \dd{x} = \dd{x}",
            font_size=0.70*fontsize, tex_template=temp).next_to(sub3, DOWN)
        note1 = MathTex(r"\frac{1}{1 - z} = \sum_{k = 0}^{\infty} z^k \text{ for $|z| < 1$}",
            font_size=0.70*fontsize, tex_template=temp, color=LIGHT_GREY).next_to(latex[10], 1.5*DOWN)


        # Mobject initialization
        latex[2].scale(0.70)
        latex[3].shift(UP)
        latex[4].shift(UP)
        latex[5].shift(UP).scale(0.80)
        latex[6].shift(UP)
        latex[7].shift(UP).scale(0.80)
        latex[12].scale(0.55)
        latex[20].scale(0.90)

        # Coloring
        sub1[0][4].set_color(YELLOW)
        for i in [7, 8]: sub1_diff[0][i].set_color(YELLOW)
        for i in [2, 3, 6, 12, 16, 18, 19]: latex[3][0][i].set_color(YELLOW)
        sub2_1[0][8].set_color(YELLOW)
        for i in [0, 4]: sub2_2[0][i].set_color(YELLOW)
        for i in range(10): sub2_diff[0][i].set_color(YELLOW)
        for i in chain([1, 2, 5, 9, 13], range(16, 26)): latex[5][0][i].set_color(YELLOW)
        sub3[0][4].set_color(YELLOW)
        for i in [8, 9]: sub3_diff[0][i].set_color(YELLOW)
        for i in [2, 3, 7, 12, 14, 15]: latex[8][0][i].set_color(YELLOW)

        # Epilogue
        result_box = SurroundingRectangle(latex[20], color=YELLOW, buff=0.2)

        # Animation
        self.play(Write(latex[0]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[0], latex[1],
                ([6, 7], [8, 9, 10]),
                ([9], [6]),
                ([11, 12], [14, 15, 16]),
                ([14], [12])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[1], latex[2],
                ([], [0, 4, 5, 6, 7, 8, 24, 25, 26, 27, 28, 29])
            )
        )
        self.wait(delay)
        self.play(latex[2].animate.shift(UP))
        self.play(Write(sub1))
        self.play(Write(sub1_diff))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[2], latex[3],
                ([2], [2]),
                ([3], [3]),
                ([6, 7, 8], [6]),
                ([14, 15, 16], [12]),
                ([20, 21, 22], [16]),
                (list(range(24, 32)), [18, 19])
            ),
            FadeOut(sub1), FadeOut(sub1_diff)
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[3], latex[4],
                ([0], []),
                ([2], [1]),
                ([3], [2])
            )
        )
        self.wait(delay)
        self.play(Write(sub2_1))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                sub2_1, sub2_2,
                ([0, 4], [8]),
                ([8], [0, 4])
            )
        )
        self.play(Write(sub2_diff))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[4], latex[5],
                ([1], [1]),
                ([2], [2]),
                ([3, 4, 5], list(range(3, 10))),
                (list(range(9, 16)), [13]),
                ([17, 18], list(range(15, 26)))
            ),
            FadeOut(sub2_2), FadeOut(sub2_diff)
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[5], latex[6],
                ([3, 4, 5, 7, 8, 9, 18, 19, 20, 21, 22, 23], [10, 11, 12, 13]),
                ([6], [9]),
                ([15, 17], []),
                ([16], [0])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[6], latex[7],
                ([7], [7, 8, 9, 21]),
                ([12, 13], [19, 22, 23, 24, 25]),
                ([10], [12, 13, 14, 15, 16, 17]),
                ([], [20, 26])
            )
        )
        self.wait(delay)
        self.play(Write(sub3))
        self.play(Write(sub3_diff))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[7], latex[8],
                ([2], [2]),
                ([3], [3]),
                ([7, 8, 9], [7]),
                ([12, 13, 14, 15, 16], [10]),
                (list(range(20, 29)), [14, 15])
            ),
            FadeOut(sub3), FadeOut(sub3_diff)
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[8], latex[9],
                ([], [0]),
                ([2], [3]),
                ([3], [4])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[9], latex[10],
                (list(range(9, 14)), list(range(9, 19)))
            ),
            FadeIn(note1)
        )
        self.wait(delay)
        self.play(FadeOut(note1))
        self.play(
            TransformByGlyphMap(
                latex[10], latex[11],
                ([2, 3, 4], [7, 8, 9]),
                (list(range(5, 10)), list(range(13, 18))),
                (list(range(10, 15)), list(range(2, 7))),
                ([15, 18], []),
                ([16, 17, 19], [10, 11, 12])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[11], latex[12],
                ([], [7, 29, 44]),
                ([7], [23, 24, 25, 26, 36]),
                ([8, 9], [27, 28, 37, 38]),
                ([10], [8, 39]),
                ([11, 12], list(chain(range(9, 18), range(30, 36), [40, 41]))),
                ([13, 14, 15, 16, 17], [18, 19, 20, 21, 22])
            )
        )
        self.wait(2*delay)
        self.play(
            TransformByGlyphMap(
                latex[12], latex[13],
                ([7, 44], [7, 19]),
                (list(range(8, 29)), [8]),
                ([29], [9]),
                (list(range(30, 36)), list(range(10, 18))),
                (list(range(36, 44)), [18])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[13], latex[14],
                ([0, 7, 8, 9, 19], [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[14], latex[15],
                (list(range(6)), list(chain(range(6), range(11, 17)))),
                (list(range(6, 15)), list(chain(range(6, 10), [10], range(17, 24))))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[15], latex[16],
                ([11, 20], [11, 12, 13]),
                ([19, 22], [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[16], latex[17],
                (list(chain(range(1, 10), range(14, 23))), list(range(3, 12))),
                ([0, 10, 11, 12, 13], [0, 1, 2])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[17], latex[18],
                (list(range(3, 12)), [3, 4, 5, 6, 7])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[18], latex[19],
                ([0, 1, 2, 3, 7], [3])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[19], latex[20],
                ([], list(range(19))),
                ([0, 1, 2, 3], [19, 20, 21, 22])
            )
        )
        self.play(
            Create(result_box),
            ApplyWave(latex[20], amplitude=0.1, wavelength=0.2)
        )
        self.wait(3*delay)
