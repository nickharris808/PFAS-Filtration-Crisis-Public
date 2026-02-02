# Granular Activated Carbon (GAC): Technical Limitations for PFAS Removal
## Why the Industry Standard Cannot Meet EPA Requirements

---

## Executive Summary

Granular Activated Carbon (GAC) is the most widely deployed technology for PFAS treatment in drinking water systems. However, fundamental physicochemical limitations prevent GAC from reliably achieving the new EPA Maximum Contaminant Level of **4 parts per trillion (ppt)** for PFOA and PFOS.

This document explains why.

---

## How GAC Works

### Basic Mechanism

GAC removes contaminants through **physical adsorption** — molecules adhere to the carbon surface via:

1. **Van der Waals forces** — Weak intermolecular attractions
2. **Hydrophobic interactions** — Non-polar molecules prefer carbon surface over water
3. **π-π interactions** — Aromatic compounds interact with graphitic carbon structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     GAC ADSORPTION SCHEMATIC                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Water Flow →                                                              │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │                                                                   │    │
│   │    ████        ████        ████        ████        ████           │    │
│   │   █    █      █    █      █    █      █    █      █    █          │    │
│   │  █  ▒▒  █    █  ▒▒  █    █      █    █      █    █      █         │    │
│   │  █  ▒▒  █    █  ▒▒  █    █      █    █      █    █      █         │    │
│   │   █    █      █    █      █    █      █    █      █    █          │    │
│   │    ████        ████        ████        ████        ████           │    │
│   │                                                                   │    │
│   │   ▒▒ = PFAS adsorbed in pores                                    │    │
│   │                                                                   │    │
│   │   Problem: PFAS binding is REVERSIBLE. Under certain conditions, │    │
│   │   PFAS can DESORB and re-enter the water stream.                 │    │
│   │                                                                   │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### GAC Types for PFAS

| GAC Type | Source | Surface Area (m²/g) | PFAS Performance |
|:---------|:-------|:-------------------|:-----------------|
| **Bituminous coal** | Coal | 900-1100 | Best for PFOS/PFOA |
| **Lignite coal** | Coal | 500-700 | Moderate |
| **Coconut shell** | Biomass | 1000-1200 | Poor (microporous) |
| **Wood-based** | Biomass | 600-800 | Poor |

**Recommendation:** Bituminous coal-based GAC is standard for PFAS applications.

---

## Fundamental Limitation #1: Weak Binding Energy

### The Thermodynamic Reality

GAC binds PFAS through **non-specific hydrophobic interactions**. The binding energies are:

| PFAS Compound | Chain Length | Binding Energy (kJ/mol) | Implication |
|:--------------|:-------------|:------------------------|:------------|
| PFOS | C8 | -48 ± 6 | Strongest (long chain) |
| PFOA | C8 | -42 ± 5 | Moderate |
| PFHxS | C6 | -35 ± 4 | Weak |
| PFHxA | C6 | -32 ± 4 | Weak |
| PFBS | C4 | -18 ± 3 | Very weak |
| PFBA | C4 | -15 ± 3 | Essentially non-binding |

**The 4 ppt requirement demands binding energies of approximately -80 kJ/mol or stronger.**

GAC achieves only **half** the required binding strength for long-chain PFAS, and **less than a quarter** for short-chain PFAS.

### Why This Matters: Equilibrium

At thermodynamic equilibrium, the effluent concentration (C_eff) is related to the binding energy (ΔG) by:

```
C_eff = C_inlet × exp(ΔG / RT)
```

Where:
- R = 8.314 J/mol·K (gas constant)
- T = 298 K (room temperature)

For GAC binding PFOA at -42 kJ/mol:
```
C_eff/C_inlet = exp(-42,000 / (8.314 × 298)) = exp(-17.0) ≈ 4 × 10⁻⁸
```

This suggests excellent removal... **but this is the equilibrium limit**. In practice, kinetic limitations and competing species prevent reaching this theoretical limit.

---

## Fundamental Limitation #2: NOM Competition

### Natural Organic Matter Outcompetes PFAS

All natural water sources contain **Natural Organic Matter (NOM)** — humic acids, fulvic acids, and other dissolved organic compounds.

NOM concentration in typical water sources:
- Surface water: 2-10 mg/L DOC (dissolved organic carbon)
- Groundwater: 0.5-2 mg/L DOC

**PFAS concentration:** 0.00001-0.0001 mg/L (10-100 ppt)

**Ratio:** NOM is 10,000-100,000× more concentrated than PFAS.

### NOM "Poisons" the GAC

NOM molecules:
1. Adsorb to the same active sites as PFAS
2. Block micropores (access to internal surface area)
3. Create a "fouling layer" that slows PFAS diffusion

