from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton


class MainMarkup(InlineKeyboardMarkup):
    InlineKeyboardMarkup()
    def __init__(self, keyboard=None, row_width=1):
        super().__init__(keyboard, row_width)
        self.add(
            InlineKeyboardButton('Помощь', callback_data='/help'),
            InlineKeyboardButton('Построить график', callback_data='/plot')
        )
class PlotMarkup(InlineKeyboardMarkup):
    def __init__(self, keyboard=None, row_width=1):
        super().__init__(keyboard, row_width)
        self.add(
            InlineKeyboardButton('По точкам',callback_data='/plot points'),
            InlineKeyboardButton('На главную',callback_data='/start')
        )
class EmptyMarkup(InlineKeyboardMarkup):
    def __init__(self, keyboard=None, row_width=1):
        super().__init__(keyboard, row_width)
        self.add(
            InlineKeyboardButton('На главную',callback_data='/start')
        )

