import tkinter.messagebox
import tkinter as tk
import customtkinter as ctk
import calculates
import re

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("test")
        self.geometry(f"{1000}x{650}")
        # self.resizable(False, False)

        self.options = {'padx': 10, 'pady': 10, 'ipadx': 5, 'ipady': 5}

        # Create frame for tht resistors
        tht_frame = FrameTHT(self)
        tht_frame.grid_propagate(False)
        tht_frame.grid(column=0, row=0, columnspan=2, **self.options)

        # Create frame for smd resistors
        self.smd_frame = FrameSMD(self)
        self.smd_frame.grid_propagate(False)
        self.smd_frame.grid(column=0, row=1, **self.options, sticky=ctk.W)

        # Create frame for capacitors
        self.cap_frame = FrameCapacitor(self)
        self.cap_frame.grid_propagate(False)
        self.cap_frame.grid(column=1, row=1, **self.options)

    def create_toplevel(self, text):
        window = ctk.CTkToplevel(self)
        window.geometry("400x200")
        window.title('Warning')

        # create label on CTkToplevel window
        label = ctk.CTkLabel(window, text=text, font=('Ubuntu Light', 20), text_color='#E6C36F')
        label.place(relx=0.5, rely=0.3, anchor='center')

        # create button on CTkToplevel window
        button = ctk.CTkButton(window,
                               text='OK',
                               font=('Ubuntu Light', 17),
                               width=150, height=40,
                               fg_color='#F45F09',
                               hover_color='#986140',
                               command=window.destroy
                               )
        button.place(relx=0.5, rely=0.7, anchor='center')


