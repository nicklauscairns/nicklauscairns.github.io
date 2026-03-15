def run():
    with open('Simulations/EarthSpaceSciences/ConnecticutRiverValleyRift.html', 'r') as f:
        lines = f.readlines()

    start_idx = 0
    for i, line in enumerate(lines):
        if '// 5. Apply Global Erosion' in line:
            start_idx = i
            break

    for line in lines[start_idx:start_idx+60]:
        print(line, end="")

run()
