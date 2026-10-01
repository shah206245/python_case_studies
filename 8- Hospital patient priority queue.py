
patient = {1:{'name':'John Doe','Age':64,'priority status':'CRITICAL'},
           2:{"name":"Marry Smith","Age":29,'priority status':"REGULAR"},
           3:{"name":"Alex Brown","Age":42,'priority status':'REGULAR'}
           }

print(50 * "=")
print("HOSPITAL TRIAGE QUEUE DASHBOARD".center(50))
print("=" * 50)
print(f"{"Pos":<4} | {"Patient Name":<15} | {"Age":<4} | {"Priority Status":<14}")
print("-" * 50)

total_waiting_patient = 0
average_patient_age = 0
for patient_pos,details in patient.items():

    patient_name = details['name']
    age = details['Age']
    priority_status = details['priority status']

    total_waiting_patient += 1

    print(f'{patient_pos:<4} | {patient_name:15} | {age:<4} | {priority_status:<14}')

    average_patient_age += age 

print(50 * "-")
print("Total Waiting Patients : ",total_waiting_patient)
print(f"Average Patient Age : {average_patient_age/3} years")
print(50 * "=")