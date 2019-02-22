import NgaSign
import SMZDM_Sign
from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    #SMZDM 签到
    SMZDM_Sign.SMZDMTrySign(browser)
    print("SMZDM over!")

    #NGA 网站签到 ,nga网页版没有签到按钮
    #NgaSign.NgaTrySign(browser)
