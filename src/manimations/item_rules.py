from manim import (
    DOWN,
    GREY_B,
    RIGHT,
    UP,
    FadeIn,
    FadeOut,
    Indicate,
    MathTex,
    Scene,
    Text,
    VGroup,
    Write,
)

# Each rule is split into terms so single terms can be highlighted.
# Index 1 is always the ⟺ sign, which the rows are aligned on.
NEEDED = (
    r"\operatorname{needed}(I)",
    r"\iff",
    r"\operatorname{item}(I)",
    r"\land",
    r"\neg\operatorname{hero}(I)",
    r"\land",
    r"\neg\operatorname{delivered}(I)",
)
SHOULD_PICK = (
    r"\operatorname{should\_pick}(I)",
    r"\iff",
    r"\operatorname{item\_here}(I)",
    r"\land",
    r"\operatorname{needed}(I)",
)
SHOULD_DROP = (
    r"\operatorname{should\_drop}(I)",
    r"\iff",
    r"\operatorname{hero}(I)",
    r"\land",
    r"\operatorname{at}(\text{goblin})",
)


class ItemRules(Scene):
    def construct(self):
        title = Text("When does Hero pick up or drop an item?", font_size=36).to_edge(UP)
        needed, should_pick, should_drop = rows_aligned_at_iff(NEEDED, SHOULD_PICK, SHOULD_DROP)
        footnote = Text(
            "¬ means “not currently believed” (negation as failure)",
            font_size=22,
            color=GREY_B,
        ).to_edge(DOWN)

        self.play(FadeIn(title))
        self.play(Write(needed), run_time=2.5)
        self.play(FadeIn(footnote))
        self.wait(2)

        self.play(Write(should_pick), run_time=2)
        self.play(Indicate(should_pick[4]), Indicate(needed[0]))
        duplicates = caption("Duplicates: once hero(gem) is believed, needed(gem) is false,\nso a second gem stays on the ground.", footnote)
        self.play(FadeIn(duplicates), Indicate(needed[4], scale_factor=1.3))
        self.wait(4)

        self.play(FadeOut(duplicates), Write(should_drop), run_time=2)
        drop_guard = caption("Drop only what is carried: the supplied drop(vase)\nwould otherwise create a vase from nothing.", footnote)
        self.play(FadeIn(drop_guard), Indicate(should_drop[2], scale_factor=1.3))
        self.wait(4)


def rows_aligned_at_iff(*rules: tuple[str, ...]) -> VGroup:
    rows = VGroup(*(MathTex(*terms, font_size=44) for terms in rules)).arrange(DOWN, buff=0.7)
    iff_x = rows[0][1].get_x()
    for row in rows:
        row.shift(RIGHT * (iff_x - row[1].get_x()))
    return rows.move_to([0, 0.4, 0])


def caption(text: str, footnote: Text) -> Text:
    return Text(text, font_size=26, line_spacing=0.9).next_to(footnote, UP, buff=0.35)
