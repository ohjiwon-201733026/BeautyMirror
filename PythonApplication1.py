import cv2
import numpy as np

src=cv2.imread("a.png.png",cv2.IMREAD_COLOR)
hsv=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
height, width, channel=hsv.shape
cv2.imshow("h",h)
cv2.imshow("s",s)
cv2.imshow("v",v)

h=cv2.inRange(h,8,20)
orange=cv2.bitwise_and(hsv,hsv,mask=h)
#orange=cv2.cvtColor(orange, cv2_COLOR_HSV2BGR)

#def tone(var inc):
lst=[0,0,0,0,0,0,0,0,0,0,0,0] 
for i in range (0,width-1):
    for j in range(0,height-1):
        H=orange.item(j,i,0)
        S=orange.item(j,i,1)
        V=orange.item(j,i,2)

        x=(H==0)and (S==0)and (V==0)
        if(x==False):
          if(S<=64):
            if(V>192):
                lst[0]+=1
            elif (V>140 and V<=192):
                lst[1]+=1
            elif( V>89 and V<=140):
                lst[2]+=1

            else: lst[3]+=1

          elif (S>64 and S<=128):
              if(V>=192):
                  lst[4]+=1
              elif(V>140 and V<=192):
                  lst[5]+=1
              elif(V>89 and V<=140):
                  lst[6]+=1
              else: 
                  lst[7]+=1
              
          elif(S>128 and S<=192):
               if(V>166):
                   lst[8]+=1
               elif(V>115 and V<=166):
                   lst[9]+=1
               else: lst[10]+=1

          else:
              lst[11]+=1

for i in range(0,11):
    print(lst[i])

max=0  # max의index
for i in range(0,11):
    if(lst[i]>=lst[max]):
        max=i
    else: max=max
    
print(max)

if (max==0): print("Pale tone") 
elif(max==1): print("Light grayish tone")
elif(max==2): print("Grayish tone")
elif(max==3):print("Dark Grayish tone")
elif(max==4):print("Light tone")
elif(max==5):print("Soft tone")
elif(max==6):print("Dull tone")
elif(max==7):print("Dark tone")
elif(max==8):print("Bright tone")
elif(max==9):print("Strong tone")
elif(max==10):print("Deep tone")
else: print("Vivid tone")
    



cv2.imshow("orange",orange)
cv2.waitKey(0)
cv2.destroyAllWindows()