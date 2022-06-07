"""
-- Use left() and right() to check  for start and end string respectively
SELECT DISTINCT city FROM station WHERE LEFT(city, 1) IN ('a','i','e','o','u') AND
RIGHT(city, 1) IN ('a','i','e','o','u');

REGEXP "^[aeiou].*"  -- Regular expression for comparing like the left()
"""
