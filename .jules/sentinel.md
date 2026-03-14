## 2025-03-08 - Protect against DOM XSS from remote error messages
**Vulnerability:** External fetch error strings (`error.message`) were unsafely injected into the UI via `.innerHTML` during catch blocks in 3Dmol.js visualizations.
**Learning:** While usually safe generic network errors, passing any external, dynamic string directly to `innerHTML` creates an XSS vector if the remote endpoint (like rcsb.org or pubchem) were compromised or returned unescaped HTML in error details.
**Prevention:** Always separate static HTML structural injection from dynamic data. Set the HTML scaffold first with `.innerHTML`, then query the specific node and use `.textContent` to inject the untrusted dynamic string.