**Result:** GAC capacity for PFAS decreases by 50-90% in the presence of typical NOM.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     NOM COMPETITION EFFECT                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   GAC Capacity for PFAS                                                     │
│        │                                                                    │
│   100% ┤  ████████                                                          │
│        │  ████████   Pristine GAC                                           │
│    80% ┤  ████████   (lab conditions, pure water)                           │
│        │  ████████                                                          │
│    60% ┤  ████████                                                          │
│        │  ████████   ████████                                               │
│    40% ┤  ████████   ████████   With NOM                                    │
│        │  ████████   ████████   (real water)                                │
│    20% ┤  ████████   ████████   ████████                                    │
│        │  ████████   ████████   ████████                                    │
│     0% ┤──████████───████████───████████───                                 │
│             Lab        Low       High                                       │
│           (DI H2O)     NOM        NOM                                       │
│                      (1 mg/L)   (5 mg/L)                                    │
│                                                                             │
│   PFAS treatment in real water may be 60-80% less effective than lab data. │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Fundamental Limitation #3: Short-Chain PFAS Failure

### The Short-Chain Problem

Modern PFAS regulations include short-chain compounds (C4-C6) as manufacturers shifted from C8 chemistry:

| Compound | Chain | GAC Removal | Typical Effluent |
|:---------|:------|:------------|:-----------------|
| PFOS | C8 | 60-90% | 2-20 ppt |
| PFOA | C8 | 60-85% | 3-25 ppt |
| PFHxS | C6 | 40-70% | 10-50 ppt |
| PFBS | C4 | **10-30%** | 50-200 ppt |
| PFBA | C4 | **<20%** | 100+ ppt |

**EPA Hazard Index** includes PFBS with an HBWC of 2,000 ppt. While this is higher than PFOA/PFOS limits, the poor GAC removal means PFBS can contribute significantly to Hazard Index exceedances.

### Why Short-Chain PFAS Don't Adsorb

Short-chain PFAS have:
1. **Shorter fluoroalkyl tails** → Fewer hydrophobic contact points
2. **Higher water solubility** → Thermodynamic preference for aqueous phase
3. **Faster diffusion** → Less residence time in pores
4. **Lower molecular weight** → Weaker van der Waals forces

**There is no operational adjustment that can make GAC effective for short-chain PFAS.** This is a molecular property of the adsorbent-adsorbate pair.

---

## Fundamental Limitation #4: Breakthrough and Leaching

### Breakthrough Curves

GAC beds eventually "break through" — the effluent concentration rises to meet the influent:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        TYPICAL PFAS BREAKTHROUGH CURVE                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Effluent/Influent Ratio (C/C₀)                                           │
│        │                                                                    │
│    1.0 ┤                                               ██████████████████   │
│        │                                          █████                     │
│    0.8 ┤                                      ████                          │
│        │                                   ███                              │
│    0.6 ┤                                ███                                 │
│        │                             ███                                    │
│    0.4 ┤                          ███                                       │
│        │                       ███                                          │
│    0.2 ┤                    ███                                             │
│        │               █████                                                │
│    0.1 ┤- - - - - -████- - - - - - - - - - - - - - ← 90% removal threshold │
│        │        ███                                                         │
│   0.05 ┤- - ████- - - - - - - - - - - - - - - - - - ← 95% removal threshold│
│        │  ██                                                                │
│      0 ┤██────────────────────────────────────────────────────────────────  │
│        └────────────────────────────────────────────────────────────────→   │
│             0     10K     20K     30K     40K     50K     60K               │
│                              Bed Volumes Treated                            │
│                                                                             │
│   PFOS breaks through first (highest loading), then PFOA, then short-chain │
│   Order of breakthrough: PFBS > PFBA > PFHxS > PFHxA > PFOA > PFOS         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### The Leaching Problem

**Critical Insight:** GAC does not just fail to remove PFAS after breakthrough — it can actively **release previously captured PFAS** back into the water stream.

This occurs when:
1. Influent PFAS concentration drops (e.g., source remediation)
2. Temperature increases
3. NOM displaces PFAS from binding sites
4. Water chemistry changes (pH, ionic strength)

**Result:** Effluent PFAS can **exceed** influent PFAS — a phenomenon called "chromatographic elution."

---

## Fundamental Limitation #5: Disposal Burden

### Spent GAC is Hazardous Waste

PFAS-laden GAC cannot be:
- Landfilled (PFAS leaches into groundwater)
- Regenerated (PFAS not destroyed, just transferred)
- Composted (PFAS persists)

**The only acceptable disposal is high-temperature incineration (>1100°C).**

### Disposal Costs

