def sol():
  counter = 0
  a = int(input("input the length for the square:"))
  for i in range(a):
    for i in range(a):
      print("* ", end = "")
      counter = counter + 1
      if(counter == a):
        counter = 0
        print("\n", end = "")
        break

sol()