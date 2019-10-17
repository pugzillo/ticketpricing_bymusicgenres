import numpy as np
import pandas as pd
import requests


headers = {
    'client_id': 'MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ',
    'client_secret': '956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d'
}


url = 'https://api.seatgeek.com/2/'
headers = {
        'Content-Type':'application/x-www-form-urlencoded',
        'Authorization':'Basic '+basic_authorization_token,}
body = {
        'grant_type':'password',
        'username':stubhub_username,
        'password':stubhub_password,
        'scope':'PRODUCTION'}

r = requests.post(url, headers=headers, data=body)
print r
print r.text

token_respoonse = r.json()
# # Work
# curl https://api.seatgeek.com/2/events/721901?client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&client_secret=956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d
# curl https://api.seatgeek.com/2/events?client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&client_secret=956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d
# curl https://api.seatgeek.com/2/venues/632?client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&client_secret=956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d
# curl "https://api.seatgeek.com/2/venues?country=US?client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&per_page=10"
# curl "https://api.seatgeek.com/2/events?type=comedy&client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&per_page=10"
# curl "https://api.seatgeek.com/2/events?type=concert&client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&per_page=100"
# curl https://api.seatgeek.com/2/events?q=coachella -u MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ:956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d
# curl https://api.seatgeek.com/2/events?datetime_utc.gte=2012-04-01 -u MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ:956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d
# curl https://api.seatgeek.com/2/venues?country=US -u MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ:956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d
# curl https://api.seatgeek.com/2/performers?q=skrillex  -u MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ:956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d

# # No work
# curl https://api.seatgeek.com/2/events?datetime_utc.gte=2012-04-01&datetime_utc.lte=2012-04-30?client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&client_secret=956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d
# curl https://api.seatgeek.com/2/events?venue.state=NY?client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&client_secret=956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d
# curl https://api.seatgeek.com/2/events?datetime_utc=2012-06-12?client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&client_secret=956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d
# curl https://api.seatgeek.com/2/events?q=coachella?client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&client_secret=956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d
# curl https://api.seatgeek.com/2/performers?q=skrillex?client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&client_secret=956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d
# curl https://api.seatgeek.com/2/venues?city=rockford?client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&client_secret=956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d
# curl https://api.seatgeek.com/2/venues?country=US?client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&client_secret=956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d
# curl 'https://api.seatgeek.com/2/events?datetime_utc=2012-06-12?client_id=MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ&per_page=100'


