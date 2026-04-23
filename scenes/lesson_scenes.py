from manim import *

from scenes.components import ExamTable, EquilibriumGraph, ParticleBox, ReactionEquation, ShiftArrow


class BaseScene(Scene):
    def add_background(self):
        bg = Rectangle(width=16, height=9, fill_color="#080C14", fill_opacity=1, stroke_width=0)
        self.add(bg)


class Scene1TitleHook(BaseScene):
    def construct(self):
        self.add_background()
        # Narration: Introduce the big idea in cinematic style.
        title = Text("Chemical Equilibrium", font_size=72, color=WHITE)
        subtitle = Text("When reactions do not stop — they balance.", font_size=32, color=BLUE_B).next_to(title, DOWN)
        arrow = MathTex(r"\rightleftharpoons", font_size=82, color=GOLD).next_to(subtitle, DOWN, buff=0.6)
        particles = VGroup(*[Dot(radius=0.03, color=BLUE_A).shift(UP * 0.8 + RIGHT * i * 0.25) for i in range(-8, 9)])

        self.play(FadeIn(title, shift=UP), run_time=1.8)
        self.play(Write(subtitle), run_time=1.2)
        self.play(FadeIn(arrow, scale=0.8), LaggedStart(*[FadeIn(d, scale=0.2) for d in particles], lag_ratio=0.05))
        self.wait(1)


class Scene2DynamicEquilibrium(BaseScene):
    def construct(self):
        self.add_background()
        # Narration: Forward and reverse happen simultaneously.
        eq = ReactionEquation(r"\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3").to_edge(UP)
        box = ParticleBox(label="Dynamic system", n_left=12, n_right=6).shift(DOWN * 0.4)
        label = Text("Forward and reverse reactions happen together", font_size=28).to_edge(DOWN)

        self.play(FadeIn(eq), FadeIn(box))
        self.play(box.jitter_animation(run_time=2.5))
        self.play(Write(label))
        self.wait(1)


class Scene3RateVsTimeGraph(BaseScene):
    def construct(self):
        self.add_background()
        # Narration: Forward rate falls, reverse rises, then equal.
        graph = EquilibriumGraph()
        forward_text = Text("Forward rate", font_size=24, color=BLUE_B).next_to(graph, LEFT)
        reverse_text = Text("Reverse rate", font_size=24, color=GOLD_C).next_to(graph, RIGHT)
        self.play(Create(graph.axes), FadeIn(graph.x_label), FadeIn(graph.y_label))
        self.play(Create(graph.forward_curve), Write(forward_text), run_time=2)
        self.play(Create(graph.reverse_curve), Write(reverse_text), run_time=2)
        self.play(FadeIn(graph.eq_line), Write(graph.eq_text), run_time=1.2)
        self.wait(1)


class Scene4LeChatelier(BaseScene):
    def construct(self):
        self.add_background()
        # Narration: If disturbed, system opposes the change.
        eq = ReactionEquation(r"\text{System at equilibrium}").to_edge(UP)
        balance = Line(LEFT * 2, RIGHT * 2, color=WHITE, stroke_width=10).shift(UP * 0.8)
        disturbance = Text("Disturbance", color=RED_B, font_size=34).shift(LEFT * 3 + DOWN * 0.2)
        shift = ShiftArrow(direction="right", label="System fights back").shift(DOWN * 1.3)

        self.play(Write(eq), GrowFromCenter(balance))
        self.play(FadeIn(disturbance, shift=RIGHT))
        self.play(balance.animate.rotate(-0.15), run_time=0.8)
        self.play(FadeIn(shift), run_time=1)
        self.wait(1)


class Scene5ConcentrationChange(BaseScene):
    def construct(self):
        self.add_background()
        # Narration: Adding reactant shifts equilibrium right.
        eq = ReactionEquation(r"\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3").to_edge(UP)
        box = ParticleBox(n_left=8, n_right=5, label="Concentration change").shift(UP * 0.1)
        added = VGroup(*[Dot(radius=0.06, color=BLUE_D).move_to(box.container.get_left() + RIGHT * (0.7 + i * 0.2)) for i in range(5)])
        shift = ShiftArrow(direction="right", label="Shifts right").to_edge(DOWN)
        exam = Text(
            "The equilibrium shifts to the right to use up the added reactant.",
            font_size=28,
            color=WHITE,
        ).to_edge(DOWN)

        self.play(FadeIn(eq), FadeIn(box))
        self.play(LaggedStart(*[FadeIn(d, shift=LEFT * 0.3) for d in added], lag_ratio=0.08), run_time=1.5)
        self.play(FadeIn(shift), run_time=1)
        self.play(ReplacementTransform(shift, exam))
        self.wait(1)


class Scene6PressureChange(BaseScene):
    def construct(self):
        self.add_background()
        # Narration: Higher pressure favors fewer gas moles.
        eq = ReactionEquation(r"\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3").to_edge(UP)
        mole_count = VGroup(
            Text("Left = 4 mol gas", font_size=30, color=BLUE_B),
            Text("Right = 2 mol gas", font_size=30, color=GOLD_C),
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT)

        container = ParticleBox(width=5.6, height=3.2, n_left=10, n_right=6, label="Gas container")
        compressed = container.copy().scale(0.8)
        compressed.label = Text("Pressure increased", font_size=24, color=RED_A).next_to(compressed.container, UP)
        shift = ShiftArrow(direction="right", label="Favors fewer gas moles").to_edge(DOWN)

        self.play(FadeIn(eq), FadeIn(container), FadeIn(mole_count))
        self.play(Transform(container, compressed), run_time=1.8)
        self.play(FadeIn(shift), run_time=1)
        self.wait(1)


