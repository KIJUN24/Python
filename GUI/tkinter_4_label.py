from tkinter import *
from selenium import webdriver

win = Tk()

win.title("Daum Log-in")
win.geometry("400x300")
win.option_add("*Font", "궁서 20")

# daum logo
lab_d = Label(win)
img = PhotoImage(file = "C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\20220112\\GUI\\image\\daum_logo_remove.png")
img = img.subsample(5) # 1/5로 축소 
lab_d.config(image = img)
lab_d.pack()


# id label
lab1 = Label(win)
lab1.config(text = "ID")
lab1.pack()


# id 입력
ent1 = Entry(win)
ent1.insert(0, "abc@abc.com")

def clear(event):
    if(ent1.get() == "abc@abc.com"):
        ent1.delete(0, len(ent1.get()))

ent1.bind("<Button-1>", clear)
ent1.pack()


# pw label
lab2 = Label(win)
lab2.config(text = "Password")
lab2.pack()


# pw 입력
ent2 = Entry(win)
ent2.config(show = "*")
ent2.pack()


# Log-in Button
but = Button(win)
but.config(text = "Login")

def login(): # Chrome Driver
    driver = webdriver.Chrome("C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\20220112\\GUI\\item\\chromedriver.exe")
    url = "https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net"
    driver.get(url)
    driver.implicitly_wait(5)
    xpath1 = "//input[@name='email']"
    driver.find_element_by_xpath(xpath1).send_keys(ent1.get())
    xpath2 = "//input[@name='password']"
    driver.find_element_by_xpath(xpath2).send_keys(ent2.get())
    xpath3 = "//button[@class='btn_g btn_confirm submit']"
    driver.find_element_by_xpath(xpath3).click()
    lab3.config(text = "[Message] login success!!")

but.config(command = login)
but.pack()


# message label
lab3 = Label(win)
lab3.pack()

win.mainloop()