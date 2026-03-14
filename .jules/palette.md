## 2024-05-18 - Missing label 'for' attributes in simulation inputs
**Learning:** Found that multiple NGSS HTML simulation forms (`<input type="range">`) did not correctly associate their `<label>` elements with the corresponding inputs using the `for` attribute. This breaks screen reader functionality and clicking labels doesn't focus the sliders.
**Action:** Always ensure any `<label>` has a `for="[input_id]"` when paired with form inputs, and use `aria-describedby` when there is supplemental helper text below the label.
