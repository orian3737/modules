def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}:")
    return user_input

adjetive1 = get_input("adjetive")
noun1 = get_input("noun")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f"""
Once upon a time there was a {adjetive1} {noun1} that loved to {verb1} all day.

one day, {noun2} walked into the room got caught the {noun1} in the act.

{noun2}: "What are you doing?"
{noun1}: "I'm just {verb1}ing, whats the big deal?"
{noun2}: "Well, it's not every day you see a {noun1} {verb1}ing in the middle of the day."
{noun1}: "I guess you're right. Maybe I shhould take a break."
{noun2}: "That's probably a good idea. Why don't we go {verb2} instead?"
{noun1}: "Sure, that sounds like fun"

And so, {noun2} and the {noun1} went off to {verb2} and had a great time.
The end.
"""
print(story)