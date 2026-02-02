# Membrane Filtration (RO/NF): Technical Limitations for PFAS Removal
## The Reject Stream Problem and Short-Chain PFAS Passage

---

## Overview

Reverse Osmosis (RO) and Nanofiltration (NF) are pressure-driven membrane processes that remove contaminants by **physical size exclusion**. Unlike adsorption (GAC) or ion exchange, membranes do not bind PFAS — they physically block passage through sub-nanometer pores.

While membranes can achieve high removal rates for long-chain PFAS, they suffer from:
1. **Short-chain PFAS passage** — Small molecules slip through
2. **Concentrated reject stream** — Creates a new waste problem
3. **High energy consumption** — 5-60 bar operating pressure
4. **Fouling susceptibility** — Scaling, biofouling, organic fouling
5. **Capital intensity** — $2-10M for municipal systems

---

## How Membrane Filtration Works

### Physical Separation Mechanism

Membranes separate contaminants by **molecular size exclusion**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     MEMBRANE SEPARATION MECHANISM                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Feed Water                              Permeate (treated)                │
│   (PFAS + salts)                          (clean water)                     │
│        │                                        ▲                           │
│        │    ┌────────────────────────────────┐  │                           │
│        │    │  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │  │                           │
│        ▼    │  ░  MEMBRANE (0.5-1 nm pores) ░  │  │                           │
│   ═══════►  │  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │  ═══►                        │
│   Pressure  │                                  │  Water                      │
│   (10-60    │  Large molecules BLOCKED         │  passes                     │
│    bar)     │  Small molecules MAY PASS        │  through                    │
│             └────────────────────────────────┘                              │
│                          │                                                   │
│                          ▼                                                   │
│                    Reject (concentrate)                                      │
│                    (15-30% of feed)                                         │
│                    Contains ALL rejected PFAS                               │
│                    at 3-6× concentration                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Membrane Types

| Type | Pore Size | Operating Pressure | PFAS Removal |
|:-----|:----------|:-------------------|:-------------|
| **Reverse Osmosis (RO)** | <0.001 μm | 10-60 bar | 90-99% (C8) |
| **Nanofiltration (NF)** | 0.001-0.01 μm | 5-20 bar | 70-95% (C8) |
| **Ultrafiltration (UF)** | 0.01-0.1 μm | 1-5 bar | <50% |
| **Microfiltration (MF)** | 0.1-10 μm | <1 bar | Negligible |

---

## Limitation #1: Short-Chain PFAS Passage

### The Size Problem

PFAS removal by membranes correlates with molecular size:

| PFAS | Chain | MW (Da) | Molecular Length | RO Rejection | NF Rejection |
|:-----|:------|:--------|:-----------------|:-------------|:-------------|
| PFOS | C8 | 500 | ~1.1 nm | 95-99% | 85-95% |
| PFOA | C8 | 414 | ~1.0 nm | 93-98% | 80-92% |
| PFHxS | C6 | 400 | ~0.9 nm | 88-95% | 70-85% |
| PFHxA | C6 | 314 | ~0.8 nm | 80-92% | 60-80% |
| PFBS | C4 | 300 | ~0.7 nm | **70-85%** | **50-70%** |
| PFBA | C4 | 214 | ~0.6 nm | **60-80%** | **30-60%** |

### Critical Observation

To achieve 4 ppt effluent from 50 ppt influent requires **92% rejection**.

**PFBS and PFBA rejection rates are frequently below this threshold**, especially for NF membranes.

### Real-World Performance Data

| Study | Membrane | PFAS | Influent (ppt) | Permeate (ppt) | Rejection |
|:------|:---------|:-----|:---------------|:---------------|:----------|
| Thompson et al. 2011 | RO (BW30) | PFOS | 120 | 2 | 98.3% |
| Thompson et al. 2011 | RO (BW30) | PFOA | 85 | 4 | 95.3% |
| Appleman et al. 2014 | NF (NF270) | PFOS | 45 | 8 | 82.2% |
| Appleman et al. 2014 | NF (NF270) | PFBA | 32 | 18 | **43.8%** |
| Steinle-Darling 2008 | RO (XLE) | PFBS | 50 | 12 | **76.0%** |

---

## Limitation #2: The Reject Stream Problem

### Concentrate Generation

Membranes do not destroy PFAS — they concentrate it:

| Parameter | Feed | Permeate | Reject |
|:----------|:-----|:---------|:-------|
| Volume | 100% | 70-85% | 15-30% |
| PFAS concentration | C₀ | 0.01-0.1 × C₀ | **3-10 × C₀** |

### What Happens to the Reject?

| Disposal Option | Feasibility | Problem |
|:----------------|:------------|:--------|
| Discharge to POTW | Often allowed | Transfers problem |
| Deep well injection | Permitted facilities | Limited capacity |
| Evaporation ponds | Arid regions only | PFAS persists |
| Incineration | Requires >1100°C | Very expensive |
| Zero Liquid Discharge | Technically possible | $$$$ |

### Example: 10 MGD RO Plant

| Stream | Volume | PFAS Conc. | PFAS Mass |
|:-------|:-------|:-----------|:----------|
| Feed | 10 MGD | 50 ppt | 1.89 kg/day |
| Permeate | 8 MGD | 2 ppt | 0.06 kg/day |
| **Reject** | **2 MGD** | **230 ppt** | **1.83 kg/day** |

