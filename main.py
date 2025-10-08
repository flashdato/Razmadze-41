from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from html import escape
import requests
import sys
import os

def has_text_align_start_style(tag):
    return tag.has_attr('style') and 'text-align:start' in tag['style']

options = Options()
options.headless = True
options.add_experimental_option("detach", True)

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

print("please input values exactly as requested!")

last_news_id = int(input("Input last news number: "))

path_to_news_image_folders = input("Input news image folder (./images/news/)(for security): ")
custom_name_for_images_directory = input("Input custom name for image files DIRECTORY (news_)(will result in images saving into path_to_news_image_folders/news_51/.): ")
custom_name_for_images = input("Input custom name for image files (news_)(will result in news_51_1.jpg): ")

path_to_news_feed_files = input("Input path to news feed files like news_1.html (./News_Feed/)(for security): ")
custom_name_for_html_files = input("Input custom name for html files (news_)(will result in news_51.html): ")


post_links = []
with open('links.txt', 'r') as file:
    post_links = [line.strip() for line in file if line.strip()] # Read and strip whitespace, ignore empty lines

def finish():
    driver.quit()
    sys.exit(0)

if len(post_links) == 0:
    print("No Links Given!")
    finish()

first_image_link = ""
image_links = []
paragraphs = []
num_of_images = 0

def check_and_reload():
    try:
        # Checking for the modal overlay that sometimes appears
        WebDriverWait(driver, 3).until( # Reduced wait time for a quick check
            EC.presence_of_element_located((By.CSS_SELECTOR, '.x6ikm8r.x10wlt62.xbe9js4.x1egiwwb'))
        )
        print("Modal element found! Attempting to close and reload...")
        # Try to find and click the close button if the modal is present
        try:
            close_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Close"]'))
            )
            driver.execute_script("arguments[0].click();", close_button)
            print("Modal closed, reloading page.")
            driver.refresh()
            time.sleep(2) # Give it a moment to reload
        except TimeoutException:
            print("Could not find close button for modal, reloading anyway.")
            driver.refresh()
            time.sleep(2)
        except NoSuchElementException:
            print("Close button not found for modal, reloading anyway.")
            driver.refresh()
            time.sleep(2)
    except TimeoutException:
        print("Modal element not found, continuing execution...")

def checkHTMLForModalRefresh(soup):
    element = soup.find(class_="x6ikm8r x10wlt62 xbe9js4 x1egiwwb")
    if element:
        print("Modal detected in HTML after scrape attempt, reloading and trying to close.")
        driver.refresh()
        try:
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Close"]'))
            )
            driver.execute_script("arguments[0].click();", close_button)
            print("Modal closed after refresh.")
        except TimeoutException:
            print("Could not find and click close button after HTML modal refresh.")
        return True
    return False

def sanitize_paragraph(paragraph):
    paragraph_soup = paragraph
    emojis = paragraph_soup.find_all('img')
    for emoji in emojis:
        emoji.extract()
    
    empty_spans = paragraph_soup.find_all('span', recursive=True)
    for span in empty_spans:
        if span.text.strip() == "":
            span.extract()
            
    return str(paragraph_soup)

