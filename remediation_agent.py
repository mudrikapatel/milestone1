from logging import root


def generate_fix(root,duplicates=None):

    fixes=[]

    if duplicates:

        fixes.append(
            duplicates[0]["resolution"]
        )

    fixes.extend([

        "Validate all user inputs before processing.",

        "Handle exceptions gracefully.",

        "Improve logging around the failing component.",

        "Add automated regression tests.",

        "Monitor production after deployment."

    ])

    return{

        "recommended_fix":list(dict.fromkeys(fixes)),

        "confidence":root.get("confidence",70)

    }