| Disposal Method | Cost ($/ton) | PFAS Fate |
|:----------------|:-------------|:----------|
| Landfill | $50-100 | ❌ Leaches — prohibited |
| Thermal regeneration | $500-800 | ❌ PFAS to atmosphere |
| Incineration (1100°C+) | **$2,000-5,000** | ✅ Destroyed |
| Supercritical water oxidation | $3,000-6,000 | ✅ Destroyed |

### Annual GAC Replacement Costs (Example)

For a 10 MGD (million gallons/day) treatment plant:

| Parameter | Value |
|:----------|:------|
| Empty Bed Contact Time (EBCT) | 15 minutes |
| GAC volume | 104,000 gallons = 14,000 ft³ |
| GAC density | 28 lb/ft³ |
| GAC mass | 196 tons |
| GAC cost | $1,500/ton |
| Replacement frequency | 12-18 months |
| **Annual GAC cost** | **$200,000-300,000** |
| **Disposal cost** | **$400,000-1,000,000** |
| **Total annual** | **$600,000-1,300,000** |

---

## Performance Data

### Typical Field Performance (Approximate Ranges)

| PFAS | Typical Influent | Typical Effluent | Removal Range |
|:-----|:-----------------|:-----------------|:--------------|
| PFOS (C8) | 20-200 ppt | 2-30 ppt | 70-95% |
| PFOA (C8) | 20-200 ppt | 5-40 ppt | 60-90% |
| PFHxS (C6) | 10-100 ppt | 5-50 ppt | 40-70% |
| PFBS (C4) | 10-100 ppt | 8-90 ppt | 10-30% |

*Note: These are approximate ranges based on EPA guidance and industry experience. Actual performance varies significantly with water quality, contact time, and GAC type. Verify against peer-reviewed literature for specific applications.*

**Key Observation:** GAC rarely achieves consistent sub-4 ppt levels needed for EPA compliance, especially for short-chain PFAS.

### Laboratory vs. Field Performance

| Condition | Lab (DI water) | Field (real water) |
|:----------|:---------------|:-------------------|
| Capacity | Higher | 50-80% lower |
| Bed life | Longer | Significantly shorter |
| Short-chain | Moderate | Poor |

**GAC performance in real water is typically 50-80% worse than laboratory predictions** due to NOM competition and other factors.

---

## Operational Adjustments: Why They Don't Work

### "Just Use More GAC"

| Adjustment | Effect | Limitation |
|:-----------|:-------|:-----------|
| Increase bed depth | Marginal improvement | Cost linear, benefit logarithmic |
| Lower flow rate | More contact time | Reduces plant capacity |
| Use two beds in series | Polishing | Still bound by thermodynamics |
| Pre-treatment (NOM removal) | Less competition | Adds cost; doesn't fix binding |

**Fundamental Issue:** No operational change can overcome the thermodynamic limitation of weak binding energy.

---

## Conclusions

### GAC Cannot Meet 4 ppt MCL Because:

1. **Binding is too weak** — -42 kJ/mol vs. required -80 kJ/mol
2. **NOM competition** — Reduces effective capacity by 50-90%
3. **Short-chain failure** — <30% removal for C4 PFAS
4. **Leaching risk** — Previously captured PFAS can desorb
5. **Disposal burden** — Hazardous waste with $2,000-5,000/ton destruction cost

### When GAC Is Appropriate

GAC may be suitable for:
- Interim treatment while better technologies develop
- Low-risk situations with only long-chain PFAS
- Pre-treatment before more selective polishing
- Small systems with limited capital

### When GAC Is Inappropriate

GAC is inappropriate for:
- Strict 4 ppt compliance with safety margin
- Waters containing short-chain PFAS (PFBS, PFBA)
- High-NOM waters (surface water)
- Long-term sustainable treatment (disposal burden)

---

## References and Further Reading

**Verifiable Government Sources:**

1. U.S. EPA. "PFAS National Primary Drinking Water Regulation." 89 FR 32532 (April 26, 2024).

2. U.S. EPA. "Technical Fact Sheet: Drinking Water Health Advisories for PFOA and PFOS." EPA/600/R-17/488 (2022).

3. U.S. EPA Office of Research and Development. Guidance on PFAS treatment technologies for public water systems.

**For Peer-Reviewed Data:**

Performance data for GAC should be verified against peer-reviewed literature. Recommended search terms:
- "granular activated carbon PFAS removal"
- "GAC PFOA breakthrough"
- "activated carbon PFBS adsorption"

Common journals: Environmental Science & Technology, Water Research, Journal of Hazardous Materials.

---

*This document is for informational purposes only. Performance data are approximate ranges and should be verified for specific applications. Consult with water treatment professionals for site-specific guidance.*