class FrameTHT(ctk.CTkFrame):
    def __init__(self, container):
        super().__init__(container, width=970, height=300, corner_radius=15)

        self.bands_colors = calculates.BANDS_COLORS

        self.tolerance_colors = calculates.TOLERANCE_COLORS

        self.selected_colors = {}

        # Create label frame name
        self.frames_name = ctk.CTkLabel(self, text='THT Resistors', font=('Ubuntu Light', 12, 'bold'))
        self.frames_name.grid(column=0, row=0, sticky=tkinter.SW, padx=10)

        # Create Label for combobox-es
        self.label_band_1 = ctk.CTkLabel(self, text='First Band', font=('Ubuntu Light', 12, 'bold'))
        self.label_band_1.grid(column=0, row=1)

        self.label_band_2 = ctk.CTkLabel(self, text='Second Band', font=('Ubuntu Light', 12, 'bold'))
        self.label_band_2.grid(column=1, row=1)

        self.label_band_3 = ctk.CTkLabel(self, text='Third Band\n(Optional)', font=('Ubuntu Light', 12, 'bold'))
        self.label_band_3.grid(column=2, row=1)

        self.label_band_4 = ctk.CTkLabel(self, text='Fourth Band\n(Multiplier)', font=('Ubuntu Light', 12, 'bold'))
        self.label_band_4.grid(column=3, row=1)

        self.label_band_1 = ctk.CTkLabel(self, text='Fifth Band\n(eTolerance)', font=('Ubuntu Light', 12, 'bold'))
        self.label_band_1.grid(column=4, row=1)

        # create a combobox
        cb_grid_options = {'row': 2, 'sticky': tk.NS}
        cb_options = {
            'button_color': '#1F6AA5',
            'width': 167,
            'corner_radius': 5,
            'text_color': 'black',
            'font': ('Ubuntu Light', 15),
            'dropdown_font': ('Ubuntu Light', 15),
            'fg_color': '#565B5E'
        }
        self.current_var_1 = ctk.StringVar()
        values = list(self.bands_colors.keys())[:-2]
        values_band_1 = list(self.bands_colors.keys())[1:-2]
        self.combobox_band_1 = ctk.CTkComboBox(self,
                                               variable=self.current_var_1,
                                               state='readonly',
                                               values=values_band_1,
                                               **cb_options,
                                               command=self.color_selected_1
                                               )
        self.combobox_band_1.grid(column=0, padx=(10, 10), **cb_grid_options)

        self.current_var_2 = ctk.StringVar()
        self.combobox_band_2 = ctk.CTkComboBox(self,
                                               variable=self.current_var_2,
                                               state='readonly',
                                               values=values,
                                               **cb_options,
                                               command=self.color_selected_2
                                               )
        self.combobox_band_2.grid(column=1, padx=10, **cb_grid_options)
        self.current_var_3 = ctk.StringVar()
        self.combobox_band_3 = ctk.CTkComboBox(self,
                                               variable=self.current_var_3,
                                               state='readonly',
                                               values=values,
                                               **cb_options,
                                               command=self.color_selected_3
                                               )
        self.combobox_band_3.grid(column=2, padx=10, **cb_grid_options)

        self.current_var_4 = ctk.StringVar()
        multiplier_values = list(self.bands_colors.keys())
        self.combobox_band_4 = ctk.CTkComboBox(self,
                                               variable=self.current_var_4,
                                               state='readonly',
                                               values=multiplier_values,
                                               **cb_options,
                                               command=self.color_selected_4
                                               )

        self.combobox_band_4.grid(column=3, padx=10, **cb_grid_options)

        self.current_var_5 = tk.StringVar()
        tolerance_values = list(self.tolerance_colors.keys())
        self.combobox_band_5 = ctk.CTkComboBox(self,
                                               variable=self.current_var_5,
                                               state='readonly',
                                               values=tolerance_values,
                                               **cb_options,
                                               command=self.color_selected_5
                                               )

        self.combobox_band_5.grid(column=4, padx=(10, 10), **cb_grid_options)

        # default values for combobox-es
        self.combobox_band_1.set('Select colour')
        self.combobox_band_2.set('Select colour')
        self.combobox_band_3.set('Select colour')
        self.combobox_band_4.set('Select colour')
        self.combobox_band_5.set('Select colour')

        # Button calculation for THT resistors
        self.button_calc = ctk.CTkButton(self,
                                         text='Calculate',
                                         font=('Ubuntu Light', 20, 'bold'),
                                         corner_radius=10,
                                         width=167,
                                         height=80,
                                         command=self.button_action
                                         )
        self.button_calc.grid(column=4, row=4, pady=10)

        # Create select code frame
        self.select_code_frame = ctk.CTkFrame(self, fg_color='#242424', corner_radius=15, height=90, width=360)
        self.select_code_frame.grid_propagate(False)
        self.select_code_frame.grid(column=0, row=3, columnspan=2, padx=10, pady=(20, 5), sticky=ctk.W)

        # Create label with name for code frame
        self.sc_frame_name = ctk.CTkLabel(self.select_code_frame,
                                          text='Select number of bands',
                                          font=('Ubuntu Light', 12, 'bold')
                                          )
        self.sc_frame_name.grid(column=0, row=0, padx=10)

        # Create radiobutton-s in code frame
        self.selected_code = tk.StringVar()
        self.selected_code.set('5')
        self.r_4_bands = ctk.CTkRadioButton(self.select_code_frame,
                                            text='4 Bands',
                                            value='4',
                                            variable=self.selected_code,
                                            command=self.change_state,
                                            font=('Ubuntu Light', 15)
                                            )
        self.r_4_bands.grid(column=0, row=1, padx=(30, 15), pady=(20, 30))
        self.r_5_bands = ctk.CTkRadioButton(self.select_code_frame,
                                            text='5 Bands',
                                            value='5',
                                            variable=self.selected_code,
                                            command=self.change_state,
                                            font=('Ubuntu Light', 15)
                                            )
        self.r_5_bands.grid(column=1, row=1, padx=(10, 30), pady=(20, 30))

        # Create result frame
        self.result_frame = ctk.CTkFrame(self, fg_color='#255B12', corner_radius=10, height=80, width=560)
        self.result_frame.grid_propagate(False)
        self.result_frame.grid(column=0, row=4, columnspan=3, padx=10, pady=(5, 5), sticky=ctk.W)

        # create label with result frame name
        self.result_frame_name = ctk.CTkLabel(self.result_frame,
                                              text='Result',
                                              font=('Ubuntu Light', 20, 'bold')
                                              )
        self.result_frame_name.grid(column=0, row=0, padx=10, sticky=ctk.W)

        # Create label with result
        self.result_label = ctk.CTkLabel(self.result_frame,
                                         font=('Ubuntu Light', 35, 'bold'),
                                         text='',
                                         width=400
                                         )
        self.result_label.grid(column=1, row=0, rowspan=2, stick=ctk.NS, pady=20)

        # for widget in self.winfo_children():
        #     widget.grid(padx=14)

    def button_action(self):

        if self.selected_code == '4':
            if len(self.selected_colors) < 4:
                app.create_toplevel(text='You must select colours\nfor all activ bands!')
            else:
                result: str = calculates.resistance_calculation(self.selected_colors)
                # update result label
                self.result_label.configure(text=result)
        else:
            if len(self.selected_colors) < 5:
                app.create_toplevel(text='You must select colours\nfor all activ bands!')
            else:
                result: str = calculates.resistance_calculation(self.selected_colors)

                # update result label
                self.result_label.configure(text=result)

    def change_state(self):
        if self.selected_code.get() == '4':
            self.combobox_band_3.configure(state=ctk.DISABLED)
            self.selected_colors['third_digit'] = 'No band'
            print(self.selected_colors)
        elif self.selected_code.get() == '5':
            self.combobox_band_3.configure(state='readonly')
            self.combobox_band_3.set('Select colour')

    def color_selected_1(self, event):
        self.selected_colors['first_digit'] = self.current_var_1.get()
        print(self.selected_colors)

    def color_selected_2(self, event):
        self.selected_colors['second_digit'] = self.current_var_2.get()
        print(self.selected_colors)

    def color_selected_3(self, event):
        self.selected_colors['third_digit'] = self.current_var_3.get()
        print(self.selected_colors)

    def color_selected_4(self, event):
        self.selected_colors['multiplier'] = self.current_var_4.get()
        print(self.selected_colors)

    def color_selected_5(self, event):
        self.selected_colors['tolerance'] = self.current_var_5.get()
        print(self.selected_colors)


