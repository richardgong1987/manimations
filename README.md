# manimations

Manim scenes, one file per scene under `src/manimations/`.

## Scenes

| File | Scene | Shows |
| --- | --- | --- |
| `at_definition.py` | `AtDefinition` | at(P) ⟺ ∃X,Y: pos(P,X,Y) ∧ pos(hero,X,Y) |

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
