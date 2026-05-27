import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = mpimg.imread("image.jpg")  
print("Original shape:", img.shape)

plt.imshow(img)
plt.title("Original Image")
plt.axis("off")
plt.show()


gray = img.mean(axis=2)

plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
plt.show()


bright = np.clip(gray + 0.2, 0, 1)
dark   = np.clip(gray - 0.2, 0, 1)


flip_h = np.fliplr(gray)
flip_v = np.flipud(gray)


h, w = gray.shape
crop = gray[h//4 : 3*h//4, w//4 : 3*w//4]


plt.figure(figsize=(15, 10))

titles = ["Gray", "Bright", "Dark", "Flip H", "Flip V", "Crop"]
images = [gray, bright, dark, flip_h, flip_v, crop]

for i, (t, im) in enumerate(zip(titles, images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(im, cmap='gray')
    plt.title(t)
    plt.axis("off")

plt.tight_layout()
plt.show()


kernel = np.ones((3,3)) / 9
blur = np.zeros_like(gray)

for i in range(1, gray.shape[0]-1):
    for j in range(1, gray.shape[1]-1):
        region = gray[i-1:i+2, j-1:j+2]
        blur[i, j] = np.sum(region * kernel)

plt.imshow(blur, cmap='gray')
plt.title("Blurred Image")
plt.axis("off")
plt.show()
