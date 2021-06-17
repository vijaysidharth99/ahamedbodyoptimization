import gmsh
import math
import os
import sys
import numpy as np
gmsh.initialize()
gmsh.model.add("m1")
LA      = 1044      #Body length total
LD      = LA*15     #Domain Length
HD      = LA*3.5    #Domain Height
R       = 100       #Fillet radius
GC      = 50        #ground clearance
HA      = 288       #body height total
l       = 222       #slant height rear
theta   = 35        #slant angle degres rear
DIL     = 200       #diffuser length
DIH     = 30        #diffuser height
FL      = 2.5*LA    #Front distance
d       = 200
lcos    = l*math.cos((theta*math.pi)/180)
lsin    = l*math.sin((theta*math.pi)/180)
k = d/1.2
param   = 0
numofnodes = 100
gmsh.model.occ.addPoint(FL+R                    ,GC                     ,0,0,1)
gmsh.model.occ.addPoint(FL+R*(1-math.cos(math.pi/4)),GC + R*(1-(math.sin(math.pi/4))),0,0,2)
gmsh.model.occ.addPoint(FL                      ,GC+R                   ,0,0,3)
gmsh.model.occ.addPoint(FL                      ,GC+HA-R                ,0,0,4)
gmsh.model.occ.addPoint(FL+R*(1-math.cos(math.pi/4)),GC + HA - R*(1 - (math.sin(math.pi/4))),0,0,5)
gmsh.model.occ.addPoint(FL+R                    ,GC+HA                  ,0,0,6)
gmsh.model.occ.addPoint(FL+LA-l*math.cos((theta*math.pi)/180) ,GC+HA                  ,0,0,7)
gmsh.model.occ.addPoint(FL+LA                   ,GC+HA-l*math.sin((theta*math.pi)/180),0,0,8)
gmsh.model.occ.addPoint(FL+LA                   ,GC+DIH                 ,0,0,9)
gmsh.model.occ.addPoint(FL+LA-DIL               ,GC                     ,0,0,10)

gmsh.model.occ.addPoint(FL+R                    ,GC+R                   ,0,0,101)
gmsh.model.occ.addPoint(FL+R                    ,GC+HA-R                ,0,0,102)

gmsh.model.occ.addPoint(FL+R    ,0                    ,0,0,11)
gmsh.model.occ.addPoint(FL-d    ,0                    ,0,0,12)
gmsh.model.occ.addPoint(FL-d    ,GC+R                 ,0,0,13)
gmsh.model.occ.addPoint(FL-d    ,GC+HA-R              ,0,0,14)
gmsh.model.occ.addPoint(FL-d    ,GC+HA+d              ,0,0,15)
gmsh.model.occ.addPoint(FL+R    ,GC+HA+d              ,0,0,16)
gmsh.model.occ.addPoint(FL+LA-lcos+ k  ,GC+HA+d       ,0,0,17)
gmsh.model.occ.addPoint(FL+LA+k    ,GC+HA+d-lsin      ,0,0,18)
gmsh.model.occ.addPoint(FL+LA+k    ,0                 ,0,0,19)
gmsh.model.occ.addPoint(FL+LA-DIL    ,0               ,0,0,20)


gmsh.model.occ.addPoint(0           ,0                    ,0,0,112)
gmsh.model.occ.addPoint(0           ,GC+R                 ,0,0,113)
gmsh.model.occ.addPoint(0           ,GC+HA-R              ,0,0,114)
gmsh.model.occ.addPoint(0           ,GC+HA+d              ,0,0,115)

gmsh.model.occ.addPoint(0           ,HD                   ,0,0,120)
gmsh.model.occ.addPoint(FL-d          ,HD                   ,0,0,121)

gmsh.model.occ.addPoint(FL+R        ,HD                   ,0,0,116)
gmsh.model.occ.addPoint(FL+LA-lcos+ k,HD                  ,0,0,117)
gmsh.model.occ.addPoint(FL+LA+k+param,HD                  ,0,0,118)

