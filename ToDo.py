action = raw_input("What would you like to do?")
day= raw_input("What day of the week?").lower()
To_Do = {
    "monday": [],
    "tuesday":[],
    "wednesday":[],
    "thursday":[],
    "friday":[],
    "saturday":[],
    "sunday":[],
}
def add():
    To_Do[day].append(action)
print To_Do
