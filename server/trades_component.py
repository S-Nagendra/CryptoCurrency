import tkinter as tk
import typing
import datetime

from main import*
from styling import *


class TradesWatch(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.body_widgets = dict()

        self._headers = ["BUYER", "PAYMENT METHOD", "RATE", "LIMITS", "ACTION"]

        self._table_frame = tk.Frame(self, bg=BG_COLOR)
        self._table_frame.pack(side=tk.TOP)

        for idx, h in enumerate(self._headers):
            header = tk.Label(self._table_frame, text=h.capitalize(), bg=BG_COLOR,
                              fg=FG_COLOR, font=BOLD_FONT)
            header.grid(row=0, column=idx)

    def add_trade(self, trade):

        b_index = self._body_index

        self.body_widgets['Buyer'] = tk.Label(self._table_frame, text=trade.buyer, bg=BG_COLOR, fg=FG_COLOR_2, font=GLOBAL_FONT)
        self.body_widgets['Name'].grid(row=b_index, column=0)

        # Payment method

        self.body_widgets['Payment method'][b_index] = tk.Label(self._table_frame, text=trade.contract.symbol, bg=BG_COLOR,
                                                                fg=FG_COLOR_2, font=GLOBAL_FONT)
        self.body_widgets['Payment method'][b_index].grid(row=b_index, column=1)

        # Rate

        self.body_widgets['Rate'][b_index] = tk.Label(self._table_frame, text=trade.Rate.capitalize(), bg=BG_COLOR, fg=FG_COLOR_2, font=GLOBAL_FONT)
        self.body_widgets['Rate'][b_index].grid(row=b_index, column=2)

        # limits

        self.body_widgets['limits'][b_index] = tk.Label(self._table_frame, text=trade.limits.capitalize(), bg=BG_COLOR, fg=FG_COLOR_2, font=GLOBAL_FONT)
        self.body_widgets['limits'][b_index].grid(row=b_index, column=3)

        # Action

        self.body_widgets['Action'][b_index] = tk.Label(self._table_frame, text=trade.action.capitalize(), bg=BG_COLOR, fg=FG_COLOR_2, font=GLOBAL_FONT)
        self.body_widgets['Action'][b_index].grid(row=b_index, column=4)

        self.body_widgets['Buy'][b_index].config(bg="orange", text="Buy")

        self._body_index += 1


        #---------base parameters-----


        self._base_params = [
            {"code_name": "Buyer name", "widget": tk.OptionMenu, "data_type": str,
             "values": [10], "width": 10, "header": "BUYER"},
            {"code_name": "payment method", "widget": tk.OptionMenu, "data_type": str, "values": self._all_contracts,
             "width": 15, "header": "Payment Method"},
            {"code_name": "timeframe", "widget": tk.OptionMenu, "data_type": str, "values": self._all_timeframes,
             "width": 10, "header": "Rate"},

            {"code_name": "limit", "widget": tk.Entry, "data_type": float, "width": 7, "header": "Limit"},
            {"code_name": "parameters", "widget": tk.Button, "data_type": float, "text": "Buy",
             "bg": BG_COLOR_2, "command": self._show_popup, "header": "", "width": 10},


        ]
