import random
when = ['A stormy night', 'On the night of new moon', 'A peaceful day', 'On the last day of Earth' ]
who = ['my clone', 'I', 'ma homie', 'a monke']
name = ['Putin', 'Kim', 'Chungus', 'Satriopov']
residence = ['my basement', 'the Queens palace', 'a secret alleyway in New York' ]
went = ['to Putin', 'quite kids backpack', 'gun store']
happened = ['overthrew the government there', 'started a revolt', 'browsed reddit']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))