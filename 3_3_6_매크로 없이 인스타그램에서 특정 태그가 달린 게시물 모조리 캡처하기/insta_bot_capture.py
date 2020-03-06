#-*-coding:euc-kr
"""
Author : Byunghyun Ban
Book : �Ϲ����� ���� ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class CaptureBot:
    def __init__(self):
        # ���� ���̽��� �����մϴ�.
        self.querry ="https://www.instagram.com/explore/tags/"
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        #self.options.add_argument("--window-size=1024,768")
        # ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # ��ũ������ �����ϴ� �Լ��Դϴ�.
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # �ν�Ÿ�׷� �α��� �Լ��Դϴ�.
    def login(self, id, ps):
        # �α��� �������� �̵��մϴ�.
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        # ID, PS �Է� ��Ҵ� <input> �±��Դϴ�. ��Ҹ� ã���ݽô�.
        input_field = self.driver.find_elements_by_tag_name("input")
        # ù ��° ��Ұ� ���̵��Դϴ�. ���̵� �Է��մϴ�.
        input_field[0].send_keys(id)
        # ��й�ȣ �Է� ��Ҵ� �� ��°�Դϴ�. ��й�ȣ�� �Է��մϴ�.
        input_field[1].send_keys(ps)
        # ����Ű�� �ļ� �α����� �������մϴ�.
        input_field[1].send_keys(Keys.RETURN)

    # �ν�Ÿ�׷����� �±׸� �˻��ϴ� �Լ��Դϴ�.
    def search_tag(self, tag):
        self.driver.get(self.querry + tag)
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)

    # �±� �˻� ȭ�鿡�� �ֱٿ� �Խõ� ù ��° ������ ��� Ŭ���մϴ�.
    def select_picture(self):
        # �ֱ� ������ xpath�� �Ʒ��� �����ϴ�.
        recent_picture_xpath = '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]'
        # �ֱ� ������ ��Ҹ� �����ɴϴ�.
        recent_picture = self.driver.find_element_by_xpath(recent_picture_xpath)
        # �ֱ� ������ Ŭ���մϴ�.
        recent_picture.click()

    # �˻�������� ���ƴٴϸ� ������ ĸó�մϴ�.
    # num���� �� ���� �Խù��� ĸó�� �� �Է��մϴ�.
    # -1�� �Է��ϸ� ����ڰ� ���� �����ϱ� ������ ������ ����մϴ�.
    def capture_pictures(self, directory, num):
        # �ݺ� ȸ���� �����ϱ� ���� �����Դϴ�.
        count = num
        # count �� 0�� �ɶ����� �ݺ��մϴ�.
        while count != 0:
            # ī��Ʈ�� �� ���� ��Ƴ����ϴ�.
            # num�� -1�� ��� ��� 0���� �۾����⸸ �ϰ� 0�� ������ �����Ƿ� ������ ����˴ϴ�.
            count -= 1
            # ȭ���� ��°�� ĸó�ϴ°� �ǹ̰� ������ ������ �Խù� �κи� ĸ���սô�.
            # �� ������ xpath�� '/html/body/div[4]/div[2]/div/article' �Դϴ�.
            article_xpath = '/html/body/div[4]/div[2]/div/article'
            # ��Ҹ� ã�� �ݴϴ�.
            article_element = self.driver.find_element_by_xpath(article_xpath)
            # ��Һ��� ��ũ������ ���� �� �ֽ��ϴ�. ��� �ݽô�.
            article_element.screenshot(directory + "/" + str(time.time()) + ".png")
            # ��� ��ٷ� �ݽô�.
            time.sleep(2)
            # ���� �Խù��� �Ѿ�ô�. ���� ��ư���� link text�� "����"���� ����Ǿ� �ֽ��ϴ�. ��Ҹ� ã���ϴ�.
            next_button = self.driver.find_element_by_link_text("����")
            # Ŭ���մϴ�.
            next_button.click()
            # �ε��� ���� 5������ ��ٷ� �ݴϴ�.
            time.sleep(5)

    # �ڵ� ����ȭ�� ���� �ڱⰡ �˾Ƽ� �ν�Ÿ �α����ϰ�, �˻��ϰ�, ĸó�� �� �ϴ� �޼��带 ����ô�.
    def insta_jungdok(self, tag, directory, num=100):
        # �±׵� �˻��ϰ�
        self.search_tag(tag)
        # ���� �� ���� ������ ����
        self.select_picture()
        # ĸó�� ���鼭 ������ �� �徿 �Ѱ��ݴϴ�.
        self.capture_pictures(directory, num)
