# Gebraucht für die Datenmanipulation, u.a. für die Integration der Fluxformulierungen

import csv
import math
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np
import scipy.integrate as integrate
import scipy.special as special
from scipy.integrate import quad




Data = []
filename = askopenfilename()
newfile = askopenfilename()
#CANCER = 0
i=0

size = [0.46,0.66,0.89,1.15,1.45,1.85,2.55,3.5,4.5,5.75,7.25,9,11,13,15,16.5]
Messgrössen = [[0.38,0.54],[0.54,0.78],[0.78,1],[1,1.3],[1.3,1.6],[1.6,2.1],[2.1,3],[3,4],[4,5],[5,6.5],[6.5,8],[8,10],[10,12],[12,14],[14,16],[16,17]]

header = []
k=4
with open(filename) as file:
    csv_reader = csv.reader(file,delimiter=",")
    for row in csv_reader:
        #CANCER =0
        if row[0]=='Month':
            k=3
            header = row
            continue
        if row[0]=='Timecode':
            k = 4
            a = row.index('LONG')
            b = row.index('LAT')
            c = row.index('13[n/ml]')
            print(row[a+k])
            print(row[40])
            header = row
            k=4
            continue
        # if float(row[k+a]) == 0:
        #     continue
        #print(i)
        #print(row)
        Data.append(row)
        i+=1

data = []
for row in Data:
    linie = []
    # linie.append('2020')
    Month = int(row[1])
    Day = int(row[2])
    Hour = int(row[3])

    Month = '0'+str(Month)
    if Day <10:
        Day = '0'+str(Day)
    else:
        Day = str(Day)

    if Hour <10:
        Hour = '0'+str(Hour)
    else:
        Hour = str(Hour)

    # linie.append(Month)
    # linie.append(Day)
    # linie.append(Hour)
    linie.append('2020'+Month+Day+Hour)
    linie.append(row[c])
    data.append(linie)

with open(newfile, mode='w', newline='') as resultate:
    resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        resultatewriter.writerow(row)



# for row in Data:
#     for n in range(19):
#         if float(row[n+4])==0:
#             row[n] = ""
#
#
# with open(newfile, mode='w', newline='') as resultate:
#     resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     resultatewriter.writerow(header)
#     for row in Data:
#         resultatewriter.writerow(row)

