# NGSS High School Engineering, Technology, and Applications of Science Standards Aligned Content

## Simulations

### HS-ETS1-1
Analyze a major global challenge to specify qualitative and quantitative criteria and constraints for solutions that account for societal needs and wants.

- [City Water Infrastructure Simulation](CityWaterInfrastructureSimulation.html) - An interactive simulation challenging students to act as city planners facing a growing population and water crisis. Define constraints (budget, environmental impact) and criteria (target capacity), and then manage infrastructure projects to balance societal needs over time. [2026-03-12 12:00:00]

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4/5 Stars | 2026-03-12 18:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> This is an engaging investigative phenomenon that places students in the role of a city planner. It challenges assumptions by demonstrating that solutions (like building desalination plants) are not perfectly "good" or "bad", but involve trade-offs between budget, capacity, and environmental impact (Criterion 4: Investigable Through Practices). It has strong Cultural and Personal Relevance (Criterion 1) as water scarcity is a pressing global issue.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> The simulation strongly supports the DCI (ETS1.A) and CCC (Influence of Science, Engineering, and Technology on Society) by illustrating the costs and benefits of new technologies like desalination or recycling plants. For the SEP (Asking Questions and Defining Problems), it demonstrates Observable Features 1.a.ii (describing extent of the problem), 2.b (describing societal needs and wants), and 3.a (specifying qualitative and quantitative criteria and constraints). It allows students to set explicit numeric constraints (budget, minimum capacity, environmental impact) and then run projects to see if they can meet those goals. However, it fails to support 1.a.iii (documenting background research from journals).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Improve SEP (Defining Problems):</b> While users can define the constraints with sliders, they aren't explicitly required to justify *why* those constraints are chosen based on the "global challenge." Add a text area in the constraint-setting modal asking students to "Provide a brief rationale for your chosen constraints based on the provided global water crisis data."</li>
          <li><b>Fulfill Observable Feature 1.a.iii (Documenting Research):</b> Add an "information hub" or a "Research Desk" button in the UI that pops up a modal with 2-3 links or summarized excerpts from real-world scientific journals or reports (e.g., IPCC reports on water scarcity, UN Water data). Require the user to click and "review" these before unlocking the ability to set constraints.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Add a "Research Data" modal with summaries/links to real-world water scarcity reports.</li>
          <li>[ ] Add logic to disable the "Approve Constraints" button until the user has opened the Research Data modal.</li>
          <li>[ ] Add a text `&lt;textarea&gt;` in the "Define City Constraints" section for students to write a short rationale for their numbers.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ETS1-2
Design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems that can be solved through engineering.

- [Electric Vehicle Design and Optimization](ElectricVehicleSimulation.html) - An interactive simulation allowing users to optimize EV parameters (battery capacity, aerodynamics, mass, speed) to maximize range and efficiency. Aligns with NGSS HS-ETS1 Engineering Design standards. Contains data logging and export for student inquiry and analysis. [2026-03-12 12:00:00]

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.5/5 Stars | 2026-03-12 18:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> This is an outstanding investigative phenomenon that models electric vehicle efficiency. It is deeply connected to current efforts to transition from fossil fuels (Criterion 1: Cultural and Personal Relevance). It requires students to balance conflicting design variables (e.g., adding battery capacity increases weight, which reduces efficiency) to achieve optimal range (Criterion 4: Investigable Through Practices).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> The simulation strongly supports the DCI (ETS1.C: Optimizing the Design Solution) by forcing users to prioritize criteria and manage tradeoffs. For the SEP (Constructing Explanations and Designing Solutions), it clearly demonstrates Observable Features 1.a (restating a complex problem into sub-problems: aerodynamics vs mass vs battery), 1.b (proposing solutions based on generated data), and 2.a (describing criteria for the sub-problem). It effectively utilizes data logging to build evidence. It lacks feature 2.b, which requires describing the rationale for the sequence of how sub-problems are solved and which criteria are prioritized.
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Improve SEP (Generating the design solution):</b> The simulation allows data generation, but does not ask students to organize their optimization process systematically. Add a "Design Strategy" text input where students declare if they are prioritizing "Aerodynamics", "Lightweighting", or "Battery Capacity" first, and why.</li>
          <li><b>Fulfill Observable Feature 2.b (Describing priorities/tradeoffs):</b> Introduce a final "Export Report" button that summarizes the test history and prompts the student to write a conclusion justifying their final design tradeoff (e.g., "I sacrificed top speed to maximize range by increasing drag coefficient...").</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Add a "Design Priority" dropdown (Aerodynamics, Mass, Battery, Speed) above the sliders for students to explicitly state their primary focus.</li>
          <li>[ ] Add a final "Submit Design Rationale" text area to explain their final parameter choices and trade-offs.</li>
          <li>[ ] Include the rationale text in the exported CSV or generated report.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ETS1-3
