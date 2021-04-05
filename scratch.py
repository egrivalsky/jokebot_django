# import datetime
# from datetime import timedelta, datetime
# import time



# now = datetime.now()

# formattedDate = now.strftime("%j")

# print(formattedDate)


from pynytimes import NYTAPI
nyt = NYTAPI('FtZ0xW7RIZ9wRxJJiR02MNv37ChQGZPO', parse_dates=True)

response = nyt.most_viewed(days = 30)

print(response[0].split(','))
# print(first['adx_keywords'].split(';')[0:2])
# print(list(first['adx_keywords'].split(';')))



