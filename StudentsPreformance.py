import pandas as pd
import csv
import statistics

with open('StudentsPerformance.csv', newline="") as f:
  reader = csv.reader(f)
  StudentPerformance_data = list(reader)

StudentPerformance_data.pop(0)

scores=[]
for i in StudentPerformance_data:
    a=float(i[5])+float(i[6])+float(i[7])
    scores.append(a)

mean = statistics.mean(scores)
standardDeviation = statistics.stdev(scores)

range1Start,range1End = mean-standardDeviation,mean+standardDeviation
range2Start,range2End = mean-2*standardDeviation,mean+2*standardDeviation
range3Start,range3End = mean-3*standardDeviation,mean+3*standardDeviation

#count = 0
#for i in data:
#    if(i > range1Start ):
#        if(i < range1End):
#            count=count+1

range1Array = [i for i in scores if i > range1Start and i < range1End]
range2Array = [i for i in scores if i > range2Start and i < range2End]
range3Array = [i for i in scores if i > range3Start and i < range3End]

Range1Count = len(range1Array)
Range2Count = len(range2Array)
Range3Count = len(range3Array)
totalCount = len(scores)

percentage_Range1 = Range1Count*100/totalCount
percentage_Range2 = Range2Count*100/totalCount
percentage_Range3 = Range3Count*100/totalCount

print(percentage_Range1,percentage_Range2,percentage_Range3)