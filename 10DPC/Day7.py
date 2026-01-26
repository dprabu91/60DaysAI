#day 7 Set

skill = {"Python", "Java", "C++", "AI", "ML", "Python"}

print(skill)

required_skill = {"Python", "SQL"}

print("Required Skills:", required_skill)

common = skill & required_skill

print ("Common Skills:", common)

frozen = frozenset(skill)

print("Frozen Set:", frozen)    


access_rules = {
    frozenset(["read"]): "viewer",
    frozenset(["read", "write"]): "editor"
}

user_permissions = frozenset(["read", "write"])

print(access_rules[user_permissions])
