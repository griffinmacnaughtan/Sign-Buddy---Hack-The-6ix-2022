from asyncio.windows_events import NULL
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
  with open('data\WLASL_v0.3.json','r') as f:
    data = json.load(f)
    for i in data:
      if i['gloss'] == string:
        for j in range(20):
          instance_url = i['instances'][j]['url']
          if(search_str('data\missing.txt',i['instances'][j]['video_id']) == False):
            continue
          if('youtube' in instance_url):
            if(i['instances'][j]['frame_end'] == -1):
              return instance_url
    
    return False
     
print(get_url('a'))

