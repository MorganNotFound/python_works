from better_profanity import profanity
while True:
    censored_text = profanity.censor(input("请输入要处理的英文句子："))
    print(censored_text)
