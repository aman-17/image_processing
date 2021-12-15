import cv2, glob, os

def descale():
    images = []
    #BoundingboxDataset/*.jpg
    #CamouflageDataset/*.png
    for img in glob.glob("BoundingboxQuarter/*"):
        img_names = os.path.basename(img).split(".")[0]
        image= cv2.imread(img)
        images.append(image)
 
        #img = cv2.imread('high.jpg', cv2.IMREAD_UNCHANGED)
        
        print('Original Dimensions : ', image.shape)
        
        scale_percent = 40 # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        
        print('Resized Dimensions : ',resized.shape)
        
        cv2.imwrite(img_names+"_descale.jpg", resized)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

descale()