# manimations

Manim scenes, one file per scene under `src/manimations/`.

## Scenes

| File | Scene | Shows |
| --- | --- | --- |
| `at_definition.py` | `AtDefinition` | at(P) ⟺ ∃X,Y: pos(P,X,Y) ∧ pos(hero,X,Y) |
| `item_rules.py` | `ItemRules` | needed, should_pick and should_drop; why duplicates are ignored |
| `cell_indexing.py` | `CellIndexing` | cell(N,X,Y): X = N mod 8, Y = ⌊N/8⌋, the row-order sweep and row wrap |
| `search_bound.py` | `SearchBound` | moves ≤ 64 × 24 + 64 = 1600, so a missing item cannot cause an endless search |
| `outcome_report.py` | `OutcomeReport` | complete, absence_proven and the three terminal messages |

The Forest project's `docs/VIDEO_SCRIPT.md` says when each clip is shown in the
demonstration video.

## Rendering

```sh
uv sync                                                           # first time only
uv run manim -pql src/manimations/at_definition.py AtDefinition   # quick 480p preview
uv run manim -pqh src/manimations/at_definition.py AtDefinition   # final 1080p60
uv run manim -s -qh src/manimations/at_definition.py AtDefinition # last frame as PNG
```

`-p` opens the result when rendering finishes. Output goes to
`media/videos/<file>/<quality>/<Scene>.mp4` (images to `media/images/<file>/`).
Rendering needs a LaTeX install (`latex` and `dvisvgm` on `PATH`).
