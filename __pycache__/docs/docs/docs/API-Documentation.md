# API Documentation

## Intelligent Bug Diagnosis Platform with Fix Recommendation Assistance

This document describes the APIs used by the Intelligent Bug Diagnosis Platform.

> The endpoint names below represent the proposed API structure. Update the paths if the final implementation uses different routes.

---

# 1. Base URL

For local development:

```text
http://localhost:8000
```

---

# 2. API Architecture

```text
Frontend
   │
   ▼
FastAPI Backend
   │
   ├── Submission API
   ├── Triage API
   ├── Log Analysis API
   ├── RAG Retrieval API
   ├── Root Cause API
   ├── Duplicate Detection API
   ├── Remediation API
   └── Analytics API
```

---

# 3. Submit Bug Report

### Endpoint

```http
POST /api/bugs
```

### Description

Creates a new bug submission.

### Request

```json
{
  "title": "Application crashes during login",
  "description": "The application crashes when a user attempts to log in.",
  "stack_trace": "NullPointerException at LoginService.java:142",
  "component": "Authentication"
}
```

### Response

```json
{
  "bug_id": "BUG-0001",
  "status": "submitted",
  "message": "Bug submitted successfully"
}
```

---

# 4. Upload Bug File

### Endpoint

```http
POST /api/bugs/upload
```

### Description

Uploads a bug report, stack trace, or error-log file.

### Supported Formats

* TXT
* LOG
* JSON
* CSV
* PDF

### Response

```json
{
  "bug_id": "BUG-0002",
  "filename": "application-error.log",
  "status": "uploaded"
}
```

---

# 5. Get Bug Details

### Endpoint

```http
GET /api/bugs/{bug_id}
```

### Example

```http
GET /api/bugs/BUG-0001
```

### Response

```json
{
  "bug_id": "BUG-0001",
  "title": "Application crashes during login",
  "status": "analysis_completed"
}
```

---

# 6. Run Triage Analysis

### Endpoint

```http
POST /api/bugs/{bug_id}/triage
```

### Response

```json
{
  "severity": "High",
  "priority": "P1",
  "affected_component": "Authentication",
  "confidence": 0.91,
  "reasoning": "The defect prevents users from completing authentication."
}
```

---

# 7. Run Log Analysis

### Endpoint

```http
POST /api/bugs/{bug_id}/log-analysis
```

### Response

```json
{
  "exception_type": "NullPointerException",
  "error_message": "User object is null",
  "failure_point": "LoginService.java:142",
  "affected_code_path": "LoginController -> LoginService",
  "confidence": 0.94
}
```

---

# 8. Historical Defect Retrieval

### Endpoint

```http
POST /api/rag/search
```

### Request

```json
{
  "query": "NullPointerException during user login",
  "top_k": 5
}
```

### Response

```json
{
  "results": [
    {
      "defect_id": "BUG-1023",
      "project": "Apache",
      "similarity": 0.92,
      "summary": "Authentication service failed due to null user object.",
      "resolution": "Added null validation before authentication."
    }
  ]
}
```

---

# 9. Root Cause Analysis

### Endpoint

```http
POST /api/bugs/{bug_id}/root-cause
```

### Response

```json
{
  "root_cause": "Missing null validation in the authentication service.",
  "confidence": 0.89,
  "supporting_evidence": [
    "Historical defect BUG-1023",
    "NullPointerException at LoginService.java:142"
  ]
}
```

---

# 10. Duplicate Detection

### Endpoint

```http
POST /api/bugs/{bug_id}/duplicates
```

### Response

```json
{
  "matches": [
    {
      "defect_id": "BUG-1023",
      "similarity_score": 0.92,
      "summary": "Authentication failure caused by missing null validation."
    },
    {
      "defect_id": "BUG-0872",
      "similarity_score": 0.86,
      "summary": "Login service failed when user information was unavailable."
    }
  ]
}
```

---

# 11. Remediation Recommendation

### Endpoint

```http
POST /api/bugs/{bug_id}/remediation
```

### Response

```json
{
  "recommendation": "Add null validation before accessing the user authentication object.",
  "supporting_evidence": [
    "BUG-1023 historical resolution",
    "Root cause analysis"
  ],
  "confidence": 0.88
}
```

---

# 12. Complete Analysis

### Endpoint

```http
POST /api/bugs/{bug_id}/analyze
```

### Description

Runs the complete multi-agent pipeline.

### Pipeline

```text
Bug
 ↓
Triage
 ↓
Log Analysis
 ↓
RAG Retrieval
 ↓
Root Cause
 ↓
Duplicate Detection
 ↓
Remediation
 ↓
Structured Findings
```

### Response

```json
{
  "bug_id": "BUG-0001",
  "triage": {},
  "log_analysis": {},
  "root_cause": {},
  "duplicates": [],
  "remediation": {}
}
```

---

# 13. Analytics

### Endpoint

```http
GET /api/analytics/defects
```

### Response

```json
{
  "total_defects": 150,
  "high_severity": 32,
  "medium_severity": 78,
  "low_severity": 40,
  "top_components": [
    "Authentication",
    "Database",
    "API"
  ]
}
```

---

# 14. Knowledge Base Growth

### Endpoint

```http
POST /api/knowledge-base/add
```

### Description

Adds a verified and resolved defect to the knowledge base.

### Request

```json
{
  "bug_id": "BUG-0001",
  "resolution": "Added null validation in authentication service.",
  "verified": true
}
```

### Response

```json
{
  "status": "added",
  "message": "Resolved defect added to knowledge base."
}
```

---

# 15. HTTP Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Successful request    |
| 201  | Resource created      |
| 400  | Invalid request       |
| 404  | Resource not found    |
| 422  | Validation error      |
| 500  | Internal server error |

---

# 16. API Testing

The APIs can be tested using:

* Swagger UI
* Postman
* cURL
* Automated Pytest tests

Swagger UI:

```text
http://localhost:8000/docs
```

---

# 17. API Security

Production deployment should include:

* Authentication
* Authorization
* API rate limiting
* Input validation
* File-type validation
* Secure secret management
* HTTPS

---

# 18. API Completion Criteria

The API layer is considered complete when:

* Bug submission works.
* File upload works.
* Triage API works.
* Log analysis API works.
* RAG retrieval works.
* Root-cause API works.
* Duplicate detection works.
* Remediation API works.
* Complete analysis endpoint works.
* Analytics endpoint works.
* Knowledge-base growth endpoint works.