gmsh.model.occ.addPoint(LD           ,HD                  ,0,0,122)
gmsh.model.occ.addPoint(LD           ,GC+HA+d-lsin        ,0,0,123)

gmsh.model.occ.addPoint(LD           ,0                   ,0,0,119)




gmsh.model.occ.addCircleArc(1,101,2,1)
gmsh.model.occ.addCircleArc(2,101,3,2)
gmsh.model.occ.addLine(3,4,3)
gmsh.model.occ.addCircleArc(4,102,5,4)
gmsh.model.occ.addCircleArc(5,102,6,5)
gmsh.model.occ.addLine(6,7,6)
gmsh.model.occ.addLine(7,8,7)
gmsh.model.occ.addLine(8,9,8)
#gmsh.model.occ.addLine(9,10,9)#diffuser
splinex1 = 3454 + 50#3504
splinex2 = 3454 + 150#3604
spliney1 = 50+20#70
spliney2 = 50#50
print(str(splinex1)+" "+str(splinex2)+" "+str(spliney1)+" "+str(spliney2))
gmsh.model.occ.addPoint(splinex1,spliney1,0,0,30)
gmsh.model.occ.addPoint(splinex2,spliney2,0,0,31)
gmsh.model.occ.addBezier([9,30,31,10],9)

gmsh.model.occ.addLine(10,1,10)

for i in range(1,11):
    gmsh.model.occ.addLine(i,i+10,i+200)

for i in range(11,20):
    gmsh.model.occ.addLine(i,i+1 ,i+300)
gmsh.model.occ.addLine(20,11,320)
for i in range(12,20):
    gmsh.model.occ.addLine(i,i+100 ,i+400)
for i in range(112,118):
    if(i == 115):
        continue
    gmsh.model.occ.addLine(i,i+1 ,i+400)

gmsh.model.occ.addLine(115,120,420)
gmsh.model.occ.addLine(121,120,421)
gmsh.model.occ.addLine(121,116,422)
gmsh.model.occ.addLine(118,122,423)
gmsh.model.occ.addLine(123,122,424)
gmsh.model.occ.addLine(123,119,425)
gmsh.model.occ.addLine(18,123,426)
gmsh.model.occ.addLine(15,121,427)


for i in range(1,10):
    gmsh.model.occ.addPlaneSurface([gmsh.model.occ.addCurveLoop([i,200+i,310+i,200+i+1])])
gmsh.model.occ.addPlaneSurface([gmsh.model.occ.addCurveLoop([10,210,320,201])])

for i in range(12,15):
     gmsh.model.occ.addPlaneSurface([gmsh.model.occ.addCurveLoop([300+i,400+i,500+i,400+i+1])])
gmsh.model.occ.addPlaneSurface([gmsh.model.occ.addCurveLoop([415,420,421,427])])
gmsh.model.occ.addPlaneSurface([gmsh.model.occ.addCurveLoop([315,427,422,416])])
gmsh.model.occ.addPlaneSurface([gmsh.model.occ.addCurveLoop([418,423,424,426])])
gmsh.model.occ.addPlaneSurface([gmsh.model.occ.addCurveLoop([426,425,419,318])])
gmsh.model.occ.addPlaneSurface([gmsh.model.occ.addCurveLoop([316,416,516,417])])
gmsh.model.occ.addPlaneSurface([gmsh.model.occ.addCurveLoop([317,417,517,418])])
gmsh.model.occ.synchronize()

numofnodes_inner = 70
prog_inner = 1

group_Left_horizontal = [412,413,414,415,421]
group_Right_horizontal = [423,426,419]
group_Top_vertical = [420,427,416,417,418,424]

group_LB1_vertical = [4,314,514]
group_LB2_vertical = [3,313,513]
group_LB3_vertical = [2,312,512]

group_RB1_vertical = [8,318,425]

group_CB1_horizontal = [1,311]
group_CB2_horizontal = [10,320]
group_CB3_horizontal = [9,319]

