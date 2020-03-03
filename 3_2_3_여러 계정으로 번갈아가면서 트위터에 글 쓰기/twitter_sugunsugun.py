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


class TwitterBot:
    def __init__(self, contents, mention_location, encoding="utf-8"):
        # ��� ��ǥ�� Ʃ�÷� �����մϴ�.
        self.mention_location = mention_location
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        self.options.add_argument("window-size=1024x768")
        # Ʈ���� Ȩ�������� �̵��մϴ�.
        self.go_to_twitter()

        # ������ ������ �о�ɴϴ�. ���ڵ��� utf-8�� �ƴ� ������ ������ ������ ���̴ϴ�.
        # �̶��� ���ڵ��� ����� �ֽø� �˴ϴ�. �⺻���� utf8�Դϴ�.
        self.contents_file = open(contents, encoding=encoding)
        # �о�� ������ �ɰ� ����Ʈ�� ����ϴ�.
        self.contents = self.contents_file.read().split("\n")

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # Ʈ���� �������� �����ϴ� �޼����Դϴ�.
    def go_to_twitter(self):
        # ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        # Ʈ���� Ȩ�������� �̵��մϴ�.
        self.driver.get("https://twitter.com/")
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

    # ��ũ������ �����ϴ� �Լ��Դϴ�.
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # Ʈ���Ϳ� ���� �ø��� �Լ��Դϴ�.
    def tweet(self, mention):
        #���â�� �� �� Ŭ���� �ݴϴ�. �ѹ��� �ؼ��� �� �� ���� �ֽ��ϴ�.
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
        #����Ű�� Ĩ�ϴ�.
        pw.key_press_once("enter")

    # �о�� ��� ��ǵ��� ���ε��ϴ� �Լ��Դϴ�.
    # 3�� �������� ����� �ø��ϴ�. �ð� ������ �ٲٰ� ������ �Լ��� ȣ���� �� �ð��� �ʴ����� �Է��մϴ�.
    def tweet_all(self, interval=15):
        for el in self.contents:
            time.sleep(interval)
            self.tweet(el.strip())
