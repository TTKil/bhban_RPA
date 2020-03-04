#-*-coding:euc-kr
"""
Author : Byunghyun Ban
Book : �Ϲ����� ���� ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""

import sys
import time
import news_bot as nb


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ���� ������ �Էµ� ���� �̸��� �Է¹޽��ϴ�.
id_filename = sys.argv[1]

# ��� �˻��� �� Ű���尡 ��ϵ� ������ �Է¹޽��ϴ�.
keyword_filename = sys.argv[3]

# Ʈ�� ���̿� �Է��� ������ �ۼ��մϴ�.
# �ʹ� ��� Ʈ���� �Է��� �� �˴ϴ�. ª�� �Է��սô�.
endswith = "#���� #���� #��"

# ũ�ѷ��� �ҷ��ɴϴ�.
BOT = nb.NewsBot(endswith)

# id ������ �ҷ��ɴϴ�.
id_file = open(id_filename)
# ����Ʈ�� ����� �ݴϴ�.
IDs = []
for line in id_file:
    splt = line.split(",")
    if len(splt) != 2:
        continue
    IDs.append((splt[0].strip(), splt[1].strip()))

# Ű���� ���ϵ� �ҷ��ɴϴ�.
keyword_file = open(keyword_filename)
# ����Ʈ�� ����� �ݴϴ�.
Keywords = keyword_file.read().split("\n")

# ���ѹݺ� �� ������ while True�� �ְ��Դϴ�.
while True:
    # ������ �ϳ��� �ҷ��ɴϴ�.
    for account in IDs:
        # ������ �ٲ������ ����̹��� ���ٰ� �� �ݴϴ�.
        BOT.driver_refresh()
        # Ű���带 �ϳ��� �ҷ��ɴϴ�.
        for keyword in Keywords:
            # �ҷ��� Ű���带 ������� �˻��� �������� �����մϴ�.
            BOT.news_go_go(keyword)
        # ������ �ٲ� ������ 1�о� ��ٷ� �ݴϴ�.
        # ������ ����� �ʹ� ���� �Է��ϸ� Ʈ���ͷκ��� ���� ���ϱ� �����Դϴ�.
        # ��, Ű���带 ����� �˳��ϰ� �Է��ߴٸ� ���� Ű����� �ٽ� ������縦 �˻��ϴ� Ȯ���� �پ��Ƿ�
        # Ű���尡 ����� �پ��ϴٸ� ��� �ð��� �ٿ��� �˴ϴ�.
        time.sleep(60)

# ũ�ѷ��� �ݾ��ݴϴ�.
BOT.kill()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
