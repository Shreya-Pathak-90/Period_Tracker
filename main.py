class period:

    def __init__(self):
        self.last_date = ""
        self.cycle_length = ""
        self.duration = ""

    def name_of_user(self)->str:
        name = input("Enter your name : ")
        print(name)

    def age(self)->int:
        age = int(input("Enter your age :"))
        print(age)

    def last_period_date(self)->str:
        self.last_date =input("What was your last period date (dd/mm/yyyy) : " )
        print(self.last_date)

    def length_of_cycle(self)->str:
        self.cycle_length = input("What is your cycle length (---- days): " )
        print(self.cycle_length)

    def period_occur_days(self)->str:
        self.duration = input("The number of days your period occurs (---- days): ")
        print(self.duration)

    def period_delayed(self)->bool:
        delayed = input("Did you missed your period? ")
        print(delayed)

    def calculate_next_period_date(self)->str:
        next_date = self.last_date + self.cycle_length
        print(f"Your next period will come on : {next_date}")

    def ovulation(self):
        ovulation_date = (self.last_date + self.cycle_length) - 14
        print(ovulation_date)    

    def period_end_date(self):
        end =  self.last_date + (self.duration - 1) 
        print(f"Your period will end on : {end}")  

    def take_inputs(self):
        self.name_of_user()
        self.age()
        self.last_period_date()
        self.length_of_cycle()
        self.period_occur_days()
        self.period_delayed()

    def calculations(self):
        self.calculate_next_period_date()
        self.ovulation()
        self.period_end_date()




def main():
    a = period()
    a.take_inputs()
    a.calculations()
    
main() 
