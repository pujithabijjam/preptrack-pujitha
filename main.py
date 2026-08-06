# ==================================================
# PREPTRACK — BOILERPLATE CODE
# Complete every section marked TODO.
# ==================================================

print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)

# --------------------------------------------------
# 1. COLLECT STUDENT DETAILS
# --------------------------------------------------

# TODO: Validate that the student name is not empty.
student_name = input("Enter student name: ")
while student_name == "":
    print("student name cannot be empty")
    student_name = input("Enter student name: ")
    if student_name !="":
        break
registration_number = input("Enter registration number: ")
graduation_year = int(input("Enter graduation year: "))
while graduation_year < 2025 or graduation_year > 2027:
    print("Please enter the valid graduation year")
    graduation_year = int(input("Enter graduation year: "))

graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027
)

# TODO: Validate attendance between 0 and 100.

while True:
    attendance = float(input("Enter attendance percentage: "))

    if 0 <= attendance <= 100:
        print("Attendance accepted.")
        break
    else:
        print("Invalid attendance. Enter a value between 0 and 100.")
# TODO: Accept only yes or no.
 
print("Has the student completed the required project?")

while True:
    project_input = input("Enter yes or no: ").lower()

    if project_input == "yes":
        project_completed = True
        break

    elif project_input == "no":
        project_completed = False
        break

    else:
        print("Invalid input. Enter only yes or no.")

# TODO: Convert project_input into True or False.


# TODO: Accept only yes or no.

print("Is the student profile verified?")

while True:
    profile_input = input("Enter yes or no: ").lower()

    if profile_input == "yes":
        profile_verified = True
        break

    elif profile_input == "no":
        profile_verified = False
        break

    else:
        print("Invalid input. Enter only yes or no.")
# TODO: Convert profile_input into True or False.


# --------------------------------------------------
# 2. INITIALIZE COUNTERS AND VARIABLES
# --------------------------------------------------

total_score = 0

attempted_days = 0
absent_days = 0

passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0


# --------------------------------------------------
# 3. PROCESS SEVEN PRACTICE DAYS
# --------------------------------------------------
for day in range(1, 8):

    # TODO: Use a while loop to accept only:
    # -1 or a score between 0 and 100.
    while True:
        score = int(input(f"Enter Day {day} score from 0 to 100, or -1 for absent: "))

        if score == -1 or (score >= 0 and score <= 100):
            print("Score accepted.")
            break
        else:
            print("Invalid score. Enter -1 or a value between 0 and 100.")

    # TODO: Handle absence.
    # Increase absent_days and use continue.
    if score == -1:
        absent_days += 1
        print(f"Day {day} Result: Absent")
        continue

    # TODO: Increase attempted_days and total_score.
    attempted_days += 1
    total_score += score

    # TODO: Initialize or update:
    # highest_score, highest_score_day,
    # lowest_score and lowest_score_day.
    if first_attempt_found == False:

        highest_score = score
        highest_score_day = day

        lowest_score = score
        lowest_score_day = day

        first_attempt_found = True
    else:

        if score > highest_score:
            highest_score = score
            highest_score_day = day

        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day

    # TODO: Classify the score:
    # 75–100  -> Strong
    # 60–74   -> Satisfactory
    # 40–59   -> Needs Improvement
    # 0–39    -> Critical

    if score >= 75:

        print(f"Day {day} Result: Strong")
        strong_days += 1
        passed_days += 1

    elif score >= 60:

        print(f"Day {day} Result: Satisfactory")
        satisfactory_days += 1
        passed_days += 1

    elif score >= 40:

        print(f"Day {day} Result: Needs Improvement")
        improvement_days += 1
        failed_days += 1
    else:

        print(f"Day {day} Result: Critical")
        critical_days += 1
        failed_days += 1

        # Store first critical day and score
        if critical_score_found == False:
            critical_score_found = True
            first_critical_day = day
            first_critical_score = score

    # TODO: Count passed and failed days.

    # TODO: Store only the first critical day and score.



# --------------------------------------------------
# 4. CALCULATE THE AVERAGE
# --------------------------------------------------

# TODO: Prevent division by zero.
if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0


# --------------------------------------------------
# 5. CREATE ELIGIBILITY CONDITIONS
# --------------------------------------------------

graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027
)

attendance_eligible = attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)


# --------------------------------------------------
# 6. DETERMINE FINAL STATUS
# --------------------------------------------------

# TODO: Check conditions in this priority:
# 1. No practice attempted
# 2. Critical score found
# 3. Fewer than six attempts
# 4. Fewer than four passed days
# 5. Average below 70
# 6. Attendance below 75
# 7. Graduation year not eligible
# 8. Project incomplete
# 9. Profile not verified
# 10. Ready for Mock Interview

if attempted_days == 0:

    final_status = "Practice Not Evaluated"
    primary_blocker = "No practice attempted"
    next_action = "Attempt the required coding practices"

elif critical_score_found:

    final_status = "Critical Support Required"
    primary_blocker = "Critical score found"
    next_action = "Revise the concepts from the first critical day"

elif attempted_days < 6:

    final_status = "Practice Incomplete"
    primary_blocker = "Fewer than six practices attempted"
    next_action = "Complete at least six practice days"

