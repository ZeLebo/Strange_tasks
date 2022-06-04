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
        tags = ["Arms"]
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
