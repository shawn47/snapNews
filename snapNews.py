# -*- coding: utf-8 -*-

import os, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from cnNewsSpider import extractNewsUrl

def take_screenshot(browser):
    # browser.set_window_size(1200, 900)
    # 以下代码是将浏览器页面拉到最下面。
    browser.execute_script("""
        (function () {
            var y = 0;
            var step = 100;
            window.scroll(0, 0);
            function f() {
                if (y < document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 100);
                } else {
                    window.scroll(0, 0);
                    document.title += "scroll-done";
                }
            }
            setTimeout(f, 1000);
        })();
    """)
    time.sleep(1)

def enNewsSnap(enTargetNewsPlatformUrl):
	# 英文
	enTitleUrlSourceTimeList = extractNewsUrl(enTargetNewsPlatformUrl)
	print(len(enTitleUrlSourceTimeList))

	dateTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	cur_path = os.path.abspath(os.curdir)
	dest_path = cur_path + '/' + dateTime + '_en'
	if not os.path.exists(dest_path):
		os.mkdir(dest_path)

	for inx, t in enumerate(enTitleUrlSourceTimeList):
		title = t[0][0].strip()
		url = t[0][1].strip()
		print(url)		
		source = t[1][0].strip()
		ntime = t[1][1].strip()
		if ('url=' in url):
			url = url.split('url=')[1]
		elif ('q=' in url):
			url = url.split('q=')[1]
		optIndex = url.find('&')
		if (optIndex > 0):
			url = url[0:optIndex]
		print(source)
		print(ntime)
		print(url)
		print(inx)
		print("======")

		imgName = "%s/%s-%d.png" % (dest_path, dateTime, inx)
		print(imgName)
		os.system("phantomjs screenshot.js {} {}".format(url, imgName))

def cnNewsSnap(cnTargetNewsPlatformUrl):
	# 中文
	cnTitleUrlSourceTimeList = extractNewsUrl(cnTargetNewsPlatformUrl)
	print(len(cnTitleUrlSourceTimeList))

	dateTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	cur_path = os.path.abspath(os.curdir)
	dest_path = cur_path + '/' + dateTime + '_cn'
	if not os.path.exists(dest_path):
		os.mkdir(dest_path)

	# h5 mode
	mobile_emulation = {"deviceName" : "iPhone 6"}
	options = Options()
	options.add_experimental_option("mobileEmulation", mobile_emulation)
	driver = webdriver.Chrome(chrome_options = options)

	driver.implicitly_wait(6)

	for inx, t in enumerate(cnTitleUrlSourceTimeList):
		title = t[0][0].strip()
		url = t[0][1].strip()
		print(url)		
		source = t[1][0].strip()
		ntime = t[1][1].strip()
		if ('url=' in url):
			url = url.split('url=')[1]
		elif ('q=' in url):
			url = url.split('q=')[1]
		optIndex = url.find('&')
		if (optIndex > 0):
			url = url[0:optIndex]
		print(url)
		print(inx)
		print("======")

		imgName = "%s/%s-%d.png" % (dest_path, dateTime, inx)
		print(imgName)

		driver.get(url)
		# take_screenshot(driver)
		time.sleep(1)
		driver.get_screenshot_as_file("%s" % (imgName))


	driver.quit()

if __name__ == '__main__':
	# qdr:n 分钟
	# qdr:s 秒
	# qdr:h 小时
	cnTargetNewsPlatformUrl = 'https://www.google.com.hk/search?q=外交部+华春莹&newwindow=1&safe=strict&source=lnms&tbm=nws&sa=X&ved=0ahUKEwiD-bGg7_rdAhWKwMQHHbCWD9kQ_AUIDigB&biw=1280&bih=698&dpr=2&num=20&tbs=qdr:h2,sbd:1'
	enTargetNewsPlatformUrl = 'https://www.google.com.hk/search?q=hua+chun+ying&newwindow=1&safe=strict&source=lnms&tbm=nws&sa=X&ved=0ahUKEwjEpcOBg4beAhUrllQKHdjTAIYQ_AUIDygC&biw=1280&bih=698&dpr=2&num=20&tbs=qdr:n75,sbd:1&hl=en'
	# cnNewsSnap(cnTargetNewsPlatformUrl)
	enNewsSnap(enTargetNewsPlatformUrl)
