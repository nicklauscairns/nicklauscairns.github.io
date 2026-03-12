evaluation = """<details>
  <summary><b>Evaluate Phenomenon & AI Action Items (Click to expand)</b></summary>
  <ul>
    <li>
      <b>Phenomenon Type:</b> Investigative phenomenon. Visually engaging, but addresses a specific chemistry sub-component (patterns of outermost electrons and reactivity) rather than a broad, complex real-world problem.
    </li>
    <li>
      <b>Rating: 3.5 out of 5 stars</b> as an NGSS style phenomenon. It effectively challenges assumptions by letting students test different metals and links the macroscopic reaction to the microscopic atomic structure (Criterion 4: Investigable Through Practices). However, it lacks deep Cultural and Personal Relevance (Criterion 1) out-of-the-box.
    </li>
    <li>
      <b>Dimensional Evaluation & Evidence Statements:</b> The simulation partially enables the target dimensions. It strongly supports the DCI (PS1.A) and CCC (Patterns) by showing causal relationships between valence electrons and reactivity across groups. However, it weakly supports the full SEP (Developing and Using Models); students act as observers rather than developers. Regarding Observable Features, it demonstrates 1.a.i-iii (identifying model components), 2.a.i (arrangement reflects patterns), and parts of 3.b.iii (reactivity trends). It currently fails to support predicting bond formation (3.b.i) or stable ions (3.b.ii).
    </li>
    <li>
      <b>AI Action Items for Improvement:</b>
      <ul>
        <li><b>Improve SEP (Developing Models):</b> Instead of static buttons for 'Drop Li' or 'Drop Na', add a `<input type='range'>` slider or `+`/`-` buttons to let students construct the atom dynamically by adding protons and electrons. Bind this to `elementData` so the simulation calculates reactivity based on the user-built valence shell.</li>
        <li><b>Fulfill Observable Feature 3.b.ii (Stable Ions):</b> Add a UI button labeled "Form Ion". When clicked, trigger an animation to remove the valence electron(s) from `aCanvas` and update the UI to display the resulting stable ion charge (e.g., `Na+`).</li>
        <li><b>Improve Phenomenon Relevance (Criterion 1):</b> Update the `elementDesc` strings for the 'Mystery Metal (X)' to explicitly frame it as a 'Lithium-Ion Battery Fire hazard'. This anchors the chemical principles in a relevant real-world context for high school students.</li>
      </ul>
    </li>
    <li>
      <b>Implementation Checklist for AI Agent:</b>
      <ul>
        <li>[ ] Refactor the UI controls to allow dynamic atom building (protons/electrons) instead of static preset metal buttons.</li>
        <li>[ ] Bind the dynamic atom state to the reaction engine to calculate `reactDuration` and `speed` based on valence electrons.</li>
        <li>[ ] Implement an "Ionize" function and animation in the `aCanvas` to visualize the loss of valence electrons and display the net charge.</li>
        <li>[ ] Rewrite the "Mystery Metal" narrative text to describe a thermal runaway event in a modern battery to increase cultural/personal relevance.</li>
      </ul>
    </li>
  </ul>
</details>"""
print("Drafted evaluation.")
