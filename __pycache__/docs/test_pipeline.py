import json
import requests


BACKEND_URL = "http://127.0.0.1:8000/analyze"


TEST_CASES = [

    {
        "id": "TC01",
        "name": "Java Null Pointer",
        "text": """
java.lang.NullPointerException: Cannot invoke method
at com.example.UserService.getUser(UserService.java:42)
at com.example.Controller.handle(Controller.java:88)
"""
    },

    {
        "id": "TC02",
        "name": "Database Failure",
        "text": """
ERROR: SQLException
Database connection failed
SELECT * FROM users
Connection to database refused
"""
    },

    {
        "id": "TC03",
        "name": "Python Key Error",
        "text": """
Traceback (most recent call last):
  File "app.py", line 25, in process_user
    value = user["email"]
KeyError: 'email'
"""
    },

    {
        "id": "TC04",
        "name": "Network Timeout",
        "text": """
ERROR SocketTimeoutException
Request to payment service timed out
at com.example.PaymentClient.call(PaymentClient.java:105)
"""
    },

    {
        "id": "TC05",
        "name": "Memory Failure",
        "text": """
java.lang.OutOfMemoryError: Java heap space
at com.example.ReportService.generate(ReportService.java:210)
"""
    }
]


def test_case(test):

    try:

        response = requests.post(
            BACKEND_URL,
            files={
                "file": (
                    "test_bug.txt",
                    test["text"].encode("utf-8"),
                    "text/plain"
                )
            },
            timeout=120
        )

        if response.status_code != 200:

            return {
                "id": test["id"],
                "name": test["name"],
                "status": "FAIL",
                "reason": (
                    f"HTTP {response.status_code}"
                )
            }

        result = response.json()

        required = [
            "triage",
            "log_analysis",
            "root_cause",
            "duplicates",
            "remediation",
            "similar_bugs"
        ]

        missing = [
            key
            for key in required
            if key not in result
        ]

        if missing:

            return {
                "id": test["id"],
                "name": test["name"],
                "status": "FAIL",
                "reason": (
                    "Missing fields: "
                    + ", ".join(missing)
                )
            }

        log = result.get(
            "log_analysis",
            {}
        )

        remediation = result.get(
            "remediation",
            {}
        )

        checks = {
            "pipeline_complete": True,

            "exception_detected":
                log.get(
                    "exception",
                    "Not Found"
                ) != "Not Found",

            "failure_point_available":
                log.get(
                    "failure_point",
                    "Not Found"
                ) != "Not Found",

            "root_cause_available":
                bool(
                    result.get(
                        "root_cause"
                    )
                ),

            "remediation_available":
                bool(
                    remediation.get(
                        "recommended_fix"
                    )
                )
        }

        passed_checks = sum(
            1
            for value in checks.values()
            if value
        )

        check_accuracy = (
            passed_checks
            / len(checks)
            * 100
        )

        return {
            "id": test["id"],
            "name": test["name"],
            "status": (
                "PASS"
                if check_accuracy >= 80
                else "PARTIAL"
            ),
            "check_accuracy": round(
                check_accuracy,
                2
            ),
            "checks": checks,
            "duplicate_count":
                len(
                    result.get(
                        "duplicates",
                        []
                    )
                ),
            "similar_bug_count":
                len(
                    result.get(
                        "similar_bugs",
                        []
                    )
                )
        }

    except Exception as e:

        return {
            "id": test["id"],
            "name": test["name"],
            "status": "FAIL",
            "reason": str(e)
        }


def main():

    print(
        "\n======================================"
    )

    print(
        "Milestone 4 End-to-End Testing"
    )

    print(
        "======================================\n"
    )

    results = []

    for test in TEST_CASES:

        print(
            f"Running {test['id']} - "
            f"{test['name']}"
        )

        result = test_case(test)

        results.append(
            result
        )

        print(
            result["status"]
        )

    passed = sum(
        1
        for r in results
        if r["status"] == "PASS"
    )

    total = len(results)

    overall = (
        passed
        / total
        * 100
    )

    report = {
        "total_test_cases": total,
        "passed": passed,
        "failed_or_partial":
            total - passed,
        "overall_pass_rate":
            round(
                overall,
                2
            ),
        "results": results
    }

    with open(
        "test_results.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4
        )

    print(
        "\n======================================"
    )

    print(
        f"Overall Pass Rate: {overall:.2f}%"
    )

    print(
        "Report saved to test_results.json"
    )

    print(
        "======================================"
    )


if __name__ == "__main__":
    main()