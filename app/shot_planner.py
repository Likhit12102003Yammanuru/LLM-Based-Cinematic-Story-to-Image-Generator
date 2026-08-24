SHOT_TYPES = [
    "wide cinematic shot",
    "medium action shot",
    "dramatic close-up shot",
    "aerial establishing shot"
]


def choose_shot(scene_id):

    return SHOT_TYPES[
        (scene_id - 1) % len(SHOT_TYPES)
    ]