from manim import *
from MF_Tools import TransformByGlyphMap
from itertools import chain

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 2560
config.pixel_width = 1440

class Thumbnail(Scene):
    def construct(self):
        integral = MathTex(r"\int_0^{\frac{\pi}{2}} \tan^s x \, dx",
            font_size=121)
        self.add(integral)

class Integral(Scene):
    def construct(self):

        # Initializing
        fontsize = 81
        delay = 0.5
        scale = 1/2

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{physics}")

        # LaTeX
        latex_strings = [
            r"\int_0^{\frac{\pi}{2}} \tan^s x \, dx",
            r"\textbf{B} \left ( u, v \right ) = 2\int_0^{\frac{\pi}{2}}(\sin x)^{2u - 1}(\cos x)^{2v - 1} \, dx",
            r"\textbf{B} \left ( {1 + s \over 2}, {1 - s \over 2} \right ) = 2\int_0^{\frac{\pi}{2}} (\sin x)^s (\cos x)^{-s} \, dx",
            r"\textbf{B} \left ( \frac{1+s}{2}, \frac{1-s}{2} \right ) = 2\int_0^{\frac{\pi}{2}} \tan^s x \, dx",
            r"\int_0^{\frac{\pi}{2}} \tan^s x \, dx = \frac{1}{2} \cdot \textbf{B} \left ( \frac{1+s}{2}, \frac{1-s}{2} \right )",
            r"\textbf{B} \left ( \frac{1+s}{2}, \frac{1-s}{2} \right )",
            r"\textbf{B} \left ( u, v \right ) = \frac{\Gamma (u) \Gamma (v)}{\Gamma (u + v)}",
            r"\Gamma (z) & = \int_0^{\infty} t^{z-1}e^{-t} \, dt \\ & = (z-1)!",
            r"\frac{\Gamma (u) \Gamma (v)}{\Gamma (u+v)}",
            r"\frac{\Gamma \left ( {1 + s \over 2} \right ) \Gamma \left ({1 - s \over 2} \right )}{\Gamma \left ({1 + s \over 2} + {1 - s \over 2} \right )}",
            r"\frac{\Gamma \left ( {1 + s \over 2} \right ) \Gamma \left ({1 - s \over 2} \right )}{\Gamma (1)}",
            r"\frac{\Gamma \left ( {1 + s \over 2} \right ) \Gamma \left ( {1 - s \over 2} \right )}{0!}",
            r"\Gamma \left ( \frac{1+s}{2} \right ) \Gamma \left ( \frac{1-s}{2} \right )",
            r"\Gamma \left ( \frac{1+s}{2} \right ) \Gamma \left ( 1 - \frac{1+s}{2} \right )",
            r"\Gamma (z) \Gamma (1-z) = \pi \csc (\pi z)",
            r"\pi \csc \left ( \pi \left ( {1 + s \over 2} \right ) \right )",
            r"\pi \csc \left ( \frac{\pi}{2} + \frac{\pi s}{2} \right )",
            r"\pi \sec \frac{\pi s}{2}",
            r"\int_0^{\frac{\pi}{2}} \tan^s x \, dx = \frac{1}{2} \cdot \textbf{B} \left ( \frac{1+s}{2}, \frac{1-s}{2} \right )",
            r"\int_0^{\frac{\pi}{2}} \tan^s x \, dx = \frac{1}{2} \cdot \pi \sec \frac{\pi s}{2}",
            r"\int_0^{\frac{\pi}{2}} \tan^s x \, dx = \frac{\pi}{2} \sec \frac{\pi s}{2}"
        ]
        latex = [MathTex(i, font_size=fontsize, tex_template=temp) for i in latex_strings]

        # Substitution and notes
        note1 = Tex(r"\text{(Beta function)}",
            color=LIGHT_GREY, font_size=fontsize/2).next_to(latex[1], DOWN)
        note2 = Tex(r"\text{(For natural $z$)}",
            color=LIGHT_GREY, font_size=fontsize/2).next_to(latex[7], DOWN*2)
        note3 = Tex(r"\text{(Reflection formula)}",
            color=LIGHT_GREY, font_size=fontsize/2).next_to(latex[14], DOWN*2)
        sub1 = MathTex(r"2u - 1 & = s \\ 2v - 1 & = -s",
            substrings_to_isolate=["s", "-s"], font_size=fontsize/2).next_to(latex[1], DOWN)
        sub2 = MathTex(r"z = {1 + s \over 2}",
            substrings_to_isolate=[r"{1 + s \over 2}"], font_size=fontsize*3/4).next_to(latex[14], DOWN*2)

        # MObject Initialization
        for i in chain(range(1, 6), range(18, 21)): latex[i].scale(scale)
        latex[13].scale(scale*1.5)
        latex[14].scale(scale*1.5)
        latex[6].shift(UP*3.5)

        # Coloring
        sub1.set_color_by_tex_to_color_map({"s": YELLOW, "-s": YELLOW})
        sub2.set_color_by_tex(r"{1 + s \over 2}", YELLOW)
        for i in chain(range(2, 7), range(8, 13), [27, 34, 35]): latex[2][0][i].set_color(YELLOW)
        for i in chain(range(2, 7), range(10, 15), range(19, 24), range(25, 30)): latex[9][0][i].set_color(YELLOW)
        for i in range(7, 12): latex[15][0][i].set_color(YELLOW)

        # Epilogue
        result = MathTex(r"\int_0^{\frac{\pi}{2}}\tan^s x \, dx = \frac{\pi}{2}\sec \frac{\pi s}{2}", font_size=70)
        result_box = SurroundingRectangle(result, color=YELLOW, buff=0.2)

        # Animation
        self.play(Write(latex[0]))
        self.wait(delay)
        self.play(Unwrite(latex[0]))
        self.wait(delay)
        self.play(
            Write(latex[1]),
            FadeIn(note1)
        )
        self.play(FadeOut(note1))
        self.play(latex[1].animate.shift(UP))
        self.play(Write(sub1))
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[1], latex[2],
            ([2], [i for i in range(2, 7)]),
            ([4], [i for i in range(8, 13)]),
            ([i for i in range(19, 23)], [27]),
            ([i for i in range(29, 33)], [34, 35])
            ),
            FadeOut(sub1)
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[2], latex[3],
            ([i for i in range(21, 36)], [i for i in range(21, 26)]),
            ([i for i in range(2, 7)], [i for i in range(2, 7)]),
            ([i for i in range(8, 13)], [i for i in range(8, 13)])
            )
        )
        self.wait(delay)
        self.play(ReplacementTransform(latex[3], latex[4]))
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[4], latex[5],
            ([i for i in range(0, 17)], [])
            )
        )
        self.wait(delay)
        self.play(Unwrite(latex[5]))
        self.play(Write(latex[6]))
        self.play(Write(latex[7]))
        self.play(FadeIn(note2))
        self.wait(delay)
        self.play(
            FadeOut(latex[7]),
            FadeOut(note2),
        )
        self.play(TransformByGlyphMap(
            latex[6], latex[8],
            ([i for i in range(7)], [])
            ),
            # latex[6].animate.shift(DOWN*2)
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[8], latex[9],
            ([2], [i for i in range(2, 7)]),
            ([6], [i for i in range(10, 15)]),
            ([11], [i for i in range(19, 24)]),
            ([13], [i for i in range(25, 30)]),
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[9], latex[10],
            ([i for i in range(2, 7)], [i for i in range(2, 7)]),
            ([i for i in range(10, 15)], [i for i in range(10, 15)]),
            ([i for i in range(19, 30)], [19])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[10], latex[11],
            ([i for i in range(17, 21)], [17, 18])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[11], latex[12],
            ([16, 17, 18], [])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[12], latex[13],
            ([11], [13]),
            ([], [10,11])
            )
        )
        self.wait(delay)
        self.play(latex[13].animate.shift(UP*2))
        self.play(
            Write(latex[14]),
            FadeIn(note3)
        )
        self.play(FadeOut(note3))
        self.wait(delay)
        self.play(Write(sub2))
        self.wait(delay)
        self.play(
            FadeOut(sub2),
            FadeOut(latex[14]),
            ReplacementTransform(latex[13], latex[15])
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[15], latex[16],
            ([i for i in range(5, 13)], [i for i in range(5, 13)])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[16], latex[17],
            ([i for i in range(4, 9)] + [13], [])
            )
        )
        self.wait(delay)
        self.play(Unwrite(latex[17]))
        self.play(Write(latex[18]))
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[18], latex[19],
            ([i for i in range(17, 31)], [i for i in range(17, 25)])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[19], latex[20],
            ([i for i in range(13, 18)], [13, 14, 15])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[20], result,
            ([i for i in range(23)], [i for i in range(23)])
            )
        )
        self.play(
            Create(result_box),
            ApplyWave(result, amplitude=0.1, wavelength=0.3)
        )
        self.wait(delay)
