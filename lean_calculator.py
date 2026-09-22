print("=== Lean Manufacturing Calculator ===")

available_time = float(input("Available production time (minutes): "))
customer_demand = float(input("Customer demand (units): "))

takt_time = available_time / customer_demand

print("\n--- Process Data ---")

number_of_steps = int(input("Number of process steps: "))

process_times = []
waiting_times = []

for i in range(number_of_steps):

    print(f"\nStep {i + 1}")

    process_time = float(input("Process time: "))
    waiting_time = float(input("Waiting time: "))

    process_times.append(process_time)
    waiting_times.append(waiting_time)


# Calculations

total_process_time = sum(process_times)

total_waiting_time = sum(waiting_times)

lead_time = total_process_time + total_waiting_time

efficiency = (total_process_time / lead_time) * 100


# Bottleneck

bottleneck_time = max(process_times)

bottleneck_step = process_times.index(bottleneck_time) + 1


# Results

print("\n=== RESULTS ===")

print(f"Takt Time: {takt_time:.2f} min/unit")

print(f"Total Process Time: {total_process_time:.2f} min")

print(f"Total Waiting Time: {total_waiting_time:.2f} min")

print(f"Lead Time: {lead_time:.2f} min")

print(f"Process Cycle Efficiency: {efficiency:.2f}%")

print(
    f"Bottleneck: Step {bottleneck_step} "
    f"({bottleneck_time:.2f} min)"
)


if bottleneck_time > takt_time:
    print("Warning: Bottleneck exceeds Takt Time.")
else:
    print("Process capacity meets customer demand.")
