CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    SELECT salary INTO result
    FROM (SELECT DISTINCT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS RK FROM Employee)
    WHERE RK = N;


    RETURN result;
END;