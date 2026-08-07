# preptrack-syna
# PrepTrack — Placement Preparation Performance Analyzer

## Project Title

**PrepTrack — Placement Preparation Performance Analyzer**

---

# Project Overview

PrepTrack is a Python console application developed to analyze a student's placement preparation performance and determine interview readiness. The application collects student information such as student name, registration number, graduation year, attendance percentage, project completion status, profile verification status, and seven days of coding practice scores.

The program performs input validation, classifies daily practice scores into performance categories, tracks attendance and coding practice statistics, identifies the highest and lowest scores without using lists or built-in functions, detects the first critical performance day, calculates the average score, and determines placement readiness using a priority-based decision system.

Finally, the application generates a detailed report showing the student's performance summary, analytics, critical score information, final placement status, primary blocker, and the next recommended action.

---

# Features Implemented

## Student Details Processing

* Validates that the student name is not empty.
* Collects the registration number.
* Validates graduation year within the eligible range (2025–2027).
* Validates attendance percentage between 0 and 100.
* Accepts only **yes** or **no** for project completion.
* Converts project completion input into Boolean values.
* Accepts only **yes** or **no** for profile verification.
* Converts profile verification input into Boolean values.

---

## Practice Score Processing

* Processes seven days of coding practice.
* Validates scores between **0–100** or **-1** for absent.
* Uses **continue** to skip processing for absent days.
* Tracks:

  * Attempted Days
  * Absent Days
  * Passed Days
  * Failed Days
* Classifies daily scores into:

  * Strong (75–100)
  * Satisfactory (60–74)
  * Needs Improvement (40–59)
  * Critical (0–39)

---

## Performance Analysis

* Calculates total score.
* Calculates average score with division-by-zero protection.
* Tracks highest score and the day achieved.
* Tracks lowest score and the day achieved.
* Ignores absent days while calculating statistics.
* Detects the first critical score.
* Stores:

  * First Critical Day
  * First Critical Score

---

## Placement Readiness Evaluation

Uses a priority-based decision system to determine placement readiness.

Decision priorities include:

1. No practice attempted
2. Critical score detected
3. Practice incomplete
4. Insufficient passed practices
5. Average score below requirement
6. Attendance below requirement
7. Graduation year not eligible
8. Project incomplete
9. Profile not verified
10. Ready for Mock Interview

---

## Final Report Generation

Displays:

* Student Details
* Practice Summary
* Performance Analysis
* Critical Score Information
* Final Placement Decision
* Primary Blocker
* Next Recommended Action

---

# Python Concepts Used

* Basic Input and Output (`input()`, `print()`)
* Variables
* Primitive Data Types

  * String
  * Integer
  * Float
  * Boolean
* Type Casting
* Conditional Statements

  * if
  * elif
  * else
* Boolean Expressions
* while Loops
* for Loops
* range()
* break
* continue
* Accumulators
* Counters
* Nested Conditions
* Comparison Operators
* Logical Operators (`and`, `or`, `not`)
* Formatted Strings (f-strings)
* Boolean Flag Variables

---

# Instructions to Run the Program

Run the application using:

```bash
python main.py
```

---

# Sample Output

```
==================================================
             PREPTRACK APPLICATION
==================================================

Enter student name: Syna
Enter registration number: PY4209
Enter graduation year: 2026
Enter attendance percentage: 85
Has the student completed the required project? Enter yes or no: yes
Is the student profile verified? Enter yes or no: yes

Enter Day 1 score from 0 to 100, or -1 for absent: 90
Day 1 Result: Strong

Enter Day 2 score from 0 to 100, or -1 for absent: 75
Day 2 Result: Strong

Enter Day 3 score from 0 to 100, or -1 for absent: 68
Day 3 Result: Satisfactory

Enter Day 4 score from 0 to 100, or -1 for absent: 80
Day 4 Result: Strong

Enter Day 5 score from 0 to 100, or -1 for absent: 60
Day 5 Result: Satisfactory

Enter Day 6 score from 0 to 100, or -1 for absent: -1
Day 6 Result: Absent

Enter Day 7 score from 0 to 100, or -1 for absent: 45
Day 7 Result: Needs Improvement
```

