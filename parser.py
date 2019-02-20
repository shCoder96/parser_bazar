from bs4 import BeautifulSoup 
from time import sleep
import requests
import smtplib
import private
# .findAll('tr')[11].findAll('td')[1].get_text()
def get_current_count_paypal():
	target_page = requests.get(private.url)
	get_html = BeautifulSoup(target_page.text)
	get_parent_block = get_html.findAll('tr')[11]
	get_children_block = get_parent_block.findAll('td')[1]
	data_convert = int(get_children_block.get_text())
	return data_convert

def send_email():
	mail_obj = smtplib.SMTP('smtp.gmail.com', 587)
	mail_obj.starttls()
	mail_obj.login(private.name, private.sec)
	mail_obj.sendmail(private.name, private.name_to, 'Time to work')

while True:
	current_count = get_current_count_paypal()
	
	try:
		current_count < previous_count
	except NameError:
		previous_count = current_count

	if current_count > previous_count:
		send_email()
		previous_count = current_count
	else:
		sleep(5)