class FrameSMD(ctk.CTkFrame):
    def __init__(self, container):
        super().__init__(container, height=290, width=500, corner_radius=10)

        # Create label widget with frame's name
        self.frames_name = ctk.CTkLabel(self, text='SMD Resistors', font=('Ubuntu Light', 12))
        self.frames_name.grid(column=0, row=0, sticky=ctk.SW, padx=10)

        # create label widget for entry widget
        self.label = ctk.CTkLabel(self, text='Enter resistor code', font=('Ubuntu Light', 18))
        self.label.grid(column=0, row=1, pady=10, padx=20, sticky=ctk.W)

        # create entry widget
        self.code_entry = ctk.CTkEntry(self,
                                       height=35,
                                       fg_color='white',
                                       text_color='black',
                                       font=('Ubuntu Light', 18),
                                       corner_radius=10,
                                       width=180,
                                       placeholder_text='e.g.: 102',
                                       placeholder_text_color='light grey'
                                       )
        self.code_entry.grid(column=1, row=1, padx=10, pady=10, columnspan=2, stick=ctk.E)

        # create frame widget for selecting code
        self.frame_code_selection = ctk.CTkFrame(self, fg_color='#242424', corner_radius=15, height=90, width=470)
        self.frame_code_selection.grid_propagate(False)
        self.frame_code_selection.grid(column=0, row=2, pady=10, padx=10, ipady=5, ipadx=5, columnspan=3, sticky=ctk.W)

        # create label widget with frame code selection name
        self.sc_frame_name = ctk.CTkLabel(self.frame_code_selection, text='Select code type',
                                          font=('Ubuntu Light', 12, 'bold'))
        self.sc_frame_name.grid(column=0, row=0, padx=10)

        # Create radiobutton-s
        self.selected = tk.StringVar()
        self.selected.set('3 numbers code')
        self.code_3_numbers = ctk.CTkRadioButton(self.frame_code_selection,
                                                 text='3 numbers',
                                                 value='3 numbers code',
                                                 variable=self.selected,
                                                 command=self.radiobutton_event
                                                 )
        self.code_3_numbers.grid(column=0, row=1, padx=(0, 5), pady=(20, 30))
        self.code_4_numbers = ctk.CTkRadioButton(self.frame_code_selection,
                                                 text='4 numbers',
                                                 value='4 numbers code',
                                                 variable=self.selected,
                                                 command=self.radiobutton_event
                                                 )
        self.code_4_numbers.grid(column=1, row=1, padx=(5, 5), pady=(20, 30))
        self.code_eia96 = ctk.CTkRadioButton(self.frame_code_selection,
                                             text='EIA96',
                                             value='EIA96 code',
                                             variable=self.selected,
                                             command=self.radiobutton_event
                                             )
        self.code_eia96.grid(column=2, row=1, padx=(5, 5), pady=(20, 30))
        self.code_below_10 = ctk.CTkRadioButton(self.frame_code_selection,
                                                text='below 10Ω',
                                                value='below 10',
                                                variable=self.selected,
                                                command=self.radiobutton_event
                                                )
        self.code_below_10.grid(column=3, row=1, padx=5, pady=(20, 30))

        # Create result frame
        self.result_frame = ctk.CTkFrame(self, fg_color='#255B12', corner_radius=10, height=70, width=330)
        self.result_frame.grid_propagate(False)
        self.result_frame.grid(column=0, row=3, padx=10, pady=(5, 5), columnspan=2, sticky=ctk.W)

        # create label with result frame name
        self.result_frame_name = ctk.CTkLabel(self.result_frame,
                                              text='Result',
                                              font=('Ubuntu Light', 17, 'bold')
                                              )
        self.result_frame_name.grid(column=0, row=0, padx=10, sticky=ctk.W)

        # Create label with result
        self.result_label = ctk.CTkLabel(self.result_frame,
                                         font=('Ubuntu Light', 18, 'bold'),
                                         text='',
                                         width=50
                                         )
        self.result_label.grid(column=1, row=1, sticky=ctk.E)

        # Button calculation for SMD resistors
        self.button_calc = ctk.CTkButton(self,
                                         text='Calculate',
                                         font=('Ubuntu Light', 17, 'bold'),
                                         corner_radius=10,
                                         width=120,
                                         height=50,
                                         command=self.button_action
                                         )
        self.button_calc.grid(column=2, row=3, padx=10, pady=5, sticky=ctk.SE)

    def radiobutton_event(self):
        selected_code = self.selected.get()
        if selected_code == '3 numbers code':
            self.code_entry.configure(placeholder_text='e.g.: 102')
        elif selected_code == '4 numbers code':
            self.code_entry.configure(placeholder_text='e.g.: 1002')
        elif selected_code == 'EIA96 code':
            self.code_entry.configure(placeholder_text='e.g.: B12 or 12B')
        elif selected_code == 'below 10':
            self.code_entry.configure(placeholder_text='e.g.: 2R1 or 2R10')



    def button_action(self):

        entry_value = self.code_entry.get()

        pattern_eia69_2 = r"^([A-FSRXY]|[a-fsrxy])((9[0-6])|([0-8][0-6]))\b"
        pattern_eia69_1 = r"^((60)|([0-5][0-9]))([A-FSRXY]|[a-fsrxy])\b"
        pattern_4_num = r"^[1-9][0-9][0-9][0-9]\b"
        pattern_3_num = r"^[1-9][0-9][0-9]\b"
        pattern_below_10 = r"([0-9][Rr][0-9][0-9]\b)|([0-9][Rr][0-9]\b)"

        if self.selected.get() == '3 numbers code':
            regex_result = re.match(pattern_3_num, entry_value)
            if regex_result:
                result = calculates.smd_3_numb_code_calc(entry_value)
                self.result_label.configure(text=result)
            else:
                app.create_toplevel(text='Entered value is incorrect')

        elif self.selected.get() == '4 numbers code':
            regex_result = re.match(pattern_4_num, entry_value)
            if regex_result:
                result = calculates.smd_4_numb_code_calc(entry_value)
                self.result_label.configure(text=result)
            else:
                app.create_toplevel(text='Entered value is incorrect')

        elif self.selected.get() == 'below 10':
            regex_result = re.match(pattern_below_10, entry_value)
            if regex_result:
                result = calculates.smd_below_10_ohm_calc(entry_value)
                self.result_label.configure(text=result)
            else:
                app.create_toplevel(text='Entered value is incorrect')

        elif self.selected.get() == 'EIA96 code':
            regex_result_1 = re.match(pattern_eia69_1, entry_value)
            regex_result_2 = re.match(pattern_eia69_2, entry_value)
            if regex_result_1 or regex_result_2:
                result = calculates.smd_eia96_calc(entry_value)
                self.result_label.configure(text=result)
            else:
                app.create_toplevel(text='Entered value is incorrect')


