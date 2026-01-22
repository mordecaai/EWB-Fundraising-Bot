import re
import requests
from bs4 import BeautifulSoup

EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

def find_all_emails(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    emails = set(re.findall(EMAIL_REGEX, text))

    for link in soup.find_all("a", href=True):
        if link["href"].startswith("mailto:"):
            email = link["href"].replace("mailto:", "").split("?")[0]
            emails.add(email)

    return emails
