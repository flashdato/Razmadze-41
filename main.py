from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from html import escape
import requests
import sys
import os

def has_text_align_start_style(tag):
    return tag.has_attr('style') and 'text-align:start' in tag['style']

# facebook_email = "9al7d7zos@mozmail.com"
# facebook_pass = "yj,shydk!;5;nHX"

options = Options()
options.headless = True
options.add_experimental_option("detach", True)

# Use ChromeDriverManager to automatically download and manage ChromeDriver
driver = webdriver.Chrome(options=options)

print("please input values exactly as requested!")
last_news_id = int(input("Input last news number"))
path_to_news_image_folders = input("Input news image folder (./images/news/)(for security)")
path_to_news_feed_files = input("Input path to news feed files like news_1.html (./News_Feed/)(for security)")

post_links = []
with open('links.txt', 'r') as file:
    post_links = file.readlines()
if(len(post_links) == 0):
    print("No Links Given!")
    finish()
first_image_link = ""
image_links = []
paragraphs = []
num_of_images = 0


def finish():
    driver.quit()
    sys.exit(0)

def download_image(image_url, save_path, filename):
    os.makedirs(save_path, exist_ok=True)
    response = requests.get(image_url)
    image_saved = False
    if response.status_code == 200:
        with open(os.path.join(save_path, filename), 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded and saved as {filename}")
        image_saved = True
    else:
        print("!!!Failed to download image!!!")
        print(f"the faulty image: {image_url}")
    if image_saved is True:
        return save_path
    else:
        return image_url


def write_html_for_given_details(paragraphs, image_links):
    global last_news_id
    global path_to_news_feed_files
    global path_to_news_image_folders
    html_content = """
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <title>სიახლე</title>
        <meta name="description" content="" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="stylesheet" href="/style.css" />
        <link rel="icon" type="image/x-icon" href="/images/logo3.png" />
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA=="crossorigin="anonymous" />
        <script>
            $(function () {
                $("#Nav").load("/NavBar/NavBar.html");
            });
            $(function () {
                $("#Footer").load("/Footer/Footer.html");
            });
        </script>
    </head>
    <body>
    <div id="Nav"></div>

    <div class="box">
        <div class="about">
            <div class="content1">
                <div class="title">სიახლე</div>
    """
    for paragraph in paragraphs:
        html_content = html_content + '<p class="infotext">' + str(paragraph) + "</p>\n" 
    html_content = html_content + "<br />\n"
    if len(image_links) != 0:
        html_content = html_content + '<div class="image-grid">'
        for index,image_link in enumerate(image_links):
            path_to_save_to = path_to_news_image_folders + "news_" + str(last_news_id) +"/" 
            filename_to_save_as = "news_" + str(last_news_id) + "_" + str(index) + ".jpg"
            new_image_link = download_image(image_link,path_to_save_to,filename_to_save_as)
            html_content = html_content + '<div class="image-box">\n'
            html_content = html_content + '<img src="/images/news/news_' + str(last_news_id) + '/news_' + str(last_news_id) + '_' + str(index) + '.jpg" alt = "Image ' + str(index) + '" class="grid-image" />\n</div>\n'
        html_content = html_content + '</div>'
    html_content = html_content + """ 
        <div class="overlay" id="overlay">
                        <div class="modal" id="modal">
                            <img src="" alt="Zoomed Image" id="zoomed-image" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <hr />
        <div id="Footer"></div>
        <script>
            // JavaScript
            const overlay = document.getElementById("overlay");
            const modal = document.getElementById("modal");
            const zoomedImage = document.getElementById("zoomed-image");

            // Function to open the zoomed image
            function openImage(src) {
                zoomedImage.src = src;
                overlay.style.display = "block";
                document.documentElement.style.overflow = "hidden"; // Disable scrolling
                document.body.style.overflow = "hidden"; // Disable scrolling
            }

            // Function to close the zoomed image
            function closeImage() {
                overlay.style.display = "none";
                document.documentElement.style.overflow = ""; // Enable scrolling
                document.body.style.overflow = ""; // Enable scrolling
            }

            // Add a click event listener to the overlay to close the image when clicking outside
            overlay.addEventListener("click", closeImage);

            // Prevent the click event on the modal from closing the image
            modal.addEventListener("click", function (event) {
                event.stopPropagation();
            });

            // Example usage to open the image
            const imageBoxes = document.querySelectorAll(".image-box");

            imageBoxes.forEach(function (imageBox) {
                const imageSrc = imageBox.querySelector("img").src;
                imageBox.addEventListener("click", function () {
                    openImage(imageSrc);
                });
            });
        </script>
    </body>

    </html>
    """
    
    with open(path_to_news_feed_files+"news_"+str(last_news_id)+".html","w") as file:
        file.write(html_content)
    print("HTML file generated successfully for news_" + str(last_news_id))




def next_post():
    global paragraphs
    global image_links
    write_html_for_given_details(paragraphs, image_links)
    global post_links
    if len(post_links) == 2:
        finish()
    post_links = post_links[2:]
    start_scrape(post_links[0])


def photo_phase2():
    global first_image_link
    global image_links
    global num_of_images
    print("in photo phase...")

    soup = BeautifulSoup(driver.page_source, "html.parser")

    images = soup.find_all("img")
    time.sleep(1)
    for image in images:
        
        width = image.get("width")
        height = image.get("height")
        if(width is None or height is None):
            if(image.get("src") == first_image_link):
                next_post()
            print(image.get("src"))
            if image.get("src") not in image_links:
                image_links.append(image.get("src"))
            if len(image_links) == num_of_images:
                next_post()
            break
        if(width == "100%" or height == "100%"):
            continue
        if width is not None and height is not None and int(width) > 32 and int(height) > 32:
            if(image.get("src") == first_image_link):
                next_post()
            print(image.get("src"))
            if image.get("src") not in image_links:
                image_links.append(image.get("src"))
            if len(image_links) == num_of_images:
                next_post()
            break
    body_element = driver.find_element("tag name","body")
    body_element.send_keys(Keys.ARROW_RIGHT)
    time.sleep(2)
    photo_phase2()
    finish()

def photo_phase1():
    global first_image_link 
    global num_of_images
    first_image_link = ""
    global image_links
    image_links = []
    print("in photo phase...")
    close_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Close"]'))
    )
    close_button.click()

    soup = BeautifulSoup(driver.page_source, "html.parser")

    images = soup.find_all("img")
    time.sleep(1)
    for image in images:
        
        width = image.get("width")
        height = image.get("height")
        if(width is None or height is None):
            print(image.get("src"))
            image_links.append(image.get("src"))
            print("***1")
            print(type(num_of_images))
            print(len(image_links))
            print(num_of_images)

            first_image_link = image.get("src")
            if len(image_links) == num_of_images:
                next_post()
            break
        if(width == "100%" or height == "100%"):
            continue
        if width is not None and height is not None and int(width) > 32 and int(height) > 32:
            print(image.get("src"))
            image_links.append(image.get("src"))
            print("***2")
            first_image_link = image.get("src")
            if len(image_links) == num_of_images:
                next_post()
            break
    body_element = driver.find_element("tag name","body")
    body_element.send_keys(Keys.ARROW_RIGHT)
    time.sleep(2)
    photo_phase2()
    finish()


