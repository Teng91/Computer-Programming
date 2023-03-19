import matplotlib.pyplot as plt

all_department = []
all_number = []
infile = open("info.txt")
for line in infile:
    line = line.strip()
    department, number = line.split(',')
    all_department.append(department)
    all_number.append(int(number))

plt.subplot(211)
plt.xlabel('department')
plt.ylabel('Number of people')
plt.title('Number of people in each department')
plt.bar(x=x,height=1,width=0.5)

plt.subplot(212)
plt.pie(autopct='%d%%')
plt.show()
