import cv2
from glob import glob
import os
#from darknet import performDetect
import configparser
import argparse
import json, time, math
import numpy as np
import matplotlib.pyplot as plt

def get_slice_coordinates(coordinates):
        coords = map(round, coordinates)
        #print(coords)
        x ,y, w, h = map(int, coords)
        xmin, ymin, xmax, ymax = x - w/2, y - h/2, x + w/2, y + h/2
        return [xmin, ymin, xmax, ymax]

def read_path():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "groundtruth_annotations")
    annotation_list=[]
    for i in glob(file_path+"/*.txt"):
        with open(i) as f:
            content=f.read()
            content_list=content.split()
            content_list=" ".join(content_list[:0] + content_list[0+1 :])
            #print(content_list)
            annotation_list.append(get_slice_coordinates(map(float,content_list.split())))
            #print(get_slice_coordinates(map(float,content_list.split())))
    return annotation_list

def new_slice():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "quarterfull")
    image_path = os.path.join(script_dir, "BoundingboxQuarter")
    destination_path = os.path.join(script_dir,"002")
    annotation_list=[]
    for i in glob(file_path+"/*.txt"):
        txt_names = os.path.basename(i).split(".")[0]
        
        with open(i) as f:
           
            data = f.readlines()
            f.close()
            img = cv2.imread(image_path+"/"+txt_names+".png")
            dh, dw, _ = img.shape


            for dt in data:

                _, x, y, w, h = map(float, dt.split(' '))

                l = int((x - w / 2) * dw)
                r = int((x + w / 2) * dw)
                t = int((y - h / 2) * dh)
                b = int((y + h / 2) * dh)
                
                if l < 0:
                    l = 0
                if r > dw - 1:
                    r = dw - 1
                if t < 0:
                    t = 0
                if b > dh - 1:
                    b = dh - 1
        print(l,t,r,b)
        with open(destination_path+"/"+txt_names+".txt", 'w') as f:
            f.write(str(l)+" "+str(t)+" "+str(b)+" "+str(r))
            
        #cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 1)
        #plt.imshow(img)

        #plt.show()
        #time.sleep(1)
    return
    #return [l,t,r,b]

def rmse_h():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "output_txt_yolo")
    json_path = os.path.join(script_dir, "yolo-batch-inference-json")
    yolo_h = []
    ground_truth_h = []
    for i in glob(file_path+"/*.txt"):
        txt_names = os.path.basename(i).split(".")[0]
        
        with open(i) as f:
           
            txt_data = f.readlines()
            #print(txt_data)
            f = open(json_path+"/"+txt_names+".json",)
            json_data = json.load(f)
            #print(txt_names)
            json_data1 = json_data["coin"][0][1][2]
            yolo_h.append(json_data1)
            txt_data_array = txt_data[0].split()[3]
            ground_truth_h.append(int(txt_data_array))
            f.close()

    mse_h = np.square(np.subtract(ground_truth_h, yolo_h)).mean()
    rmse_h = math.sqrt(mse_h)
    print("Root Mean Square Error of height:\n")

    return rmse_h

def rmse_txt_h():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "slice_dataset")
    file_path2 = os.path.join(script_dir, "slice_hough")
    #json_path = os.path.join(script_dir, "yolo-batch-inference-json")
    yolo_h = []
    ground_truth_h = []
    for i in glob(file_path+"/*.txt"):
        txt_names = os.path.basename(i).split(".")[0]
        
        with open(i) as f:
           
            txt_data = f.readlines()
            txt_data_array = txt_data[0].split()[3]
            #print(txt_data_array)
            yolo_h.append(int(txt_data_array))
            #print(yolo_h)
            f.close()

    for i in glob(file_path2+"/*.txt"):
        txt_names1 = os.path.basename(i).split(".")[0]
        
        with open(i) as f:
           
            txt_data1 = f.readlines()
            txt_data_array1 = txt_data1[0].split()[3]
            #print(txt_data_array1)
            ground_truth_h.append(int(txt_data_array1))
            #print(ground_truth_h)
            f.close()



    mse_h = np.square(np.subtract(ground_truth_h, yolo_h)).mean()
    rmse_h = math.sqrt(mse_h)
    print("Root Mean Square Error of height:\n")
    return rmse_h
    
def rmse_txt_w():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "slice_dataset")
    file_path2 = os.path.join(script_dir, "slice_hough")
    #json_path = os.path.join(script_dir, "yolo-batch-inference-json")
    yolo_h = []
    ground_truth_h = []
    for i in glob(file_path+"/*.txt"):
        txt_names = os.path.basename(i).split(".")[0]
        
        with open(i) as f:
           
            txt_data = f.readlines()
            txt_data_array = txt_data[0].split()[2]
            #print(txt_data_array)
            yolo_h.append(int(txt_data_array))
            #print(yolo_h)
            f.close()

    for i in glob(file_path2+"/*.txt"):
        txt_names1 = os.path.basename(i).split(".")[0]
        
        with open(i) as f:
           
            txt_data1 = f.readlines()
            txt_data_array1 = txt_data1[0].split()[2]
            ground_truth_h.append(int(txt_data_array1))
            f.close()



    mse_h = np.square(np.subtract(ground_truth_h, yolo_h)).mean()
    rmse_h = math.sqrt(mse_h)
    print("Root Mean Square Error of width:\n")
    return rmse_h

