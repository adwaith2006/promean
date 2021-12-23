import csv
with open("heightweight.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

new_data=[]
for w in range(len(file_data)):
    num=file_data[w][2]
    new_data.append(float(num))

length_data=len(new_data)
total=0
for x in new_data:
    total+=x

mean=total/length_data
print('Mean of data is:'+ str(mean))


