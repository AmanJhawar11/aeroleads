
import requests
import re
import csv
import os
from time import sleep
import json  

s = requests.Session()  # Use a session for all requests
company_link = "https://www.linkedin.com/company/nestle-s-a-/"
output_file_name = "leads.csv"
pagination_delay = 5
cookies = 'li_rm=AQEJckaRoP2WewAAAZpYl1wqv3amtYuK-15eqjCsNZJJE8Z5dQWEA19N3Ob55hSfZegtoOCvIz7NtPhQ1qUhdKCENmxfrkNlkRseHY6tnYX5_NNSr1ObJScF; bcookie="v=2&33d51255-93a1-444d-8bff-dfa58abf5c9c"; bscookie="v=1&20251106095505ad5fb1d0-48e0-4c64-8aad-bf363a63a761AQFxD7EXZsyVHPkUYjaTxxCxMxYQiZsq"; aam_uuid=03643563616104153961015854858984425152; g_state={"i_l":0}; timezone=Asia/Calcutta; li_theme=light; li_theme_set=app; li_sugr=77feca1b-555a-4470-b51b-481495fea552; _guid=f3ec816a-61ce-42e9-92e8-8d399a91b4c2; AnalyticsSyncHistory=AQKVQUsXrei3JwAAAZpYmDy8czHWx-L75jCG2dXIfcLbKG8yUpF4VZHwNGB-ObNCS45LpFU2rQWl9s7BBBE6KA; _gcl_au=1.1.1270519494.1762422963; dfpfpt=921c6623fb694ac693134b1ddad09da3; lang=v=2&lang=en-us; li_gc=MTswOzE3NjI0MjUzMDQ7MjswMjEkA3lZ5YVd5iyAAHOCen0JcxUao2K85HprF0GyAySnAA==; li_alerts=e30=; li_at=AQEDAWEjuTIBzaWoAAABmli8KgAAAAGafMiuAE4ArlRsOb1yuB4aOwhXzWIbc4kfmmk8i_rAD2vUIy2Jp0tbHyguittxot1CedngPIMGFvxTpyZj4_6sS5ncgjGbzw4WYUqme2oU4EdO1bp8-AFqRTBz; liap=true; JSESSIONID="ajax:8888652255836212651"; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; fptctx2=taBcrIH61PuCVH7eNCyH0K%252fD9DJ44Cptuv0RyrXgXCvn5RscnqNTmnW34Zb4IGEPHW4fVxtCR9NxTI83PQN13XEjDI3kPDf5HpGad3SchKS7UqoF7%252fJw5cK8zy7Pt7%252bd1Lz%252fxCw%252fGxNMG%252fJTvW28zmzGy2cBaN0B%252b9awP%252fKKzl4WY3XXyPzZweTbhj3Uxg%252bT4LtfdE%252bWxEh%252beFygYPt8lox6ZLVqhILctkxz1Too6oCF%252bYV4Tde6myVFgvsnWguXjDMXxq%252b6IrZELMMvmabR74kpIlOdVkHqLUhhQUGqyAnq5GfeGhtECZXiqE0W5YLrvcUJM5Ys1ORtWM1TUbqwkMEx8v5N2O7R%252bV2KAWe1j%252f8%253d; lms_ads=AQF8cvwk5h3PSAAAAZpYvLbtEKcw0iioPgPmkJHsx2ffscvqqtfy7OkbgzEp08GsU4U3nuewKrSlTf3jKjTdGjhzIptkmMzC; lms_analytics=AQF8cvwk5h3PSAAAAZpYvLbtEKcw0iioPgPmkJHsx2ffscvqqtfy7OkbgzEp08GsU4U3nuewKrSlTf3jKjTdGjhzIptkmMzC; sdui_ver=sdui-flagship:0.1.19125+SduiFlagship0; UserMatchHistory=AQI_K0hg0xNUOwAAAZpaQjk2jrtA5lRukIeVRaEf745nqV0EbQvgYBiscnWtgQkpAA_f8-mkXuiwpb03Qr9KNC2IbX3013IHUmitKT-w5onSdWxfrdn3T_5OYsgGp2SrYHD3DARctcmaVcYeVonBwqBJJlq4ZKRIcq9OY2aaq_j_AVXw3XeRzyerebZrjMpydAHV5gVDIFCujNfxChMTo-i1aV_TfUhMjZs8QaFWX4pFrzhtHu5tsg2_sjze77tCCFwNmZmsAUChXfYcGFihg4M3Tsu07EdSGczoEwa082UmcJZF_0FCOrjtQ3povM9N8V0xKRh4eEB39fQp57prvIfqoTiAGfXGLqvTJOiozJiQtK1MxQ; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C20399%7CMCMID%7C04147127759365567831069083330972873995%7CMCAAMLH-1763055681%7C12%7CMCAAMB-1763055681%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1762458081s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1147430003; li_mc=MTsyMTsxNzYyNDc5MDM5OzE7MDIxUy6MeLuE/3jIV83v4fCh/z6OD7fvhW+nv6REr7HNZqg=; lidc="b=TB22:s=T:r=T:a=T:p=T:g=5243:u=2:x=1:i=1762479354:t=1762512710:v=2:sig=AQEvOd2a2avtsPteDsY8iP-1nzV0VA0F'