elif passed_days < 4:

    final_status = "Insufficient Passed Practices"
    primary_blocker = "Fewer than four practices passed"
    next_action = "Pass at least four coding practices"

elif average_score < 70:

    final_status = "Practice Improvement Required"
    primary_blocker = "Average score below 70"
    next_action = "Improve the average score to at least 70"

elif attendance < 75:

    final_status = "Attendance Improvement Required"
    primary_blocker = "Attendance below 75"
    next_action = "Improve attendance to at least 75 percent"

elif not graduation_eligible:

    final_status = "Graduation Criteria Not Met"
    primary_blocker = "Graduation year not eligible"
    next_action = "Check the eligible graduation-year requirement"

elif not project_completed:

    final_status = "Application On Hold"
    primary_blocker = "Project incomplete"
    next_action = "Complete the required project"

elif not profile_verified:

    final_status = "Application On Hold"
    primary_blocker = "Profile not verified"
    next_action = "Complete profile verification"

else:

    final_status = "Ready for Mock Interview"
    primary_blocker = "None"
    next_action = "Proceed to placement mock interviews"

# ==================================================
# DISPLAY VALUES WHEN NO PRACTICE WAS ATTEMPTED
# ==================================================

if attempted_days == 0:
    final_status = "Practice Not Evaluated"
    primary_blocker = "No practice attempted"
    next_action = "Attempt the required coding practices"
elif critical_score_found:
    final_status = "Critical Support Required"
    primary_blocker = "Critical score found"
    next_action = "Revise the concepts from the first critical day"

elif attempted_days < 6:
    final_status = "Practice Incomplete"
    primary_blocker = "Fewer than six practices attempted"
    next_action = "Complete at least six practice days"
    
elif passed_days < 4:
    final_status = "Insufficient Passed Practices"
    primary_blocker = "Fewer than four practices passed"
    next_action = "Pass at least four coding practices"
    
elif average_score < 70:
    final_status = "Practice Improvement Required"
    primary_blocker = "Average score below 70"
    next_action = "Improve the average score to at least 70"
    
elif attendance < 75:
    final_status = "Attendance Improvement Required"
    primary_blocker = "Attendance below 75"
    next_action = "Improve attendance to at least 75 percent"

elif not graduation_eligible:
    final_status = "Graduation Criteria Not Met"
    primary_blocker = "Graduation year not eligible"
    next_action = "Check the eligible graduation-year requirement"

elif not project_completed:
    final_status = "Application On Hold"
    primary_blocker = "Project incomplete"
    next_action = "Complete the required project"

elif not profile_verified:
    final_status = "Application On Hold"
    primary_blocker = "Profile not verified"
    next_action = "Complete profile verification"


else:
    final_status = "Ready for Mock Interviews"
    primary_blocker = "None"
    next_action = "Proceed to placement mock interviews"


# --------------------------------------------------
# 7. DISPLAY FINAL REPORT
# --------------------------------------------------

print()
print("=" * 50)
print("              PREPTRACK REPORT")
print("=" * 50)
print()
print("STUDENT PROFILE")
print()
print(f"Student Name           : {student_name}")
print(f"Registration Number    : {registration_number}")
print(f"Graduation Year        : {graduation_year}")
print(f"Attendance             : {attendance}")
print(f"Project Completed      : {project_completed}")
print(f"Profile Verified       : {profile_verified}")

print()
print("PRACTICE SUMMARY")
print()

print("Total Practice Days    : 7")
print(f"Attempted Days         : {attempted_days}")
print(f"Absent Days            : {absent_days}")
print(f"Passed Days            : {passed_days}")
print(f"Failed Days            : {failed_days}")

print()
print(f"Strong Days             : {strong_days}")
print(f"Satisfactory Days       : {satisfactory_days}")
print(f"Needs Improvement Days  : {improvement_days}")
print(f"Critical Days           : {critical_days}")

print()
print("PERFORMANCE ANALYSIS")
print()
print(f"Total Score            : {total_score}")
print(f"Average Score          : {average_score:.2f}")
if attempted_days > 0:
    print(f"Highest Score          : {highest_score}")
    print(f"Highest Score Day      : {highest_score_day}")
    print(f"Lowest Score           : {lowest_score}")
    print(f"Lowest Score Day       : {lowest_score_day}")
else:
    print(f"Highest Score          : Not Available")
    print(f"Lowest Score           : Not Available")
    print(f"Highest Score Day      : Not Available")
    print(f"Lowest Score Day       : Not Available")


# TODO: Display highest and lowest values only when
# at least one practice was attempted.
print()
print("CRITICAL SCORE INFORMATION")
print()
# TODO: Display first critical details only when
# a critical score exists.
print(f"Critical Score Found   : {critical_score_found}")
if critical_score_found:
    print(f"First Critical Day     : {first_critical_day}")
    print(f"First Critical Score   : {first_critical_score}")
else:
    print(f"First Critical Day     : Not Available")
    print(f"First Critical Score   : Not Available")
print()
print("FINAL DECISION")

print()
print(f"Final Status           : {final_status}")
print(f"Primary Blocker        : {primary_blocker}")
print(f"Next Action            : {next_action}")

print("=" * 50)