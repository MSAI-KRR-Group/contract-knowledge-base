import urllib.request
from bs4 import BeautifulSoup

def get_license_name(url):

    try:
        page = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(page, features="html.parser")

        for svg in soup.find_all('svg'):
            if "octicon-law" in svg.get("class"):
                license_name = svg.parent.text.replace(" ", "").replace("\n", "")
                if "MIT" in license_name:
                    return "mit_license"
                elif "GPL" in license_name:
                    return "gnu_license"
                else:
                    return "<github_repo>"
    except:
        return 'Unsupported'