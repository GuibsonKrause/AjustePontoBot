# arquivo: ajuste_ponto.py

from typing import List, Dict
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AjustePontoBot:
    def __init__(
        self,
        sistema_url: str,
        profile_dir: str = r"C:\selenium\profile",
        timeout: int = 15,
    ) -> None:
        # Configura o ChromeDriver e usa sessão previamente logada
        service = Service(executable_path=r"C:\chromedriver-win64\chromedriver.exe")
        chrome_options = Options()
        chrome_options.add_argument(f"--user-data-dir={profile_dir}")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout)
        self.driver.get(sistema_url)

    def adicionar_ajuste(self, ajuste: Dict[str, str]) -> None:
        self._clicar_botao_ajuste_ponto()
        time.sleep(1)
        self._preencher_data(ajuste["data"])
        time.sleep(1)
        self._preencher_hora(ajuste["hora"])
        time.sleep(1)
        self._selecionar_dropdown("Tipo", ajuste["tipo"])
        time.sleep(1)
        self._selecionar_dropdown("Localização", ajuste["local"])
        time.sleep(1)
        self._selecionar_dropdown("Motivo", ajuste["motivo"])
        time.sleep(1)
        self._confirmar()
        time.sleep(1)

    def _clicar_botao_ajuste_ponto(self) -> None:
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Ajuste de ponto') or contains(text(),'Ajuste de Ponto')]")
            )
        )
        btn.click()

    def _preencher_data(self, data: str) -> None:
        campo = self.wait.until(
            EC.element_to_be_clickable((By.ID, "single-date-picker"))
        )
        campo.click()
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'SingleDatePicker_picker')]")
            )
        )

        # Extrai dia e clica
        parts = data.split()
        dia = str(int(parts[1].strip(',')))
        xpath_dia = (
            f"//div[contains(@class,'CalendarMonthGrid')]//div[@data-visible='true']"
            f"//td[@role='button' and normalize-space(text())='{dia}' and not(contains(@class,'blocked'))]"
        )
        dia_elem = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_dia))
        )
        dia_elem.click()

        # Aguarda fechamento do picker
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'SingleDatePicker_picker')]")
            )
        )

    def _preencher_hora(self, hora: str) -> None:
        campo = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label/div[contains(text(),'Hora')]/following::input[1]")
            )
        )
        campo.clear()
        campo.send_keys(hora)

    def _selecionar_dropdown(self, label: str, valor: str) -> None:
        inp = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//label/div[contains(text(),'{label}')]/ancestor::div[contains(@class,'ActionInput_wrapper')]//input"
                )
            )
        )
        inp.click()
        time.sleep(1)

        opc = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[contains(@class,'SharedDropdownMenu_optionsList')]//div[normalize-space(text())='{valor}']"
                )
            )
        )
        opc.click()
        # Aguarda fechamento da lista
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, f"//div[normalize-space(text())='{valor}']")
            )
        )

    def _confirmar(self) -> None:
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Confirmar')]")
            )
        )
        btn.click()

    def fechar(self) -> None:
        self.driver.quit()


def main() -> None:
    sistema_url = "https://admin.oitchau.com.br/punches/"
    dias_input = input("Digite os dias (ex: 1,2,10): ")
    dias = [d.strip() for d in dias_input.split(',') if d.strip()]

    ajustes: List[Dict[str, str]] = []
    ano_atual = datetime.now().year
    for dia in dias:
        data_fmt = f"abr {int(dia)}, {ano_atual}"
        ajustes.extend([
            {"data": data_fmt, "hora": "09:00", "tipo": "Entrada", "local": "HOME OFFICE", "motivo": "Outro"},
            {"data": data_fmt, "hora": "12:00", "tipo": "intervalo Início", "local": "HOME OFFICE", "motivo": "Outro"},
            {"data": data_fmt, "hora": "13:00", "tipo": "intervalo Final", "local": "HOME OFFICE", "motivo": "Outro"},
            {"data": data_fmt, "hora": "18:00", "tipo": "Saída", "local": "HOME OFFICE", "motivo": "Outro"},
        ])

    bot = AjustePontoBot(sistema_url)
    try:
        for ajuste in ajustes:
            bot.adicionar_ajuste(ajuste)
    finally:
        bot.fechar()

if __name__ == "__main__":
    main()
