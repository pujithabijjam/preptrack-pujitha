# preptrack-pujitha
Project Title

PrepTrack — Placement Preparation Performance Analyzer

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


Project Outcome

The PrepTrack application successfully evaluates a student's placement preparation by validating inputs, analyzing coding-practice performance, identifying strengths and weaknesses, tracking critical performance indicators, and generating a detailed placement readiness report. It provides clear feedback and recommendations that help students understand their current preparation level and the improvements required before attending placement mock interviews.
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
