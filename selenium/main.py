from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the driver and navigate to the LinkedIn job search page
driver = webdriver.Chrome(executable_path="C:/Users/david/Desktop/chromedriver.exe")
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3594319244&f_AL=true&f_E=1%2C2%2C3&f_WT=2&geoId=91000011&keywords=developer&location=Latin%20America&refresh=true")
# Click on the login button

login_button = driver.find_element_by_class_name('nav__button-secondary')
login_button.click()


# Enter the email and password and click on the login button
email_field = driver.find_element_by_id('username')
password_field = driver.find_element_by_id('password')
email_field.send_keys('david._101@hotmail.com')
password_field.send_keys('Floria0991')
password_field.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(2)

while True:
    #wait for the page to load
    time.sleep(4)
    job_titles = driver.find_elements_by_css_selector(".job-card-container--clickable")

    for job_title in job_titles:
        job_title.click()
        time.sleep(2)


    try:
            apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
            apply_button.click()

            # Click the "Next" button as many times as there are "Next" buttons
            while True:
                try:
                    next_button = driver.find_element_by_xpath('//button[@aria-label="Continue to next step"]')
                    next_button.click()
                    time.sleep(2)
                except:
                    # If there is no "Next" button, assume there is only a "Review" and "Submit" button
                    break

            time.sleep(2)

            # Check for the "Review" button, but if there are aditional questions, dont anser them, just click the close button, and move on to the next job
            try:
                review_button = driver.find_element_by_xpath('//button[@aria-label="Review your application"]')
                review_button.click()
                time.sleep(2)

                # Check for the "Submit" button
                submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                submit_button.click()
                time.sleep(3)

                # Close the review modal
                close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                close_button.click()
            except:
                # If there is no "Review" button, assume there is only a "Submit" button
                submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                submit_button.click()
                time.sleep(3)
                close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                close_button.click()

            # Wait for the application to submit
            time.sleep(3)
    except:
            # If there is no "Easy Apply" button, move on to the next job
            continue

    # Click on the next button to go to the next page
    print("Moving to next page")
    try:
        next_button = driver.find_element_by_xpath('//button[@aria-label="Page 2"]')
        next_button.click()
        time.sleep(4)
        job_titles = driver.find_elements_by_css_selector(".job-card-container--clickable")

        for job_title in job_titles:
            job_title.click()
            time.sleep(2)

            try:
                apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
                apply_button.click()

                # Click the "Next" button as many times as there are "Next" buttons
                while True:
                    try:
                        next_button = driver.find_element_by_xpath('//button[@aria-label="Continue to next step"]')
                        next_button.click()
                        time.sleep(2)
                    except:
                        # If there is no "Next" button, assume there is only a "Review" and "Submit" button
                        break

                time.sleep(2)

                # Check for the "Review" button, but if there are aditional questions, dont anser them, just click the close button, and move on to the next job
                try:
                    review_button = driver.find_element_by_xpath('//button[@aria-label="Review your application"]')
                    review_button.click()
                    time.sleep(2)

                    # Check for the "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)

                    # Close the review modal
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()
                except:
                    # If there is no "Review" button, assume there is only a "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()

                # Wait for the application to submit
                time.sleep(2)
            except:
                # If there is no "Easy Apply" button, move on to the next job
                continue
    except:
        # If there is no "Next" button, assume we have reached the last page and exit the loop
        continue
    try:
        next_button = driver.find_element_by_xpath('//button[@aria-label="Page 3"]')
        next_button.click()
        time.sleep(2)
        job_titles = driver.find_elements_by_css_selector(".job-card-container--clickable")

        for job_title in job_titles:
            job_title.click()
            time.sleep(2)

            try:
                apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
                apply_button.click()

                # Click the "Next" button as many times as there are "Next" buttons
                while True:
                    try:
                        next_button = driver.find_element_by_xpath('//button[@aria-label="Continue to next step"]')
                        next_button.click()
                        time.sleep(2)
                    except:
                        # If there is no "Next" button, assume there is only a "Review" and "Submit" button
                        break

                time.sleep(2)

                # Check for the "Review" button, but if there are aditional questions, dont anser them, just click the close button, and move on to the next job
                try:
                    review_button = driver.find_element_by_xpath('//button[@aria-label="Review your application"]')
                    review_button.click()
                    time.sleep(2)

                    # Check for the "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)

                    # Close the review modal
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()
                except:
                    # If there is no "Review" button, assume there is only a "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()

                # Wait for the application to submit
                time.sleep(2)
            except:
                # If there is no "Easy Apply" button, move on to the next job
                continue
    except:
        # If there is no "Next" button, assume we have reached the last page and exit the loop
        continue
    try:
        next_button = driver.find_element_by_xpath('//button[@aria-label="Page 4"]')
        next_button.click()
        time.sleep(2)
        job_titles = driver.find_elements_by_css_selector(".job-card-container--clickable")

        for job_title in job_titles:
            job_title.click()
            time.sleep(2)

            try:
                apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
                apply_button.click()

                # Click the "Next" button as many times as there are "Next" buttons
                while True:
                    try:
                        next_button = driver.find_element_by_xpath('//button[@aria-label="Continue to next step"]')
                        next_button.click()
                        time.sleep(2)
                    except:
                        # If there is no "Next" button, assume there is only a "Review" and "Submit" button
                        break

                time.sleep(2)

                # Check for the "Review" button, but if there are aditional questions, dont anser them, just click the close button, and move on to the next job
                try:
                    review_button = driver.find_element_by_xpath('//button[@aria-label="Review your application"]')
                    review_button.click()
                    time.sleep(2)

                    # Check for the "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)

                    # Close the review modal
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()
                except:
                    # If there is no "Review" button, assume there is only a "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()

                # Wait for the application to submit
                time.sleep(2)
            except:
                # If there is no "Easy Apply" button, move on to the next job
                continue
    except:
        # If there is no "Next" button, assume we have reached the last page and exit the loop
        continue
    try:
        next_button = driver.find_element_by_xpath('//button[@aria-label="Page 5"]')
        next_button.click()
        time.sleep(2)
        job_titles = driver.find_elements_by_css_selector(".job-card-container--clickable")

        for job_title in job_titles:
            job_title.click()
            time.sleep(2)

            try:
                apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
                apply_button.click()

                # Click the "Next" button as many times as there are "Next" buttons
                while True:
                    try:
                        next_button = driver.find_element_by_xpath('//button[@aria-label="Continue to next step"]')
                        next_button.click()
                        time.sleep(2)
                    except:
                        # If there is no "Next" button, assume there is only a "Review" and "Submit" button
                        break

                time.sleep(2)

                # Check for the "Review" button, but if there are aditional questions, dont anser them, just click the close button, and move on to the next job
                try:
                    review_button = driver.find_element_by_xpath('//button[@aria-label="Review your application"]')
                    review_button.click()
                    time.sleep(2)

                    # Check for the "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)

                    # Close the review modal
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()
                except:
                    # If there is no "Review" button, assume there is only a "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()

                # Wait for the application to submit
                time.sleep(2)
            except:
                # If there is no "Easy Apply" button, move on to the next job
                continue
    except:
        # If there is no "Next" button, assume we have reached the last page and exit the loop
        continue
    try:
        next_button = driver.find_element_by_xpath('//button[@aria-label="Page 6"]')
        next_button.click()
        time.sleep(2)
        job_titles = driver.find_elements_by_css_selector(".job-card-container--clickable")

        for job_title in job_titles:
            job_title.click()
            time.sleep(2)

            try:
                apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
                apply_button.click()

                # Click the "Next" button as many times as there are "Next" buttons
                while True:
                    try:
                        next_button = driver.find_element_by_xpath('//button[@aria-label="Continue to next step"]')
                        next_button.click()
                        time.sleep(2)
                    except:
                        # If there is no "Next" button, assume there is only a "Review" and "Submit" button
                        break

                time.sleep(2)

                # Check for the "Review" button, but if there are aditional questions, dont anser them, just click the close button, and move on to the next job
                try:
                    review_button = driver.find_element_by_xpath('//button[@aria-label="Review your application"]')
                    review_button.click()
                    time.sleep(2)

                    # Check for the "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)

                    # Close the review modal
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()
                except:
                    # If there is no "Review" button, assume there is only a "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()

                # Wait for the application to submit
                time.sleep(2)
            except:
                # If there is no "Easy Apply" button, move on to the next job
                continue
    except:
        # If there is no "Next" button, assume we have reached the last page and exit the loop
        continue
    try:
        next_button = driver.find_element_by_xpath('//button[@aria-label="Page 7"]')
        next_button.click()
        time.sleep(2)
        job_titles = driver.find_elements_by_css_selector(".job-card-container--clickable")

        for job_title in job_titles:
            job_title.click()
            time.sleep(2)

            try:
                apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
                apply_button.click()

                # Click the "Next" button as many times as there are "Next" buttons
                while True:
                    try:
                        next_button = driver.find_element_by_xpath('//button[@aria-label="Continue to next step"]')
                        next_button.click()
                        time.sleep(2)
                    except:
                        # If there is no "Next" button, assume there is only a "Review" and "Submit" button
                        break

                time.sleep(2)

                # Check for the "Review" button, but if there are aditional questions, dont anser them, just click the close button, and move on to the next job
                try:
                    review_button = driver.find_element_by_xpath('//button[@aria-label="Review your application"]')
                    review_button.click()
                    time.sleep(2)

                    # Check for the "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)

                    # Close the review modal
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()
                except:
                    # If there is no "Review" button, assume there is only a "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()

                # Wait for the application to submit
                time.sleep(2)
            except:
                # If there is no "Easy Apply" button, move on to the next job
                continue
    except:
        # If there is no "Next" button, assume we have reached the last page and exit the loop
        continue
    try:
        next_button = driver.find_element_by_xpath('//button[@aria-label="Page 8"]')
        next_button.click()
        time.sleep(2)
        job_titles = driver.find_elements_by_css_selector(".job-card-container--clickable")

        for job_title in job_titles:
            job_title.click()
            time.sleep(2)

            try:
                apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
                apply_button.click()

                # Click the "Next" button as many times as there are "Next" buttons
                while True:
                    try:
                        next_button = driver.find_element_by_xpath('//button[@aria-label="Continue to next step"]')
                        next_button.click()
                        time.sleep(2)
                    except:
                        # If there is no "Next" button, assume there is only a "Review" and "Submit" button
                        break

                time.sleep(2)

                # Check for the "Review" button, but if there are aditional questions, dont anser them, just click the close button, and move on to the next job
                try:
                    review_button = driver.find_element_by_xpath('//button[@aria-label="Review your application"]')
                    review_button.click()
                    time.sleep(2)

                    # Check for the "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)

                    # Close the review modal
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()
                except:
                    # If there is no "Review" button, assume there is only a "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()

                # Wait for the application to submit
                time.sleep(2)
            except:
                # If there is no "Easy Apply" button, move on to the next job
                continue
    except:
        # If there is no "Next" button, assume we have reached the last page and exit the loop
        continue
    try:
        next_button = driver.find_element_by_xpath('//button[@aria-label="Page 9"]')
        next_button.click()
        time.sleep(2)
        job_titles = driver.find_elements_by_css_selector(".job-card-container--clickable")

        for job_title in job_titles:
            job_title.click()
            time.sleep(2)

            try:
                apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
                apply_button.click()

                # Click the "Next" button as many times as there are "Next" buttons
                while True:
                    try:
                        next_button = driver.find_element_by_xpath('//button[@aria-label="Continue to next step"]')
                        next_button.click()
                        time.sleep(2)
                    except:
                        # If there is no "Next" button, assume there is only a "Review" and "Submit" button
                        break

                time.sleep(2)

                # Check for the "Review" button, but if there are aditional questions, dont anser them, just click the close button, and move on to the next job
                try:
                    review_button = driver.find_element_by_xpath('//button[@aria-label="Review your application"]')
                    review_button.click()
                    time.sleep(2)

                    # Check for the "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)

                    # Close the review modal
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()
                except:
                    # If there is no "Review" button, assume there is only a "Submit" button
                    submit_button = driver.find_element_by_xpath('//button[@aria-label="Submit application"]')
                    submit_button.click()
                    time.sleep(3)
                    close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                    close_button.click()

                # Wait for the application to submit
                time.sleep(2)
            except:
                # If there is no "Easy Apply" button, move on to the next job
                continue
    except:
        # If there is no "Next" button, assume we have reached the last page and exit the loop
        break




