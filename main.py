print('a. v = at + U \nb. P = mv \nc. F = ma\nd. v = d/t\ne. W = mg')
selected_formula = input('What formula would you like to use? ')
if selected_formula == 'a':
    acceleration = float(input('Enter the acceleration: '))
    time = float(input('Enter the time: '))
    initial_vel = float(input('Enter the initial velocity: '))
    print((acceleration * time) + initial_vel)
elif selected_formula == 'b':
    mass = float(input('Enter mass: '))
    velocity = float(input('Enter velocity: '))
    print(mass * velocity)
elif selected_formula == 'c':
    mass = float(input('Enter mass: '))
    acceleration = float(input('Enter the acceleration: '))
    print(mass * acceleration)
