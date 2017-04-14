from sqlalchemy import create_engine,asc
from sqlalchemy.orm import sessionmaker
from puppies import Base,Shelter,Puppy
from sqlalchemy import func
import datetime


engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def query_one():
    #Query all of the puppies and return the results in ascending alphabetical order

    allpuppies = session.query(Puppy).order_by("name asc")

    for item in allpuppies:
        print(str(item.id) + "\t" + item.name + "\t\t" + item.gender + "\t" +
              str(item.dateOfBirth) + "\t" +
              str(item.weight)) 


def query_two():
    #Query all of the puppies that are less than 6 months old organized by the youngest first
    today = datetime.date.today()
    sixmonthsago = today - datetime.timedelta(days = 183)
    puppiesSixmonths = session.query(Puppy).filter(Puppy.dateOfBirth >= sixmonthsago).order_by("dateOfBirth desc")
    for item in puppiesSixmonths:
        print(str(item.id) + "\t" + item.name + "\t\t" + item.gender + "\t" +
              str(item.dateOfBirth) + "\t" +
              str(item.weight)) 

        

 
    

def query_three():
    #3. Query all puppies by ascending weight
    print("------------------------------------")
    print("Query all puppies by ascending weight")

    allpuppiesByWeight = session.query(Puppy).order_by("weight asc")

    for item in allpuppiesByWeight:
        print(str(item.id) + "\t" + item.name.strip() + "\t\t" + str(item.weight) + "\t" + str(item.shelter_id))




def query_four():
    #4. Query all puppies grouped by the shelter in which they are staying
    print("------------------------------------")
    print("Query all puppies grouped by the shelter in which they are staying")

    puppiesGroupByShelter = session.query(Shelter,func.count(Puppy.id)).join(Puppy).group_by("shelter_id").all()

    for item in puppiesGroupByShelter:
        #print(str(item.id) + "\t" + item.name + "\t" + str(item.shelter.id) + "\t" + item.shelter.name)
        #print(str(item.id) + "\t" + str(item.shelter.id) + "\t" + item.shelter.name)
        print(str(item.Shelter.id) + "\t" + item.Shelter.name + "\t" + str(item[1]))


#query_four()
#query_three()
#query_one() 
query_two()
