from imageio.v2 import imread
import re



img = imread('7-smarty/smarty_files/oxygen.png')
data = []
mid_row = img.shape[0] // 2
for i in range(img.shape[1]):
    # print(img[mid_row][i])
    if img[mid_row][i][0] != img[mid_row][i][1]:
        break
    if i % 7 == 0:
        data.append(chr(img[mid_row][i][0]))
print(''.join(data))

next_level = re.findall(r'\d+', ''.join(data))
print(''.join([chr(int(x)) for x in next_level]))
