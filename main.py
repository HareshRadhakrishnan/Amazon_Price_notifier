import requests
from bs4 import BeautifulSoup
import smtplib
Target_price = 120
amazon_link ="https://www.amazon.com/dp/B0863JB424/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B0863JB424&pd_rd_w=9hiXP&pf_rd_p=91afecf5-8b2e-41e2-9f11-dc6992c6eaa1&pd_rd_wg=mRbTT&pf_rd_r=9SJGVK7MHXK9EGJ2HEWE&pd_rd_r=cd77df5c-8b12-4c1d-a690-d3130db1201d&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTThFMldKQkEyMUI3JmVuY3J5cHRlZElkPUEwNTE2NzM0MUk2RzYyRTVINEFaMyZlbmNyeXB0ZWRBZElkPUEwNDQwOTA3MTRJUFhQWTE2T1dGTCZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
header = {
"Accept-Language":"en-US,en;q=0.9",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
'From': 'hareshsrilanka@gmail.com'
}
response= requests.get(url=amazon_link,headers= header)
site =response.text

soup = BeautifulSoup(site,"html.parser")

price = soup.find(id ="priceblock_ourprice").getText()
price = float(price.split("$")[1])

if price < Target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="mymail@gmail.com",password="MyPassword")
        connection.sendmail(from_addr="hareshsrilanka@gmail.com",to_addrs="haresh2569@gmail.com",msg=f"The Price is been Reduce to {price}$ now")

