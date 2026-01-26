# day 6

Profile ={
            "Name": "Prabu",
            "Age": 25, "City": "Dallas"
            }


Profile["Skill"] = "AI Developer"


Profile["Age"] += 1


Profile2 ={ "Salary": 100000, "Experience": 3}

print(Profile2)

#mergeed_profile = Profile | Profile2

mergeed_profile = {**Profile, **Profile2}

print(mergeed_profile)