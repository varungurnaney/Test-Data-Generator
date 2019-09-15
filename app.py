import requests
import json
import sys
import html
import pprint
from random import randrange, randint
from datetime import timedelta, datetime

class Generator(): 

	def __init__(self): 
		self.count = 50 # Set minimum count to 50
		self.id = 0

	def get_count(self): 
		# escape string to sanitize the input 
		if html.escape(sys.argv[1], quote=True)=="-c" and str(sys.argv[2]).isdecimal(): 
		#set min count atleast 50 results 
			if int(sys.argv[2])>50: self.count = sys.argv[2] 
		else: 
		#return an error message if the count was not a decimal
			print('[{"Error Code: 101", "Message": "Count is not a valid decimal Number"}]')
			sys.exit()


	def get_samples_using_service(self):
		if html.escape(sys.argv[3], quote=True)=="-k":
			headers = {'X-API-Key': html.escape(sys.argv[4], quote=True)}
		else: 
			return '[{"Error Code: 103", "Message": "Key is invalid"}]' 

		response = requests.get('https://my.api.mockaroo.com/test_medical_data.json?count='+str(self.count)+'', headers=headers)

		if response.status_code == 200: 
			return response.json() 
		else: 
			return '[{"Error Code: 102", "Message": "Unable to reach test data service"}]'
			

	def random_date(self):
	    delta = datetime.strptime('1/1/2009','%m/%d/%Y') - datetime.strptime('1/1/2008','%m/%d/%Y')
	    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
	    random_second = randrange(int_delta)
	    result = datetime.strptime('1/1/2008','%m/%d/%Y') + timedelta(seconds=random_second) 
	    return datetime.strftime(result,'%m-%d-%Y')

	def get_samples_raw(self):

		response = {}
		response['total']=self.count
		response['results']=[]

		#can alterantively  use names.get_first_name() or names.get_last_name()
		first_names = ['Michael', 'Pam', 'Jim', 'Angela', 'Dwight K', 'Kevin', 'Stanley', 'Oscar', 'Andy','Phyllis']
		last_names = ['Scott', 'Beasley', 'Harlpert', 'Martin', 'Schrute', 'Malone', 'Hudson', 'Martinez', 'Bernard','Vance']
		service_description = ['routine teeth cleaning','root canal','flu shot','eye check up','diabetes check up',"Preventive care"]
		service_performed_by = ['Dr Lenoard', 'Dr Cooper', 'Dr Koothrapali', 'Mr Hofstader']
		#service_date = random_date(d1, d2)
		service_amount_currency = ['USD', 'CAD']

		for i in range(0,self.count): 
			self.id+=1
			response['results'].append({
				'id': self.id ,
				'client_first_name': first_names[randint(0,9)], 
				'client_last_name': last_names[randint(0,9)], 
				'service_description': 	service_description[randint(0,5)], 
				'service_date': self.random_date(),
				'service_performed_by': service_performed_by[randint(0,3)],
				'service_amount_paid': randint(40,250),
				'service_amount_currency': service_amount_currency[randint(0,1)]
				})

			


		return response





if __name__== "__main__":

	g = Generator()
	g.get_count()
	if "--no-api" in sys.argv :
		with open('data.json', 'w') as outfile:
			json.dump(g.get_samples_raw(), outfile)
	else: 
		with open('data.json', 'w') as outfile:
			json.dump(g.get_samples_using_service(), outfile)
	





  
















