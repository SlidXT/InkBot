import random
import help
import keepAlive
from replit import db

def main(message):
  # Special Commands
  
  if message.startswith(",help"):
    return help.main(message)
  
  if message.startswith(",add"):
    return addCommand(message)

  if message.startswith(",del"):
    return delCommand(message)

  if message.startswith(",rand"):
    return randomNum(message)

  # Developer Commands
  if message.startswith("$HELP DEVELOP"):
    return help.developer()

  if message.startswith("$ONLINE TIME"):
    return str(keepAlive.uptime) + " MINS"
    
  if message.startswith("$TIME EDIT"):
    chat = message.split(" ", 2)
    keepAlive.uptime += int(chat[2])
    return "New Time: " + str(keepAlive.uptime)

  if message.startswith("$LIST COMMAND"):
    return db.keys()

  if message.startswith("$INSTALL INKBOT"):
    return "Your Link Here" # Add Your Bot Invite Link Here

  # Filter Developer Commands
  if message.startswith("$"):
    return ""
    
  # Automatic Commands
  return runCommand(message)

def runCommand(message):
  if message not in db.keys():
    return "Command Not Found!"
  return db[message]

def addCommand(message):
  chat = message.split(" ", 2)
  command = "," + chat[1].lower()
  if len(chat) != 3:
    return "Invalid Syntax!"
  if command in db.keys():
    return "Command Already Exists!"

  command = "," + chat[1].lower()
  db[command] = chat[2]
  return "Command Added!"

def delCommand(message):
  chat = message.split(" ")
  command = "," + chat[1].lower()
  if len(chat) != 2:
    return "Invalid Syntax!"
  if command not in db.keys():
    return "Command Not Found!"

  del db[command]
  return "Command Deleted!"

def randomNum(message):
  chat = message.split(" ")
  if len(chat) == 1:
    return random.randint(1, 6)
  if len(chat) != 3:
    return "Invalid Syntax!"
  if not chat[1].isdigit() or not chat[2].isdigit():
    return "Invalid Syntax!"
  if int(chat[1]) > int(chat[2]):
    return "Min Is Larger Than Max!"
    
  rand = random.randint(int(chat[1]), int(chat[2]))
  return rand