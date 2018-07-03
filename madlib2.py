def collect_responses():
    responses = {}
    print "Please fill in the blanks below:"
    print "____(name)____'s favorite subject in school is ____(subject)____."
    responses['name'] = raw_input("What is name? ")
    responses['subject'] = raw_input("What is subject? ") 
    return responses

def madlib(responses):
    template = '%s\'s favorite subject in school is %s.' % (responses['name'], responses['subject'])
    return template



answers = collect_responses()
print madlib(answers)