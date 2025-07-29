from os import system, name, path 
from random import choice
from time import sleep
from typing import Dict

def clear_screen() -> None:
	"""Clear the console screen"""
	system('cls' if name == 'nt' else 'clear')

def display_header(title : str) -> None:
	"""Display a consistent header for all screens"""
	clear_screen()
	print("\n" + "="*50)
	print(f"{title.title():^50}")
	print("="*50 + "\n")

def get_gender(question : str) -> str:
	""" Gets and validates user gender """
	valid_gender = ["male", "female"]
	while True:
		user_input : str = input(question).lower()
		if user_input in valid_gender:
			return user_input
		print("Please, Enter", " or ".join(valid_gender))
	

def get_input(question: str, question_key: str) -> str:
	""" Gets and validates user input """
	user_input = input(question).strip()
	if not user_input:
		print("Cannot be empty, try again.")
		return get_input(question, question_key)
		
	if question_key not in ["resident", "football"] and any(c.isdigit() for c in user_input):
		print("Cannot contain a number.")
		return get_input(question, question_key)
	
	if question_key in ["name", "resident", "school", "football"]:
		user_input = user_input.title()
	
	return user_input

def response(questions : Dict[str, str]) -> Dict[str, str]:
	""" Collects data from the user """
	user_response : Dict[str, str] = {}

	while questions.__len__() != 0:
		display_header("Simple Personal Assistance")
		question_key : str = choice(list(questions.keys()))
	
		if question_key != "gender":
			question : str = questions[question_key]
			question_value : str = get_input(question, question_key)
		else:
			question : str = questions[question_key]
			question_value : str = get_gender(question)
			
		user_response.update({question_key : question_value})
		del questions[question_key]
	
	return user_response

def get_summary(response : Dict[str, str]) -> Dict[int, str]:
	""" gets a sample of summaries from the user's data  """
	first_person : str = "he" if response["gender"] == "male" else "she"
	ownership : str = "his" if response["gender"] == "male" else "her"
	
	return {
		1 : f"As {response['name']} walked into {ownership} favorite food joint in {response['resident']}, {first_person} couldn't help but order {ownership} go-to dish, {response['food']}. While waiting for {ownership} food, {first_person}  pulled out {ownership} phone and checked the latest  updates on {response['football']}. After lunch, {response['name']} decided to spend the afternoon {response['hobby']} and thinking about {ownership} time at {response['school']}.",
		2 : f"{response['name']} was stoked to get tickets to the {response['football']} match against their arch-rivals in {response['resident']} {first_person} rocked {ownership} {response['football']} scarf and fueled up with {response['food']} before the game. As {response['name']} cheered on {ownership} team, {first_person} thought back to {ownership} days at {response['school']} when {first_person} first fell in love with football. After the match, {response['name']} celebrated by {response['hobby']} with friends.",
		3 : f"{response['name']} was ecstatic to see {response['football']} play a thrilling match in {response['resident']}. {first_person.title()} sported {ownership} {response['football']} scarf and munched on {response['food']} throughout the game. The excitement of the match reminded {response['name']} of {ownership} time at {response['school']}, where {first_person} first discovered {ownership} passion for football. After the game, {response['name']} spent the evening {response['hobby']} and discussing the highlights with friends.",
		4 : f"{response['name']} was beyond excited to join the {response['football']} fan club in {response['resident']}. {first_person} proudly wore {ownership} {response['football']} jersey and brought {response['food']} to share with fellow fans at the club's first meeting. {response['name']} had been a fan of the team since {response['school']} and was thrilled to connect with others who shared {ownership} passion. Together, {first_person} planned to {response['hobby']} and cheer on {ownership} team throughout the season.",
		5 : f"Yesterday, {response['name']} went to the {response['resident']} stadium to watch {ownership} favorite football team, {response['football']}, play a thrilling match. After the game, {first_person} celebrated with a plate of {response['food']} and wore {ownership} lucky {response['football']} socks. {response['name']} had a blast and can't wait for the next match! {first_person.title()} has been a fan of {response['football']} since {first_person} was in {response['school']}."
	}

def get_response() -> Dict[str, str]:
	""" gets the response from the user"""
	questions : Dict[str, str] = {
		"name" : "What is your name? ",
		"football" : "What's your favorite soccer team? ",
		"resident" : "Where do you live? ",
		"food" : "What's your favorite food? ",
		"school" : "What senior high school did you attend? ",
		"hobby" : "What do you enjoy doing in your free time? ",
		"gender" : "What's your gender?(male/female) "
	}
	user_response : Dict[str, str] = response(questions)
	
	return user_response

def status(param : str) -> str:
	""" Validates whether the user enters yes or no """
	user : str = input(f"\nDo you want to {param}?(yes/no): ").strip().lower()
	if not user in ["yes", "no"]:
		print("Please, Enter yes or no")
		return status(param)
	return user

def save(response : Dict[str, str], summary : str) -> None:
	""" Creates a file and saves user's summary into it """
	base_file_name : str = f"{response['name']}.txt"
	file_name : str = base_file_name
	
	counter : int = 1
	while path.isfile(file_name):
		file_name = f"{response['name']} {counter}.txt"
		counter += 1
	
	print("Loading...")
	sleep(1)
	with open(file_name, "w") as file:
		file.write(summary)
	print(f"File {file_name} saved successfully")

def count_down(seconds: int) -> None:
	""" Displays a countdown animation before the summary is displayed"""
	bars = "=" * 5
	for i in range(seconds, 0, -1):
		clear_screen()
		print(f"\n{bars:^50}\n{i:^50}\n{bars:^50}")
		sleep(1)
		clear_screen()
		sleep(1)

def display_summary(summary: str) -> None:
	""" Displays the summary to the console"""
	clear_screen()
	print("Wait...")
	sleep(1)
	count_down(3)
	display_header("Summary")
	print(summary, "\n")

def rating() -> int:
	""" Validates the rating input by the user"""
	while True:
		try:
			rating = int(input("Rate the assistant (1 to 5): "))
			if 1 <= rating <= 5:
				return rating
			else:
				print("Please enter a value between 1 and 5.")
		except ValueError:
			print("Please enter a value like 1 or 2 or 3 or 4 or 5.")

def main() -> None:
	response : Dict[str, str] = get_response()
	summary : Dict[int, str] = get_summary(response)
	summary_key : str = choice(list(summary.keys()))
	input("\nPress Enter key to continue...")
	display_summary(summary[summary_key])
	user_rating = rating()
	save_summary : str = status("save summary")
	if save_summary == "yes":
		save(response, summary[summary_key] + f"\n\nRating : {user_rating}.")
	input("\nPress Enter key to continue...")
	display_header("Try again")
	try_again : str = status("try again")
	if try_again == "yes":
		main()
	else:
		print("\nThank You!!!")
		
if __name__ == "__main__":
	main()