def download_image(image_url, save_path, filename):
    os.makedirs(save_path, exist_ok=True)
    image_saved = False
    try:
        response = requests.get(image_url, timeout=10) # Added timeout for requests
        if response.status_code == 200:
            with open(os.path.join(save_path, filename), 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded and saved as {filename}")
            image_saved = True
        else:
            print(f"!!!Failed to download image!!! Status code: {response.status_code}")
            print(f"The faulty image: {image_url}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image {image_url}: {e}")

    if image_saved:
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
        sanitized_paragraph = sanitize_paragraph(paragraph)
        html_content = html_content + '<p class="infotext">' + str(sanitized_paragraph) + "</p>\n" 
    html_content = html_content + "<br />\n"
    if len(image_links) != 0:
        html_content = html_content + '<div class="image-grid">'
        for index,image_link in enumerate(image_links):
            path_to_save_to = path_to_news_image_folders + custom_name_for_images_directory + str(last_news_id) +"/" 
            filename_to_save_as = custom_name_for_images + str(last_news_id) + "_" + str(index) + ".jpg"
            new_image_link = download_image(image_link,path_to_save_to,filename_to_save_as)
            html_content = html_content + '<div class="image-box">\n'
            html_content = html_content + '<img src="' + path_to_news_image_folders[1:] + custom_name_for_images_directory + str(last_news_id) + '/' + custom_name_for_images + str(last_news_id) + '_' + str(index) + '.jpg" alt = "Image ' + str(index) + '" class="grid-image" />\n</div>\n'
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

    os.makedirs(path_to_news_feed_files, exist_ok=True) 
    with open(os.path.join(path_to_news_feed_files, custom_name_for_html_files + str(last_news_id) + ".html"), "w", encoding="utf-8") as file: # Added encoding
        file.write(html_content)
    print("HTML file generated successfully for " + custom_name_for_html_files + str(last_news_id))


def next_post():
    global paragraphs
    global image_links
    global last_news_id
    global post_links

    write_html_for_given_details(paragraphs, image_links)
    
    # Clear data for the next post
    paragraphs = []
    image_links = []
    
    # Ensure there are enough links for the next iteration (link + num_of_images)
    if len(post_links) >= 2:
        post_links.pop(0) # Remove the current link
        post_links.pop(0) # Remove the current num_of_images
        
        if len(post_links) >= 2: # Check if there's still a link and num_of_images for the *next* post
            print(f"Proceeding to next post: {post_links[0]}")
            start_scrape(post_links[0])
        else:
            print("No more links to process. Finishing.")
            finish()
    else:
        print("Not enough links remaining to process the next post. Finishing.")
        finish()


def photo_phase2():
    global first_image_link
    global image_links
    global num_of_images

    print("In photo phase 2...")
    try:
        # Wait for the last close button to be clickable
        close_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="Close"]'))
        )
        
        # Filter out buttons that are not interactable or have unwanted classes
        interactable_close_buttons = []
        for btn in close_buttons:
            # Check if the button is visible and enabled
            if btn.is_displayed() and btn.is_enabled():
                # Get class attribute to check for unwanted classes
                btn_class = btn.get_attribute("class")
                # Define unwanted classes (consider refining this regex/string check if needed)
                unwanted_class_substring = "x1i10hfl" # A common class for non-modal close buttons
                if unwanted_class_substring not in btn_class:
                    interactable_close_buttons.append(btn)
        
        if interactable_close_buttons:
            close_button_to_click = interactable_close_buttons[-1] # Click the last interactable one
            print(f"Clicking close button: {close_button_to_click.get_attribute('outerHTML')}")
            driver.execute_script("arguments[0].click();", close_button_to_click)
            time.sleep(1) # Give a moment for the modal to close
        else:
            print("No interactable close button found to dismiss modal/overlay.")

    except TimeoutException:
        print("No close button found in photo_phase2 within the timeout.")
        # If no close button, assume the modal is not present or has already closed
        pass
    except Exception as e:
        print(f"An error occurred while trying to close button in photo_phase2: {e}")

    soup = BeautifulSoup(driver.page_source, "html.parser")
    # This check might cause a reload loop if the modal continuously appears.
    # It's generally better to handle it with the WebDriverWait first.
    # if checkHTMLForModalRefresh(soup):
    #     photo_phase2() # Recurse if a modal was found and closed

    images = soup.find_all("img")
    
    found_new_image = False
    for image in images:
        width = image.get("width")
        height = image.get("height")
        src = image.get("src")

        # Skip small images or 100% width/height images (like placeholders)
        if (width is not None and height is not None and (width == "100%" or height == "100%" or int(width) <= 32 or int(height) <= 32)):
            continue
        
        # Consider images without explicit width/height if they are likely content images
        if src and src.startswith("http") and src not in image_links:
            image_links.append(src)
            found_new_image = True
            print(f"Found image: {src}")
            if len(image_links) == num_of_images:
                print("All images found. Moving to next post.")
                next_post()
                return # Important to return here to avoid further execution

    if found_new_image and len(image_links) == num_of_images:
        print("All images collected after finding a new one. Moving to next post.")
        next_post()
        return

    if len(image_links) < num_of_images:
        print(f"Collected {len(image_links)} of {num_of_images} images. Scrolling right...")
        try:
            body_element = driver.find_element(By.TAG_NAME, "body")
            body_element.send_keys(Keys.ARROW_RIGHT)
            time.sleep(2)
            photo_phase2() # Recurse to find more images
        except Exception as e:
            print(f"Error scrolling or finding body element: {e}")
            print("Could not scroll right, assuming no more images can be found this way.")
            # If scrolling fails, and we haven't found all images, we might be stuck or done.
            # Decide if this should finish the current post or raise an error.
            if len(image_links) > 0: # If at least some images were found
                print(f"Finished current post with {len(image_links)} images (expected {num_of_images}).")
                next_post()
            else:
                print("No images found for this post. Finishing.")
                next_post()
    else:
        print("All images already found or no more images to be found via scrolling.")
        next_post()


