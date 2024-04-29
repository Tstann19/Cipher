import sys

new_message=""
counter=0
line=0

shift=int(sys.argv[1])
text=sys.stdin.read()

for char in text:
  if char.isalpha():
    char=char.upper()
    shifted_char=chr((ord(char)-65 + shift)%26+65)
    new_message+=shifted_char
    counter+=1
    line+=1

    if counter==5:
      new_message+=" "
      counter=0
    if line==50:
      new_message+="\n"
      line=0

print(new_message)