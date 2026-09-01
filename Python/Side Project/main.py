from subjects import subjects

from user_data import (
    create_user,
    login,
    get_user,
    load_progress,
    save_progress
)

def print_subjects(subjects):
    print("\n===== SUBJECTS =====")

    for number, subject in enumerate(subjects, start=1):
        display_name = subject.replace("_", " ").title()
        print(f"{number}. {display_name}")

    print("0. Exit")



def choose_subject(subjects):
    print_subjects(subjects)

    choice = input("\nSelect a subject by number or name: ").lower()

    if choice == "0" or choice == "exit":
        return None

    subject_names = list(subjects.keys())

    if choice.isdigit():
        choice_number = int(choice)

        if 1 <= choice_number <= len(subject_names):
            return subject_names[choice_number - 1]

    else:
        choice = choice.replace(" ", "_")

        if choice in subjects:
            return choice

    print("Invalid subject.")
    return "invalid"



def choose_category(subject):
    display_name = subject.replace("_", " ").title()

    print(f"\n===== {display_name} =====")
    print("1. Labs")
    print("2. Knowledge Checks")
    print("0. Back")

    choice = input("\nSelect an option: ").lower()

    if choice == "1" or choice == "labs":
        return "labs"

    elif choice == "2" or choice in ["knowledge checks", "knowledge_check", "kc", "kcs"]:
        return "knowledge_checks"

    elif choice == "0" or choice == "back":
        return None

    else:
        print("Invalid option.")
        return "invalid"



def print_labs(subjects, subject):
    labs = subjects[subject]["labs"]

    display_name = subject.replace("_", " ").title()

    print(f"\n===== {display_name} Labs =====\n")

    if not labs:
        print("No labs available.")
        return

    lab_list = []

    for lab_id, lab_data in labs.items():
        name = lab_data[0]
        completed = lab_data[1]

        if completed:
            status = "Complete"
        else:
            status = "Incomplete"

        lab_list.append(f"{lab_id} - {name} - {status}")

    # Print two labs per row
    for i in range(0, len(lab_list), 2):

        left = lab_list[i]

        if i + 1 < len(lab_list):
            right = lab_list[i + 1]
        else:
            right = ""

        print(f"{left:<70}{right}")



def print_kcs(subjects, subject):
    kcs = subjects[subject]["knowledge_checks"]

    display_name = subject.replace("_", " ").title()

    print(f"\n===== {display_name} Knowledge Checks =====\n")

    if not kcs:
        print("No knowledge checks available.")
        return

    kc_list = []

    for kc_id, kc_data in kcs.items():
        name = kc_data[0]
        score = kc_data[1]

        if score is None:
            result = "Not Attempted"
        else:
            result = f"{score}%"

        kc_number = kc_id.replace("kc_", "")
        kc_list.append(f"{kc_number} - {name} - {result}")

    # Print two knowledge checks per row
    for i in range(0, len(kc_list), 2):

        left = kc_list[i]

        if i + 1 < len(kc_list):
            right = kc_list[i + 1]
        else:
            right = ""

        print(f"{left:<70}{right}")



def edit_lab_status(subjects, subject, username):
    labs = subjects[subject]["labs"]

    while True:
        print_labs(subjects, subject)

        choice = input(
            "\nEnter lab numbers to mark complete "
            "(separate with spaces or commas), or 0 to go back: "
        ).strip()

        if choice == "0":
            return

        # Allow either commas or spaces
        choices = choice.replace(",", " ").split()

        valid_labs = []
        invalid_labs = []

        for lab_id in choices:
            if lab_id in labs:
                valid_labs.append(lab_id)
            else:
                invalid_labs.append(lab_id)

        # Mark valid labs complete
        for lab_id in valid_labs:
            labs[lab_id][1] = True

        # Save after making the changes
        if valid_labs:
            save_progress(subjects, username)

            print("\nUpdated:")
            for lab_id in valid_labs:
                print(f"{lab_id} - {labs[lab_id][0]} - Complete")

        if invalid_labs:
            print(
                "\nInvalid lab number(s): "
                + ", ".join(invalid_labs)
            )

        input("\nPress Enter to return to the lab list...")




def edit_kc_score(subjects, subject, username):
    kcs = subjects[subject]["knowledge_checks"]

    while True:
        print_kcs(subjects, subject)

        choice = input(
            "\nEnter the KC number to edit, or 0 to go back: "
        ).strip()

        if choice == "0":
            return

        kc_id = f"kc_{choice}"

        if kc_id not in kcs:
            print("Invalid KC number.")
            continue

        kc_name = kcs[kc_id][0]
        current_score = kcs[kc_id][1]

        if current_score is None:
            score_text = "Not Attempted"
        else:
            score_text = f"{current_score}%"

        print(f"\n{choice} - {kc_name}")
        print(f"Current score: {score_text}")

        new_score = input(
            "Enter a score from 0-100, or 'none' to clear: "
        ).lower()

        if new_score == "none":
            kcs[kc_id][1] = None

            save_progress(subjects, username)

            print("Score cleared.")

        elif new_score.isdigit():
            new_score = int(new_score)

            if 0 <= new_score <= 100:
                kcs[kc_id][1] = new_score

                save_progress(subjects, username)

                print(f"{kc_name} updated to {new_score}%.")

            else:
                print("Score must be between 0 and 100.")

        else:
            print("Invalid score.")



def subject_menu(subjects, subject, username):
    while True:
        category = choose_category(subject)

        if category is None:
            break

        if category == "invalid":
            continue

        if category == "labs":
            edit_lab_status(subjects, subject, username)

        elif category == "knowledge_checks":
            edit_kc_score(subjects, subject, username)



def main():
    while True:
        username = get_user()

        if username is None:
            print("Goodbye!")
            break

        user_data = load_progress(username)

        if user_data is None:
            continue

        while True:
            selected_subject = choose_subject(user_data)

            if selected_subject is None:
                save_progress(user_data, username)
                print("\nProgress saved.")
                break

            if selected_subject == "invalid":
                continue

            subject_menu(user_data, selected_subject, username)



main()