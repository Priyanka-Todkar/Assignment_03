# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
# Explanation:
# Summation should like 8+2+3+0+7 = 20

def sum_numbers(numbers):
    total_sum = 0
    sum_expression = ""
    for i, num in enumerate(numbers):
        total_sum += num
        if num >= 0:
            if i == 0:
                sum_expression += str(num)
            else:
                sum_expression += "+" + str(num)
        else:
            sum_expression += str(num)
    return total_sum, sum_expression

sample_list = [8, 2, 3, 0, 7]
result, expression = sum_numbers(sample_list)
print("The sum of the numbers", expression, "=", result)