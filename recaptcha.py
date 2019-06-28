from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

from PIL import Image


driver = webdriver.Firefox()


urls = ['http://lattes.cnpq.br/0118224405460667', 'http://lattes.cnpq.br/0167581436112139', 'http://lattes.cnpq.br/0192715697891274', 'http://lattes.cnpq.br/0683060368138422', 'http://lattes.cnpq.br/0950965556955470', 'http://lattes.cnpq.br/0982289255520210', 'http://lattes.cnpq.br/1512576316406197', 'http://lattes.cnpq.br/1739997490142452', 'http://lattes.cnpq.br/1863175020067147', 'http://lattes.cnpq.br/1959285307720446', 'http://lattes.cnpq.br/2190849183511530', 'http://lattes.cnpq.br/2338841032640543', 'http://lattes.cnpq.br/2465553753502316', 'http://lattes.cnpq.br/3086288257972856', 'http://lattes.cnpq.br/3234356076237014', 'http://lattes.cnpq.br/3251775617012106', 'http://lattes.cnpq.br/3579290766137836', 'http://lattes.cnpq.br/3648952311886499', 'http://lattes.cnpq.br/3748302988128047', 'http://lattes.cnpq.br/3818385640376862', 'http://lattes.cnpq.br/3823772604133067', 'http://lattes.cnpq.br/3973077511904385', 'http://lattes.cnpq.br/4031770197674534', 'http://lattes.cnpq.br/4115626573281821', 'http://lattes.cnpq.br/4180982601229727', 'http://lattes.cnpq.br/4620227627509693', 'http://lattes.cnpq.br/4674017654568180', 'http://lattes.cnpq.br/4830529654070227', 'http://lattes.cnpq.br/5054703666891291', 'http://lattes.cnpq.br/5280610737740095', 'http://lattes.cnpq.br/5309315072574421', 'http://lattes.cnpq.br/5701925275743346', 'http://lattes.cnpq.br/5823662263613939', 'http://lattes.cnpq.br/6552120101074110', 'http://lattes.cnpq.br/7017802459850019', 'http://lattes.cnpq.br/7298637758046404', 'http://lattes.cnpq.br/7883906947985490', 'http://lattes.cnpq.br/8145269117998909', 'http://lattes.cnpq.br/8536808087464212', 'http://lattes.cnpq.br/9103911570385178', 'http://lattes.cnpq.br/9107895746529145', 'http://lattes.cnpq.br/9121073346944517', 'http://lattes.cnpq.br/9153211954743941', 'http://lattes.cnpq.br/9696422050573770', 'http://lattes.cnpq.br/9754410711541612']

driver.get('http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4537755Y5')
sleep(2)
frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
driver.switch_to.frame(frame)
el = driver.find_element_by_xpath("//*[@id='recaptcha-anchor']")
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(el, 5, 5)
sleep(0.2)
#action.click()
#action.perform()
driver.switch_to.default_content()
el = driver.find_element_by_xpath("//*[@id='submitBtn']")
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(el, 5, 5)
sleep(0.2)
#action.click()
#action.perform()
