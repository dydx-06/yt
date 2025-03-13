from manim import *
from MF_Tools import TransformByGlyphMap
from itertools import chain

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class Thumbnail(Scene):
    def construct(self):
        integral = MathTex(r"\int_0^{\infty} \frac{\cos x}{\cosh x} \, dx",
            font_size=121)
        self.add(integral)

class Integral(Scene):
    def construct(self):
        fontsize = 42
        delay = 0.175

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{physics}")

        # Integrals
        integrals_latex = [
            r"\int_0^{\infty}\frac{\cos x}{\cosh x}\, dx",
            r"\int_0^{\infty}\frac{2\cos x}{e^x + e^{-x}}\, dx",
            r"\int_{-\infty}^{\infty} \frac{\cos x}{e^x + e^{-x}}\, dx",
            r"\int_{-\infty}^{\infty} \frac{\text{Re  } e^{ix}}{e^x + e^{-x}}\, dx",
            r"\text{Re} \int_{-\infty}^{\infty} \frac{e^{ix}}{e^x + e^{-x}} \, dx",
            r"\text{Re} \int_{-\infty}^{\infty} \frac{e^{ix}\cdot e^{x}}{e^{2x} + 1} \, dx",
            r"\text{Re} \int_{-\infty}^{\infty} \frac{(e^x)^i}{(e^x)^2 + 1} \cdot e^{x}\, dx",
            r"\text{Re} \int_0^{\frac{\pi}{2}} {(\tan x)^i \over (\tan x)^2 + 1} \cdot \sec^2 x \, dx",
            r"\text{Re} \int_0^{\frac{\pi}{2}} \frac{\tan^i x}{\tan^2x + 1} \cdot \sec^2 x \, dx",
            r"\text{Re} \int_0^{\frac{\pi}{2}} \frac{\tan^i x}{\sec^2 x} \cdot \sec^2 x \, dx",
            r"\text{Re} \int_0^{\frac{\pi}{2}} \tan^i x \, dx",
            # <Beta function>
            r"\int_0^{\infty} \frac{\cos x}{\cosh x} \, dx = \text{Re} \int_0^{\frac{\pi}{2}} \tan^i x \dd{x}",
            r"\int_0^{\infty} \frac{\cos x}{\cosh x} \, dx= \text{Re } \frac{1}{2} \cdot \textbf{B}\left ( \frac{1 + i}{2}, \frac{1 - i}{2}\right )",
            r"\int_0^{\infty} \frac{\cos x}{\cosh x} \, dx= \text{Re } \frac{1}{2} \cdot \pi \sech \frac{\pi}{2}",
            r"\int_0^{\infty} \frac{\cos x}{\cosh x} \, dx= \frac{\pi}{2} \sech \frac{\pi}{2}"
        ]

        integrals = [MathTex(i, font_size=fontsize, tex_template=temp) for i in integrals_latex]

        # Beta function
        betas_latex = [
            r"\textbf{B} \left (u, v \right ) & = 2\int_0^{\frac{\pi}{2}}(\sin x)^{2u-1}(\cos x)^{2v-1} \, dx",
            r"\textbf{B} \left ( {1 + i \over 2}, {1 - i \over 2}\right ) = 2 \int_0^{\frac{\pi}{2}}(\sin x)^i (\cos x)^{-i} \, dx",
            r"\textbf{B} \left ( {1 + i \over 2}, {1 - i \over 2}\right ) = 2 \int_0^{\frac{\pi}{2}}\tan^i x \, dx",
            r"\int_0^{\frac{\pi}{2}} \tan^i x \, dx = \frac 12 \textbf{B} \left ( \frac{1 + i}{2}, \frac{1 - i}{2}\right )",
            r"\textbf{B} \left ( u, v \right ) = \frac{\Gamma (u) \Gamma (v)}{\Gamma (u + v)}",
            r"\textbf{B} \left ({1 + i \over 2}, {1 - i \over 2} \right ) = {\Gamma \left ( {1 + i \over 2 }\right ) \Gamma \left ( {1 - i \over 2} \right ) \over \Gamma \left ( {1 + i \over 2} + {1 - i \over 2}\right )}",
            r"{\Gamma \left ( {1 + i \over 2 }\right ) \Gamma \left ( {1 - i \over 2} \right ) \over \Gamma \left ( {1 + i \over 2} + {1 - i \over 2}\right )}",
            r"{\Gamma \left ( {1 + i \over 2 }\right ) \Gamma \left ( {1 - i \over 2} \right ) \over \Gamma (1)}",
            r"\Gamma \left ( {1 + i \over 2 }\right ) \Gamma \left ( {1 - i \over 2} \right )",
            r"\Gamma \left ( {1 + i} \over 2 \right ) \Gamma \left ( 1 - {1 + i \over 2 } \right )",
            r"\Gamma (z) \Gamma (1 - z) = \pi \csc (\pi z)",
            r"\pi \csc \left (\pi\left ( {1 + i \over 2}\right ) \right )",
            r"\pi \csc \left ( {\pi \over 2} + {\pi i \over 2}\right )",
            r"\pi \sec \left ( \frac{\pi i}{2} \right )",
            r"\pi \sech \frac{\pi}{2}"
        ]

        betas = [MathTex(i, font_size=fontsize, tex_template=temp) for i in betas_latex]

        # Substitution and notes
        sub1 = MathTex(r"e^x = \tan x", substrings_to_isolate=[r"\tan x"], font_size=fontsize).next_to(integrals[6], DOWN)
        sub1_diff = MathTex(r"e^x \, dx = \sec^2 x \, dx", substrings_to_isolate=[r"\sec^2 x \, dx"], font_size=fontsize).next_to(sub1, DOWN)
        sub2 = MathTex(r"2u - 1 & = i \\ 2v - 1 & = -i", substrings_to_isolate=["i", "-i"], font_size=fontsize).next_to(betas[0], DOWN)
        sub3 = MathTex(r"z = {1 + i \over 2}", substrings_to_isolate=[r"1 + i \over 2"], font_size=fontsize).next_to(betas[10], DOWN*1.5)
        note1 = Tex(r"\text{(Even integrand)}", color=DARK_GREY, font_size=fontsize/2).next_to(integrals[2], DOWN)
        note2 = Tex(r"\text{(Beta function)}", color=DARK_GREY, font_size=fontsize/2).next_to(betas[0], DOWN)
        note3 = Tex(r"\text{(Reflection formula)}", color=DARK_GREY, font_size=fontsize/2).next_to(betas[10], DOWN)

        # Coloring
        sub1.set_color_by_tex(r"\tan x", YELLOW)
        sub1_diff.set_color_by_tex(r"sec^2 x \, dx", YELLOW)
        sub2.set_color_by_tex_to_color_map({"i": YELLOW, "-i": YELLOW})
        sub3.set_color_by_tex(r"1 + i \over 2", YELLOW)
        for i in chain(range(8, 12), range(16, 20), range(25, 32)):
            integrals[7][0][i].set_color(YELLOW)
        for i in chain(range(2, 7), range(8, 13), [27], [34], [35]):
            betas[1][0][i].set_color(YELLOW)
        for i in chain(range(2, 7), range(8, 13), range(17, 22), range(25, 30), range(34, 39), range(40, 45)):
            betas[5][0][i].set_color(YELLOW)
        for i in range(7, 12):
            betas[11][0][i].set_color(YELLOW)

        # Epilogue
        result_box = SurroundingRectangle(integrals[14], color=YELLOW, buff=0.2)
        epilogue1 = Tex("Next time:")
        epilogue1.shift(UP*1.5)
        epilogue2 = MathTex(r"\int_0^{\infty} \frac{(1+x)\ln^4(x)\tan^{-1}(x)}{\sqrt{x}(1+x^2)} \, dx")

        # Animation
        self.play(Write(integrals[0]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(integrals[0], integrals[1],
                ([], [3]),
                ([3, 4, 5, 6, 7], [4, 5, 6, 7, 8]),
                ([8, 9, 10, 11, 12], [9, 10, 11, 12, 13, 14])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(integrals[1], integrals[2],
                ([2], []),
                ([], [2, 3]),
                ([3], [])              
            ),
            FadeIn(note1)
        )
        self.play(FadeOut(note1))
        self.wait(delay/5)
        self.play(TransformByGlyphMap(integrals[2], integrals[3],
                ([4, 5, 6, 7], [4, 5, 6, 7, 8])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(integrals[3], integrals[4],
                ([4, 5], [0, 1])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(integrals[4], integrals[5],
                ([], [9, 10, 11]),
                ([10, 11, 12, 13, 14, 15], [13, 14, 15, 16, 17])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(integrals[5], integrals[6],
                ([6, 7, 8], [6, 7, 8, 9, 10]),
                ([9, 10, 11], [19, 20, 21]),
                ([13, 14, 15], [12, 13, 14, 15, 16])
            )
        )
        self.play(integrals[6].animate.shift(UP*1.5))
        self.play(Write(sub1))
        self.play(Write(sub1_diff))
        self.wait(delay)
        self.play(TransformByGlyphMap(integrals[6], integrals[7],
                ([3], [3, 4, 5]),
                ([4, 5], [6]),
                ([7, 8], [8, 9, 10, 11]),
                ([13, 14], [16, 17, 18, 19]),
                ([20, 21, 22, 23], [25, 26, 27, 28, 29, 30, 31])
            ),
            FadeOut(sub1),
            FadeOut(sub1_diff)
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(integrals[7], integrals[8],
                ([7, 12], []),
                ([13], [10]),
                ([15, 20], []),
                ([21], [16])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(integrals[8], integrals[9],
                ([13, 14, 15, 16, 17, 18, 19], [13, 14, 15, 16, 17])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(integrals[9], integrals[10],
                ([i for i in range(12, 24)], [])
            )
        ) 
        self.wait(delay)
        self.play(Unwrite(integrals[10]))
        self.play(Write(betas[0]),
                FadeIn(note2)
        )
        self.play(FadeOut(note2))
        self.wait(delay)
        self.play(
            betas[0].animate.shift(UP),
            Write(sub2)
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(betas[0], betas[1],
                ([2], [2, 3, 4, 5, 6]),
                ([4], [8, 9, 10, 11, 12]),
                ([19, 20, 21, 22], [27]),
                ([29, 30, 31, 32], [34, 35])
            ),
            FadeOut(sub2) 
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(betas[1], betas[2],
                ([i for i in range(21, 36)], [21, 22, 23, 24, 25])
            )
        )
        self.wait(delay)
        self.play(ReplacementTransform(betas[2], betas[3]))
        self.wait(delay)
        self.play(Unwrite(betas[3]))
        self.play(Write(betas[4]))
        self.play(TransformByGlyphMap(betas[4], betas[5],
                ([2], [2, 3, 4, 5, 6]),
                ([4], [8, 9, 10, 11, 12]),
                ([9], [17, 18, 19, 20, 21]),
                ([13], [25, 26, 27, 28, 29]),
                ([18], [34, 35, 36, 37, 38]),
                ([20], [40, 41, 42, 43, 44])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(betas[5], betas[6],
                ([i for i in range(15)], [])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(betas[6], betas[7],
                ([i for i in range(19, 30)], [19])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(betas[7], betas[8],
                ([i for i in range(16, 21)], [])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(betas[8], betas[9],
                ([], [10, 11]),
                ([11], [13])
            )
        )
        self.wait(delay)
        self.play(betas[9].animate.shift(UP*2))
        self.play(Write(betas[10]),
                FadeIn(note3)
        )
        self.play(FadeOut(note3))
        self.play(Write(sub3))
        self.wait(delay)
        self.play(FadeOut(betas[10]), FadeOut(sub3))
        self.play(betas[9].animate.shift(DOWN*2))
        self.play(ReplacementTransform(betas[9], betas[11]))
        self.wait(delay)
        self.play(TransformByGlyphMap(betas[11], betas[12],
                ([5, 6, 10, 12], []),
                ([7, 11], [5, 6, 7]),
                ([9, 11], [9, 10, 11, 12])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(betas[12], betas[13],
                ([5, 6, 7, 8], [])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(betas[13], betas[14],
                ([4, 6, 9], []),
                ([], [4])
            )
        )
        self.wait(delay)
        self.play(Unwrite(betas[14]))
        self.play(Write(integrals[11]))
        self.wait(delay)
        self.play(TransformByGlyphMap(integrals[11], integrals[12],
                ([i for i in range(18, 30)], [i for i in range(18, 36)])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(integrals[12], integrals[13],
                ([i for i in range(18, 36)], [i for i in range(18, 30)])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(integrals[13], integrals[14],
                ([18, 19, 20, 21, 22], [16, 17, 18]),
                ([16, 17], [])
            )
        )
        self.play(Create(result_box),
            ApplyWave(integrals[14], amplitude=0.1, wavelength=0.3)
        )
        self.wait(delay)
        self.play(FadeOut(result_box),
            FadeOut(integrals[14])
        )
        self.play(FadeIn(epilogue1, shift=UP),
            FadeIn(epilogue2, shift=UP)
        )
        self.wait(2*delay)
