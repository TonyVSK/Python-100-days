from bs4 import BeautifulSoup
import requests

# ===================================================================================================================================
# SCRAPING AMAZON PROCUCT PAGE TO GET PRICE
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"


response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find("span", class_="a-price-whole")


if price:
    try:
        preco_texto = price.text.replace(".", "")
        preco_inteiro = int(preco_texto)  
        print(preco_inteiro)
    except TypeError:
        print("TypeError found.")
    else:
        pass


# ===================================================================================================================================
# SENDING EMAIL WHEN PRICE IS LOW
    
import smtplib
if price < 100:
    # Email to send
    my_email = "putyoursemailhere@email.com"
    password = "useyourpasswordhere"
    # # smtp-mail.outlook.com
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="putyoursecondemailhere@email.com", 
            msg=f"Good news! low price at the product\n\nthe product you're wanting is with low price, about {price} $, go to {URL}"
        )