from PIL import Image

im = Image.open("11-odd_even/odd even_files/cave.jpg")

even_img = Image.new('RGB', (im.width // 2, im.height // 2))
odd_img = Image.new('RGB', (im.width // 2, im.height // 2))
for i in range(im.width):
    for j in range(im.height):
        if (i % 2 == 0 and j % 2 == 0):
            even_img.putpixel((i // 2, j // 2), im.getpixel((i, j)))
        if (i % 2 == 1 and j % 2 == 1):
            odd_img.putpixel((i // 2, j // 2), im.getpixel((i, j)))
even_img.save("11-odd_even/even.jpg")
odd_img.save("11-odd_even/odd.jpg")
