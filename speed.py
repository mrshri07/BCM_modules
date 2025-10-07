
''''speed = 20
driver_seatbelt_on = False

if speed > 120 and driver_seatbelt_on == False:
    print("Overspeed with no seatbelt!")
elif speed <= 120 or driver_seatbelt_on == True:
    print("Safe driving.")


door_closed = True
ignition_on = True
engine_oil_ok = True

if door_closed==True and ignition_on==True and engine_oil_ok==True:
    print("Car can start")
else:
    print("Car cannot start")
list=[5,8,9,5,4,6,'ijyytf']
print(list)
list[2]=10
print(list)


tuple={8,9,5,6,3,2,8}
print(tuple)
#tuple[3]=5
print(tuple)

dic={'name':'shreyas','age':'25'}
print(dic)
dic['age']='30'
print(dic)

x=input("Enter name:")
print(x)
y=input("num")
print(y)



engine_running=False
dark=False
if engine_running==False:
    if dark==True:
        print("headlight is on")
    else:
        print("headlight is off")
else:
    print("headlight not work")




engine_temp=10
engine_rpm=5000

if engine_temp > 100 and engine_rpm > 3000:
    print("High Temp & High RPM")
elif engine_temp > 100 and engine_rpm <= 3000:
        print("High Temp")
elif engine_temp <= 100 and engine_rpm > 3000:
    print("High RPM")
else:
    print("Normal Operation")

tuple=(8,9,5,6,3,2,8)
print(tuple)
print(type(tuple))


a=int(input ("a="))
b=int(input("b="))


print(a+b)

sensor_data = b'\x10\x20\x30'  # immutable values

data_array = bytearray(sensor_data)  # muttable of value
print(data_array)
data_array[1] = 0x99
print(data_array)
print([hex(byte) for byte in data_array])

can_fram = bytes([0x10, 0x02, 0x04])

Dta_array = bytearray(can_fram)
Dta_array[2] = 0x07

print(Dta_array)
print(f'')







x=[1,2,3]
print(x)
x.append([4,5])
print("X=",x)
x.extend([5,6])
print("X=",x)

def div(a,b):
    print(a/b)



div(1,2)
"""a=4
b=5
if(a<b):
    print("a<b")
else:
    print("b<a")

a=2
x=range(a,1)

print(x)
print(type(x))

d="dygcshujx"
print(d[1:4:2])


my_list=[1,2,3,4,5]

iterator=iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

rows = 10
for i in range(1, rows + 1):
    print("#" * i)


x="*"
for i in range(6):
    print(x*i)






def greet(name):
    print(f"Hello, {name}!")
def age(age):
  print(f"age={age}")

greet("xfcg")
age(54)
greet("sfdghj")

age(9)
"""
my_list=[1,2,3,4,5,6]
gen = my_list()

for my_list in gen:
    print(my_list)
'''
class Truck:
    def __init__(self, manufacturer, model, load_capacity):
        self.manufacturer = manufacturer
        self.model = model
        self.load_capacity = load_capacity  # in tons
        self.current_load = 0

    def load_cargo(self, weight):
        if self.current_load + weight > self.load_capacity:
            print(f"Cannot load {weight} tons. Exceeds capacity of {self.load_capacity} tons.")
        else:
            self.current_load += weight
            print(f"Loaded {weight} tons. Current load: {self.current_load} tons.")

    def unload_cargo(self, weight):
        if weight > self.current_load:
            print(f"Cannot unload {weight} tons. Only {self.current_load} tons loaded.")
        else:
            self.current_load -= weight
            print(f"Unloaded {weight} tons. Current load: {self.current_load} tons.")

# Instantiate two Truck objects
truck1 = Truck("Volvo", "FH16", 20)
truck2 = Truck("Mercedes", "Actros", 25)

# Call methods on truck1
truck1.load_cargo(10)
truck1.unload_cargo(5)
truck1.load_cargo(15)

# Call methods on truck2
truck2.load_cargo(18)
truck2.unload_cargo(10)
truck2.load_cargo(8)

































