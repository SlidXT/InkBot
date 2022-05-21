def main(message):
  chat = message.split(" ")

  if len(chat) == 1:
    return "```,add - Add Commands\n,del - Delete Commands\n,rand - Random Number\nUse `,help Command` For More Info```"
    
  if chat[1].lower() in ",add":
    return "This adds a new command, use the format, `,add prompt response`. Ensure that the prompt has no spaces, but the response can. To call the function, simply use , + prompt."
    
  if chat[1].lower() in ",del":
    return "This deletes a command, use the format, `,del promt`. Ensure to **not** use the , sign, like how you call a command."
    
  if chat[1].lower() in ",rand":
    return "This returns a random number between the 2 variables given, inclusive. Use the format, `,rand min max`. Otherwise it will give a random number from 1 - 10"

  return "We Don't Seem To Have A Help Function For That"

def developer():
    return "```$ONLINE TIME - INKBOT UPTIME\n$TIME EDIT - EDIT TIME +-\n$LIST COMMAND - LIST STORED COMMANDS\n$INSTALL INKBOT - SERVER INVITE LINK```"