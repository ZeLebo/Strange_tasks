import random

heavy_exercises = [
    ('Тяга гантели к поясу (5 x 12)','Тяга гантели к поясу (4 x 12)'),
    ('Тяга штанги к поясу (5 x 6-8)', 'Тяга штанги к поясу (4 x 12'),
    ('Тяга к подбородку (5 x 12)', 'Тяга к подбородку (4 x 12)'),
    ('Мертвая тяга (4 x 12)', 'Мертвая тяга (5 x 6-8)'),
    ('Гребная тяга (5 x 12)',)
    ]

medium_exercises = [
    ("Подтягивания широким хватом (5 x 6-8)", "Подтягивания широким хватом (4 x 12)"),
    ("Pull over в crossover (30, 20, 15, 10)", "Pull over в crossover (4 x 12)"),
    ('Тяга в Hammer одной рукой (5 x 12)', 'Тяга в Hammer одной рукой (30, 20, 15, 10)'),
    ('Тяга в Hammer двумя руками (5 x 12)', 'Тяга в Hammer двумя руками (4 x 15)'),
    ('Обратная тяга (4 x 12)', 'Обратная тяга (5 x 6-8)')
]


def generate():
    result = []
    for i in random.sample(heavy_exercises, 3 if len(heavy_exercises) > 3 else len(heavy_exercises)):
        result.append(i[random.randint(0, len(i) - 1)])
    for i in random.sample(medium_exercises, 3 if len(medium_exercises) > 3 else len(medium_exercises)):
        result.append(i[random.randint(0, len(i) - 1)])

    return result
