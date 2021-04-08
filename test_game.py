import pytest
from .pages.main_page import MainPage
from .pages.game_page import GameBoard


def test_solver_game(browser):
    link = "https://meduza.io/games/tsvet-nastroeniya-krasnyy-igra-meduzy"
    main_page = MainPage(browser, link)
    main_page.open_browser()
    main_page.start_bnt_click()
    main_page.close_cookies()
    game_page = GameBoard(browser, browser.current_url)
    game_page.switch_to_game_frame()
    for i in range(1,1000):
        game_page.solver_game()
