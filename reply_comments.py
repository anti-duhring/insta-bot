from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from time import sleep
import threading

class ReplyBot:

    def initialize_crawler(self, post_link, username, password, comment_text):

        self.post_link = post_link
        self.username = username
        self.password = password
        self.comment_text = comment_text

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        p = 'chromedriver.exe'
        driver = webdriver.Chrome(p, options=chrome_options)

        try:
            login = threading.Thread(target=self.login, args=(driver,))
            login.start()
        except:
            print('Erro ao fazer login')
    
    def login(self, driver):

        driver.get('https://www.instagram.com/accounts/login/')
        sleep(5)

        username = driver.find_element(By.CSS_SELECTOR, 'form#loginForm input[name="username"]')
        username.click()
        username.send_keys(self.username)

        password = driver.find_element(By.CSS_SELECTOR, 'form#loginForm input[name="password"]')
        password.click()
        password.send_keys(self.password)

        submit = driver.find_element(By.CSS_SELECTOR, 'form#loginForm button[type="submit"]')
        submit.click()
        sleep(5)

        try:
            self.go_to_post(driver=driver)
        except:
            print('Erro ao acessar link do post')

    def go_to_post(self, driver):

        driver.get("https://www.instagram.com/p/{post_link}/".format(post_link=self.post_link))
        sleep(5)

        try:
            self.get_replys_list(driver=driver)
        except:
            print('Erro ao obter comentários')
    
    def get_replys_list(self, driver):

        replys = driver.find_elements(By.CSS_SELECTOR, 'div[role="presentation"] ul > ul')

        for reply in replys:
            reply_user = reply.find_element(By.CSS_SELECTOR, 'h3')
            reply_button = reply.find_element(By.CSS_SELECTOR, 'button')

            if 'Ver respostas' in reply.text:
                print('O comentário do usuário @{reply_user} já havia sido respondido'.format(reply_user=reply_user.text))
            elif reply_user.text not in self.username:
                try:
                    reply_button.click()
                    sleep(2)
                    print('Respondendo comentário do usuário @{reply_user}'.format(reply_user=reply_user.text))
                    self.reply_back(driver=driver)
                except:
                    print('Erro ao responder comentários')
    
    def reply_back(self, driver):

        reply_box = driver.find_element(By.CSS_SELECTOR, 'form[method="POST"] textarea')
        reply_box.click()
        reply_box.send_keys(self.comment_text)

        reply_submit = driver.find_element(By.CSS_SELECTOR, 'form[method="POST"] button[type="submit"]')
        reply_submit.click()
        sleep(4)


username = 'casabela_belojardim'
password = 'Maju0405!'
post_link = 'CjEklPQuBFV'
comment_text = 'Obrigado pelo comentário! Venha conhecer nossa loja na Rua João Pessoa, 27 - Calçadão, Centro de Belo Jardim. Funcionamos de Seg à sex das 8hrs às 18hrs e no sábado das 8hrs às 12hrs.'

ReplyBot().initialize_crawler(post_link=post_link, username=username, password=password, comment_text=comment_text)