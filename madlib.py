
def mad_lib():
    adj = input('Adjective: ')
    verb1 = input('Verb: ')
    verb2 = input('Verb: ')
    famous_person = input('Famous Person: ')
    mad_lib_string = f"Computer programming is so {adj}! It makes me so excited all the time because \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"
    print(mad_lib_string)


if __name__ == '__main__':
    mad_lib()

