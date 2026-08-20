def find_duplicates(text, retrieved=None):

    duplicates = []

    if not retrieved:
        return duplicates

    for bug in retrieved:

        similarity = bug.get("similarity", 0)

        if similarity >= 40:

            duplicates.append({

                "bug_id": bug["Bug_ID"],

                "title": bug["Title"],

                "summary": bug.get(
                    "Historical_Summary",
                    bug["Title"]
                ),

                "similarity": similarity,

                "root_cause": bug["Root_Cause"],

                "resolution": bug["Suggested_Fix"],

                "suggested_fix": bug["Suggested_Fix"]

            })

    return duplicates