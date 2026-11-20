from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount

total = 250.0

print("No Discount:", NoDiscount().apply(total))
print("10% discount:", PercentageDiscount(10).apply(total))
print("Bulk discount:", BulkDiscount(200, 20).apply(total))
print("Student discount:", StudentDiscount().apply(total))