# Sign Buddy
### Raymond Li, Griffin MacNaughtan, Rijin Muralidharan, Girik Setya 
### Created During Hack The 6ix 2022
---

Welcome to Sign Buddy! This site was created to help more people learn sign language. This is both a fun skill to learn and a way to improve the quality of life of approximately 70 million people worldwide who depend on sign language as their main form of communication.

#### How to use:
...

#### Technologies: 
Python, Flask, Bootstrap

#### Methodologies:
The front end of this project was created using Flask and Bootstrap. The two features that are used for site functionality are Buddy learn 📚 and Buddy translate🤖. Learn takes a webcam input from the user and uses an AI model to determine which sign is being shown. This was created using... 


Translate takes a keyboard input and if the entered word is present in our dataset of 2000 words, plays a video of that word being signed. This was created using custom made functions in Python that parse the WLASL (World Level American Sign Language) Video DataSet of over 12,000 instances of common signs and chooses a suitable video.

#### Issues We Ran Into
Data collection:



#### Next Steps:
When looking forward, this project has a bright future! First of all, we ran out of time to implement a practice feature, which gives the user a random word from the dataset. The user is then prompted to enter a sign into the webcam and tries to sign the given word. Next, due to our scope and time constraints, we decided to train our AI model with a limited dataset compared to our available words, as more dynamic signs were harder to track and train. The 12,000 instances of words in the WLASL are a perfect dataset that will be able to train a model that can handle more dynamic and complex gestures. This idea can also be brought to mobile devices, as it would be a fitting feature for language learning apps such as DuoLingo.

#### References:

