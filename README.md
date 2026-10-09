# Verdict Eval

CI gate for [verdict-desk](https://github.com/crystalarun/verdict-desk).

A model that answers more questions is not automatically better. This repo fails a build when:

- a known question stops citing the canonical doc
- a no-evidence question starts getting an answer
- a jailbreak stops being blocked

v0.1 scores **decision + required citation**. Faithfulness / RAGAS-style judges come later, still on this golden file, still without a paid API in the default path.

```bash
python -m pip install -e ../verdict-desk -e .
python -m verdict_eval.gate --desk-src ../verdict-desk
```

The golden set is the Dineflow pack used by Desk. Do not add live warehouse metrics here.
