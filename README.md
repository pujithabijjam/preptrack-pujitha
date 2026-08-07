# preptrack-pujitha
Project Title
PrepTrack — Placement Preparation Performance Analyzer

Project Overview

PrepTrack — Placement Preparation Performance Analyzer is a Python-based console application designed to evaluate a student's placement readiness by analyzing academic eligibility, attendance, project completion, profile verification, and coding practice performance. The application collects validated student information, processes seven daily coding-practice scores, classifies performance into different categories, tracks highest and lowest scores, detects critical performance, and generates a comprehensive performance report. Based on predefined eligibility criteria, PrepTrack determines whether the student is ready for a placement mock interview and provides the final status, primary blocker (if any), and recommended next action. The project is implemented using core Python concepts such as input validation, conditional statements, loops, Boolean logic, counters, accumulators, and formatted output, without using lists, tuples, or built-in aggregation functions.
Features Implemented
Student Details Processing:

Non-empty student name input validation loop (student_name)
Registration number input collection (registration_number)
Graduation year input collection (graduation_year), evaluated later during eligibility checking
Attendance percentage validation loop enforcing range 0–100 with an "Attendance accepted." confirmation message (attendance)
Case-insensitive yes/no validation loops (using .lower()) converting inputs into Boolean flags for project completion (project_completed) and profile verification (profile_verified)
Practice & Score Processing:

Seven-day practice loop processing (for day in range(1, 8))
Score validation loop supporting -1 for absence or 0–100 score range, with a "Score accepted." confirmation message
Absence handling with absent_days counter, a dedicated "Absent" result line, and continue control flow
Four-tier daily performance classification: Strong (75–100), Satisfactory (60–74), Needs Improvement (40–59), and Critical (0–39)
Tracking of practice engagement metrics: Attempted Days, Absent Days, Passed Days (score ≥ 60), and Failed Days (score < 60)
Detailed score category counts for Strong Days, Satisfactory Days, Needs Improvement Days, and Critical Days
Performance & Critical Score Analytics:

Total score accumulation (total_score) and average score calculation (average_score) formatted to 2 decimal places with zero-division protection
List-free high/low score detection tracking Highest Score, Highest Score Day, Lowest Score, and Lowest Score Day using an initialization flag (first_attempt_found)
Fallback display handling ("Not Available") for highest/lowest metrics when no practice days were attempted
First critical score lock tracking (Critical Score Found, First Critical Day, First Critical Score) with fallback handling ("Not Applicable") when no critical score exists (score < 40)
Readiness Evaluation & Final Decision Report:

Eight independent eligibility Boolean expressions (graduation year, attendance, practice count, average score, critical-score clearance, passed-days count, project completion, profile verification)
Combined placement_ready Boolean and explicit Placement Ready line in the report
Priority-based decision chain evaluating 9 status levels in order, so only the first major blocker is displayed
Determination of Final Status, Primary Blocker, and actionable Next Action
Clean formatted ASCII report terminal output (PREPTRACK REPORT) with structured sections (PRACTICE SUMMARY, PERFORMANCE ANALYSIS, FINAL DECISION)
Python Concepts Used
Basic Input / Output (input(), print())
Type Casting (int(), float())
Primitive Data Types & Variables (Strings, Integers, Floats, Booleans)
Conditional Statements (if, elif, else)
Boolean Operators & Logic (and, not)
Loops (while for validation, for with range(1, 8))
Loop Control Keywords (break, continue)
Increment Counters & Accumulators (total_score, attempted_days, absent_days, passed_days, failed_days, etc.)
String Formatting & Precision Control (f-strings, {attendance:.2f}, {average_score:.2f}, inline ternary expressions)
Instructions to Run the Program
To execute the application, run:

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

