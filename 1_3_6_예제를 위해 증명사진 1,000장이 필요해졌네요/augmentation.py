#-*-coding:euc-kr
"""
Author : Byunghyun Ban
Book : �Ϲ����� ���� ���� �ڵ�ȭ
Last Modification : 2020.02.15.
"""
import time
import os
from PIL import Image
import sys

# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ��Ǯ�� �̹��� �̸��� �Է¹޽��ϴ�.
image_filename = sys.argv[1]

# ������� ������ ������ �����մϴ�.
out_dir ="augmentation"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

# ���� �̹��� ������ �ҷ��ɴϴ�.
image = Image.open(image_filename)
Xdim, Ydim = image.size

# ����� ���� ������ ������ �� ī���͸� �����մϴ�.
COUNT = 1

# �ϴ� ������ �����մϴ�. 2�� 0��
temp_new_file_name = "%05d.png" %COUNT
COUNT += 1
image.save(out_dir + "/" + temp_new_file_name)
image.close()

# ��� ���ϸ��� ������ ����Ʈ�� ����ϴ�.
FILELIST = [temp_new_file_name]

# ���� ���� �̹����� ��� �о�� �¿��Ī�� �����մϴ�. 2�� 1��
for i in range(len(FILELIST)):
    image = Image.open(out_dir + "/" + FILELIST[i])
    new_temp_name = "%05d.png" %COUNT
    COUNT += 1
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    image.save(out_dir + "/" + new_temp_name)
    image.close()
    FILELIST.append(new_temp_name)

# ���� ���� �̹����� ��� �о�� ���ϴ�Ī�� �����մϴ�. 2�� 2��
for i in range(len(FILELIST)):
    image = Image.open(out_dir + "/" + FILELIST[i])
    new_temp_name = "%05d.png" % COUNT
    COUNT += 1
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image.save(out_dir + "/" + new_temp_name)
    image.close()
    FILELIST.append(new_temp_name)

# ���� ���� �̹����� ��� �о�� �������� �����մϴ�. 2�� 3��
for i in range(len(FILELIST)):
    image = Image.open(out_dir + "/" + FILELIST[i])
    new_temp_name = "%05d.png" % COUNT
    COUNT += 1
    image = image.convert('1')
    image.save(out_dir + "/" + new_temp_name)
    image.close()
    FILELIST.append(new_temp_name)

# ���� ���� �̹����� ��� �о�� 1���� ȸ���մϴ�. 2�� 3�� * 180
for el in FILELIST:
    for i in range(180):
        # ����ϰ� 1,000�常 ����ô�.
        if COUNT > 1000:
            break
        image = Image.open(out_dir + "/" + el)
        image = image.rotate(i+1)
        image = image.resize((Xdim, Ydim))
        new_temp_name = "%05d.png" % COUNT
        COUNT += 1
        image.save(out_dir + "/" + new_temp_name)
        image.close()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
