from duplicate_agent import duplicate_detection
from root_cause_agent import root_cause
from remediation_agent import remediation

test_bugs = [

{
"description":"Application crashes while login"
},

{
"description":"Null pointer exception while payment"
},

{
"description":"Dashboard takes 30 seconds to load"
}

]

for bug in test_bugs:

    print("="*40)

    print("Input:",bug["description"])

    rc = root_cause(bug["description"])

    dup = duplicate_detection(bug["description"])

    fix = remediation(bug["description"])

    print("Root Cause")
    print(rc)

    print("Duplicate")
    print(dup)

    print("Recommendation")
    print(fix)