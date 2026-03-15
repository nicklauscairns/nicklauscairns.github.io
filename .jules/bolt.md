## 2024-03-14 - Uncached DOM queries in animation loops
**Learning:** Found Uncached DOM queries (`document.getElementById`) inside `requestAnimationFrame` loops in `Simulations/EarthSpaceSciences/GreatOxidationEvent.html`.
**Action:** Always cache DOM elements outside of tight animation loops to prevent performance bottlenecks and improve frame rates.

## 2024-05-15 - Uncached DOM queries in EM Radiation Effects animation loop
**Learning:** Found Uncached DOM queries (`document.getElementById`) inside a fast-firing `drawSimulation` update sequence tied to `requestAnimationFrame` in `Simulations/PhysicalSciences/EMRadiationEffects.html`.
**Action:** Always cache DOM elements outside of tight animation loops to prevent performance bottlenecks and improve frame rates.