def rmse_w():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "output_txt_yolo")
    json_path = os.path.join(script_dir, "yolo-batch-inference-json")
    yolo_w = []
    ground_truth_w = []
    for i in glob(file_path+"/*.txt"):
        txt_names = os.path.basename(i).split(".")[0]
        
        with open(i) as f:
           
            txt_data = f.readlines()
            #print(txt_data)
            f = open(json_path+"/"+txt_names+".json",)
            json_data = json.load(f)
            #print(txt_names)
            json_data1 = json_data["coin"][0][1][3]
            yolo_w.append(json_data1)
            txt_data_array = txt_data[0].split()[2]
            ground_truth_w.append(int(txt_data_array))
            f.close()

    mse_w = np.square(np.subtract(ground_truth_w, yolo_w)).mean()
    rmse_w = math.sqrt(mse_w)
    print("Root Mean Square Error of width:\n")
    
    return rmse_w

if __name__ == '__main__':
    new_slice()


'''
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-data_dir", "--data_dir", required = True, help = 'Path to directory containing input images for detection')
    ap.add_argument("-target_dir", "--target_dir", required = True, help = 'Path to directory that stores the box detections drawn on the input images')
    ap.add_argument("-json_dir", "--json_dir", required = True, help = 'Path to directory that stores the output jsons containing the box coordinates')

    args = ap.parse_args()
    source_dir = args.data_dir
    target_dir = args.target_dir
    json_dir = args.json_dir

    for d in [target_dir, json_dir]:
        if not os.path.exists(d):
            os.makedirs(d)

    config = configparser.ConfigParser()
    config.read('config.ini')

    yolo_section = config["yolo"]

    weights_file = str(yolo_section["weights"])
    meta_data = str(yolo_section["meta_data"])
    classes = str(yolo_section["classes"])
    yolo_cfg = str(yolo_section["cfg_file"])
    libso = str(yolo_section["libso"])
    class_iou_threshold = float(yolo_section["class_iou_threshold"])
    
    validation_imgs = [file.split('/')[-1] for file in glob(source_dir + '/*.jpg')]
    print(len(validation_imgs), "images found.")

    validation_imgs_set = set(validation_imgs)
    
    #Compute what images have been processd until now
    processed_images_yolo_bb_set = set([file.split('/')[-1] for file in glob(target_dir + '/*.jpg')])
    processed_images_json_bb_set = set([file.split('/')[-1] for file in glob(json_dir + '/*.json')])

    #The intersection of these two sets correspond to complete processing set
    proceesed_file_set = processed_images_yolo_bb_set.intersection(processed_images_json_bb_set)
    print(len(proceesed_file_set), "Processed images found.")

    #Compute input folder set
    unprocessed_file_list = list(validation_imgs_set.difference(proceesed_file_set))
    print(len(unprocessed_file_list), "Number of images Processing in this batch")

    #Map the source dir name to all the list
    unprocessed_file_list = [os.path.join(source_dir,file_name) for file_name in unprocessed_file_list]
    print(unprocessed_file_list[0])


    for idx, img_path in enumerate(unprocessed_file_list):
        filename = img_path.split('/')[-1]
        print(idx + 1, filename)
        
        # img = cv2.imread(img_path, 0)
        # box_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        box_img = cv2.imread(img_path)
        filename = img_path.split('/')[-1]
        yolo_output = performDetect(imagePath = img_path, thresh= 0.25, configPath = yolo_cfg, weightPath = weights_file, metaPath= meta_data)
        print(yolo_output)
        yolo_output = [(i[0], [i[1], get_slice_coordinates(i[2])]) for i in yolo_output]
        
        keys = list(set([i[0] for i in yolo_output]))
        yolo_output_dict = {}
        for key in keys:
            value = [i[1] for i in yolo_output if i[0] == key]
            yolo_output_dict[key] = value
        
        
        for elem in yolo_output:
            class_name, c = elem
            conf, coords = c
            # print coords
            xmin, ymin, xmax, ymax = coords
            box_img = cv2.rectangle(box_img, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
            cv2.putText(box_img, class_name, (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (200,0,0), 3, lineType=cv2.LINE_AA)

        cv2.imwrite(os.path.join(target_dir, filename), box_img)
        json_path = os.path.join(json_dir, filename.split('.')[0] + '.json')
        with open(json_path, 'w') as json_file:
            json.dump(yolo_output_dict, json_file)
        
'''