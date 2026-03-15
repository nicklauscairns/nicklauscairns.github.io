# NGSS High School Earth and Space Sciences Standards Aligned Content

## Simulations

### HS-ESS1-1
Develop a model based on evidence to illustrate the life span of the sun and the role of nuclear fusion in the sun’s core to release energy in the form of radiation.

- [Stellar Phenomena Simulator](StellarPhenomenaSimulator.html) - An interactive simulation exploring the stages of stellar life, from a stellar nursery to a star's ultimate fate.

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.0/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Functions as a strong investigative phenomenon for stellar evolution (Criterion 4). Students can explore different stellar life cycles. However, it could be improved by connecting stellar nucleosynthesis to the elements in our everyday lives (Criterion 1: Cultural and Personal Relevance).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports the DCI (ESS1.A) regarding the lifespan of the sun and nuclear fusion, and the CCC (Energy and Matter). For HS-ESS1-1, it demonstrates 1.a.i (identifying components like hydrogen, helium, energy) and 2.a (relationships between fusion and energy). It could better support HS-ESS1-3 by explicitly showing the production of specific elements over the life cycle.
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Improve DCI Alignment (HS-ESS1-3):</b> Add a specific "Nucleosynthesis Tracker" UI element that highlights which elements (e.g., Carbon, Oxygen, Iron) are currently being fused during each stage of the star's life cycle.</li>
          <li><b>Enhance Relevance (Criterion 1):</b> Add an informational pop-up or text area that connects the elements being produced (e.g., Iron) to their presence on Earth and in the human body ("we are made of star-stuff").</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Implement a "Nucleosynthesis Tracker" UI panel displaying current elements being fused.</li>
          <li>[ ] Add narrative text linking stellar element production to elements found on Earth and in biological systems.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ESS1-2
Construct an explanation of the Big Bang theory based on astronomical evidence of light spectra, motion of distant galaxies, and composition of matter in the universe.

- [Big Bang Evidence Explorer](BigBangEvidenceExplorer.html) - An interactive exploration of the three key pieces of evidence supporting the Big Bang Theory: cosmic redshift, primordial composition, and the cosmic microwave background.

  <details>
    <summary><b>Evaluation: Anchoring Phenomenon | 4.5/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Excellent anchoring phenomenon for cosmological theories. It clearly presents the three key pillars of evidence for the Big Bang (Criterion 4). It is highly engaging but is somewhat abstract (Criterion 1), which is typical for cosmology.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Fully supports the DCI (ESS1.A) and CCC (Energy and Matter). For HS-ESS1-2, it successfully demonstrates 1.a.i, ii, and iii (identifying evidence from spectra, CMB, and composition) and supports constructing the explanation (3.a).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance SEP (Constructing Explanations):</b> Add a "Student Explanation Builder" text area where users must synthesize the three pieces of evidence (Redshift, CMB, Composition) into a cohesive written explanation of the Big Bang, perhaps with guided prompts.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Implement a text area for students to write an explanation.</li>
          <li>[ ] Add guided prompts within the text area based on the three pieces of evidence.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ESS1-3
Communicate scientific ideas about the way stars, over their life cycle, produce elements.

- [Stellar Nucleosynthesis Explorer](StellarNucleosynthesis.html) - An interactive simulation demonstrating the life cycle of stars (low and high mass) and how they produce elements through nuclear fusion and supernovae, with real-time nucleon conservation tracking.

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.5/5 Stars | 2026-03-13 14:43:55</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Excellent investigative phenomenon for stellar nucleosynthesis (Criterion 4). Students can actively explore how different initial masses lead to different life cycles and element production. The atomic balancer effectively reinforces conservation laws.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports the DCI (ESS1.A) regarding the production of elements in stars and supernovae, and the CCC (Energy and Matter) via explicit nucleon tracking. For HS-ESS1-3, it provides the interactive model needed to communicate how stars produce elements over their life cycles.
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Improve SEP (Communicating Information):</b> Add a feature where students can generate a "Stellar Report Card" at the end of a star's life, summarizing the elements produced and the conservation of matter, which they can then use to communicate their findings.</li>
          <li><b>Enhance Relevance (Criterion 1):</b> Include visual percentages or abundances of the created elements relative to what is found in the human body or on Earth.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Implement a "Stellar Report Card" summary view at the end of the simulation.</li>
          <li>[ ] Add elemental abundance comparisons (e.g., "This Iron is found in your blood").</li>
        </ul>
      </li>
    </ul>
  </details>



### HS-ESS1-4
Use mathematical or computational representations to predict the motion of orbiting objects in the solar system.

