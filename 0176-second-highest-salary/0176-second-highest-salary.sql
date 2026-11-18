select (select salary from (
    select salary,dense_rank()
    over(order by salary desc) as ranked 
    from employee
)as sec_sal 
where ranked =2 
limit 1)as SecondHighestSalary