Evaluate a solution to a complex real-world problem based on prioritized criteria and trade-offs that account for a range of constraints, including cost, safety, reliability, and aesthetics as well as possible social, cultural, and environmental impacts.

- [Wind Turbine Optimization Simulation](WindTurbineSimulation.html) - An engineering simulation challenging users to optimize wind turbine parameters to maximize energy output. [2026-03-12 12:00:00]

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4/5 Stars | 2026-03-12 18:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> This simulation serves as an excellent investigative phenomenon where students optimize a wind turbine. It explicitly addresses the challenge of clean energy and requires students to make trade-offs between cost, efficiency, and structural integrity based on different design parameters (Criterion 4). It has relevance as renewable energy is an important global goal (Criterion 1).
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> The simulation robustly supports the DCI (ETS1.B: Developing Possible Solutions) by allowing users to explore a range of constraints (e.g., cost, reliability). For the SEP (Constructing Explanations and Designing Solutions), it demonstrates Observable Features 1.a.i (generating criteria like cost vs. energy output), 1.a.ii (assigning priorities to criteria like blade length vs. cost), and 1.a.iii (analyzing strengths and weaknesses of different blade designs). However, it lacks features 1.a.iv (describing possible barriers to implementation, such as social/cultural) and 1.a.v (providing an evidence-based decision).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Improve SEP (Evaluating Solutions):</b> The simulation currently focuses purely on technical/cost tradeoffs. It needs to include social and environmental impacts (e.g., noise pollution, bird strikes) to fully satisfy HS-ETS1-3. Add an "Environmental & Social Impact" metric to the dashboard that calculates a score based on blade length and turbine speed.</li>
          <li><b>Fulfill Observable Feature 1.a.iv (Implementation Barriers):</b> Add a feature where certain locations (e.g., "Near residential zone", "Offshore") present different constraints (like maximum noise limits) or barriers to entry. The student must select a location and design a turbine that passes those specific environmental barriers.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Add an "Environmental & Social Impact" gauge or bar chart that increases as blade length and speed increase (representing noise and wildlife risk).</li>
          <li>[ ] Introduce a "Deploy Location" dropdown with preset noise/aesthetic constraints (e.g., Urban, Rural, Offshore).</li>
          <li>[ ] Add logic to check if the designed turbine meets the "Deploy Location" constraints and show a success/failure message regarding community acceptance.</li>
        </ul>
      </li>
    </ul>
  </details>

### HS-ETS1-4
Use a computer simulation to model the impact of proposed solutions to a complex real-world problem with numerous criteria and constraints on interactions within and between systems relevant to the problem.

- [Spacecraft Reentry Optimization Simulation](SpacecraftReentrySimulation.html) - An interactive simulation challenging users to design a reentry vehicle by balancing mass, shield diameter, angle, and material to survive atmospheric entry. [2026-03-12 12:00:00]

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 3.5/5 Stars | 2026-03-12 18:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> This serves as a captivating investigative phenomenon, simulating spacecraft reentry. It effectively tests students’ understanding of thermal dynamics, mass, and velocity during a critical mission phase (Criterion 4: Investigable Through Practices). While scientifically robust and flashy, it lacks everyday Cultural and Personal Relevance (Criterion 1) as aerospace engineering is highly specialized, but the physics (friction, heat) are universal.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> The simulation robustly supports the DCI (ETS1.B: Developing Possible Solutions) by utilizing a computer model to simulate a physical system. For the SEP (Using Mathematics and Computational Thinking), it demonstrates Observable Features 1.a.ii (identifying the system modeled), 1.a.iii (identifying variables that can be changed: mass, angle, diameter), 2.a.i (selecting inputs), and 2.a.ii (using the model to simulate effects). However, it does not explicitly prompt students to interpret results against *expected* results (3.a) or identify the simulation's limitations (3.d).
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><b>Improve SEP (Computational Modeling Analysis):</b> To address 3.a (comparing to expected results), provide a target "Mission Profile" before launch, such as a max safe temperature and max deceleration force. Students must write down their predictions and compare them to the actual flight data chart.</li>
          <li><b>Fulfill Observable Feature 3.d (Simulation Limitations):</b> Add an "Assumptions & Limitations" info panel or tooltip. Require students to acknowledge (e.g., via a checkbox before launch) that this model assumes a uniform atmosphere, ignores ablation physics, and uses a simplified ballistic trajectory.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist for AI Agent:</b>
        <ul>
          <li>[ ] Add a "Mission Briefing" UI card outlining target safety limits (Max G-force: 15G, Max Temp: 2000K).</li>
          <li>[ ] Add an "Assumptions & Limitations" info modal listing the physical simplifications used in the mathematical model.</li>
          <li>[ ] Add a prompt after the simulation runs for students to select if their design "Met", "Exceeded", or "Failed" the mission criteria compared to expected results.</li>
        </ul>
      </li>
    </ul>
  </details>
