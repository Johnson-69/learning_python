favourite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}
print('\n')

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")
print('\n')

for name in favourite_languages.keys():
    print(name.title())
print('\n')

# You can pull the keys, omitting 'keys()'.
for name in favourite_languages:
    print(name.title())