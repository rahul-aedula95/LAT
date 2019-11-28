from random import randrange
import calendar
import time
import datetime

class logger:

	def __init__(self):
		self.set_log_messages()

	def set_log_messages(self):
		self.log_messages = ['Failure to implement application','Successful run of the application','Warning during application run']

	def generate_random(self):
		return (randrange(100))

	def stream_logs(self):

		while True:
			rand_number = self.generate_random()
			print (self.choose_log_message(rand_number))

	def choose_log_message(self,number):
		stamp = self.set_timestamp()

		if number < 75:
			return(self.log_messages[1]+stamp)


		elif number >=75 and number <95:
			return(self.log_messages[0]+stamp)

		else:
			return(self.log_messages[2]+stamp)




	def set_timestamp(self):
		return (datetime.datetime.now().isoformat())


if __name__ == '__main__':
	
	log = logger()
	log.stream_logs()
	