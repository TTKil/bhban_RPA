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


class LikeBot:
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
        # �ε��� ���� 10�� ���� ��ٷ� �ݴϴ�.
        time.sleep(10)
        # ID, PS �Է� ��Ҵ� <input> �±��Դϴ�. ��Ҹ� ã���ݽô�.
        input_field = self.driver.find_elements_by_tag_name("input")
        # ù ��° ��Ұ� ���̵��Դϴ�. ���̵� �Է��մϴ�.
        input_field[0].send_keys(id)
        # ��й�ȣ �Է� ��Ҵ� �� ��°�Դϴ�. ��й�ȣ�� �Է��մϴ�.
        input_field[1].send_keys(ps)
        # ����Ű�� �ļ� �α����� �������մϴ�.
        input_field[1].send_keys(Keys.RETURN)
        # 10�� ���� ��ٷ� �ݴϴ�.
        time.sleep(10)

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

    # �˻�������� ���ƴٴϸ� ������ ���ƿ� �����ϴ�.
    # num���� �� ���� �Խù��� ���ƿ� ���� �Է��մϴ�.
    # -1�� �Է��ϸ� ����ڰ� ���� �����ϱ� ������ ������ ����մϴ�.
    def press_like(self, num):
        # �ݺ� ȸ���� �����ϱ� ���� �����Դϴ�.
        count = num
        # count �� 0�� �ɶ����� �ݺ��մϴ�.
        while count != 0:
            # ī��Ʈ�� �� ���� ��Ƴ����ϴ�.
            # num�� -1�� ��� ��� 0���� �۾����⸸ �ϰ� 0�� ������ �����Ƿ� ������ ����˴ϴ�.
            count -= 1
            # ���ƿ� ��ư�� �±׸� ���� ã��� ����ϴ�. ���ƿ� ��ư�� <svg> �±׷� ������� �ִµ�
            # �� ȭ�鿡 <svg> �±׸� ���� �ִ� ��ư�� �� �� ���� �ƴմϴ�.
            # �׷��Ƿ� �ϴ� <svg> �±׸� ���� ��Ҹ� ���� ����ɴϴ�.
            svg = self.driver.find_elements_by_tag_name("svg")
            # <svg> �±״� ���ο� aria-label �̶�� �̸��� ��Ʈ����Ʈ�� ���� �ֽ��ϴ�.
            # �� ��Ʈ����Ʈ�� '���ƿ�' �� svg��Ҹ� ã�Ƴ� Ŭ���սô�.
            # for ������ �ϴ� svg �±׵��� ������ �ҷ��ɴϴ�.
            for el in svg:
                # �±� ������ aria-label ��Ʈ����Ʈ�� ���ƿ� �� ��츸 ��Ƴ��ϴ�.
                # �̹� ���ƿ䰡 ������ �ִ� ��� ��Ʈ����Ʈ ���� "���ƿ� ���" �� ����˴ϴ�.
                # ���� �� ����� �̹� ���ƿ並 ���� �� �Խù��� �ǳʶ� �� �ִٴ� ������ �����ϴ�.
                if el.get_attribute("aria-label") == "���ƿ�":
                    # ���ƿ� ��ư�ϰ�� Ŭ���մϴ�.
                    el.click()
            # ���� �Խù��� �Ѿ�ô�. ���� ��ư���� link text�� "����"���� ����Ǿ� �ֽ��ϴ�. ��Ҹ� ã���ϴ�.
            next_button = self.driver.find_element_by_link_text("����")
            # Ŭ���մϴ�.
            next_button.click()
            # �ε��� ���� 5������ ��ٷ� �ݴϴ�.
            time.sleep(5)

    # �ڵ� ����ȭ�� ���� �ڱⰡ �˾Ƽ� �ν�Ÿ �α����ϰ�, �˻��ϰ�, ĸó�� �� �ϴ� �޼��带 ����ô�.
    def insta_jungdok(self, id, ps, tag, num=100):
        # �α����� �ϰ�
        self.login(id, ps)
        # �±׵� �˻��ϰ�
        self.search_tag(tag)
        # ���� �� ���� ������ ����
        self.select_picture()
        # ���ƿ並 �����鼭 ������ �� �徿 �Ѱ��ݴϴ�.
        self.press_like(num)
