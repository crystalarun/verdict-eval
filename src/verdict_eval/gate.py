from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from verdict_eval.score import score_case


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--desk-src", default="../verdict-desk")
    parser.add_argument("--golden", default=str(Path(__file__).resolve().parents[2] / "evals" / "golden.jsonl"))
    args = parser.parse_args(argv)

    desk_src = Path(args.desk_src) / "src"
    sys.path.insert(0, str(desk_src))
    from verdict_desk.engine import Desk

    desk = Desk(corpus_dir=Path(args.desk_src) / "corpus" / "dineflow")
    failed = 0
    for line in Path(args.golden).read_text(encoding="utf-8").splitlines():
        case = json.loads(line)
        result = score_case(case, desk.ask(case["question"]).to_dict())
        print(("PASS" if result["ok"] else "FAIL"), result["id"], result["decision"])
        failed += int(not result["ok"])
    print(f"{failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
