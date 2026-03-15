## 2025-03-08 - Protect against DOM XSS from remote error messages
**Vulnerability:** External fetch error strings (`error.message`) were unsafely injected into the UI via `.innerHTML` during catch blocks in 3Dmol.js visualizations.
**Learning:** While usually safe generic network errors, passing any external, dynamic string directly to `innerHTML` creates an XSS vector if the remote endpoint (like rcsb.org or pubchem) were compromised or returned unescaped HTML in error details.
**Prevention:** Always separate static HTML structural injection from dynamic data. Set the HTML scaffold first with `.innerHTML`, then query the specific node and use `.textContent` to inject the untrusted dynamic string.

## 2025-03-08 - Protect against DOM XSS in UI logging utilities
**Vulnerability:** In `CityWaterInfrastructureSimulation.html`, the `addLogEntry` utility directly interpolated string arguments (`msg`) into `p.innerHTML` using an ES6 template literal.
**Learning:** While the input currently came from static strings within the file, utilities like custom loggers are highly likely to eventually print dynamic or user-influenced data (like API responses or dynamic entity names). Keeping raw `innerHTML` generation for generic utility functions is a latent DOM XSS risk waiting to be exploited.
**Prevention:** Instead of string interpolation into `innerHTML`, structure the node securely using `document.createElement()`, assign styling via `.className`, and safely append user strings using `document.createTextNode(msg)` or `element.textContent = msg`.