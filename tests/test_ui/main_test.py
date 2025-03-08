import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("url", ["https://only.digital/", "https://only.digital/projects", "https://only.digital/company",
                                 "https://only.digital/fields", "https://only.digital/blog"])
def test_footer_elements(driver, url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "footer")))

    # Проверка наличия футера
    assert driver.find_element(By.CSS_SELECTOR, "footer") is not None

    # Проверка наличия элементов в футере
    assert driver.find_element(By.CSS_SELECTOR, "footer .Footer_logo__2QEhf") is not None
    assert driver.find_element(By.CSS_SELECTOR, "footer .Footer_button__RHd0Q") is not None
    assert driver.find_element(By.CSS_SELECTOR, "footer .SocialButton_root__MjR_H") is not None
    assert driver.find_element(By.CSS_SELECTOR, "footer .Footer_year__nyNCc") is not None