import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# here we load the image
img = Image.open("lord.jpeg") ## add your image here
img_np = np.array(img)

print(img_np.shape)

plt.imshow(img_np)
# plt.show()

## CONVERSION TO GRAYSCALE
# Gray = 0.299R + 0.587G + 0.114B

def toGrayscale(img):
    return(0.299 * img[:,:,0] + 0.587 * img[:,:,1] + 0.114 * img[:,:,2]).astype(np.uint8)

gray = toGrayscale(img_np)
plt.imshow(gray, cmap='gray')
# plt.show()

## BLUR IMAGE

def convolve(img, kernel):
    kh, kw = kernel.shape
    h, w = img.shape

    pad_h = kh // 2
    pad_w = kw // 2

    # padded image
    padded = np.pad(img, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')

    output = np.zeros((h,w))

    for i in range(h):
        for j in range(w):
            region = padded[i:i+kh, j:j+kw]
            output[i,j] = np.sum(region * kernel)

    return output.astype(np.uint8)

# now we blure the image

blur_kernel = np.ones((7,7)) / 49
blurred = convolve(gray, blur_kernel)

plt.imshow(blurred, cmap='gray')
# plt.show()

##  EDGE DETECTION

sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

edges_x = convolve(gray, sobel_x)

sobel_y = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

edges_y = convolve(gray, sobel_y)

edges = np.sqrt(edges_x**2 + edges_y**2)
edges = (edges / edges.max() * 255).astype(np.uint8)

plt.imshow(edges, cmap='gray')
# plt.show()

Image.fromarray(gray).save("gray.png")
Image.fromarray(blurred).save("blurred.png")
Image.fromarray(edges).save("edges.png")
