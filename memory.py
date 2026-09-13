import json
import os
import re

MEMORY_FILE = "memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def remember(user_message):

    memory = load_memory()

    # Remember user's name
    name_patterns = [
        r"my name is (.+)",
        r"i am (.+)",
        r"i'm (.+)"
    ]

    for pattern in name_patterns:
        match = re.search(pattern, user_message.lower())

        if match:
            memory["name"] = match.group(1).strip().title()

    # Remember "I like ..."
    like_match = re.search(r"i like (.+)", user_message.lower())
    if like_match:
        memory["likes"] = like_match.group(1).strip()

    # Remember "I study ..."
    study_match = re.search(r"i study (.+)", user_message.lower())
    if study_match:
        memory["study"] = study_match.group(1).strip()

    # Remember "I live in ..."
    live_match = re.search(r"i live in (.+)", user_message.lower())
    if live_match:
        memory["location"] = live_match.group(1).strip()

    save_memory(memory)


def get_memory_prompt():

    memory = load_memory()

    prompt = ""

    if "name" in memory:
        prompt += f"The user's name is {memory['name']}.\n"

    if "study" in memory:
        prompt += f"The user studies {memory['study']}.\n"

    if "likes" in memory:
        prompt += f"The user likes {memory['likes']}.\n"

    if "location" in memory:
        prompt += f"The user lives in {memory['location']}.\n"

    return prompt