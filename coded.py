
#Password and other info
class pwd:
	def passed():
		with open("D:\\Softwares\\Python Vids\\Home study\\pwd.db", "r") as f:
			content = f.read()
		return content