# driver.get("https://facebook.com")
# print(driver.title)


# login_email_bar = driver.find_element("id", "email")
# login_pass_bar = driver.find_element("id", "pass")

# login_email_bar.send_keys(facebook_email)
# login_pass_bar.send_keys(facebook_pass)
# login_pass_bar.send_keys(Keys.RETURN)
# print("login done")
# print()

# time.sleep(3)

# driver.get("https://www.facebook.com/groups/811852329428129/posts/1447010382578984/");
#driver.get("https://www.facebook.com/permalink.php?story_fbid=pfbid036QkZbRmdeFMNNCwx3YVgx9SwmEgyHVv8iVRjVFtyVHmmKJJQLxTBerXte8FKugsxl&id=61551591826516");
def start_scrape(link):
    global last_news_id
    last_news_id = last_news_id + 1
    global num_of_images
    print(num_of_images)
    num_of_images = int(post_links[1])
    driver.get(link)
    # Wait for the element with aria-label="Close" to be present
    close_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Close"]'))
    )

    # Click on the close button
    close_button.click()

    soup = BeautifulSoup(driver.page_source, "html.parser")

    global paragraphs 
    paragraphs = []
    titles = soup.find_all('div', {'style': 'text-align: start;'})

    breakNOW = False
    for title in titles:
        if breakNOW == True:
            break
        isParagraph = True
        if title is None:
            continue
        current_element = title
        while current_element.name != "body":
            #time.sleep(1)
            #print(current_element.name)
            # TODO
            attribute = current_element.get("aria-label");
            if attribute is None:
                current_element = current_element.parent
                continue
            if len(attribute) >= 10 and attribute[0:10] == "Comment by":
                #print(attribute)
                #print("***")
                breakNOW = True
                isParagraph = False
                break
            current_element = current_element.parent
        if isParagraph == True:
            paragraphs.append(title)

    for paragraph in paragraphs:
        print(paragraph.text.strip())
        print()


    #print(title.text.strip())

    time.sleep(10)
    if (num_of_images == 0):
        next_post()

    images = soup.find_all("img")
    time.sleep(3)
    for image in images:
        width = image.get("width")
        height = image.get("height")
        if(width is None or height is None):
            current_element = image
            while current_element.name != 'a' and current_element.parent:
                current_element = current_element.parent
            driver.get(current_element.get("href"))
            photo_phase1()
            break
        if(width == "100%" or height == "100%"):
            continue
        if width is not None and height is not None and int(width) > 32 and int(height) > 32:
            current_element = image
            while current_element.name != 'a' and current_element.parent:
                current_element = current_element.parent
            driver.get(current_element.get("href"))
            photo_phase1()
            break
    finish()
    # title = soup.find(has_text_align_start_style)
    # title = soup.find('div', {'style': 'text-align: start;'})

    # print(title.text.strip())

    # time.sleep(10)

    #driver.quit()
start_scrape(post_links[0])
