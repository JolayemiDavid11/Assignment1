def calculate_velocity(distance, time):
    velocity = distance / time
    print("Velocity is:", velocity)

def calculate_area(radius):
    area = 3.14 * radius * radius
    print("Area is:", area)

choice = input("Enter 'v' to calculate velocity or 'a' to calculate area of a circle: ").lower()

if choice == 'v':
    distance = float(input("Enter the distance: "))
    time = float(input("Enter the time: "))
    calculate_velocity(distance, time)
elif choice == 'a':
    radius = float(input("Enter the radius: "))
    calculate_area(radius)
else:
    print("Invalid choice. Please enter 'v' or 'a'.")
