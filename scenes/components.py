from __future__ import annotations

import numpy as np

from manim import *


class ParticleBox(VGroup):
    """Reusable particle container for gas/equilibrium demonstrations."""

    def __init__(
        self,
        width: float = 5,
        height: float = 3,
        n_left: int = 8,
        n_right: int = 8,
        left_color: ManimColor = BLUE_C,
        right_color: ManimColor = GOLD_C,
        label: str = "Closed system",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.container = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.12,
            stroke_color=BLUE_E,
            fill_color="#0E1420",
            fill_opacity=0.6,
        )
        self.left_particles = VGroup(*[Dot(radius=0.06, color=left_color) for _ in range(n_left)])
        self.right_particles = VGroup(*[Dot(radius=0.06, color=right_color) for _ in range(n_right)])
        self.label = Text(label, font_size=24, color=WHITE).next_to(self.container, UP, buff=0.2)

        for p in self.left_particles:
            p.move_to(self.random_point_in_box(width, height) + LEFT * 0.8)
        for p in self.right_particles:
            p.move_to(self.random_point_in_box(width, height) + RIGHT * 0.8)

        self.add(self.container, self.left_particles, self.right_particles, self.label)

    @staticmethod
    def random_point_in_box(width: float, height: float) -> np.ndarray:
        x = np.random.uniform(-width / 2 + 0.25, width / 2 - 0.25)
        y = np.random.uniform(-height / 2 + 0.25, height / 2 - 0.25)
        return np.array([x, y, 0])

    def jitter_animation(self, run_time: float = 2.0) -> AnimationGroup:
        anims = []
        w = self.container.width
        h = self.container.height
        for p in [*self.left_particles, *self.right_particles]:
            anims.append(
                p.animate.move_to(self.random_point_in_box(w, h)).set_run_time(run_time).set_rate_func(linear)
            )
        return AnimationGroup(*anims, lag_ratio=0.03)


class ReactionEquation(VGroup):
    """Reusable reaction equation visual with dynamic shift arrow."""

    def __init__(self, equation: str, font_size: int = 42, **kwargs):
        super().__init__(**kwargs)
        self.eq = MathTex(equation, font_size=font_size, color=WHITE)
        self.add(self.eq)


class ShiftArrow(VGroup):
    """Arrow + label helper for left/right shift indications."""

    def __init__(self, direction: str = "right", label: str = "Shifts right", **kwargs):
        super().__init__(**kwargs)
        vec = RIGHT if direction.lower() == "right" else LEFT
        self.arrow = Arrow(ORIGIN, vec * 2, buff=0, stroke_width=8, color=GOLD)
        self.text = Text(label, font_size=26, color=GOLD).next_to(self.arrow, DOWN, buff=0.15)
        self.add(self.arrow, self.text)


class EquilibriumGraph(VGroup):
    """Rate vs time graph used in equilibrium scenes."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 8, 2],
            x_length=8,
            y_length=4,
            axis_config={"color": BLUE_B},
            tips=False,
        )
        self.x_label = self.axes.get_x_axis_label(Text("Time", font_size=24))
        self.y_label = self.axes.get_y_axis_label(Text("Rate", font_size=24))

        self.forward_curve = self.axes.plot(lambda x: 5 * np.exp(-0.55 * x) + 2, color=BLUE_B)
        self.reverse_curve = self.axes.plot(lambda x: 6 - 4 * np.exp(-0.55 * x), color=GOLD_C)

        self.eq_line = DashedLine(
            self.axes.c2p(0, 4.0), self.axes.c2p(10, 4.0), color=WHITE, stroke_opacity=0.4
        )
        self.eq_text = Text("At equilibrium: rate forward = rate reverse", font_size=24, color=WHITE).next_to(
            self.axes, DOWN
        )
        self.add(
            self.axes,
            self.x_label,
            self.y_label,
            self.forward_curve,
            self.reverse_curve,
            self.eq_line,
            self.eq_text,
        )


class ExamTable(VGroup):
    """Summary table for shift changes."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        table_data = [
            ["Add reactant", "Right", "Use up added reactant"],
            ["Increase pressure", "Fewer gas moles", "Reduces pressure"],
            ["Increase temperature (exo)", "Left", "Oppose added heat"],
            ["Catalyst", "No shift", "Speeds both directions"],
        ]
        table = Table(
            table_data,
            col_labels=[
                Text("Change", weight=BOLD),
                Text("Shift", weight=BOLD),
                Text("Reason", weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_color": BLUE_D},
            element_to_mobject=lambda x: Text(str(x), font_size=24),
        ).scale(0.6)
        self.add(table)
