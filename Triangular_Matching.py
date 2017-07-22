# pyFingerprint-Verification
#Fingerprint verification based on triangular matching algorithm implemented using Python 3.5
# Fingerprint Verification Based on Triangular Matching
# Triangular Matching Module
# Developed by Shreya Sonali & Abhijit Raj Narayan Singh.

from math import *

matchedMinutiae = []
refList = []
testList = []
matchedCount = 0

def GetNextMinutiae(refList):
    i = int(input())
    xy = refList[i]
    return xy

def GetNextTestMinutiae(ref):
    for i in range(len(testList)):
        if ref == xy:
            xy1 = xy
    return xy1

def LineLength(ref1, ref2, test1, test2):
    refLen = sqrt((ref1[0]-ref2[0])**2 + (ref1[1]-ref2[1])**2)
    testLen = sqrt((test1[0]-test2[0])**2 + (test1[1]-test2[1])**2)
    diffLen = abs(refLen - testLen)
    return diffLen

def ComputeAngle(ref1, ref2, test1, test2):
    m1 = ((ref1[1]-ref2[1])/(ref1[0]-ref2[0]))
    m2 = ((test1[1]-test2[1])/(test1[0]-test2[0]))
    angle = atan(abs((m1-m2)/(1+m1*m2)))
    return angle

def AddMatchedMinutiae(ref1, test1, ref2, test2):
    if ref1 == test1:
        matchedMinutiae.append(ref1)
    if ref2 == test2:
        matchedMinutiae.append(ref2)

def GetNextMinutiaePair(ref1, test1, ref2, test2):
    A = y0-(m1*(x0-ref1[0])+ref1[1])
    B = y-(m2*(x-test1[0])+test1[1])
    for i in range(len(refList)):
        R = refList[i]
        y0 = R[1]
        x0 = R[0]
        if A == 0:
            RR = R
    for i in range(len(testList)):
        T = testList[i]
        y = T[1]
        x = T[0]
        if B == 0:
            TT = T
    return (RR, TT)

def GetNextCloseMinutiae(ref1, ref2):
    for i in range(len(refList)):
        if refList[i]!=ref1 && refList[i]!=ref2:
            ref3 = refList[i]
            refLenL = sqrt((ref1[0]-ref3[0])**2 + (ref1[1]-ref3[1])**2)
            refLenM = sqrt((ref2[0]-ref3[0])**2 + (ref2[1]-ref3[1])**2)
            if refLenM < refLenL:
                return ref3
            else:
                return 0

def ComputeTestCoordinates(ref3, ref1, test1, ref2, test2):
    A = ((test1[0]-test2[0])*(ref1[0]-ref2[0])+(test1[1]-test2[1])*(ref2[1]-ref2[1]))/((ref1[0]-ref2[0])**2 + (ref1[1]-ref2[1])**2)
    B = ((test1[0]-test2[0])*(ref1[0]-ref2[0])-(test1[1]-test2[1])*(ref2[1]-ref2[1]))/((ref1[0]-ref2[0])**2 + (ref1[1]-ref2[1])**2)
    GX = test1[0] - A*ref1[0] - B*ref1[1]
    GY = test1[1] - A*ref1[1] - B*ref1[0]
    X = A*ref3[0]+B*ref3[1]+GX
    Y = -B*ref3[0]+A*ref3[1]+GY
    test0 = (X,Y)
    return test0

def NumberOfMatchedMinutiae():
    for i in range(len(refList)):
        for j in range(len(testList)):
            if refList[i]==testList[j]:
                matchedCount += 1
    return matchedCount

def MaxDistance(ref1, ref2, test1, test2):
    refLen = sqrt((ref1[0]-ref2[0])**2 + (ref1[1]-ref2[1])**2)
    testLen = sqrt((test1[0]-test2[0])**2 + (test1[1]-test2[1])**2)
    diffLen = abs(refLen - testLen)
    if (diffLen/refLen)*100 <= 10:
        print("This much Deformation is Allowed")
    else:
        print("Too much Deformation, Please reuse the Test Image")

def MaxAngle():
    ang = ComputeAngle(ref1, ref2, test1, test2)
    if (ang*180)/pi <= 20:
        print("This much Deformation is Allowed")
    else:
        print("Too much Deformation, Please reuse the Test Image")

def MinimumMatch():
    matchedMinutiae = NumberOfMatchedMinutiae()
    if matchedMinutiae >= 14:
        print(" VERIFIED IDENTITY! ")
    else:
        print(" NOT VERIFIED! ")



ref1 = GetNextMinutiae()
ref2 = GetNextMinutiae()

test1 = GetNextTestMinutiae(ref1)
test2 = GetNextTestMinutiae(ref2)

if (test2 != null):
    dist = LineLength(ref1, ref2, test1, test2)
    angle = ComputeAngle(ref1, ref2, test1, test2)







        
    
    
    
                
            
        
    
    
    
    
    




    
    
            
    
    
    
