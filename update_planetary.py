import re

with open('Simulations/EarthSpaceSciences/PlanetaryDefense.html', 'r') as f:
    html = f.read()

# 1. Replace inline CSS with Tailwind classes

# Find body tag and style block
style_block_pattern = r'<style>[\s\S]*?</style>'
html = re.sub(style_block_pattern, '', html)

# The body tag already has Tailwind classes: class="h-screen flex flex-col items-center justify-center p-4"
# We need to add background styles that were in the second inline style block.
body_tag_pattern = r'<body class="([^"]*)">'
html = re.sub(body_tag_pattern, r'<body class="\1 bg-[radial-gradient(white,rgba(255,255,255,.2)_2px,transparent_2px),radial-gradient(white,rgba(255,255,255,.15)_1px,transparent_1px),radial-gradient(white,rgba(255,255,255,.1)_2px,transparent_2px)] bg-[size:550px_550px,350px_350px,250px_250px] bg-[position:0_0,40px_60px,130px_270px]">', html)

# We will inject the tailwind configuration for animations if needed, but we can also just use standard tailwind or a tiny style tag just for the keyframes.
# The prompt says: "Keep only truly necessary CSS (e.g., keyframes that Tailwind cannot express without config) and minimize it."

minimal_style = """
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .control-range { -webkit-appearance: none; appearance: none; background: transparent; cursor: pointer; }
        .control-range::-webkit-slider-runnable-track { width: 100%; height: 6px; border-radius: 3px; background: #475569; }
        .control-range::-webkit-slider-thumb { -webkit-appearance: none; appearance: none; width: 18px; height: 18px; border-radius: 50%; background: #fb923c; margin-top: -6px; }
        .control-range::-webkit-slider-thumb:hover { background: #fdba74; }
        .control-range:disabled::-webkit-slider-thumb { background: #64748b; cursor: not-allowed; }
        @keyframes explode { 0% { transform: scale(0.1) translate(-50%, -50%); opacity: 1; } 100% { transform: scale(3) translate(-50%, -50%); opacity: 0; } }
        .explosion { animation: explode 0.8s ease-out forwards; }
    </style>
"""

html = html.replace('<script src="https://cdn.tailwindcss.com"></script>', minimal_style)

# Add tailwind classes to elements
html = html.replace('class="glass-panel ', 'class="bg-slate-800/85 backdrop-blur-md border border-white/10 rounded-xl shadow-lg ')
html = html.replace('class="w-full h-full object-contain"', 'class="w-full h-full object-contain bg-slate-950 rounded-lg border border-slate-700"')
html = html.replace('class="explosion transform -translate-x-1/2 -translate-y-1/2"', 'class="absolute w-[50px] h-[50px] bg-[radial-gradient(circle,#fbbf24_0%,#ef4444_50%,rgba(255,0,0,0)_100%)] rounded-full pointer-events-none hidden explosion"')

# Remove the second inline style block
html = re.sub(r'<!-- Background Stars \(CSS only for body\) -->[\s\S]*?</style>', '', html)


# 5. Fix premature success status
# Find: if (timeYears > 2.0 && !collisionOccurred) {
new_success_logic = """
            // Check success (missed closely and moving away, or safely far)
            const dotProduct = dx * asteroid.vx + dy * asteroid.vy;
            // If distance is large enough or moving away
            if (timeYears > 1.2 && !collisionOccurred && dotProduct > 0 && distToEarth > EARTH_RADIUS_AU * 2) {
                // Determine minimum distance passed
                els.trajStatus.textContent = "EARTH SAVED!";
                els.trajStatus.className = "text-green-400 font-bold";
                els.statusOverlay.style.borderColor = "#10b981"; // green
            }
"""
html = re.sub(r'// Check success \(missed closely and moving away, or safely far\)[\s\S]*?// Allow it to keep running, but we marked success\s*\}', new_success_logic.strip(), html)


# 6. Fix 1/r^2 singularity
new_accel = """
        function updateAccel() {
            const r2 = asteroid.x*asteroid.x + asteroid.y*asteroid.y;
            const r = Math.sqrt(r2);
            if (r < 0.01) return; // Prevent singularity
            const aMag = -(G * M_SUN) / r2;
            asteroid.ax = aMag * (asteroid.x / r);
            asteroid.ay = aMag * (asteroid.y / r);
        }
"""
html = re.sub(r'function updateAccel\(\) \{[\s\S]*?\}', new_accel.strip(), html)


with open('Simulations/EarthSpaceSciences/PlanetaryDefense.html', 'w') as f:
    f.write(html)
