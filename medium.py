import csv
import json
import pandas as pd 
import datetime
from pathlib import Path

# You'll first need to sign in to your account, then you can access this URL without issues: 
#   https://medium.com/@chrishoina/stats/total/1548525600000/1668776608433
#    NOTES:
#       Replace the "@chrishoina" with your own username 
#       The two numbers you see are Unix Epochs; you can modify those as needed, 
#       in my case I wanted to see:
#           * 1548525600000 - At the time of this post, this seems to whenever you first post was published, or when 
#             you first created a Medium account. In this case, for me this was Sat, Jan/26/2019 6:00:00PM - GMT
#           * 1665670606216 - You shouldn't need to change this, since it will just default to the present date. 

# Step 1 - convert this to a,(.txt) file
p =  Path("/Users/choina/Documents/socialstats/1668776608433.json")
p.rename(p.with_suffix('.txt'))

# Step 2 - Now "read" in that text file, and remove those pesky characters/artifacts from position 0 through position 15. Which means, you'll be retaining everything from position 16 onward. Because this is the actual JSON payload I'm interested in.

with open("/Users/choina/Documents/socialstats/1668776608433.txt", "r") as f:
    stats_in_text_file_format = f.read()

# This [16:] essentially means, grab everything that is in this range. Since there is nothing after the colon, it will just default to the end (which is what I want in this case).
    
    cleansed_stats_from_txt_file = stats_in_text_file_format[16:]

    print(cleansed_stats_from_txt_file)

# This took me a day to figure out, but this text file needs to be encoded properly, so it can be saved as a JSON file (which is what is about to happen). I always forget this, but I do know that the json.dumps = dump string, which json.dump = dump object. There is a difference, I'm not the expert, but the docs were helpful. 
    json.dumps(cleansed_stats_from_txt_file)

# Step 3 - Here I create a new file, then indicate we are going to "w"rite to it. Here we just take the progress from Step 2 and apply it here. 

with open('medium_stats_ready_for_pandas.json', 'w') as f:
    f.write(cleansed_stats_from_txt_file)

# Step 4 - Onto Pandas! We've already imported the pandas library as "pd"
# We first create a data frame, and name the columns. I kept the names very similar to avoid confusion. I feared that timestampMs might be a reserved word in Oracle DB, or just too close, so I renamed it. 

df = pd.DataFrame(columns=['USERID', 'FLAGGEDSPAM', 'STATSDATE', 'UPVOTES', 'READS', 'VIEWS', 'CLAPS', 'SUBSCRIBERS'])  

with open("/Users/choina/Documents/socialstats/medium_stats_ready_for_pandas.json", "r") as f: 
    data = json.load(f)
    data = data['payload']['value']

    print(data)

for i in range(0, len(data)):
    df.loc[i] = [data[i]['userId'], data[i]['flaggedSpam'], data[i]['timestampMs'], data[i]['upvotes'], data[i]['reads'], data[i]['views'], data[i]['claps'], data[i]['updateNotificationSubscribers']]

df['STATSDATE'] = pd.to_datetime(df['STATSDATE'], unit="ms")

print(df.columns)
print(df.head)

# Step 5 - Saving this as a csv file. It is now ready to drop into my Autonomous Database. You can do this manually, or if you were really smart you could create a table, REST-enable it and then POST to it via a cURL command or a Python POST request. 

with open("medium_stats_ready_for_database_update.csv", "w") as f:
    df.to_csv(f, index=False, header=True)






# url = '[ORDS Endpoint]' 

# # import mimetypes

# # with open('/Users/choina/Documents/socialstats/pandasdf.csv', 'r') as f:
# #     mimetypes.read_mime_types
# #     mimetypes.guess_type('/Users/choina/Documents/socialstats/pandasdf.csv')
# #     print(mimetypes.readfp('file: /Users/choina/Documents/socialstats/pandasdf.csv'))

# # r = requests.post(url)
# # print(r.raise_for_status)
# # print(r.text)
# # print(r.content)
# # print(r.headers)

# # r = requests.get(url)
# # r.headers
# # r.cookies

# files = (open('pandasdf.csv', 'rb'), 'text/csv')

# import requests
# import csv 

# url = '[ORDS Endpoint]'  

# with open('pandasdf.csv', 'rb') as f:
#     data = f.read()

# headers = {'Content-Type': 'text/csv','accept': 'application/json'}
# r = requests.post(url, data=data, headers=headers)

# print(r.status_code)
# print(r.content)
# print(r.text)

# files = f
# headers = {"Content-Type": "text/csv"}

# print(r.text)

# files = {'file:' (open('/Users/choina/Documents/socialstats/pandasdf.csv', 'rb'))}

# import csv 

# with open('pandasdf.csv', 'r') as file:
#     csv_reader = csv.reader(file)

#     for line in csv_reader:
#         print(line[2])

#     print(csv_reader)
