import selenium
from selenium import webdriver
from time import sleep 
import pytest
import subprocess
from selenium.webdriver.common.by import By
import os

@pytest.fixture
def driver():
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    # Iniciar o driver
    driver = webdriver.Edge()

    # Definir tempo limite para carregamento da página
    driver.set_page_load_timeout(2)
    yield driver

    # Encerrar o driver e o processo
    driver.quit()
    process.kill()

def test_app(driver):
    driver.get("http://localhost:8501")
    sleep(5)

def test_check_title(driver):
    # Verifica se o título da página é "Hello World"
    driver.get("http://localhost:8501")
    sleep(10)

    page_title = driver.title
    expected_title = "Hello World"
    assert expected_title == page_title

def test_check_streamlit_h1(driver):

    driver.get("http://localhost:8501")
    sleep(10)

    h1_element = driver.find_element(By.TAG_NAME, "h1")
    assert h1_element.text == "Esse é um teste"

def test_check_usuario(driver):
    # Verifica se o usuário é validado com sucesso
    driver.get("http://localhost:8501")

    sleep(10)

    # Caminho do arquivo de sucesso
    sucess_file_path = os.path.abspath("data/arquivo_excel.xlsx")

    # Envia o arquivo para o input
    driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(sucess_file_path)

    # Espera 5 segundos para o usuário ser validado
    sleep(10)

    # Verifica se o usuário é validado com sucesso
    assert "Schema validado com sucesso" in driver.page_source