class FrameCapacitor(ctk.CTkFrame):
    def __init__(self, container):
        super().__init__(container, height=290, width=440, corner_radius=10)

        # Create label with name for Capacitor's frame
        frames_name = ctk.CTkLabel(self, text='Capacitors', font=('Ubuntu Light', 12))
        frames_name.grid(column=0, row=0, sticky=ctk.SW, padx=10)

        # create label widget for entry widget
        self.label = ctk.CTkLabel(self, text='Enter capacitor code', font=('Ubuntu Light', 18))
        self.label.grid(column=0, row=1, pady=10, padx=20, sticky=ctk.W)

        # create entry widget
        self.code_entry = ctk.CTkEntry(self,
                                       height=35,
                                       fg_color='white',
                                       text_color='black',
                                       font=('Ubuntu Light', 18),
                                       corner_radius=10,
                                       width=180,
                                       placeholder_text='e.g.: 102',
                                       placeholder_text_color='light grey'
                                       )
        self.code_entry.grid(column=1, row=1, padx=10, pady=10, stick=ctk.E)

        # Create segment button widget
        self.segmented_button_var = ctk.StringVar(value="10pF or more")
        self.segment_button = ctk.CTkSegmentedButton(self,
                                                     values=["10pF or more", "below 10pF"],
                                                     corner_radius=10,
                                                     font=('Ubuntu Light', 15, 'bold'),
                                                     variable=self.segmented_button_var,
                                                     height=40,
                                                     command=self.segment_button_event
                                                     )
        self.segment_button.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

        # Create result frame
        self.result_frame = ctk.CTkFrame(self, fg_color='#255B12', corner_radius=10, height=70, width=425)
        self.result_frame.grid_propagate(False)
        self.result_frame.grid(column=0, row=4, padx=10, pady=(5, 5), columnspan=2, sticky=ctk.S)

        # create label with result frame name
        self.result_frame_name = ctk.CTkLabel(self.result_frame,
                                              text='Result',
                                              font=('Ubuntu Light', 17, 'bold')
                                              )
        self.result_frame_name.grid(column=0, row=0, padx=10, sticky=ctk.W)

        # Create label with result
        self.result_label = ctk.CTkLabel(self.result_frame,
                                         font=('Ubuntu Light', 18, 'bold'),
                                         text='',
                                         width=50
                                         )
        self.result_label.grid(column=1, row=1, sticky=ctk.E)

        # Button calculation for SMD resistors
        self.button_calc = ctk.CTkButton(self,
                                         text='Calculate',
                                         font=('Ubuntu Light', 17, 'bold'),
                                         corner_radius=10,
                                         width=120,
                                         height=50,
                                         command=self.button_action
                                         )
        self.button_calc.grid(column=1, row=3, padx=10, pady=(10, 5), sticky=ctk.SE)

    def segment_button_event(self, event):
        choice = self.segmented_button_var.get()

        if choice == "10pF or more":
            self.code_entry.configure(placeholder_text='e.g.: 104')
        elif choice == "below 10pF":
            self.code_entry.configure(placeholder_text='e.g.: 1R0')

    def button_action(self):
        choice = self.segmented_button_var.get()
        entered_value = self.code_entry.get()

        if choice == "10pF or more":
            result = calculates.capacitors_calc(entered_value)
            self.code_entry.delete(0, ctk.END)
            self.result_label.configure(text=result)

        elif choice == "below 10pF":
            result = calculates.capacitors_calc_below_10p(entered_value)
            self.code_entry.delete(0, ctk.END)
            self.result_label.configure(text=result)


if __name__ == "__main__":
    app = App()
    app.mainloop()
