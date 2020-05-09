

techs = ['Python\n', 'Django\n', 'Ruby\n', 'C++\n']

with open('my_techs.txt','w') as file_writer:
    file_writer.writelines(techs)  # lista


techs2 = ['Python', 'Django', 'Ruby', 'C++']

with open('my_techs.txt','a') as file_writer:
        for t in techs2:
            file_writer.write(t + '\n')  # string