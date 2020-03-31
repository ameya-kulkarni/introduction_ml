con=open("/Users/gunnvantsaini/Downloads/yolov3-master/data/custom/train.txt","a")
for i in range(1,301):
    con.write(f"data/custom/images/{i}.jpeg"+"\n")
con.close()
con=open("/Users/gunnvantsaini/Downloads/yolov3-master/data/custom/test.txt","a")
for i in range(301,334):
    con.write(f"data/custom/images/{i}.jpeg"+"\n")
con.close()