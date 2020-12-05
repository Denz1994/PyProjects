from string import Template


# TODO: Turn this into a class.
# TODO: Give it a file and namespace.
class Member:
    # Shared between all Member instances
    employed = True

    def __init__(self, name, age, title, isNewMember, company):
        self.name = name
        self.age = age
        self.title = title
        self.isNewMember = isNewMember
        self.company = company

    def reportOut(self):
        print(f'{self.name} is present!')


# TODO: Iterate and fill in from a database.
name = 'John Smith'
age = '20'
isNewMember = True
title = 'Sales Rep'
company = 'Bridge Capital'

juniorStaff = Member(name, age, title, isNewMember, company)

'''
Using messaging with various supported string manipulations.
'''
roleMsg = Template('$name is a member at $company.').substitute(name=juniorStaff.name, company=juniorStaff.company)

# Using f-strings: f"{var} and argument specifiers
patientMsg = f'{juniorStaff.name} is a {juniorStaff.title}.' if juniorStaff.isNewMember else '%s is not a %s.' % (
    juniorStaff.name, juniorStaff.title)
endMsg = '\n' + 'Finished.\n'


# This first arg has to be the worst looking syntax I've seen in a while. Just pick
# a format and stick with it buddy.
print('%sThis is {} he is {} years old.'.format(juniorStaff.name, juniorStaff.age) % '\n', patientMsg, roleMsg, sep='\n', end=endMsg)


