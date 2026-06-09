def calculate_status(volunteer):

    available_hours = volunteer["max_hours_per_week"] - volunteer["hours_worked"]
    volunteer["available_hours"] = available_hours
    if available_hours >= 10:
        volunteer["status"] = "Available"
    elif available_hours >= 5:
        volunteer["status"] = "Some available"
    else:
        volunteer["status"] = "Not available"
    return volunteer

def print_summary(volunteers):
    available = 0
    some_available = 0
    not_available = 0

    print("\nVolunteer Daily Summary")
    print("-" * 40)

    for number, volunteer in enumerate(volunteers, start=1):
        print(
            f"{number}. {volunteer['name']} | "
            f"Role: {volunteer['role']} | "
            f"Available Hours: {volunteer['available_hours']} | "
            f"Status: {volunteer['status']}"
        )

        if volunteer["status"] == "Available":
            available += 1
        elif volunteer["status"] == "Some available":
            some_available += 1
        else:
            not_available += 1

    print("-" * 40)
    print(f"Green: {available}, Amber: {some_available}, Red: {not_available}")

volunteers = [
    {
        "name": "John",
        "role": "Driver",
        "work_hours_today": 4,
        "max_hours_per_week": 20,
        "hours_worked": 6
    },
    {
        "name": "Ben",
        "role": "Director",
        "work_hours_today": 5,
        "max_hours_per_week": 15,
        "hours_worked": 12
    },
    {
        "name": "Anna",
        "role": "Cleaner",
        "work_hours_today": 3,
        "max_hours_per_week": 18,
        "hours_worked": 7
    },
    {
        "name": "David",
        "role": "Reception",
        "work_hours_today": 6,
        "max_hours_per_week": 25,
        "hours_worked": 20
    },
    {
        "name": "Emma",
        "role": "Support",
        "work_hours_today": 2,
        "max_hours_per_week": 12,
        "hours_worked": 4
    },
    {
        "name": "Jackie",
        "role": "Coordinator",
        "work_hours_today": 5,
        "max_hours_per_week": 30,
        "hours_worked": 28
    }
]

valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

day = ""

while day not in valid_days:
    day = input("Enter a weekday (Monday-Friday): ").lower()

    if day not in valid_days:
        print("Invalid day. Please try again.")

print(f"\nVolunteer report for {day.title()}")

for volunteer in volunteers:
    calculate_status(volunteer)

print_summary(volunteers)
