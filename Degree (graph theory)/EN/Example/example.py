def start(a, b):
    # Calculate the result of a × b using repeated addition through a while loop
    
    # ╔═══════════════╦════════════════════════════════════╗
    # ║ Variable      ║ Description                        ║
    # ╠═══════════════╬════════════════════════════════════╣
    # ║ a             ║ Counter for repetitions (how many times b is added)   ║
    # ║ b             ║ The constant number being added repeatedly               ║
    # ║ z             ║ The result, starts from 0 and increases with each addition ║
    # ╚═══════════════╩════════════════════════════════════╝
    
    z = 0  # Initial value: z₀ = 0
    
    # ┌──────────────[ Start of the loop ]──────────────┐
    # │  While a > 0:                                   │
    # │     z = z + b      ←  zₙ₊₁ = zₙ + b             │
    # │     a = a - 1       ←  Decrease the counter a    │
    # └─────────────────────────────────────────────┘
    
    while a > 0:
        # 🧮 Operation:
        #    z  →  z + b
        #    a  →  a - 1
        z = z + b
        a = a - 1
    
        # 📊 Example of one iteration:
        #    Before:  [z = 4]  [a = 2]  [b = 2]
        #    After : [z = 6]  [a = 1]  [b = 2]
        #
        #    Diagram of the operation:
        #    ┌──────────────┐
        #    │ z = z + b    │   ← Add b to z
        #    │ a = a - 1    │   ← Decrease the repetition counter
        #    └──────────────┘
    
    # ⛳ After the loop ends (when a = 0):
    # z equals: b + b + ... (a times) = a × b
    return z

# Example: Calculate 3 × 2
# z changes like this: 0 → 2 → 4 → 6
result = start(3, 2)
print(result)  # Output: 6
