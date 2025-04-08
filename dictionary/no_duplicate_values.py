favourite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
    'john': 'python',
}
print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())