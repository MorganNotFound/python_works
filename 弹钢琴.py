import winsound
tone={'1':532,'2':588,'3':660,'4':698,'5':784,'6':880,'7':998}
while True:
    winsound.Beep(tone[input()],300)