group_CT1_horizontal = [5,315,422]
group_CT2_horizontal =[6,316,516]
group_CT3_horizontal =[7,317,517]


for i in range(1,11): #inner loop
    gmsh.model.mesh.setTransfiniteCurve(200+i,80,"Progression",1.05)

for i in group_Left_horizontal:
    gmsh.model.mesh.setTransfiniteCurve(i,50,"Progression",1.05)
for i in group_Right_horizontal:
    gmsh.model.mesh.setTransfiniteCurve(i,70,"Progression",1.07)
for i in group_CB1_horizontal:
    gmsh.model.mesh.setTransfiniteCurve(i,numofnodes_inner,"Progression",prog_inner)
for i in group_CB2_horizontal:
    gmsh.model.mesh.setTransfiniteCurve(i,450,"Progression",prog_inner)
for i in group_CB3_horizontal:
    gmsh.model.mesh.setTransfiniteCurve(i,200,"Progression",prog_inner)
for i in group_CT1_horizontal:
    gmsh.model.mesh.setTransfiniteCurve(i,100,"Progression",prog_inner)
for i in group_CT2_horizontal:
    gmsh.model.mesh.setTransfiniteCurve(i,300,"Progression",)
for i in group_CT3_horizontal:
    gmsh.model.mesh.setTransfiniteCurve(i,40,"Progression",1.05)
for i in group_Top_vertical:
    gmsh.model.mesh.setTransfiniteCurve(i,60,"Progression",1.03)
for i in group_LB1_vertical:
    gmsh.model.mesh.setTransfiniteCurve(i,numofnodes_inner,"Progression",prog_inner)
for i in group_LB2_vertical:
    gmsh.model.mesh.setTransfiniteCurve(i,numofnodes_inner,"Progression",prog_inner)
for i in group_LB3_vertical:
    gmsh.model.mesh.setTransfiniteCurve(i,numofnodes_inner,"Progression",prog_inner)
for i in group_RB1_vertical:
    gmsh.model.mesh.setTransfiniteCurve(i,numofnodes_inner,"Progression",prog_inner)

for i in range(1,10):
    gmsh.model.mesh.setTransfiniteSurface(i,"Left",[ i,10+i,10+1+i,i+1])
gmsh.model.mesh.setTransfiniteSurface(10,"Left",[ 10,20,11,1])

gmsh.model.mesh.setTransfiniteSurface(11,"Left",[ 12,112,113,13])
gmsh.model.mesh.setTransfiniteSurface(12,"Left",[ 13,113,114,14])
gmsh.model.mesh.setTransfiniteSurface(13,"Left",[ 14,114,115,15])
gmsh.model.mesh.setTransfiniteSurface(14,"Left",[ 15,115,120,121])
gmsh.model.mesh.setTransfiniteSurface(15,"Left",[ 15,121,116,16])
gmsh.model.mesh.setTransfiniteSurface(18,"Left",[ 16,116,117,17])
gmsh.model.mesh.setTransfiniteSurface(19,"Left",[ 17,117,118,18])
gmsh.model.mesh.setTransfiniteSurface(16,"Left",[ 18,118,122,123])
gmsh.model.mesh.setTransfiniteSurface(17,"Left",[ 18,123,119,19])
gmsh.model.addPhysicalGroup(1, [512,513,514,420], 1)
gmsh.model.setPhysicalName(1, 1, "Inlet")

gmsh.model.addPhysicalGroup(1, [425,424], 2)
gmsh.model.setPhysicalName(1, 2, "Outlet")

gmsh.model.addPhysicalGroup(1, [421,422,423,516,517], 3)
gmsh.model.setPhysicalName(1, 3, "Top")

gmsh.model.addPhysicalGroup(1, [412,311,320,319,419], 4)
gmsh.model.setPhysicalName(1, 4, "Bottom")

