#day 5 

task =["eat", "sleep", "code"]

print(task)


task.append("repeat")

print(task)

for i in task:
    print(i)
    if i == "code":
        print("Time to code!")
    else:
        print("Not coding time yet.")

