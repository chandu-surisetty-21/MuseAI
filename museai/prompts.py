def get_prompt_template(task="story"):
    templates = {
        "story": "Once upon a time, in a land far away,",
        "dialogue": "Character A: Hello! How are you?\nCharacter B:",
        "poem": "Roses are red,\nViolets are blue,"
    }
    return templates.get(task, "Write something creative:")
