# Dec 8
# Install the package pattern
# Dec 8
import pattern.en


def SingularPlural(s, cat):
    singular = pattern.en.singularize(s)
    plural = pattern.en.pluralize(singular)
    if type(cat) == int:
        if cat in [1, -1]:
            print(singular)
        else:
            print(plural)
    elif type(cat) == str:
        if (s == singular and cat == plural) or (s == plural and cat == singular):
            print(f"Singular : {singular}")
            print(f"Plural: {plural}")
        else:
            print("Invalid Input")


# Give desired inputs
SingularPlural("Apple", 2)
SingularPlural("Apples", 1)
SingularPlural("Apples", "Apple")
SingularPlural("Apples", "Orange")

# Sample I/O
# Apples
# Apple
# Singular : Apple
# Plural: Apples
# Invalid Input
