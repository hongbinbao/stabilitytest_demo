#!/usr/bin/python
# -*- coding:utf-8 -*- 

import unittest
from uiautomatorplug.android import device as d

class AppStoreTest(unittest.TestCase):
    def setUp(self):
        """
        called before  each test method start.
        """
        #if UI object not found. the watcher method will be invoked
        d.watcher('AUTO_FC_WHEN_ANR').when(text='ANR').when(text='强行关闭') .press('enter')
        d.wakeup() #wakeup device 

    def testLaunchAndExitAppStore(self):
        """
        launch  app store and exit
        """
        #verify App Store exists on home screen
        assert d(text="应用商店").exists, 'App Store icon not found!'
        #click the UI object and wait for the window update
        d(text="应用商店").sibling(className='android.view.View').click.wait()
        #verify the App store was launched successfully
        assert d(resourceId='com.xiaomi.mitv.appstore:id/title_chinese_textview', text='应用商店').wait.exists(timeout=5000), 'launch App Store failed!'
        #send BACK key to exit App Store
        d.press('back')
        #verify if exiting from App Store successfully
        assert d(text="应用商店").wait.exists(timeout=10000), 'exit from App Store failed!' #

    def tearDown(self):
        """
        called after each test method executed.
        """
        for i in xrange(6): d.press('back') #send BACK key 6 times. exit from APP
        d.press('home') #send HOME key. exit from APP
        d.press('home') #send HOME key. exit from APP
        for i in xrange(8): d.press('left') #send LEFT key. and reset the focus of HOME

#nosetests --with-plan-loader --plan-file ./demoplan --loop 2 --with-file-output --verbosity 2