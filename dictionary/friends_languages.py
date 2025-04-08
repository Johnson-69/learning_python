favourite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil', 'sarah']
print('\n')

for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")