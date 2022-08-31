const { test, expect } = require('@playwright/test');

const fs = require("fs");

require('dotenv/config');

// Import module
const Client = require('@infosimples/node_two_captcha');

// Declare your client
client = new Client('96558d1ab63188f84c5444eacc2d8107', {
                    timeout: 60000,
                    polling: 5000,
                    throwErrors: false});


test('test', async ({ page }) => {
  // Go to https://uvt.set.rn.gov.br/#/home
  await page.goto('https://uvt.set.rn.gov.br/#/home');
  // Click button:has-text("Usuário e senha")
  await page.locator('button:has-text("Usuário e senha")').click();
  // Click input[name="code"]
  await page.locator('input[name="code"]').click();
  // Fill input[name="code"]
  await page.locator('input[name="code"]').fill(process.env.CODE_UVT);
  // Click input[name="password"]
  await page.locator('input[name="password"]').click();
  // Click input[name="password"]
  await page.locator('input[name="password"]').fill(process.env.PASS_UVT);
  // Click input[name="captcha"]
  await page.locator('input[name="captcha"]').click();
  //Solving Captcha
  await page.locator('text=Área Restrita Código Senha Captcha (solicitar nova imagem) Acessar Acesso com e- >> img').screenshot({ path: 'captcha.png' });
  
  const test = await page.locator('text=Área Restrita Código Senha Captcha (solicitar nova imagem) Acessar Acesso com e- >> img').url();
  
  console.log(test);

  // Insert MANUALLY CAPTCHA
  const decode = client.decode({
    url: 'http://bit.ly/1xXZcKo'
  }).then(function(response) {
    console.log(response.text);
  });


  // Click text=Acessar
  await page.locator('text=Acessar').click();
  // Click button:has-text("Selecionar uma empresa")
  await page.locator('button:has-text("Selecionar uma empresa")').click();
  // Click text=VIP CONSULTE LTDA
  await page.locator('text=VIP CONSULTE LTDA').click();
  // Click text=Extrato Fiscal
  await page.locator('text=Extrato Fiscal').click();
  await expect(page).toHaveURL('https://uvt.set.rn.gov.br/#/services/extratoFiscal');
  // Getting content
  const content = await page.content();
  console.log(content);

  fs.writeFileSync("scrappy.txt", content);

});