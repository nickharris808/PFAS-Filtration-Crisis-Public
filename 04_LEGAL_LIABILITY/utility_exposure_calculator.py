#!/usr/bin/env python3
"""
PFAS Liability Exposure Calculator for Water Utilities

This educational tool estimates potential legal and regulatory exposure
for water utilities based on PFAS contamination levels and population served.

DISCLAIMER: This calculator provides rough estimates based on publicly
available settlement data and regulatory information. It does not constitute
legal advice. Consult with qualified legal counsel for actual liability analysis.

Data Sources:
- 3M AFFF Settlement: $10.3B for ~3,000 water systems (~$3.4M average)
- Chemours/DuPont Settlement: $1.19B 
- EPA MCL Violation Penalties: $70,117/day (2024 rate)
- Personal injury class actions: $25-75/person (typical range)

Author: Genesis Platform Inc.
License: CC BY-NC-ND 4.0
"""

import json
import argparse
from dataclasses import dataclass
from typing import Dict, Any, Optional
from datetime import datetime


# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS (based on public data)
# ─────────────────────────────────────────────────────────────────────────────

# EPA Maximum Contaminant Levels (ppt = parts per trillion = ng/L)
EPA_LIMITS = {
    "PFOA": 4.0,
    "PFOS": 4.0,
    "PFHxS": 10.0,
    "PFNA": 10.0,
    "HFPO-DA": 10.0,  # GenX
}

# Penalty rate (per day, per violation) - 2024 rate
EPA_PENALTY_RATE = 70117  # dollars

# Settlement-based per-capita liability estimates
# Based on 3M ($10.3B / ~300M affected) and class action ranges
PER_CAPITA_LIABILITY = {
    "low": 25,      # Conservative estimate
    "mid": 50,      # Based on 3M settlement
    "high": 100,    # Based on higher-value claims
}

# Treatment cost estimates (per 1000 gallons treated)
TREATMENT_COSTS = {
    "gac": {"capital_per_mgd": 800000, "om_per_1000gal": 0.75},
    "ix": {"capital_per_mgd": 1200000, "om_per_1000gal": 0.50},
    "ro": {"capital_per_mgd": 2000000, "om_per_1000gal": 1.50},
    "novel": {"capital_per_mgd": 600000, "om_per_1000gal": 0.35},  # Projected
}


# ─────────────────────────────────────────────────────────────────────────────
# DATA CLASSES
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class PFASResult:
    """Individual PFAS measurement result."""
    compound: str
    concentration_ppt: float
    
    @property
    def exceeds_mcl(self) -> bool:
        limit = EPA_LIMITS.get(self.compound, float("inf"))
        return self.concentration_ppt > limit
    
    @property
    def exceedance_factor(self) -> float:
        limit = EPA_LIMITS.get(self.compound, float("inf"))
        if limit == 0:
            return float("inf") if self.concentration_ppt > 0 else 0
        return max(0, (self.concentration_ppt / limit) - 1)


@dataclass  
class UtilityProfile:
    """Water utility characteristics."""
    name: str
    population_served: int
    daily_flow_mgd: float  # Million gallons per day
    pfas_results: list  # List of PFASResult
    years_of_exposure: int = 5  # Estimated years of undetected exposure
    
    @property
    def in_compliance(self) -> bool:
        return not any(r.exceeds_mcl for r in self.pfas_results)
    
    @property
    def total_exceedance_factor(self) -> float:
        return sum(r.exceedance_factor for r in self.pfas_results)


# ─────────────────────────────────────────────────────────────────────────────
# CALCULATION FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def calculate_regulatory_penalties(
    profile: UtilityProfile,
    violation_days: int = 365
) -> Dict[str, float]:
    """
    Calculate potential EPA MCL violation penalties.
    
    Penalties are assessed per compound, per day of violation.
    """
    if profile.in_compliance:
        return {"total": 0, "per_compound": {}, "note": "In compliance - no penalties"}
    
    violating_compounds = [r for r in profile.pfas_results if r.exceeds_mcl]
    per_compound = {}
    
    for result in violating_compounds:
        penalty = EPA_PENALTY_RATE * violation_days
        per_compound[result.compound] = {
            "daily_penalty": EPA_PENALTY_RATE,
            "annual_penalty": penalty,
            "concentration_ppt": result.concentration_ppt,
            "mcl_ppt": EPA_LIMITS[result.compound],
            "exceedance_factor": result.exceedance_factor,
        }
    
    total = sum(p["annual_penalty"] for p in per_compound.values())
    
    return {
        "total": total,
        "per_compound": per_compound,
        "violation_days": violation_days,
        "note": f"Penalties for {len(violating_compounds)} compounds exceeding MCL",
    }


