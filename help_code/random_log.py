import random
import csv

def writ_csv(csv_name,list):
    with open(csv_name, 'w', newline='') as f:
        reader = csv.writer(f, delimiter=',')
        for i in list:
            reader.writerow(i)


if __name__ == '__main__':
    # writ_csv('test_csv.csv', i)
    list_args = []
    list_person = []

    person = 0
    test_app = 0

    person_index = 74
    test_app_index = 100


    while True:
        if person < person_index:

            if test_app < test_app_index:
                test_app += 1
                args = random.uniform(9,10.1) # <--random uniform float
                args = '{:.2f}'.format(args) # <--format 2 point float
                list_args.append(args)

                print("test_app{}: {}".format(test_app, args))

            else:
                person += 1
                list_person.append(list_args)
                list_args = []
                test_app = 0 # <--reset test app

                print("person{}".format(person))

                writ_csv("test_new.csv", list_person) # <--write csv file

        else:
            print('-- FINISH APP --')
            break