#
# def ln(x):
#     return math.log(x,math.e)
#
# def Schwarz(d,U_10,h):
#     k=  ((1.08+(1+(1/(1-h)))**(1/3))*ln(10))**(-1)
#     r80 = d2r80(d,h)
#     return (800*(U_10/r80)**2.5)*(1/r80)*k
#
# def Andreas(d,U_10):
#     k=0.5
#     r = 0.5*d
#     return r*1.2*(10**3)*math.exp(0.52*U_10-(0.05*U_10+0.64)*r)/(ln(10)*r)*k
#
# def Gong(d,U_10,T,h):
#     k = ((1.08+(1+(1/(1-h)))**(1/3))*ln(10))**(-1)
#     r80 = d2r80(d, h)
#     q1 = 1.373*(U_10**3.41)*(r80**(-(4.7*(1+30*r80)**(-0.017*r80**(-1.44)))))
#     q2 = (1+0.057*r80**3.45)
#     q3 = 10**(1.607*math.exp(-(1-(math.log10(r80)/0.433))**2))
#     q4 = 0.3+0.1*T-0.0076*T**2+0.00021*T**3
#     q5 = (1/r80)
#     return q1*q2*q3*q4*q5*k
#
# def d2r80(d,h):
#     return d/(1.08*(1+(1/(1-h)))**(1/3))
#
# def r802d(r80,h):
#     return r80*(1.08*(1+(1/(1-h)))**(1/3))
#
# for row in Data:
#     h= float(row[k+27])/100
#     U_10 = float(row[k+25]) / 3.6
#     SST = float(row[k+35])
#
#     S = 0
#     lowerlimit = max(0.38,r802d(3,h),r802d(0.07,h),0.5)
#     upperlimit =min(17,r802d(20,h),r802d(25,h),14)
#     for i in range(16):
#         if Messgrössen[i][0] >= lowerlimit and Messgrössen[i][1] <= upperlimit:
#             S += float(row[k + i])
#         elif Messgrössen[i][0] <= lowerlimit and Messgrössen[i][1] >= lowerlimit:
#             S += float(row[k + i]) * ((Messgrössen[i][1] - lowerlimit) / (Messgrössen[i][1] - Messgrössen[i][0]))
#         elif Messgrössen[i][0] <= upperlimit and Messgrössen[i][1] >= upperlimit:
#             S += float(row[k + i]) * ((upperlimit - Messgrössen[i][0]) / (Messgrössen[i][1] - Messgrössen[i][0]))
#
#
#
#     row.append(lowerlimit)
#     row.append(upperlimit)
#     row.append(S)
#     I = quad(Schwarz, lowerlimit,upperlimit, args=(U_10,h))[0]
#     row.append(I)
#
#     I = quad(Gong,lowerlimit, upperlimit, args=(U_10,SST,h))[0]
#     row.append(I)
#
#     I = quad(Andreas, lowerlimit,upperlimit , args=(U_10,))[0]
#     row.append(I)
#
#     S = 0
#     lowerlimit = max(0.38, r802d(3, h), r802d(0.07, h))
#     upperlimit = min(17, r802d(20, h), r802d(25, h))
#     for i in range(16):
#         if Messgrössen[i][0] >= lowerlimit and Messgrössen[i][1] <= upperlimit:
#             S += float(row[k + i])
#         elif Messgrössen[i][0] <= lowerlimit and Messgrössen[i][1] >= lowerlimit:
#             S += float(row[k + i]) * ((Messgrössen[i][1] - lowerlimit) / (Messgrössen[i][1] - Messgrössen[i][0]))
#         elif Messgrössen[i][0] <= upperlimit and Messgrössen[i][1] >= upperlimit:
#             S += float(row[k + i]) * ((upperlimit - Messgrössen[i][0]) / (Messgrössen[i][1] - Messgrössen[i][0]))
#
#
#
#     row.append(lowerlimit)
#     row.append(upperlimit)
#     row.append(S)
#     I = quad(Schwarz, lowerlimit, upperlimit, args=(U_10, h))[0]
#     row.append(I)
#     I = quad(Gong,lowerlimit, upperlimit, args=(U_10, SST, h))[0]
#     row.append(I)
#
#     S = 0
#     lowerlimit = max(0.38,r802d(3, h))
#     upperlimit = min(17, r802d(25, h))
#     for i in range(16):
#         if Messgrössen[i][0] >= lowerlimit and Messgrössen[i][1] <= upperlimit:
#             S += float(row[k + i])
#         elif Messgrössen[i][0] <= lowerlimit and Messgrössen[i][1] >= lowerlimit:
#             S += float(row[k + i]) * ((Messgrössen[i][1] - lowerlimit) / (Messgrössen[i][1] - Messgrössen[i][0]))
#         elif Messgrössen[i][0] <= upperlimit and Messgrössen[i][1] >= upperlimit:
#             S += float(row[k + i]) * ((upperlimit - Messgrössen[i][0]) / (Messgrössen[i][1] - Messgrössen[i][0]))
#
#     row.append(lowerlimit)
#     row.append(upperlimit)
#     row.append(S)
#     I = quad(Schwarz, lowerlimit, upperlimit, args=(U_10,h))[0]
#     row.append(I)
#
#
#     S = 0
#     lowerlimit = max(0.38, r802d(0.07, h))
#     upperlimit = min(17, r802d(20, h))
#     for i in range(16):
#         if Messgrössen[i][0] >= lowerlimit and Messgrössen[i][1] <= upperlimit:
#             S += float(row[k + i])
#         elif Messgrössen[i][0] <= lowerlimit and Messgrössen[i][1] >= lowerlimit:
#             S += float(row[k + i]) * ((Messgrössen[i][1] - lowerlimit) / (Messgrössen[i][1] - Messgrössen[i][0]))
#         elif Messgrössen[i][0] <= upperlimit and Messgrössen[i][1] >= upperlimit:
#             S += float(row[k + i]) * ((upperlimit - Messgrössen[i][0]) / (Messgrössen[i][1] - Messgrössen[i][0]))
#
#
#     row.append(lowerlimit)
#     row.append(upperlimit)
#     row.append(S)
#     I = quad(Gong, lowerlimit, upperlimit, args=(U_10,SST,h))[0]
#     row.append(I)
#
#     S = 0
#     lowerlimit = max(0.38, 0.5)
#     upperlimit = min(17,14)
#     for i in range(16):
#         if Messgrössen[i][0] >= lowerlimit and Messgrössen[i][1] <= upperlimit:
#             S += float(row[k + i])
#         elif Messgrössen[i][0] <= lowerlimit and Messgrössen[i][1] >= lowerlimit:
#             S += float(row[k + i]) * ((Messgrössen[i][1] - lowerlimit) / (Messgrössen[i][1] - Messgrössen[i][0]))
#         elif Messgrössen[i][0] <= upperlimit and Messgrössen[i][1] >= upperlimit:
#             S += float(row[k + i]) * ((upperlimit - Messgrössen[i][0]) / (Messgrössen[i][1] - Messgrössen[i][0]))
#     row.append(lowerlimit)
#     row.append(upperlimit)
#     row.append(S)
#     I = quad(Andreas, lowerlimit, upperlimit, args=(U_10,))[0]
#     row.append(I)
#
#
#
# with open(newfile, mode='w', newline='') as resultate:
#     resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     resultatewriter.writerow(header)
#     for row in Data:
#         resultatewriter.writerow(row)