def calculate_litigation_exposure(
    profile: UtilityProfile,
) -> Dict[str, Any]:
    """
    Calculate potential third-party litigation exposure.
    
    Based on settlement data from 3M, Chemours, and class action ranges.
    """
    if profile.in_compliance:
        return {
            "low": 0,
            "mid": 0,
            "high": 0,
            "note": "In compliance - reduced litigation risk",
        }
    
    # Affected population estimate (assume 80% of served population)
    affected_population = int(profile.population_served * 0.8)
    
    # Exceedance multiplier (higher exposure = higher damages)
    exceedance_mult = min(1 + profile.total_exceedance_factor * 0.1, 3.0)
    
    # Duration multiplier
    duration_mult = min(1 + profile.years_of_exposure * 0.05, 2.0)
    
    # Calculate estimates
    low = affected_population * PER_CAPITA_LIABILITY["low"] * exceedance_mult
    mid = affected_population * PER_CAPITA_LIABILITY["mid"] * exceedance_mult * duration_mult
    high = affected_population * PER_CAPITA_LIABILITY["high"] * exceedance_mult * duration_mult
    
    return {
        "affected_population": affected_population,
        "low": low,
        "mid": mid,
        "high": high,
        "exceedance_multiplier": exceedance_mult,
        "duration_multiplier": duration_mult,
        "note": "Based on 3M/Chemours settlement data and class action ranges",
    }


def calculate_treatment_costs(
    profile: UtilityProfile,
    technology: str = "gac",
    years: int = 20,
) -> Dict[str, float]:
    """
    Calculate treatment costs for PFAS removal.
    
    Includes capital costs and 20-year O&M.
    """
    if technology not in TREATMENT_COSTS:
        technology = "gac"
    
    costs = TREATMENT_COSTS[technology]
    
    # Capital cost
    capital = costs["capital_per_mgd"] * profile.daily_flow_mgd
    
    # Annual O&M (365 days × MGD × 1000 gal × cost per 1000 gal)
    annual_om = 365 * profile.daily_flow_mgd * 1000 * costs["om_per_1000gal"]
    
    # Present value of O&M (simple sum, no discounting for educational purposes)
    total_om = annual_om * years
    
    # Total
    total = capital + total_om
    
    return {
        "technology": technology,
        "capital": capital,
        "annual_om": annual_om,
        "years": years,
        "total_om": total_om,
        "total": total,
        "cost_per_1000gal": costs["om_per_1000gal"],
    }


def generate_liability_report(profile: UtilityProfile) -> Dict[str, Any]:
    """
    Generate comprehensive liability exposure report.
    """
    regulatory = calculate_regulatory_penalties(profile)
    litigation = calculate_litigation_exposure(profile)
    treatment = calculate_treatment_costs(profile, "gac", 20)
    
    # Total exposure estimates
    total_low = regulatory["total"] + litigation["low"] + treatment["total"]
    total_mid = regulatory["total"] + litigation["mid"] + treatment["total"]
    total_high = regulatory["total"] + litigation["high"] + treatment["total"]
    
    return {
        "utility": {
            "name": profile.name,
            "population_served": profile.population_served,
            "daily_flow_mgd": profile.daily_flow_mgd,
            "years_of_exposure": profile.years_of_exposure,
        },
        "pfas_levels": [
            {
                "compound": r.compound,
                "concentration_ppt": r.concentration_ppt,
                "mcl_ppt": EPA_LIMITS.get(r.compound, "N/A"),
                "exceeds_mcl": r.exceeds_mcl,
            }
            for r in profile.pfas_results
        ],
        "compliance_status": profile.in_compliance,
        "regulatory_penalties": regulatory,
        "litigation_exposure": litigation,
        "treatment_costs": treatment,
        "total_exposure": {
            "low": total_low,
            "mid": total_mid,
            "high": total_high,
        },
        "report_generated": datetime.now().isoformat(),
        "disclaimer": (
            "This report is for educational purposes only and does not constitute "
            "legal advice. Actual liability may vary significantly based on specific "
            "circumstances. Consult with qualified legal counsel."
        ),
    }


def format_currency(amount: float) -> str:
    """Format number as currency."""
    if amount >= 1e9:
        return f"${amount/1e9:.2f}B"
    elif amount >= 1e6:
        return f"${amount/1e6:.2f}M"
    elif amount >= 1e3:
        return f"${amount/1e3:.1f}K"
    else:
        return f"${amount:,.0f}"


