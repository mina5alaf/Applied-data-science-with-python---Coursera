#people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson',
         # 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


#def split_title_and_name(person):
   # title = person.split()[0]
  #  lastname = person.split()[-1]
  #  return '{} {}'.format(title, lastname)


#print(list(map(split_title_and_name, people)))*/


#people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson',
        #  'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

#def split_title_and_name(person):
#    return person.split()[0] + ' ' + person.split()[-1]

    #option 1
#for person in people:
#    print(split_title_and_name(person) == (
#    lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

    #option 2
#list(map(split_title_and_name, people)) == list(
#map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [
    a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

print(correct_answer[:50])
