#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 06, 2018 11:09:11 AM -03  platform: Darwin

from zebra import zebra
import json
import pickle
import requests
import logging
from datetime import datetime
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import badgesapp_support

# Your API URL w/o backslash
API_URL = 'https://eb.tems.com.ar/api'


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Application(root)
    badgesapp_support.init(root, top)
    root.mainloop()


w = None


def create_Application(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Application(w)
    badgesapp_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Application():
    global w
    w.destroy()
    w = None


def get_printer_list(zebra):
    return zebra.getqueues()


class Application:
    def __init__(self, top=None):

        self.printer_object = zebra()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font10 = "-family {Helvetica Neue} -size 13 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Helvetica Neue} -size 7 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("600x400+343+138")
        top.title("Mercury Badges")
        top.configure(background="#F8F7FA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.PrinterSelectionCanvas = tk.Canvas(top)
        self.PrinterSelectionCanvas.place(
            relx=0.008,
            rely=0.013,
            relheight=0.975,
            relwidth=0.983,
        )
        self.PrinterSelectionCanvas.configure(background="#F8F7FA")
        self.PrinterSelectionCanvas.configure(highlightbackground="#d9d9d9")
        self.PrinterSelectionCanvas.configure(highlightcolor="black")
        self.PrinterSelectionCanvas.configure(insertbackground="black")
        self.PrinterSelectionCanvas.configure(selectbackground="#c4c4c4")
        self.PrinterSelectionCanvas.configure(selectforeground="black")
        self.PrinterSelectionCanvas.configure(width=283)

        self.log_label = tk.Text(self.PrinterSelectionCanvas)
        self.wl = WidgetLogger(self.log_label)
        self.log_label.place(
            relx=0.034,
            rely=0.564,
            height=144,
            width=415,
        )
        self.log_label.configure(background="#ffffff")
        self.log_label.configure(foreground="#000000")
        self.log_label.configure(highlightbackground="#d9d9d9")
        self.log_label.configure(highlightcolor="black")
        self.log_label.configure(state=tk.DISABLED)

        self.printer_radio_buttons = []
        self.populate_radio_buttons()

        self.choose_printer_label = tk.Label(self.PrinterSelectionCanvas)
        self.choose_printer_label.place(
            relx=0.068,
            rely=0.077,
            height=24,
            width=122,
        )
        self.choose_printer_label.configure(activebackground="#f9f9f9")
        self.choose_printer_label.configure(activeforeground="black")
        self.choose_printer_label.configure(background="#F8F7FA")
        self.choose_printer_label.configure(foreground="#000000")
        self.choose_printer_label.configure(highlightbackground="#d9d9d9")
        self.choose_printer_label.configure(highlightcolor="black")
        self.choose_printer_label.configure(text='''Choose a printer:''')

        self.disclaimer_label = tk.Label(self.PrinterSelectionCanvas)
        self.disclaimer_label.place(
            relx=0.042,
            rely=0.949,
            height=7,
            width=221,
        )
        self.disclaimer_label.configure(activebackground="#f9f9f9")
        self.disclaimer_label.configure(activeforeground="black")
        self.disclaimer_label.configure(background="#F8F7FA")
        self.disclaimer_label.configure(font=font11)
        self.disclaimer_label.configure(foreground="#000000")
        self.disclaimer_label.configure(highlightbackground="#d9d9d9")
        self.disclaimer_label.configure(highlightcolor="black")
        self.disclaimer_label.configure(
            text='''Disclaimer: This app was designed\
to support only Zebra printers.'''
        )

        self.start_button = tk.Button(
            self.PrinterSelectionCanvas,
            command=self.configure_printer,
        )
        self.start_button.place(
            relx=0.746,
            rely=0.233,
            height=22,
            width=125,
        )
        self.start_button.configure(activebackground="#d9d9d9")
        self.start_button.configure(activeforeground="#000000")
        self.start_button.configure(background="#d9d9d9")
        self.start_button.configure(foreground="#000000")
        self.start_button.configure(highlightbackground="#d9d9d9")
        self.start_button.configure(highlightcolor="black")
        self.start_button.configure(relief='raised')
        self.start_button.configure(text='''Connect printer''')

        self.printer_id_label = tk.Label(self.PrinterSelectionCanvas)
        self.printer_id_label.place(
            relx=0.797,
            rely=0.077,
            height=24,
            width=71,
        )
        self.printer_id_label.configure(activebackground="#f9f9f9")
        self.printer_id_label.configure(activeforeground="black")
        self.printer_id_label.configure(background="#F8F7FA")
        self.printer_id_label.configure(foreground="#000000")
        self.printer_id_label.configure(highlightbackground="#d9d9d9")
        self.printer_id_label.configure(highlightcolor="black")
        self.printer_id_label.configure(text='''Printer ID''')

        self.printer_id = tk.Text(self.PrinterSelectionCanvas)
        self.printer_id.place(
            relx=0.746,
            rely=0.128,
            relheight=0.056,
            relwidth=0.212,
        )
        self.printer_id.configure(background="white")
        self.printer_id.configure(font="TkTextFont")
        self.printer_id.configure(foreground="black")
        self.printer_id.configure(highlightbackground="#d9d9d9")
        self.printer_id.configure(highlightcolor="black")
        self.printer_id.configure(insertbackground="black")
        self.printer_id.configure(selectbackground="#c4c4c4")
        self.printer_id.configure(selectforeground="black")
        self.printer_id.configure(width=108)
        self.printer_id.configure(wrap='word')

        self.restore_connection_details()

        self.static_status_label = tk.Label(self.PrinterSelectionCanvas)
        self.static_status_label.place(
            relx=0.811,
            rely=0.31,
            height=30,
            width=52,
        )
        self.static_status_label.configure(activebackground="#f9f9f9")
        self.static_status_label.configure(activeforeground="black")
        self.static_status_label.configure(background="#F8F7FA")
        self.static_status_label.configure(font=font10)
        self.static_status_label.configure(foreground="#000000")
        self.static_status_label.configure(highlightbackground="#d9d9d9")
        self.static_status_label.configure(highlightcolor="black")
        self.static_status_label.configure(text='''Status''')

        self.status_label = tk.Label(self.PrinterSelectionCanvas)
        self.status_label.place(relx=0.775, rely=0.362, height=24, width=97)
        self.status_label.configure(activebackground="#f9f9f9")
        self.status_label.configure(activeforeground="black")
        self.status_label.configure(background="#F8F7FA")
        self.status_label.configure(foreground="#000000")
        self.status_label.configure(highlightbackground="#d9d9d9")
        self.status_label.configure(highlightcolor="black")
        self.status_label.configure(text='''Disconnected''')

        self.refresh_printer_button = tk.Button(self.PrinterSelectionCanvas)
        self.refresh_printer_button.place(
            relx=0.110,
            rely=0.154,
            height=22,
            width=80,
        )
        self.refresh_printer_button.configure(activebackground="#F8F7FA")
        self.refresh_printer_button.configure(activeforeground="#F8F7FA")
        self.refresh_printer_button.configure(background="#F8F7FA")
        self.refresh_printer_button.configure(foreground="#000000")
        self.refresh_printer_button.configure(highlightbackground="#d9d9d9")
        self.refresh_printer_button.configure(highlightcolor="black")
        self.refresh_printer_button.configure(text='''Refresh''')
        self.refresh_printer_button.configure(
            command=self.refresh_radio_buttons,
        )

        self.test_printer_button = tk.Button(self.PrinterSelectionCanvas)
        self.test_printer_button.place(
            relx=0.093,
            rely=0.22,
            height=22,
            width=100,
        )
        self.test_printer_button.configure(activebackground="#F8F7FA")
        self.test_printer_button.configure(activeforeground="#F8F7FA")
        self.test_printer_button.configure(background="#F8F7FA")
        self.test_printer_button.configure(foreground="#000000")
        self.test_printer_button.configure(highlightbackground="#d9d9d9")
        self.test_printer_button.configure(highlightcolor="black")
        self.test_printer_button.configure(text='''Test Printer''')
        self.test_printer_button.configure(command=self.test_printer)

    def configure_printer(self):
        self.printer_object.setqueue(self.selected_printer.get())
        if self.check_saved_settings():
            self.connect_to_printer()
        else:
            self.setup_printer()
            self.connect_to_printer()

    def check_saved_settings(self):
        try:
            conn = self.get_connection_details()
            if (conn['printer_id'] and conn['printer_secret'] and conn['printer_name']):
                if conn['printer_id'] == self.printer_id.get('1.0', tk.END).replace('\n', ''):
                    return True
                else:
                    return False
        except Exception:
            return False

    def setup_printer(self):
        url = '{}/printer/{}/configure/'.format(
            API_URL,
            self.printer_id.get('1.0', tk.END).replace('\n', '')
        )
        r = requests.get(url)
        json_data = json.loads(r.text)
        if json_data.get('secret_key'):
            self.printer_secret_key = json_data.get('secret_key')
            self.save_connection_details()
            self.log(
                'Successfully configured a new printer.'
            )
            self.log(
                'Printer information has been saved.'
            )
        else:
            self.log(
                'Something went wrong while configuring the printer:\n\
{}'.format(json_data.get('Error'))
            )
            self.log(
                'Check on the mercury app online the printer settings.'
            )

    def connect_to_printer(self):
        try:
            self.status_label.configure(text='Ready')
            self.print_from_queue()
        except Exception as e:
            self.log(
                'Connection Error: {}'.format(e)
            )

    def print_from_queue(self):
        queue = self.get_printer_jobs()
        if type(queue) is list:
            if len(queue) > 0:
                for job in queue:
                    self.printer_object.output(job['content'])
                    self.change_job_status(job['job_key'])
            else:
                self.log('Queue is empty')

    def change_job_status(self, job_id):
        url = '{}/printer/{}/job/{}/'.format(
            API_URL,
            self.printer_id.get('1.0', tk.END).replace('\n', ''),
            job_id,
        )
        re = requests.post(url, data={'secret_key': self.printer_secret_key})
        return re.json()

    def get_printer_jobs(self):
        try:
            url = '{}/printer/{}/queue/'.format(
                API_URL,
                self.printer_id.get('1.0', tk.END).replace('\n', '')
            )
            req = requests.get(
                url,
            )
            self.log('Printing Queue @ {}'.format(
                str(datetime.now())
            ))
            if req.json() is dict:
                self.log('Error: {}'.format(req.json()['Error']))
            else:
                for job in req.json():
                    self.log('Sending {} to local queue'.format(job['job_key']))
            return req.json()
        except Exception as e:
            self.log('Error trying to get the printing queue')
            self.log(e)

    def test_printer(self):
        if self.selected_printer.get() != ('' or None):
            self.printer_object.setqueue(self.selected_printer.get())
            self.printer_object.output(badgesapp_support.ZEBRA_TEST_ZPL)
            self.log('Testing printer...')
        else:
            self.log('Please select a printer before testing.')

    def save_connection_details(self):
        if (
            self.printer_id.get('1.0', tk.END) and
                self.printer_id.get('1.0', tk.END) and
                self.selected_printer) != '/n':
            conn = {
                "printer_id":
                self.printer_id.get('1.0', tk.END).replace('\n', ''),
                "printer_secret":
                self.printer_secret_key,
                "printer_name":
                self.selected_printer.get()
            }
            file = open(r'config.pkl', 'wb')
            pickle.dump(conn, file)
            file.close()

    def get_connection_details(self):
        file = open(r'config.pkl', 'rb')
        conn = pickle.load(file)
        file.close()
        return conn

    def restore_connection_details(self):
        try:
            conn = self.get_connection_details()
            self.printer_id.insert(tk.END, conn.get('printer_id'))
            self.printer_secret_key = conn.get('printer_secret')
            self.selected_printer.set(conn.get('printer_name', ''))
            self.log('Connection details were successfully loaded.')
        except Exception:
            self.log('No connection details could be loaded.')

    def refresh_radio_buttons(self):
        for button in self.printer_radio_buttons:
            button.destroy()
        self.populate_radio_buttons()
        self.log('Refreshing printers...')

    def log(self, text):
        self.log_label.configure(state=tk.NORMAL)
        self.wl.emit(text)
        self.log_label.configure(state=tk.DISABLED)
        self.log_label.see(tk.END)

    def populate_radio_buttons(self):
        it = 0
        if len(self.printer_radio_buttons) > 0:
            for button in self.printer_radio_buttons:
                button.destroy()
        self.selected_printer = tk.StringVar()
        self.printer_radio_buttons = []
        for p in self.printer_object.getqueues():
            printer_radio_button = tk.Radiobutton(self.PrinterSelectionCanvas)
            printer_radio_button.place(
                relx=0.305,
                rely=0.077 + it,
                relheight=0.056,
                relwidth=0.4,
            )
            printer_radio_button.configure(activebackground="#d9d9d9")
            printer_radio_button.configure(activeforeground="#000000")
            printer_radio_button.configure(background="#F8F7FA")
            printer_radio_button.configure(foreground="#000000")
            printer_radio_button.configure(highlightbackground="#d9d9d9")
            printer_radio_button.configure(highlightcolor="black")
            printer_radio_button.configure(justify='left')
            printer_radio_button.configure(text=p)
            printer_radio_button.configure(value=p)
            printer_radio_button.configure(variable=self.selected_printer)
            self.printer_radio_buttons.append(printer_radio_button)
            it += 0.055


class WidgetLogger(logging.Handler):
    def __init__(self, widget):
        logging.Handler.__init__(self)
        self.widget = widget

    def emit(self, record):
        self.widget.insert(tk.INSERT, record + '\n')


if __name__ == '__main__':
    vp_start_gui()
