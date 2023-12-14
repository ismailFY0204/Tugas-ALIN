import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

img_path = 'Ismail_.jpeg'
img = cv2.imread(img_path)

# Periksa apakah gambar berhasil dibaca
if img is None:
    print(f'Gagal membaca gambar dari path: {img_path}')
else:
    # Cetak bentuk gambar
    print(img.shape)

    fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(fix_img)
    plt.show()

    R, G, B = fix_img[:,:,0], fix_img[:,:,1], fix_img[:,:,2]
    print(np.array(fix_img))


    warv_img = (0.299*R) + (0.587*G) + (0.114*B)
    print(warv_img)

    plt.axis('off')
    plt.imshow(warv_img, cmap = 'gray')
    plt.savefig('Metode Weighted Average.jpg' , bbox_inches = 'tight')