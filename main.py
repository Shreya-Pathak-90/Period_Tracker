class period:

    def name_of_user(self)->str:
        name = input("Enter your name : ")
        print(name)

    def age(self)->int:
        age = int(input("Enter your age :"))
        print(age)

    def last_period_date(self)->str:
        last_date =input("What was your last period date (dd/mm/yyyy) : " )
        print(last_date)

    def cycle_length(self)->str:
        cycle_length = input("What is your cycle length (---- days): " )
        print(cycle_length)

    def period_occur_days(self)->str:
        duration = input("The number of days your period occurs (---- days): ")
        print(duration)

    def period_delayed(self)->bool:
        delayed = input("Did you missed your period? ")
        print(delayed)


def main():
    a = period()
    a.name_of_user()
    a.age()
    a.last_period_date()
    a.cycle_length()
    a.period_occur_days()
    a.period_delayed()


main() 
