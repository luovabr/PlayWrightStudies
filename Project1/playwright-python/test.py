import os

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from dotenv import load_dotenv

load_dotenv()

with sync_playwright() as p:
    
    def handle_response(response): 
		# the endpoint we are insterested in 
        if ("extrato" in response.url): 
            print(response.json()) 
    
    browser = p.chromium.launch(slow_mo=100)
    page = browser.new_page()

    page.on("response", lambda response: print("<<", response))
    page.on("request", lambda request: print(">>", request))
    page.on("response", handle_response)

    page.goto('https://uvt.set.rn.gov.br/#/home')
    page.locator('button:has-text("Usuário e senha")').click()
    page.locator('input[name="code"]').click();
    page.locator('input[name="code"]').fill(os.getenv('CODE_UVT'))
    page.locator('input[name="password"]').click()
    page.locator('input[name="password"]').fill(os.getenv('PASS_UVT'))
    page.locator('input[name="captcha"]').click()
    page.locator('text=Área Restrita Código Senha Captcha (solicitar nova imagem) Acessar Acesso com e- >> img').screenshot(path="captcha.png")
    captcha = input("Digite o CAPTCH\n")
    page.locator('input[name="captcha"]').fill(captcha)
    page.locator('text=Acessar').click()
    page.locator('button:has-text("Selecionar uma empresa")').click()
    page.locator('text=VIP CONSULTE LTDA').click()
    
    page.locator('text=Extrato Fiscal').click()

    expect(page).to_have_url('https://uvt.set.rn.gov.br/#/services/extratoFiscal')
    
    page.wait_for_selector("text=Extrato Fiscal do Contribuinte")

    
