student_record = {"S101" : ("Bob",87,93,95),
                  "S102" : ("Alice",85,80,88),
                  "S103" : ("Charlie",54,68,64)
}

print(50 * "=")
print("Academic Performance Dashboard".center(50))
print(50 * "=")
print(f"{"Rank":<4} | {"ID":<4} | {"Name":<7} | {"Average":<7} | {"Grade":<5} | {"Status":<4}")
print(50 * "-")

average_score = 0
top_average = 0
top_student = ""
for index,(item_id , details) in enumerate(student_record.items(),start=1):
    name = details[0]
    marks = details[1] + details[2] + details[3]
    average = marks / 3

    if average > 91 and average <=100:
        grade = "A"
        status = "PASS"
    elif average > 71 and average <=90:
        grade  = "B"
        status = "PASS"
    elif average > 51 and average <=70:
        grade = "C"
        status = "PASS"
    else:
        grade = "D"
        status = "FAIL"
    print(f"{index:<4} | {item_id:<4} | {name:<7} | {average:<7.2f} | {grade:<5} | {status:<4}")

    if average > top_average :
        top_average = average
        top_student = name

    average_score += average
    
class_average_score  = average_score / 3
print(50 * "-")
print(f"Class Averag Score  : {class_average_score:.2f}")
print(f"Top Scoring Student : {top_student} {top_average:.2f}")
print(50 * "=")


