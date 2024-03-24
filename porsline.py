import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import csv


def rand_date(s):
    ra_int_y = ""
    if s == 1:
        ra_int_y = str(random.randrange(1320, 1340))
    if s == 2:
        ra_int_y = str(random.randrange(1340, 1360))
    if s == 3:
        ra_int_y = str(random.randrange(1360, 1380))
    if s == 4:
        ra_int_y = str(random.randrange(1380, 1403))

    ra_int_m = random.randrange(1, 13)
    if ra_int_m < 10:
        ra_int_m = str("0" + str(ra_int_m))
    else:
        ra_int_m = str(ra_int_m)

    ra_int_d = random.randrange(1, 30)
    if ra_int_d < 10:
        ra_int_d = str("0" + str(ra_int_d))
    else:
        ra_int_d = str(ra_int_d)

    date = f"{ra_int_y}/{ra_int_m}/{ra_int_d}"
    time.sleep(1)
    return date


def rand_child():
    return str(random.randrange(1, 5))


def rand_bit():
    return str(random.randrange(1, 3))


def rand_4():
    return random.randrange(1, 4)

count = 0

while True:
    #file_name = "variables.csv"
    time.sleep(5)
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    chrome_options.add_experimental_option("detach", True)
    driver.get('https://survey.porsline.ir/s/J0cNWzS')
    # variables
    birth_l = rand_4()
    birth_d = rand_date(birth_l)

    marriage = rand_bit()
    if birth_l < 3:
        marriage = birth_l + 1
    gender = random.randrange(1, 3)
    grade = 3
    home = random.randrange(1, 3)
    home_m = str(random.randrange(45, 145, 5))
    fun = [" پارک", "مسافرت", "پیاده روی", " تماشای تلویزون ", " فضای مجازی", " نشستن در خانه ", " مظالعه", " درخانه نشستن", " وقت گذراندن با خانواده"]
    women = [" فقر و نداشتن امکانات اساسی", " فرصت‌های شغلی محدود", " بی‌تحصیلی و عدم دسترسی به آموزش",
            " عدم دسترسی به خدمات بهداشتی و درمانی", " ازدواج زودهنگام و اختلاف سنی", " تبعیض جنسیتی و خشونت علیه زنان"
            , " مشکلات بهداشتی جمعیتی", " عدم دسترسی به منابع مالی", " تبعیض جنسیتی در زمینه اشتغال", " خطرات امنیتی"]
    child = [" فقر و نداشتن دسترسی به نیازهای اساسی مانند غذا، آب، و مسکن", " بی‌توجهی به تحصیل و عدم دسترسی به آموزش معیار",
            " خطرات امنیتی و تعرض به خشونت جسمی یا جنسی.", " عدم دسترسی به خدمات بهداشتی و درمانی مناسب",
            " بی‌توجهی به حقوق کودکان و اجبار به کار کودکانه", " فرار از خانه و مواجهه با خطرات خیابان", " فقدان مراکز تفریحی و فرصت‌های فرهنگی",
            " آلودگی محیطی و عوامل زیست‌محیطی مضر", " تنش و خشم خانواده به دلیل فشارهای اقتصادی", " بی‌توجهی به رفاه روحی و روانی کودکان و نیازهای اجتماعی آنها.",
            " فقدان فرصت‌های مرتبط با فناوری و ابزار آموزشی", " محرومیت از فرصت‌های متعارف و عدم دسترسی به فرصت‌های توسعه فردی و تحصیلی"]
    man = [" بی‌توجهی به مسئولیت‌های خانوادگی به دلیل فشارهای اقتصادی ", " مشکلات امنیتی و تعرض به خطرات خشونت و  جرم در محیط‌های فقیر",
        " تبعیض و تبعیض در دسترسی به عدالت و امکانات عمومی.", " عدم دسترسی به منابع اطلاعاتی و فرصت‌های ارتباطی.",
        " ازدواج زودهنگام و مشکلات مربوط به آن برای خود و خانواده.", " بی‌توجهی به نیازهای روحی و روانی و تاثیر آن بر سلامت روانی.",
        " بی‌توجهی به حقوق انسانی و مسائل حقوقی به دلیل شرایط اجتماعی نامساعد.", " استفاده از مواد مخدر و الکل به دلیل فشارهای روانی و اجتماعی.",
        " عدم دسترسی به فرصت‌های شغلی مناسب و کسب درآمد مناسب.", " ناتوانی در تأمین نیازهای اقتصادی خانواده و تحمیل فشارهای اقتصاد",
        " تنش و خشم در خانواده به دلیل فشارهای اقتصادی و اجتماعی"]
    yong_man = [" بی‌توجهی به تحصیل و عدم دسترسی به آموزش معیار", " خطرات امنیتی و تعرض به خشونت جسمی یا جنسی", " بی‌توجهی به حقوق جوانان و اجبار به کار جوانانه",
                " محرومیت از فرصت‌های متعارف و عدم دسترسی به فرصت‌های توسعه فردی و تحصیلی.", " تنش و خشم خانواده به دلیل فشارهای اقتصادی",
                " دم امکان دستیابی به فرصت‌های اشتغال و توسعه مهارت‌های اجتماعی", "ناتوانی دولت در ارائه خدمات اساسی به مناطق فقیر",
                " اثرات منفی بر سلامت جسمی و روانی جوانان به دلیل شرایط نامساعد زندگ", "بی‌توجهی به نیازهای روانی و اجتماعی جوانان و نوجوانان"]

    fun_c = random.sample(fun, 2)
    women_c = random.sample(women, 2)
    child_c = random.sample(child, 2)
    yong_c = random.sample(yong_man, 2)
    man_c = random.sample(man, 2)

    # , "فراغت", "زنان", "کودکان", "جوانان", "مردان"

    # with open(file_name, mode='w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["تولد", "سال", "ازدواج", "جنسیت", "خانه", "متراژ"])
    #     writer.writerow([birth_d, "birth_l", str(marriage), str(gender), str(grade), str(home), home_m])

    # print("Variables saved to", file_name)

    # q 0

    time.sleep(0.5)
    button1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'//*[@id="__next"]/div/main/div/main/div/div[2]/div/div/div[2]/button')))
    button1.click()
    #time.sleep(0.5)

    # q 1 نام و نام خانوادگی

    #time.sleep(0.5)
    entry1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'//*[@id="__next"]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/input')))
    entry1.send_keys("شاطرآباد کرمانشاه")
    #time.sleep(0.5)
    button1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'//*[@id="__next"]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button1.click()
    time.sleep(0.5)

    # q 2 استان

    #time.sleep(0.5)
    entry2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/span[1]/input')))
    entry2.send_keys("کرمانشاه")
    #time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/ul/li')))
    button.click()
    time.sleep(0.5)

    # q 3 شهرستان

    time.sleep(0.5)
    entry2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/input')))
    entry2.send_keys("کرمانشاه")
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button.click()
    time.sleep(0.5)

    # q 4 نام محله

    time.sleep(0.5)
    entry3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/input')))
    entry3.send_keys("شاطرآباد")
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button.click()
    time.sleep(0.5)

    # q 5 تاریخ تولد
    time.sleep(0.5)
    entry3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/div/div/input')))
    entry3.send_keys(rand_date(birth_l))
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button.click()
    time.sleep(0.5)

    # q 6 جنسیت
    time.sleep(2)
    if gender == 1:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]')))
        button.click()
    if gender == 2:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
        button.click()
    time.sleep(2)

    # q 7 وضعیت تاهل

    time.sleep(1)
    if marriage == 1:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]')))
        button.click()
    else:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
        button.click()
    time.sleep(0.5)

    # q 8 در صورت تاهل، یکی از گزینه های زیر را انتخاب نمایید:
    time.sleep(1)
    if marriage == 0:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[2]/div/div[1]/div[1]')))
        button.click()
    else:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]')))
        button.click()
    time.sleep(2)

    # q 9 تاریخ ازدواج

    time.sleep(1)
    if marriage == 0:
        time.sleep(0.5)
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[2]/div/div[1]/div[1]')))
        button.click()

    else:
        entry = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,
            f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/div/div/input')))
        entry.send_keys(rand_date(marriage))
        time.sleep(1)
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,
            f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
        button.click()

    time.sleep(0.5)

    # q 10 تعداد فرزندان

    time.sleep(0.5)
    if (marriage > 0) and (marriage < 4):
        entry3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/input')))
        entry3.send_keys(rand_child())
        #time.sleep(0.5)
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
        button.click()
    else:
        entry3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/input')))
        entry3.send_keys("0")
        # time.sleep(0.5)
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,
            f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
        button.click()
    time.sleep(0.5)

    # q 11 در صورت طلاق، تاریخ طلاق را وارد کنید

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[2]/div/div[1]/div[1]')))
    button.click()
    time.sleep(0.5)

    # q 12 دین
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]')))
    time.sleep(0.5)
    button.click()
    time.sleep(0.5)

    # q 13 مذهب
    time.sleep(1)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]')))
    time.sleep(1)
    button.click()


    # q 14 تابعیت
    time.sleep(1)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]')))
    button.click()
    time.sleep(0.5)

    # q 15 درصورت تابعیت غیر ایرانی، کشور  را ذکر نمایید.

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button.click()
    time.sleep(0.5)

    # q 16 مدرک تحصیلی
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[2]/div[{grade}]')))
    button.click()
    time.sleep(0.5)

    # q 17 وضعیت اشتغال
    time.sleep(0.5)
    if gender == 2:
        if birth_l in range(1, 3):
            button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
            button.click()
        else:
            button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH,
                f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[4]')))
            button.click()
    else:
        if birth_l < 3:
            button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[8]')))
            button.click()
        else:
            button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH,
                f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[5]')))
            button.click()
    time.sleep(0.5)

    # q 18 قومیت

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]')))
    button.click()
    time.sleep(0.5)

    # q 19 وضعیت مسکن

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[{home}]')))
    button.click()
    time.sleep(0.5)


    # q 20 متراژ خانه محل سکونت


    time.sleep(0.5)
    entry2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/input')))
    entry2.send_keys(home_m)
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button.click()
    time.sleep(0.5)

    # q 21 وضعیت سند خانه محل سکونت

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 22 تاریخ حدودی ساخت خانه محل سکونت   را ذکر نمایید.

    time.sleep(0.5)
    entry2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/div/div/input')))
    entry2.send_keys(rand_date(random.randrange(1, 2)))
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button.click()
    time.sleep(0.5)

    # q 23 تاریخ حدودی شروع زندگی در این محل را ذکر نمایید.

    time.sleep(0.5)
    entry2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/div/div/input')))
    entry2.send_keys(rand_date(random.randrange(3, 4)))
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button.click()
    time.sleep(0.5)

    # q 24 وضعیت مسکن
    time.sleep(0.5)
    if birth_l < 2:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[5]')))
        button.click()
    else:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[11]')))
        button.click()
    time.sleep(0.5)

    # q 25 آیا تجربه مهاجرت از استانی به استان گیر دارید؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 26 آیا تجربه مهاجرت از روستا به شهر را دارید؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[{rand_bit()}]')))
    button.click()
    time.sleep(0.5)

    # q 27 آیا سابقه پرداخت حق بیمه دارید؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[{rand_bit()}]')))
    button.click()
    time.sleep(0.5)

    # q 28 آیا دارای بیمه مکمل درمانی هستید؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[{rand_bit()}]')))
    button.click()
    time.sleep(0.5)

    # q 29 درآمد ماهیانه شما کفاف هزینه‌های زندگی‌تان را برآورده می‌کند؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[{str(int(rand_bit()) + 1)}]')))
    button.click()
    time.sleep(0.5)

    # q 30 آیا از سازمان‌های حمایتی کمکی دریافت می‌کنید؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)


    # q 31 اگر پاسخ مثبت است. نام سازمان یا نهاد را ذکر نمایید.

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button.click()
    time.sleep(0.5)

    # q 32 چقدر از درآمد ماهیانه شما، قابلیت پس‌انداز دارد؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[5]')))
    button.click()
    time.sleep(0.5)


    # q 33 چقدر احساس امنیت در محل زندگی خود دارید؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[3]')))
    button.click()
    time.sleep(0.5)


    # q 34 آیا برنامه‌ای جهت جابه‌جایی از محل فعلی خودتان دارید؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 35 آیا برای اوقات فراغت‌تان برنامه مشخصی دارید؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]')))
    button.click()
    time.sleep(0.5)

    # q 36 چه برنامه ای برای اوقات فراغت خود دارید؟

    time.sleep(0.5)
    entry2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/input')))
    entry2.send_keys(random.choice(fun))
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button.click()
    time.sleep(0.5)

    # q 37 میزان استفاده شما از گوشی هوشمند و شبکه‌های اجتماعی چقدر است؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[3]')))
    button.click()
    time.sleep(0.5)

    # q 38 به چه میزان در فعالیت‌های فرهنگی (مسجد، کانون‌ها و ...) مشارکت دارید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[3]')))
    button.click()
    time.sleep(0.5)

    # q 39 سابقه استفاده از خدمات مشاوره یا مددکاری اجتماعی به چه میزان داشته‌اید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[6]')))
    button.click()
    time.sleep(0.5)

    # q 40 سابقه مصرف مواد مخدر یا محرک دارید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 41 سابقه مصرف سیگار دارید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]')))
    button.click()
    time.sleep(0.5)

    # q 42 آیا سابقه بیماری روانی جدی (مزمن) دارید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 43 آیا سابقه بیماری جسمی جدی (مزمن) دارید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 44 آیا احساس ثبات و امنیت شغلی و حرفه‌ای دارید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 45 به چه میزان تمایل به همکاری جهت حل مشکلات محله و محل زندگی‌تان دارید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 46 در مواقع بروز مشکل تا چه اندازه می‌توانید به اطرافیان خود تکیه کنید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 47 چقدر تمایل دارید تا در فعالیت‌های خیرخواهانه مشارکت داشته باشید؟ چقدر تمایل دارید تا در فعالیت‌های خیرخواهانه مشارکت داشته باشید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]')))
    button.click()
    time.sleep(0.5)

    # q 48 چقدر با نزدیکان‌تان روابط دوستانه و صمیمانه‌ دارید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 49 چقدر احساس پذیرش توسط دیگران در موقعیت‌های اجتماعی مختلف دارید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 50 چقدر احساس می‌کنید منابع و فرصت‌های موجود در جامعه عادلانه توزیع شده است؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[5]')))
    button.click()
    time.sleep(0.5)

    # q 51 در تعاملات و مراودات خود چقدر احساس برخورد یکسان دارید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[4]')))
    button.click()
    time.sleep(0.5)

    # q 52 تا چه اندازه خود را در برابر وظایف شغلی و خانوادگی‌تان متعهد و مسئول می‌دانید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[3]')))
    button.click()
    time.sleep(0.5)

    # q 53 تا چه اندازه خودتان می‌توانید از پس مسائل و مشکلات زندگی‌تان بربیایید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 54 تا چه اندازه از شرایط زندگی خود احساس رضایت و خشنودی دارید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 55 تا چه اندازه توان صبر و تحمل در برابر مسائل و مشکلات زندگی‌تان را دارید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[3]')))
    button.click()
    time.sleep(0.5)

    # q 56 تا چه اندازه تمایل به توسعه مهارت‌های فردی و زندگی‎تان با شرکت در کارگاه‌ها و کلاس‌های آموزشی دارید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]')))
    button.click()
    time.sleep(0.5)

    # q 57 تا چه اندازه برای توسعه مهارت‌های فردی و زندگی‎تان در کارگاه‌ها و کلاس‌های آموزشی شرکت می‌کنید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]')))
    button.click()
    time.sleep(0.5)

    # q 58 چقدر مشارکت و همراهی مردم را جهت حل مشکلات محیط زندگی‌تان، قابل قبول می‌دانید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[3]')))
    button.click()
    time.sleep(0.5)

    # q 59 به عنوان یک شهروند، چقدر خود را موثر و مفید می‌دانید؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[5]')))
    button.click()
    time.sleep(0.5)

    # q 60 میزان پرخاشگری و خشونت‌های اجتماعی در خانواده شما چقدر است؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[5]')))
    button.click()
    time.sleep(0.5)

    # q 61 میزان درگیری و نزاع در محیط پیرامون زندگی‎‌تان به چه میزان است؟
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[4]')))
    button.click()
    time.sleep(0.5)

    # q 62 مهم‌ترین آسیب اجتماعی حوزه زنان در این محله از نظر شما (شهروند) به ترتیب اولویت چیست؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/textarea')))
    button.send_keys(women_c)
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button.click()
    time.sleep(0.5)

    # q 63 مهم‌ترین آسیب اجتماعی حوزه کودکان در این محله از نظر شما (شهروند) به ترتیب اولویت چیست؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/textarea')))
    button.send_keys(child_c)
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button.click()
    time.sleep(0.5)

    # q 64 مهم‌ترین آسیب اجتماعی حوزه جوان در این محله از نظر شما (شهروند) به ترتیب اولویت چیست؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/textarea')))
    button.send_keys(yong_c)
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button.click()
    time.sleep(0.5)

    # q 64 مهم‌ترین آسیب اجتماعی حوزه مردان در این محله از نظر شما (شهروند) به ترتیب اولویت چیست؟

    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/span/textarea')))
    button.send_keys(man_c)
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button')))
    button.click()
    time.sleep(0.5)

    # ارسال
    
    time.sleep(0.5)
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[1]/div[2]/div/div/button')))
    button.click()
    time.sleep(0.5)


    time.sleep(5)
    driver.quit()
    count += 1
    print(count)
    time.sleep(5)
#----------- button

# button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#     (By.XPATH, f'')))
# button.click()
#time.sleep(0.5)

#------date

# #time.sleep(0.5)
# entry = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#     (By.XPATH, f'')))
# entry.send_keys("۱۳۷۸/۰۴/۲۳")
# #time.sleep(0.5)
# button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#     (By.XPATH, f'')))
# button.click()
# time.sleep(0.5)

#--------next

# time.sleep(0.5)
# button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#     (By.XPATH, f'/html/body/div[1]/div/main/div/main/div/div[2]/div/div[2]/div/div[1]/div[1]')))
# button.click()
# time.sleep(0.5)

#--------- entry + button

# time.sleep(0.5)
# entry3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#     (By.XPATH, f'')))
# entry3.send_keys("")
# #time.sleep(0.5)
# button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#     (By.XPATH, f'')))
# button.click()
# time.sleep(0.5)

#------- chose
# button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#     (By.XPATH, f'')))
# button.click()
# time.sleep(0.5)

