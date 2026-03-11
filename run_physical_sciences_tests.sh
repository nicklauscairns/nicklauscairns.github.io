#!/bin/bash
tests=(
    "test_physics.py"
    "test_projectile_motion.py"
    "test_boat_simulation.py"
    "test_egg_drop.py"
    "test_field_energy.py"
    "test_electromagnetism.py"
    "test_macroscopic_energy.py"
    "test_energy_change.py"
    "test_thermal_equilibrium.py"
    "test_imf.py"
    "test_bond_energy.py"
    "test_reaction_rates.py"
    "test_le_chatelier.py"
    "test_conservation_of_mass.py"
    "test_nuclear_processes.py"
    "test_molecular_structures.py"
    "test_chemical_reactions.py"
    "test_digital_transmission.py"
    "test_wave_particle.py"
    "test_em_radiation.py"
    "test_wave_technology.py"
    "test_alkali_metals.py"
    "test_stage_lighting.py"
    "test_from_sparks_to_waves.py"
    "test_gravity_electrostatics.py"
)

for t in "${tests[@]}"; do
    if [ -f "tests/$t" ]; then
        echo "Running $t..."
        python "tests/$t"
    else
        echo "Warning: tests/$t not found."
    fi
done
