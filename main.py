# This is a sample Python script.
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time
import os
import shlex, subprocess

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def create_folder_perl(repertoire):
    if not os.path.exists(repertoire):
        pipe = subprocess.Popen(["perl", "perl.pl", "-folder=" + repertoire, "output.xml"], stdout=subprocess.PIPE)
    while not os.path.exists(repertoire):
        time.sleep(0.05)

def create_file_perl(repertoire):
    if not os.path.exists(repertoire):
        pipe = subprocess.Popen(["perl", "perl.pl", "-file=" + repertoire, "output.xml"], stdout=subprocess.PIPE)
    while not os.path.exists(repertoire):
        time.sleep(0.05)


def create_folder(repertoire):
    #print(repertoire)
    if not os.path.exists(repertoire):
        os.makedirs(repertoire)
    while not os.path.exists(repertoire):
        time.sleep(0.05)

def valid_name(name):
    temp = name.replace(" ", "_")
    temp = temp.replace("#", "")
    temp = temp.replace("-", "_")
    temp = temp.replace(":", "_")
    temp = temp.replace("?", "_")
    temp = temp.replace("!", "_")
    temp = temp.replace("/", "_")
    temp = temp.replace("\\", "_")
    temp = temp.replace("*", "_")
    temp = temp.replace("\"", "_")
    return temp

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # call perl function for create file and folder when switch_perl = True
    switch_perl = False

    lien = "https://www.freecodecamp.org/learn/responsive-web-design/"
    Web_browser = webdriver.Chrome(executable_path="C:\selenium browser drivers\chromedriver.exe")
    Web_browser.get(lien)


    # open dropdown button => Expand courses
    button = Web_browser.find_elements_by_xpath('//button[@aria-expanded="false"]')
    for element in button:
        element.click()
        time.sleep(1)

    # Parsing
    html = Web_browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    Section = soup.find_all('h3')
    Web_browser.close()
    Titre = []

    for i in range(0, len(Section)-1):
        Titre.append([valid_name(Section[i].text),[]])


    Sub_Section = soup.find_all('ul', {'class':'map-challenges-ul'})

    for i in range(0, len(Sub_Section)):
        Sub_Section_title = Sub_Section[i].find_all('a')
        Titre[i].append([])
        for element_Sub_Section_title in Sub_Section_title:
            temp = element_Sub_Section_title.text.replace("Not PassedNot Passed","")
            temp = valid_name(temp)
            Titre[i][1].append(temp)

        print(len(Titre[i][1]))

    # generate a json
    #with open('data.json', 'w') as outfile:
    #    json.dump(Titre, outfile)
    file = [".hmtl",".css",".js"]
    temp_titre = Titre[len(Titre)-1][0]
    if(switch_perl==True):
        create_folder_perl(temp_titre)
    else:
        create_folder(temp_titre)

    Titre.pop(len(Titre)-1)


    for element in Titre:
        if (switch_perl == True):
            create_folder_perl("./"+temp_titre+"/"+element[0])
        else:
            create_folder("./"+temp_titre+"/"+element[0])
        for sub_element in element[1]:
            if (switch_perl == True):
                create_folder_perl("./"+temp_titre+"/"+element[0]+"/"+sub_element)
            else:
                create_folder("./"+temp_titre+"/"+element[0]+"/"+sub_element)
            for sub_file in file:
                if (switch_perl == True):
                    create_file_perl("./" + temp_titre + "/" + element[0] + "/" + sub_element + "/freecodecamps" + sub_file)
                else:
                    f = open("./" + temp_titre + "/" + element[0] + "/" + sub_element + "/freecodecamps" + sub_file,"w")
                    f.close()







'''
    for element in Titre:
        create_folder("./"+temp_titre+"/"+element[0])
        for sub_element in element[1]:
            create_folder("./"+temp_titre+"/"+element[0]+"/"+sub_element)
            for sub_file in file:
                f = open("./"+temp_titre+"/"+element[0]+"/"+sub_element+"/freecodecamps"+sub_file, "w")
                f.close()

'''







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
