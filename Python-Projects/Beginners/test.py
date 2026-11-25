# # # # # # import csv
# # # # # # with open("quiz_questions/history_easy.csv","r") as file:
# # # # # #     reader = csv.reader(file)
# # # # # #     rows = list(reader)
# # # # # #     for i in rows:
# # # # # #         for j in i:
# # # # # #             print(j)
# # # # # #         input()

# # # # # #rows_to_remove = rows.pop()
# # # # # #print(rows)
# # # # # #print(rows_to_remove)
# # # # # ans = ['[c', 'b]']

# # # # # for i in ans:
# # # # #     ans = i
# # # # # print(ans)

# # # # # amount = 100
# # # # # if type(amount) is not int:
# # # # #     print("not int")
# # # # # else:
# # # # #     print("int")


# # # # # def amount():
# # # # #     while True:
# # # # #         try:
# # # # #             amount = float(input("Enter the amount: "))
# # # # #             break
# # # # #         except ValueError:
# # # # #             print("You need to enter only numbers for amount")
# # # # #             print()
# # # # #             continue

# # # # # amount()

# # # # # def source():
# # # # #     while True:
# # # # #         source = input("Source currency (USD/EUR/INR): ").upper()
# # # # #         if source not in ['USD','INR','EUR']:
# # # # #             print(f'{source} currency is not supported' )
# # # # #         else:
# # # # #             break

# # # # # source()
# # # # import csv
# # # # def exchange_rates():
# # # #     with open("exchange_rates.csv","r") as file:
# # # #         reader = csv.reader(file)
# # # #         rows = dict(reader)
# # # #         print(rows)
# # # #         return rows

# # # # def main():
# # # #     amt = 100
# # # #     src = "INR"
# # # #     tgt = "USD"
# # # #     exchange_rate = exchange_rates()
# # # #     print(f"{exchange_rate[src]} {src} is equal to {exchange_rate[tgt]} {tgt} ")
# # # #     amount = amt * float(exchange_rate[tgt])
# # # #     print(amount)


# # # # # main()
# # # # my_dict = {"name": "Emma", "age": 25, "city": "NY"}

# # # # for key in my_dict.keys():
# # # #     print(key)

# # #         rows = []
# # #         print("Enter the amount to be deposited : ")
# # #         amount = int(input())
# # #         print("Enter your 4 digit pin : ")
# # #         pin = input()

# # #         with open("atm_records.csv","r",newline="") as file:
# # #             reader = csv.reader(file)
# # #             for row in reader:
# # #                 if  row[0] == pin:
# # #                     row[3] = str(int((row[3]))+ amount)
# # #                     print(row[3])
# # #                 rows.append(row)
# # #                 print(rows)
# # #         with open("atm_records.csv","w",newline="") as file:
# # #             writer = csv.writer(file)
# # #             writer.writerows(row)
# # #             return
# # #         print("Invalid Pin")  
# # import csv 
# # def load_account():
# #     with open("atm_records.csv","r",newline="") as file:
# #         reader = csv.reader(file)
# #         return reader

# # reader = load_account()
# # for row in reader:
# #     print(row)

# word = "word"
# if "w" in word:
#     print("Correct")
import random
symbols = ["🍒", "⭐", "🍋", "🔔", "💎"]
spin = random.sample(symbols, k=3)
print(" | ".join(spin))