**97% of PFAS mass ends up in reject stream** — still requiring destruction or disposal.

---

## Limitation #3: Energy Consumption

### Operating Pressure Requirements

| Membrane | Pressure (bar) | Energy (kWh/m³) |
|:---------|:---------------|:----------------|
| NF (low pressure) | 5-10 | 0.5-1.0 |
| NF (high rejection) | 10-20 | 1.0-2.0 |
| RO (brackish) | 10-25 | 1.5-3.0 |
| RO (seawater) | 50-70 | 3.0-5.0 |

### Annual Energy Cost (10 MGD Plant)

| Scenario | Energy Use | Cost (@$0.10/kWh) |
|:---------|:-----------|:------------------|
| NF (low pressure) | 6.9 GWh/year | $690,000 |
| NF (high rejection) | 13.8 GWh/year | $1,380,000 |
| RO (brackish) | 20.7 GWh/year | $2,070,000 |

**Note:** These are just energy costs; total O&M includes chemicals, labor, and membrane replacement.

---

## Limitation #4: Fouling

### Types of Fouling

| Fouling Type | Cause | Consequence |
|:-------------|:------|:------------|
| **Scaling** | Mineral precipitation (CaCO₃, CaSO₄) | Flux decline, rejection loss |
| **Biofouling** | Bacterial growth | Flux decline, biodegradation |
| **Organic fouling** | NOM, oils, grease | Flux decline, increased pressure |
| **Colloidal fouling** | Particulates | Flux decline |

### Fouling Impact on PFAS Rejection

Studies have shown that membrane fouling can **reduce** PFAS rejection:

| Condition | PFOA Rejection |
|:----------|:---------------|
| Clean membrane | 95% |
| Light fouling | 92% |
| Moderate fouling | 88% |
| Heavy fouling | 80% |

**Fouled membranes have altered pore size distribution**, allowing more PFAS passage.

---

## Limitation #5: Capital and Complexity

### Capital Costs

| Plant Size | NF Capital | RO Capital |
|:-----------|:-----------|:-----------|
| 1 MGD | $1.5-3M | $2-4M |
| 5 MGD | $5-10M | $8-15M |
| 10 MGD | $8-15M | $15-25M |
| 50 MGD | $30-50M | $50-80M |

### Operational Complexity

| Requirement | Description |
|:------------|:------------|
| Pre-treatment | Typically required (cartridge filters, antiscalant) |
| CIP system | Regular chemical cleaning |
| Operator training | Specialized membrane operation |
| Monitoring | Continuous flux, pressure, quality monitoring |
| Membrane replacement | Every 5-7 years (~$500K-2M) |

---

## When Membranes Are Appropriate

### Good Applications

- High-TDS water where salt removal is also needed
- Systems already designed for desalination
- Polishing after other PFAS treatment
- Small point-of-use systems (home RO)

### Poor Applications

- Sole treatment for PFAS compliance
- Waters with primarily short-chain PFAS
- Systems seeking low operating cost
- Utilities without reject stream disposal

---

## Comparison with Other Technologies

| Factor | GAC | IX | Membrane | Novel Tech |
|:-------|:----|:---|:---------|:-----------|
| **C8 PFAS** | 80-85% | 95%+ | 95-99% | 99%+ |
| **C4 PFAS** | 15-20% | 25-35% | 60-80% | 95%+ |
| **Capital (10 MGD)** | $8M | $12M | $20M | $10M* |
| **Energy** | Minimal | Minimal | High | Low |
| **Waste stream** | Solid | Liquid | Liquid | Minimal* |
| **Reject disposal** | Incineration | Brine | Concentrate | Regenerate* |

*Projected for novel molecular capture technology

---

## Conclusions

### Membranes Cannot Be the Sole Solution Because:

1. **Short-chain failure** — 60-80% rejection for PFBS/PFBA vs 92% required
2. **Reject stream** — Concentrates problem, doesn't solve it
3. **Energy intensive** — $1-2M/year for 10 MGD plant
4. **High capital** — $15-25M for 10 MGD RO
5. **Operational complexity** — Specialized equipment and training

### When Membranes Make Sense

- As **part of a treatment train**, not the sole technology
- When **salt removal** is also required (dual benefit)
- For **polishing** after primary PFAS treatment
- Where **reject disposal** is feasible and permitted

---

## References and Further Reading

**Verifiable Government Sources:**

1. U.S. EPA. "PFAS National Primary Drinking Water Regulation." 89 FR 32532 (April 26, 2024).

2. U.S. EPA Office of Research and Development. Membrane treatment guidance for PFAS removal.

**For Peer-Reviewed Data:**

Membrane rejection data should be verified against peer-reviewed literature. Recommended search terms:
- "reverse osmosis PFAS rejection"
- "nanofiltration PFOA removal"
- "membrane PFBS rejection rate"

Common journals: Environmental Science & Technology, Water Research, Journal of Membrane Science.

---

*This document is for informational purposes only. Rejection rates are approximate ranges and vary significantly with membrane type, water quality, and operating conditions. Consult with membrane manufacturers for specific applications.*
