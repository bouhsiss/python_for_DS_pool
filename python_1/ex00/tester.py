from give_bmi import give_bmi, apply_limit

height =  [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
apply_limit = apply_limit(bmi, 25)
print(apply_limit, type(apply_limit))
