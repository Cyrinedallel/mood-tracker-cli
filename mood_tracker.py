import json
from datetime import datetime
from collections import Counter

FILENAME = "mood_data.json"

def load_data():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=2)

def add_mood():
    today = datetime.now().strftime("%Y-%m-%d")
    mood = input("How do you feel today? (happy/sad/neutral/other): ").strip().lower()
    data = load_data()
    data[today] = mood
    save_data(data)
    print(f"Saved mood '{mood}' for {today}.")

def show_history():
    data = load_data()
    if not data:
        print("No mood history yet.")
        return
    print("\nMood History:")
    for date, mood in sorted(data.items()):
        print(f"{date}: {mood}")
def show_stats():
    data = load_data()
    if not data:
        print("No mood data available to analyze.")
        return

    mood_counts = Counter(data.values())
    print("\nMood Statistics:")
    for mood, count in mood_counts.items():
        print(f"{mood}: {count}")
def main():
    print("Mood Tracker")
    while True:
        print("\nOptions:")
        print("1. Add mood")
        print("2. View history")
        print("3. View mood stats")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_mood()
        elif choice == "2":
            show_history()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()