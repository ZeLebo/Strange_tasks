import sys
import notion_integration as ni

set_up = """What group of training do you want to use?
1. Back
2. Pectoral
3. Legs
4. Shoulders
5. Biceps
6. Triceps
7. Arms
8. Back + Biceps
9. Pectorals + Triceps
0. Legs + Shoulders
"""


def generate_training(group):
    def generate():
        pass

    tags = []
    if group == 1:
        from exercise_lists.back_list import generate
        tags = ["Back"]
    elif group == 2:
        from exercise_lists.pectoral_list import generate
        tags = ["Pectorals"]
    elif group == 3:
        from exercise_lists.leg_list import generate
        tags = ["Legs"]
    elif group == 4:
        from exercise_lists.shoulder_list import generate
        tags = ["Shoulders"]
    elif group == 5:
        from exercise_lists.biceps_list import generate
        tags = ["Biceps"]
    elif group == 6:
        from exercise_lists.triceps_list import generate
        tags = ["Triceps"]
    elif group == 7:
        from exercise_lists.biceps_list import generate
        tags = ["Biceps", "Triceps"]
        biceps = generate()
        from exercise_lists.triceps_list import generate
        triceps = generate()
        result = []
        for i in zip(biceps, triceps):
            result.append(i[0])
            result.append(i[1])
        return result, tags

    elif group == 8:
        # back + biceps
        tags = ["Back", "Biceps"]
        from exercise_lists.back_list import generate
        back = generate()
        from exercise_lists.biceps_list import generate
        biceps = generate()
        return (back, biceps), tags

    elif group == 9:
        # Pectorals + Triceps
        tags = ["Pectorals", "Triceps"]
        from exercise_lists.pectoral_list import generate
        pectorals = generate()
        from exercise_lists.triceps_list import generate
        triceps = generate()
        return (pectorals, triceps), tags

    elif group == 0:
        # Legs + Shoulders
        tags = ["Legs", "Shoulders"]
        from exercise_lists.leg_list import generate
        legs = generate()
        from exercise_lists.shoulder_list import generate
        shoulders = generate()
        return (legs, shoulders), tags

    return generate(), tags


def main():
    try:
        training_group = int(input(set_up)[0])
    except ValueError:
        print("Invalid input")
        sys.exit(1)
    if training_group < 0 or training_group > 9:
        print("Invalid input")
        sys.exit(1)

    training, tags = generate_training(training_group)
    add_notion = input("Do you want to add this training to your Notion? (y/n): ")
    if add_notion == "y":
        ni.create_page(training, tags)
    else:
        if isinstance(training, tuple):
            for group in training:
                for i, exercise in enumerate(group):
                    print(f"{i + 1}. {exercise}")
        else:
            for i, exersice in enumerate(training):
                print(f"{i + 1}. {exersice}")


if __name__ == '__main__':
    main()
