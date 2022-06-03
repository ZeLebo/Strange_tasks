import random

hard = "(4 x 6-8)"
medium = "(4 x 12)"
many = "(30, 20, 15, 10)"

heavy_exercises = [
    (f"Разгибания гантели из-за головы {hard}", f"Разгибания гантели из-за головы {medium}"),
    (f"Жим штанги узким хватом на трицепс {medium}", f"Жим штанги узким хватом на трицепс {hard}"),
    (f"Французский жим гантелей {medium}", f"Французский жим гантелей {many}"),
    (f"Французский жим {hard}", f"Французский жим {medium}"),
    (f"Отжимания на брусьях {medium}", f"Отжимания на брусьях с отягощением {hard}"),
    ]

medium_exercises = [
    (f"Разгибания на блоке с прямой рукоятью {many}", f"Разгибания на блоке с прямой рукоятью {medium}"),
    (f"Разгибания на блоке с канатом {medium}", f"Разгибания на блоке с канатом {many}"),
    (
        f"Трицепс на блоке из-за головы {many}",
        f"Трицепс на блоке из-за головы {medium}",
        f"Трицепс на блоке из-за головы {hard}"
     ),
    ]


def generate():
    result = []
    for i in random.sample(heavy_exercises, 2):
        result.append(i[random.randint(0, len(i) - 1)])
    i = random.choice(medium_exercises)
    result.append(i[random.randint(0, len(i) - 1)])
    return result
