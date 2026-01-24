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


def scrape_multiple_websites(website_list):
    """
    Scrapes emails from multiple websites and exports results.
    """
    all_results = []
    total_emails_before_dedup = 0
    seen_emails = set()  # Track unique emails across all sites
    duplicates_removed = 0
    
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
                total_emails_before_dedup += 1
                
                # Check for duplicates
                if email not in seen_emails:
                    seen_emails.add(email)
                    all_results.append({
                        'email': email
                    })
                else:
                    duplicates_removed += 1
                    print(f"    ⚠ Duplicate removed: {email}")
        else:
            print(f"  ℹ No emails found")
        
        print()
    
    # Export to CSV
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"scraped_emails_{timestamp}.csv"
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in all_results:
            writer.writerow(row)
    
    # Summary
    print(f"\n{'='*80}")
    print(f"SCRAPING COMPLETE")
    print(f"{'='*80}")
    print(f"Total websites scraped: {len(website_list)}")
    print(f"Total emails found (before dedup): {total_emails_before_dedup}")
    print(f"Duplicates removed: {duplicates_removed}")
    print(f"Unique emails exported: {len(all_results)}")
    print(f"Results exported to: {filename}")
    print(f"{'='*80}\n")
    
    return all_results


if __name__ == "__main__":
    websites = [
        "https://www.atomica.com/",
        "https://www.brandnew.net/",
        "https://www.intriplex.com/",
        "http://www.minhantech.com/",
        "http://www.condormachining.com/",
        "http://metalsupply.us/",
        "https://www.bardex.com/",
        "http://www.aboveallcnc.com/",
        "https://www.sbtool.com/",
        "https://polamprecision.com/",
        "http://www.kordaandgeis.com/contact.htm",
        "https://sbcontrol.com/",
        "http://www.enerpro-inc.com/",
        "https://www.physics.ucsb.edu/pro-machine-shop",
        "http://www.cncmachining.com/",
        "https://spracher.com/",
        "http://www.burnetmachining.com/",
        "http://www.inovati.com/",
        "https://www.zymbit.com/",
        "http://www.santabarbaraautomation.com/",
        "http://bentleywood.com/",
        "http://www.stinnerframeworks.com/",
        "http://www.mirmar.com/",
        "http://www.seir.com/",
        "http://bw-environmental.com/",
        "http://www.tetratech.com/",
        "https://www.dudek.com/",
        "http://www.woodenvironmental.com/",
        "https://bren.ucsb.edu/",
        "https://purifiedenvironments.com/?utm_source=google&utm_medium=organic&utm_campaign=gbp-listing",
        "http://www.aecom.com/",
        "http://www.everettassociates.net/",
        "https://www.esassoc.com/",
        "https://www.cardno.com/",
        "https://www.yorkeengr.com/",
        "http://www.soilmoisture.com/",
        "http://www.watershedenvironmental.com/contact/",
        "https://www.wilsonenv.com/",
        "http://engineering.ucsb.edu/",
        "https://www.countyofsb.org/414/Environmental-Health",
        "https://inovati.com/",
        "https://www.langan.com/",
        "http://www.edcnet.org/",
        "http://www.amecfw.com/",
        "http://www.earthsystems.com/",
        "http://www.campbellgeo.com/",
        "https://bosl.ucsb.edu/",
        "http://egrgeotech.com/",
        "https://cee.stanford.edu/",
        "http://www.flowersassoc.com/",
        "http://millennium-ehs.com/",
        "https://www.stantec.com/en/offices/united-states-locations/california-offices-filtered/santa-barbara-california-office?utm_source=google-business-profile&utm_medium=organic&utm_campaign=website-gbp_listing_united-states&utm_content=california_santa-barbara",
        "https://cee.sjsu.edu/",
        "https://www.aquaflo.com/goleta",
        "http://www.safeenv.com/",
        "https://www.sveginc.com/",
        "http://www.msi.ucsb.edu/",
        "http://www.chemengr.ucsb.edu/",
        "http://www.goletaplumber.net/",
        "https://rivieraplumbing.com/",
        "http://mrrooter.com/santa-barbara-county",
        "https://ezflowdrains.com/",
        "http://www.drainmasters805.com/",
        "http://apexplumbingsb.com/",
        "http://www.luigicrisaplumbing.com/",
        "http://mlwdis.com/",
        "http://www.servicenowsantabarbara.com/",
        "https://dhrhconstruction.com/",
        "http://www.missionplumbingsb.com/",
        "https://www.carrollplumbingsb.com/",
        "https://www.lewisplumbingsantabarbara.com/",
        "https://www.coastplumb.com/",
        "https://www.lopez-plumbing.com/",
        "https://silverleafsb.com/",
        "https://www.caldwellconstruction.com/",
        "https://andersys.com/",
        "https://toroconstructionsantabarbara.com/?utm_source=GMB&utm_medium=Organic&utm_campaign=Toro+Construction",
        "https://www.servpro.com/locations/ca/servpro-of-santa-barbara?utm_medium=organic&utm_source=gbp",
        "http://www.keaplumbing.com/",
        "https://www.911restorationsantabarbara.com/",
        "https://www.qwikresponse.com/",
        "https://www.leeandsonsplumbingandheating.com/",
        "https://petesdrywall.com/",
        "http://anacapaplumbing.com/",
        "https://electriciansantabarbara.com/?utm_source=google&utm_medium=organic&utm_campaign=google_my_business&utm_id=electrician_santabarbara",
        "https://sartainemergencyplumbing.com/",
        "http://athenacontractors.net/contact_us.html",
        "https://www.macalusopools.com/",
        "http://rinconplumbing.net/",
        "https://wightons.com/",
        "https://www.rjcarrollplumbing.com/",
        "https://www.eliterooter.com/location/santa-barbara/?utm_source=google&utm_medium=organic&utm_campaign=gmb",
        "https://santabarbarawaterfalls.com/",
        "https://www.rootersolutions.com/?utm_source=GMB&utm_medium=organic&utm_campaign=santabarbara",
        "http://castleconstructionofsb.com/",
        "https://www.sbhandyman805.com/",
        "http://www.sbplumbing.com/",
        "http://www.sanginitiplumbing.net/",
        "https://www.homedepot.com/l/Goleta/CA/Goleta/93117/6623/services?emt=HSGMBGoogleMaps",
        "https://remodelsbyelite.com/",
        "http://www.pacificplumbingsb.com/",
        "http://sunnysocalplumbersantabarbaraca.com/",
        "https://www.channelplumbingsb.com/",
        "https://tokarevbs.com/",
        "http://www.stewartsderooting.com/",
        "http://www.glscompanies.net/",
        "https://www.specialtyplumbingsb.com/",
        "http://homefurnacecompany.com/",
        "https://constructionind.com/",
        "https://metropha.com/",
        "https://www.kellowconstruction.com/?utm_medium=gmb&utm_source=google_profile&utm_campaign=gmb",
        "https://thecharmingplumber.com/",
        "https://www.skyelineinc.com/",
        "http://maccodreams.com/",
        "https://swissdesignsconstruction.com/",
        "http://seguroconstruction.com/",
        "https://www.acehandymanservices.com/",
        "http://phils-plumbing.com/",
        "https://jcplumbingsupply.biz/",
        "https://curtlaniniplumbingandheating.com/",
        "https://www.ferguson.com/store/ny/medford/plumbingpvf-3518?utm_source=google&utm_medium=organic&utm_campaign=rt_lis_listingtraffic&utm_content=listing",
        "https://www.allcityplumbing4u.com/?utm_source=googlebusinessprofile&utm_medium=organic&utm_campaign=ranchocucamongagbp",
        "https://www.heritagehomeandplumbing.com/",
        "http://aaronsplumbing.biz/",
        "https://fixaleak.org/?utm_source=google&utm_medium=organic&utm_campaign=GMBListing-Bohemia-NY",
        "https://www.heisesplumbing.com/",
        "https://rc-plumbing-solutions.com/",
        "http://riosplumbingsantabarbara.com/"
    ]
    
    results = scrape_multiple_websites(websites)