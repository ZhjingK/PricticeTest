from selenium.webdriver.common.by import By


def handler_black(func):
    def wrapper(*args, **kwargs):
        from AppTestHomework.page.basepage import BasePage

        _black_list = [
            (By.XPATH, '//*[@text="确认"]'),
            (By.XPATH, '//*[@text="下次再说"]'),
            (By.XPATH, '//*[@text="确定"]'),
        ]

        _max_num = 3
        _error_num = 0

        instance: BasePage = args[0]

        try:
            element = func(*args, **kwargs)

            _error_num = 0
            instance.driver.implicitly_wait(5)
            return element

        except Exception as e:
            instance.driver.implicitly_wait(1)

            if _error_num > _max_num:
                raise e

            _error_num += 1

            for black in _black_list:
                ele = instance.finds(*black)
                if len(ele) > 0:
                    ele[0].click()

                    return wrapper(*args, **kwargs)
            raise e

    return wrapper


