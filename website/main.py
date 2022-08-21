from flask import Flask, render_template, request, flash

app = Flask(__name__)

import json

def search_str(file_path, id):
    #print(id)
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if id in content:
            return True
        else:
            return False

def get_url(string):
  with open('Sign-Buddy-Hack-The-6ix-2022/data/WLASL_v0.3.json','r') as f:
    data = json.load(f)
    for i in data:
      if i['gloss'] == string:
        for j in range(20):
          instance_url = i['instances'][j]['url']
          if(search_str('Sign-Buddy-Hack-The-6ix-2022/data/missing.txt',i['instances'][j]['video_id']) == False):
            continue
          if('youtube' in instance_url):
            if(i['instances'][j]['frame_end'] == -1):
              return instance_url
    return False

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/learn')
def learn():
    return render_template("learn.html")

@app.route('/translate',methods=['GET','POST'])
def translate():
  if request.method == 'POST':
    test_1 = request.form.get("translate")
    vid = get_url(test_1)
    if(type(vid) == bool):

      return render_template("error.html")

    newVideo = vid.split("https://www.youtube.com/watch?v=")
    return render_template("translate.html", vid=newVideo[1])
  
  
  return render_template("translate.html", vid='DYjjcoTkNa0')

if __name__ == '__main__':
    app.run(debug=True) 

