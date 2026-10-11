
import tkinter as tk
from tkinter import ttk
import subprocess
import re
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
REQUEST_FILE = PROJECT_DIR / "roll_request.txt"
SIMULATOR = PROJECT_DIR / "dice_interface"

SYMBOLS = {
    1: "⚀", 2: "⚁", 3: "⚂",
    4: "⚃", 5: "⚄", 6: "⚅"
}

roll_count = 0
history = []

root = tk.Tk()
root.title("Digital Dice Simulator")
root.geometry("520x650")
root.resizable(False, False)
root.configure(bg="#172033")

tk.Label(
    root, text="DIGITAL DICE SIMULATOR",
    font=("Arial", 19, "bold"),
    bg="#172033", fg="white"
).pack(pady=18)

tk.Label(
    root, text="Powered by Verilog + Icarus Verilog",
    font=("Arial", 10), bg="#172033", fg="#CBD5E1"
).pack()

controls = tk.Frame(root, bg="#172033")
controls.pack(pady=16)

tk.Label(
    controls, text="Number of dice:",
    font=("Arial", 12, "bold"),
    bg="#172033", fg="white"
).grid(row=0, column=0, padx=8)

dice_count = tk.IntVar(value=2)
selector = ttk.Combobox(
    controls, textvariable=dice_count,
    values=[1, 2, 3], state="readonly", width=5
)
selector.grid(row=0, column=1, padx=8)

dice_area = tk.Frame(root, bg="#172033")
dice_area.pack(pady=12)

result_label = tk.Label(
    root, text="Choose your dice and roll!",
    font=("Arial", 16, "bold"),
    bg="#172033", fg="#60A5FA"
)
result_label.pack(pady=8)

counter_label = tk.Label(
    root, text="Total rolls: 0",
    font=("Arial", 12),
    bg="#172033", fg="white"
)
counter_label.pack(pady=5)

history_label = tk.Label(
    root, text="Recent results: None",
    font=("Arial", 10),
    bg="#172033", fg="#CBD5E1",
    wraplength=460
)
history_label.pack(pady=8)


def get_verilog_result(request_number):
    REQUEST_FILE.write_text(str(request_number), encoding="utf-8")

    process = subprocess.run(
        ["vvp", "-n", str(SIMULATOR)],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True,
        timeout=5
    )

    output = process.stdout + "\n" + process.stderr

    if process.returncode != 0:
        raise RuntimeError(output.strip() or "Verilog simulation failed")

    match = re.search(r"DICE_RESULT=(\d+)", output)

    if not match:
        raise RuntimeError(output.strip() or "No Verilog result found")

    value = int(match.group(1))

    if value not in SYMBOLS:
        raise RuntimeError(f"Invalid dice value: {value}")

    return value


def roll_dice():
    global roll_count

    button.config(state="disabled")
    result_label.config(text="Rolling...", fg="#FACC15")
    root.update_idletasks()

    try:
        number = dice_count.get()

        # Run the Verilog simulator once for each die.
        values = [
            get_verilog_result(roll_count + i + 1)
            for i in range(number)
        ]

        roll_count += number

        for widget in dice_area.winfo_children():
            widget.destroy()

        for index, value in enumerate(values, start=1):
            card = tk.Frame(
                dice_area, bg="white",
                padx=10, pady=8,
                highlightbackground="#60A5FA",
                highlightthickness=2
            )
            card.grid(row=0, column=index - 1, padx=6)

            tk.Label(
                card, text=SYMBOLS[value],
                font=("Segoe UI Symbol", 54),
                bg="white", fg="black"
            ).pack()

            tk.Label(
                card, text=f"Die {index}: {value}",
                font=("Arial", 10, "bold"),
                bg="white", fg="#172033"
            ).pack()

        total = sum(values)
        result_label.config(
            text=f"Total Score: {total}",
            fg="#60A5FA"
        )

        counter_label.config(text=f"Total dice rolled: {roll_count}")

        history.insert(0, f"{values} = {total}")
        del history[5:]

        history_label.config(
            text="Recent results:\n" + "\n".join(history)
        )

    except Exception as error:
        result_label.config(text="Simulation error", fg="#F87171")
        print("Error:", error)

    finally:
        button.config(state="normal")


button = tk.Button(
    root, text="ROLL DICE",
    font=("Arial", 15, "bold"),
    bg="#22C55E", fg="white",
    activebackground="#16A34A",
    width=18, command=roll_dice
)
button.pack(pady=18)

root.mainloop()
