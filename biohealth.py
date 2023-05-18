from PIL import Image, ImageFilter, ImageEnhance, ImageOps
# 1. 좌우반전 2. 상하반전 3. 회전 4. 흑백 5. 엠보싱 6. 스케치 7. 경계선 0. 종료 동의대학교 C20173374 강명현
img = Image.open("D:\summer.jpg")
img.show()
while True :
    print("1. 좌우반전 2. 상하반전 3. 회전 4. 흑백 5. 엠보싱 6. 스케치 7. 경계선 0. 종료")
    num = input()

    if num == '1' :
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img.show()
    elif num == '2' :
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img.show()
    elif num == '3' :
        img = img.rotate(45,expand=True)
        img.show()
    elif num == '4' :
        img = ImageOps.grayscale(img)
        img.show()
    elif num == '5' :
        img = img.filter(ImageFilter.EMBOSS)
        img.show()
    elif num == '6' :
        img = img.filter(ImageFilter.CONTOUR)
        img.show()
    elif num == '7' :
        img = img.filter(ImageFilter.FIND_EDGES)
        img.show()
    elif num == '0' :
        img.close()
        break
    