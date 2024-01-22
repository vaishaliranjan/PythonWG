def calculate_acceleration(v1,v2,t1,t2):
    a= (v2-v1)/(t2-t1)
    return a

print(calculate_acceleration(0,10,0,20))