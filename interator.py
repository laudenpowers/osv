from time import sleep
from selenium.webdriver.support.ui import Select
from selenium import webdriver

import credentials

driver = webdriver.Chrome('chromedriver.exe')

FILEPATH = 'senhas'
FILEPATH2 = 'oldsenha'
driver.get(url="https://*******")

def is_the_page_ready(driver, id):
    try:
        ident = driver.find_element_by_id(id)
        return True
    except:
        return False


def login(driver):
	while is_the_page_ready(driver, 'usernameInput') != True:
		sleep(0.5)
	username = driver.find_element_by_id("usernameInput")
	username.send_keys(credentials.login)
	password = driver.find_element_by_id("passwordDisplayInput")
	password.send_keys(credentials.senha)
	button_login = driver.find_element_by_id('theButton')
	button_login.click()


def click_configuration_tab(driver):
	while is_the_page_ready(driver, 'startId') != True:
		sleep(0.5)

		#pagina carregou, so clicar na aba

	texts = driver.find_elements_by_class_name("text")

	# peguei todos os elementos na DOM que continham TEXT como classe
	#for t in texts: # percorri os elementos coletados acima, e então fui printando o conteúdo, mas é necessário verificar
	# se sempre serão a mesma posição, qualquer coisa faz um validador com IF para bater os nomes
	#	if(t.text == "Configuration"): # por exemplo
	texts[0].click()


def click_open_voice(driver):
	sleep(2)
	texts = driver.find_elements_by_class_name("text")
	texts[6].click()
	#for t in texts:
	#	print(t.text)

	#OpenScape Voice

def click_business_group(driver):
	sleep(2)
	driver.find_element_by_name("bgImage").click()
def click_general(driver):
	sleep(2)
	texts = driver.find_elements_by_class_name("text")
	texts[20].click()
	#for t in texts:
	#	print(t.text)

def click_authorization_codes(driver):
	sleep(2)
	texts = driver.find_elements_by_class_name("text")
	texts[22].click()

def click_add (driver):
	sleep(2)
	driver.find_element_by_id("authorizationCodeListForm:authorizationCodeListGrid:addButton").click()


def insere_senha(driver, senha):
	click_add(driver)
	handles = driver.window_handles # buscando as abas/popups/browsers abertos
	for i in range(len(handles)):
		sleep(0.5)
		driver.switch_to.window(handles[i]) # vasculha as telas abertas, até achar a que encontra o campo do START
		sleep(0.5)
		try:
			driver.find_element_by_id("modifyAuthorizationCodeForm:startDN") # acha o campo, para ter certeza que a tela selecionada
																			 # é a correta
			break # quebra o for, pq estamos na tela certa
		except:
			pass # caso não tenha o campo start, ele vai gerar um exception, pq ele não vai achar o campo

	driver.find_element_by_id("modifyAuthorizationCodeForm:startDN").clear()
	sleep(1)
	driver.find_element_by_id("modifyAuthorizationCodeForm:startDN").send_keys(senha)
	sleep(2)
	driver.find_element_by_id("modifyAuthorizationCode_actionBarButtonSave_styleSwitch").click()
	#driver.close()
	driver.switch_to.window(handles[0])

def select_search(driver):
	sleep(2)
	sec = Select(driver.find_element_by_id("authorizationCodeListForm:authorizationCodeListGrid:filterGenericComboBoxAUTH_CODE"))
	sec.select_by_value("authCode")

def delete_senha(driver, oldsenha):
	driver.find_element_by_id("authorizationCodeListForm:authorizationCodeListGrid:authCodeAUTH_CODE").send_keys(oldsenha)
	sleep(1)
	driver.find_element_by_id("authorizationCodeListForm:authorizationCodeListGrid:applyFilterButtonId").click()
	sleep(1)
	driver.find_element_by_name("authorizationCodeListForm:authorizationCodeListGrid:_idJsp2js_c3c23c64_54fd_4e01_b09e_8bf1fcf1897f_p1_").click()
	sleep(1)
	driver.find_element_by_id("authorizationCodeListForm:authorizationCodeListGrid:deleteButton").click()
	sleep(1)
	alert = driver.switch_to.alert
	alert.accept()
	driver.find_element_by_id("authorizationCodeListForm:authorizationCodeListGrid:authCodeAUTH_CODE").clear()



login(driver)
click_configuration_tab(driver)
click_open_voice(driver)
click_business_group(driver)
click_general(driver)
click_authorization_codes(driver)


#### Remover senha #####
#select_search(driver)
#fopen = open(FILEPATH2)
#lin = fopen.readline()
#print(lin)
#pwds = lin.split(",")
#for p in pwds:
#	delete_senha(driver, p)
#	sleep(1)


###### Incluir senha ######
fopen = open(FILEPATH)
lin = fopen.readline()
print(lin)
pwds = lin.split(",")
for p in pwds:
	insere_senha(driver, p)
	sleep(1)

