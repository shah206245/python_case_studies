job_requirement = {'Python','SQL','Git','Docker'}

candidate_profile = {'Sarah':{'Python','SQL','Git','Docker'},
                     'John':{'Python','SQL'},
                     'Mike':{'SQL'}
                     }

print(50 * "=")
print("HR REQUIREMENT MATCH REPORT".center(50))
print(50 * "=")
print(f'{'Candidate':<10} | {"Match Score":<11} | {"Matched Skills":<14} | {"Missing":<20}')
print(50 * "-")

for name,skill in candidate_profile.items():

    match_skill = job_requirement.intersection(skill)

    missing_skill = job_requirement.difference(skill)

    score = (len(match_skill) / len(job_requirement)) * 100

    if match_skill == job_requirement:
        best_score_name = name
        best_score = "(100%)"
        match_skill = "All Required"
        missing_skill = "None"
    else:
        match_skill = ", ".join(match_skill)
        missing_skill = ", ".join(missing_skill)
    print(f'{name:<10} | {score:<11.1f} | {match_skill:<14} | {missing_skill:<20}')

print(50 * "-") 
print("Best Candidate Match : ",best_score_name, best_score)    
print(50 * "=")
