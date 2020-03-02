#-*-coding:euc-kr
"""
Author : Byunghyun Ban
Book : �Ϲ����� ���� ���� �ڵ�ȭ
Last Modification : 2020.02.18.
"""
import post_crawler as pc
import os
import time
import sys

#�۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ����ȣ�� ����� CSV������ �ҷ��ɴϴ�.
post_codes = sys.argv[1]

# ������� ����� �������� �Է¹޽��ϴ�.
out_dir = sys.argv[2]

# ������� ������ ������ ������ �ݴϴ�.
if out_dir not in os.listdir():
    os.mkdir(out_dir)

# CSV ������ �о�ɴϴ�.
csv = open(post_codes)

# ���ݱ��� �۾��� ����ȣ ������ ���� ���� ī���͸� �����մϴ�.
count = 1

# ũ�ѷ��� �ҷ��ɴϴ�.
crawler = pc.PostCrawler()

# �۾��� �� �� ������ �ɷ����� ���� �κ��Դϴ�.
# �۾��� �� �� ����ȣ�� ������ ����Ʈ�� �����մϴ�.
done_list = []
# ��� ���� ���� ������� �о�ɴϴ�.
temp = os.listdir(out_dir)

# ��� ���� ���� ��������� �ϳ��ϳ� �ҷ����鼭
# png������ ��� ����Ʈ�� �̸��� �����մϴ�.
for el in temp:
    if ".png" in el:
        done_list.append(el)

# CSV ������ ���پ� ������ �۾��� �����մϴ�.
for line in csv:
    # CSV �����̴ϱ� �ĸ��� �ɰ� �� �ֽ��ϴ�. �ɰ��ݽô�.
    # ���� ����ȣ�� ���� �ִٸ� ����ȣ�� ����ִ� ����Ʈ�� ��ȯ�ǰ�
    # ����ȣ�� �̸��� �Էµ� ����̶�� ����ȣ�� �������ɴϴ�.
    querry = line.split(",")[0].strip()

    # ���� ������ '-' �� �ԷµǾ� �ִٸ� �ٵ� �����ݽô�.
    if "-" in querry:
        # �������� �������� �ɰ��ݴϴ�.
        splt = querry.split("-")
        querry = "".join(splt)

    # ������ 13���� ������ �������� �����մϴ�. �ƴ϶�� ���� ������ �Ѱܹ����ϴ�.
    if len(querry) != 13 or not querry.isdigit():
        continue

    # �̹� ��ũ������ ĸó�� ������ ��� �۾��� �ߴ��ϰ� ���� ������ �Ѱܹ����ϴ�.
    if querry + ".png" in done_list:
        continue

    # ��ũ������ ������ ��� �ݽô�.
    crawler.save_screenshot(querry, out_dir)

    # ī���͸� 1 ������ŵ�ϴ�.
    count += 1

# ũ�ѷ��� �ݾ��ݴϴ�.
crawler.kill()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
