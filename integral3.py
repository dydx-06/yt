from manim import *
from MF_Tools import TransformByGlyphMap
from itertools import chain

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 2560
config.pixel_width = 1440

class Thumbnail(Scene):
    def construct(self):
        integral = MathTex(r"\int_0^{\infty} \frac{(x + 1)\ln^4(x)\tan^{-1}(x)}{\sqrt{x}(x^2 + 1)} \, dx",
            font_size = 60)
        self.add(integral)

class Integral(Scene):
    def construct(self):

        # Initializing
        fontsize = 44   
        delay = 0.5
        scale = 4/5

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{physics}")

        # Main mobjects
        raw_latex = [
            r"\int_0^{\infty} \frac{(x + 1)\ln^4(x)\tan^{-1}(x)}{\sqrt{x}(x^2 + 1)} \, dx",
            r"I = \int_0^{\infty} \frac{(x + 1)\ln^4(x)\tan^{-1}(x)}{\sqrt{x}(x^2 + 1)} \, dx",
            r"I = \int_{\infty}^0 \frac{(x^{-1} + 1)\ln^4(x^{-1})\tan^{-1}(x^{-1})}{\sqrt{x^{-1}(x^{-2} + 1)}} \cdot \frac{dx}{-x^2}",
            r"I = \int_0^{\infty} \frac{(x + 1)\ln^4(x)\tan^{-1}(x^{-1})}{\sqrt{x}(x^2 + 1)} \, dx",
            r"I = \int_0^{\infty} \frac{(x + 1)\ln^4(x)\tan^{-1}(x)}{\sqrt{x}(x^2 + 1)} \, dx",
            r"+",
            r"2I = \int_0^{\infty} \frac{(x+1)\ln^4(x)}{\sqrt{x}(x^2 + 1)} (\tan^{-1}(x) + \tan^{-1}(x^{-1})) \, dx",
            r"I = \frac{1}{2} \int_0^{\infty} \frac{(x+1)\ln^4(x)}{\sqrt{x}(x^2 + 1)} \cdot \frac{\pi}{2} \, dx",
            r"I = \frac{\pi}{4}\int_0^{\infty} \frac{(x+1)\ln^4(x)}{\sqrt{x}(x^2 +1)} \, dx",
            r"I = \frac{\pi}{4}\int_0^{\frac{\pi}{2}} \frac{(\tan x + 1)\ln^4 (\tan x)}{\sqrt{\tan x}(\tan^2 x + 1)} \cdot \sec^2 x \, dx",
            r"I = \frac{\pi}{4}\int_0^{\frac{\pi}{2}} \frac{(\tan x + 1)\ln^4(\tan x)}{\sqrt{\tan x} \cdot \sec^2 x} \cdot \sec^2 x \, dx",
            r"I = \frac{\pi}{4}\int_0^{\frac{\pi}{2}} \left ( \sqrt{\tan x} + \frac{1}{\sqrt{\tan x}} \right )\ln^4 (\tan x) \, dx",
            r"+",
            r"\frac{\pi}{4}\int_0^{\frac{\pi}{2}}\sqrt{\tan x}\ln^4 (\tan x) \, dx",
            r"\frac{\pi}{4}\int_0^{\frac{\pi}{2}}\frac{\ln^4(\tan x)}{\sqrt{\tan x}} \, dx",
            r"\frac{\pi}{4}\int_0^{\frac{\pi}{2}} \frac{\ln^4 (\tan (\pi/2 - x))}{\sqrt{\tan (\pi/2 - x)}} \, dx",
            r"\frac{\pi}{4}\int_0^{\frac{\pi}{2}} \frac{\ln^4(\cot x)}{\sqrt{\cot x}} \, dx",
            r"\frac{\pi}{4}\int_0^{\frac{\pi}{2}} \sqrt{\tan x}\ln^4(\tan x) \, dx",
            r"\frac{\pi}{4} \int_0^{\frac{\pi}{2}} 2\sqrt{\tan x}\ln^4(\tan x) \, dx",
            r"I = \frac{\pi}{2} \int_0^{\frac{\pi}{2}} \sqrt{\tan x}\ln^4(\tan x) \, dx",
            r"\pdv{s}(\tan x)^s = (\tan x)^s \ln(\tan x)",
            r"\pdv[2]{s}(\tan x)^s = (\tan x)^s \ln^2(\tan x)",
            r"\pdv[3]{s}(\tan x)^s = (\tan x)^s \ln^3(\tan x)",
            r"\pdv[4]{s}(\tan x)^s = (\tan x)^s \ln^4(\tan x)",
            r"I = \frac{\pi}{2} \int_0^{\frac{\pi}{2}} \sqrt{\tan x}\ln^4(\tan x) \, dx",
            r"I = \frac{\pi}{2} \int_0^{\frac{\pi}{2}} \pdv[4]{s}(\tan x)^s \eval_{s=\frac{1}{2}} \, dx",
            r"I = \frac{\pi}{2} \frac{d^4}{ds^4} \left ( \int_0^{\frac{\pi}{2}} \tan^s x \, dx \right ) \eval_{s=\frac{1}{2}}",
            r"\int_0^{\frac{\pi}{2}} \tan^s x \, dx = \frac{\pi}{2} \sec \frac{\pi s}{2}",
            r"I = \frac{\pi}{2} \frac{d^4}{ds^4} \left ( \frac{\pi}{2} \sec \frac{\pi s}{2} \right ) \eval_{s = \frac{1}{2}}",
            r"I = \frac{\pi^2}{4} \frac{d^4}{ds^4} \left ( \sec \frac{\pi s}{2} \right ) \eval_{s = \frac{1}{2}}",
            r"I = \frac{\pi^2}{4} \cdot \frac{57\pi^4}{8\sqrt{2}}",
            r"I = \frac{57\pi^6}{32\sqrt{2}}"
        ]

        latex = [MathTex(i, font_size=fontsize, tex_template=temp) for i in raw_latex]
        result_box = SurroundingRectangle(latex[31], color=YELLOW, buff=0.2)

        # Mobject initialization
        latex[4].shift(DOWN * 1.5)
        latex[6].scale(scale)
        latex[11].scale(scale)
        latex[13].shift(UP * 1.5)
        for i in range(14, 18): latex[i].shift(DOWN * 1.5)

        # Substitutions and notes
        sub1 = MathTex(r"x = \frac{1}{x}",
                    substrings_to_isolate=[r"\frac{1}{x}"], font_size=fontsize).next_to(latex[0], DOWN)
        sub1_diff = MathTex(r"dx = \frac{dx}{-x^2}",
                    substrings_to_isolate=[r"\frac{dx}{-x^2}"], font_size=fontsize).next_to(sub1, DOWN)
        note1 = MathTex(r"\tan^{-1} (x) + \tan^{-1} \left ( \frac{1}{x} \right ) = \frac{\pi}{2}",
                    font_size=fontsize/1.5, color=LIGHT_GREY).next_to(latex[7], DOWN)
        sub2 = MathTex(r"x = \tan x",
                    substrings_to_isolate=[r"\tan x"], font_size=fontsize).next_to(latex[8], DOWN)
        sub2_diff = MathTex(r"dx = \sec^2 x \, dx",
                    substrings_to_isolate=[r"\sec^2 x \, dx"], font_size=fontsize).next_to(sub2, DOWN)
        note2 = MathTex(r"\int_a^b f(t) \, dt = \int_a^b f(a + b - t) \, dt",
                    font_size=fontsize/1.5, color=LIGHT_GREY).next_to(latex[15], DOWN)
        note3 = Tex(r"(1) \text{Proof in description}",
                    font_size=fontsize/1.5, color=LIGHT_GREY).next_to(latex[27], DOWN)

        # Coloring
        sub1.set_color_by_tex(r"\frac{1}{x}", YELLOW)
        sub1_diff.set_color_by_tex(r"\frac{dx}{-x^2}", YELLOW)
        for i in chain([6, 7, 8, 16, 17, 18, 26, 27, 28, 33, 34, 35, 37, 38, 39], range(43, 50)):
            latex[2][0][i].set_color(YELLOW)
        for i in range(22, 25): latex[3][0][i].set_color(YELLOW)
        #flash.set_color_by_tex(r"x^{-1}", YELLOW)
        sub2.set_color_by_tex(r"\tan x", YELLOW)
        sub2_diff.set_color_by_tex(r"\sec^2 x \, dx", YELLOW)
        for i in chain([11, 12, 13, 14, 22, 23, 24, 25, 30, 31, 32, 33, 35, 36, 37, 38, 39], range(43, 51)):
            latex[9][0][i].set_color(YELLOW)
        for i in range(21, 24):
            for j in [1, 5, 23]: latex[i][0][j].set_color(YELLOW)

        # Animation
        self.play(Write(latex[0]))
        self.play(TransformByGlyphMap(
            latex[0], latex[1],
            ([], [0, 1])
            )
        )
        self.wait(delay)
        self.play(latex[1].animate.shift(UP))
        self.play(Write(sub1))
        self.play(Write(sub1_diff))
        self.wait(delay)
        self.play(
            FadeOut(sub1),
            FadeOut(sub1_diff)
        )
        self.play(latex[1].animate.shift(DOWN))
        self.play(TransformByGlyphMap(
            latex[1], latex[2],
            ([3], [3]),
            ([4], [4]),
            ([6], [6, 7, 8]),
            ([14], [16, 17, 18]),
            ([22], [26, 27, 28]),
            ([27], [33, 34, 35]),
            ([29, 30], [37, 38, 39]),
            ([34, 35], list(range(43, 50)))
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[2], latex[3],
            ([3], [3]),
            ([4], [4]),
            ([6, 7, 8], [6]),
            ([16, 17, 18], [14]),
            ([33, 34, 35], [29]),
            ([37, 38, 39], [31, 32]),
            (list(range(43, 50)), [36, 37])
            )
        )
        self.wait(delay)
        self.play(latex[3].animate.shift(UP*1.5))
        self.play(Write(latex[4]))
        self.play(GrowFromCenter(latex[5]))
        self.wait(delay)
        self.play(
            FadeOut(latex[3], shift = ORIGIN - latex[3].get_center()),
            FadeOut(latex[4], shift = ORIGIN - latex[4].get_center()),
            FadeOut(latex[5]),
            FadeIn(latex[6])
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[6], latex[7],
            ([0], [2, 3, 4]),
            ([2], [1]),
            (list(range(27, 48)), [29, 30, 31, 32])
            ),
            FadeIn(note1)
        )
        self.wait(delay)
        self.play(FadeOut(note1))
        self.play(TransformByGlyphMap(
            latex[7], latex[8],
            ([2, 3, 1, 29, 30, 31, 32], [2, 3, 4])
            )
        )
        self.play(latex[8].animate.shift(UP))
        self.play(Write(sub2))
        self.play(Write(sub2_diff))
        self.wait(delay)
        self.play(
            FadeOut(sub2),
            FadeOut(sub2_diff)
        )
        self.play(latex[8].animate.shift(DOWN))
        self.play(TransformByGlyphMap(
            latex[8], latex[9],
            ([6], [6, 7, 8]),
            ([9], [11, 12, 13, 14]),
            ([17], [22, 23, 24, 25]),
            ([22], [30, 31, 32, 33]),
            ([24], [35, 36, 37, 39]),
            ([29, 30], list(range(43, 51)))
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[9], latex[10],
            (list(range(34, 43)), list(range(34, 40)))
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[10], latex[11],
            ([11, 12, 13, 14], list(range(11, 17))),
            ([15], [17]),
            ([16], list(range(18, 26))),
            ([17], [26]),
            (list(range(18, 27)), list(range(27, 36))),
            (list(range(27, 34)), []),
            (list(range(34, 46)), [])
            )
        )
        self.wait(delay)
        self.play(
            FadeOut(latex[11], run_time = 1),
            FadeIn(latex[13], shift = UP),
            FadeIn(latex[14], shift = DOWN),
            GrowFromCenter(latex[12])
        )
        self.wait(delay * 1.5)
        self.play(TransformByGlyphMap(
            latex[14], latex[15],
            ([15], list(range(15, 22))),
            ([23], list(range(29, 36)))
            ),
            FadeIn(note2)
        )
        self.play(FadeOut(note2))
        self.play(TransformByGlyphMap(
            latex[15], latex[16],
            (list(range(12, 22)), list(range(12, 16))),
            (list(range(26, 36)), list(range(20, 24)))
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[16], latex[17],
            (list(range(17, 24)), list(range(8, 14)))
            )
        )
        self.wait(delay)
        self.play(
            FadeOut(latex[17], shift = UP*1.5),
            FadeOut(latex[13], shift = DOWN*1.5),
            FadeOut(latex[12]),
            FadeIn(latex[18])
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[18], latex[19],
            ([], [0, 1]),
            ([8, 2], [4])
            )
        )
        self.wait(delay)
        self.play(Unwrite(latex[19]))
        self.play(Write(latex[20]))
        self.play(TransformByGlyphMap(
            latex[20], latex[21],
            ([], [1, 5]),
            ([], [23])
            )
        )
        self.play(TransformByGlyphMap(
            latex[21], latex[22],
            ([1], [1]),
            ([5], [5]),
            ([23], [23])
            )
        )
        self.play(TransformByGlyphMap(
            latex[22], latex[23],
            ([1], [1]),
            ([5], [5]),
            ([23], [23])
            )
        )
        self.wait(delay)
        self.play(Unwrite(latex[23]))
        self.play(Write(latex[24]))
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[24], latex[25],
            (list(range(10, 25)), list(range(10, 32)))
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[25], latex[26],
            (list(range(10, 16)), list(range(5, 11))),
            ([16, 21], [11, 24]),
            (list(range(23, 32)), list(range(25, 34)))
            )
        )
        self.play(latex[26].animate.shift(UP * 2))
        self.play(Write(latex[27]))
        self.play(FadeIn(note3))
        self.wait(delay)
        self.play(
            Unwrite(latex[27]),
            FadeOut(note3)
        )
        self.play(latex[26].animate.shift(DOWN * 2))
        self.play(TransformByGlyphMap(
            latex[26], latex[28],
            (list(range(11, 25)), list(range(11, 23)))
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[28], latex[29],
            ([2, 3, 4, 12, 13, 14], [2, 3, 4, 5])
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[29], latex[30],
            (list(range(6, 30)), list(range(6, 16)))
            )
        )
        self.wait(delay)
        self.play(TransformByGlyphMap(
            latex[30], latex[31],
            ([2, 3, 9, 10], [4, 5]),
            ([4, 6, 11], [6]),
            ([5, 12], [7, 8])
            )
        )
        self.play(
            Create(result_box),
            ApplyWave(latex[31], amplitude=0.08, wavelength=0.2)
        )
        self.wait(1)