- [Planetary Defense: Asteroid Deflection](PlanetaryDefense.html) - Use orbital mechanics and kinetic impactors to alter an asteroid's trajectory and save Earth from a catastrophic collision. [2026-03-14 04:45:29]

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.5/5 Stars | 2026-03-14 04:45:29</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Highly engaging investigative phenomenon applying orbital mechanics to a high-stakes scenario. Meets Criterion 1 (Relevance) through the existential threat of asteroid impact and Criterion 4 (Investigable) through interactive trajectory modification.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports DCI (ESS1.B) regarding Earth and the solar system and DCI (PS2.A) on forces and motion. Supports SEP (Using Mathematics and Computational Thinking).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance SEP (Computational Modeling):</b> Explicitly show the change in orbital parameters (e.g., semi-major axis, eccentricity) before and after the kinetic impact.</li>
          <li><b>Include Realistic Constraints:</b> Introduce a "budget" or "launch window" constraint to force students to optimize the timing and mass of their kinetic impactor.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Display orbital parameters (semi-major axis, eccentricity) in real-time.</li>
          <li>[ ] Add budget/launch window constraints to the mission parameters.</li>
        </ul>
      </li>
    </ul>
  </details>

- [Orbital Motion & Kepler's Laws Simulation](OrbitalMotion2.html) - An interactive simulation exploring Newton's Law of Universal Gravitation and Kepler's Laws by adjusting planetary parameters.

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 3.5/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Good investigative phenomenon for exploring gravitational forces and planetary orbits. Students can adjust parameters to see effects (Criterion 4). It lacks a direct connection to a real-world problem or relatable scenario (Criterion 1).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Supports the DCI (ESS1.B) and CCC (Systems and System Models). For HS-ESS1-4, it demonstrates using computational representations to predict motion (1.a, 2.a). However, it could be more explicit in demonstrating Kepler's Laws quantitatively.
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Improve Quantitative Modeling (SEP):</b> Add a real-time data table or graph that explicitly calculates and displays the values for Kepler's Laws (e.g., T^2 / a^3) as the simulation runs, allowing students to verify the laws mathematically.</li>
          <li><b>Enhance Relevance (Criterion 1):</b> Include a scenario where students must adjust parameters to successfully insert a satellite into a specific orbit (like a geostationary orbit or a Mars transfer orbit).</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Add a real-time data table displaying calculations for Kepler's Laws.</li>
          <li>[ ] Create a "Satellite Insertion Challenge" scenario with specific target parameters.</li>
        </ul>
      </li>
    </ul>
  </details>

- [Orbital Motion & Kepler's Third Law](OrbitalMotion.html) - An interactive simulation exploring how star mass, initial distance, and velocity affect a planet's orbit, and demonstrating Kepler's Third Law.

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 3.5/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Similar to OrbitalMotion2, this is a solid investigative phenomenon for exploring orbital dynamics (Criterion 4). It is primarily a physics sandbox and lacks a specific driving question or problem (Criterion 1).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Supports the DCI (ESS1.B) and CCC (Systems and System Models) for HS-ESS1-4. It allows for qualitative observation of Kepler's Third Law.
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Improve Differentiation:</b> Clearly distinguish the learning objectives of this simulation from `OrbitalMotion2.html`. Focus this one specifically on Kepler's Third Law by providing multiple planets simultaneously for comparison of their periods and distances.</li>
          <li><b>Enhance SEP (Using Mathematical Representations):</b> Add a graphing feature that plots Orbital Period (T) vs. Semi-major Axis (a) to visually demonstrate the T^2 vs a^3 relationship.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Modify the simulation to support multiple orbiting bodies simultaneously.</li>
          <li>[ ] Implement a dynamic graph plotting Orbital Period vs. Semi-major Axis.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ESS1-5
Evaluate evidence of the past and current movements of continental and oceanic crust and the theory of plate tectonics to explain the ages of crustal rocks.

- [Radiometric Dating Explorer](RadiometricDatingExplorer.html) - An interactive tool simulating radioactive decay to demonstrate how scientists determine the absolute ages of crustal rocks and meteorites.

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.0/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Effectively serves as an investigative phenomenon for understanding radioactive decay and absolute dating (Criterion 4). It challenges the assumption that rocks can't be dated accurately. It could be grounded better with specific, famous rock formations or meteorites (Criterion 1).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports the DCI (ESS1.C) regarding the age of crustal rocks and meteorites, and the CCC (Stability and Change). For HS-ESS1-5 and HS-ESS1-6, it demonstrates applying scientific reasoning based on ancient materials (1.a, 2.a).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance Relevance (Criterion 1):</b> Replace generic "Rock Sample A" with actual examples (e.g., Acasta Gneiss, Allende Meteorite) with brief descriptions of their significance in determining Earth's age.</li>
          <li><b>Improve SEP (Evaluating Evidence):</b> Add a feature where students must compare the dating results of different isotopes (e.g., U-Pb vs. K-Ar) on the same sample to evaluate the reliability and concordance of the evidence.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Replace generic samples with specific, historically significant rock/meteorite examples.</li>
          <li>[ ] Implement a "Concordance Check" feature allowing comparison of different isotopic dating methods on the same sample.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ESS1-6
Apply scientific reasoning and evidence from ancient Earth materials, meteorites, and other planetary surfaces to construct an account of Earth’s formation and early history.

- [Cratering & Surface Age Explorer](CrateringHistory.html) - Investigate why Earth has so few visible impact craters compared to the Moon, despite forming at the same time 4.6 billion years ago.

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 5/5 Stars | 2026-03-13 20:22:40</b></summary>
    <ul>
      <li><b>Overview:</b> The simulation successfully demonstrates how heavy bombardment affected both Earth and the Moon equally early in their histories, but Earth's active geological processes subsequently erased its craters. This directly addresses the performance expectation by providing visual evidence and allowing for scientific reasoning about surface age.</li>
      <li><b>Dimensional Evaluation & Evidence Statements:</b> The simulation strongly aligns with the DCIs regarding the history of planet Earth (ESS1.C) and incorporates the SEP of constructing explanations by providing an interactive model. It also effectively utilizes the CCC of Stability and Change.</li>
      <li><b>AI Action Items for Improvement:</b> None at this time. The simulation meets all current requirements and incorporates previous code review feedback.</li>
      <li><b>Implementation Checklist for AI Agent:</b> All initial and peer-review items completed.</li>
    </ul>
  </details>




### HS-ESS2-1
Develop a model to illustrate how Earth’s internal and surface processes operate at different spatial and temporal scales to form continental and ocean-floor features.

- [Hartford Basin Rift & Dinosaur Tracks Modeler](HartfordBasinRiftModel.html) - An interactive simulation of the Central Valley of Connecticut, modeling how Triassic rifting, Jurassic sedimentation and volcanism, and Pleistocene glaciation interact to preserve and expose dinosaur tracks. [2026-03-15 07:15:00]

  <details>
    <summary><b>Evaluation: Anchor Phenomenon | 5.0/5 Stars | 2026-03-15 07:15:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Phenomenal anchor for New England students. Meets Criterion 1 (Relevance) by using a famous local state park (Dinosaur State Park in Rocky Hill, CT) and Criterion 4 (Investigable) by allowing students to manipulate deep-time geological forces (rifting, lava flows, glaciation) to solve the mystery of why the tracks are exposed today.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Directly supports DCI (ESS2.A) regarding Earth's materials and systems and DCI (ESS2.B) on plate tectonics. Strongly supports SEP (Developing and Using Models) and CCC (Scale, Proportion, and Quantity) by illustrating interactions across hundreds of millions of years.
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance Crosscutting Concepts:</b> Include explicit scale markers or a timeline mini-map to better emphasize the temporal jumps between the 200 Ma deposition and the 10k Ya glaciation.</li>
          <li><b>Improve Interactivity:</b> Allow users to vary the sediment thickness or the basalt thickness to see how different deposition rates would have changed the modern surface geology.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Add an interactive timeline mini-map showing the current epoch.</li>
          <li>[ ] Add user controls for sediment and basalt layer thicknesses.</li>
        </ul>
      </li>
    </ul>
  </details>
- [Connecticut River Valley Rift Simulation](ConnecticutRiverValleyRift.html) - Explore the 200-million-year geological history of the Hartford Basin, Portland brownstone deposition, and the volcanic Metacomet Ridge in Central Connecticut.
- [Metacomet Ridge Formation](MetacometRidgeFormation.html) - An interactive geological simulation modeling the formation of the Metacomet Ridge, including Higby and Beseck Mountains in Middletown, Connecticut.

- [Tectonic Landscape Modeler](TectonicLandscapeModeller.html) - An interactive simulation exploring how slow constructive forces (uplift) and destructive forces (weathering, mass wasting) shape Earth's surface over geologic time.

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.0/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Excellent investigative phenomenon for visualizing deep time and slow geological processes (Criterion 4). It allows students to compress millions of years to see the interplay of constructive and destructive forces. It could use more specific real-world geographical connections (Criterion 1).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports the DCI (ESS2.A) regarding Earth's materials and systems, and the CCC (Stability and Change). For HS-ESS2-1, it demonstrates 1.a (identifying components of the model) and 2.a (relationships between uplift and erosion).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance Relevance (Criterion 1):</b> Add "Scenario Presets" based on real locations (e.g., "Himalayas" with high uplift, "Appalachians" with high erosion/low uplift) to anchor the abstract model to tangible places.</li>
          <li><b>Improve SEP (Developing and Using Models):</b> Allow students to directly manipulate the spatial scale (e.g., zooming in on a specific mountain vs. viewing a whole continent) to better fulfill the "different spatial and temporal scales" aspect of the standard.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Create real-world geographical preset buttons that configure the uplift/erosion parameters.</li>
          <li>[ ] Implement a spatial zoom feature to change the scale of observation.</li>
        </ul>
      </li>
    </ul>
  </details>

- [Puerto Rico Trench Gravity Anomaly](PuertoRicoTrenchGravityAnomaly.html) - Model the subduction of the North American plate under the Caribbean plate to investigate the massive free-air gravity anomaly of the Puerto Rico Trench.

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.5/5 Stars | 2026-03-14 19:43:34</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Highly specific and engaging investigative phenomenon. Meets Criterion 1 (Relevance) through its focus on Puerto Rico, and Criterion 5 (Challenges Assumptions) by introducing "mystery variables" like crustal thinning and carbonate platforms to explain extreme gravitational deficits.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports the DCI (ESS2.B) on plate tectonics and ocean-floor features, and the SEP (Developing and Using Models). For HS-ESS2-1, it demonstrates the relationship between internal processes (subduction, density) and surface measurements (gravity anomalies).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance Data Analysis:</b> Add a feature to overlay actual satellite gravity data points alongside the simulated curve to allow students to evaluate the accuracy of their model.</li>
          <li><b>Improve Interactivity:</b> Implement draggable control points on the 3D crust mesh to manually warp the subduction angle at different depths rather than using a single slider.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Overlay real-world satellite gravity data on the Chart.js graph.</li>
          <li>[ ] Implement draggable control points for the subducting slab in Three.js.</li>
        </ul>
      </li>
    </ul>
  </details>

- [Formation of the Metacomet Ridge](HartfordBasinGeology.html) - An interactive Earth science simulation allowing students to model the tectonic rifting, volcanism, and glacial erosion that formed the Metacomet Ridge in Central Connecticut (e.g., Mount Higby). Aligns with NGSS HS-ESS2-1.
### HS-ESS2-2
Analyze geoscience data to make the claim that one change to Earth's surface can create feedbacks that cause changes to other Earth systems.

- [Ice-Albedo Feedback Loop](IceAlbedoFeedback.html) - An interactive simulation demonstrating the positive feedback loop between rising global temperatures, melting sea ice, and decreasing surface albedo.

  <details>
    <summary><b>Evaluation: Anchoring Phenomenon | 4.5/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Strong anchoring phenomenon for understanding climate feedback loops. The visual melting of ice and corresponding temperature rise is clear and immediate (Criterion 4). It connects well to current events and global climate concerns (Criterion 1).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Directly supports the DCI (ESS2.A) on Earth materials and systems and the CCC (Stability and Change). For HS-ESS2-2, it allows students to analyze data to make claims about feedbacks (1.a, 3.a).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance SEP (Analyzing Data):</b> While the visual is good, add a data logging feature that records Temperature and Albedo over time into a downloadable CSV or an on-screen table, so students can perform quantitative analysis.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Add a "Data Log" table that populates with Temperature, Ice Cover, and Albedo values at regular intervals.</li>
          <li>[ ] Implement a "Download CSV" button for the logged data.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ESS2-3
Develop a model based on evidence of Earth’s interior to describe the cycling of matter by thermal convection.

- [Mantle Convection Explorer](MantleConvectionExplorer.html) - An interactive simulation exploring how the outward flow of energy from Earth's core drives thermal convection in the mantle and the surface expression of plate tectonics.

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 3.5/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Good investigative phenomenon for visualizing the unseen process of mantle convection (Criterion 4). It helps bridge the gap between core heat and surface tectonics. It can feel a bit disconnected from human experience (Criterion 1).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Supports the DCI (ESS2.A, ESS2.B) on Earth materials/systems and plate tectonics, and the CCC (Energy and Matter). For HS-ESS2-3, it demonstrates the model of thermal convection (1.a, 2.a).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Improve SEP (Developing Models):</b> Instead of just watching convection happen, allow students to draw or place heat sources and sinks to see how the convection cells form and change in response to their inputs.</li>
          <li><b>Enhance Relevance (Criterion 1):</b> Connect the upwelling magma to specific surface features, like mid-ocean ridges or volcanic hotspots (e.g., Hawaii), perhaps with a split-screen view showing the surface impact.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Allow user placement of heat sources/sinks at the core-mantle boundary.</li>
          <li>[ ] Add a "Surface View" UI element that correlates mantle upwelling to surface volcanic activity.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ESS2-4
Use a model to describe how variations in the flow of energy into and out of Earth’s systems result in changes in climate.

- [Tambora 1816: Year Without a Summer](Tambora1816.html) - Investigate how stratospheric aerosols from a massive volcanic eruption affected Earth's energy budget and caused the 1816 global climate anomaly. [2026-03-14 05:04:50]

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.5/5 Stars | 2026-03-14 05:04:50</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Excellent investigative phenomenon linking geological events to global climate changes. Meets Criterion 4 (Investigable) by modeling the effects of stratospheric aerosols on Earth's energy budget.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports DCI (ESS2.D) regarding weather and climate and DCI (ESS2.A) on Earth materials and systems. Supports SEP (Developing and Using Models).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Fulfill Observable Feature 3.a (Analyzing Data):</b> Include historical temperature anomaly data alongside the simulated results so students can evaluate the model's accuracy.</li>
          <li><b>Improve CCC (Cause and Effect):</b> Add a feature highlighting the specific chain of events from SO2 injection to aerosol formation to albedo change to temperature drop.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Overlay historical temperature anomaly data onto the simulation graphs.</li>
          <li>[ ] Create a step-by-step visual flowchart illustrating the cause-and-effect mechanism.</li>
        </ul>
      </li>
    </ul>
  </details>
- [Greenhouse Effect & Earth's Energy Budget Simulation](GreenhouseEffect.html) - An interactive simulation exploring how greenhouse gases affect Earth's energy budget and global temperature.

  <details>
    <summary><b>Evaluation: Anchoring Phenomenon | 5.0/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Excellent anchoring phenomenon. It perfectly models the energy budget and the differential absorption of radiation (Criterion 4). It is highly relevant to modern climate change discussions (Criterion 1).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Fully supports the DCI (ESS2.D) on weather and climate and the CCC (Energy and Matter). For HS-ESS2-4, it comprehensively demonstrates variations in energy flow resulting in climate changes (1.a, 2.a, 2.b).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance Model Complexity (SEP):</b> Add different types of greenhouse gases (e.g., CO2 vs. Methane) with different global warming potentials (absorption efficiencies) to allow for deeper investigation.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Separate the generic "Greenhouse Gases" slider into distinct "CO2" and "Methane" sliders.</li>
          <li>[ ] Adjust the simulation logic to account for the differing absorption characteristics of these specific gases.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ESS2-5
Plan and conduct an investigation of the properties of water and its effects on Earth materials and surface processes.

- [Water Properties & Earth Processes](WaterPropertiesEarthProcesses.html) - An interactive lab environment exploring frost wedging, chemical weathering, and stream transport.

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.0/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> A good multi-faceted investigative phenomenon. It bridges the microscopic properties of water with macroscopic geological processes (Criterion 4). It could be improved by focusing on local environments students might recognize (Criterion 1).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports the DCI (ESS2.C) on the roles of water in Earth's surface processes and the CCC (Structure and Function). For HS-ESS2-5, it allows planning and conducting investigations (1.a, 2.a).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Improve SEP (Planning Investigations):</b> Instead of pre-set experiments, provide a "Lab Bench" where students select a material (e.g., limestone vs. granite) and an environmental condition (e.g., freeze/thaw cycle vs. acidic rain) to design their own investigation.</li>
          <li><b>Enhance Relevance (Criterion 1):</b> Include examples of local phenomena caused by these processes, like potholes in roads (frost wedging) or sinkholes (chemical weathering).</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Refactor UI into a "Lab Bench" requiring students to pair a material with a weathering agent before running the simulation.</li>
          <li>[ ] Add narrative text or images of real-world results (potholes, caves) when specific weathering processes occur.</li>
        </ul>
      </li>
    </ul>
  </details>


- [Puerto Rican Karst Topography: Water & Bedrock Interactions](PuertoRicanKarstTopography.html) - An interactive simulation investigating how water chemically weathers limestone over thousands of years to create the unique karst landforms of Puerto Rico (sinkholes, mogotes, and aquifers).

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.5/5 Stars | 2026-03-12 18:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Excellent investigative phenomenon exploring how water's properties affect Earth's surface materials, specifically focusing on the unique Puerto Rican karst belt. Strongly meets Criterion 4 (Investigable) by allowing students to adjust rainfall, acidity, and fractures to observe the formation of sinkholes and aquifers.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports the DCI (ESS2.C) on the roles of water in Earth's surface processes and the CCC (Structure and Function). For HS-ESS2-5, it allows planning and conducting investigations (1.a, 2.a) to produce data on chemical weathering.
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><i>Minor Feature addition:</i> Add a layer of permeable topsoil to demonstrate how organic decay contributes to water acidity before it reaches the bedrock.</li>
          <li><i>UX Adjustment:</i> Enhance the visual distinction between dry caves and active groundwater aquifers.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist:</b>
        <ul>
          <li>[x] HTML5 Canvas for real-time cellular automata bedrock dissolution.</li>
          <li>[x] Sliders for environmental variables (Rainfall, pH, Fractures).</li>
          <li>[x] Chart.js data tracking of dissolved limestone and aquifer volume.</li>
        </ul>
      </li>
    </ul>
  </details>

- [Frost Heaves and Connecticut Stone Walls](FrostHeavesAndConnecticutStoneWalls.html) - Simulate the physics of ice expansion and frost heaving that pushes rocks to the surface, explaining the abundance of stone walls in New England.


### HS-ESS2-6
Develop a quantitative model to describe the cycling of carbon among the hydrosphere, atmosphere, geosphere, and biosphere.

- [Global Carbon Cycle Model](GlobalCarbonCycleModel.html) - A quantitative box-model simulation demonstrating the conservation of mass and the flows of carbon between Earth's major reservoirs, highlighting human impacts.

  <details>
    <summary><b>Evaluation: Anchoring Phenomenon | 4.5/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Extremely relevant anchoring phenomenon for understanding climate change and human impact (Criterion 1). The box-model clearly visualizes the flow of carbon (Criterion 4), but mathematical relationships might need to be explicitly calculated.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Directly supports the DCI (ESS2.D) on carbon cycling and the CCC (Energy and Matter). For HS-ESS2-6, it allows for quantitative modeling of the carbon cycle (1.a, 2.a).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Improve SEP (Quantitative Modeling):</b> Make the fluxes (arrows between reservoirs) numerically adjustable and show real-time calculated changes to the total mass in each reservoir, rather than just preset animations.</li>
          <li><b>Enhance Relevance (Criterion 1):</b> Include specific historical data sets (e.g., pre-industrial vs. modern carbon levels) as preset scenarios students can load.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Implement numerical input fields for carbon fluxes (e.g., fossil fuel emissions, photosynthesis rate).</li>
          <li>[ ] Add "Pre-Industrial" and "Current Day" preset buttons to load historical data parameters.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ESS2-7
Construct an argument based on evidence about the simultaneous coevolution of Earth’s systems and life on Earth.

- [The Great Oxidation Event](GreatOxidationEvent.html) - An interactive timeline model simulating how early photosynthetic life altered Earth's atmosphere, exhausted ocean chemical sinks, and paved the way for complex aerobic life.

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.0/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Great investigative phenomenon connecting Earth systems to biological evolution (Criterion 4). It is visually engaging and demonstrates coevolution well. It lacks a direct modern analog for students to relate to (Criterion 1).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports the DCI (ESS2.E) on the coevolution of Earth's systems and life, and the CCC (Stability and Change). For HS-ESS2-7, it aids in constructing an argument based on evidence (1.a, 2.a).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance SEP (Constructing Arguments):</b> After running the simulation, prompt students with a specific claim (e.g., "Life caused the Great Oxidation Event, not geological changes") and ask them to select evidence from the timeline to support or refute it.</li>
          <li><b>Improve Model Complexity:</b> Explicitly show the exhaustion of ocean chemical sinks (like Iron precipitating out as Banded Iron Formations) before atmospheric oxygen begins to rise.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Add an interactive "Argument Builder" section at the end of the timeline.</li>
          <li>[ ] Update the simulation logic and visuals to clearly depict the formation of Banded Iron Formations prior to atmospheric oxygenation.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ESS3-1
Construct an explanation based on evidence for how the availability of natural resources, occurrence of natural hazards, and changes in climate have influenced human activity.

- [Human Settlement & Migration Simulator](HumanMigrationSettlementSimulator.html) - An interactive map demonstrating how human populations migrate towards natural resources and are displaced by natural hazards and climate change. Features specific historical case studies (Nile River Valley, The Dust Bowl), a modern Climate Refugee scenario, and a dynamic population data logger for quantitative analysis.

  <details>
    <summary><b>Evaluation: Anchoring Phenomenon | 5.0/5 Stars | 2026-03-13 13:49:23</b></summary>
    <ul>
      <li>
        <b>Overview:</b> An exceptional anchoring phenomenon for modeling human geography and environmental impact. It deeply integrates real-world scenarios (Dust Bowl, Climate Refugees) with interactive, quantifiable data (Population Data Logger) (Criteria 1 & 4). It clearly demonstrates the push and pull factors of settlement.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Exceeds requirements for the DCI (ESS3.A: Natural Resources, ESS3.B: Natural Hazards) and CCC (Cause and Effect). For HS-ESS3-1, it profoundly enhances the SEP (Constructing Explanations) by providing students with explicit graphical data (population vs. time with hazard markers) to support their evidence-based arguments (1.a, 2.a, 2.b).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance SEP (Analyzing Data):</b> Provide an interactive export feature allowing students to download the charted population data as a CSV file to perform external statistical analysis or combine with real-world datasets.</li>
          <li><b>Deepen DCI (Human Impacts):</b> Introduce a "Technology/Adaptation" mechanic, such as building dams to mitigate floods or irrigation to reduce drought impact, allowing students to test solutions against natural hazards.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Add a "Download CSV" button to export the chart data.</li>
          <li>[ ] Implement interactive "Adaptation" toggles (e.g., Dams, Irrigation) that modify hazard impact variables.</li>
        </ul>
      </li>
    </ul>
  </details>

- [Portland Brownstone Quarry Simulator](PortlandBrownstoneQuarry.html) - A resource management simulator focusing on the historical Portland, CT brownstone quarries, demonstrating how natural resources, economics, and natural hazards (flooding) influence human settlement and industry.

### HS-ESS3-2
Evaluate competing design solutions for developing, managing, and utilizing energy and mineral resources based on cost-benefit ratios.*

- [Energy & Mineral Resources Cost-Benefit Analysis](EnergyResourcesCostBenefit.html) - Evaluate competing design solutions for developing, managing, and utilizing energy and mineral resources based on cost-benefit ratios. [2026-03-14 04:45:29]

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.0/5 Stars | 2026-03-14 04:45:29</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Strong investigative phenomenon for evaluating resource management strategies. Meets Criterion 4 (Investigable) by challenging students to balance cost, energy output, and environmental impact.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Supports DCI (ESS3.A) regarding natural resources and DCI (ETS1.B) on developing possible solutions. Supports SEP (Engaging in Argument from Evidence).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance SEP (Evaluating Solutions):</b> Require students to explicitly define their prioritized criteria (e.g., "low cost" vs "low emissions") before beginning the analysis, and evaluate their final solution against those specific criteria.</li>
          <li><b>Improve Data Visualization:</b> Use a radar chart to visually compare the trade-offs (Cost, Energy, Environment, Social) of different resource portfolios.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Add a pre-simulation step to define prioritized criteria.</li>
          <li>[ ] Implement a radar chart for multi-variable trade-off visualization.</li>
        </ul>
      </li>
    </ul>
  </details>



### HS-ESS3-3
Create a computational simulation to illustrate the relationships among management of natural resources, the sustainability of human populations, and biodiversity.

- [Sustainable Resource Management Simulator](ResourceManagementSimulator.html) - A computational simulation where users must balance human population growth against biodiversity loss and resource depletion.

  <details>
    <summary><b>Evaluation: Anchoring Phenomenon | 4.5/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Very strong anchoring phenomenon. It is highly relevant to students' lives (sustainability, energy policy) (Criterion 1) and provides a complex system to investigate (Criterion 4).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Directly supports the DCI (ESS3.A, ESS3.C) on natural resources and human impacts, and the CCC (Stability and Change). For HS-ESS3-3, it successfully serves as a computational simulation to illustrate relationships (1.a, 2.a).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Improve Computational Model (SEP):</b> Ensure the underlying mathematical model explicitly calculates a "Sustainability Index" that incorporates resource depletion rates, population growth, and biodiversity metrics, displaying this formula transparently to the user.</li>
          <li><b>Enhance Relevance (Criterion 1):</b> Allow students to choose different starting biomes (e.g., arid desert vs. temperate forest), as resource management strategies differ drastically based on local context.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Implement and explicitly display a "Sustainability Index" formula and real-time score.</li>
          <li>[ ] Add a "Select Biome" starting screen that alters base resources and population growth rates.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ESS3-4
Evaluate or refine a technological solution that reduces impacts of human activities on natural systems.*

- [Urban Watershed Mitigation Design](TechnologicalSolutionEvaluation.html) - Evaluate and refine technological solutions to reduce agricultural and urban runoff impacts on a local watershed. [2026-03-13 21:16:17]

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.5/5 Stars | 2026-03-13 21:16:17</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Excellent investigative phenomenon for testing technological solutions to human impacts. Meets Criterion 1 (Relevance) through local water quality issues and Criterion 4 (Investigable) by allowing iterative design of mitigation strategies (e.g., green roofs, retention ponds).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports DCI (ESS3.C) regarding human impacts on Earth systems and DCI (ETS1.B). Supports SEP (Designing Solutions).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Fulfill Observable Feature 3.a (Refining Solutions):</b> Implement a strict "budget" system where mitigation strategies cost money, forcing students to optimize their design to achieve target water quality without overspending.</li>
          <li><b>Improve Feedback Loop:</b> Provide detailed feedback on exactly *why* a specific pollutant (e.g., nitrates vs heavy metals) wasn't mitigated by the chosen strategy.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Implement a budget system for deploying mitigation strategies.</li>
          <li>[ ] Add specific feedback regarding pollutant-specific mitigation failures.</li>
        </ul>
      </li>
    </ul>
  </details>



### HS-ESS3-5
Analyze geoscience data and the results from global climate models to make an evidence-based forecast of the current rate of global or regional climate change and associated future impacts to Earth systems.

- [Global Climate Impacts & Mitigation Forecast](GlobalClimateImpacts.html) - A computational dashboard forecasting the future rate of climate change and its specific impacts on glacial ice and ocean pH.

  <details>
    <summary><b>Evaluation: Anchoring Phenomenon | 5.0/5 Stars | 2026-03-12 12:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Excellent anchoring phenomenon. It allows for direct forecasting and data analysis on the most pressing global issue (Criterion 1). It integrates multiple Earth systems effectively (Criterion 4).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Fully supports the DCI (ESS3.D) on global climate change and the CCC (Stability and Change). For HS-ESS3-5, it allows students to analyze data and make evidence-based forecasts (1.a, 2.a).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance SEP (Analyzing Data):</b> Incorporate real-world historical data sets (e.g., Keeling Curve for CO2, or actual global temperature anomalies from NOAA) as a baseline comparison against the simulation's future projections.</li>
          <li><b>Improve Interactivity:</b> Allow students to plot their own projected trendlines before running the simulation to see how well their hypothesis matches the computational forecast.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Integrate historical baseline data (NOAA/Keeling Curve) into the forecasting graphs.</li>
          <li>[ ] Implement a "Draw Prediction" tool allowing users to sketch a trendline on the graph prior to running the forecast model.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ESS3-6
Use a computational representation to illustrate the relationships among Earth systems and how those relationships are being modified due to human activity.

- [Earth Systems Interactions Simulator](EarthSystemsInteractions.html) - Explore how human activities like fossil fuel emissions and deforestation impact Earth's interacting systems over time. [2026-03-14 04:45:29]

  <details>
    <summary><b>Evaluation: Anchor Phenomenon | 5.0/5 Stars | 2026-03-14 04:45:29</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Outstanding anchoring phenomenon modeling complex interconnected systems. Strongly meets Criterion 4 (Investigable) by allowing manipulation of human activities and observing rippling effects across the atmosphere, biosphere, hydrosphere, and geosphere.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Comprehensively supports DCI (ESS2.A, ESS3.C) and CCC (Systems and System Models, Stability and Change). Thoroughly supports SEP (Using Mathematics and Computational Thinking).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance CCC (Systems Thinking):</b> Visually map the feedback loops (e.g., ice-albedo feedback) directly on the interface when they are triggered by human activity inputs.</li>
          <li><b>Improve Data Export:</b> Allow students to export the multi-system variable data over time for independent graphing and analysis.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Implement visual indicators/lines for active feedback loops between systems.</li>
          <li>[ ] Add a "Download CSV" feature for the simulated systems data.</li>
        </ul>
      </li>
    </ul>
  </details>

- [Long Island Sound Hypoxia Simulation](LongIslandSoundHypoxia.html) - An interactive simulation exploring how human-caused nutrient runoff, combined with seasonal temperature changes, creates dead zones (hypoxia) in coastal ecosystems and impacts marine life.

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.5/5 Stars | 2026-03-15 10:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Excellent investigative phenomenon for a specific, relatable New England environmental issue. Meets Criterion 1 (Relevance) through local impact and Criterion 4 (Investigable) by allowing manipulation of interacting factors (runoff, temperature, wind).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports DCI (ESS3.C) on human impacts on Earth systems and DCI (LS2.C) on ecosystem dynamics. Supports SEP (Using Mathematics and Computational Thinking) by modeling variable interactions.
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Enhance Data Export:</b> Add a feature to download the logged chart data as a CSV for independent student analysis.</li>
          <li><b>Improve Interactivity:</b> Allow users to specify the type of "Mystery Factor" (e.g., Hurricane, Cold Front) rather than a generic slider.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Add CSV download button for the historical oxygen/algae data.</li>
          <li>[ ] Replace "Mystery Factor" slider with specific weather event buttons.</li>
        </ul>
      </li>
    </ul>
  </details>
