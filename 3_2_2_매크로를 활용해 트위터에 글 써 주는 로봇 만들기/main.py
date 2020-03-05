#-*-coding:euc-kr
"""
Author : Byunghyun Ban
Book : �Ϲ����� ���� ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""

import sys
import time
import twitter_bot_tweet as tb


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ���̵� �Է¹޽��ϴ�.
id = sys.argv[1]

# �н����带 �Է¹޽��ϴ�.
ps = sys.argv[2]

# Ʈ���� ������� ���� ������ �Է¹޽��ϴ�.
filename = sys.argv[3]

# Ʈ�� �Է� x��ǥ�� �Է¹޽��ϴ�.
mention_x = int(sys.argv[4].strip())

# Ʈ�� �Է� y��ǥ�� �Է¹޽��ϴ�.
mention_y = int(sys.argv[5].strip())

# ũ�ѷ��� �ҷ��ɴϴ�.
BOT = tb.TwitterBot(filename, (mention_x, mention_y))

# �α����� �õ��մϴ�.
BOT.login(id, ps)

# �α��ο� ���������� ��ũ�����̳� �� �� ����ݽô�.
BOT.save_screenshot(str(time.time) + ".png")

# Ʈ���Ϳ� ��� ����� �ø��ϴ�.
BOT.tweet_all()

# ��� ȭ���� ��� �����ϱ� ���� 10�ʵ��� ��ġ�մϴ�.
time.sleep(10)

# ũ�ѷ��� �ݾ��ݴϴ�.
BOT.kill()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
