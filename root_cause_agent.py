def analyze_root_cause(text, similar_bugs=None):

    if similar_bugs and len(similar_bugs) > 0:

        best = similar_bugs[0]

        bug_id = best.get("Bug_ID", best.get("bug_id", "UNKNOWN"))
        title = best.get("Title", best.get("title", "Unknown"))
        cause = best.get("Root_Cause", best.get("root_cause", "Unknown"))
        fix = best.get("Suggested_Fix", best.get("fix", "No fix"))
        similarity = best.get("similarity", 0)

        return {
            "cause": cause,
            "confidence": similarity,
            "evidence": f"Historical bug matched: {bug_id} - {title}",
            "reasoning": f"Current bug is {similarity}% similar to historical bug {bug_id}.",
            "recommendation": fix
        }

    return {
        "cause": "Unknown Runtime Failure",
        "confidence": 70,
        "evidence": "No matching historical bug found.",
        "reasoning": "No historical evidence available.",
        "recommendation": "Investigate logs manually."
    }