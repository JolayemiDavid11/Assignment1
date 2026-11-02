print("===== PHYSICS FORMULA CALCULATOR =====")

# 1. SPEED
print("\n1. SPEED")
distance = float(input("Enter distance in metres: "))
time = float(input("Enter time in seconds: "))
speed = distance / time
print("Speed =", speed, "m/s")

# 2. FORCE
print("\n2. FORCE")
mass = float(input("Enter mass in kg: "))
acceleration = float(input("Enter acceleration in m/s2: "))
force = mass * acceleration
print("Force =", force, "N")


# 3. WEIGHT
print("\n3. WEIGHT")
mass = float(input("Enter mass in kg: "))
gravity = 9.8
weight = mass * gravity
print("Weight =", weight, "N")


# 4. KINETIC ENERGY
print("\n4. KINETIC ENERGY")
mass = float(input("Enter mass in kg: "))
velocity = float(input("Enter velocity in m/s: "))
kinetic_energy = 0.5 * mass * velocity ** 2
print("Kinetic Energy =", kinetic_energy, "J")


# 5. POTENTIAL ENERGY
print("\n5. POTENTIAL ENERGY")
mass = float(input("Enter mass in kg: "))
height = float(input("Enter height in metres: "))
gravity = 9.8
potential_energy = mass * gravity * height
print("Potential Energy =", potential_energy, "J")
