def camelcase(sentence):
    title_case = sentence.title()
    upper_camel_cased = title_case.replace(' ', '')

    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def banner():
    '''display program name'''
    message = "Awesome Camel Case Converter"
    stars = '*' * len(message)
    print(f'\n{stars}\n{message}\n{stars}\n')

def instructions():
        '''display program instructions'''
        print('This program converts a sentence into camel case. Enter a sentence below:\n')

def main():
    banner()
    instructions()
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()
