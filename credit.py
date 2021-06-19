from cs50 import get_string

card = get_string("Card: ")
while len(card) < 13:
    card = get_string("card: ")

copy = []
#total sum after algorithm
sum_total = 0;
for i in range(len(card) - 1, -1, -2):
    sum_total += int(card[i])
print(sum_total)
#sum of all digits aftr doubling
sum_dig = 0
for i in range(len(card) - 2, -1, -2):
    prod = int(card[i]) #doubled value
    prod = str(prod)
    for j in range(len(prod)):
        sum_prod = 0  #sum of doubled digits
        sum_prod += int(prod[j])

    sum_dig += sum_prod
sum_total += sum_dig
print(sum_total)
if (sum_total % 10 == 0):
    print("valid")
else:
    print("invalid")



