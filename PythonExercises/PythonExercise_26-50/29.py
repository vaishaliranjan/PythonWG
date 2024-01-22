def volume_calculator(h):
    RADIUS=10
    PI= 3.14
    liquid_volume= ((4 * PI * RADIUS ** 3)/3)-(PI * h**2 *( 3 * RADIUS - h)/3)
    print(liquid_volume)
volume_calculator(2)
