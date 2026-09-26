import urllib.request
import urllib.parse
import json
import os
import time

def test_submission(test_name, data, expected_strings=[], expected_not_strings=[]):
    url = 'http://127.0.0.1:5000/submit'
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=encoded_data)
    try:
        start_t = time.perf_counter()
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            elapsed = time.perf_counter() - start_t
            
            # Print performance metric for M4 requirement
            print(f"[{test_name}] Elapsed time: {elapsed:.2f} seconds")
            
            for expected in expected_strings:
                if expected not in html:
                    print(f"[{test_name}] FAILED - Missing expected text: '{expected}'")
                    return False
            for not_expected in expected_not_strings:
                if not_expected in html:
                    print(f"[{test_name}] FAILED - Found unexpected text: '{not_expected}'")
                    return False
            
            print(f"[{test_name}] SUCCESS")
            return html
    except urllib.error.HTTPError as e:
        html = e.read().decode('utf-8')
        for expected in expected_strings:
            if expected in html:
                print(f"[{test_name}] SUCCESS (Expected Error Triggered)")
                return html
        print(f"[{test_name}] HTTP ERROR - {e.code}")
        return False
    except Exception as e:
        print(f"[{test_name}] ERROR - {e}")
        return False

# Unit tests for functions
from risk_engine import calculate_risk, get_risk_status, calculate_success_probability
from swot_analysis import generate_swot
from feasibility import calculate_feasibility
from recommendation_engine import generate_recommendations
from mitigation_engine import generate_mitigations
from langgraph_agent import run_langgraph_analysis

print("Running Unit Tests...")
# M1/M2 tests
score_high = calculate_risk("High", "Low", "Limited", "Low", "Limited")
assert score_high == 100, f"Expected 100, got {score_high}"

# M3 tests
m1_data_mock = {"budget": 5000}
m2_data_mock = {
    "market_competition": "High",
    "resource_availability": "Limited",
    "team_expertise": "Low",
    "feasibility_score": 40,
    "market_opportunity": 70
}

# 1. Recommendation generation & 3. Priority conditions
recs = generate_recommendations(m1_data_mock, m2_data_mock)
assert any(r["title"] == "Competitive Positioning" and r["priority"] == "High" for r in recs)

# 4. Mitigation generation & 5. Correct mapping
mits = generate_mitigations(m2_data_mock)
assert any(m["risk"] == "High Competition" and m["strategy"] == "Differentiation Strategy" for m in mits)

# 6. Gemini Fallback & 7. LangGraph graph construction & 8. LangGraph full execution
os.environ.pop("GEMINI_API_KEY", None)
project_data_mock = {"project_name": "Test"}
m3_state = run_langgraph_analysis(project_data_mock, m1_data_mock, m2_data_mock)
assert m3_state["is_llm_based"] is False
assert "Deterministic Fallback" in m3_state["strategic_reasoning"]
assert "VALID" in m3_state["validation_result"]

print("Unit Tests Passed!\n")

print("Running Integration Tests...")

# M4 Validation Test
test_submission(
    "TEST M4-1: Input Validation Rejection", 
    {
        'project_name': '',  # Empty name should fail validation
        'target_market': 'Teens globally',
        'budget': '5000'
    }, 
    expected_strings=["Validation Error: Project Name, Description, Target Market, and Objectives are required."]
)

# M4 Validation Test - Bad Number
test_submission(
    "TEST M4-2: Input Validation Numeric Rejection", 
    {
        'project_name': 'Valid',
        'project_description': 'Valid',
        'target_market': 'Valid',
        'objectives': 'Valid',
        'budget': 'not_a_number'
    }, 
    expected_strings=["Validation Error: Budget must be a valid numeric value."]
)

# M4 Complete E2E Integration
valid_payload = {
    'project_name': 'M4 Project',
    'project_description': 'Testing M4 Dashboard',
    'target_market': 'Teens globally',
    'budget': '5000',
    'competition': 'Big tech firms',
    'resources': '1 dev',
    'objectives': 'Launch Q3',
    'rm_competition': 'High',
    'rm_team': 'Low',
    'rm_resources': 'Limited',
    'rm_innovation': 'Low',
    'rm_research': 'Limited',
    'f_market': '80',
    'f_team': '30',
    'f_comp': '20',
    'f_res': '20'
}

html_result = test_submission(
    "TEST M4-3: Complete Workflow (M1->M4) & Dashboard Output", 
    valid_payload,
    expected_strings=[
        "Project Intelligence Report", 
        "100", 
        "Data Ingestion",
        "Download Final Report"
    ],
    expected_not_strings=[
        "Internal Server Error",
        "Traceback"
    ]
)

if html_result:
    import re
    # Extract project ID from the download link to test report generation
    match = re.search(r'/download_report/(\d+)', html_result)
    if match:
        pid = match.group(1)
        url = f'http://127.0.0.1:5000/download_report/{pid}'
        req = urllib.request.Request(url)
        try:
            with urllib.request.urlopen(req) as response:
                report = response.read().decode('utf-8')
                if "Failure Prediction AI - Assessment Report" in report and "M4 Project" in report:
                    print("[TEST M4-4: Report Download] SUCCESS")
                else:
                    print("[TEST M4-4: Report Download] FAILED - Unexpected report content")
        except Exception as e:
            print(f"[TEST M4-4: Report Download] ERROR - {e}")
    else:
        print("[TEST M4-4: Report Download] FAILED - Could not find project ID in HTML")

