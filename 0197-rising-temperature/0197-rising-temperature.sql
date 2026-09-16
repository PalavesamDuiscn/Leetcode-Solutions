select t.id 
from  Weather t join Weather y
on  t.recordDate=date_add(y.recordDate,interval 1 day)
where t.temperature>y.temperature;