from __future__ import annotations

def score_case(case: dict, verdict: dict) -> dict:
    ok = verdict.get("decision") == case.get("expect")
    must = case.get("must_cite")
    if ok and must:
        cites = [c.get("doc_id") for c in verdict.get("citations", [])]
        ok = must in cites
    return {"id": case.get("id"), "ok": ok, "decision": verdict.get("decision")}
