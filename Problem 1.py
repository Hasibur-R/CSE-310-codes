#The initial velocity of a car is   u    m/s and the acceleration is    a   m/s2 
u=float(input("Ente the Intitial velocty of CAR: "))
a=float(input("Enter the acceleration: "))

#a. Find out the velocity of the car after t sec.
t=float(input("Enter the time: "))
T=u+(a*t)
print(f"Velocity of the car after {t}sec: {T}")

print("\n\n")
#b. Find the distance covered by the car after t sec.
s =u*t +0.5*a *t *t
print(f"The distance covered by the car after {t}sec: {s}")