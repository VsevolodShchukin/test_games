from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import GameLocators

class GameBoard(BasePage):
    def switch_to_game_frame(self):
        self.browser.switch_to.frame("/embed/colors-game")

    def solver_game(self):
        backgrounds = []
        boxes = self.browser.find_elements(*GameLocators.ALL_BOXES_IN_BOARD)
        number_of_boxes = len(boxes)
        for value in boxes:
            styles_of_box = value.get_attribute("style")
            backgrounds.append(styles_of_box)

        for i in range(number_of_boxes):
            if i == number_of_boxes - 1:
                correct_child = number_of_boxes
                break
            elif backgrounds[i] != backgrounds[i + 1] and backgrounds[i] != backgrounds[i - 2]:
                correct_child = str(i+1)
                break
            else:
                i = i + 1
        correct_color = f"._3K3dipl65wOMpaMU-KVKf0:nth-child({correct_child})"
        correct_btn = self.browser.find_element(By.CSS_SELECTOR, correct_color)
        correct_btn.click()