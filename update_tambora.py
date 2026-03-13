import re

with open('Simulations/EarthSpaceSciences/Tambora1816.html', 'r') as f:
    html = f.read()

# 2. Fix inline CSS in Tambora1816.html
style_block_pattern = r'<style>[\s\S]*?</style>'
html = re.sub(style_block_pattern, '', html)

minimal_style = """
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .slider-custom { -webkit-appearance: none; appearance: none; background: transparent; cursor: pointer; }
        .slider-custom::-webkit-slider-runnable-track { width: 100%; height: 6px; border-radius: 3px; background: #475569; }
        .slider-custom::-webkit-slider-thumb { -webkit-appearance: none; appearance: none; width: 18px; height: 18px; border-radius: 50%; background: #38bdf8; margin-top: -6px; }
        .slider-custom::-webkit-slider-thumb:hover { background: #7dd3fc; }
        .slider-custom:disabled::-webkit-slider-thumb { background: #64748b; cursor: not-allowed; }
    </style>
"""

html = html.replace('<script src="https://cdn.tailwindcss.com"></script>', minimal_style)

# Add tailwind classes to elements
html = html.replace('class="min-h-screen flex flex-col items-center p-4"', 'class="min-h-screen flex flex-col items-center p-4 bg-slate-900 text-slate-50 overflow-x-hidden"')
html = html.replace('class="glass-panel ', 'class="bg-slate-800/70 backdrop-blur-md border border-white/10 rounded-xl shadow-lg ')
html = html.replace('id="earthCanvas" width="320" height="320" class="w-full h-full"', 'id="earthCanvas" width="320" height="320" class="w-full h-full rounded-full bg-[radial-gradient(circle_at_30%_30%,#1e40af,#082f49)] shadow-[0_0_20px_rgba(56,189,248,0.2),inset_-20px_-20px_40px_rgba(0,0,0,0.8)]"')
html = html.replace('class="aerosol-overlay inset-0 w-full h-full"', 'class="absolute inset-0 w-full h-full rounded-full pointer-events-none mix-blend-screen"')

with open('Simulations/EarthSpaceSciences/Tambora1816.html', 'w') as f:
    f.write(html)
