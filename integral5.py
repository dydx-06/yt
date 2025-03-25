from manim import *
from MF_Tools import TransformByGlyphMap
from itertools import chain

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 2560
config.pixel_width = 1440

class Thumbnail(Scene):
    def construct(self):
        integral = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} \, dx",
            font_size=90)
        self.add(integral)

class Integral(Scene):
    def construct(self):

        # Initializing
        fontsize = 60
        delay = 0.5
        scale = 0.8

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{physics}")

        # LaTeX
        raw_latex = [
            r"\int_{-\infty}^{\infty} e^{-x^2} \dd{x}",
            r"I(t) = \left ( \int_{0}^{t} e^{-x^2} \dd{x} \right )^2",
            r"\int_{-\infty}^{\infty} e^{-x^2} \dd{x} = 2\left (\lim_{t \to \infty} I(t) \right )^{\frac 12}",
            r"\dv{t} I(t) = \dv{t} \left ( \int_{0}^{t} e^{-x^2} \dd{x} \right )^2",
            r"\dv{t} I(t) = 2\int_0^t e^{-x^2} \dd{x} \cdot \dv{t} \int_0^t e^{-x^2} \dd{x}",
            r"\dv{t} I(t) = 2\int_0^t e^{-x^2} \dd{x} \cdot e^{-t^2}", # 5
            r"\dv{t} I(t) = 2\int_0^t e^{- t^2 - x^2} \dd{x}",
            r"\dv{t} I(t) = 2\int_0^1 e^{-t^2 - (tx)^2} t\dd{x}",
            r"\dv{t} I(t) = 2\int_0^1 te^{-t^2 - t^2x^2} \dd{x}",
            r"\dv{t} I(t) = \int_0^1 2te^{-(1 + x^2)t^2} \dd{x}",
            r"\dv{t} I(t) = \int_0^1 -\pdv{t} \left ( \frac{e^{-(1 + x^2)t^2}}{1 + x^2}\right ) \dd{x}", # 10
            r"\dv{t} I(t) = \dv{t} \int_0^1 - \frac{e^{-(1 + x^2)t^2}}{1 + x^2} \dd{x}",
            r"\int \dv{t} I(t) \dd{t} = \int \left ( \dv{t} \int_0^1 - \frac{e^{-(1 + x^2)t^2}}{1 + x^2} \dd{x} \right ) \dd{t}",
            r"I(t) = -\int_0^1 \frac{e^{-(1 + x^2)t^2}}{1 + x^2} \dd{x} + C",
            r"I(t) = \left ( \int_0^t e^{-x^2} \dd{x} \right )^2",
            r"I(0) = \left ( \int_0^0 e^{-x^2} \dd{x} \right )^2", # 15
            r"I(0) = 0",
            r"I(0) = -\int_0^1 \frac{e^{-(1 + x^2) \cdot 0}}{1 + x^2} \dd{x} + C",
            r"0 = -\int_0^1 \frac{1}{1 + x^2} \dd{x} + C",
            r"0 = - \tan^{-1}(x) \eval_0^1 + C",
            r"0 = - \frac{\pi}{4} + C", # 20
            r"C = \frac{\pi}{4}",
            r"I(t) = -\int_0^1 \frac{e^{-(1 + x^2)t^2}}{1 + x^2} \dd{x} + \frac{\pi}{4}",
            r"\lim_{t \to \infty} I(t) = \lim_{t \to \infty} -\int_0^1 \frac{e^{-(1 + x^2)t^2}}{1 + x^2} \dd{x} + \frac{\pi}{4}",
            r"\lim_{t \to \infty} I(t) = -\int_0^1 \lim_{t \to \infty} \frac{e^{-(1 + x^2)t^2}}{1 + x^2} \dd{x} + \frac{\pi}{4}",
            r"\lim_{t \to \infty} I(t) = -\int_0^1 \frac{0}{1 + x^2} \dd{x} + \frac{\pi}{4}", # 25
            r"\lim_{t \to \infty} I(t) = \frac{\pi}{4}",
            r"\int_{-\infty}^{\infty} e^{-x^2} \dd{x} = 2\left (\lim_{t \to \infty} I(t) \right )^{\frac 12}",
            r"\int_{-\infty}^{\infty} e^{-x^2} \dd{x} = 2\left (\frac{\pi}{4}\right )^{\frac 12}",
            r"\int_{-\infty}^{\infty} e^{-x^2} \dd{x} = \sqrt{\pi}",
        ]

        latex = [MathTex(i, font_size=fontsize, tex_template=temp) for i in raw_latex]
        result_box = SurroundingRectangle(latex[29], color=YELLOW, buff=0.2)

        # Substitutions and notes
        note1 = MathTex(r"I : \mathbb R \to \mathbb R",
                    font_size=fontsize/1.5, color=LIGHT_GREY).next_to(latex[1], DOWN*2)
        sub1 = MathTex(r"x = tx",
                    font_size=fontsize, substrings_to_isolate=[r"tx"]).next_to(latex[6], DOWN*2)
        sub1_diff = MathTex(r"\dd{x} = t\dd{x}",
                    font_size=fontsize, tex_template=temp, substrings_to_isolate=[r"t\dd{x}"]).next_to(sub1, DOWN)

        # Mobject initialization
        for i in [2, 4, 10, 11, 13, 14, 15, 16, 17, 22, 25]: latex[i].scale(scale)
        for i in [12, 23, 24]: latex[i].scale(0.6)
        for i in [14, 15, 16]: latex[i].next_to(latex[13], DOWN*2)

        # Coloring
        sub1.set_color_by_tex(r"tx", YELLOW)
        sub1_diff.set_color_by_tex(r"t\dd{x}", YELLOW)
        for i in [11, 19, 20, 23, 24, 25]: latex[7][0][i].set_color(YELLOW)
        for i in [2, 7]: latex[15][0][i].set_color(YELLOW)
        for i in [13, 14, 15]: latex[28][0][i].set_color(YELLOW)

        # Animation
        self.play(Write(latex[0]))
        self.wait(delay)
        self.play(Unwrite(latex[0]))
        self.play(
            Write(latex[1]),
            FadeIn(note1)
        )
        self.play(FadeOut(note1))
        self.wait(delay)
        self.play(latex[1].animate.shift(UP*2.5))
        self.play(Write(latex[2]))
        self.wait(delay)
        self.play(FadeOut(latex[2]))
        self.play(latex[1].animate.shift(DOWN*2.5))
        self.play(
            TransformByGlyphMap(
                latex[1], latex[3],
                ([], list(chain(range(4), range(9, 13))))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[3], latex[4],
                (list(range(9, 13)), list(range(19, 24))),
                ([13, 23], []),
                ([24], [9]),
                (list(range(14, 23)), list(chain(range(10, 19), range(24, 33))))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[4], latex[5],
                (list(range(20, 33)), list(range(20, 24)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[5], latex[6],
                (list(range(19, 24)), [14, 15, 16])
            )
        )
        self.wait(delay)
        self.play(Write(sub1))
        self.play(Write(sub1_diff))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[6], latex[7],
                ([11], [11]),
                ([18], list(range(18, 22))),
                ([20, 21], [23, 24, 25])
            ),
            FadeOut(sub1, sub1_diff)
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[7], latex[8],
                ([18, 21], []),
                ([19], [19]),
                ([20], [21]),
                ([22], [20, 22]),
                ([23], [13])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[8], latex[9],
                ([9], [12]),
                ([15, 18], [15, 18]),
                ([16, 17, 19, 20], [22, 23]),
                ([21, 22], [17, 19, 20]),
                ([], [16, 21])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[9], latex[10],
                (list(range(14, 24)), list(range(18, 28))),
                ([12, 13], []),
                ([], list(chain(range(12, 18), range(28, 34))))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[10], latex[11],
                ([12], [16]),
                (list(range(13, 17)), list(range(9, 13))),
                ([17, 33], [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[11], latex[12],
                ([], [0, 9, 10, 12, 13, 39, 40, 41])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[12], latex[13],
                (list(chain(range(5), [9, 10], range(12, 18), [39, 40, 41])), []),
                ([21], [5]),
                ([], [26, 27])
            )
        )
        self.wait(delay)
        self.play(Write(latex[14]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[14], latex[15],
                ([2], [2]),
                ([7], [7])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[15], latex[16],
                (list(range(5, 17)), [5])
            )
        )
        self.wait(delay)
        self.play(FadeOut(latex[16]))
        self.play(
            TransformByGlyphMap(
                latex[13], latex[17],
                ([2], [2]),
                ([17, 18], [17, 18])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[17], latex[18],
                ([0, 1, 3], []),
                (list(range(9, 19)), [6])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[18], latex[19],
                (list(range(3, 14)), list(range(3, 17)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[19], latex[20],
                (list(range(3, 17)), [3, 4, 5])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[20], latex[21],
                ([0, 7], [0]),
                ([2, 6], [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[21], latex[22],
                ([0, 1], []),
                ([2, 3, 4], [27, 28, 29]),
                ([], list(range(27)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[22], latex[23],
                ([], list(chain(range(6), range(11, 17))))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[23], latex[24],
                (list(range(11, 17)), list(range(15, 21)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[24], latex[25],
                (list(range(15, 31)), [15])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[25], latex[26],
                (list(range(11, 24)), [])
            )
        )
        self.play(latex[26].animate.shift(DOWN*2))
        self.play(Write(latex[27]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[27], latex[28],
                (list(range(13, 23)), [13, 14, 15])
            ),
            FadeOut(latex[26])
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[28], latex[29],
                ([11, 12, 14, 15, 16], []),
                ([17, 18, 19], [11, 12])
            )
        )
        self.play(
            Create(result_box),
            ApplyWave(latex[29], amplitude =0.1, wavelength=0.3)
        )
        self.wait(delay)
