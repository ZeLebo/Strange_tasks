import random

hard = "(4 x 6-8)"
medium = "(4 x 12)"
many = "(30, 20, 15, 10)"

heavy_exercises = [
    (f"Подъём штанги на бицепс {hard}", f"Подъём штанги на бицепс {medium}"),
    (f"Подтягивания обратным хватом {medium}", f"Подтягивания обратным хватом {hard}"),
    (f"Молотки {many}", f"Молотки {medium}"),
    (f"Бицепс на скамье Скотта {hard}", f"Бицепс на скамье Скотта {medium}")
    ]

medium_exercises = [
    (f"Бицепс сидя с гантелями {medium}", f"Бицепс сидя с гантелями {hard}"),
    (f"Бицепс в crossover {many}", f"Бицепс в crossover {medium}")
    ]


def generate():
    result = []
    for i in random.sample(heavy_exercises, 2):
        result.append(i[random.randint(0, len(i) - 1)])
    result.append(i := random.choice(medium_exercises)[random.randint(0, len(i) - 1)])
    return result