# for row in Data:
#     for i in range(16):
#         row[k+i] = float(row[k+i])*1000000
#
#     row[40] = float(row[40])*1000000
#
# with open(newfile, mode='w', newline='') as resultate:
#     resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for row in Data:
#         resultatewriter.writerow(row)
#
#
#





# for entry in size:
#     Newdata = []
#     for n in range(391):
#         Newdata.append(entry)
#
#     with open(newfile, mode='a', newline='') as resultate:
#         resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         for row in Newdata:
#             resultatewriter.writerow(row)
#
#

# b = 0
# Newdata = []
# for Month in range(3):
#     for Day in range(31):
#         for Hour in range(24):
#             b = 0
#             for row in Data:
#                 if row[1:4] ==[str(Month+7),str(Day),str(Hour)]:
#                     Newdata.append(row)
#                     b = 1
#                     break
#
#             if b ==0:
#                 x = []
#                 x.append(Month+7+(Day/31)+(Hour/(31*24)))
#                 x.append(Month+7)
#                 x.append(Day)
#                 x.append(Hour)
#                 for k in range(19):
#                     x.append(0)
#
#                 Newdata.append(x)
#
# with open(newfile, mode='a', newline='') as resultate:
#     resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for row in Newdata:
#         resultatewriter.writerow(row)
#
#
# Timestamps = []
# for row in Data:
#     x=[]
#     if row[0]=="Month":
#          continue
#     x.append(float(row[0])+(float(row[1])/31)+(float(row[2])/(31*24)))
#     for entry in row:
#         x.append(entry)
#     Timestamps.append(x)
#
# print(Timestamps)
# with open(newfile, mode='a', newline='') as resultate:
#     resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for row in Timestamps:
#         resultatewriter.writerow(row)





# for row in Data:
#     x=[]
#     if row[0]=="Month":
#         continue
#     for i in range(16):
#         row[3+i] = float(row[3+i])/(math.log10(Messgrössen[i][1])-math.log10(Messgrössen[i][0]))
#
# print(Data)
# with open(newfile, mode='a', newline='') as resultate:
#     resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for row in Data:
#         resultatewriter.writerow(row)



#
# Mittel = []
# for i in range(19):
#     Mittel.append(0)
#
# n=0
# for row in Data:
#     n+=1
#     if row[0]=="Month":
#         continue
#     print(row)
#     for i in range(19):
#         Mittel[i]+=float(row[3+i])
#
# print(n)
# print(Mittel)
# for q in range(len(Mittel)):
#     Mittel[q] = (Mittel[q]/n)
#
# print(Mittel)
# with open(newfile, mode='a', newline='') as resultate:
#     resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     resultatewriter.writerow(Mittel)



# Sum = 0
#
# for row in Data:
#     Sum = 0
#     print(row[0])
#     if row[0]=="Timecodes":
#         continue
#
#     for i in range(16):
#         Sum+=float(row[4+i])
#     row.append(Sum)
#
#
# print(Data)
# with open(newfile, mode='a', newline='') as resultate:
#     resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for row in Data:
#         resultatewriter.writerow(row)







