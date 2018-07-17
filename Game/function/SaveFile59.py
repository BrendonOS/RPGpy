def checksave():
  f=open("savedata.txt", "r")
  if f.mode == 'r':
    saveplace = f.read
def savenow():
  file = open("savedata.txt", "w")
  
  file.write(placetosave)
  
  file.close()
  
  
  
  
