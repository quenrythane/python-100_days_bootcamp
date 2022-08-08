from time import sleep
from Bot import cookie_bot

game_is_running = True
while game_is_running:
    for _ in range(10):
        for _ in range(10):
            cookie_bot.clicking_cookie(13*6)  # 13 CpS
            cookie_bot.try_catch_golden_cookie()

        cookie_bot.update_products_dict()
        cookie_bot.update_upgrades_list()
        cookie_bot.try_buy_upgrade()
        cookie_bot.try_buy_product()
        print("-*"*20)

    cookie_bot.save_game()


cookie_bot.driver.quit()
sleep(100)
print("exit")
