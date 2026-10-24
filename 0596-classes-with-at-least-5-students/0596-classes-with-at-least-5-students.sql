select  class 
from Courses
group by class
having count(Student)>=5