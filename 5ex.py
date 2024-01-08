'''Marvel Movie Character Creator
--
Do you like 'hanging around'?: No
Then you're not Spider-man

Do you have a 'gravelly'voice?: No
Aww,then you're not Korg

Do you often feel 'Marvelous'?:Yes
Aha! You're Captain Marvel!Hi!'''

ans1=input("Do you like 'hanging around'?:")
if ans1 == "yes":
 print("Then you're Spider-man")
else:
 print("Then you're not Spider-man")
 ans2= input("Do you have a 'gravelly'voice?:")
 if ans2=="yes":
  print("Aww,then you're  Korg")
 else:
  print("Aww,then you're not Korg")

  ans3=input("Do you often feel 'Marvelous'?:")
  if ans3=="yes":
   print("Aha! You're Captain Marvel!Hi!")
  else:
   print("Aha! You're  not Captain Marvel!Hi!")
