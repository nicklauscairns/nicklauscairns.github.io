# NGSS High School Physical Sciences Standards Aligned Content

## Simulations

### HS-PS1-1
Use the periodic table as a model to predict the relative properties of elements based on the patterns of electrons in the outermost energy level of atoms.

- [Alkali Metals Phenomenon](AlkaliMetalsPhenomenon.html) - Observe the reaction patterns and atomic structures of different elements.
  <details>
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
          <li><b>Improve SEP (Developing Models):</b> Instead of static buttons for 'Drop Li' or 'Drop Na', add a <code>&lt;input type='range'&gt;</code> slider or <code>+</code>/<code>-</code> buttons to let students construct the atom dynamically by adding protons and electrons. Bind this to <code>elementData</code> so the simulation calculates reactivity based on the user-built valence shell.</li>
          <li><b>Fulfill Observable Feature 3.b.ii (Stable Ions):</b> Add a UI button labeled "Form Ion". When clicked, trigger an animation to remove the valence electron(s) from <code>aCanvas</code> and update the UI to display the resulting stable ion charge (e.g., <code>Na+</code>).</li>
          <li><b>Improve Phenomenon Relevance (Criterion 1):</b> Update the <code>elementDesc</code> strings for the 'Mystery Metal (X)' to explicitly frame it as a 'Lithium-Ion Battery Fire hazard'. This anchors the chemical principles in a relevant real-world context for high school students.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Refactor the UI controls to allow dynamic atom building (protons/electrons) instead of static preset metal buttons.</li>
          <li>[ ] Bind the dynamic atom state to the reaction engine to calculate <code>reactDuration</code> and <code>speed</code> based on valence electrons.</li>
          <li>[ ] Implement an "Ionize" function and animation in the <code>aCanvas</code> to visualize the loss of valence electrons and display the net charge.</li>
          <li>[ ] Rewrite the "Mystery Metal" narrative text to describe a thermal runaway event in a modern battery to increase cultural/personal relevance.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-PS1-2
Construct and revise an explanation for the outcome of a simple chemical reaction based on the outermost electron states of atoms, trends in the periodic table, and knowledge of the patterns of chemical properties.

- [Chemical Reaction Outcomes Predictor](ChemicalReactionsOutcomes.html) - An interactive sandbox to predict outcomes and explore the octet rule by combining atoms with varying valence electrons.

### HS-PS1-3
Plan and conduct an investigation to gather evidence to compare the structure of substances at the bulk scale to infer the strength of electrical forces between particles.

- [Intermolecular Forces Investigation](IntermolecularForces.html) - Observe boiling points and surface tension to infer the strength of London Dispersion, Dipole-Dipole, and Hydrogen Bonding forces.

### HS-PS1-4
Develop a model to illustrate that the release or absorption of energy from a chemical reaction system depends upon the changes in total bond energy.

- [Bond Energy Changes Simulator](BondEnergy.html) - An animated model illustrating how breaking bonds absorbs energy and forming bonds releases energy, and how the net change determines if a reaction is endothermic or exothermic.

### HS-PS1-5
Apply scientific principles and evidence to provide an explanation about the effects of changing the temperature or concentration of the reacting particles on the rate at which a reaction occurs.

- [Reaction Rates Simulation](ReactionRatesSimulation.html) - Explore how changing temperature (kinetic energy) and concentration affects collision frequency, reaction rates, and activation energy barriers using an interactive particle model.

### HS-PS1-6
Refine the design of a chemical system by specifying a change in conditions that would produce increased amounts of products at equilibrium.

