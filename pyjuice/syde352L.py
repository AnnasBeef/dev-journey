import numpy as np

def calc_params(case, x1, x2, y1, y3, a_volts):
    """
    Returns: OS, zeta, wd, wn, K, num, A, B
    Plant: P(s) = num / (s^2 + A s + B)
    """
    # Overshoot ratio (not percent)
    OS = (y1 - y3) / y3

    # Basic validity checks
    if OS <= 0:
        raise ValueError(f"Overshoot must be > 0. Got OS={OS}. (Need y1 > y3)")
    if x2 <= x1:
        raise ValueError(f"Need x2 > x1. Got x1={x1}, x2={x2}")
    if a_volts == 0:
        raise ValueError("Step input a_volts cannot be 0.")

    # Damping ratio
    lnOS = np.log(OS)
    zeta = -lnOS / np.sqrt(np.pi**2 + lnOS**2)

    # Damped frequency
    if case == 1:
        wd = 2*np.pi / (x2 - x1)   # peak-to-peak
    elif case == 2:
        wd = np.pi / (x2 - x1)     # peak-to-valley (half period)
    else:
        raise ValueError("case must be 1 or 2")

    # Natural frequency
    if zeta >= 1:
        raise ValueError(f"zeta must be < 1 for underdamped assumption. Got zeta={zeta}")
    wn = wd / np.sqrt(1 - zeta**2)

    # Gain
    K = y3 / a_volts

    # Coefficients for the 2nd-order plant
    B = wn**2
    A = 2*zeta*wn
    num = K * wn**2

    return OS, zeta, wd, wn, K, num, A, B


def tf_string(num, A, B, label="P"):
    return (
        f"{label}(s) = ({num:.6g}) / (s^2 + ({A:.6g}) s + ({B:.6g}))"
    )


# -------------------------------
# Collect 5 plants
# -------------------------------
plants = []  # each: dict with case,x1,x2,y1,y3,a,OS,zeta,wd,wn,K,num,A,B

print("Enter 5 trials to build P1..P5.")
for i in range(1, 6):
    print(f"\n--- Trial {i} ---")
    case = int(input("case (1=peak-peak, 2=peak-valley): "))
    x1 = float(input("x1 (s): "))
    x2 = float(input("x2 (s): "))
    y1 = float(input("Y1 (peak value): "))
    y3 = float(input("Y3 (steady-state value): "))
    a  = float(input("a (step input, volts): "))

    OS, zeta, wd, wn, K, num, A, B = calc_params(case, x1, x2, y1, y3, a)

    plants.append({
        "case": case, "x1": x1, "x2": x2, "y1": y1, "y3": y3, "a": a,
        "OS": OS, "zeta": zeta, "wd": wd, "wn": wn, "K": K,
        "num": num, "A": A, "B": B
    })

# -------------------------------
# Output the 5 plant transfer functions
# -------------------------------
print("\n\n==============================")
print("5 Individual Plant Transfer Functions")
print("==============================")
for i, p in enumerate(plants, start=1):
    print(tf_string(p["num"], p["A"], p["B"], label=f"P{i}"))
    print(f"  coeffs: num={p['num']:.6g}, A={p['A']:.6g}, B={p['B']:.6g}")

# -------------------------------
# Average plant (average coefficients)
# -------------------------------
num_avg = float(np.mean([p["num"] for p in plants]))
A_avg   = float(np.mean([p["A"]   for p in plants]))
B_avg   = float(np.mean([p["B"]   for p in plants]))

print("\n\n==============================")
print("Averaged Plant (Coefficient Average)")
print("==============================")
print(tf_string(num_avg, A_avg, B_avg, label="Pavg"))
print(f"  avg coeffs: num_avg={num_avg:.6g}, A_avg={A_avg:.6g}, B_avg={B_avg:.6g}")