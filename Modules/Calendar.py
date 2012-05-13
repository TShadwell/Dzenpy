import abstract
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
name="calendar"
def getCal(last):
	soup= BeautifulSoup(urlopen("https://www.google.com/calendar/feeds/thomas.shadwell%40gmail.com/private-7b88f240e89d9ddd0fb3b6306d01addb/basic"))
	now=datetime.now()
	tomorrow=datetime.now()+timedelta(days=1)
	etoday=[x.title.string for x in soup.find_all('entry') if now.strftime("When: %a %d %b %Y") in x.summary.string]
	etomorrow=[x.title.string for x in soup.find_all('entry') if tomorrow.strftime("When: %a %d %b %Y") in x.summary.string]
	return("Today: " + ", ".join(etoday)+ " "if len(etoday) else "")+("Tomorrow: " + ", ".join(etomorrow)if len(etomorrow) else "")
display=abstract.Module(6000,getCal).display
