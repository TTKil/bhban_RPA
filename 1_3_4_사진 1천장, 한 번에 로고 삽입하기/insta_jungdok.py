#-*-coding:euc-kr
"""
Author : Byunghyun Ban
Book : �Ϲ����� ���� ���� �ڵ�ȭ
Last Modification : 2020.02.13.
"""
import time
import os
from PIL import Image
import sys

# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ������ ����� �������� �Է¹޽��ϴ�.
directory = sys.argv[1]

# ������ ������ �ΰ� ������ �Է¹޽��ϴ�.
logo_filename = sys.argv[2]

# ������� ������ ������ �����մϴ�.
os.mkdir("images_with_logo")

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# �ΰ� ������ �ҷ��ɴϴ�.
logo = Image.open(logo_filename)

# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in input_files:
    # ��Ȥ �̹��� ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    exp = filename.strip().split('.')[-1]
    if exp not in "JPG jpg JPEG jpeg PNG png BMP bmp":
        continue

    # �̹����� �ҷ��ɴϴ�.
    image = Image.open(directory + "/" + filename)

    # �̹����� ũ�⸦ �˾Ƴ��ϴ�.
    Xdim, Ydim = image.size

    # �ΰ������� �̹����� �°� ������ Ȯ��/����մϴ�.


    # ���ο� �̹����� �����մϴ�. �� �� ���簢���̰� ������ background_color �Դϴ�.
    new_image = Image.new("RGBA", (new_size, new_size), background_color)

    # �� �� ��濡 ���� �̹����� �����ϴ�. ������ ��ġ�� ������.
    new_image.paste(image, (x_offset, y_offset))

    # ����� �̹����� �����մϴ�.
    new_image.save("squared_images/" + filename)

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
