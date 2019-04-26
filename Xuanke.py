from selenium import webdriver
from time import sleep
import random
def Statement():
    print("         关于2018-2019学年第二学期本科生选课选教的通知\n"
          "杜绝恶意抢课行为。学校教学资源可以满足同学们有序、合理的选课需求，学\n"
          "生应当在本专业教学计划前提下量力而行、均衡选课，对利用非法抢课软件恶\n"
          "意抢课、扰乱正常选课秩序的行为，一经查实，学校将强行关闭涉事学生的账\n"
          "号，并依据相关条例予以追责！\n"
          "                                               教务处 2018年12月20日\n\n")

    print("声明:\n"
          "\n"
          "多谢你的支持，本程序只作学习交流使用，仅供个人研究\n"
          "之用，请下载后在24小时内删除，请勿用于商业及非法用\n"
          "途，如由此引起的相关法律法规责任，与Poet无关！\n")
    print("同意此声明请输入Y")
    key = input()
    if key != ('Y' or 'y'):
        print('Byebye~')
        sleep(2)
        exit()

def Rundriver(browser):
    print("此程序是借助python中的selenium,需要的环境/软件/驱动支撑有:Winodws/Linux、Google Chrome、Chromedrive.exe\n")
    print("详细教程请访问：\n"
          "-----------------参考文章-----------------\n"
          "1.官网 http://chromedriver.chromium.org/\n"
          "2.Github关于ChromeDriver的wiki https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver\n"
          "3.如何快速下载、安装和配置chromedriver?  https://jingyan.baidu.com/article/f7ff0bfcdd89ed2e27bb1379.html\n"
          "4.驱动的下载地址: http://chromedriver.storage.googleapis.com/index.html\n"
          "5.提醒一定要浏览器版本与插件版本相对应!\n"
          "!!!6.chromedriver.exe放到chrome的安装目录!!!\n")

    print("请输入chromedriver.exe的路径(与chrome的安装目录一致)，例如:\n"
          "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
    path = input()
    browser = webdriver.Chrome(path)
    browser.implicitly_wait(30)
    return browser

def login(browser):
    try:
        url = "http://my.hfut.edu.cn/login.portal"
        browser.get(url)
    except:
        pass
    count = 0

    while 1:
        print("尝试登录信息门户")
        while 1:
            try:
                print("输入用户名")
                username = input()
                browser.find_element_by_id("username").send_keys(username)
                print("输入密码(信息门户)")
                password = input()
                browser.find_element_by_id("password").send_keys(password)
                print("输入验证码")
                code = input()
                browser.find_element_by_id("code").send_keys(code)
                break
            except:
                count = count + 1
                print("页面加载失败，刷新重试..." + str(count))
                if browser.current_url == url:
                    try:
                        browser.refresh()
                    except:
                        pass
                else:
                    try:
                        browser.get(url)
                    except:
                        pass
                continue

        try:
            browser.find_element_by_xpath("//*[@id=\"loginForm\"]/table[1]/tbody/tr[3]/td/input[1]").click()
            if browser.find_element_by_xpath("//*[@id=\"pp382\"]/a/span").text=="首页":
                print("登陆成功")
                print('正在进行身份核验>>>')
                break
        except:
            print(browser.find_element_by_xpath("//*[@id=\"loginMsg\"]").text)
            print("登录失败")
            login(browser)

def CheckID(browser,s):
    text1 = browser.find_element_by_xpath("//*[@id=\"pf281\"]/div/div[2]/table/tbody/tr/td[2]/div/ul/li[2]").text
    VIPnum = text1[-10:]
    if s.find(VIPnum) < 0:
        print('身份有误!您没有权限使用此程序')
        sleep(2.66)
        exit()
    print('身份正确，欢迎大佬及其家属使用此程序')
    browser.implicitly_wait(120)

def EnterWeb(browser):
    try:
        url2 = "http://jxglstu.hfut.edu.cn/eams5-student/wiscom-sso/login"
        browser.get(url2)
    except:
        pass
    sleep(2)

    try:
        url2 = "http://jxglstu.hfut.edu.cn/eams5-student/for-std/course-select/"
        browser.get(url2)
    except:
        pass

    try:
        browser.find_element_by_xpath("/html/body/div/div[2]/div/div/div[3]/div/h4/a").click()
    except:
        pass

def CoreFunction(browser):
    try:
        print("请输入关键词   (建议:教学班号，因为这样可以保证下方只出现一个\"选课\"按钮，例如:0500075X--001 )     ")
        classname = input()
        browser.switch_to.window(browser.window_handles[1])
        browser.find_element_by_xpath("//*[@id=\"global_filter\"]").send_keys(classname)
    except:
        print("无法输入内容")
        pass
    print("请输入休眠时间区间(具体指点击“选课”到 弹出对话框出现 的时间)(用空格隔开)，例如:1.2 2.6")
    a,b=input().split()
    count = 1
    select = browser.find_element_by_xpath("//*[@id=\"suitable-lessons-table\"]/tbody/tr/td[10]/button")
    #off = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button")
    browser.execute_script("$(arguments[0]).click()", select)
    sleep(random.uniform(float(a), float(b)))
    message = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/h1").text
    while 1:
        print("第" + str(count) + "次选课：\n\t"+ message)
        if message == "选课成功":
            break
        #browser.execute_script("$(arguments[0]).click()", off)
        count = count + 1
        browser.execute_script("$(arguments[0]).click()", select)
        sleep(random.uniform(float(a), float(b)))
        message = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/h1").text
    print("大佬及其家属恭喜你抢到" + classname + '!!!\n\n')
    print("如果还要继续抢其他课，请输入Poet")
    scanf=input()
    if scanf==('Poet'and'poet'and'YzhNB'and'yggnb'):
        EnterWeb(browser)
        CoreFunction(browser)
    else:
        print('祝您抢课愉快，生活幸福,再见!')
        sleep(2.66)
        exit()

def main():
    Statement()
    browser = None
    browser = Rundriver(browser)
    login(browser)
    s = 'Number1,Number2,...,NumberN'
    CheckID(browser,s)
    EnterWeb(browser)
    CoreFunction(browser)

main()
