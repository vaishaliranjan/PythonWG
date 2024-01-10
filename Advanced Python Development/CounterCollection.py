from collections import Counter

device_temp=[13.4,35.2,15.0,16.4,15.0]
temp_counter = Counter(device_temp)
print(temp_counter[15.0])

print(Counter({"hello":3, "hi":12})['hi'])

student ={
    "name":122,
    "sd":34
}
student_COUNTER = Counter(student)
print(student_COUNTER["name"])