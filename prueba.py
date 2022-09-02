import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#ingreso a la URL
driver.get("http://192.168.56.101:8117/")

#Cargo el usuario
user = driver.find_element(By.ID, "user")
user.clear()
user.send_keys("root")

#Cargo la contraseña
password = driver.find_element(By.NAME, "pass")
password.clear()
password.send_keys("password")
password.send_keys(Keys.RETURN)

#Hay que redirigir de nuevo porque no toma el puerto sino
driver.get("http://192.168.56.101:8117/") 

#Lleno un campo de la sección "Creacion rapida de ticket"
contenidoTicket = driver.find_element(By.NAME, "Content")
contenidoTicket.clear()
contenidoTicket.send_keys("Probando")

#Hago clic en crear
crearTicket = driver.find_element(By.NAME, "SubmitTicket").click

time.sleep(5)
driver.close()