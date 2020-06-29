# -*-coding:euc-kr
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


class Thaad:
    def __init__(self, id, ps, keyword_file_name, target_file_name):
        # ������ ����̹��� �� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� ��帮���� ����մϴ�. �̷��� ��帮���� �۾��� ����˴ϴ�.
        self.options.add_argument("headless")
        # �ʿ��� ��� ������ â ũ�⸦ ������ �ݴϴ�.
        self.options.add_argument("--window-size=848,1500")
        # �ɼ��� �ݿ��� ũ�ҵ���̹��� ���� �ݴϴ�.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        # �α����� �����մϴ�.
        self.brunch_login(id, ps)
        # ���ݱ��� ������ ���� ������ ����ϱ� ���� ������ ����ϴ�.
        self.count = 0
        # �α������� �����մϴ�. �� Ŭ������ �����ϴ� ������ �ð����� ���ϸ��� �������ϴ�.
        self.log_output = str(time.time()) + ".txt"
        # ���� ��� Ű���带 ������ ������ ����ϴ�.
        self.kill_keywords = []
        # ���� ��� Ű���� ������ �о�ɴϴ�.
        self.read_kill_keyword(keyword_file_name)
        # ��ȣ ��� �Խù� �ּҸ� ������ ������ ����ϴ�.
        self.target_urls = []
        # ��ȣ ��� �Խù� �ּ� ������ �о�ɴϴ�.
        self.read_target_urls(target_file_name)
        print("file read done.")

    def brunch_login(self, id, ps):
        # �α����� ���� �غ� �մϴ�. īī���귱ġ�� ��� �α��� �ּҰ� ������ ��ϴ�.
        # �ٸ� ����Ʈ�� Ȱ���Ͻ� ��� �ռ� �α��� �������� �����Ͽ� �α��� �ּҸ� �����Ͽ� �ּ���.
        brunch_login_url = "https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fclient_id%3De0201caea90cafbb237e250f63a519b5%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fbrunch.co.kr%252Fcallback%252Fauth%252Fkakao%26scope%3D%26state%3DaHR0cHM6Ly9icnVuY2guY28ua3IvL3NpZ25pbi9maW5pc2g_c2lnbmluPXRydWUmdXJsPSUyRg%26grant_type%3Dauthorization_code"
        # �α��� �ּҷ� �̵��մϴ�.
        self.driver.get(brunch_login_url)
        # �귱ġ�� ��� ���̵� �Է� ����� �̸��� 'email'�Դϴ�. �� ��Ҹ� ã�Ƴ� �ٷ� id�� �Է��սô�.
        self.driver.find_element_by_name("email").send_keys(id)
        # �귱ġ�� ��� ��й�ȣ �Է� ����� �̸��� 'password'�Դϴ�. �� ��Ҹ� ã�Ƴ� �ٷ� ps�� �Է��սô�.
        # �߰��� ����Ű�� �ļ� �α����� �����մϴ�.
        self.driver.find_element_by_name("password").send_keys(ps + Keys.RETURN)
        # 10������ ��ٸ��ϴ�.
        time.sleep(10)
        print("login success")

    # ���� ��� Ű���� ������ �ҷ����� �Լ��Դϴ�.
    def read_kill_keyword(self, filename):
        # ������ �о�ɴϴ�.
        file = open(filename)
        # ������ �� �پ� �о�ɴϴ�.
        for line in file:
            # �� ������ self.kill_keywords�� �Է��մϴ�.
            self.kill_keywords.append(line.strip())
        # ������ �ݾ��ݴϴ�.
        file.close()

    def read_target_urls(self, filename):
        # ������ �о�ɴϴ�.
        file = open(filename)
        # ������ �� �پ� �о�ɴϴ�.
        for line in file:
            # �� ������ self.target_urls�� �Է��մϴ�.
            # �ڿ� �ִ� "#comments"�� �ָ��ϼ���. �귱ġ�� ��� �Խù� �ּ� �ڿ� #comments�� �Է��ϸ�
            # ��� â���� �ٷ� ������ �� �ֽ��ϴ�. ���� ���̵��� Ȯ �������ϴ�.
            # ���ǿ��� �����ڵ�ȭ�� ������� �ִ��� ������ ���� �ϰ�, ������ ���� Ȯ���ؾ� �մϴ�.
            # �ڵ����� ���迡 �ð��� �� ���� �����ϼ���.
            self.target_urls.append(line.strip() + "#comments")
        # ������ �ݾ��ݴϴ�.
        file.close()

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # ��ũ������ �����ϴ� �Լ��Դϴ�.
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # ��带 �����ϴ� �Լ��Դϴ�.
    def run_thaad(self):
        # �α� ������ �����մϴ�. ���⿡ ������ ������ ������ �α׸� ����մϴ�.
        log = open(self.log_output, 'w')
        # ��ȣ ��� url���� �ϳ��� �ҷ��ɴϴ�.
        for target_url in self.target_urls:
            # �Խù��� �̵��մϴ�.
            self.driver.get(target_url)
            # �ε��� ���� 3�� ���� ��ٸ��ϴ�.
            time.sleep(3)
            # �귱ġ�� ��� �� ������ ����� �ε���� �ʽ��ϴ�.
            # �ѹ� �� ������ �̵��� ��û�մϴ�. �̷��� ���â�� ��ϴ�.
            self.driver.get(target_url)
            # ����� cont_info ��� �̸��� Ŭ������ ǥ��˴ϴ�. �̰� ��� �ҷ��ɽô�.
            replies = self.driver.find_elements_by_class_name("cont_info")
            # ���� ����� �ϳ��� �ҷ����� �� �ϴ� ��찡 �߻��� �� �ְ���.
            if len(replies) == 0:
                # �� ��� ���� �Խù��� �Ѿ�����ϴ�.
                continue

            # ���� ��� ������ �м��ؼ� ���� Ű���尡 �ԷµǾ� �ֳ� Ȯ���մϴ�.
            # ��� ��Ҹ� �ϳ��� �ҷ��ɴϴ�.
            for i, elm in enumerate(replies):
                # �ڵ带 ª�� ����� ���� ������ ����ϴ�.
                # ����� �˻��ϰ�, ���� Ű���尡 ��ۿ� �ԷµǾ� �ִٸ� True�� �ٲ�ϴ�.
                target_detected = False
                # ���� Ű���带 �ϳ��� �ҷ��ɴϴ�.
                for keyword in self.kill_keywords:
                    # Ű���尡 ��� �ȿ� �ִ��� �˻��մϴ�.
                    if keyword in elm.text:
                        # ��ۿ��� Ű���尡 �߰ߵȴٸ� target_detected�� True�� �ٲٰ� ������ �����մϴ�.
                        target_detected = True
                        break
                # ��ۿ��� Ű���尡 �߰ߵ� ��� �Ʒ� �ڵ尡 ����˴ϴ�.
                if target_detected:
                    # �߰��� ���� ������ 1�� �߰��մϴ�.
                    self.count += 1
                    # ���� �ð��� ����� ������ �����մϴ�.
                    line = time.ctime() + "\n" + elm.text
                    # �װ� ȭ�鿡 ����մϴ�.
                    print(line)
                    # �귱ġ�� ��� ����� ȭ�鿡 ǥ�ð� �� �Ǵ� ��찡 �ֽ��ϴ�. ��Ҵ� �˻� �Ǹ鼭 ������.
                    # ����� Ŭ���ؾ��� ������ư�� Ȱ��ȭ�ǹǷ� �ϴ� Ŭ���� �����ؾ� �մϴ�.
                    # ����� Ŭ�� ������ ���°� �ɶ����� ��ũ���� ��� �����ݴϴ�.
                    for i in range(30):
                        try:
                            # ��� Ŭ���� �õ��մϴ�.
                            elm.click()
                        # Ŭ���� ������ ���
                        except:
                            # �Ʒ� ���� ȭ��ǥ Ű���带 ��� �������ϴ�.
                            for j in range(i):
                                self.driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_DOWN)
                            continue
                        # Ŭ���� �����ߴٸ� ���� ��ư�� Ȱ��ȭ�˴ϴ�.
                        del_button = elm.find_elements_by_tag_name("button")[-1]
                        # ���� ��ư�� �߰ߵǾ����� �˻��մϴ�.
                        # �߰ߵ��� �ʾҴٸ� �ϴ� ���� ��۷� �Ѿ�ϴ�.
                        if "����" in del_button.text:
                            # ������ư�� Ŭ���մϴ�.
                            del_button.click()
                            # ������ư�� Ŭ���ϸ� ���â�� �˾����� ��ϴ�. Ȯ�� ��ư�� �����ݽô�.
                            # �������� �̷��� �ȶ��մϴ�.
                            self.driver.switch_to.alert.accept()
                            # ������ ���������Ƿ� �α׸� ���Ͽ� ����մϴ�.
                            log.write(line)
                            # ���� ���� ���θ� ȭ�鿡 ����մϴ�.
                            print("Deleted Success")
                            # �ϴ� ��� �ϳ��� ���������Ƿ� �̷����� �±׵��� ��Ʈ�����ϴ�.
                            # �ٽ� ��ȣ ��� �Խù��� ���â���� �̵��� �۾��� �ݺ��մϴ�.
                            self.driver.get(elm)
                            break
        # �۾��� �������� �α� ������ �����մϴ�.
        log.close()
