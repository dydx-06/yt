from manim import *
from MF_Tools import TransformByGlyphMap
from itertools import chain

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 2560
config.pixel_width = 1440

class Thumbnail(Scene):
    def construct(self):
        integral = MathTex(r"\int_{-\infty}^{\infty} \frac{\sin x}{x} \, dx",
            font_size=60)
        self.add(integral)

class Integral(Scene):
    def construct(self):

        # Initializing
        fontsize = 60
        delay = 0.4
        scale = 3 / 5

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{physics}")

        # LaTeX mobjects
        raw_latex = [
            r"\int_{-\infty}^{\infty} \frac{\sin x}{x} \, dx",
            r"I = \int_{-\infty}^{\infty} \frac{\sin x}{x} \, dx",
            r"f(z) = \frac{e^{iz}}{z}",
            r"R \to \infty",
            r"\varepsilon \to 0",
            r"\oint_C f = \int_{\varepsilon}^R f + \int_{\Gamma} f + \int_{-R}^{-\varepsilon} f + \int_{\gamma} f", # 5
            r"\oint_{C} f",
            r"2\pi i \sum_{k = 1}^n \mathrm{Res} (f, z_k)",
            r"2\pi i \sum_{k = 1}^n 0",
            r"0",
            r"\oint_C f = \int_{\varepsilon}^R f + \int_{\Gamma} f + \int_{-R}^{-\varepsilon} f + \int_{\gamma} f", # 10
            r"0 = \int_{\varepsilon}^R f + \int_{\Gamma} f + \int_{-R}^{-\varepsilon} f + \int_{\gamma} f",
            r"\int_{\varepsilon}^R f + \int_{-R}^{-\varepsilon} f + \int_{\Gamma} f + \int_{\gamma} f = 0",
            r"\int_{\Gamma}f",
            r"\int_{\Gamma} \frac{e^{iz}}{z} \, dz",
            r"\Gamma : \phi \mapsto Re^{i\phi}", # 15
            r"\int_0^{\pi} \frac{\exp (iRe^{i\phi})}{Re^{i\phi}} \cdot iRe^{i\phi} \, d\phi",
            r"\int_0^{\pi} i\exp (iRe^{i\phi}) \, d\phi",
            r"\int_0^{\pi} i\exp(iR(\cos \phi + i\sin \phi)) \, d\phi",
            r"\int_0^{\pi} i\exp(iR\cos \phi - R\sin \phi) \, d\phi",
            r"\int_0^{\pi} i e^{iR\cos\phi}e^{-R\sin \phi} \, d\phi", # 20
            r"\int_{\Gamma} f =  \int_0^{\pi} i e^{iR\cos\phi}e^{-R\sin \phi} \, d\phi",
            r"\abs{\int_{\Gamma} f} \leq \int_0^{\pi} \abs{ie^{iR\cos\phi}e^{-R\sin \phi}} \, d\phi",
            r"\abs{\int_{\Gamma} f} \leq \int_0^{\pi} \abs{i}\abs{e^{iR\cos\phi}}\abs{e^{-R\sin \phi}} \, d\phi",
            r"\abs{\int_{\Gamma} f} \leq \int_0^{\pi} 1 \cdot 1 \cdot e^{-R\sin\phi} \, d\phi",
            r"\abs{\int_{\Gamma} f} \leq \int_0^{\pi} e^{-R\sin\phi} \, d\phi", # 25
            r"\abs{\int_{\Gamma} f} \leq \int_0^{\pi} 0 \, d\phi",
            r"\abs{\int_{\Gamma} f} \leq 0",
            r"\int_{\Gamma} f = 0",
            r"0",
            r"\int_{\varepsilon}^R f + \int_{-R}^{-\varepsilon} f + \int_{\Gamma} f + \int_{\gamma} f = 0", # 30
            r"\int_{\varepsilon}^R f + \int_{-R}^{-\varepsilon} f + 0 + \int_{\gamma} f = 0",
            r"\int_{\varepsilon}^R f + \int_{-R}^{-\varepsilon} f + \int_{\gamma} f = 0",
            r"\int_{\gamma} f",
            r"\int_{\gamma} \frac{e^{iz}}{z} \, dz",
            r"\gamma : \phi \mapsto \varepsilon e^{i\phi}", # 35
            r"\int_{\pi}^0 \frac{\exp(i\varepsilon e^{i\phi})}{\varepsilon e^{i\phi}} \cdot i\varepsilon e^{i\phi} \, d\phi",
            r"-\int_0^{\pi} i\exp(i\varepsilon e^{i\phi}) \, d\phi",
            r"-\int_0^{\pi} i\exp(0) \, d\phi",
            r"-\int_0^{\pi}i \, d\phi",
            r"-i \pi", # 40
            r"\int_{\varepsilon}^R f + \int_{-R}^{-\varepsilon} f + \int_{\gamma} f = 0",
            r"\int_{\varepsilon}^R f + \int_{-R}^{-\varepsilon} f - i\pi = 0",
            r"\int_{\varepsilon}^R f + \int_{-R}^{-\varepsilon} f = i\pi",
            r"\int_{0}^{\infty} f + \int_{-\infty}^{0} f = i\pi",
            r"\int_{-\infty}^{\infty} f = i\pi", # 45
            r"\int_{-\infty}^{\infty} \frac{e^{iz}}{z} \, dz = i\pi",
            r"\mathrm{Im} \int_{-\infty}^{\infty} \frac{e^{iz}}{z} \, dz = \mathrm{Im} (i\pi)",
            r"\int_{-\infty}^{\infty} \frac{\mathrm{Im} (e^{iz})}{z} \, dz = \mathrm{Im} (i\pi)",
            r"\int_{-\infty}^{\infty} \frac{\sin z}{z} \, dz = \pi",
            r"\int_{-\infty}^{\infty} \frac{\sin x}{x} \, dx = \pi", # 50
        ]

        latex = [MathTex(i, font_size=fontsize, tex_template=temp) for i in raw_latex]
        result_box = SurroundingRectangle(latex[50], color=YELLOW, buff=0.2)

        # Notes
        note1 = MathTex(r"\abs{\int_C w} \leq \int_C \abs{w}",
                    tex_template=temp, font_size=fontsize/1.5, color=LIGHT_GREY).next_to(latex[22], DOWN)
        note2 = MathTex(r"R \to \infty",
                    font_size=fontsize/1.5, color=LIGHT_GREY).next_to(latex[26], DOWN)
        note3 = MathTex(r"\varepsilon \to 0",
                    font_size=fontsize/1.5, color=LIGHT_GREY).next_to(latex[38], DOWN)
        note4 = MathTex(r"R & \to \infty \\ \varepsilon & \to 0",
                    font_size=fontsize/1.5, color=LIGHT_GREY).next_to(latex[44], DOWN)

        # Contour
        ax = Axes(
            x_range=(-3, 3),
            y_range=(-0.5, 3),
            x_length=6,
            y_length=3,
            y_axis_config={'include_ticks': False, 'include_tip': False},
            x_axis_config={'include_ticks': True, 'include_tip': False}
        )
        ax.shift(UP*5)
        origin = ax.get_origin()

        re = MathTex(r"\text{Re}", font_size=40).next_to(ax.x_axis.get_end(), RIGHT)
        im = MathTex(r"\text{Im}", font_size=40).next_to(ax.y_axis.get_end(), UP)

        contour = [
            Line(start=origin + RIGHT * 1, end=origin + RIGHT * 2, color=BLUE_C),
            Arc(radius=2, angle=PI, color=BLUE_C),
            Line(start=origin + LEFT * 2, end=origin + LEFT * 1, color=BLUE_C),
            Arc(radius=1, start_angle=PI, angle=-PI, color=BLUE_C)
        ]
        for i in [1, 3]: contour[i].move_arc_center_to(origin)

        graph_glyphs = [
            MathTex(r"-R", font_size=35).next_to(origin + 2 * LEFT, DOWN),
            MathTex(r"-\varepsilon", font_size=35).next_to(origin + LEFT, DOWN),
            MathTex(r"\varepsilon", font_size=35).next_to(origin + RIGHT, DOWN),
            MathTex(r"R", font_size=35).next_to(origin + 2 * RIGHT, DOWN),
            MathTex(r"\Gamma", font_size=35).next_to(origin + 1.5 * RIGHT + 1.5 * UP),
            MathTex(r"\gamma", font_size=35).next_to(origin + 0.75 * RIGHT + 0.75 * UP)
        ]
        graph_glyphs_animation = [Write(i) for i in graph_glyphs]

        # Mobject initialization
        latex[3].next_to(ax, DOWN)
        latex[4].next_to(latex[3], DOWN)
        for i in chain(range(3, 6), range(10, 13)): latex[i].scale(scale)
        latex[15].next_to(latex[14], DOWN*2)
        for i in chain(range(21, 25), range(30, 33)): latex[i].scale(scale*4/3)
        latex[35].next_to(latex[34], DOWN*2)

        # Coloring
        for i in chain(range(8, 12), range(14, 26)):
            latex[16][0][i].set_color(YELLOW)
            latex[36][0][i].set_color(YELLOW)


        # Animation
        self.play(Write(latex[0]))
        self.play(
            TransformByGlyphMap(
                latex[0], latex[1],
                ([], [0, 1])
            )
        )
        self.wait(delay)
        self.play(Unwrite(latex[1]))
        self.play(Write(latex[2]))
        self.wait(delay)
        self.play(
            Create(ax),
            latex[2].animate.shift(DOWN*5)
        )
        self.play(FadeIn(re, im))
        self.wait(delay)
        for i in contour: self.play(Create(i))
        self.play(*graph_glyphs_animation)
        self.play(
            Write(latex[3]),
            Write(latex[4])
        )
        self.wait(delay)
        self.play(Write(latex[5]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[5], latex[6],
                (list(range(3, 23)), [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[6], latex[7],
                ([2], [12]),
                ([0, 1], list(chain(range(12), range(13, 17))))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[7], latex[8],
                (list(range(8, 17)), [8])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[8], latex[9],
                (list(range(8)), [])
            )
        )
        self.wait(delay)
        self.play(FadeOut(latex[9]))
        self.wait(delay)
        self.play(Write(latex[10]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[10], latex[11],
                ([0, 1, 2], [0])
            ),
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[11], latex[12],
                ([0, 1], [19, 20])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[12], latex[13],
                (list(range(12)) + list(range(15, 21)), [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[13], latex[14],
                ([2], list(range(2, 9)))
            )
        )
        self.play(Write(latex[15]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[14], latex[16],
                ([1], [1, 2]),
                ([2], [3, 4, 5]),
                ([3], [7]),
                ([4], [6, 8, 9, 10, 11, 12]),
                ([6], [14, 15, 16, 17]),
                ([7, 8], list(range(18, 26)))
            ),
            FadeOut(latex[15])
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[16], latex[17],
                (list(chain(range(13, 19), range(20, 24))), []),
                ([19], [3])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[17], latex[18],
                ([10, 11, 12], list(range(10, 22)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[18], latex[19],
                ([9], [9, 15]),
                ([8, 16, 15], [8, 14]),
                ([10, 21], [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[19], latex[20],
                ([4, 5, 6], [4, 11]),
                (list(range(8, 14)), list(range(5, 11))),
                (list(range(14, 20)), list(range(12, 18))),
                ([7, 20], [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[20], latex[21],
                ([], list(range(4))),
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[21], latex[22],
                ([], list(chain(range(4), range(7, 11)))),
                ([3], [11]),
                ([], [15, 16, 32, 33])
            ),
            FadeIn(note1)
        )
        self.play(FadeOut(note1))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[22], latex[23],
                ([15, 16], [15, 18, 19, 29, 30]),
                ([32, 33], [17, 27, 28, 38, 39])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[23], latex[24],
                (list(range(15, 18)), [15]),
                (list(range(18, 29)), [17]),
                ([29, 30, 38, 39], []),
                ([], [16, 18])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[24], latex[25],
                (list(range(15, 19)), [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[25], latex[26],
                (list(range(15, 22)), [15])
            ),
            FadeIn(note2)
        ),
        self.play(FadeOut(note2))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[26], latex[27],
                ([12, 13, 14, 16, 17], [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[27], latex[28],
                (list(chain(range(4), range(7, 11))), []),
                ([11], [3])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[28], latex[29],
                (list(range(4)), [])
            )
        )
        self.wait(delay)
        self.play(FadeOut(latex[29]))
        self.play(Write(latex[30]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[30], latex[31],
                ([12, 13, 14], [12])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[31], latex[32],
                ([11, 12], [])
            )
        )
        self.play(
            TransformByGlyphMap(
                latex[32], latex[33],
                (list(chain(range(12), [15, 16])), [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[33], latex[34],
                ([2], list(range(2, 9)))
            )
        )
        self.play(Write(latex[35]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[34], latex[36],
                ([1], [1, 2]),
                ([2], [3, 4, 5]),
                ([4], list(range(8, 12))),
                ([], [6, 12]),
                ([6], list(range(14, 18))),
                ([7, 8], list(range(18, 26)))
            ),
            FadeOut(latex[35])
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[36], latex[37],
                ([], [0]),
                ([1, 2], [2, 3]),
                (list(chain(range(13, 19), range(20, 24))), []),
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[37], latex[38],
                (list(range(9, 14)), [9])
            ),
            FadeIn(note3)
        )
        self.play(FadeOut(note3))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[38], latex[39],
                (list(range(5, 11)), [])
            )
        )
        self.play(
            TransformByGlyphMap(
                latex[39], latex[40],
                ([1, 2, 3, 5, 6], [2])
            )
        )
        self.wait(delay)
        self.play(FadeOut(latex[40]))
        self.play(Write(latex[41]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[41], latex[42],
                (list(range(11, 15)), [11, 12, 13])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[42], latex[43],
                ([11, 12, 13, 15], [12, 13])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[43], latex[44],
                ([1], [1]),
                ([2], [2]),
                ([6, 7], [6]),
                ([8, 9], [7, 8])
            ),
            FadeIn(note4)
        )
        self.play(FadeOut(note4))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[44], latex[45],
                ([0, 5], [0]),
                ([1], [1]),
                ([2, 6], []),
                ([3, 9], [4]),
                ([4], []),
                ([7, 8], [2, 3])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[45], latex[46],
                ([4], list(range(4, 11)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[46], latex[47],
                ([], [0, 1, 14, 15, 16, 19])
            ),
            FadeOut(latex[2], ax, *graph_glyphs, *contour, im, re, latex[3], latex[4])
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[47], latex[48],
                ([0, 1], [4, 5]),
                ([], [6, 10])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[48], latex[49],
                (list(range(4, 11)), list(range(4, 8))),
                (list(chain(range(16, 20), [21])), [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[49], latex[50],
                ([7], [7]),
                ([9], [9]),
                ([11], [11])
            )
        )
        self.wait(delay)
        self.play(
            Create(result_box),
            ApplyWave(latex[50], amplitude=0.1, wavelength=0.2)
        )
