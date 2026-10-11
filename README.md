# 🎲 Digital Dice Simulator Using Verilog HDL

A software-based Digital Dice Simulator developed as a Problem-Based Learning (PBL) project for the **Digital Design Through Verilog HDL (DDVH)** course.

The project uses Verilog HDL to generate dice values from 1 to 6, a seven-segment decoder to represent the output, Icarus Verilog for simulation, GTKWave for waveform analysis, and Python Tkinter for the graphical user interface.

## 🎯 Objectives

- Design a digital dice using Verilog HDL.
- Generate dice values from 1 to 6 using a Linear Feedback Shift Register (LFSR).
- Implement a seven-segment display decoder.
- Verify the design using a Verilog testbench.
- Analyze simulation waveforms using GTKWave.
- Develop a graphical interface using Python Tkinter.
- Demonstrate the project using software tools without requiring physical hardware.

## 🛠️ Tools and Technologies

- **Verilog HDL** — digital logic design
- **Icarus Verilog** — compilation and simulation
- **GTKWave** — waveform visualization
- **Python 3** — graphical interface
- **Tkinter** — GUI development
- **Git and GitHub** — source code management

## 📁 Project Structure

```text
Digital-Dice-Simulator/
├── dice.v
├── seg7_decoder.v
├── dice_tb.v
├── dice_interface_tb.v
├── dice_gui.py
├── .gitignore
└── README.md
```

## ⚙️ Features

- Generates dice values between 1 and 6.
- Uses an LFSR-based pseudo-random sequence.
- Converts dice values into seven-segment display patterns.
- Provides Verilog simulation and waveform output.
- Includes a Python graphical interface.
- Demonstrates multiple dice and total-score functionality in the GUI.

## 🚀 Getting Started

### Prerequisites

Install the following software on your computer:

- Python 3
- Icarus Verilog
- GTKWave (optional, for waveform analysis)

Ensure that `python`, `iverilog`, and `vvp` are accessible from your terminal.

### 1. Clone the repository

```bash
git clone https://github.com/Keerthi1072/Digital-Dice-Simulator.git
cd Digital-Dice-Simulator
```

### 2. Compile the Verilog design

```bash
iverilog -g2012 -o dice_sim dice.v dice_tb.v
```

### 3. Run the simulation

```bash
vvp dice_sim
```

### 4. View the waveform

```bash
gtkwave dice.vcd
```

### 5. Compile the GUI interface testbench

```bash
iverilog -g2012 -s dice_interface_tb -o dice_interface dice.v seg7_decoder.v dice_interface_tb.v
```

Create a request file containing `1` before running the interface simulation:

```powershell
Set-Content -Path roll_request.txt -Value "1"
vvp -n dice_interface
```

### 6. Launch the graphical interface

```bash
python dice_gui.py
```

## 🧪 Simulation Results

The initial Verilog simulation generated the following dice sequence:

`6, 1, 3, 4, 5, 1, 4, 2, 6, 1, 4, 2`

The seven-segment decoder was verified for dice values 1 through 6. For example, dice value 6 produces the active-low segment pattern `0000010`.

The LFSR generates a deterministic pseudo-random sequence; statistical uniformity is not guaranteed.

## 🧠 Working Principle

1. The LFSR generates a pseudo-random binary sequence.
2. The dice mapping logic converts the sequence into a value from 1 to 6.
3. The seven-segment decoder converts the value into segment-control bits.
4. The testbench verifies the design and produces simulation output.
5. The Python GUI invokes the Verilog simulator and displays its returned dice result.

## 🔮 Future Enhancements

- Improve pseudo-random distribution and statistical testing.
- Add configurable dice counts and roll history.
- Enhance waveform-based verification.
- Implement the design on an FPGA board if hardware becomes available.
