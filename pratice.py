''''

x=5
y=10
print(f"before swaping x:{x},y:{y}")
#x,y=y,x
x=x+y
y=x-y
x=x-y
print(f" after swaping x:{x},y:{y}")

x="sreyas krishnan a s"
print(x)
print(len(x))
print(str(x)[::-1])



x=["apple","cat","bat","dog"]
print(sorted(x))



x =int(input("Enter the number = "))
fact = 1

while x>0:
    fact = fact * x
    x = x - 1

print("Factorial is:", fact)
a = 0
b = 10
for i in range(100):
    c = a + b
    print(c)
    a = b
    b = c

n = 10
for i in range(1, n):
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        print(i)

# Initial conditions
speed = 80  # km/h
time = 2  # hours
fuel_tank = 50  # liters
fuel_used = 20  # liters
engine_status = 1  # 1 = ON
battery_level = 18  # %

# Arithmetic operators
distance = speed * time
remaining_fuel = fuel_tank - fuel_used

print(f"Distance Travelled: {distance} km")
print(f"Remaining Fuel: {remaining_fuel} liters")

# Relational and Logical operators
if remaining_fuel < 10 and engine_status == 1:
    print("Critical: Low Fuel with Engine ON!")

if remaining_fuel < 10 or battery_level < 20:
    print("Check Vehicle: Low fuel or low battery!")

# Assignment operators
# Updating fuel after a small trip
small_trip_distance = 10  # km
fuel_consumed_small_trip = 2

distance += small_trip_distance
remaining_fuel -= fuel_consumed_small_trip

print(f"Updated Distance: {distance} km")
print(f"Updated Remaining Fuel: {remaining_fuel} liters")
def log_with_message(msg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{msg}: About to call {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{msg}: Finished calling {func.__name__}")
            return result
        return wrapper
    return decorator

# Apply the decorator with a custom message
@log_with_message("EngineMonitor")
def check_engine_temp(temp):
    return temp < 100

# Test the decorated function
is_safe = check_engine_temp(95)'''


a = "we should learn about python!"
print(a)








































