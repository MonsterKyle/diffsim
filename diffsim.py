import random
import time
import tkinter as tk

def main_menu():
    def start_game(duration, test_mode):
        for widget in main_window.winfo_children():
            widget.destroy()

        number_label = tk.Label(main_window, text="", font=("Arial", 36))
        number_label.pack(pady=150)

        previous_number = random.randint(1, 9)
        current_number = 0
        number_label.config(text=str(previous_number))
        main_window.update()
        time.sleep(2)

        start_time = time.time()
        end_time = start_time + duration
        correct_answers = 0
        total_answers = 0

        def check_answer(event):
            nonlocal previous_number, current_number, correct_answers, total_answers
            try:
                player_input = int(event.char)
                difference = abs(previous_number - current_number)
                if player_input == difference:
                    correct_answers += 1
                total_answers += 1
                previous_number = current_number
                generate_next_number()

            except ValueError:
                pass

        def generate_next_number():
            nonlocal current_number, previous_number
            if time.time() < end_time:
                if test_mode:
                    while True:
                        current_number = random.randint(1, 9)
                        if abs(current_number - previous_number) <= 4 and current_number != previous_number:
                            break
                else:
                    while True:
                        current_number = random.randint(1, 9)
                        if current_number != previous_number:
                            break
                number_label.config(text=str(current_number))
                main_window.update()
                main_window.bind("<Key>", check_answer)
            else:
                main_window.unbind("<Key>")
                accuracy = 0.00
                if total_answers > 0:
                    accuracy = (correct_answers / total_answers) * 100
                    accuracy = round(accuracy, 2)

                number_label.config(text=f"Time's up!\nCorrect: {correct_answers}\nTotal: {total_answers}\nAccuracy: {accuracy}%", font=("Arial", 20))
                number_label.pack(pady=10)
                main_window.update()
                restart_button = tk.Button(main_window, text="Main Menu", command=show_main_menu)
                restart_button.pack(pady=20)

        generate_next_number()

    def show_main_menu():
        for widget in main_window.winfo_children():
            widget.destroy()

        test_mode_var = tk.BooleanVar()
        test_mode_check = tk.Checkbutton(main_window, text="Test Mode (Difference <= 4)", variable=test_mode_var)
        test_mode_check.pack(pady=10)

        start_10sec_button = tk.Button(main_window, text="10 Second Mode", command=lambda: start_game(10, test_mode_var.get()))
        start_10sec_button.pack(pady=10)

        start_120sec_button = tk.Button(main_window, text="2 Minute Mode", command=lambda: start_game(120, test_mode_var.get()))
        start_120sec_button.pack(pady=10)

        start_300sec_button = tk.Button(main_window, text="5 Minute Mode", command=lambda: start_game(300, test_mode_var.get()))
        start_300sec_button.pack(pady=10)

    main_window = tk.Tk()
    main_window.title("Difference Game")
    main_window.geometry("640x480")

    show_main_menu()

    main_window.mainloop()

if __name__ == "__main__":
    main_menu()