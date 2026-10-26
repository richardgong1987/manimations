from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    Arrow,
    FadeIn,
    Indicate,
    MathTex,
    Scene,
    Text,
    VGroup,
    Write,
)

COMPLETE = r"\operatorname{complete} \iff \neg\exists I\; \operatorname{undelivered}(I)"
# Split so the visited count can be highlighted on its own.
ABSENCE_PROVEN = (
    r"\operatorname{absence\_proven} \iff",
    r"|\operatorname{visited}| = 64",
    r"\land\; \neg\operatorname{collection\_uncertain} \;\land\; \neg\exists I\; \operatorname{hero}(I)",
)

# (condition, terminal message, colour), checked top to bottom by !report.
OUTCOMES = (
    (r"\operatorname{complete}", "SUCCESS: all three item types handed to Goblin.", GREEN),
    (r"\operatorname{absence\_proven}", "SEARCH COMPLETE: 64 cells inspected;\nsome item types are missing.", BLUE),
    (r"\text{otherwise}", "INCOMPLETE: inspected N cells;\nabsence is not proven.", ORANGE),
)


class OutcomeReport(Scene):
    def construct(self):
        title = Text("Which outcome does Hero report?", font_size=36).to_edge(UP)
        complete = MathTex(COMPLETE, font_size=34)
        absence_proven = MathTex(*ABSENCE_PROVEN, font_size=34)
        definitions = VGroup(complete, absence_proven).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        definitions.next_to(title, DOWN, buff=0.6)
        outcomes = outcome_rows().next_to(definitions, DOWN, buff=0.7)
        teleporter_note = Text(
            "A teleporter cell is never inspected, so |visited| ≤ 63:\n"
            "a missing item is then reported as INCOMPLETE, never as proven absent.",
            font_size=24,
            line_spacing=0.9,
        ).to_edge(DOWN, buff=0.4)

        self.play(FadeIn(title))
        self.play(Write(complete), run_time=2)
        self.play(Write(absence_proven), run_time=3)
        self.wait(2)

        for row in outcomes:
            self.play(FadeIn(row, shift=RIGHT * 0.3))
            self.wait(1.5)

        self.play(outcomes.animate.shift(UP * 0.3), FadeIn(teleporter_note))
        self.play(Indicate(absence_proven[1], color=ORANGE, scale_factor=1.3))
        self.wait(4)


def outcome_rows() -> VGroup:
    rows = VGroup()
    for condition, message, colour in OUTCOMES:
        check = MathTex(condition, font_size=34, color=colour)
        arrow = Arrow(LEFT, RIGHT, buff=0, color=colour).scale(0.5)
        printed = Text(message, font="Menlo", font_size=18, line_spacing=0.8)
        rows.add(VGroup(check, arrow, printed).arrange(RIGHT, buff=0.3))
    rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
    # Line the arrows up so the messages form one column.
    arrow_x = max(row[1].get_x() for row in rows)
    for row in rows:
        row[1:].shift(RIGHT * (arrow_x - row[1].get_x()))
    return rows
