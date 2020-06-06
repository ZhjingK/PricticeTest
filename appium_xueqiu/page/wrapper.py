from functools import wraps

from selenium.webdriver.common.by import By


def handle_black(func):
    # 为了被封装的函数能保留原来的内置属性
    # @wraps(func)
    def wrapper(*args, **kwargs):
        from appium_xueqiu.page.base_page import BasePage
        _black_list = [
            # 后台更新
            (By.ID, 'com.xueqiu.android:id/image_cancel'),
            # 领取福利
            (By.ID, 'com.xueqiu.android:id/ib_close'),
            # 点击搜索按钮，伪造弹窗元素
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, '//*[@text="确认"]'),
            (By.XPATH, '//*[@text="取消"]'),
            (By.XPATH, '//*[@text="下次再说"]')
        ]

        _max_num = 3
        _error_num = 0
        instance: BasePage = args[0]

        try:
            element = func(*args, **kwargs)
            _error_num = 0

            # 隐式等待回复原来的等待，
            instance._driver.implicitly_wait(10)

            return element
        except Exception as e:
            instance._driver.implicitly_wait(1)

            if _error_num > _max_num:
                raise e

            _error_num += 1

            for ele in _black_list:
                ele_list = instance.finds(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return wrapper(*args, **kwargs)

            raise e

    return wrapper
