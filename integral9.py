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

        integral = MathTex(r"\int_0^{\infty} e^{-x}\ln^2(x) \dd{x}",
            font_size=80, tex_template=temp)
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
            r"\int_0^{\infty} e^{-x}\ln^2(x) \dd{x}", # 0
            r"\Gamma (z) = \int_0^{\infty} e^{-x}x^{z-1} \dd{x}",
            r"\dv{z} \Gamma (z) = \dv{z} \int_0^{\infty} e^{-x}x^{z-1} \dd{x}",
            r"\dv{z} \Gamma (z) = \int_0^{\infty} \pdv{z} \left ( e^{-x}x^{z-1} \right ) \dd{x}",
            r"\dv[2]{z} \Gamma (z) = \int_0^{\infty} \pdv[2]{z} \left ( e^{-x}x^{z-1}\right ) \dd{x}",
            r"\dv[2]{z} \Gamma (z) = \int_0^{\infty} \ln^2 (x) e^{-x} x^{z-1} \dd{x}", # 5
            r"\Gamma '' (1) = \int_0^{\infty} e^{-x}\ln^2 (x) \dd{x}",
            r"\Gamma '' (1)",
            r"(\Gamma \cdot \psi)' (1)",
            r"\Gamma'(1)\psi (1) + \psi ' (1) \Gamma (1)",
            r"\Gamma (1) \psi^2 (1) + \psi ' (1)", # 10
            r"\psi^2 (1) + \psi ' (1)",
            r"\psi (z + 1) = -\gamma + \sum_{k=1}^{\infty} \frac 1k - \frac 1{k + z}",
            r"\psi (1) = -\gamma + \sum_{k=1}^{\infty} \frac 1k - \frac 1k",
            r"\psi (1) = -\gamma + \sum_{k=1}^{\infty} 0",
            r"\psi (1) = -\gamma", # 15
            r"\gamma^2 + \psi ' (1)",
            r"\psi (z + 1) = -\gamma + \sum_{k=1}^{\infty} \frac 1k - \frac 1{k + z}",
            r"\dv{z} \psi (z+1) = \dv{z} \left ( -\gamma + \sum_{k=1}^{\infty} \frac 1k - \frac 1{k + z} \right )",
            r"\psi ' (z + 1) = \sum_{k = 1}^{\infty} \frac{1}{(k + z)^2}",
            r"\psi ' (1) = \sum_{k=1}^{\infty} \frac{1}{k^2}", # 20
            r"\psi ' (1) = \frac{\pi^2}{6}",
            r"\gamma^2 + \frac{\pi^2}{6}",
            r"\int_0^{\infty} e^{-x}\ln^2(x) \dd{x} = \gamma^2 + \frac{\pi^2}{6}"
        ]

        latex = [MathTex(i, font_size=fontsize, tex_template=temp) for i in raw_latex]

        # Notes and substitutions
        note1 = MathTex(r"\text{(1) Digamma function: } \psi (z) = \dv{z} \ln \Gamma (z) \text{ for $z > 0$}",
                        color=LIGHT_GREY, font_size=0.5*fontsize, tex_template=temp).next_to(latex[8], 1.5*DOWN)
        note2 = MathTex(r"\text{(2) $\gamma$ denotes the Euler-Mascheroni constant}",
                        color=LIGHT_GREY, font_size=0.5*fontsize, tex_template=temp).next_to(latex[12], 1.5*DOWN)

        # Mobject initialization
        for i in range(2, 7): latex[i].scale(0.75)
        latex[12].scale(0.75)
        latex[16].shift(3*UP)
        latex[17].scale(0.75)
        latex[18].scale(0.60)
        latex[22].shift(3*UP)
        latex[23].scale(0.75)

        # Epilogue
        result_box = SurroundingRectangle(latex[23], color=YELLOW, buff=0.2)

        # Animation
        self.play(Write(latex[0]))
        self.wait(delay)
        self.play(FadeOut(latex[0]))
        self.play(Write(latex[1]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[1], latex[2],
                ([], [0, 1, 2, 3, 9, 10, 11, 12])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[2], latex[3],
                ([9, 10, 11, 12], [12, 13, 14, 15]),
                ([], [16, 24])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[3], latex[4],
                ([], [1, 5, 15, 19])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[4], latex[5],
                (list(chain(range(14, 21), [28])), list(range(14, 20)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[5], latex[6],
                (list(range(6)), [1, 2]),
                ([8], [4]),
                ([23, 24, 25, 26], []),
                ([20, 21, 22], [10, 11, 12]),
                (list(range(14, 20)), list(range(13, 19)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[6], latex[7],
                (list(range(6, 21)), [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[7], latex[8],
                ([0, 1], [0, 1, 2, 3, 4]),
                ([2], [5])
            ),
            FadeIn(note1)
        )
        self.wait(delay)
        self.play(FadeOut(note1))
        self.play(
            TransformByGlyphMap(
                latex[8], latex[9],
                (list(range(6)), [0, 1, 5, 10, 11, 15]),
                ([6, 7, 8], [2, 3, 4, 6, 7, 8, 12, 13, 14, 16, 17, 18]),
                ([], [9])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[9], latex[10],
                ([1], [5]),
                (list(range(15, 19)), [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[10], latex[11],
                ([0, 1, 2, 3], [])
            )
        )
        self.wait(delay)
        self.play(latex[11].animate.shift(3*UP))
        self.play(Write(latex[12]), FadeIn(note2))
        self.wait(delay)
        self.play(FadeOut(note2))
        self.play(
            TransformByGlyphMap(
                latex[12], latex[13],
                ([2, 3], []),
                ([22, 23], [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[13], latex[14],
                (list(range(13, 20)), [13])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[14], latex[15],
                (list(range(7, 14)), [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[11], latex[16],
                ([0, 2, 3, 4], [0])
            )
        )
        self.play(FadeOut(latex[15]))
        self.play(Write(latex[17]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[17], latex[18],
                ([], [0, 1, 2, 3, 11, 12, 13, 14, 15, 33])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[18], latex[19],
                ([15, 33], [15, 19]),
                ([], [20]),
                ([0, 1, 2, 3], [1]),
                ([11, 12, 13, 14, 16, 17, 18, 24, 25, 26, 27], []),
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
            latex[19], latex[20],
            ([3, 4, 15, 17, 18, 19], []),
                ([20], [14])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[20], latex[21],
                (list(range(6, 15)), [6, 7, 8, 9])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[16], latex[22],
                (list(range(3, 8)), list(range(3, 7)))
            )
        )
        self.play(FadeOut(latex[21]))
        self.play(latex[22].animate.shift(3*DOWN))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[22], latex[23],
                ([], list(range(15)))
            )
        )
        self.play(
            Create(result_box),
            ApplyWave(latex[23], amplitude=0.1, wavelength=0.2)
        )
        self.wait(3*delay)
