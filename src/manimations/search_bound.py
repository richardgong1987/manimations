from manim import (
    DOWN,
    GREEN,
    LEFT,
    UP,
    YELLOW,
    FadeIn,
    MathTex,
    Scene,
    SurroundingRectangle,
    Create,
    Text,
    VGroup,
    Write,
)

# The step budgets come from hero.asl: target_step_budget(24) and delivery_step_budget(64).
SEARCH_TARGETS = r"\text{search targets: } N = 0, 1, \dots, 63 \quad \text{(stop when } N \ge 64 \text{ or nothing is needed)}"
TRAVEL_BUDGET = r"\text{each target: budget } B = 24, 23, \dots, 1 \;\Rightarrow\; \le 24 \text{ moves}"
DELIVERY_BUDGET = r"\text{delivery to Goblin: } \le 64 \text{ moves}"
BOUND_TERMS = (r"\text{moves}", r"\le", r"64 \times 24 + 64", r"=", r"1600")


class SearchBound(Scene):
    def construct(self):
        title = Text("Why a missing coin cannot cause an endless search", font_size=36).to_edge(UP)
        reasons = VGroup(
            MathTex(SEARCH_TARGETS, font_size=34),
            MathTex(TRAVEL_BUDGET, font_size=34),
            MathTex(DELIVERY_BUDGET, font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        reasons.next_to(title, DOWN, buff=0.8).to_edge(LEFT, buff=0.8)
        bound = MathTex(*BOUND_TERMS, font_size=56).next_to(reasons, DOWN, buff=0.9).set_x(0)
        observed = Text(
            "Scenario 1 (no coin): 70 actions, then\n“SEARCH COMPLETE: 64 cells inspected; some item types are missing.”",
            font_size=24,
            line_spacing=0.9,
        ).to_edge(DOWN, buff=0.6)

        self.play(FadeIn(title))
        for reason in reasons:
            self.play(Write(reason), run_time=2)
            self.wait(2)

        self.play(Write(bound[:3]), run_time=2)
        self.play(Write(bound[3:]))
        self.play(Create(SurroundingRectangle(bound[4], color=YELLOW, buff=0.15)))
        self.wait(2)

        self.play(FadeIn(observed.set_color(GREEN), shift=UP * 0.2))
        self.wait(4)
