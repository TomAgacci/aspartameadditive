#!/usr/bin/env python3
"""
Aspartame Sweetness Modulator — Mineral-Salt Additive
Kitchen-style R&D conceptual guide (non-procedural).
"""

def print_section(title, body):
    print("=" * 80)
    print(title.upper())
    print("=" * 80)
    print(body)
    print("\n")


def main():
    rd_goal = """
Objective:
Design a salt-based additive that, when added to aspartame, makes its sweetness profile:

- Less lingering
- More “sugar-like” in mouthfeel
- Without obvious salty, metallic, or bitter off-notes

Positioning:
- Not a sweetener by itself
- A modular taste-shaping component for diet beverages and low-calorie products
"""

    scientific_backbone = """
Core idea:
Use mineral ions as entourage molecules around aspartame to:

- Change how it diffuses through tongue mucus
- Modulate receptor activation (sweet + calcium-sensing)
- Alter onset, peak, and linger of perceived sweetness

Key constraint:
- NaCl alone is not enough—a realistic system uses K/Mg/Ca salts at low, controlled levels.
- NaCl may be present, but not as the sole active.
"""

    kitchen_env = """
Human-scale “kitchen-style” R&D environment:
Think of this as a lab that feels like a kitchen, but still operates under scientific rules.

Core modules:

Module A – Water & base handling
- Kitchen analogue: kettles, carafes, filters
- R&D role: prepare purified water and base solutions with controlled pH and low background minerals.

Module B – Mineral stock preparation
- Kitchen analogue: measuring cups, small mixing bowls, stirrers
- R&D role: prepare stock solutions of food-grade K/Mg/Ca salts at known concentrations
  (measured with lab tools, not spoons).

Module C – Mixing & conditioning
- Kitchen analogue: stand mixer, immersion blender, temperature-controlled bath
- R&D role: combine mineral stocks with aspartame solutions, condition them at controlled
  temperatures, and let them equilibrate.

Module D – Sensory testing station
- Kitchen analogue: tasting counter, cups, spoons
- R&D role: human tasters compare:
  * HFCS/sucrose reference cola
  * Plain aspartame cola
  * Aspartame + mineral additive prototypes
  Record onset, peak sweetness, linger, and mouthfeel.

Module E – Iteration & logging
- Kitchen analogue: recipe notebook, whiteboard
- R&D role: track:
  * Mineral ratios
  * Perceived effects
  * Off-notes
  * Promising prototypes
"""

    human_flow = """
Human process flow (no recipes, just roles):

Step 1 – Define targets
- Choose a reference drink (e.g., HFCS cola).
- Define desired sweetness curve and mouthfeel in words and simple scales.

Step 2 – Build prototypes
- Prepare multiple aspartame-based test drinks.
- Add different mineral profiles (vary K/Mg/Ca within safe, food-grade ranges).

Step 3 – Run sensory panels
- Have humans taste in blind, randomized order.
- Score:
  * Sweetness intensity
  * Onset speed
  * Linger duration
  * Mouthfeel (thin vs syrupy)
  * Off-notes (salty, metallic, bitter)

Step 4 – Narrow and refine
- Identify 2–3 mineral profiles that:
  * Reduce linger
  * Improve mouthfeel
  * Avoid off-notes
- Iterate around those profiles.

Step 5 – Pre-industrial handoff
- Once a profile looks promising, hand off:
  * Target mineral ratios
  * Sensory data
  * Use-case (cola, flavored water, etc.)
- To a food-science lab or manufacturer for:
  * Safety/toxicology
  * Regulatory review
  * Industrial process design
"""

    kitchen_scale = """
Where “kitchen supplies” fit in the bigger scale:

In a larger factory built from “kitchen-style” units, the human process scales like this:

- Multiple Module A/B/C stations:
  * Each behaves like a “smart kitchen” node preparing base and mineral mixes.

- Central sensory & QA hub:
  * Humans still taste and validate prototypes and production samples.

- Industrial backbone behind the scenes:
  * Even if the front-end feels like a kitchen, the back-end must handle:
    - Precise dosing
    - Purity checks
    - Batch tracking
    - Compliance
"""

    rd_brief = """
R&D BRIEF — Salt-Based Additive for Aspartame Sweetness Modulation
(Concept: “Kitchen-Style Microfactory” Human-Process R&D)

1. Project Title
Aspartame Sweetness Modulator — Mineral-Salt Additive (Kitchen-Style R&D Framework)

2. Project Objective
Develop a safe, food-grade mineral-salt additive that, when added to aspartame-sweetened beverages,
produces a sweetness profile closer to sucrose/HFCS, specifically:

- Reduced lingering sweetness
- Faster onset
- More “syrupy” mouthfeel
- Fewer metallic or diet-like off-notes

The additive is not a sweetener; it is a taste-modulating component.

3. Scientific Rationale
Aspartame’s sweetness profile differs from sucrose due to:

- Slower diffusion through tongue mucus
- Longer receptor activation
- Lack of sucrose-like mouthfeel

Research suggests specific mineral ions (K+, Mg2+, Ca2+) can:

- Compress the mucus hydrogel
- Activate the calcium-sensing receptor
- Shorten sweetness linger
- Improve mouthfeel

NaCl alone cannot achieve this effect, but may be included at trace levels.

4. Additive Concept (High-Level)
A multi-mineral salt system composed of:

- Potassium chloride (KCl)
- Magnesium chloride (MgCl2)
- Calcium chloride (CaCl2)
- Optional trace NaCl for flavor balancing

The additive will be delivered as a liquid concentrate or dry blend, depending on lab recommendation.

5. R&D Environment — “Kitchen-Style Microfactory” Concept
The R&D process will use human-operated stations inspired by kitchen appliances, but with scientific controls.

Module A — Water Preparation
- Kitchen analogue: kettles, carafes, filters
- R&D role: prepare purified, low-mineral water with controlled pH

Module B — Mineral Stock Handling
- Kitchen analogue: measuring cups, bowls, stirrers
- R&D role: prepare mineral stock solutions at known concentrations

Module C — Mixing & Conditioning
- Kitchen analogue: stand mixer, immersion blender, temperature bath
- R&D role: combine mineral stocks with aspartame solutions under controlled conditions

Module D — Sensory Testing
- Kitchen analogue: tasting counter
- R&D role: human sensory panels comparing HFCS cola vs. aspartame vs. prototypes

Module E — Data Logging & Iteration
- Kitchen analogue: recipe notebook
- R&D role: track mineral ratios, sensory outcomes, off-notes, and promising prototypes

6. Research Questions
- What mineral ratios produce the closest match to sucrose’s sweetness curve?
- How do mineral ions interact with aspartame in acidic cola matrices?
- What concentration ranges avoid salty, metallic, or bitter off-notes?
- How does carbonation affect the additive’s performance?
- What delivery format (liquid vs. dry) is most stable and scalable?

7. Deliverables
Primary Deliverables:
- 3–5 optimized mineral profiles
- Sensory data comparing each profile to sucrose/HFCS
- Safety and toxicology assessment
- Recommended concentration ranges for beverage use
- Stability data (temperature, pH, storage)

Secondary Deliverables:
- Prototype additive samples
- R&D documentation
- Manufacturing feasibility assessment
- Regulatory pathway outline (GRAS, FDA, etc.)

8. Constraints & Requirements
- All minerals must be food-grade
- No artificial sweeteners added beyond aspartame
- No unsafe concentrations of any mineral
- No kitchen-level manufacturing instructions
- All processes must be validated in a controlled lab environment

9. Success Criteria
The additive is considered successful if:

- Aspartame + additive matches sucrose/HFCS within acceptable sensory tolerance
- No detectable salty, metallic, or bitter off-notes
- Additive is stable, safe, and compatible with standard beverage matrices
- Human sensory panels prefer the modulated aspartame over plain aspartame

10. Recommended Next Steps
- Lab prepares initial mineral stock solutions
- Run first-round sensory tests
- Narrow to promising mineral ratios
- Conduct safety and stability testing
- Develop prototype additive
- Begin pilot-scale production planning
"""

    print_section("1. R&D GOAL", rd_goal)
    print_section("2. SCIENTIFIC BACKBONE", scientific_backbone)
    print_section("3. KITCHEN-STYLE R&D ENVIRONMENT", kitchen_env)
    print_section("4. HUMAN PROCESS FLOW", human_flow)
    print_section("5. KITCHEN SUPPLIES AT SCALE", kitchen_scale)
    print_section("FULL R&D BRIEF", rd_brief)


if __name__ == "__main__":
    main()
