#-*-coding:euc-kr
"""
Author : Byunghyun Ban
Book : �Ϲ����� ���� ���� �ڵ�ȭ
Last Modification : 2020.02.13.
"""
import time
import os
import numpy as np
from PIL import Image
import sys

# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ������ ����� �������� �Է¹޽��ϴ�.
directory = sys.argv[1]

# �� �ۼ�Ʈ ������ ����� ������ ������ �Է¹޽��ϴ�.
percent = float(sys.argv[2])/100

# ������� ������ ������ �����մϴ�.
os.mkdir("resized_image")

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in input_files:
    # ��Ȥ �̹��� ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    exp = filename.strip().split('.')[-1]
    if exp not in "JPG jpg JPEG jpeg PNG png":
        continue

    # �̹����� �ҷ��ɴϴ�.
    image = Image.open(directory + "/" + filename)

    # �̹����� ũ�⸦ �˾Ƴ��ϴ�.
    Xdim, Ydim = image.size

    # ���⿡ ������ ���� ���ο� �̹����� ����� ����մϴ�.
    Xdim *= percent
    Ydim *= percent

    # �̹��� ����� �����մϴ�.
    image = image.resize((int(Xdim), int(Ydim)))

    # ����� �̹����� �����մϴ�.
    image.save("resized_image/" + filename)

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
