from manim import BLUE, GREEN, YELLOW, Indicate, MathTex, Scene, VGroup, Write

AT_DEFINITION_TEX = (
    r"\operatorname{at}(P) \iff \exists X, Y:"
    r" \operatorname{pos}(P, X, Y) \land \operatorname{pos}(\text{hero}, X, Y)"
)

# Colouring the variables makes the join visible: the same X and Y must
# appear in both pos/3 facts, so P and the hero share one cell.
VARIABLE_COLORS = {"P": YELLOW, "X": BLUE, "Y": GREEN}


class AtDefinition(Scene):
    def construct(self):
        formula = MathTex(AT_DEFINITION_TEX, tex_to_color_map=VARIABLE_COLORS)
        self.play(Write(formula), run_time=3)
        self.wait()

        self.play(Indicate(occurrences_of(formula, "X", "Y")))
        self.wait(2)


def occurrences_of(formula: MathTex, *texs: str) -> VGroup:
    # get_part_by_tex returns only the first match; we need every occurrence.
    return VGroup(
        *(
            formula.id_to_vgroup_dict[match_id]
            for tex, match_id in formula.matched_strings_and_ids
            if tex in texs
        )
    )
