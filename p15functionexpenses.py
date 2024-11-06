mad_exp_list=[100,200,300,400]
sinu_exp_list=[500,600,700,800]

def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total

mads_total=calculate_total(mad_exp_list)
sinus_total=calculate_total(sinu_exp_list)

print("Madhav's total",mads_total)
print("Saurabh 's total",sinus_total)