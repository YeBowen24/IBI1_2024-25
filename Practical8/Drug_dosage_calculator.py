def consume_volume(weight,strength): #weight:int; strength:list[weight,volume]
    drug_w = weight * 15
    volume = drug_w / strength[0] * strength[1]
    return volume 

age = int(input('Input your age here:'))
weight = int(input('Input your weight(kg) here(10kg-100kg) :'))
strength = input('Input the strength of the paracetamol you use here: e.g. 120mg/5ml please input as 120/5 ')
strength = strength.split('/')
strength = [int(x) for x in strength]
V = consume_volume(weight,strength) # Function call 
print('You need %dml of the paracetamol (you provided in the input).'%(V))
#list_of_ints = [int(x) for x in list_of_strings]