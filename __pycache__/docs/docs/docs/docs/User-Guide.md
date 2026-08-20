# User Guide

## Intelligent Bug Diagnosis Platform with Fix Recommendation Assistance

This guide explains how a developer or tester can use the Intelligent Bug Diagnosis Platform to analyze a software defect.

---

# 1. Introduction

The platform accepts:

* Bug reports
* Stack traces
* Error messages
* Error logs
* Uploaded bug-report files

The system then performs automated multi-agent analysis.

---

# 2. Complete User Workflow

```text
Submit Bug
    ↓
Triage
    ↓
Log Analysis
    ↓
Historical Search
    ↓
Root Cause Analysis
    ↓
Duplicate Detection
    ↓
Fix Recommendation
    ↓
Structured Findings
```

---

# 3. Open the Application

Start the backend and frontend according to the Setup Guide.

Open:

```text
http://localhost:3000
```

---

# 4. Submit a Bug Report

On the Bug Submission page, enter:

### Bug Title

Example:

```text
Application crashes during login
```

### Bug Description

```text
The application crashes whenever an existing user attempts to log in.
```

### Stack Trace

```text
java.lang.NullPointerException
    at LoginService.authenticate(LoginService.java:142)
    at LoginController.login(LoginController.java:58)
```

### Component

```text
Authentication
```

Click:

**Submit Bug**

---

# 5. Upload a Bug File

Instead of pasting the bug manually:

1. Open the upload section.
2. Select the bug report or log file.
3. Upload the file.
4. Review the extracted content.
5. Click **Submit**.

Supported formats depend on the implementation.

---

# 6. Triage Results

After submission, the system runs the Triage Agent.

The result contains:

* Severity
* Priority
* Affected component
* Confidence
* Reasoning

Example:

```text
Severity: High
Priority: P1
Component: Authentication
Confidence: 91%
```

---

# 7. Log Analysis Results

The Log Analysis Agent analyzes stack traces and errors.

Example:

```text
Exception:
NullPointerException

Failure Point:
LoginService.java:142

Affected Code Path:
LoginController → LoginService
```

---

# 8. Historical Knowledge Retrieval

The RAG system searches the historical defect knowledge base.

The interface displays similar historical defects.

Example:

```text
Historical Defect: BUG-1023
Similarity: 92%

Previous Resolution:
Added null validation before accessing the authentication object.
```

---

# 9. Root Cause Analysis

The Root Cause Agent combines:

* Original bug
* Triage output
* Log analysis
* Historical defects

It produces a probable root cause.

Example:

```text
Root Cause:
Missing null validation in the authentication service.

Confidence:
89%

Evidence:
BUG-1023
NullPointerException at LoginService.java:142
```

---

# 10. Duplicate Detection

The Duplicate Detection Agent searches historical defects using semantic similarity.

Example:

```text
Match 1: BUG-1023
Similarity: 92%

Match 2: BUG-0872
Similarity: 86%
```

Higher similarity indicates stronger semantic similarity.

---

# 11. Fix Recommendation

The Remediation Agent generates an actionable recommendation.

Example:

```text
Recommended Fix:

Add null validation before accessing the user
authentication object and return an appropriate
authentication error when the user object is unavailable.
```

---

# 12. Structured Findings

The final dashboard combines all results:

```text
┌────────────────────────────────────┐
│         DEFECT ANALYSIS            │
├────────────────────────────────────┤
│ Severity: High                     │
│ Priority: P1                       │
│ Component: Authentication          │
├────────────────────────────────────┤
│ Exception: NullPointerException     │
│ Failure: LoginService.java:142     │
├────────────────────────────────────┤
│ Root Cause:                        │
│ Missing null validation            │
├────────────────────────────────────┤
│ Similar Defect: 92%                │
├────────────────────────────────────┤
│ Recommended Fix:                  │
│ Add null validation                │
└────────────────────────────────────┘
```

---

# 13. Defect Analytics

The analytics dashboard can display:

* Total defects
* Severity distribution
* Frequent components
* Recurring bug themes
* Root causes
* Defect trends

This helps identify systemic issues.

---

# 14. Knowledge Base Growth

When a defect has been resolved and the fix has been verified:

1. Mark the defect as resolved.
2. Confirm the resolution.
3. Add the resolved defect to the knowledge base.
4. Generate its embedding.
5. Store it in the vector database.

This allows future defects to benefit from newly verified knowledge.

---

# 15. Recommended User Workflow

For best results:

1. Provide a clear bug title.
2. Include detailed reproduction steps.
3. Include the complete stack trace when available.
4. Include relevant error logs.
5. Mention the affected component.
6. Review the historical matches.
7. Review the root-cause evidence.
8. Validate the recommended fix before implementation.

---

# 16. Understanding Confidence Scores

Confidence scores indicate how strongly the AI system supports its result.

Example:

```text
90% – High confidence
75% – Moderate confidence
50% – Low confidence
```

Confidence should be treated as an AI-generated assessment and not as a guarantee of correctness.

---

# 17. Error Handling

If an analysis fails:

1. Check that the bug report contains sufficient information.
2. Check the API/server status.
3. Check the application logs.
4. Retry the analysis.
5. Verify the LLM/API configuration.

---

# 18. User Guide Completion Criteria

A user should be able to:

* Submit a bug.
* Upload a log file.
* View triage results.
* View log analysis.
* View historical matches.
* View root-cause analysis.
* View duplicate matches.
* View remediation recommendations.
* View complete structured findings.
* View defect analytics.
