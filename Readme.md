Project Overview

PrepTrack is a Python-based console application developed to evaluate a student's placement preparation and determine their readiness for a placement mock interview. The application collects validated student information, including the student name, registration number, graduation year, attendance percentage, project completion status, profile verification status, and seven daily coding-practice scores. It validates every user input before processing and analyzes the student's performance using predefined evaluation criteria.

The application classifies daily coding-practice scores into Strong, Satisfactory, Needs Improvement, and Critical categories while tracking important performance metrics such as attempted days, absent days, passed days, failed days, highest score, lowest score, average score, and the first critical score. Based on these results, it evaluates placement eligibility using attendance, graduation year, coding performance, project completion, and profile verification. Finally, the program generates a comprehensive PREPTRACK REPORT containing the Student Profile, Practice Summary, Performance Analysis, Critical Score Information, and Final Decision. The project is implemented entirely using core Python programming concepts without using lists, tuples, or built-in aggregation functions.

Objectives

Collect and validate student information.
Process seven days of coding-practice scores.
Classify daily performance into different categories.
Track practice statistics and score analytics.
Evaluate placement readiness using multiple eligibility conditions.
Generate a structured placement performance report.

Features Implemented
Student Details Processing

Student name validation
Registration number input
Graduation year validation
Attendance percentage validation
Project completion verification
Profile verification

Coding Practice Processing

Seven-day practice evaluation
Score validation (0–100 or -1 for absent)
Absence handling
Daily performance classification
Attempted and absent day tracking
Passed and failed day counting

Performance Analysis

Total score calculation
Average score calculation
Highest score tracking
Lowest score tracking
Critical score detection
First critical day identification

Placement Readiness Evaluation

Graduation year eligibility
Attendance eligibility
Practice completion verification
Average score evaluation
Critical score verification
Passed day verification
Project completion check
Profile verification check

Final Report Generation

Student Profile
Practice Summary
Performance Analysis
Critical Score Information
Final Placement Decision

Python Concepts Used

Input and Output
Variables
Data Types
Type Casting
Conditional Statements
Boolean Expressions
While Loop
For Loop
Range Function
Break Statement
Continue Statement
Counters and Accumulators
Arithmetic Operators
Relational Operators
Logical Operators
f-Strings
String Formatting

Technologies Used

Python 3
Visual Studio Code
Command Line / Terminal

How to Run the Project

python main.py

or

python3 main.py

Sample Output

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
==================================================

===============================================================
                    TEST RESULT SUMMARY
===============================================================

Test-Result Summary

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


Individual Contribution

Name: Bijjam Pujitha

Repository URL: https://github.com/pujithabijjam/preptrack-pujitha.git

My main contribution: Implemented the complete execution flow in main.py — building input validation loops for all profile fields, constructing the seven-day practice analysis loop, tracking score metrics without any prohibited data structures, and establishing the priority-based final decision chain.

Features I implemented: Interactive input validation loops (student_name, attendance, project_input, profile_input, score); daily score classification and category counting; list-free tracking for highest_score and lowest_score; first critical score locking logic; eight eligibility Boolean expressions and a combined placement_ready flag; a 9-tier if-elif-else priority decision chain; and formatted terminal report rendering.

Python Concepts I used: while loops, for loops with range(), break, continue, if-elif-else structures, Boolean expressions, accumulators, type casting, and formatted f-strings.

Most difficult logic: Tracking highest_score and lowest_score across iterations without using lists, arrays, or built-in max()/min() functions, while correctly excluding absent days (-1) from every comparison.

Problem I faced: Making sure an absent day (-1) never got compared against lowest_score or added into total_score and average_score.

How I solved it: Placed the if score == -1 check immediately after score validation to increment absent_days and trigger continue, skipping all classification and comparison logic for that day. Used the first_attempt_found flag to set the initial highest/lowest values on the first attempted day, then applied > and < comparisons only on subsequent attempted days.


Code Review Completed

Reviewed Member: [Dudekula Syna Begum]

Repository URL: [https://github.com/pujithabijjam/preptrack-pujitha.git]

What Was Done Well:

The absent-day check (if score == -1) runs immediately after score validation and before any classification logic, so continue correctly skips highest/lowest comparison, total_score accumulation, and passed/failed counting for that day.
The highest/lowest score logic uses the first_attempt_found flag to seed both values from the first attempted day instead of defaulting to 0, which correctly avoids a false low score when a student's actual scores are all above 0.

Issue Identified:

The final_status values used in the placement decision logic do not fully match the status names defined in the Project Requirements Document (PRD). Some conditions use different or reused status messages instead of the exact PRD-specified values. For example, the "Fewer than Four Passed Days" condition should return "Insufficient Passed Practices", while the "Average Score Below 70" condition should return "Practice Improvement Required". Similarly, the statuses for graduation eligibility, project completion, and profile verification should exactly follow the PRD wording to maintain consistency.

Suggested Improvement:

Update all final_status assignments in the decision-making logic to use the exact status names specified in the PRD. This ensures consistency between the implementation and the project requirements, improves report accuracy, and allows automated and manual test cases to verify the output using the expected status strings without mismatches.

Feedback Received

Reviewed By:[Dudekula Syna Begum]

During the project review, it was observed that the final_status values in the placement decision logic did not exactly match the status names specified in the Project Requirements Document (PRD). Some conditions reused incorrect status messages, while others used wording that differed from the required specification. The reviewer recommended updating all final_status assignments to use the exact PRD-defined status names, including Insufficient Passed Practices, Practice Improvement Required, Graduation Criteria Not Met, and Application On Hold where applicable. This feedback was provided to ensure consistency between the implementation and the project requirements, improve report accuracy, and enable both manual and automated test cases to validate the application using the expected output strings.

Improvement Made After Review

Based on the review feedback, the placement decision logic was refined to align completely with the Project Requirements Document (PRD). All final_status values were updated to use the exact status names specified in the PRD, ensuring consistency between the application output and the project requirements. The status messages for Insufficient Passed Practices, Practice Improvement Required, Graduation Criteria Not Met, and Application On Hold were corrected wherever necessary. These improvements enhanced the accuracy of the final report, ensured compliance with the project specification, and improved the reliability of both manual and automated test case validation.




