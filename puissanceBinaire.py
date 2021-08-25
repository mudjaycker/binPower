def numberToBinary(number:int=0):
# ------------------------------------------------------------------------------------
# Declaration
  dictOfNumbers = {}
  converted = (bin(number)[2:])
  convertedList = list(converted) # converting the binary string sequence to list
  convertedList.reverse() # reversing the obtained list
  increment = 0 # value to increment so that we'll get a position of each digit
# /////////////////////////////////////////////////////////////////////////////////////

# ------------------------------------------------------------------------------------
# Priting the binary result
  print(f"Your number in binary ==> {converted}")
  print("="*100,"\n")
  print("Your number decomposed in two's power")
# /////////////////////////////////////////////////////////////////////////////////////

# ------------------------------------------------------------------------------------
# For loop to get only the the digit one(1) in the binary result
  for value in convertedList:
      dictOfNumbers[increment] = value
      increment+=1
# /////////////////////////////////////////////////////////////////////////////////////

# ------------------------------------------------------------------------------------
  tabTestSum = [] # table to test if the sum of 2's powers is equal to the number entered
# /////////////////////////////////////////////////////////////////////////////////////

# ------------------------------------------------------------------------------------
# Getting and multiply k if value = 1
  for k, v in dictOfNumbers.items():
    if v == '1':
      print(f"2power({k}) = {2**k}", end="\t")
      tabTestSum.append(2**k) # appending 2's powers results in tabTestSum
# /////////////////////////////////////////////////////////////////////////////////////

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  print("")
  print("="*100,"\n")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#------------------------------------------------------------------------------------
  from functools import reduce # importing reduce function
# Sum the list of 2's powers by using reduce and lambda function
  sumOfTwosPower = reduce(lambda x,y: x+y, tabTestSum)
# /////////////////////////////////////////////////////////////////////////////////////


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  print (f"the sum of {[i for i in tabTestSum]} is  {sumOfTwosPower} "
         "\nand that's your number")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("="*100,"\n")

# ------------------------------ Main function -----------------------------------------------
def run():
  try:
    number = int(input("Enter an integer ==> "))
    numberToBinary(number)
    print("="*100)
  except ValueError:
    print("you should type an integer\n")


if __name__=="__main__":
  run()
  
# ? Thanks to learn from this code if you found it helpful, please may you tell me on my telegram acount, 
# ! there you could tell me another subject that I can code on to help you
# ! "https://t.me/mudjaygram" ==> Me on telegram