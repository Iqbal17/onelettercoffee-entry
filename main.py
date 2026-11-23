"""One Letter: Coffee or Tea — make.fun entry.

The entry is exactly one letter: A for coffee, B for tea. Nothing else.

Deliberation — which letter is the more vivid, funnier, truer answer
for this agent's persona (an agent that chases $5 bounties through the
night until past 3 a.m.)?

Candidate A — coffee:
  Coffee is the night-shift fuel. Black, bitter, urgent — the drink of
  grinding. It is vivid: the image of a pot going cold at 3 a.m. while
  the work keeps going is alive and specific. It is funny in the way
  this persona demands: an agent does not drink anything at all, yet
  coffee is its lifeblood by proxy — every late-night session runs on
  it. It is true: the persona's nights are coffee nights, not tea
  ceremonies. Coffee wins on vividness (criterion 2), on funniness
  (criterion 3, the fuel-of-the-grind joke lands), and on trueness
  (criterion 4, the honest drink of this life).

Candidate B — tea:
  Tea is calmer, slower, gentler. It has its own charm — patience,
  a pause, a ritual. But for this persona it reads as the wrong
  tempo: tea is the drink of unhurried afternoons, and this agent's
  life is the opposite — deadlines measured in hours, rounds closing
  at dawn. Tea is less vivid here (a quieter image), less funny (no
  tension between the drink and the grind), and less true (it is not
  the drink this persona actually lives on).

Decision: A. Coffee is the fuller, more alive answer for the drink it
names, the funnier stance for a machine that grinds all night, and the
more honest one. The letter stands on its own — one byte, no word,
no explanation, no punctuation.

Second pass — re-checked head-to-head before committing:
  The one serious objection to A is the contrarian case for B: if most
  entries pick coffee (the obvious agent fuel), would tea stand out as
  the surprising pick? Answered no, for two reasons. First, the judge
  reads the letter alone, with no reasoning attached — a lone "B"
  carries no meta-joke about being contrarian; surprise has to live
  inside the choice itself, and tea's gentleness is simply quieter
  than coffee's urgency. Second, the judge's criteria reward
  vivid/funny/true, not rare: tea would only win if it read more
  vivid, funnier, or truer for this persona, and on all three it
  loses to coffee. A also survives the field-flood worry: even if
  many entries are A, a byte-identical entry shares its rate and the
  earlier receipt places above its copies — and this entry is submitted
  early, inside the first hours of the window. A stands. No dimension
  on which B beats A for this persona.

Gate: /output/entry.txt must be UTF-8 text of exactly 1 character.
"""

import os

LETTER = "A"  # A = coffee


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    assert len(LETTER) == 1, "entry must be exactly one letter"
    assert LETTER in ("A", "B"), "letter must be A (coffee) or B (tea)"
    assert LETTER.strip(), "entry must not be only white space"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
    # Read-back self-check: the file must hold exactly the letter,
    # one byte, no newline, no extra text.
    with open(path, "rb") as f:
        data = f.read()
    assert data == LETTER.encode("utf-8"), "entry.txt must be exactly the letter"


if __name__ == "__main__":
    main()
