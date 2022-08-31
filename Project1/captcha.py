import requests
import base64
import io
from PIL import Image

def QueryCaptcha():

    response = requests.get('https://api.set.rn.gov.br/autbasic/captcha')

    response = response.json()

    secret = response['result']['secret']

    arquivo = response['result']['arquivo']

    img = arquivo[arquivo.find('/9'):]

    print(img)

    im = Image.open(io.BytesIO(base64.b64decode(img)))

    im.show()

    codeCaptcha = str(input("Digite o Captcha de result.jpg\n"))

    return codeCaptcha, secret;


cookies = {
    'ARRAffinity': '9de0650c499f1d7797f94557ee8db86e6bffc6141b85025f08c2165525f5807b',
    'SET-AUTH-RS': 'qlRWh0cOHnsAgvSQO1sFA8Dgq92GgJpMmqFcCSoP9y01wZS%2f9b6SXOrcQ9J2lhvJW4wKtxU%2fst49X3JDAfnCDg%3d%3d',
    'SET-AUTH-EK': 'YzhmNmFiMjNmZA%3d%3d%3apToYNTdBX6w0kgcZd3oveQ%3d%3d',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'pt-BR,pt;q=0.9',
    'Authorization': 'Basic MTIzNDU2OjY1NDMyMQ==',
    'Connection': 'keep-alive',
    'Origin': 'https://uvt.set.rn.gov.br',
    'Referer': 'https://uvt.set.rn.gov.br/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    'captcha_token': 'xskwLap0Mp0+lhZYaXrwoMCZ67DKldz9euGYYuwv4gc=', #secret
    'captcha_value': 'IVPBV', #codeCaptcha
    'client_id': 'ea359bfc', #investigar, a princípio não muda.
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://api.set.rn.gov.br/autbasic/signin/basic?client_id=ea359bfc&redirect_uri=https:%2F%2Fuvt.set.rn.gov.br&response_type=code+id_token&scope=openid&state=fltar7uqr57', cookies=cookies, headers=headers)