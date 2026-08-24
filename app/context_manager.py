class ContextManager:

    def __init__(self):

        self.context = {
            "current_location": None,
            "active_characters": [],
            "recent_characters": [],
            "current_mood": None
        }

    def update_context(self, scene):

        # Update location
        if scene["location"] != "cinematic environment":
            self.context["current_location"] = scene["location"]

        # Update characters
        for char in scene["characters"]:

            if char not in self.context["active_characters"]:
                self.context["active_characters"].append(char)

        # Store recent characters
        self.context["recent_characters"] = scene["characters"]

    def enrich_scene(self, scene, text):

        # ---------- LOCATION MEMORY ----------

        if scene["location"] == "cinematic environment":

            if self.context["current_location"]:
                scene["location"] = (
                    self.context["current_location"]
                )

        return scene

