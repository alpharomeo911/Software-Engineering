# Main Class
class Covid19():
	def __init__(self, current_location, username, email, phone_number, address):
		self.current_location = current_location
		self.username = username
		self.email = email
		self.phone_number = phone_number
		self.address = address

	def change_profile(self, username, email, phone_number, address):
		self.username = username
		self.email = email
		self.phone_number = phone_number
		self.address = address


class User(Covid19):
	def __init__(self, current_location, username, email, phone_number, address, user_id):
		super().__init__(current_location, username, email, phone_number, address)
		self.user_id = user_id
		self.user_family = []
		self.user_documnet = {}
		self.user_status = ""

	def add_family(self, user):
		if user.user_id:
			self.user_family.append(user)
			return "Added Family"
		else:
			return "User does not exist"
		
	def test_email(self):
		if not self.email.find('@') or self.email.find(' '):
			return "Please provide a valid email."
		else:
			return "Email is Valid."

	def show_family_health(self):
		for fam in user_family:
			print()

	def upload_document(self, dict_report):
		self.user_documnet = dict_report
		allowed_file_format = ['jpg', 'png', 'pdf']
		if dict_report['document_name'][-1:-4].lower() not in allowed_file_format:
			return "Please select a valid file format."
		else:
			return "Document Successfully Updated."

	def take_self_assessment(self):
		to_disp = f'''****** Taking Self Assessment Test ******
		user_id: {self.user_id}
		user_status: {self.user_status}
		'''
		print(to_disp)