def photo_phase1():
    global first_image_link 
    global num_of_images
    global image_links

    first_image_link = ""
    image_links = [] # Reset for each new post

    print("In photo phase 1...")
    
    try:
        # Wait for the close button, allowing it to be clickable
        close_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="Close"]'))
        )

        interactable_close_buttons = []
        for btn in close_buttons:
            if btn.is_displayed() and btn.is_enabled():
                btn_class = btn.get_attribute("class")
                unwanted_class_substring = "x1i10hfl" 
                if unwanted_class_substring not in btn_class:
                    interactable_close_buttons.append(btn)

        if interactable_close_buttons:
            close_button = interactable_close_buttons[-1] # Try clicking the last one
            print(f"Clicking close button in photo_phase1: {close_button.get_attribute('outerHTML')}")
            driver.execute_script("arguments[0].click();", close_button)
            time.sleep(1) # Give a moment for the modal to close
        else:
            print("No interactable close button found in photo_phase1.")

    except TimeoutException:
        print("No close button found in photo_phase1 within the timeout, continuing.")
        pass # No close button found, proceed
    except Exception as e:
        print(f"An error occurred while trying to close button in photo_phase1: {e}")

    soup = BeautifulSoup(driver.page_source, "html.parser")

    images = soup.find_all("img")
    
    image_to_click_for_gallery = None

    for image in images:
        width = image.get("width")
        height = image.get("height")
        src = image.get("src")

        if src and src.startswith("http"): # Ensure it's a valid image source
            # General heuristic for a 'main' image that might open a gallery
            # Prioritize images that are not small or placeholder-like.
            if (width is None or height is None) or (int(width) > 32 and int(height) > 32 and width != "100%" and height != "100%"):
                # Check if this image is wrapped in an anchor tag leading to a full view
                current_element = image
                while current_element and current_element.name != 'a':
                    current_element = current_element.parent
                
                if current_element and current_element.name == 'a' and current_element.get("href"):
                    if "photo" in current_element.get("href") or "permalink.php" in current_element.get("href"): # Heuristic for gallery link
                        image_to_click_for_gallery = current_element
                        print(f"Found potential gallery opener: {current_element.get('href')}")
                        break # Found a candidate, break and click it

    if image_to_click_for_gallery:
        try:
            print("Clicking on image to open gallery...")
            driver.get(image_to_click_for_gallery.get("href")) # Directly navigate to the gallery link
            time.sleep(3) # Give time for the gallery to load
            photo_phase2()
        except Exception as e:
            print(f"Error navigating to image gallery: {e}")
            print("Failed to open gallery, attempting to proceed without images or next post.")
            if num_of_images == 0:
                next_post()
            else:
                print("Could not collect images as planned, finishing current post and moving on.")
                next_post()
    else:
        print("No suitable image found to open a gallery. If num_of_images > 0, this might be an issue.")
        if num_of_images == 0:
            next_post() # If no images expected, proceed
        else:
            print(f"Expected {num_of_images} images but couldn't open a gallery. Finishing current post.")
            next_post()


