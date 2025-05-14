from manim import *
from MF_Tools import TransformByGlyphMap
from itertools import chain

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 2560
config.pixel_width = 1440

class Thumbnail(Scene):
    def construct(self):
        integral = MathTex(r"\int_0^{\infty} \frac{\sin(x)\sin(\sin x)}{x^2}e^{\cos x} \, dx",
            font_size=60)
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
            r"\int_0^{\infty} \frac{\sin(x)\sin(\sin x)}{x^2} e^{\cos x} \dd{x}",
            r"\int_0^{\infty} \frac{\sin(x) \mathrm{Im} (e^{i\sin x})}{x^2} e^{\cos x} \dd{x}",
            r"\mathrm{Im} \int_0^{\infty} \frac{\sin x}{x^2} e^{\cos x + i\sin x} \dd{x}",
            r"\mathrm{Im} \int_0^{\infty} \frac{\sin x}{x^2} e^{e^{ix}} \dd{x}",
            r"\mathrm{Im} \int_0^{\infty} \frac{\sin x}{x^2} \sum_{k = 0}^{\infty} \frac{(e^{ix})^k}{k!} \dd{x}",
            r"\mathrm{Im} \sum_{k=0}^{\infty} \frac{1}{k!} \int_0^{\infty} \frac{\sin x}{x^2} e^{kix} \dd{x}", # 5
            r"\sum_{k = 0}^{\infty} \frac{1}{k!} \int_0^{\infty} \frac{\sin x}{x^2} \mathrm{Im} (e^{kix}) \dd{x}",
            r"\sum_{k = 0}^{\infty} \frac{1}{k!} \int_0^{\infty} \frac{\sin x}{x^2} \sin kx \dd{x}",
            r"\sum_{k = 1}^{\infty} \frac{1}{k!} \int_0^{\infty} \frac{\sin x \sin kx}{x^2} \dd{x}",
            r"\sum_{k = 1}^{\infty} \frac{1}{k!} \int_0^{\infty} \frac{\cos (k - 1)x - \cos (k + 1)x}{2x^2} \dd{x}",
            r"\frac{1}{2} \sum_{k = 1}^{\infty} \frac{1}{k!} \int_0^{\infty} \int_{k-1}^{k+1} \frac{\sin (yx)}{x} \dd{y} \dd{x}", # 10
            r"\frac{1}{2} \sum_{k = 1}^{\infty} \frac{1}{k!} \int_{k-1}^{k+1} \int_0^{\infty} \frac{\sin (yx)}{x} \dd{x} \dd{y}",
            r"\int_0^{\infty} \frac{\sin (at)}{t} \dd{t} = \frac{\pi}{2} \quad a > 0",
            r"\frac{1}{2} \sum_{k = 1}^{\infty} \frac{1}{k!} \int_{k-1}^{k+1} \frac{\pi}{2} \dd{y}",
            r"\frac{1}{2} \sum_{k = 1}^{\infty} \frac{1}{k!} \cdot 2 \cdot \frac{\pi}{2}",
            r"\frac{\pi}{2} \sum_{k = 1}^{\infty} \frac{1}{k!}", # 15
            r"\frac{\pi}{2} (e - 1)",
            r"\int_0^{\infty} \frac{\sin(x)\sin(\sin x)}{x^2} e^{\cos x} \dd{x} = \frac{\pi}{2}(e-1)"
        ]

        latex = [MathTex(i, font_size=fontsize, tex_template=temp) for i in raw_latex]

        # Notes
        note1 = MathTex(r"\cos A - \cos B = -2\sin \frac{A + B}{2}\sin \frac{A - B}{2}",
                        color=LIGHT_GREY, font_size=fontsize/1.5).next_to(latex[9], DOWN)
        note2 = MathTex(r"(1) \text{ Proof in description}",
                        color=LIGHT_GREY, font_size=fontsize/2).next_to(latex[12], DOWN)

        # Mobject initialization
        for i in [9, 10, 11, 12]: latex[i].scale(0.75)
        latex[17].scale(0.7)

        # Coloring
        latex[8][0][4].set_color(YELLOW)

        # Epilogue
        result_box = SurroundingRectangle(latex[17], color=YELLOW, buff=0.2)

        # Animation
        self.play(Write(latex[0]))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[0], latex[1],
                ([9, 10, 11], [9, 10]),
                ([13, 14, 15, 16], [14, 15, 16, 17]),
                ([12, 17], [11, 18]),
                ([], [12, 13])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[1], latex[2],
                ([9, 10], [0, 1]),
                ([6, 8, 11, 12, 18], []),
                (list(range(13, 18)), list(range(17, 23)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[2], latex[3],
                (list(range(13, 23)), [13, 14, 15])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[3], latex[4],
                ([12, 13, 14, 15], list(range(12, 26)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[4], latex[5],
                ([17, 21], []),
                ([18, 19, 20, 22], [21, 22, 23, 24]),
                (list(chain(range(12, 17), [23, 24, 25])), list(range(2, 11)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[5], latex[6],
                ([0, 1], [19, 20]),
                ([], [21, 26])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[6], latex[7],
                (list(chain(range(19, 23), [26, 24])), [19, 20, 21]),
                ([23, 25], [22, 23])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[7], latex[8],
                (list(range(19, 24)), list(range(16, 21)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[8], latex[9],
                ([12, 13, 14], [12, 13, 14]),
                ([15], list(range(15, 21))),
                ([], [21]),
                ([16, 17, 18], [22, 23, 24]),
                ([19, 20], list(range(25, 31))),
                ([], [32])
            ),
            FadeIn(note1)
        )
        self.play(FadeOut(note1))
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[9], latex[10],
                ([32], [0, 1, 2]),
                ([16, 17, 18], [19, 20, 21]),
                ([26, 27, 28], [16, 17, 18]),
                (list(chain(range(12, 16), range(19, 26), [29, 30])), list(range(22, 29))),
                ([], [15, 31, 32]),
                ([34], [])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[10], latex[11],
                ([13], [20]),
                ([14], [21]),
                ([16, 17, 18], [13, 14, 15]),
                ([19, 20, 21], [16, 17, 18]),
                ([32], [34]),
                ([34], [32])
            )
        )
        self.wait(delay)
        self.play(latex[11].animate.shift(UP*2))
        self.play(
            Write(latex[12]),
            FadeIn(note2)
        )
        self.wait(delay)
        self.play(FadeOut(note2, latex[12]))
        self.play(
            TransformByGlyphMap(
                latex[11], latex[13],
                (list(range(19, 33)), [19, 20, 21])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[13], latex[14],
                (list(chain(range(12, 19), [22, 23])), [12, 13, 14])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[14], latex[15],
                ([0, 1, 2, 12, 13, 14], []),
                ([15, 16, 17], [0, 1, 2])
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[15], latex[16],
                (list(range(3, 12)), list(range(3, 8)))
            )
        )
        self.wait(delay)
        self.play(
            TransformByGlyphMap(
                latex[16], latex[17],
                ([], list(range(29)))
            )
        )
        self.wait(delay)
        self.play(
            Create(result_box),
            ApplyWave(latex[17], amplitude=0.1, wavelength=0.2)
        )
        self.wait(delay)


