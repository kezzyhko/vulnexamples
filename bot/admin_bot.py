from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import asyncio

bot_name = "a7_admin_bot"
input_name = "message"


def log(message):
    print("%s > %s" % (bot_name, message))


def login():
    driver.get("http://a7.localhost:8000/login/")
    elem = driver.find_element_by_id("id_username")
    elem.send_keys("admin")
    elem = driver.find_element_by_id("id_password")
    elem.send_keys("1qQmeow")
    elem.send_keys(Keys.ENTER)

    assert "Welcome" in driver.page_source
    log("authorized successfully")

    return driver.find_element_by_id(input_name)


def logout():
    driver.get("http://a7.localhost:8000/logout/")
    log("logouted")


def send(message):
    input_form.send_keys(message)
    input_form.send_keys(Keys.ENTER)

    time.sleep(1)

    log("message was successfully sent")


async def check_for_new_and_say_hello():

    stored = []
    while not close_checker:

        messages = driver.find_elements_by_class_name("connected")

        sent = False

        for e in messages:
            if e not in stored:
                if not sent:

                    user = e.find_element_by_class_name("username")
                    user = user.text

                    if user == "admin":
                        send("Hello, %s! (Yes, I know that I said hello to myself)" % user)
                    else:
                        send("Hello, %s!" % user)

                    sent = True

                    log("sent hello to %s" % user)
                stored.append(e)

        time.sleep(1)


async def user_io():
    while True:
        string = input()
        if string.split()[0] == "send":
            send(' '.join(string.split()[1::]))

        if string.split()[0] == "close":
            close_checker = True
            exit()

        if string.split()[0] == "restart":
            close_checker = True
            time.sleep(2)
            logout()
            input_form = login()


if __name__ == "__main__":

    driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])

    driver.set_window_size(1000, 500)
    driver.get('http://a7.localhost:8000/login/')
    time.sleep(2)

    input_form = login()

    close_checker = False

    loop = asyncio.get_event_loop()

    loop.create_task(check_for_new_and_say_hello())

    # asyncio.async(check_for_new_and_say_hello())

    loop.run_forever()


