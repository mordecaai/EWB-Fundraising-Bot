import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import re
import csv
from datetime import datetime

def scrape_emails(url):
    try:
        # Send GET request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        emails = set()
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            
            if href.startswith('mailto:'):
                email = href.replace('mailto:', '').split('?')[0]
                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                    emails.add(email)
        
        return emails
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return set()
    except Exception as e:
        print(f"An error occurred: {e}")
        return set()
""""
if __name__ == "__main__":
    # Get URL from user
    website_url = input("Enter the website URL: ")
    
    # Scrape emails
    print(f"\nScraping emails from: {website_url}")
    found_emails = scrape_emails(website_url)
    
    # Display results
    if found_emails:
        print(f"\nFound {len(found_emails)} email address(es):")
        for email in sorted(found_emails):
            print(f"  - {email}")
    else:
        print("\nNo email addresses found.")
"""


# ... (keep your existing scrape_emails function as is) ...

# Add this new function after your scrape_emails function:
def scrape_multiple_websites(website_list):
    """
    Scrapes emails from multiple websites and exports results.
    """
    all_results = []
    total_emails = 0
    
    print(f"\n{'='*80}")
    print(f"Starting scrape of {len(website_list)} websites...")
    print(f"{'='*80}\n")
    
    for i, url in enumerate(website_list, 1):
        print(f"[{i}/{len(website_list)}] Scraping: {url}")
        
        emails = scrape_emails(url)
        
        if emails:
            print(f"  ✓ Found {len(emails)} email(s):")
            for email in sorted(emails):
                print(f"    - {email}")
                all_results.append({
                    'website': url,
                    'email': email
                })
                total_emails += 1
        else:
            print(f"  ℹ No emails found")
        
        print()
    
    # Export to CSV
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"scraped_emails_{timestamp}.csv"
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['website', 'email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in all_results:
            writer.writerow(row)
    
    # Summary
    print(f"\n{'='*80}")
    print(f"SCRAPING COMPLETE")
    print(f"{'='*80}")
    print(f"Total websites scraped: {len(website_list)}")
    print(f"Total emails found: {total_emails}")
    print(f"Results exported to: {filename}")
    print(f"{'='*80}\n")
    
    return all_results


# Replace your existing if __name__ == "__main__": block with this:
if __name__ == "__main__":
    websites = [
        "https://www.goletaengineering.com/",
        "http://www.bengalengineering.com/",
        "http://fecivil.com/",
        "http://www.klvse.com/",
        "http://www.aecom.com/",
        "http://www.multiplex-engineering.com/",
        "https://www.cushmancontracting.com/",
        "http://www.aaeng.com/",
        "http://www.vansandestructural.com/",
        "http://www.psfeg.com/",
        "http://www.wmsurveysinc.com/",
        "https://www.caldwellconstruction.com/",
        "https://ashleyvance.com/",
        "https://craddock.biz/",
        "http://www.obrienwall.com/",
        "https://www.geosyntec.com/",
        "https://www.stantec.com/en/offices/united-states-locations/california-offices-filtered/santa-barbara-california-office",
        "https://www.meceng.com/",
        "http://www.flowersassoc.com/",
        "http://www.smithengineering.net/",
        "https://www.windwardeng.com/",
        "http://www.mnsengineers.com/",
        "https://www.doyle-morgan.com/",
        "http://www.greerse.com/",
        "http://doyle-morgan.com/",
        "http://www.19six.com/",
        "http://www.jmpe.net/",
        "https://aneng.com/",
        "http://www.smithstructural.com/",
        "http://egrgeotech.com/",
        "http://www.studioengineersinc.com/",
        "http://wwsurveying.com/",
        "https://www.bbb.org/local-bbb/bbb-of-the-tri-counties",
        "https://www.ideaengineering.com/",
        "https://puebloconstruction.net/",
        "http://www.kenneyconstruction.com/",
        "http://www.cecelectricalservices.com/",
        "https://www.cardno.com/",
        "http://www.drs-engineering.net/",
        "http://www.rjreng.com/",
        "http://www.lewis-engineering.com/",
        "http://www.fmcassoc.com/",
        "http://thesysoncorp.com/",
        "https://www.yorkeengr.com/",
        "http://yceinc.com/",
        "http://www.3ceng.com/",
        "http://www.pacificcoastcivil.com/",
        "https://pasquiniengineering.com/",
        "http://www.joseph-engineering.com/",
        "https://www.lcegroupinc.com/",
        "http://www.wallacegroup.us/",
        "http://www.tsstructural.com/",
        "http://shawnpierceengineering.com/",
        "http://jtengineering.com/",
        "http://luminare-design.com/",
        "https://fieldenengineeringgroup.com/",
        "http://www.villafanaengineering.com/",
        "http://www.tartaglia-engineering.com/",
        "https://impactrecruitment.com/contact",
        "http://www.garingtaylor.com/",
        "http://www.thengineers.com/",
        "https://www.infratechengineering.com/",
        "https://www.superstructures.com/",
        "https://parkerresnick.com/",
        "http://www.de-simone.com/",
        "https://achieveengineer.com/",
        "http://www.mpengs.com/",
        "http://www.jbb.com/",
        "http://allcityengineering.com/",
        "http://www.davidreithandassoc.com/",
        "http://www.artisanengineering.biz/",
        "http://www.samschwartz.com/",
        "http://www.greystoneeng.com/",
        "http://www.52engineering.com/"
    ]
    
    results = scrape_multiple_websites(websites)