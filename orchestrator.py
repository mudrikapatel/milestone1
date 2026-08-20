



from bug_parser import parse_file
from triage_agent import analyze_triage
from log_analysis_agent import analyze_log

from rag.retrieval import BugRetriever
from rag.reranker import BugReranker
from similarity import find_similar_bugs
from root_cause_agent import analyze_root_cause
from duplicate_agent import find_duplicates
from remediation_agent import generate_fix
retriever = BugRetriever()
reranker = BugReranker()


def analyze_bug(filepath):

    print("Step 1: Parsing file")
    text = parse_file(filepath)

    print("Step 2: Running Triage Agent")
    triage = analyze_triage(text)

    print("Step 3: Running Log Analysis Agent")
    log = analyze_log(text)

    print("Step 4: Running RAG Retrieval")

    try:
        retrieved = retriever.search(text, top_k=3)
    except Exception as e:
        print("RAG ERROR:", e)
        retrieved = []

    print("Step 5: Reranking")

    try:
        similar = reranker.rerank(retrieved)

        if not similar:
            similar = retrieved

    except Exception as e:
        print("RERANK ERROR:", e)
        similar = retrieved

    print("===== SIMILAR BUGS =====")
    print(similar)

    print("Step 6: Root Cause")

    try:

        root = analyze_root_cause(
            text,
            similar
        )

    except Exception as e:

        print("ROOT CAUSE ERROR:", e)

        root = {
            "cause": "Unable to determine root cause",
            "confidence": 50,
            "evidence": "Root cause agent failed.",
            "reasoning": str(e),
            "recommendation": "Investigate manually."
        }

    print(root)

    print("Step 7: Duplicate Detection")

    try:

        duplicates = find_duplicates(
            text,
            similar
        )

    except Exception as e:

        print("DUPLICATE ERROR:", e)

        duplicates = []

    print(duplicates)

    print("Step 8: Remediation")

    try:

        remediation = generate_fix(
            root,
            duplicates
        )

    except Exception as e:

        print("FIX ERROR:", e)

        remediation = {
            "recommended_fix": [
                "Review logs and debug failing module."
            ],
            "confidence": 50
        }

    print(remediation)

    return {

        "triage": triage,

        "log_analysis": log,

        "root_cause": root,

        "duplicates": duplicates,

        "remediation": remediation,

        "similar_bugs": similar

    }