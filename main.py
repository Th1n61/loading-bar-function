import time, os
test_percent=0# for test purposes
run = True#also for test purposes
print('\033[?25l')
os.system("clear")
def loader(percent,top_padding):
  bar = ''
  if percent == 100:
    print('\n'*top_padding)
    print('['+"\033[32m"+'████████Done████████'+"\033[0m"+']100%')
    print('\033[?25l')
    return
  print('\n'*top_padding)
  boo=(round(percent//5))
  bar+='['
  for i in range(0,20):
    if i < boo:
      bar+=("\033[34m"+'█'+"\033[0m")
    else:
      bar+=(' ')
  bar+=']'
  if percent < 10:
    bar+=('  '+str(percent)+'%')
  else:
    bar+=(' '+str(percent)+'%')
  print(bar)
        
while run:# testing function
  time.sleep(0.3)
  os.system("clear")
  if test_percent == 100:
    run =  False
  loader(test_percent,3)
  test_percent+=1
