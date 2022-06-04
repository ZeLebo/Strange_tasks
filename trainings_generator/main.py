import sys
import notion_integration as ni
from generator import generate_training, set_up


def print_terminal(training, tags=None):
    if isinstance(training, tuple):
        for tag_num, group in enumerate(training):
            print(tags[tag_num].upper())
            for i, exercise in enumerate(group):
                print(f"{i + 1}. {exercise}")
    else:
        print(tags[0].upper())
        for i, exersice in enumerate(training):
            print(f"{i + 1}. {exersice}")


def ask_terminal():
    try:
        training_group = int(input(set_up)[0])
    except ValueError:
        print("Invalid input")
        sys.exit(1)
    if training_group < 0 or training_group > 9:
        print("Invalid input")
        sys.exit(1)
    return training_group


def check_param(param):
    if param == "--help" or param == "-h" or param == "--h":
        print("Usage: python3 main.py [--group] [--notion] [--term] [--help]")
        print("--help, --h: print this message")

        print("OUTPUT OPTIONS:")
        print("--notion: add training to Notion")
        print("--term: print training to terminal")

        print("GROUPS (can define multiple):")
        print("--back: back training")
        print("--pectoral, --pec: pectorals training")
        print("--legs: legs training")
        print("--shoulder, --shoulders, --shoul: shoulders training")
        print("--biceps, --bicep, --bic: biceps training")
        print("--triceps, --tricep, --tri: triceps training")
        print("--arms, --biceps-triceps: arms training")
        print("--back-biceps, --back-bic: back + biceps training")
        print("--pectoral-triceps, --pectoral-tri, --pt: pectorals + triceps training")
        print("--leg-shoulder, --legs-shoul, --ls: legs + shoulders training")
        print("'--' is optional")
        sys.exit(0)

    if param in ["--back", "back"]:
        training_group = 1
        return generate_training(training_group)
    elif param in ["--pectoral", "--pec", "pec", "pectoral"]:
        training_group = 2
        return generate_training(training_group)
    elif param in ["--legs", "legs", "--leg", "leg", "l"]:
        training_group = 3
        return generate_training(training_group)
    elif param in ["--shoulder", "--shoulders", "--shoul", "shoulder", "shoulders", "shoul"]:
        training_group = 4
        return generate_training(training_group)
    elif param in ["--biceps", "--bicep", "--bic", "biceps", "bicep", "bic"]:
        training_group = 5
        return generate_training(training_group)
    elif param in ["--triceps", "--tric", "--tri", "--tr", "triceps", "tric", "tri", "tr"]:
        training_group = 6
        return generate_training(training_group)
    elif param in ["--arms", "--biceps-triceps", "arms", "biceps-triceps"]:
        training_group = 7
        return generate_training(training_group)
    elif param in ["--back-biceps", "--back-bic", "--bb", "back-biceps", "back-bic", "bb"]:
        training_group = 8
        return generate_training(training_group)
    elif param in ["--pectoral-triceps", "--pectoral-tri", "--pt", "pectoral-triceps", "pectoral-tri", "pt"]:
        training_group = 9
        return generate_training(training_group)
    elif param in ["--legs-shoulder", "--legs-shoul", "--ls", "legs-shoulder", "legs-shoul", "ls"]:
        training_group = 0
        return generate_training(training_group)
    else:
        return None, None


def ask_notion(training, tags):
    add_notion = input("Do you want to add this training to your Notion? (y/n): ")
    if add_notion == "y":
        ni.create_page(training, tags)
    else:
        print_terminal(training, tags)


def is_notion():
    if "--notion" in sys.argv or "--not" in sys.argv or "--n" in sys.argv:
        return True
    elif "notion" in sys.argv or "not" in sys.argv or "n" in sys.argv:
        return True
    else:
        return False


def is_term():
    if "--term" in sys.argv or "term" in sys.argv:
        return True
    elif "--t" in sys.argv or "t" in sys.argv:
        return True
    else:
        return False


def main():
    # if no args, ask for terminal output
    if len(sys.argv) <= 1:
        training_group = ask_terminal()
        training, tags = generate_training(training_group)
    else:
        training, tags = (), []
        # training, tags = check_args()
        # check params
        for param in sys.argv[1:]:
            train, tag = check_param(param)
            if train:
                if isinstance(train, tuple):
                    training += train
                    for tg in tag:
                        tags.append(tg)
                else:
                    # add to training
                    tmp = list(training)
                    tmp.append(train)
                    training = tuple(tmp)
                    # add to tags
                    tags += tag
        if len(training) == 0:
            training_group = ask_terminal()
            training, tags = generate_training(training_group)

    # output options
    # if --notion --term in arguments
    if is_notion():
        ni.create_page(training, tags)

    elif is_term():
        print_terminal(training, tags)

    else:
        ask_notion(training, tags)


if __name__ == '__main__':
    main()
