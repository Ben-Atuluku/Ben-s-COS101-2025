print('Formula a. Velocity = Acceleration × time + Initial velocity ... |(v = at + U)')
print('Formula b. Momentum = Mass × Velocity                         ...|(P = mv)')
print('Formula c. Force = Mass × Acceleration                        ...|(F = ma)')
print('Formula d. Velocity = Displacement/Time                       ...|(v = d/t)')
print('Formula e. Weight = Mass × Acceleration due to gravity        ...|(W = mg)')
selected_formula = input('\nWhat formula would you like to use?\n Enter a formula between a-e: ')
if selected_formula == 'a':
    acceleration = float(input('Enter the acceleration: '))
    time = float(input('Enter the time: '))
    initial_vel = float(input('Enter the initial velocity: '))
    print('Velocity = ' + str((acceleration * time) + initial_vel) + 'm/s')
elif selected_formula == 'b':
    mass = float(input('Enter mass: '))
    velocity = float(input('Enter velocity: '))
    print('Momentum = ' + str(mass * velocity) + 'Kgm/s')
elif selected_formula == 'c':
    mass = float(input('Enter mass: '))
    acceleration = float(input('Enter the acceleration: '))
    print('Force = ' + str(mass * acceleration) + 'N')
elif selected_formula == 'd':
    displacement = float(input('Enter the displacement: '))
    time = float(input('Enter the time: '))
    print('Velocity = ' + str(displacement / time) + 'm/s')
elif selected_formula == 'e':
    mass = float(input('Enter the mass: '))
    print('Weight = ' + str(mass * 9.8) + 'N')
else:
    print("Invalid formula... \nPlease enter a formula between a and e")
