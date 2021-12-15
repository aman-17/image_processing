#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

using namespace cv;
using namespace std;

int H_MIN = 0;
int H_MAX = 255;
int S_MIN = 0;
int S_MAX = 255;
int V_MIN = 0;
int V_MAX = 255;

void on_trackbar(int, void*)
 {

 }

void createTrackbars()
{
//create window for trackbars
namedWindow("Trackbars", 0);
//create memory to store trackbar name on window
char TrackbarName[50];
sprintf(TrackbarName, "H_MIN", H_MIN);
sprintf(TrackbarName, "H_MAX", H_MAX);
sprintf(TrackbarName, "S_MIN", S_MIN);
sprintf(TrackbarName, "S_MAX", S_MAX);
sprintf(TrackbarName, "V_MIN", V_MIN);
sprintf(TrackbarName, "V_MAX", V_MAX);
//create trackbars and insert them into window to change H,S,V values

createTrackbar("H_MIN", "Trackbars", &H_MIN, H_MAX, on_trackbar);
createTrackbar("H_MAX", "Trackbars", &H_MAX, H_MAX, on_trackbar);
createTrackbar("S_MIN", "Trackbars", &S_MIN, S_MAX, on_trackbar);
createTrackbar("S_MAX", "Trackbars", &S_MAX, S_MAX, on_trackbar);
createTrackbar("V_MIN", "Trackbars", &V_MIN, V_MAX, on_trackbar);
createTrackbar("V_MAX", "Trackbars", &V_MAX, V_MAX, on_trackbar);
}

int main()
{
 Mat image, HSV, threshold;
 vector< vector<Point> > contours;
 vector<Vec4i> hierarchy;

 createTrackbars();

 image = imread("thumb.jpg");
 imshow("Original_image",image);

 cvtColor(image, HSV, CV_BGR2HSV);
 imshow("HSV_image", HSV);
 for (;;)
 {
    inRange(HSV, Scalar(H_MIN, S_MIN, V_MIN), Scalar(H_MAX, S_MAX, V_MAX), threshold);
    imshow("HSV_threshold", threshold);

    Mat result(threshold.size(), CV_8UC3, Scalar(0.0, 0.0, 0.0));
    findContours(threshold, contours, hierarchy, CV_RETR_CCOMP, CV_CHAIN_APPROX_SIMPLE);
    drawContours(result, contours, -1, Scalar(255.0, 255.0, 255.0), 1, 8);
    imshow("contours_image", result);

    if (waitKey(30) >= 0)
        break;
 }

 return(0);
 }