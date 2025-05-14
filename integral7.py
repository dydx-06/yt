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

        integral = MathTex(r" \int_0^{\infty} \frac{1}{\big ( \{ x\}\mathrm{lcm} \, (\lceil x\rceil, \lfloor 1/\{ x\}\rfloor) \big )^2} \dd{x}",
            font_size=50, tex_template=temp)
        self.add(integral)

class Integral(Scene):
    def construct(self):

        # Initializing
        fontsize = 50
        delay = 0.6
        scale = 0.75

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{physics}")

        # LaTeX
        raw_latex = [
            r"\int_0^{\infty} \frac{1}{\big ( \{x\}\mathrm{lcm} \, (\lceil x\rceil, \lfloor 1/\{ x\}\rfloor) \big )^2} \dd{x}",
            r"\int_0^{\infty} \big ( \{x\} \mathrm{lcm} \, (\lceil x \rceil, \lfloor 1/\{x\} \rfloor )\big )^{-2} \dd{x}",
            r"\sum_{i = 0}^{\infty} \int_i^{i+1} \big ( \{x\} \mathrm{lcm} \, (i + 1, \lfloor 1/\{x\} \rfloor)\big )^{-2} \dd{x}",
            r"\sum_{i = 0}^{\infty} \int_i^{i+1} \big ( (x - \lfloor x \rfloor) \, \mathrm{lcm} \, (i + 1, \lfloor 1/(x - \lfloor x \rfloor) \rfloor )\big )^{-2} \dd{x}",
            r"\sum_{i = 0}^{\infty} \int_i^{i+1} \big ( (x - i) \, \mathrm{lcm} \, (i + 1, \lfloor 1/(x - i) \rfloor )\big )^{-2} \dd{x}",
            r"\sum_{i = 0}^{\infty} \int_1^{\infty} \big ( \mathrm{lcm} \, (i + 1, \lfloor x \rfloor ) \big )^{-2} \dd{x}", # 5
            r"\sum_{i = 0}^{\infty} \sum_{j = 1}^{\infty} \int_j^{j+1} \big ( \mathrm{lcm} \, (i + 1, \, j)\big )^{-2} \dd{x}",
            r"\sum_{i = 1}^{\infty} \sum_{j = 1}^{\infty} \int_j^{j+1} \big ( \mathrm{lcm} \, (i, \, j) \big )^{-2} \dd{x}",
            r"\sum_{i = 1}^{\infty} \sum_{j = 1}^{\infty} \frac{1}{\big (\mathrm{lcm} \, (i, \, j)\big )^2}",
            r"\underset{1 \leq t \leq n}{\sum_{a_s \geq 0}} \; \underset{1 \leq s \leq n}{\sum_{b_t \geq 0}} \frac{1}{\big (p_1^{\max (a_1, b_1)} p_2^{\max (a_2, b_2)} \cdots p_n^{\max (a_n, b_n)} \big )^2}",
            r"\left ( \sum_{a_1, b_1 \geq 0} \frac{1}{p_1^{2\max (a_1, b_1)}}\right ) \left (\sum_{a_2, b_2 \geq 0} \frac{1}{p_2^{2\max (a_2, b_2)}} \right ) \cdots \left ( \sum_{a_n, b_n \geq 0} \frac{1}{p_n^{2\max (a_n, b_n)}}\right )", # 10
            r"\prod_{p} \sum_{a, b \geq 0} \frac{1}{p^{2\max (a, b)}}",
            r"\prod_p \left ( \underbrace{\sum_{a = 0}^{\infty} \frac{1}{p^{2a}}}_{a \, = \, b} + \underbrace{\sum_{b = 1}^{\infty} \sum_{a = 0}^{b - 1} \frac{1}{p^{2b}}}_{a \, < \, b} + \underbrace{\sum_{a = 1}^{\infty} \sum_{b = 0}^{a - 1} \frac{1}{p^{2a}}}_{a \, > \, b}\right )",
            r"\prod_p \left ( \sum_{a = 0}^{\infty} \frac{1}{p^{2a}} + \sum_{b = 1}^{\infty} \sum_{a = 0}^{b - 1} \frac{1}{p^{2b}} + \sum_{b = 1}^{\infty} \sum_{a = 0}^{b - 1} \frac{1}{p^{2b}}\right )",
            r"\prod_p \left ( \sum_{a = 0}^{\infty} \frac{1}{p^{2a}} + 2\sum_{b = 1}^{\infty} \sum_{a = 0}^{b - 1} \frac{1}{p^{2b}} \right )",
            r"\prod_p \left ( \frac{1}{1 - p^{-2}} + \frac{2p^{-2}}{(1 - p^{-2})^2}\right )", # 15
            r"\prod_p \frac{1 + p^{-2}}{(1 - p^{-2})^2}",
            r"\prod_p \frac{1 - p^{-4}}{(1 - p^{-2})^3}",
            r"\left ( \prod_p \frac{1}{1 - p^{-4}} \right )^{-1} \left ( \prod_p \frac{1}{1 - p^{-2}}\right )^3",
            r"\zeta^{-1}(4) \, \zeta^3 (2)",
            r"\left ( \frac{\pi^4}{90} \right )^{-1} \left ( \frac{\pi^2}{6} \right )^3", # 20
            r"\frac{5\pi^2}{12}",
            r"\int_0^{\infty} \frac{1}{\big ( \{x\}\mathrm{lcm} \, (\lceil x\rceil, \lfloor 1/\{ x\}\rfloor) \big )^2} \dd{x} = \frac{5\pi^2}{12}"
        ]

        latex = [MathTex(i, font_size=fontsize, tex_template=temp) for i in raw_latex]

        # Notes and substitutions
        note1 = MathTex(r"\lfloor x \rfloor = n \text{ for } n \leq x < n + 1 \text{ where } n \in \mathbb Z",
                        font_size=fontsize, color=LIGHT_GREY, tex_template=temp).next_to(latex[0], 2*DOWN)
        note2 = MathTex(r"\{x\} = x - \lfloor x \rfloor",
                        font_size=fontsize, color=LIGHT_GREY, tex_template=temp).next_to(note1, DOWN)
        note3 = MathTex(r"\lceil x \rceil = \lfloor x \rfloor + 1",
                        font_size=fontsize, color=LIGHT_GREY, tex_template=temp).next_to(note2, DOWN)
        sub1 = MathTex(r"\frac{1}{x - i} = x",
                        font_size=fontsize, tex_template=temp).next_to(latex[4], DOWN)
        diff1 = MathTex(r"-\frac{\dd{x}}{(x - i)^2} = \dd{x}",
                        font_size=fontsize, tex_template=temp).next_to(sub1, DOWN)
        note4 = MathTex(r"i = p_1^{a_1}p_2^{a_2} \cdots p_n^{a_n}",
                        font_size=fontsize, color=LIGHT_GREY, tex_template=temp).next_to(latex[9], 2*DOWN)
        note5 = MathTex(r"j = p_1^{b_1}p_2^{b_2} \cdots p_n^{b_n}",
                        font_size=fontsize, color=LIGHT_GREY, tex_template=temp).next_to(note4, DOWN)
        note6 = MathTex(r"\text{where $p_k$ denotes the $k$th prime number, and $a_i, b_i \in \mathbb N$ for $i \in \mathbb N$}",
                        font_size=fontsize, color=LIGHT_GREY, tex_template=temp).next_to(note5, DOWN)
        note7 = MathTex(r"n \to \infty",
                        font_size=fontsize, tex_template=temp).next_to(latex[9], 2*UP)
        note8 = MathTex(r"\prod_{p \text{ prime}} \frac{1}{1 - p^{-s}} = \zeta (s)",
                        font_size=fontsize, color=LIGHT_GREY, tex_template=temp).next_to(latex[19], DOWN)

        # Mobject initialization
        note1.scale(1.25*scale)
        for i in [2, 3, 4, 9]: latex[i].scale(scale)
        latex[10].scale(scale/1.4)
        note6.scale(scale/1.275)
        for i in [12, 13, 22]: latex[i].scale(1.25*scale)

        # Coloring
        sub1[0][6].set_color(YELLOW)
        for i in [11, 12]: diff1[0][i].set_color(YELLOW)
        for i in [6, 7, 18, 24, 25]: latex[5][0][i].set_color(YELLOW)

        # Epilogue
        result_box = SurroundingRectangle(latex[22], color=YELLOW, buff=0.2)

        # Animation
        self.play(Write(latex[0]))
        self.wait(delay)
        self.play(FadeIn(note1), FadeIn(note2), FadeIn(note3))
        self.wait(delay)
        self.play(FadeOut(note1), FadeOut(note2), FadeOut(note3))
        self.play(
            TransformByGlyphMap(
                latex[0], latex[1],
                ([3, 4], [24]),
                (list(range(5, 27)), list(chain(range(3, 24), [25])))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[1], latex[2],
                ([], list(range(5))),
                ([1], [6, 7, 8]),
                ([2], [9]),
                ([11, 12, 13], [18, 19, 20])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[2], latex[3],
                ([11, 12, 13], list(range(11, 18))),
                ([25, 26, 27], list(range(29, 36)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[3], latex[4],
                ([14, 15, 16], [14]),
                ([32, 33, 34], [30])
            )
        )
        self.wait(delay)
        self.play(Write(sub1))
        self.play(Write(diff1))
        self.wait(delay)
        self.play(FadeOut(sub1), FadeOut(diff1))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[4], latex[5],
                ([6, 7, 8], [6]),
                ([9], [7]),
                (list(range(11, 16)), []),
                (list(range(25, 32)), [18])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[5], latex[6],
                ([], list(range(5, 10))),
                ([6], [11, 12, 13]),
                ([7], [14]),
                ([17, 18, 19], [22])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[6], latex[7],
                ([4], [4]),
                ([20, 21, 22], [20])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[7], latex[8],
                (list(chain(range(10,15), [27, 28])), []),
                ([25], [10, 11]),
                (list(chain(range(15, 25), [26])), list(chain(range(12, 23))))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[8], latex[9],
                ([0, 5], []),
                ([2, 3, 4], list(range(1, 10))),
                ([7, 8, 9], list(range(11, 20))),
                (list(range(13, 21)), list(range(23, 62)))
            ),
            Write(note7)
        )
        self.play(FadeIn(note4), FadeIn(note5), FadeIn(note6))
        self.wait(3*delay)
        self.play(
            TransformByGlyphMap(
                latex[9], latex[10],
                ([0, 10], [2, 29, 59]),
                (list(chain(range(1, 10), range(11, 20))), list(chain(range(3, 10), range(30, 37), range(60, 67)))),
                ([], [0, 1, 25, 25, 27, 28, 52, 53, 55, 56, 57, 58, 82, 83]),
                (list(range(23, 64)), list(chain(range(10, 25), range(37, 52), range(67, 82)))),
                ([20], [10, 37, 67])
            ),
            FadeOut(note4), FadeOut(note5), FadeOut(note6)
        )
        self.wait(3*delay)
        self.play(
            TransformByGlyphMap(
                latex[10], latex[11],
                ([0, 1, 25, 26, 27, 28, 52, 53, 54, 55, 56, 57, 58, 82, 83], [0, 1]),
                ([10, 37, 67], [8]),
                ([11, 38, 68], [9]),
                ([2, 29, 59], [2]),
                (list(chain(range(3, 10), range(30, 37), range(60, 67))), list(range(2, 8))),
                (list(chain(range(12, 25), range(39, 52), range(69, 82))), list(range(10, 20)))
            ),
            FadeOut(note7)
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[11], latex[12],
                ([2], [8, 9, 28, 29, 33, 34, 35, 36, 55, 56, 60, 61, 62, 63]),
                ([3, 4, 5, 6, 7], [10, 11, 12, 30, 31, 32, 37, 38, 39, 57, 58, 59, 64, 65, 66]),
                ([8], [13, 40, 67]),
                ([9], [14, 41, 68]),
                (list(range(10, 20)), [15, 16, 17, 42, 43, 44, 69, 70, 71]),
                ([], [2, 3, 4, 5, 6, 7, 81, 82, 83, 84, 85, 86]),
                ([], [27, 54]),
                ([], list(chain(range(18, 27), range(45, 54), range(72, 81))))
            )
        )
        self.wait(3*delay)
        self.play(
            TransformByGlyphMap(
                latex[12], latex[13],
                ([2, 3, 4, 5, 6, 7], [2]),
                ([81, 82, 83, 84, 85, 86], [49]),
                (list(chain(range(18, 27), range(45, 54), range(72, 81))), []),
                ([57], [34]),
                ([60], [37]),
                ([64], [41]),
                ([71], [48])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[13], latex[14],
                (list(range(31, 49)), [14])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[14], latex[15],
                (list(range(3, 13)), list(range(3, 10))),
                (list(range(14, 32)), list(range(11, 24)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[15], latex[16],
                (list(range(2, 25)), list(range(2, 16)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[16], latex[17],
                ([3], [3]),
                ([6], [6]),
                ([15], [15])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[17], latex[18],
                ([], [0, 3, 4, 10, 11, 12, 13, 16, 17, 21]),
                ([0, 1], [1, 2, 14, 15]),
                ([2, 3, 4, 5, 6], [5, 6, 7, 8, 9]),
                ([8, 14], []),
                ([9, 10, 11, 12, 13], [18, 19, 20, 21, 22]),
                ([15], [24])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[18], latex[19],
                (list(range(11)), [0, 3, 4, 5]),
                ([11, 12], [1, 2]),
                (list(range(12, 24)), [6, 8, 9, 10]),
                ([24], [7])
            ),
            FadeIn(note8)
        )
        self.wait(delay)
        self.play(FadeOut(note8))
        self.play(
            TransformByGlyphMap(
                latex[19], latex[20],
                ([0, 3, 4, 5], list(range(7))),
                ([1, 2], [7, 8]),
                ([6, 8, 9, 10], list(range(9, 15))),
                ([7], [15])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[20], latex[21],
                ([1, 10], [1]),
                ([0, 6, 9, 14], []),
                ([2, 7, 8, 11, 15], [2]),
                ([3, 12], [3]),
                ([4, 5, 13], [0, 4, 5])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[21], latex[22],
                ([], list(range(30)))
            )
        )
        self.play(
            Create(result_box),
            ApplyWave(latex[22], amplitude=0.1, wavelength=0.2)
        )
        self.wait(delay)
