from datetime import date
from datetime import datetime
import webbrowser as wb
today = date.today()
d1 = today.strftime("%d/%m/%Y")
now = datetime.now()
while True:
	print ("robot: How can i help you ")
	you = input ("you: ")

	if "date" in you:
		print ("robot: ...")
		print ("robot:", d1)
	elif "time" in you:
		dt_string = now.strftime("%H:%M:%S")
		print("robot: ...")
		print("robot: ", dt_string)
	elif "google" in you:
		print("robot: what do you want to search")
		search = input ("you: ")
		url = (f"https://www.google.com/search?q="+search)
		wb.get().open(url)
	elif "youtube" in you:
		print("robot: what do you want to search")
		search = input ("you: ")
		url = (f"https://www.youtube.com/results?search_query="+search)
		wb.get().open(url)
	elif "facebook" in you:
		url = f"https://www.facebook.com/"
		wb.get().open(url)
	elif "file" in you:
		print ("robot: enter name file")
		name = input("you: ")
		print ("robot: enter file type")
		loai = input ("you: ")
		f = open(name+"."+loai, 'r')
		str= f.read()
		print ("robot: ", str)
	elif "lqdoj" in you:
		url = f"https://lqdoj.edu.vn/"
		wb.get().open(url)
	elif "math" in you:
		print ("robot: day:4,6 time:7h30 to 9h15")
	elif "english" in you:
		print ("robot: day:3,5 time: 7h30 to 9h")
	elif "it" in you:
		print ("robot: day:7 time: 3h to 5h")
	elif "bye" in you:
		print("good bye, nice to see you again")
		break
	elif "translate" in you:
		url = f"https://translate.google.com/"
		wb.get().open(url)
	else:
		print("robot: i can't hear you, try again")
	