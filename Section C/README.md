# Celestine_TEST
### Stereo matching algorithm
For each pixel in the first image
– Find corresponding epipolar line in the right image 
– Examine all pixels on the epipolar line and pick the best match 
– Triangulate the matches to get depth information.

If necessary, rectify the two stereo images to transform epipolar lines into scanlines • For each pixel x in the first image 
– Find corresponding epipolar scanline in the right image 
– Examine all pixels on the scanline and pick the best match x’ 
– Compute disparity x-x’ and set depth(x) = fB/(x-x’)

Slide a window along the right scanline and compare contents of that window with the reference window in the left image.

We calculated Disparity(d) using various loss functions:
Actually we have created different functions for different Loss function.

Before computing the disparity map, we convert the two images to grayscale so that we only have one value (0 - 255) for each pixel.
To compute the sum of absolute differences between the template and a block, we subtract each pixel in the template from the corresponding pixel in the block and take the absolute value of the differences. Then we sum up all of these differences and this gives a single value that roughly measures the similarity between the two image patches. A lower value  means the patches are more similar.
The disparity values that we calculate using the block matching will all be integers, since they correspond to pixel offsets. It’s possible, though, to interpolate between the closest matching block and its neighbors to fine -tune the disparity value to a “sub-pixel” location.

1)  Answer - B

![alt-text-1](https://github.com/piyush-98/Celestini_TEST/blob/master/C/SSD.png)  ![alt-text-2](https://github.com/piyush-98/Celestini_TEST/blob/master/C/Normal%20Correlation.png)


### CODE OUTPUT :

![alt-text-1](https://github.com/piyush-98/Celestini_TEST/blob/master/C/output.png)  ![alt-text-2](https://github.com/piyush-98/Celestini_TEST/blob/master/C/output1.png)



2) Answer - B ( RMSE/d value when you use block size W=7 )

![alt-text-1](https://github.com/piyush-98/Celestini_TEST/blob/master/C/disparity.jpeg)

3) Time complexity: O(n^3
Space complexity: O(n^3)
Time taken: 358 seconds




