def calculate_speed():
  distance = float(input("Enter distance (in meters): "))
  time = float(input("Enter time (in seconds): "))
  if time == 0:
    print("Error: Time cannot be zero.")
  else:
    speed = distance / time
    print(f"Speed = {speed:.2f} m/s")


def calculate_force():
  mass = float(input("Enter mass (in kg): "))
  acceleration = float(input("Enter acceleration (in m/s²): "))
  force = mass * acceleration
  print(f"Force = {force:.2f} N")


def calculate_weight():
  mass = float(input("Enter mass (in kg): "))
  gravity = 9.81  # Standard gravity on Earth in m/s²
  weight = mass * gravity
  print(f"Weight = {weight:.2f} N (using g = {gravity} m/s²)")


def calculate_kinetic_energy():
  mass = float(input("Enter mass (in kg): "))
  velocity = float(input("Enter velocity (in m/s): "))
  ke = 0.5 * mass * (velocity**2)
  print(f"Kinetic Energy = {ke:.2f} J")


def calculate_potential_energy():
  mass = float(input("Enter mass (in kg): "))
  height = float(input("Enter height (in meters): "))
  gravity = 9.81
  pe = mass * gravity * height
  print(f"Potential Energy = {pe:.2f} J (using g = {gravity} m/s²)")


def main():
  while True:
    print("\n--- Physics Calculator ---")
    print("1. Speed (v = d / t)")
    print("2. Force (F = m * a)")
    print("3. Weight (W = m * g)")
    print("4. Kinetic Energy (KE = 0.5 * m * v²)")
    print("5. Potential Energy (PE = m * g * h)")
    print("6. Exit")

    choice = input("\nSelect an option (1-6): ")

    if choice == "1":
      calculate_speed()
    elif choice == "2":
      calculate_force()
    elif choice == "3":
      calculate_weight()
    elif choice == "4":
      calculate_kinetic_energy()
    elif choice == "5":
      calculate_potential_energy()
    elif choice == "6":
      print("Exiting calculator. Goodbye!")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
  main()
