import os
import cv2
'''
get merged result and draw Bounding-Box
'''
labelpath = 'C:\\Users\\Hust\\Desktop\\pipeline\\result\\test\\'
class_dir = os.listdir(labelpath)
# f = open(labelpath+class_dir)
# a = labelpath + class_dir
# print(a)
# draw_coord = open('draw_coord.txt', 'w')
classcoord = []
for labelnames in class_dir:
    # print(labelpath+names)
    (name,ext) = os.path.splitext(labelnames)
    label = labelpath + labelnames
    f = open(label, 'r')
    all_coord = f.readlines()
    f.close()
    if all_coord == []:
        print(name, "is None")
        pass
    # classcoord = []
    # print(all_coord)
    for coord in all_coord:
        # classcoord = []
        # print(coord)
        # print(type(coord))
        # print(coord.split(' '))
        classname = name
        # x = float(coord.split(' ')[2])
        # y = float(coord.split(' ')[3])
        # w = float(coord.split(' ')[4])
        # h = float(coord.split(' ')[5])
        x1 = float(coord.split(' ')[2])
        y1 = float(coord.split(' ')[3])
        x2 = float(coord.split(' ')[4])
        y2 = float(coord.split(' ')[5])
        # w = float(coord.split(' ')[2])
        # h = float(coord.split(' ')[3])
        # x = float(coord.split(' ')[4])
        # y = float(coord.split(' ')[5])
        # x1 = int(x - w/2.0)
        # y1 = int(y - h/2.0)
        # w = int(w)
        # h = int(h)
        # x2 = int(x + w/2.0)
        # y2 = int(y + h/2.0)
        classcoord.append(x1)
        classcoord.append(y1)
        classcoord.append(x2)
        classcoord.append(y2)
        # classcoord.append(w)
        # classcoord.append(h)
        classcoord.append(classname)
        # classcoord.append(coord)
        # draw_coord.write("%s\n"%classcoord[0])
    # print(type(classcoord[0]))
    # draw_coord.write(classcoord)
# draw_coord.close()
# print(classcoord)
# print(len(classcoord))
img = cv2.imread(r'C:\Users\Hust\Desktop\pipeline\example\images\P0340.png')
color_dict = {"baseball-diamond":(0,0,0),"basketball-court":(0,0,0),"bridge":(0,0,0),"ground-track-field":(0,0,0),\
    "harbor":(0,0,0),"helicopter":(0,0,0),"large-vehicle":(0,255,255),"plane":(0,0,0),\
        "roundabout":(0,0,0),"ship":(0,255,0),"small-vehicle":(125,5,125),"soccer-ball-field":(0,0,0),\
            "storage-tank":(0,0,0),"swimming-pool":(0,0,0),"tennis-court":(0,0,0)}
for i in range(0, len(classcoord),5):
    # print(i)
    x1 = int(classcoord[i])
    y1 = int(classcoord[i+1])
    x2 = int(classcoord[i+2])
    y2 = int(classcoord[i+3])
    # w = classcoord[i+2]
    # h = classcoord[i+3]
    name = classcoord[i+4]
    # name_index = int(name)
    # print(color_dict[name])
    # print(name_index)
    # print(type(name_index))
    # print(x1,y1,w,h,name)
    # print(type(x1),type(name))
    img = cv2.rectangle(img,(x1,y1),(x2,y2),color=color_dict[name],thickness=2)
    img = cv2.putText(img,name,(x1,y1-5),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0,125,180))
    # cv2.imshow('image',img)
    # cv2.imwrite('result.png',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
cv2.imshow('image',img)
cv2.imwrite('result.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

        
        
