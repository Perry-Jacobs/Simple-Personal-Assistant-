# Simple-Personal-Assistant-

## Overview
This Python program is a simple personal assistant that collects user information and generates personalized summaries based on their inputs. The program features interactive prompts, data validation, and the ability to save generated summaries to text files.

## Features
- Interactive questionnaire collecting personal information
- Data validation for all user inputs
- Random selection of questions to make the interaction dynamic
- Gender-aware summary generation with appropriate pronouns
- Multiple summary templates for variety
- Countdown animation before displaying results
- Rating system for user feedback
- File saving functionality with automatic name generation
- Option to restart the program

## Requirements
- Python 3.x
- Standard Python libraries (os, random, time, typing)

## How to Use
1. Run the program in a Python environment
2. Answer the series of questions that appear:
   - Name
   - Favorite soccer team
   - Place of residence
   - Favorite food
   - High school attended
   - Hobby
   - Gender (male/female)
3. The program will generate a personalized summary
4. Choose whether to save the summary to a file
5. Rate your experience with the assistant
6. Option to try again or exit

## Data Validation
The program includes robust validation for:
- Non-empty inputs
- Numeric characters where not allowed
- Proper gender selection
- Yes/no confirmation responses
- Rating values (1-5)

## File Saving
- Summaries are saved as text files with the user's name
- Automatic numbering prevents overwriting existing files
- Files include the generated summary and user rating

## Customization
The program can be easily modified by:
- Adding/removing questions in the `questions` dictionary
- Creating new summary templates in the `get_summary` function
- Adjusting the countdown timer duration
- Changing file naming conventions

## Example Output
The generated summaries follow patterns like:
"As [Name] walked into [his/her] favorite food joint in [Residence], [he/she] couldn't help but order [his/her] go-to dish, [Food]..."

## Exit Option
Users can choose to exit the program after each complete cycle.

## Note
This program is designed for educational purposes and demonstrates various Python programming concepts including:
- Functions and type hints
- Dictionaries and randomization
- String formatting
- File operations
- User input validation
- Basic console animations