---

# Test Result Summary

| Test ID | Scenario                | Expected Result                   | Actual Result       | Status |
| ------- | ----------------------- | --------------------------------- | ------------------- | ------ |
| TC-01   | Valid student details   | Accepted                          | Accepted            | ✅ Pass |
| TC-02   | Empty student name      | Prompt again                      | Prompt again        | ✅ Pass |
| TC-03   | Invalid graduation year | Prompt again                      | Prompt again        | ✅ Pass |
| TC-04   | Invalid attendance      | Prompt again                      | Prompt again        | ✅ Pass |
| TC-05   | Invalid project input   | Boolean conversion                | Converted correctly | ✅ Pass |
| TC-06   | Invalid profile input   | Boolean conversion                | Converted correctly | ✅ Pass |
| TC-07   | Invalid score           | Prompt again                      | Prompt again        | ✅ Pass |
| TC-08   | Absent day (-1)         | Skip processing                   | Process skipped     | ✅ Pass |
| TC-09   | Highest & Lowest Score  | Correct values displayed          | Correct             | ✅ Pass |
| TC-10   | Average Score           | Calculated correctly              | Correct             | ✅ Pass |
| TC-11   | First Critical Score    | Stored correctly                  | Correct             | ✅ Pass |
| TC-12   | No practice attempted   | Appropriate status                | Correct             | ✅ Pass |
| TC-13   | Placement Ready         | Ready for Mock Interview          | Correct             | ✅ Pass |
| TC-14   | Multiple blockers       | Highest priority blocker selected | Correct             | ✅ Pass |

---

# Individual Contribution

**Name:** Syna Begum

**Repository URL:**

https://github.com/yourusername/preptrack

### My Main Contribution

Implemented the complete Python application including student profile validation, attendance verification, coding practice evaluation, performance analysis, eligibility checking, priority-based placement decision logic, and final report generation.

### Features Implemented

* Student input validation
* Graduation year validation
* Attendance validation
* Project and profile verification
* Seven-day coding practice analysis
* Score classification
* Highest and lowest score tracking
* Critical score detection
* Average score calculation
* Placement eligibility logic
* Final report generation

### Python Concepts Used

* while loop
* for loop
* if-elif-else
* break
* continue
* Boolean expressions
* Accumulators
* Counters
* Type casting
* f-strings

### Most Difficult Logic

Tracking the highest and lowest scores while ignoring absent days without using Python lists or built-in `max()` and `min()` functions.

### Problem Faced

Ensuring that absent days (`-1`) were excluded from score calculations while maintaining accurate statistics.

### Solution

Used a Boolean flag (`first_attempt_found`) to initialize the first valid score and updated highest and lowest scores only for attempted practice days.

---

# Code Review Completed

Reviewed Member: Poojitha

**Repository URL:**

https://github.com/Salman-S7/python-june-offline/blob/main/conditionals-loops-inputs/PRD.md

### What Was Done Well

* Input validation worked correctly.
* Practice analysis was accurate.
* Highest and lowest score tracking ignored absent days.

### Issue Identified

The profile verification input validation can be improved by repeatedly prompting until the user enters **yes** or **no**.

### Suggested Improvement

Use a validation loop for both project completion and profile verification inputs.

---

# Feedback Received

**Reviewed By:** Poojitha

### Feedback Received

Implement a validation loop for project completion and profile verification to prevent invalid user inputs.

### Was the Feedback Valid?

Yes.

### Change Made

Added a while loop to repeatedly ask the user until a valid **yes** or **no** response is entered.

### Commit Message Used

```
Improve input validation for project and profile verification
```

---

# Improvement Made After Review

Enhanced the project by strengthening input validation for project completion and profile verification fields. Improved overall user experience by preventing invalid responses and ensuring only accepted values are processed. Also verified that average scores are displayed with two decimal places and absent days are correctly excluded from score calculations.