def print_report(report: Dict[str, Any]) -> None:
    """Print formatted liability report."""
    print("\n" + "="*70)
    print("   PFAS LIABILITY EXPOSURE REPORT")
    print("="*70)
    
    util = report["utility"]
    print(f"\nUtility: {util['name']}")
    print(f"Population Served: {util['population_served']:,}")
    print(f"Daily Flow: {util['daily_flow_mgd']:.1f} MGD")
    print(f"Estimated Exposure Duration: {util['years_of_exposure']} years")
    
    print("\n" + "-"*70)
    print("PFAS LEVELS")
    print("-"*70)
    print(f"{'Compound':<12} {'Level (ppt)':<15} {'MCL (ppt)':<12} {'Status':<12}")
    print("-"*70)
    
    for r in report["pfas_levels"]:
        status = "❌ EXCEEDS" if r["exceeds_mcl"] else "✅ OK"
        print(f"{r['compound']:<12} {r['concentration_ppt']:<15.1f} {r['mcl_ppt']:<12} {status:<12}")
    
    compliance = "✅ IN COMPLIANCE" if report["compliance_status"] else "❌ NOT IN COMPLIANCE"
    print(f"\nOverall Status: {compliance}")
    
    print("\n" + "-"*70)
    print("REGULATORY PENALTIES (Annual)")
    print("-"*70)
    reg = report["regulatory_penalties"]
    print(f"Total Annual Penalties: {format_currency(reg['total'])}")
    if reg["per_compound"]:
        for compound, data in reg["per_compound"].items():
            print(f"  - {compound}: {format_currency(data['annual_penalty'])}")
    
    print("\n" + "-"*70)
    print("LITIGATION EXPOSURE")
    print("-"*70)
    lit = report["litigation_exposure"]
    print(f"Affected Population: {lit.get('affected_population', 0):,}")
    print(f"Low Estimate:  {format_currency(lit['low'])}")
    print(f"Mid Estimate:  {format_currency(lit['mid'])}")
    print(f"High Estimate: {format_currency(lit['high'])}")
    
    print("\n" + "-"*70)
    print("TREATMENT COSTS (20-Year)")
    print("-"*70)
    tx = report["treatment_costs"]
    print(f"Technology: {tx['technology'].upper()}")
    print(f"Capital Cost: {format_currency(tx['capital'])}")
    print(f"Annual O&M: {format_currency(tx['annual_om'])}")
    print(f"Total (20-year): {format_currency(tx['total'])}")
    
    print("\n" + "="*70)
    print("TOTAL LIABILITY EXPOSURE")
    print("="*70)
    total = report["total_exposure"]
    print(f"\n  Low Estimate:  {format_currency(total['low'])}")
    print(f"  Mid Estimate:  {format_currency(total['mid'])}")
    print(f"  High Estimate: {format_currency(total['high'])}")
    
    print("\n" + "-"*70)
    print("⚠️  DISCLAIMER")
    print("-"*70)
    print(report["disclaimer"])
    print("\n" + "="*70)
    
    print("\n📧 For solutions that eliminate this liability, contact:")
    print("   [Available upon request]")
    print("")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="PFAS Liability Exposure Calculator for Water Utilities",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic calculation
  python utility_exposure_calculator.py --population 100000 --flow 10 --pfoa 25 --pfos 15
  
  # With all compounds
  python utility_exposure_calculator.py --population 50000 --flow 5 --pfoa 20 --pfos 30 --pfhxs 15 --genx 8
  
  # JSON output
  python utility_exposure_calculator.py --population 100000 --flow 10 --pfoa 25 --json
        """
    )
    
    parser.add_argument("--name", type=str, default="Example Utility",
                       help="Utility name")
    parser.add_argument("--population", type=int, required=True,
                       help="Population served")
    parser.add_argument("--flow", type=float, required=True,
                       help="Daily flow in MGD (million gallons per day)")
    parser.add_argument("--years", type=int, default=5,
                       help="Estimated years of exposure (default: 5)")
    
    # PFAS levels
    parser.add_argument("--pfoa", type=float, default=0,
                       help="PFOA concentration in ppt")
    parser.add_argument("--pfos", type=float, default=0,
                       help="PFOS concentration in ppt")
    parser.add_argument("--pfhxs", type=float, default=0,
                       help="PFHxS concentration in ppt")
    parser.add_argument("--pfna", type=float, default=0,
                       help="PFNA concentration in ppt")
    parser.add_argument("--genx", type=float, default=0,
                       help="HFPO-DA (GenX) concentration in ppt")
    
    parser.add_argument("--json", action="store_true",
                       help="Output as JSON instead of formatted report")
    
    args = parser.parse_args()
    
    # Build PFAS results
    pfas_results = []
    if args.pfoa > 0:
        pfas_results.append(PFASResult("PFOA", args.pfoa))
    if args.pfos > 0:
        pfas_results.append(PFASResult("PFOS", args.pfos))
    if args.pfhxs > 0:
        pfas_results.append(PFASResult("PFHxS", args.pfhxs))
    if args.pfna > 0:
        pfas_results.append(PFASResult("PFNA", args.pfna))
    if args.genx > 0:
        pfas_results.append(PFASResult("HFPO-DA", args.genx))
    
    if not pfas_results:
        print("Error: At least one PFAS concentration must be provided.")
        print("Use --help for usage information.")
        return
    
    # Create profile
    profile = UtilityProfile(
        name=args.name,
        population_served=args.population,
        daily_flow_mgd=args.flow,
        pfas_results=pfas_results,
        years_of_exposure=args.years,
    )
    
    # Generate report
    report = generate_liability_report(profile)
    
    if args.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        print_report(report)


if __name__ == "__main__":
    main()
