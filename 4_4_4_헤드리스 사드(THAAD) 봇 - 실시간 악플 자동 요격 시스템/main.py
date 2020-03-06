#-*-coding:euc-kr
"""
Author : Byunghyun Ban
Book : �Ϲ����� ���� ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""

import sys
import os
import time
import thaad


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# id�� �Է¹޽��ϴ�.
id = sys.argv[1]

# �н����带 �Է¹޽��ϴ�.
ps = sys.argv[2]

# Ű���尡 ����� ������ �Է¹޽��ϴ�.
keyword_file_name = sys.argv[3]

# ��ȣ���� �Խù� �ּҵ��� ����� ������ �Է¹޽��ϴ�.
target_file_name = sys.argv[4]

# �� �� �ݺ��� �� �Է¹޽��ϴ�. 0�� �Է¹����� ������ �ݺ��մϴ�.
number = int(sys.argv[5])

# ũ�ѷ��� �ҷ��ɴϴ�.
BOT = thaad.Thaad(id, ps, keyword_file_name, target_file_name)

# �ݺ����� while�� ¯�Դϴ�.
number -= 1
while number != 0:
    BOT.run_thaad()
    number -= 1
BOT.run_thaad()

# ũ�ѷ��� �ݾ��ݴϴ�.
BOT.kill()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
