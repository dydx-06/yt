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

        integral = MathTex(r"\int_0^{\pi/2} \ln (x^2 + \ln^2 (\cos x)) \dd{x}",
            font_size=60, tex_template=temp)
        self.add(integral)

class Integral(Scene):
    def construct(self):

        # Initializing
        fontsize = 60
        delay = 0.6

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{physics}")

        # LaTeX
        raw_latex = [
            r"\int_0^{\pi/2} \ln (x^2 + \ln^2 (\cos x)) \dd{x}", # 0
            r"\int_0^{\pi/2} \ln \abs{xi + \ln(\cos x)}^2 \dd{x}",
            r"\int_0^{\pi/2} \ln \abs{\ln e^{ix} + \ln (\cos x)}^2 \dd{x}",
            r"\int_0^{\pi/2} \ln \abs{\ln (e^{ix}\cos x)}^2 \dd{x}",
            r"\int_0^{\pi/2} \ln \abs{\ln \left ( e^{ix} \cdot \frac{e^{-ix} + e^{ix}}{2} \right )}^2 \dd{x}",
            r"2\int_0^{\pi/2} \ln \abs{\ln \left ( \frac{1 + e^{2ix}}{2} \right )} \dd{x}", # 5
            r"z = \abs{z}e^{i\arg z}",
            r"\ln (z) = \ln \left ( \abs{z}e^{i\arg z} \right )",
            r"\ln (z) = \ln \abs{z} + \ln e^{i\arg z}",
            r"\ln (z) = \ln \abs{z} + i\arg z",
            r"\Re \ln (z) = \ln \abs{z}", # 10
            r"2\int_0^{\pi/2} \Re \ln \ln \left ( \frac{1 + e^{2ix}}{2} \right ) \dd{x}",
            r"2\Re \int_0^{\pi/2} \ln \ln \left ( \frac{1 + e^{2ix}}{2} \right ) \dd{x}",
            r"2\Re \int_0^{\pi/2} \ln \left ( \ln (1 + e^{2ix}) - \ln 2\right ) \dd{x}",
            r"f(z) = \ln \left ( \ln (1 + z) - \ln 2 \right )",
            r"f(z) = f(0) + f'(0)z + \frac{f''(0)}{2!}z^2 + \cdots", # 15
            r"f(e^{2ix}) = f(0) + f'(0)e^{2ix} + \frac{f''(0)}{2!}e^{4ix} + \cdots",
            r"\Re \int_0^{\pi/2} f(e^{2ix}) \dd{x}= \Re \left ( \int_0^{\pi/2} f(0) \dd{x} + \int_0^{\pi/2} f'(0)e^{2ix}\dd{z} + \cdots \right )",
            r"\Re \frac{\pi}{2} \ln (-\ln 2) + 0",
            r"\frac{\pi}{2} \ln \ln 2",
            r"\frac 12 \int_0^{\pi/2} \ln (x^2 + \ln^2 (\cos x)) \dd{x} = \frac{\pi}{2} \ln \ln 2", # 20
            r"\int_0^{\pi/2} \ln (x^2 + \ln^2 (\cos x)) \dd{x} = \pi \ln \ln 2"
            ]

        latex = [MathTex(i, font_size=fontsize, tex_template=temp) for i in raw_latex]

        # Substitutions and notes
        note1_1 = MathTex(r"i^2 = -1",
            font_size=fontsize/1.5, tex_template=temp, color=LIGHT_GREY).next_to(latex[1], DOWN)
        note1_2 = MathTex(r"\abs{x + iy} = \sqrt{x^2 + y^2}",
            font_size=fontsize/1.5, tex_template=temp, color=LIGHT_GREY).next_to(note1_1, DOWN)
        note2 = MathTex(r"z \in \mathbb C",
            font_size=fontsize/1.5, tex_template=temp, color=LIGHT_GREY).next_to(latex[6], DOWN)
        note3_1 = MathTex(r"f : \{ e^{it} : t \in (0, \pi) \} \to \mathbb C",
            font_size=fontsize/1.5, tex_template=temp, color=LIGHT_GREY).next_to(latex[14], UP)
        note3_2 = Tex(r"Note that $f$ is analytic",
            font_size=fontsize/1.5, tex_template=temp, color=LIGHT_GREY,).next_to(latex[14], DOWN)
        note4 = Tex(r"Real parts of the integrals of all terms of order $x$ and greater vanish.",
            font_size=fontsize/2.25, tex_template=temp, color=LIGHT_GREY).next_to(latex[18], DOWN)

        # Mobject initialization
        latex[4].scale(0.90)
        latex[13].scale(0.85)
        latex[15].scale(0.75)
        latex[16].scale(0.70)
        latex[17].scale(0.45)
        latex[20].scale(0.75)
        latex[21].scale(0.80)

        # Epilogue
        result_box = SurroundingRectangle(latex[21], color=YELLOW, buff=0.2)

        # Animation
        self.play(Write(latex[0]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[0], latex[1],
                ([7], [7]),
                ([9, 13], [20]),
                ([], [9]),
                ([20], [19])
            ),
            FadeIn(note1_1),
            FadeIn(note1_2)
        )
        self.wait(delay)
        self.play(
            FadeOut(note1_1),
            FadeOut(note1_2)
        )
        self.play(
            TransformByGlyphMap(
                latex[1], latex[2],
                ([7], [7, 8]),
                ([8, 9], [12, 13]),
                ([], [9, 10, 11]),
                ([19], [23, 24])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[2], latex[3],
                ([9, 10, 15, 16], [9, 10]),
                ([11, 12, 13], [12, 13, 14]),
                ([14], []),
                ([17, 22], [11, 19])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[3], latex[4],
                ([7, 8], [7, 8, 9, 10]),
                ([11], [13]),
                ([], [17]),
                ([15, 16, 17, 18], list(range(18, 28))),
                ([19], [28]),
                ([20, 21], [29, 30, 31, 32])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[4], latex[5],
                (list(range(14, 22)), [15]),
                ([], [18]),
                ([33], [0])
            )
        )
        self.wait(delay)
        self.play(latex[5].animate.shift(UP*4))
        self.wait(delay)
        self.play(
            Write(latex[6]),
            FadeIn(note2)
        )
        self.wait(delay)
        self.play(FadeOut(note2))
        self.play(
            TransformByGlyphMap(
                latex[6], latex[7],
                ([], [0, 1, 2, 4, 6, 7, 8, 18])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[7], latex[8],
                ([8, 18], []),
                ([6, 7], [6, 7, 12, 13]),
                ([], [11])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[8], latex[9],
                ([12, 13, 14], []),
                (list(range(15, 20)), list(range(12, 17)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[9], latex[10],
                ([], [0, 1]),
                (list(range(11, 17)), [])
            )
        )
        self.wait(delay)
        self.play(
            latex[10].animate.shift(DOWN*4),
            latex[5].animate.shift(DOWN*4)
        )
        self.play(
            TransformByGlyphMap(
                latex[5], latex[11],
                (list(chain(range(8, 12), range(24, 28))), []),
                ([], [6, 7])
            )
        )
        self.play(FadeOut(latex[10]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[11], latex[12],
                ([6, 7], [1, 2])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[12], latex[13],
                ([12], [13]),
                ([19], [21]),
                ([20], [24]),
                ([10, 11], [11, 12, 22, 23]),
                ([], [10, 25])
            )
        )
        self.wait(delay)
        self.play(latex[13].animate.shift(UP*4))
        self.play(Write(latex[14]))
        self.play(
            FadeIn(note3_1),
            FadeIn(note3_2)
        )
        self.wait(delay)
        self.play(
            latex[14].animate.shift(DOWN*4),
            FadeOut(note3_1),
            FadeOut(note3_2)
        )
        self.wait(delay)
        self.play(Write(latex[15]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[15], latex[16],
                ([2], [2, 3, 4, 5]),
                ([15], [18, 19, 20, 21]),
                ([26, 27], [32, 33, 34, 35])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[16], latex[17],
                (list(range(22, 36)), []),
                ([], list(chain(range(7), [14, 15], range(17, 25), [29, 30], range(32, 37), [46, 47, 52])))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[17], latex[18],
                (list(range(32, 52)), [14]),
                ([19, 52], []),
                (list(range(17)), []),
                (list(range(20, 31)), list(range(2, 13))),
                ([31], [13])
            ),
            FadeIn(note4)
        )
        self.wait(delay)
        self.play(
            FadeOut(note4),
            FadeOut(latex[14]),
            FadeOut(latex[13])
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[18], latex[19],
                ([0, 1, 7, 8, 12, 13, 14], [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[19], latex[20],
                (list(range(8)), list(range(27, 35))),
                ([], list(range(27)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[20], latex[21],
                ([0, 1, 2, 28, 29], [])
            )
        )
        self.play(
            Create(result_box),
            ApplyWave(latex[21], amplitude=0.1, wavelength=0.2)
        )
        self.wait(delay*3)
