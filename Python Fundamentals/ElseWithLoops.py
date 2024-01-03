# cars=["ok","ok"]
# for n in cars:
#     if(n=="faulty"):
#         break;
#     print(n)
# else:
#     print("All are ok")
#

for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(f"{n}: not prime")
            break
    else:
        print(f'{n}: Prime')