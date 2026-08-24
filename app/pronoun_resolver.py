def resolve_pronouns(scene, text, context):

    lower_text = text.lower()

    # He / She
    if (
        " he " in f" {lower_text} "
        or " she " in f" {lower_text} "
    ):

        if context["recent_characters"]:

            scene["characters"] = [
                context["recent_characters"][-1]
            ]

    # They
    if " they " in f" {lower_text} ":

        if context["active_characters"]:

            scene["characters"] = (
                context["active_characters"]
            )

    # Unknown Character fallback
    if "Unknown Character" in scene["characters"]:

        if context["recent_characters"]:

            scene["characters"] = (
                context["recent_characters"]
            )

    return scene