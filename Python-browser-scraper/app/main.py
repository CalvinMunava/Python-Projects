import re
import requests
from database import Database
from bs4 import BeautifulSoup
from classes.name_model import Name,Surname

def scrapeNames():
    print("Scraping Names")
    try:
        data = []  # Initialize an empty list
        # URL to scrape
        url = "https://www.ancestors.co.za/database/trees/firstnames-all.php?tree="

        print("********Submitting Request********")
        # Send GET request to the URL
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, verify=False, timeout=30)

        # Check if request was successful
        if response.status_code == 200:
            print("********Successful Response********")
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all div elements with class "titlebox"
            title_boxes = soup.find_all('div', class_='titlebox')

            print("********Starting Loop of Names********")
            for title_box in title_boxes:
                # Find all td elements within the current titlebox
                name_elements = title_box.find_all('td', class_='sncol')

                # Iterate over each name element
                for name_element in name_elements:
                    # Find all <a> tags within the current name element
                    name_links = name_element.find_all('a')

                    # Check if any <a> tags are found
                    if name_links:
                        # Iterate over each <a> tag
                        for name_link in name_links:
                            # Extract name from the <a> tag
                            name_text = name_link.text.strip()


                            # Skip names starting with "??", empty names, or single-character names
                            if name_text.startswith("??") or not name_text or len(name_text) == 1:
                                continue
                            else:                               
                                # Extract occurrences from the text within the <td> element
                                text_content = name_element.get_text(separator='|').strip()
                                lines = text_content.split('\n')
                                # print("Text content:", text_content)

                                for line in lines:
                                    line = line.strip()           
                                    if line:
                                        parts = line.split('|')                                    
                                        # Extract name and occurrences
                                        name_text = str(parts[1].strip()).replace("'", "''")  # Extract the name

                                        occurrences = parts[2].strip() # Extract the occurrences and convert to integer
                                        occourances_stripped = occurrences.strip('()')
                                        occourances_int = 1
                                        try:
                                            occourances_int = int(occourances_stripped)
                                        except ValueError:
                                            pass
                                        # Create Name object and append to data list
                                        name = Name(name=name_text, nameCount=occourances_int)
                                        data.append(name)             
            # Breakout Print
            print("********Ended Loop of Names********")

            if len(data) > 0:
                # Filter and count unique names
                unique_names = {}  # Dictionary to store unique names with counts
                for name in data:
                    # Skip names with zero occurrences or single characters
                    if name.nameCount > 0 and len(name.name) > 1:
                        # Strip special characters and leading/trailing spaces from the name
                        cleaned_name = name.name.strip(' "*')

                        # Strip '*' from the name
                        cleaned_name = cleaned_name.replace('*', '')

                        cleaned_name = cleaned_name.replace('.', '')

                        # Add cleaned_name to unique_names dictionary with its count
                        cleaned_name = cleaned_name.strip()  # Trim leading and trailing spaces
                        if cleaned_name not in unique_names:
                            unique_names[cleaned_name] = name.nameCount
                        else:
                            # If name already exists, increment its count
                            unique_names[cleaned_name] += name.nameCount
                # Add to Database
                db = Database()
                for name, count in unique_names.items():
                    sql_insert = f"""INSERT INTO [dbo].[CustomerNames] ([name], [nameCount]) VALUES ('{name}', {count})"""
                    db.insert(sql_insert)

        else:
            print("Failed to retrieve data from the URL.")
            print("Error :" + str(response.text))
    except ConnectionError as ce:
        print("Connection Error Occurred: " + str(ce))
    except Exception as e:
        print("Exception Occurred : " + str(e))


def scrapeSurNames():
    print("Scraping Surnames")
    try:
        data = []  # Initialize an empty list
        # URL to scrape
        url = "https://www.ancestors.co.za/database/trees/surnames-all.php?tree="

        print("********Submitting Request********")
        # Send GET request to the URL
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, verify=False, timeout=30)

        # Check if request was successful
        if response.status_code == 200:
            print("********Successful Response********")
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all div elements with class "titlebox"
            title_boxes = soup.find_all('div', class_='titlebox')

            print("********Starting Loop of Surnames********")
            for title_box in title_boxes:
                # Find all td elements within the current titlebox
                name_elements = title_box.find_all('td', class_='sncol')

                # Iterate over each name element
                for name_element in name_elements:
                    # Find all <a> tags within the current name element
                    name_links = name_element.find_all('a')

                    # Check if any <a> tags are found
                    if name_links:
                        # Iterate over each <a> tag
                        for name_link in name_links:
                            # Extract name from the <a> tag
                            name_text = name_link.text.strip()


                            # Skip names starting with "??", empty names, or single-character names
                            if name_text.startswith("??") or not name_text or len(name_text) == 1:
                                continue
                            else:                               
                                # Extract occurrences from the text within the <td> element
                                text_content = name_element.get_text(separator='|').strip()
                                lines = text_content.split('\n')
                                # print("Text content:", text_content)

                                for line in lines:
                                    line = line.strip()           
                                    if line:
                                        parts = line.split('|')                                    
                                        # Extract name and occurrences
                                        name_text = str(parts[1].strip()).replace("'", "''")  # Extract the name

                                        occurrences = parts[2].strip() # Extract the occurrences and convert to integer
                                        occourances_stripped = occurrences.strip('()')
                                        occourances_int = 1
                                        try:
                                            occourances_int = int(occourances_stripped)
                                        except ValueError:
                                            pass
                                        # Create Name object and append to data list
                                        name = Surname(surname=name_text, surnameCount=occourances_int)
                                        data.append(name)             
            # Breakout Print
            print("********Ended Loop of Surnames********")

            if len(data) > 0:
                # Filter and count unique names
                unique_names = {}  # Dictionary to store unique names with counts
                for name in data:
                    # Skip names with zero occurrences or single characters
                    if name.surnameCount > 0 and len(name.surname) > 1:
                        # Strip special characters and leading/trailing spaces from the name
                        cleaned_name = name.surname.strip(' "*')

                        # Strip '*' from the name
                        cleaned_name = cleaned_name.replace('*', '')

                        cleaned_name = cleaned_name.replace('.', '')

                        # Add cleaned_name to unique_names dictionary with its count
                        cleaned_name = cleaned_name.strip()  # Trim leading and trailing spaces
                        if cleaned_name not in unique_names:
                            unique_names[cleaned_name] = name.surnameCount
                        else:
                            # If name already exists, increment its count
                            unique_names[cleaned_name] += name.surnameCount
                # Add to Database
                db = Database()
                for name, count in unique_names.items():
                    sql_insert = f"""INSERT INTO [dbo].[CustomerSurname] ([surname], [surnameCount]) VALUES ('{name}', {count})"""
                    db.insert(sql_insert)

        else:
            print("Failed to retrieve data from the URL.")
            print("Error :" + str(response.text))
    except ConnectionError as ce:
        print("Connection Error Occurred: " + str(ce))
    except Exception as e:
        print("Exception Occurred : " + str(e))



if __name__ == '__main__': 
    scrapeNames()
    scrapeSurNames()



