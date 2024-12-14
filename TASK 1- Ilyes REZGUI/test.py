
from datetime import datetime


try:
    dateinput=input(" please enter date").to_datetime()
    if not isinstance(dateinput,type(datetime)):
        raise Exception        
except Exception :
    print(" the input should be in datetime")


