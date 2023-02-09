def login():
  print("== Replit Login System ==")
  print()
  
  while True:
    name = input("What is your username?  ")
    password = input("What is your password?  ")
    print()
    
    if name == "munachidozie" and password == "Pa55w.rd":
      print("Welcome to Replit! Have a wonderful Repl day.")
      break
    else:
      print("Bzzzzzt. Wrong username or password. Try again. Input correct details this time.")
      print()
      continue

login()