class LinkedIn:
    def __init__(self):
        self.fieldnames = ["Profile Link", "Name", "Designation", "Location"]
        self.results_list = []
    def save_results_to_csv(self):
        """
        Saves all collected data from self.results_list to the CSV file.
        This is called only ONCE at the end of the script.
        """
        if not self.results_list:
            print("No data to save.")
            return

        print(f"\nSaving {len(self.results_list)} records to {output_file_name}...")

        
        with open(output_file_name, mode='w', encoding='utf-8-sig', newline='') as csvFile:
            writer = csv.DictWriter(
                csvFile, fieldnames=self.fieldnames, delimiter=',', quotechar='"')
            
            writer.writeheader()
            
            writer.writerows(self.results_list)
        
        print(f"Successfully saved all data to {output_file_name}")

    @classmethod
    def getCompanyID(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Dnt': '1',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }
        try:
            
            resp = s.get(company_link, headers=headers).text
        except requests.exceptions.RequestException as e: # OPTIMIZED: Be specific in error handling
            print(f"Failed to open {company_link}. Error: {e}")
            return None
            
        try:
            companyID = re.findall(
                r'"objectUrn":"urn:li:organization:([\d]+)"', resp)[0]
        except IndexError: # error if pattern is not found
            print("Company ID not found in the page source.")
            return None
        return companyID

    def paginateResults(self, companyID):
        # Get the CSRF token from the cookie string robustly
        csrf_token = ""
        try:
            # Look for the JSESSIONID value, removing the quotes
            csrf_token = re.findall(r'JSESSIONID="(.+?)"', cookies)[0]
        except IndexError:
            print("Error: Could not find JSESSIONID in the cookie. Exiting.")
            return
            
        headers = {
            'Accept': 'application/vnd.linkedin.normalized+json+2.1',
            'Cookie': cookies,
            'Csrf-Token': csrf_token, # Use the extracted token
            'Dnt': '1',
            'Referer': f'https://www.linkedin.com/search/results/people/?currentCompany=%5B%22{companyID}%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH&page=2&sid=7Gd',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'X-Li-Lang': 'en_US',
            'X-Li-Page-Instance': 'urn:li:page:d_flagship3_search_srp_people_load_more;Ux/gXNk8TtujmdQaaFmrPA==',
            'X-Li-Track': '{"clientVersion":"1.13.9792","mpVersion":"1.13.9792","osName":"web","timezoneOffset":6,"timezone":"Asia/Dhaka","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.3125,"displayWidth":1920.1875,"displayHeight":1080.1875}',
            'X-Restli-Protocol-Version': '2.0.0',
        }
        
        for page_no in range(0, 20, 10):
            print(f"Checking facet: {page_no}/10")
            link = (
                f"https://www.linkedin.com/voyager/api/graphql?variables=(start:{page_no}"
                f",origin:COMPANY_PAGE_CANNED_SEARCH,query:(flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:currentCompany,value:List({companyID}))"
                f",(key:resultType,value:List(PEOPLE))),includeFiltersInResponse:false))"
                f"&queryId=voyagerSearchDashClusters.e1f36c1a2618e5bb527c57bf0c7ebe9f"
            )

            try:
                resp = s.get(link, headers=headers)
                resp.raise_for_status() # Raises error for bad responses (4xx, 5xx)
                results = resp.json().get('included', []) # Use .get with a default
            
            except requests.exceptions.RequestException as e:
                print(f"Failed to open {link}. Error: {e}")
                continue
            except json.JSONDecodeError:
                print(f"Failed to parse JSON from {link}. Response: {resp.text[:100]}...")
                continue
            
            if not results:
                print("No 'included' data on this page, or end of results.")
                break 

            for person_data in results:
                if person_data.get('$type') == "com.linkedin.voyager.dash.search.EntityResultViewModel":
                    
                    person_name = person_data.get('title', {}).get('text', 'N/A')
                    profile_link = person_data.get('navigationUrl', 'N/A')
                    designation = person_data.get('primarySubtitle', {}).get('text', 'N/A')
                    person_location = person_data.get('secondarySubtitle', {}).get('text', 'N/A')
                    
                    print(f"Profile Link: {profile_link}")
                    print(f"Name: {person_name}")
                    print(f"Designation: {designation}")
                    print(f"Location: {person_location}")
                    print()
                    
                    dataset_dict = {
                        "Profile Link": profile_link,
                        "Name": person_name,
                        "Designation": designation,
                        "Location": person_location
                    }
                    self.results_list.append(dataset_dict)

            print(f"Waiting for {pagination_delay} seconds")
            sleep(pagination_delay)


if __name__ == "__main__":
    companyID = LinkedIn.getCompanyID()
    if companyID is not None:
        linkedin = LinkedIn()
        linkedin.paginateResults(companyID)
        
        linkedin.save_results_to_csv()
