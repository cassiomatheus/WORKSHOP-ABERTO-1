import selenium
from selenium import webdriver
from time import sleep 
import pytest
import subprocess

@pytest.fixture
def driver():
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    # Iniciar o driver
    driver = webdriver.Edge()

    # Definir tempo limite para carregamento da página
    driver.set_page_load_timeout(5)
    yield driver

    # Encerrar o driver e o processo
    driver.quit()
    process.kill()

def test_app(driver):
    driver.get("http://localhost:8501")
    sleep(5)