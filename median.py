import csv
with open("heightweight.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    num=file_data[i][2]
    new_data.append(float(num))

length_data=len(new_data)
new_data.sort()

if length_data % 2 == 0:
    median_1=float(new_data[length_data//2])
    median_2=float(new_data[length_data//2 + 1])
    median=(median_1+median_2)/2
else :
    median=new_data[length_data/2]

print('Median is:'+ str(median))