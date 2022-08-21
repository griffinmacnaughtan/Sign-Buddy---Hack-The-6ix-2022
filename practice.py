import random, string

def random_letter(): #for easy practice mode
    x = list(string.ascii_lowercase)
    y = random.choice(x)
    return y

def random_word(): #for hard practice mode(future implementation)
    line = random.choice(open('data\wlasl_class_list.txt').readlines())
    line.split("\t")[-1]
    i = 0
    for i in range(5):
        if line[i] == '\t':
            break
        i+=1
    x = line[i+1:]
            
    return x

def check_attempt(randomWord, webcamGesture):
    randomWord = randomWord.strip()
    webcamGesture = webcamGesture.strip()
    if webcamGesture == randomWord:
        return True
    else:
        return False
    
print(random_letter())