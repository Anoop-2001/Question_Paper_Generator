import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for i in range(0, 5):
    f = open('fq%s.txt' % i, "w")
    f.write("Name:\nDate:\nUSN:\n")
    f.close()
    count = 0
    lis = []
    ques = list(capitals.keys())
    ques_all = random.sample(ques, 50)
    for k, v in capitals.items():

        while True:
            y = random.randint(0, 49)
            if y not in lis:
                lis.append(y)
                break

        count += 1
        msg1 = str(str(count) + "what is the capital of " + ques_all[y] + " ?\n ")
        ans = list(capitals.values())
        ans4 = random.sample(ans, 4)
        x = random.randint(0, 3)
        ans4[x] = capitals[ques_all[y]]
        msg2 = str(" a." + ans4[0] + " b." + ans4[1] + " c." + ans4[2] + " d." + ans4[3] + "\n\n")
        f = open('fq%s.txt' % i, "a")
        f.write(msg1 + "\n" + msg2)
        f.close()
        f = open('fa%s.txt' % i, "a")
        f.write(str(count) + ":" + ans4[x] + "\n")
        f.close()
