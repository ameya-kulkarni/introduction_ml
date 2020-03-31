import os
from PIL import Image
path_labels="/Users/gunnvantsaini/OneDrive/project_codes/content/dl_basics/sony/data/guns-object-detection/Labels"
path_imgs="/Users/gunnvantsaini/OneDrive/project_codes/content/dl_basics/sony/data/guns-object-detection/Images"
path_new="/Users/gunnvantsaini/OneDrive/project_codes/content/dl_basics/sony/data/guns-object-detection/NewLabels"
def get_names(path_labels):
    return os.listdir(path_labels)
def read_file(name,path_labels):
    path_to_name=os.path.join(path_labels,name)
    con=open(path_to_name,'r')
    data=con.readlines()
    return data 
def process_file(name,data,path_imgs):
    image_name=name.split(".")[0]+".jpeg"
    path_img=os.path.join(path_imgs,image_name)
    img=Image.open(path_img)
    H=img.height 
    W=img.width
    coords=[]
    for d in data[1:]:
        cls=0
        xmin,ymin,xmax,ymax=d.split(" ")
        cx=(float(xmin)+float(xmax))/2
        cx=cx/W
        cy=(float(ymin)+float(ymax))/2
        cy=cy/H
        w= (float(xmax)-float(xmin))/W
        h=(float(ymax)-float(ymin))/H
        element=str(cls)+" "+str(cx)+" "+str(cy)+" "+str(w)+" "+str(h)
        coords.append(element)
    return coords
def write_files(preproc,name,path_new):
    path_write=os.path.join(path_new,name)
    con=open(path_write,"a")
    for item in preproc:
        con.write(item+"\n")
        print(f"Writting {name}")
    con.close()
names=get_names(path_labels)
Data=[read_file(name,path_labels) for name in names]
out=[process_file(name,data,path_imgs) for name,data in zip(names,Data)]
for p,n in zip(out,names):
    write_files(p,n,path_new)
