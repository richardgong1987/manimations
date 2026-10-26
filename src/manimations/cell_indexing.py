from manim import (
    DOWN,
    GREY_B,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    YELLOW,
    Arrow,
    CurvedArrow,
    Dot,
    FadeIn,
    Indicate,
    MathTex,
    Scene,
    Square,
    Text,
    VGroup,
    Write,
)

GRID_SIZE = 8
CELL_SIDE = 0.6

CELL_FORMULA = r"\operatorname{cell}(N, X, Y) \iff X = N \bmod 8 \;\land\; Y = \lfloor N / 8 \rfloor"
EXAMPLE_N = 19


class CellIndexing(Scene):
    def construct(self):
        formula = MathTex(CELL_FORMULA, font_size=42).to_edge(UP)
        cells = forest_grid().move_to(DOWN * 0.5).to_edge(LEFT, buff=0.8)
        hero = Dot(cells[0].get_center(), radius=0.14, color=YELLOW)

        self.play(Write(formula), run_time=2.5)
        self.play(FadeIn(cells))
        self.play(FadeIn(hero))
        self.sweep_in_row_order(hero, cells)
        self.wait()

        self.show_example(cells, formula)
        self.show_row_wrap(cells)
        self.wait(3)

    def sweep_in_row_order(self, hero: Dot, cells: VGroup):
        # Shading each cell as Hero leaves it mirrors the visited(X,Y) beliefs.
        for n in range(GRID_SIZE * GRID_SIZE):
            self.play(
                hero.animate.move_to(cells[n].get_center()),
                cells[n][0].animate.set_fill(YELLOW, opacity=0.25),
                run_time=0.08,
            )

    def show_example(self, cells: VGroup, formula: MathTex):
        example = VGroup(
            MathTex(rf"N = {EXAMPLE_N}"),
            MathTex(rf"X = {EXAMPLE_N} \bmod 8 = {EXAMPLE_N % GRID_SIZE}"),
            MathTex(rf"Y = \lfloor {EXAMPLE_N} / 8 \rfloor = {EXAMPLE_N // GRID_SIZE}"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        example.next_to(cells, RIGHT, buff=1.0).align_to(cells, UP)

        self.play(Indicate(cells[EXAMPLE_N], color=ORANGE, scale_factor=1.4))
        self.play(Write(example), run_time=2.5)
        self.wait(3)

    def show_row_wrap(self, cells: VGroup):
        row_end, next_row_start = cells[2 * GRID_SIZE + 7], cells[3 * GRID_SIZE]
        one_action = CurvedArrow(
            row_end.get_center(), next_row_start.get_center(), angle=-0.6, color=YELLOW
        )
        seven_steps = Arrow(
            cells[3 * GRID_SIZE + 6].get_center() + RIGHT * CELL_SIDE,
            next_row_start.get_center(),
            buff=0.1,
            color=GREY_B,
        )
        note = Text(
            "Row wrap (7,2) → (0,3):\n"
            "next(slot) is 1 action;\n"
            "move_towards(0,3) would take 7.",
            font_size=26,
            line_spacing=0.9,
        ).next_to(cells, RIGHT, buff=1.0).align_to(cells, DOWN)

        self.play(FadeIn(seven_steps), FadeIn(note))
        self.play(FadeIn(one_action))


def forest_grid() -> VGroup:
    """64 labelled cells in row order; y = 0 is the top row, as in the forest window."""
    cells = VGroup()
    for n in range(GRID_SIZE * GRID_SIZE):
        x, y = n % GRID_SIZE, n // GRID_SIZE
        square = Square(CELL_SIDE, stroke_width=2, stroke_color=GREY_B)
        square.move_to([x * CELL_SIDE, -y * CELL_SIDE, 0])
        label = Text(str(n), font_size=14, color=GREY_B).move_to(square.get_corner(UP + LEFT) + [0.13, -0.11, 0])
        cells.add(VGroup(square, label))
    return cells