- [Le Chatelier's Principle Simulator](LeChatelier.html) - Interactively stress an equilibrium system (Haber Process) by changing concentration, volume, and temperature to see how the system shifts.

### HS-PS1-7
Use mathematical representations to support the claim that atoms, and therefore mass, are conserved during a chemical reaction.

- [Conservation of Mass Simulator](ConservationOfMass.html) - Balance chemical equations and observe how total mass and atom counts remain perfectly conserved across the reaction.

### HS-PS1-8
Develop models to illustrate the changes in the composition of the nucleus of the atom and the energy released during the processes of fission, fusion, and radioactive decay.

- [Nuclear Processes Simulator](NuclearProcesses.html) - Visualize the changes in protons and neutrons, and the massive energy released, during Alpha Decay, Nuclear Fission, and Nuclear Fusion.

### HS-PS2-1
Analyze data to support the claim that Newton's second law of motion describes the mathematical relationship among the net force on a macroscopic object, its mass, and its acceleration.

- [Interactive Boat River Crossing Simulation](InteractiveBoatRiverCrossingSimulation.html) - A physics simulation exploring relative velocity and vector addition as a boat crosses a flowing river.
- [Projectile Motion Simulation](ProjectileMotionSimulation.html) - An interactive physics simulation to study the kinematics of projectile motion by adjusting launch variables.

### HS-PS2-2
Use mathematical representations to support the claim that the total momentum of a system of objects is conserved when there is no net force on the system.

- [Conservation of Momentum Simulation](ConservationOfMomentumSimulation.html) - Explore 1D elastic and inelastic collisions. Adjust masses, velocities, and elasticity to observe the conservation of momentum and changes in kinetic energy.

### HS-PS2-3
Apply scientific and engineering ideas to design, evaluate, and refine a device that minimizes the force on a macroscopic object during a collision.

- [Collision Force Minimizer](EggDropCrashCushion.html) - An interactive physics sandbox where users engineer the thickness and material stiffness of a crash cushion to minimize impact forces and protect a fragile payload during a drop.

### HS-PS2-4
Use mathematical representations of Newton's Law of Gravitation and Coulomb's Law to describe and predict the gravitational and electrostatic forces between objects.

- [Gravity and Electrostatics Simulator](GravityAndElectrostaticsSimulator.html) - An interactive simulation to compare gravitational and electrostatic forces, manipulate mass/charge/distance, and explore the inverse-square law through data logging and graphing.

### HS-PS2-5
Plan and conduct an investigation to provide evidence that an electric current can produce a magnetic field and that a changing magnetic field can produce an electric current.

- [Electromagnetism & Induction Sandbox](ElectromagnetismInduction.html) - Plan investigations using interactive electromagnets to see how current produces magnetic fields, and use a moving magnet near a coil to see how changing magnetic flux induces a current.

### HS-PS2-6
Communicate scientific and technical information about why the molecular-level structure is important in the functioning of designed materials.

- [Molecular Structures & Designed Materials](MolecularStructuresMaterials.html) - Explore how the molecular-level structure of metals (conductivity), polymers (flexibility), and pharmaceuticals (specificity) determines their macro-scale functioning.

### HS-PS3-1
Create a computational model to calculate the change in the energy of one component in a system when the change in energy of the other component(s) and energy flows in and out of the system are known.

- [Energy Change Computational Model](EnergyChangeModel.html) - An interactive mathematical and computational model for a 3-component system, balancing kinetic, potential, and thermal energy changes with total energy flow.

### HS-PS3-2
Develop and use models to illustrate that energy at the macroscopic scale can be accounted for as a combination of energy associated with the motions of particles (objects) and energy associated with the relative position of particles (objects).

- [Macroscopic vs. Microscopic Energy Model](MacroscopicEnergyModel.html) - An interactive dual-view model illustrating how macroscopic temperature and elastic potential energy are derived from microscopic particle motion and relative particle positions.

### HS-PS3-3
Design, build, and refine a device that works within given constraints to convert one form of energy into another form of energy.

- [Stage Lighting Simulator](StageLightingSimulator.html) - Investigate the energy transfer and circuit topography of two stage lighting tracks.

### HS-PS3-4
Plan and conduct an investigation to provide evidence that the transfer of thermal energy when two components of different temperature are combined within a closed system results in a more uniform energy distribution among the components in the system (second law of thermodynamics).

- [Thermal Equilibrium Sandbox](ThermalEquilibriumSandbox.html) - An interactive closed-system sandbox to investigate how components of different materials, masses, and initial temperatures transfer heat until reaching a uniform energy distribution (thermal equilibrium).

### HS-PS3-5
Develop and use a model of two objects interacting through electric or magnetic fields to illustrate the forces between objects and the changes in energy of the objects due to the interaction.

- [Electric & Magnetic Field Energy Simulator](ElectricMagneticFieldEnergy.html) - Interactively drag charged or magnetic objects to observe how distance impacts force magnitude and stored field potential energy.

### HS-PS4-1
Use mathematical representations to support a claim regarding relationships among the frequency, wavelength, and speed of waves traveling in various media.

- [From Sparks to Waves](FromSparksToWavesSimulation.html) - An interactive lightning and wave oscilloscope simulation exploring propagation and oscilloscope models.

### HS-PS4-2
Evaluate questions about the advantages of using a digital transmission and storage of information.

- [Digital vs. Analog Transmission Advantages](DigitalTransmissionAdvantage.html) - An interactive simulation demonstrating how digital thresholding allows a noisy signal to be perfectly reconstructed, while analog continuous signals permanently degrade.

### HS-PS4-3
Evaluate the claims, evidence, and reasoning behind the idea that electromagnetic radiation can be described either by a wave model or a particle model, and that for some situations one model is more useful than the other.

- [Wave-Particle Duality](WaveParticleDuality.html) - Evaluate two interactive models: the double-slit experiment (wave interference) and the photoelectric effect (particle threshold energy).

### HS-PS4-4
Evaluate the validity and reliability of claims in published materials of the effects that different frequencies of electromagnetic radiation have when absorbed by matter.

- [EM Radiation Effects on Matter](EMRadiationEffects.html) - Evaluate the claims that low-frequency radiation causes safe thermal heating, while high-frequency radiation acts as ionizing radiation that damages cellular DNA.

### HS-PS4-5
Communicate technical information about how some technological devices use the principles of wave behavior and wave interactions with matter to transmit and capture information and energy.

- [Wave Technology: Information & Energy](WaveInformationTechnology.html) - An interactive exploration of how Solar Cells capture energy from light waves, and how Fiber Optics use total internal reflection to transmit digital data.
