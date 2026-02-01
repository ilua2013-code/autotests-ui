import allure
from elements.base_element import BaseElement
from playwright.sync_api import  expect, Locator

class FileInput(BaseElement):
    @property
    def type_of(self):
        return "file input"

    def set_input_file(self, file: str, nth: int = 0, **kwargs):
        with allure.step(f'Set file {file} to thbe {self.type_of} "{self.name}'):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)