# preptrack-pujitha
# PrepTrack — Placement Preparation Performance Analyzer

## Project Title

**PrepTrack — Placement Preparation Performance Analyzer**

---

# Project Overview

prepTrack is a Python-based console application developed to evaluate a student's placement preparation and determine their readiness for a placement mock interview. The application collects validated student information, including the student name, registration number, graduation year, attendance percentage, project completion status, profile verification status, and seven daily coding-practice scores. It validates every user input before processing and analyzes the student's performance using predefined evaluation criteria.

The application classifies daily coding-practice scores into Strong, Satisfactory, Needs Improvement, and Critical categories while tracking important performance metrics such as attempted days, absent days, passed days, failed days, highest score, lowest score, average score, and the first critical score. Based on these results, it evaluates placement eligibility using attendance, graduation year, coding performance, project completion, and profile verification. Finally, the program generates a comprehensive PREPTRACK REPORT containing the Student Profile, Practice Summary, Performance Analysis, Critical Score Information, and Final Decision. The project is implemented entirely using core Python programming concepts without using lists, tuples, or built-in aggregation functions.



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
Enter student name: Bijjam Pujitha
Enter registration number: 8777
Enter graduation year: 2026
Enter attendance percentage: 90
Attendance accepted.
Has the student completed the required project?
Enter yes or no: yes
Is the student profile verified?
Enter yes or no: yes
Enter Day 1 score from 0 to 100, or -1 for absent: 90
Score accepted.
Day 1 Result: Strong
Enter Day 2 score from 0 to 100, or -1 for absent: 80
Score accepted.
Day 2 Result: Strong
Enter Day 3 score from 0 to 100, or -1 for absent: 85
Score accepted.
Day 3 Result: Strong
Enter Day 4 score from 0 to 100, or -1 for absent: 75
Score accepted.
Day 4 Result: Strong
Enter Day 5 score from 0 to 100, or -1 for absent: 50
Score accepted.
Day 5 Result: Needs Improvement  
Enter Day 6 score from 0 to 100, or -1 for absent: -1
Score accepted.
Day 6 Result: Absent
Enter Day 7 score from 0 to 100, or -1 for absent: 40
Score accepted.
Day 7 Result: Needs Improvement  

==================================================
              PREPTRACK REPORT   
==================================================

STUDENT PROFILE

Student Name           : Bijjam Pujitha
Registration Number    : 8777    
Graduation Year        : 2026    
Attendance             : 90.0    
Project Completed      : True    
Profile Verified       : True    

PRACTICE SUMMARY

Total Practice Days    : 7       
Attempted Days         : 6       
Absent Days            : 1       
Passed Days            : 4       
Failed Days            : 2       

Strong Days             : 4      
Satisfactory Days       : 0      
Needs Improvement Days  : 2      
Critical Days           : 0      

PERFORMANCE ANALYSIS

Total Score            : 420     
Average Score          : 70.00   
Highest Score          : 90      
Highest Score Day      : 1       
Lowest Score           : 40      
Lowest Score Day       : 7       

First Critical Score   : Not Available

FINAL DECISION

Final Status           : Ready for Mock Interviews
Primary Blocker        : None
Next Action            : Proceed to placement mock interviews
```

---

# Test Result Summary

+----+----------------------------------+-------------------------------+--------+
| No | Test Case                        | Result                        | Status |
+----+----------------------------------+-------------------------------+--------+
| 1  | Student Name Validation          | Successfully Validated        | PASS   |
| 2  | Registration Number Input        | Successfully Recorded         | PASS   |
| 3  | Graduation Year Validation       | 2026 Accepted                 | PASS   |
| 4  | Attendance Validation            | 90% Accepted                  | PASS   |
| 5  | Project Completion Validation    | Yes Accepted                  | PASS   |
| 6  | Profile Verification Validation  | Yes Accepted                  | PASS   |
| 7  | Score Validation                 | Valid Scores Accepted         | PASS   |
| 8  | Seven-Day Practice Processing    | Successfully Processed        | PASS   |
| 9  | Absence Handling                 | 1 Absent Day Recorded         | PASS   |
| 10 | Performance Classification       | Correctly Classified          | PASS   |
| 11 | Highest Score Tracking           | 90 (Day 1)                    | PASS   |
| 12 | Lowest Score Tracking            | 40 (Day 7)                    | PASS   |
| 13 | Average Score Calculation        | 70.00                         | PASS   |
| 14 | Critical Score Detection         | No Critical Score Found       | PASS   |
| 15 | Placement Readiness Evaluation   | Ready for Mock Interviews     | PASS   |
| 16 | Final Report Generation          | Successfully Generated        | PASS   |
+----+----------------------------------+-------------------------------+--------+


---

# Individual Contribution

**Name:** Bijjam Pujitha

**Repository URL:**
https://github.com/pujithabijjam/preptrack-pujitha.git


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

Reviewed Member: Syna

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

**Reviewed By:** Syna

### Feedback Received

During the project review, it was observed that the final_status values in the placement decision logic did not exactly match the status names specified in the Project Requirements Document (PRD). Some conditions reused incorrect status messages, while others used wording that differed from the required specification. The reviewer recommended updating all final_status assignments to use the exact PRD-defined status names, including Insufficient Passed Practices, Practice Improvement Required, Graduation Criteria Not Met, and Application On Hold where applicable. This feedback was provided to ensure consistency between the implementation and the project requirements, improve report accuracy, and enable both manual and automated test cases to validate the application using the expected output strings.



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

Based on the review feedback, the placement decision logic was refined to align completely with the Project Requirements Document (PRD). All final_status values were updated to use the exact status names specified in the PRD, ensuring consistency between the application output and the project requirements. The status messages for Insufficient Passed Practices, Practice Improvement Required, Graduation Criteria Not Met, and Application On Hold were corrected wherever necessary. These improvements enhanced the accuracy of the final report, ensured compliance with the project specification, and improved the reliability of both manual and automated test case validation.
