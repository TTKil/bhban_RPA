#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : �Ϲ����� ���� ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self):
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        self.options.add_argument("--window-size=1024,768")
        # �ɼ��� �Է��ؼ� ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        # Ʈ���� �޽������� ������ ������ ����ϴ�.
        self.contents = []

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # ũ�ҵ���̹��� ���ٰ� �ٽ� �Ѵ� �ż����Դϴ�.
    def reload_browser(self):
        # ����̹��� ���ϴ�.
        self.kill()
        # �ɼ��� �Է��ؼ� ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)

    # �α����� �����ϴ� �޼����Դϴ�.
    def login(self, id, ps):
        # Ʈ���� �α���â���� ���ϴ�.
        self.driver.get("https://twitter.com/login")
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(3)
        # ���̵� �Է��ϱ� ���� ���̵� �Է�â ��Ҹ� ã�ƿɴϴ�.
        # Ʈ������ ��� ���̵� �Է�â�� session[username_or_email] �̶�� �̸��� ���� �ֽ��ϴ�.
        id_input = self.driver.find_element_by_name("session[username_or_email]")
        # id�� �Է��մϴ�.
        id_input.send_keys(id)

        # ��й�ȣ�� �Է��մϴ�.
        # Ʈ������ ��� ��й�ȣ �Է�â�� session[password] ��� �̸��� ���� �ֽ��ϴ�.
        ps_input = self.driver.find_element_by_name("session[password]")
        ps_input.send_keys(ps)
        ps_input.send_keys(Keys.RETURN)

    # ������ �о�� Ʈ���� �޽����� �����ϴ� �޼����Դϴ�.
    def prepare_contents(self, filename):
        # ���ڵ��� utf8�� �ƴ� ��� �������ּ���.
        file = open(filename, encoding="utf8")
        self.contents = file.read().split("\n")

    # �޽����� �Է¹޾� Ʈ���ϴ� �ż����Դϴ�.
    def tweet(self, string):
        # Ʈ�� ����� ���� �Է��� �� �ְ� ���� �������� �̵��մϴ�.
        self.driver.get("https://twitter.com/intent/tweet")
        time.sleep(5)
        # �޽��� �Է�â ��Ҹ� ã���ϴ�. xpath�� �����մϴ�.
        board = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        # �޽��� �Է�â�� �޽����� �����ϴ�.
        board.send_keys(string)
        # Ctrl + Enter�� ���� �޽����� �Խ��մϴ�.
        board.send_keys(Keys.CONTROL + Keys.RETURN)

    # self.contents�� ����� ��� �޽����� �ϳ��� Ʈ���ϴ� �ż����Դϴ�.
    def tweet_all(self, interval):
        # for���� ����� ��� �޽����� �ϳ��� �����մϴ�.
        for el in self.contents:
            # �޽����� �ϳ��� Ʈ���մϴ�.
            self.tweet(el)
            # �ε��� �� �ɸ� �� �����Ƿ� ��ٷ��ݴϴ�.
            time.sleep(interval)

    # ������ �о�� ����, ��� Ʈ���ϴ� �ż����Դϴ�.
    def twitter_jungdok(self, filename, interval=10):
        self.prepare_contents(filename)
        time.sleep(5)
        self.tweet_all(interval)

    def save_screenshot(self):
        self.driver.save_screenshot("test.png")
