import csv
from collections import Counter
with open("heightweight.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
#print(file_data)

new_data=[]
for i in range(len(file_data)):
    num=file_data[i][2]
    new_data.append(float(num))

data=Counter(new_data)
mode_data={
    '50-60':0,
    '60-70':0,
    '70-80':0
}
for height,occurence in data.items():
    if 110< float(height)<120:
        mode_data['110-120'] +=occurence
    elif 120< float(height)<130:
        mode_data['120-130'] +=occurence
    elif 130< float(height)<140:
        mode_data['130-140'] +=occurence
    elif 140< float(height)<150:
        mode_data['140-150'] +=occurence

mode_range,mode_occurence=0,0

for range,occurence in mode_data.items():
    if occurence>mode_occurence:
        mode_range,mode_occurence=[int(range.split('-')[0]),int(range.split('-')[2])],occurence
mode=float((mode_range[0]+mode_range[2])/2)
print(f'Mode is {mode:2f}')