class Scene7TemperatureChange(BaseScene):
    def construct(self):
        self.add_background()
        # Narration: Exothermic reaction + heat means shift left.
        eq = ReactionEquation(r"2\text{SO}_2 + \text{O}_2 \rightleftharpoons 2\text{SO}_3,\ \Delta H < 0").to_edge(UP)
        heat = Text("Heat is a product", font_size=30, color=GOLD).shift(UP * 0.8)
        flame = Triangle(color=ORANGE, fill_opacity=0.8).scale(0.4).shift(DOWN * 0.2)
        shift = ShiftArrow(direction="left", label="Increase T ⇒ shift left").to_edge(DOWN)
        exam = Text("Added heat is opposed, so equilibrium shifts left.", font_size=26).to_edge(DOWN)

        self.play(FadeIn(eq), FadeIn(heat))
        self.play(GrowFromEdge(flame, DOWN), Flash(flame, color=RED_A), run_time=1.4)
        self.play(FadeIn(shift), run_time=1)
        self.play(ReplacementTransform(shift, exam), run_time=1)
        self.wait(1)


class Scene8Catalyst(BaseScene):
    def construct(self):
        self.add_background()
        # Narration: Catalyst lowers activation energy but no equilibrium shift.
        axes = Axes(x_range=[0, 10, 2], y_range=[0, 6, 2], x_length=8, y_length=4, tips=False).shift(DOWN * 0.2)
        uncatalysed = axes.plot(lambda x: 0.1 * (x - 5) ** 2 + 1.8, color=RED_C)
        catalysed = axes.plot(lambda x: 0.05 * (x - 5) ** 2 + 1.2, color=GREEN_C)
        t1 = Text("Without catalyst", font_size=24, color=RED_C).to_edge(LEFT)
        t2 = Text("With catalyst", font_size=24, color=GREEN_C).next_to(t1, DOWN)
        claim = Text("No shift in equilibrium position", font_size=30, color=GOLD).to_edge(DOWN)

        self.play(Create(axes))
        self.play(Create(uncatalysed), FadeIn(t1), run_time=1.4)
        self.play(Create(catalysed), FadeIn(t2), run_time=1.4)
        self.play(Write(claim), run_time=1)
        self.wait(1)


class Scene9ExperimentVisualiser(BaseScene):
    def construct(self):
        self.add_background()
        # Narration: Side-by-side closed systems disturbed differently.
        left_flask = ParticleBox(width=4.2, height=2.8, label="Closed system", n_left=8, n_right=8).shift(LEFT * 3)
        right_flask = ParticleBox(width=4.2, height=2.8, label="Closed system", n_left=8, n_right=8).shift(RIGHT * 3)
        temp_disturb = Text("Disturbance: +Temperature", font_size=24, color=RED_B).next_to(left_flask, DOWN)
        conc_disturb = Text("Disturbance: +Reactant", font_size=24, color=BLUE_B).next_to(right_flask, DOWN)
        new_eq = Text("New equilibrium", font_size=30, color=GOLD).to_edge(DOWN)

        self.play(FadeIn(left_flask), FadeIn(right_flask))
        self.play(left_flask.jitter_animation(1.8), right_flask.jitter_animation(1.8))
        self.play(Write(temp_disturb), Write(conc_disturb))
        self.play(
            left_flask.right_particles.animate.set_opacity(0.35),
            right_flask.right_particles.animate.set_opacity(1.0).scale(1.1),
            run_time=1.4,
        )
        self.play(FadeIn(new_eq))
        self.wait(1)


class Scene10ExamMethod(BaseScene):
    def construct(self):
        self.add_background()
        # Narration: 6-step exam method learners should memorise.
        title = Text("Exam Method", font_size=56, color=WHITE).to_edge(UP)
        steps = [
            "1. Identify the disturbance.",
            "2. Apply Le Chatelier's Principle.",
            "3. Check concentration, pressure, or temperature.",
            "4. Count gas moles if pressure changes.",
            "5. Check ΔH if temperature changes.",
            "6. Write a full scientific sentence.",
        ]
        bullets = VGroup(*[Text(s, font_size=30, color=BLUE_A) for s in steps]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        bullets.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=1)

        self.play(Write(title))
        self.play(LaggedStart(*[FadeIn(b, shift=RIGHT * 0.2) for b in bullets], lag_ratio=0.2), run_time=3)
        self.wait(1)


class Scene11PracticeQuestion(BaseScene):
    def construct(self):
        self.add_background()
        # Narration: Walk through a full exam-style pressure question.
        reaction = ReactionEquation(r"\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3,\ \Delta H < 0").to_edge(UP)
        question = Text("What happens to ammonia yield when pressure increases?", font_size=32, color=WHITE).next_to(
            reaction, DOWN
        )
        mole = Text("4 mol gas  →  2 mol gas", font_size=36, color=BLUE_B).shift(DOWN * 0.3)
        compress = Text("Pressure ↑", font_size=34, color=RED_B).next_to(mole, DOWN)
        shift = ShiftArrow(direction="right", label="Shift right").next_to(compress, DOWN)
        answer = Text("Ammonia yield increases.", font_size=38, color=GOLD).to_edge(DOWN)

        self.play(FadeIn(reaction), Write(question))
        self.play(Write(mole), run_time=1.2)
        self.play(FadeIn(compress), run_time=0.8)
        self.play(FadeIn(shift), run_time=1)
        self.play(ReplacementTransform(shift, answer), run_time=1)
        self.wait(1)


class Scene12FinalRecap(BaseScene):
    def construct(self):
        self.add_background()
        # Narration: Final recap table to lock in exam marks.
        title = Text("Final Recap", font_size=58, color=WHITE).to_edge(UP)
        table = ExamTable().scale(1.1)
        self.play(Write(title))
        self.play(FadeIn(table), run_time=1.8)
        self.wait(2)
