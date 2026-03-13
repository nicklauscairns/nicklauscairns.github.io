## 2024-03-14 - Uncached DOM queries in animation loops
**Learning:** Found Uncached DOM queries (`document.getElementById`) inside `requestAnimationFrame` loops in `Simulations/EarthSpaceSciences/GreatOxidationEvent.html`.
**Action:** Always cache DOM elements outside of tight animation loops to prevent performance bottlenecks and improve frame rates.
