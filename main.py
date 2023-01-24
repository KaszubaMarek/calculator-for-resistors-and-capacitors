# git@github.com:KaszubaMarek/calculator-for-resistors-and-capacitors.git
from tkinter.messagebox import showinfo
import tkinter.messagebox
import tkinter as tk
import customtkinter as ctk
import calculates

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
        self.sc_frame_name = ctk.CTkLabel(self.select_code_frame, text='Select number of bands', font=('Ubuntu Light', 12, 'bold'))
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
        self.result_label.grid(column=1, row=1, sticky=ctk.E)

        for widget in self.winfo_children():
            widget.grid(padx=14)

    def button_action(self):

        if self.selected_code == '4':
            if len(self.selected_colors) < 4:
                # showinfo(title='Error',
                #          message='You must select colours for all activ bands!')
                app.create_toplevel(text='You must select colours\nfor all activ bands!')
            else:
                result: str = calculates.resistance_calculation(self.selected_colors)
                # update result label
                self.result_label.configure(text=result)
        else:
            if len(self.selected_colors) < 5:
                # showinfo(title='Error',
                #          message='You must select colours for all activ bands!')
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
        super().__init__(container, height=270, width=500, corner_radius=10)

        # Create label widget with frame's name
        frames_name = ctk.CTkLabel(self, text='SMD Resistors', font=('Ubuntu Light', 12))
        frames_name.grid(column=0, row=0, sticky=ctk.SW, padx=10)

        # create label widget for entry widget
        label = ctk.CTkLabel(self, text='Insert code resistor', font=('Ubuntu Light', 18))
        label.grid(column=0, row=1, pady=10, padx=10, sticky=ctk.W)

        # create entry widget
        code = tk.StringVar()
        code_entry = ctk.CTkEntry(self,
                                  textvariable=code,
                                  height=35,
                                  fg_color='white',
                                  text_color='black',
                                  font=('Ubuntu Light', 18),
                                  corner_radius=10,
                                  width=130
                                  )
        code_entry.grid(column=1, row=1, padx=10, pady=10, stick=ctk.E)

        # create frame widget for selecting code
        frame_code_selection = ctk.CTkFrame(self, fg_color='#242424', corner_radius=15, height=90, width=470)
        frame_code_selection.grid_propagate(False)
        frame_code_selection.grid(column=0, row=2, pady=10, padx=10, ipady=5, ipadx=5, columnspan=3, sticky=ctk.W)

        # create label widget with frame code selection name
        self.sc_frame_name = ctk.CTkLabel(frame_code_selection, text='Select code type',
                                          font=('Ubuntu Light', 12, 'bold'))
        self.sc_frame_name.grid(column=0, row=0, padx=10)

        # Create radiobutton-s
        selected = tk.StringVar()
        selected.set('3 numbers code')
        code_3_numbers = ctk.CTkRadioButton(frame_code_selection,
                                            text='3 numbers',
                                            value='3 numbers code',
                                            variable=selected
                                            )
        code_3_numbers.grid(column=0, row=1, padx=(0, 5), pady=(20, 30))
        code_4_numbers = ctk.CTkRadioButton(frame_code_selection,
                                            text='4 numbers',
                                            value='4 numbers code',
                                            variable=selected,
                                            )
        code_4_numbers.grid(column=1, row=1, padx=(5, 5), pady=(20, 30))
        code_eia96 = ctk.CTkRadioButton(frame_code_selection,
                                        text='EIA96',
                                        value='EIA96 code',
                                        variable=selected,
                                     )
        code_eia96.grid(column=2, row=1, padx=(5, 5), pady=(20, 30))
        code_below_10 = ctk.CTkRadioButton(frame_code_selection,
                                           text='below 10Ω',
                                           value='below 10',
                                           variable=selected,
                                           )
        code_below_10.grid(column=3, row=1, padx=5, pady=(20, 30))

        # Create result frame
        self.result_frame = ctk.CTkFrame(self, fg_color='#255B12', corner_radius=10, height=50, width=330)
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

        # Button calculation for THT resistors
        self.button_calc = ctk.CTkButton(self,
                                         text='Calculate',
                                         font=('Ubuntu Light', 17, 'bold'),
                                         corner_radius=10,
                                         width=120,
                                         height=50,
                                         )
        self.button_calc.grid(column=2, row=3, padx=10, pady=10, sticky=ctk.E)


class FrameCapacitor(ctk.CTkFrame):
    def __init__(self, container):
        super().__init__(container, height=270, width=440, corner_radius=10)

        # Create label with name for
        frames_name = ctk.CTkLabel(self, text='Capacitors', font=('Ubuntu Light', 12))
        frames_name.grid(column=0, row=0, sticky=tkinter.SW, padx=10)

        # # create label for entry widget
        # label_code_selection = ttk.LabelFrame(frame_smd, text='Select code type')
        # label_code_selection.grid(column=0, row=1, columnspan=4, pady=5, padx=5, ipady=5, ipadx=5)
        #
        # # Create Entry Widget
        #
        # code = ctk.StringVar()
        # code_entry = ctk.CTkEntry(self, textvariable=code)
        # code_entry.grid(column=1, row=0, padx=30, pady=10, columnspan=3, sticky=tk.W)


if __name__ == "__main__":
    app = App()
    app.mainloop()
