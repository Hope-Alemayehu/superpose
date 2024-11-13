# Qiskit Hello World

A simple Qiskit program that demonstrates a 50/50 superposition of states using an interferometer.

## How to Use

### Step 1: Create a Virtual Environment
To start, create a new virtual environment by running the following command:

```bash
python -m venv myenv
```
### Step 2: Activate the Virtual Environment
Activate the virtual environment with:

Windows:
```bash
myenv\Scripts\activate
```
Mac/Linux:
```bash
source myenv/bin/activate
```
### Step 3: Install Required Packages
Install the required packages using:

```bash
pip install -r requirements.txt
```
### Step 4: Run the Program
Run the program by entering:

```bash
python Superpose.py
```
### Step 5: Enter Number of Qubits
When prompted, specify the number of qubits you want to use.

### Step 6: View Results
The program will generate a histogram of the measurement outcomes, showing the 50/50 superposition of states.

## What it Does
This program creates a simple interferometer circuit with a specified number of qubits. It applies a Hadamard gate to each qubit, creating a superposition, and then measures the outcome. The result is demonstrated by a histogram displaying the measurement results.

## Requirements
- Python: 3.7 or later (64-bit)
- Qiskit: 0.32.1
- Aer: 0.10.0
- Matplotlib: 3.5.1
