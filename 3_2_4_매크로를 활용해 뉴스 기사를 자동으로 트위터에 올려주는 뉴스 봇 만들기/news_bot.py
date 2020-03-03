#-*-coding:euc-kr
"""
Author : Byunghyun Ban
Book : �Ϲ����� ���� ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pywinmacro as pw
import time
import pyperclip


class NewsBot:
    def __init__(self, mention_location):
        # ��� ��ǥ�� Ʃ�÷� �����մϴ�.
        self.mention_location = mention_location
        # ���� ���̽��� �����մϴ�.
        self.querry ="https://www.google.com/search?tbm=nws&q="
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        #self.options.add_argument("--window-size=1024,768")
        # ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        # ������ ������ ������ ����Ʈ�� ����ϴ�.
        self.news_list = []
        # �ϴ� Ʈ���� �α���ȭ������ ���ϴ�.
        self.go_to_twitter()
        # 5�� ���� ��ٷ��ݴϴ�.
        time.sleep(5)

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # �˻��� �ǽ��մϴ�.
    def search(self, keyword):
        self.driver.get(self.querry + keyword)
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(3)

    # �������� ���ΰ�ħ�մϴ�.
    def refresh(self):
        pw.key_press_once("f5")

    # �������� ��� ������ �����ϰ� Ŭ�����忡 �����մϴ�.
    def copy_all(self):
        pw.ctrl_a()
        pw.ctrl_c()

    # �������� ��� ������ ������ ���� ��縸 �̾Ƴ��� �Լ��Դϴ�.
    def scrap_news(self):
        # �ϴ� �������� ��� ���빰�� �����մϴ�.
        self.copy_all()
        # ���� ����Ʈ�� �ʱ�ȭ�մϴ�.
        self.news_list = []
        # �ؽ�Ʈ�� Ŭ�����忡�� ������ ��Ʈ������ �� �ɴϴ�.
        full_text = pyperclip.paste()
        # �� �پ� �ɰ��ݴϴ�.
        split = full_text.split("\n")

        # ���� ������ �̹��� ����, ������, �Խ� �ð�, ���� ��� ������ ������ �����˴ϴ�.
        # ���빰�� �� �پ� �����鼭 ������ ������ ���ô�.
        #������ ���� ������ ����� ��Ʈ���� ����� �ݴϴ�.

        # ���ڵ��� �� �پ� �ҷ��ɴϴ�.
        for i, line in enumerate(split):
            # ������ �� �ѱ�ٰ� ������ '���丮 �̹���'��� ���ڰ� ���� ���� �ѱ�ϴ�.
            if "���丮 �̹���" not in line:
                continue
            # '���丮 �̹���' ��� �ܾ �߰ߵǸ� �� ������ ���� 3���� ���� �ϳ��� ������ ����ϴ�.
            new_news = "\n".join(split[i+1:i+4])
            # ������� ������ news_list�� �����մϴ�.
            self.news_list.append(new_news)

    # ���� ��縦 ���ۿ��� �˻��� ��, ����Ʈ�� �ٵ�� �Լ��Դϴ�.
    def news_crawler(self, keyword):
        self.search(keyword)
        self.scrap_news()

    # ��ũ������ �����ϴ� �Լ��Դϴ�.
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # Ʈ���� �������� �����ϴ� �޼����Դϴ�.
    def go_to_twitter(self):
        # Ʈ���� Ȩ�������� �̵��մϴ�.
        self.driver.get("http://twitter.com/")
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)

    # �α����� �����ϴ� �޼����Դϴ�.
    def login(self, id, ps):
        # ���̵� �Է��մϴ�.
        pw.typinrg(id)
        # tab Ű�� �����ݽô�. ��κ��� ����Ʈ���� ��ȣâ���� �̵��մϴ�.
        pw.key_press_once("tab")
        # ��й�ȣ�� ���� �Է��մϴ�.
        pw.typinrg(ps)
        # 1�� �����ݴϴ�.
        time.sleep(1)
        # ����Ű�� �����ݴϴ�. ��κ��� ����Ʈ���� �α����� ����˴ϴ�.
        pw.key_press_once("enter")
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)

    # Ʈ���Ϳ� ���� �ø��� �Լ��Դϴ�.
    def tweet(self, mention):
        # ���â�� �� �� Ŭ���� �ݴϴ�. �ѹ��� �ؼ��� �� �� ���� �ֽ��ϴ�.
        pw.click(self.mention_location)
        pw.click(self.mention_location)
        pw.type_in(mention)
        # 1�� �����ݴϴ�.
        time.sleep(1)
        # �� Ű�� ���� �� �����ϴ�.
        for i in range(6):
            pw.key_press_once("tab")
        # 1�� �����ݴϴ�.
        time.sleep(1)
        # ����Ű�� Ĩ�ϴ�.
        pw.key_press_once("enter")

    # ��ũ���� ��� ������ Ʈ���Ϳ� �ø��� �Լ��Դϴ�.
    # 15�� �������� ������ �ø��ϴ�. �ð� ������ �ٲٰ� ������ �Լ��� ȣ���� �� �ð��� �ʴ����� �Է��մϴ�.
    # �ؽ��±׸� �Է��� ��� �Բ� �����մϴ�.
    def tweet_all(self, hashtags="", interval=15):
        for el in self.news_list:
            time.sleep(interval)
            self.tweet(el.strip() + " " + hashtags)

    # ���ۿ��� ������ �˻��ϰ�,
    # Ʈ���Ϳ� �ڵ����� �α��� �� ��,
    # �ܾ�� ��� ������ ���ε���� �ϴ� �Լ��Դϴ�.
    # 15�� �������� ������ �ø��ϴ�. �ð� ������ �ٲٰ� ������ �Լ��� ȣ���� �� �ð��� �ʴ����� �Է��մϴ�.
    # �ؽ��±׸� �Է��� ��� �Բ� �����մϴ�.
    def tweet_all_news(self, keyword, hashtags="", interval=15):
        self.news_crawler(keyword)
        self.go_to_twitter()
        self.tweet_all(hashtags, interval)
        time.sleep(interval)