gmsh.model.addPhysicalGroup(1, [1,2,3,4,5,6,7,8,9,10], 5)
gmsh.model.setPhysicalName(1, 5, "AhamedBody")
gmsh.option.setNumber("Mesh.RecombineAll", 1)
gmsh.model.mesh.generate()
gmsh.option.setNumber("Mesh.SaveAll",1)
gmsh.write("unique.su2")
if '-nopopup' not in sys.argv:
   gmsh.fltk.run()
gmsh.finalize()





def nodeNumbers(lines,coords):#file and 
    broken_String = lines[1].split(" ")
    num_of_elements = int(broken_String[1])
    linenum = 3 + num_of_elements
    nodenum = []
    print(str(num_of_elements)+ " "+ str(linenum))
    for i in range(linenum,3*linenum):
        broken_String = lines[i].split(" ")

        if (len(broken_String) < 3):
            print("Istopeed at"+" "+str(i))
            break
        x = broken_String[0]
        y = broken_String[1]
        n = broken_String[2]
        for k in [0,2,4,6]:
            if(coords[k] == x and coords[k+1] == y):
                print("Ifound"+ " " +coords[k]+" "+coords[k+1])
                print(k)
                nodenum.append(int(n))
                print(n)
    return nodenum
def determine(list1,num):
    for i in range(0,len(nodeNum)):##to be changed as number of coords t be removed increases
        if list1[i] <= num:
            num =  num -1
    return num
os.system("cd Desktop")
# os.system("cd mshfiles")
command = "ren *.su2 *.txt"
os.system(command)
f = open('unique.txt', 'r') # 'r' = read
lines = f.readlines()
broken_String = lines[1].split(" ")
num_of_elements = int(broken_String[1])
broken_String = lines[num_of_elements+2].split(" ")
number_of_nodes = int(broken_String[1])
linenum = 3 + num_of_elements
nodeNum = nodeNumbers(lines,[str(splinex1), str(spliney1), str(splinex2), str(spliney2),"2710","238","2710","150"])#x,y,x1,y1,x2,y2.......
nodeNum = sorted(nodeNum)
print(nodeNum[0])
print(nodeNum[1])
print(nodeNum[2])
print(nodeNum[3])
writingfile = open('newfile.txt','w')

##########################################################
writingfile.write(lines[0])
writingfile.write(lines[1])
#######################Elements numbering
for i in range(2, num_of_elements+2): #till num_of_elements + 2
    broken_String = lines[i].split(" ")
    a = int(broken_String[1])
    b = int(broken_String[2])
    c = int(broken_String[3])
    d = int(broken_String[4])
    #print(str(a)+" "+str(b)+" "+str(c)+" "+str(d))
    writingfile.write(broken_String[0]+" "+ str(determine(nodeNum,a))+" "+str(determine(nodeNum,b))+" "+str(determine(nodeNum,c))+" "+str(determine(nodeNum,d))+" "+broken_String[5])

broken_String = lines[num_of_elements+2].split(" ")
number_of_nodes = int(broken_String[1])
writingfile.write(broken_String[0]+" "+str(int(broken_String[1])-len(nodeNum))+'\n')
finding = 0
###################Node area
for i in range(num_of_elements+3, num_of_elements+3+number_of_nodes): #till num_of_elements + 2
    broken_String = lines[i].split(" ")
    a = int(broken_String[2])
    for j in range(0,len(nodeNum)):#to be chaged as the number of nodes to be removed increases
        if(nodeNum[j] == a):
            finding = 1
            break
    if(finding == 1):
        finding = 0
        continue
    writingfile.write(broken_String[0]+" "+ broken_String[1] + " " + str(determine(nodeNum,a)) + '\n')

##################Boundarycodition area
for i in range(num_of_elements+3+number_of_nodes,len(lines)):
    broken_String = lines[i].split(" ")
    if(len(broken_String) == 2):
        writingfile.write(lines[i])
    else:
        a = int(broken_String[1])
        b = int(broken_String[2])
        writingfile.write(broken_String[0]+" "+str(determine(nodeNum,a))+" "+str(determine(nodeNum,b))+ '\n')

writingfile.close()
command = "ren *.txt *.su2"
os.system(command)
f.close()
