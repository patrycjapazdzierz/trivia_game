import requests
import html



def get_question():
    try:
        response = requests.get(
            "https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean",
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data["results"]

    except requests.exceptions.RequestException:
        print("Could not connect to the API.")
        return []



def play_quiz(question):
    question_number = 0
    score = 0
    while True:
        current_question = question[question_number]
        clean_question = html.unescape(current_question["question"])
        print(clean_question)

        while True:
            answer = input("true or false?").lower()
            if answer not in ["true", "false"]:
                print("Wrong Answer")
            else:
                break
        if answer == current_question["correct_answer"].lower():
                score += 1
                print("Correct")
        else:
                print("Wrong Answer")
        question_number += 1

        if question_number == len(question):
            break
    print(f"Your score is {score}/10")

if __name__ == "__main__":
    question = get_question()
    play_quiz(question)



