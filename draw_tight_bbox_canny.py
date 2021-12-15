import cv2, os, json, argparse, numpy as np, pandas as pd
from glob import glob

def create_canvas(imgs, add_argument = False, debug = False):
	shapes = [img.shape[:2] for img in imgs]
	hts = [i[0] for i in shapes]
	wts = [i[1] for i in shapes]
	canvas_h, canvas_w = int(max(hts)), int(sum(wts))
	# print shapes
	# print canvas_h, canvas_w
	if debug:
		canvas_h = int(1.5*canvas_h)	
	
	if add_argument:
		additional_width = 5*(len(imgs) - 1)
		canvas = np.ones((canvas_h, canvas_w + additional_width), np.uint8)*255
		
	else:
		canvas = np.ones((canvas_h, canvas_w), np.uint8)*255
	
	w_start = 0
	for idx in range(len(imgs)):
		h = hts[idx]
		w = wts[idx]
		
		canvas[ : h, w_start : w_start + w ] = imgs[idx]
		seperator_line_start = w_start + w
		canvas[ : , seperator_line_start : seperator_line_start + 5 ] = 255
		
		w_start += w
		if add_argument:
			w_start += 5
	return canvas

def decide_contour(mean, std, mean_thresh = 100,std_thresh = 40):

    # 1. low mean is a dull image 
    # 2. low contrast but high mean means image is very bright
    #   more "edges" will be detected by canny throughout the image
    #   tight is safer, but not the best, after observation
    # 3. 
    
    # wide1 are wide2 are returned only for debugging purposes
    if mean >= mean_thresh and std <= std_thresh:
        # return "wide1"
        return "wide"
    elif mean < mean_thresh and std <= std_thresh:
        # return "wide2"
        return "wide"
    elif std > std_thresh:
        return "tight"


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--folder', '-folder', required = True, \
        help = "Path to input directory containing only the localized images of coins, as detected by YOLO")
    ap.add_argument('--out_dir', '-out_dir', required = True, \
        help = "Path to output directory where the contour maps, coin bounding box images and other debugging related images are stored")
    
    args = ap.parse_args()

    folder = args.folder
    out_dir = args.out_dir
    
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    imgs = sorted(glob(folder + '/*'))
    print(len(imgs), "images found")

    report_lines = []
    for idx, img_path in enumerate(imgs[:]):

        #try:
    
        filename = img_path.split('/')[-1].split('.')[0]
        print(idx + 1, filename)
        
        image = cv2.imread(img_path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        mean, std = image_gray.mean(), image_gray.std()

        def auto_canny(image, sigma=0.33):
            # compute the median of the single channel pixel intensities
            v = np.median(image)
            # apply automatic Canny edge detection using the computed median
            lower = int(max(0, (1.0 - sigma) * v))
            upper = int(min(255, (1.0 + sigma) * v))
            edged = cv2.Canny(image, lower, upper)
            # return the edged image
            return edged


        chosen_contour = decide_contour(mean, std)
        report_lines.append([filename, chosen_contour])
        # smoothing an image allows us to ignore much of the detail and instead focus on the actual structure.
        blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)
        # try changing above values as well

        wide = cv2.Canny(blurred, 10, 200)
        mid = cv2.Canny(blurred, 30, 150)
        tight = cv2.Canny(blurred, 240, 250)
        auto = auto_canny(blurred)

        # only for debugging
        cv2.imwrite(os.path.join(out_dir, filename + '_wide.jpg'), wide)
        cv2.imwrite(os.path.join(out_dir, filename + '_mid.jpg'), mid)
        cv2.imwrite(os.path.join(out_dir, filename + '_tight.jpg'), tight)
        #cv2.imwrite(os.path.join(out_dir, filename + '_auto.jpg'), auto)
        

        canvas = create_canvas([image_gray, wide, mid, tight, auto], add_argument = True, debug = False)
        cv2.imwrite(os.path.join(out_dir, filename + '_canvas.jpg'), canvas)
        # debugging part ends

        _, final_chosen_thresh_image = cv2.threshold(tight, 127, 255, cv2.THRESH_BINARY)
        # threshold value 127 chosen as mose of the values in the image tight are either very close to 255 or to 0

        # set of all points in tight where pixel is white after binarizing it
        r, c = np.where(final_chosen_thresh_image == 255)
        xmin, ymin, xmax, ymax = c.min(), r.min(), c.max(),  r.max()
        # [xmin, ymin, xmax, ymax] are the tight bounding box coordinates around the coin

        img = cv2.rectangle(image,(xmin, ymin),(xmax, ymax),(0,255,0),1)
        cv2.imwrite(os.path.join(out_dir, filename + '_box.jpg'), img)

        # except Exception as e:
        #     print e, filename

    # for debugging only, an excel sheet that contains the chosen contour map
    df = pd.DataFrame(report_lines, columns = ['Filename', 'Chosen contour'])
    df.set_index(['Filename'], inplace = True)
    df.to_excel('contour_report.xlsx')