def start_scrape(link):
    global last_news_id
    global num_of_images
    global paragraphs
    global post_links # Need to access and modify post_links here

    print(f"\n--- Processing Link: {link.strip()} ---")
    last_news_id += 1 # Increment for each new news item
    
    # Extract num_of_images from the next item in post_links
    if len(post_links) < 2:
        print("Not enough links in list to get link and num_of_images.")
        finish()
    
    try:
        num_of_images = int(post_links[1])
        print(f"Expecting {num_of_images} images for this post.")
    except ValueError:
        print(f"Error: Expected number of images for link {link} is not a valid integer: '{post_links[1]}'. Skipping post.")
        # If num_of_images is invalid, move to the next set of links
        post_links.pop(0) # Remove the current faulty link
        post_links.pop(0) # Remove the faulty num_of_images
        if len(post_links) > 0:
            start_scrape(post_links[0])
        else:
            finish()
        return


    driver.get(link.strip()) # Use strip() to remove newline characters
    time.sleep(3) # Give page more time to load initially

    # Perform initial check for modal or reload
    check_and_reload()
    time.sleep(2) # Give it a moment after reload

    soup = BeautifulSoup(driver.page_source, "html.parser")

    paragraphs = []
    # Find all divs that likely contain post content, looking for text-align: start
    # Facebook's CSS is highly dynamic, so relying solely on style might be brittle.
    # However, for now, we'll keep it.
    
    # A more general approach would be to look for common Facebook post structures
    # like a div with role="article" or specific data-testid attributes.
    
    # For now, let's refine the text-align: start search to be more specific to post content
    # Look for div elements within a likely post container
    post_content_divs = soup.find_all('div', style='text-align: start;')

    breakNOW = False
    for p_tag in post_content_divs:
        # Check if the parent chain indicates it's part of the main post content
        # rather than comments or other UI elements.
        current_element = p_tag
        is_comment_or_unwanted = False
        while current_element and current_element.name != "body":
            attribute = current_element.get("aria-label")
            if attribute and attribute.startswith("Comment by"):
                is_comment_or_unwanted = True
                break
            current_element = current_element.parent
        
        if not is_comment_or_unwanted:
            # Ensure paragraph content is substantial and not just empty spans
            if p_tag.text.strip(): # Add check for actual text content
                paragraphs.append(p_tag)
                print(f"Extracted paragraph: {p_tag.text.strip()}")
        else:
            print("Skipping element identified as comment or unwanted content.")


    if not paragraphs:
        print("No paragraphs found, attempting to re-evaluate.")
        # Could add more aggressive scrolling or waiting here if initial grab fails

    # If no images are expected, proceed to the next post immediately
    if num_of_images == 0:
        print("No images expected for this post.")
        next_post()
        return

    # Try to find an image to click to open the gallery view
    image_clicked = False
    images_on_page = driver.find_elements(By.TAG_NAME, "img")
    for img_element in images_on_page:
        try:
            # Attempt to click on a significant image to open its full-screen view
            # This is a heuristic and might need adjustment based on Facebook's UI
            width = img_element.get_attribute("width")
            height = img_element.get_attribute("height")
            src = img_element.get_attribute("src")

            if src and src.startswith("http"):
                # Avoid very small images or common UI elements
                if (width and height and int(width) > 50 and int(height) > 50 and width != "100%" and height != "100%") or \
                   (not width and not height and "scontent" in src): # Heuristic for content images without explicit size
                    
                    # Try to click the image or its parent <a> if it leads to a gallery
                    try:
                        # Sometimes the image itself is clickable, sometimes it's wrapped in an <a>
                        ActionChains(driver).move_to_element(img_element).perform()
                        driver.execute_script("arguments[0].click();", img_element)
                        print(f"Clicked on image: {src}")
                        image_clicked = True
                        time.sleep(3) # Wait for the gallery to load
                        photo_phase1() # Enter photo phase to scrape images
                        return # Exit start_scrape as photo_phase1 will handle next steps
                    except Exception as click_error:
                        print(f"Could not click image directly: {click_error}. Trying parent link.")
                        parent_a = img_element.find_element(By.XPATH, "./ancestor::a[1]")
                        if parent_a and parent_a.get_attribute("href"):
                            href = parent_a.get_attribute("href")
                            if "photo" in href or "permalink.php" in href:
                                driver.get(href)
                                print(f"Navigated to gallery link: {href}")
                                image_clicked = True
                                time.sleep(3)
                                photo_phase1()
                                return
        except Exception as e:
            # Continue if an image causes an error (e.g., cannot get attribute)
            print(f"Error processing an image element: {e}")
            continue

    if not image_clicked:
        print("No clickable image found to open gallery. Proceeding as if no images are present or could be accessed.")
        next_post() # Move to the next post if no gallery could be opened

start_scrape(post_links[0])
