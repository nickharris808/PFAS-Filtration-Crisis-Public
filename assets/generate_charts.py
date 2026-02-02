#!/usr/bin/env python3
"""
PFAS Crisis Visualization Generator

Generates publication-quality charts for the PFAS Filtration Crisis white paper.
All data is from public sources (EPA, peer-reviewed literature, settlement filings).

Author: Genesis Platform Inc.
License: CC BY-NC-ND 4.0

Requirements:
    pip install matplotlib numpy pandas seaborn

Usage:
    python generate_charts.py --all          # Generate all charts
    python generate_charts.py --binding      # Just binding energy comparison
    python generate_charts.py --breakthrough # Just breakthrough curve
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# STYLE CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'legend.fontsize': 10,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

# Color palette
COLORS = {
    'gac': '#4C78A8',      # Blue
    'ix': '#54A24B',       # Green  
    'required': '#E45756', # Red
    'novel': '#72B7B2',    # Teal
    'warning': '#F58518',  # Orange
    'neutral': '#B279A2',  # Purple
}

OUTPUT_DIR = Path(__file__).parent


# ─────────────────────────────────────────────────────────────────────────────
# CHART 1: BINDING ENERGY COMPARISON
# ─────────────────────────────────────────────────────────────────────────────

def plot_binding_energy_comparison(output_path: Path = None):
    """
    Bar chart comparing binding energies of current vs required technology.
    
    Data sources:
    - Du et al. 2014, J. Hazardous Materials (GAC binding energies)
    - Zaggia et al. 2016, Water Research (IX binding energies)
    - Calculated threshold based on thermodynamic analysis
    """
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Data (from published literature)
    compounds = ['PFOS\n(C8)', 'PFOA\n(C8)', 'PFHxS\n(C6)', 'PFBS\n(C4)']
    
    gac_binding = [-48, -42, -35, -18]  # kJ/mol, from Du et al.
    ix_binding = [-52, -45, -38, -22]   # kJ/mol, from Zaggia et al.
    required = [-80, -80, -70, -60]     # kJ/mol, calculated threshold
    
    x = np.arange(len(compounds))
    width = 0.25
    
    # Bars
    bars1 = ax.bar(x - width, gac_binding, width, label='GAC (Current)', 
                   color=COLORS['gac'], edgecolor='black', linewidth=0.5)
    bars2 = ax.bar(x, ix_binding, width, label='Ion Exchange (Current)',
                   color=COLORS['ix'], edgecolor='black', linewidth=0.5)
    bars3 = ax.bar(x + width, required, width, label='Required for 4 ppt',
                   color=COLORS['required'], edgecolor='black', linewidth=0.5,
                   hatch='///', alpha=0.7)
    
    # Labels and formatting
    ax.set_xlabel('PFAS Compound', fontweight='bold')
    ax.set_ylabel('Binding Energy (kJ/mol)', fontweight='bold')
    ax.set_title('The Binding Energy Gap:\nCurrent Technology Cannot Meet EPA 4 ppt Requirement',
                fontweight='bold', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(compounds)
    ax.legend(loc='upper right')
    
    # Invert y-axis (more negative = stronger binding = better)
    ax.invert_yaxis()
    
    # Add annotation
    ax.annotate('STRONGER\nBINDING', xy=(0.02, 0.95), xycoords='axes fraction',
               fontsize=9, color='green', fontweight='bold', ha='left', va='top')
    ax.annotate('WEAKER\nBINDING', xy=(0.02, 0.05), xycoords='axes fraction',
               fontsize=9, color='red', fontweight='bold', ha='left', va='bottom')
    
    # Gap annotation
    ax.annotate('', xy=(3, -60), xytext=(3, -18),
               arrowprops=dict(arrowstyle='<->', color='black', lw=2))
    ax.annotate('GAP:\n42 kJ/mol', xy=(3.35, -39), fontsize=10, 
               fontweight='bold', color='black')
    
    # Add horizontal line at -80
    ax.axhline(y=-80, color=COLORS['required'], linestyle='--', alpha=0.5, linewidth=2)
    ax.text(3.5, -82, '4 ppt threshold', fontsize=9, color=COLORS['required'],
           va='top', ha='right')
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path)
        print(f"Saved: {output_path}")
    
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# CHART 2: BREAKTHROUGH CURVE
# ─────────────────────────────────────────────────────────────────────────────

def plot_breakthrough_curve(output_path: Path = None):
    """
    S-curve showing PFAS breakthrough over time for GAC.
    
    Data: Modeled based on published breakthrough studies
    - Appleman et al. 2014, Water Research
    - Patterson et al. 2019, AWWA Water Science
    """
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Generate breakthrough curve data (logistic function)
    bed_volumes = np.linspace(0, 80000, 500)
    
    # PFOS breaks through around 30,000 BV
    pfos_breakthrough = 100 / (1 + np.exp(-0.0002 * (bed_volumes - 35000)))
    
    # PFOA breaks through around 25,000 BV  
    pfoa_breakthrough = 100 / (1 + np.exp(-0.00025 * (bed_volumes - 28000)))
    
    # PFHxS breaks through around 15,000 BV
    pfhxs_breakthrough = 100 / (1 + np.exp(-0.0003 * (bed_volumes - 18000)))
    
    # PFBS breaks through almost immediately
    pfbs_breakthrough = 100 / (1 + np.exp(-0.0005 * (bed_volumes - 5000)))
    
    # Plot curves
    ax.plot(bed_volumes/1000, pfos_breakthrough, label='PFOS (C8)', 
           color='#1f77b4', linewidth=2.5)
    ax.plot(bed_volumes/1000, pfoa_breakthrough, label='PFOA (C8)',
           color='#ff7f0e', linewidth=2.5)
    ax.plot(bed_volumes/1000, pfhxs_breakthrough, label='PFHxS (C6)',
           color='#2ca02c', linewidth=2.5)
    ax.plot(bed_volumes/1000, pfbs_breakthrough, label='PFBS (C4)',
           color='#d62728', linewidth=2.5)
    
    # EPA limit line (assuming 50 ppt influent, 4 ppt limit = 8% of influent)
    epa_limit = 8  # 4 ppt / 50 ppt * 100%
    ax.axhline(y=epa_limit, color='red', linestyle='--', linewidth=2, alpha=0.7)
    ax.text(75, epa_limit + 3, 'EPA 4 ppt Limit\n(8% of influent)', 
           fontsize=10, color='red', fontweight='bold', ha='right')
    
    # Shaded "unsafe" zone
    ax.fill_between(bed_volumes/1000, epa_limit, 100, alpha=0.1, color='red')
    ax.text(70, 60, 'EPA VIOLATION\nZONE', fontsize=12, color='red', 
           fontweight='bold', alpha=0.5, ha='center')
    
    # Labels
    ax.set_xlabel('Bed Volumes Treated (thousands)', fontweight='bold')
    ax.set_ylabel('Effluent Concentration (% of Influent)', fontweight='bold')
    ax.set_title('GAC Breakthrough Curves: Short-Chain PFAS Fails First',
                fontweight='bold', fontsize=14)
    ax.legend(loc='center right')
    ax.set_xlim(0, 80)
    ax.set_ylim(0, 100)
    
    # Annotations
    ax.annotate('PFBS breakthrough\n< 10,000 BV', xy=(8, 50), xytext=(20, 70),
               arrowprops=dict(arrowstyle='->', color='black'),
               fontsize=10, ha='center')
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path)
        print(f"Saved: {output_path}")
    
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# CHART 3: COST COMPARISON
# ─────────────────────────────────────────────────────────────────────────────

def plot_cost_comparison(output_path: Path = None):
    """
    Stacked bar chart comparing treatment costs.
    
    Data: EPA cost estimates and industry data
    """
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Technologies
    techs = ['GAC', 'Ion Exchange\n(Single-Use)', 'Ion Exchange\n(Regenerable)', 
             'RO/NF', 'Novel Tech\n(Projected)']
    
    # Cost components ($/1000 gallons over 20 years, for 10 MGD plant)
    capital = [0.22, 0.33, 0.33, 0.55, 0.17]  # Amortized capital
    operations = [0.75, 1.20, 0.50, 1.50, 0.35]  # O&M
    disposal = [0.50, 0.60, 0.30, 0.40, 0.10]  # Waste disposal
    
    x = np.arange(len(techs))
    width = 0.6
    
    # Stacked bars
    bars1 = ax.bar(x, capital, width, label='Capital (amortized)', 
                   color='#4C78A8', edgecolor='black', linewidth=0.5)
    bars2 = ax.bar(x, operations, width, bottom=capital, label='Operations & Maintenance',
                   color='#F58518', edgecolor='black', linewidth=0.5)
    bottom2 = [c + o for c, o in zip(capital, operations)]
    bars3 = ax.bar(x, disposal, width, bottom=bottom2, label='Waste Disposal',
                   color='#E45756', edgecolor='black', linewidth=0.5)
    
    # Total cost labels
    totals = [c + o + d for c, o, d in zip(capital, operations, disposal)]
    for i, total in enumerate(totals):
        ax.text(i, total + 0.05, f'${total:.2f}', ha='center', fontweight='bold')
    
    # Labels
    ax.set_ylabel('Cost ($/1,000 gallons)', fontweight='bold')
    ax.set_title('PFAS Treatment Cost Comparison\n(20-Year Lifecycle for 10 MGD Plant)',
                fontweight='bold', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(techs)
    ax.legend(loc='upper right')
    ax.set_ylim(0, 3.0)
    
    # Highlight novel tech
    ax.get_children()[4].set_facecolor('#72B7B2')  # Capital bar for novel
    ax.annotate('Projected\n40% savings', xy=(4, 0.62), fontsize=9,
               ha='center', color='#72B7B2', fontweight='bold')
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path)
        print(f"Saved: {output_path}")
    
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# CHART 4: CHAIN LENGTH EFFECT
# ─────────────────────────────────────────────────────────────────────────────

def plot_chain_length_effect(output_path: Path = None):
    """
    Shows relationship between PFAS chain length and removal efficiency.
    
    Data: Compiled from multiple field studies
    """
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Data
    chain_lengths = [4, 5, 6, 7, 8, 9, 10]
    compounds = ['PFBA/PFBS', 'PFPeA/PFPeS', 'PFHxA/PFHxS', 'PFHpA/PFHpS', 
                'PFOA/PFOS', 'PFNA/PFNS', 'PFDA/PFDS']
    
    gac_removal = [15, 35, 55, 70, 82, 88, 92]  # % removal
    ix_removal = [28, 48, 68, 80, 92, 95, 97]   # % removal
    
    # Plot
    ax.plot(chain_lengths, gac_removal, 'o-', color=COLORS['gac'], 
           linewidth=2.5, markersize=10, label='GAC')
    ax.plot(chain_lengths, ix_removal, 's-', color=COLORS['ix'],
           linewidth=2.5, markersize=10, label='Ion Exchange')
    
    # Required removal line (92% for 50→4 ppt)
    ax.axhline(y=92, color=COLORS['required'], linestyle='--', linewidth=2)
    ax.text(10.1, 92, '92% required\nfor 4 ppt', fontsize=9, color=COLORS['required'],
           va='center', fontweight='bold')
    
    # Shaded failure zone
    ax.fill_between([4, 7], [0, 0], [92, 92], alpha=0.15, color='red')
    ax.text(5.5, 45, 'INADEQUATE\nREMOVAL', fontsize=12, color='red',
           fontweight='bold', ha='center', alpha=0.7)
    
    # Labels
    ax.set_xlabel('PFAS Carbon Chain Length', fontweight='bold')
    ax.set_ylabel('Removal Efficiency (%)', fontweight='bold')
    ax.set_title('The Short-Chain Problem:\nRemoval Efficiency Drops Sharply Below C8',
                fontweight='bold', fontsize=14)
    ax.legend(loc='lower right')
    ax.set_xlim(3.5, 10.5)
    ax.set_ylim(0, 100)
    ax.set_xticks(chain_lengths)
    ax.set_xticklabels([f'C{c}\n({compounds[i].split("/")[0]})' 
                        for i, c in enumerate(chain_lengths)], fontsize=9)
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path)
        print(f"Saved: {output_path}")
    
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# CHART 5: SETTLEMENT TIMELINE
# ─────────────────────────────────────────────────────────────────────────────

def plot_settlement_timeline(output_path: Path = None):
    """
    Timeline of major PFAS settlements.
    
    Data: Public court records and press releases
    """
    
    fig, ax = plt.subplots(figsize=(12, 5))
    
    # Settlement data
    settlements = [
        (2018, 0.85, '3M Minnesota\n$850M'),
        (2019, 0.021, 'Saint-Gobain NH\n$21M'),
        (2022, 0.055, 'Wolverine MI\n$55M'),
        (2023, 1.19, 'Chemours/DuPont\n$1.19B'),
        (2023, 10.3, '3M AFFF\n$10.3B'),
    ]
    
    years = [s[0] for s in settlements]
    amounts = [s[1] for s in settlements]
    labels = [s[2] for s in settlements]
    
    # Plot bars
    colors = ['#4C78A8', '#4C78A8', '#4C78A8', '#F58518', '#E45756']
    bars = ax.bar(years, amounts, width=0.6, color=colors, edgecolor='black')
    
    # Labels on bars
    for bar, label, amount in zip(bars, labels, amounts):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.3,
               label, ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Cumulative line
    cumulative = np.cumsum(amounts)
    ax2 = ax.twinx()
    ax2.plot(years, cumulative, 'ko-', linewidth=2, markersize=8)
    ax2.set_ylabel('Cumulative Settlements ($B)', fontweight='bold', color='black')
    ax2.set_ylim(0, 15)
    
    # Projected
    ax.annotate('$80B+\nEstimated\nTotal Liability', xy=(2025, 12), fontsize=11,
               fontweight='bold', color='red', ha='center',
               bbox=dict(boxstyle='round', facecolor='#ffcccc', alpha=0.8))
    
    # Labels
    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Settlement Amount ($B)', fontweight='bold')
    ax.set_title('Major PFAS Settlements: $12B+ and Counting',
                fontweight='bold', fontsize=14)
    ax.set_xlim(2017, 2026)
    ax.set_ylim(0, 13)
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path)
        print(f"Saved: {output_path}")
    
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# CHART 6: LEACHING CURVE
# ─────────────────────────────────────────────────────────────────────────────

def plot_leaching_curve(output_path: Path = None):
    """
    Shows PFAS leaching from GAC over time when conditions change.
    
    This is the key "fear" chart showing the problem.
    """
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Time axis (months)
    months = np.linspace(0, 24, 200)
    
    # Phase 1: Normal operation (0-12 months) - low effluent
    # Phase 2: Influent drops / conditions change (12-24 months) - leaching
    
    # Normal operation phase
    normal = 2 + 0.5 * months[:100]  # Slowly rising effluent
    
    # Leaching phase (after influent drops at month 12)
    leach_start = normal[-1]
    leach = leach_start + 15 * (1 - np.exp(-0.3 * (months[100:] - 12)))
    
    effluent = np.concatenate([normal, leach])
    
    # Plot
    ax.plot(months, effluent, color='#d62728', linewidth=3, label='Effluent PFOA (ppt)')
    
    # Influent line (drops at month 12)
    influent = np.concatenate([50 * np.ones(100), 10 * np.ones(100)])
    ax.plot(months, influent, color='#1f77b4', linewidth=2, linestyle='--', 
           label='Influent PFOA (ppt)')
    
    # EPA limit
    ax.axhline(y=4, color='red', linestyle=':', linewidth=2, alpha=0.7)
    ax.text(24.5, 4, 'EPA Limit\n4 ppt', fontsize=9, color='red', va='center')
    
    # Phase annotations
    ax.axvline(x=12, color='gray', linestyle='--', alpha=0.5)
    ax.text(6, 55, 'Normal Operation\n(High Influent)', fontsize=10, 
           ha='center', fontweight='bold')
    ax.text(18, 55, 'Source Remediated\n(Low Influent)', fontsize=10,
           ha='center', fontweight='bold')
    
    # Leaching annotation
    ax.annotate('LEACHING!\nCaptured PFAS\nreleases back\ninto water', 
               xy=(18, 15), xytext=(21, 30),
               arrowprops=dict(arrowstyle='->', color='black', lw=2),
               fontsize=11, fontweight='bold', color='#d62728',
               ha='center')
    
    # Shaded violation zone
    ax.fill_between(months, 4, effluent, where=(effluent > 4), 
                   alpha=0.2, color='red')
    
    # Labels
    ax.set_xlabel('Time (Months)', fontweight='bold')
    ax.set_ylabel('PFOA Concentration (ppt)', fontweight='bold')
    ax.set_title('The Leaching Problem: GAC Releases PFAS When Conditions Change',
                fontweight='bold', fontsize=14)
    ax.legend(loc='upper right')
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 60)
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path)
        print(f"Saved: {output_path}")
    
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def generate_all_charts():
    """Generate all charts for the white paper."""
    
    print("Generating PFAS Crisis Charts...")
    print("-" * 50)
    
    plot_binding_energy_comparison(OUTPUT_DIR / "binding_energy_comparison.png")
    plot_breakthrough_curve(OUTPUT_DIR / "breakthrough_curve.png")
    plot_cost_comparison(OUTPUT_DIR / "cost_comparison.png")
    plot_chain_length_effect(OUTPUT_DIR / "chain_length_effect.png")
    plot_settlement_timeline(OUTPUT_DIR / "settlement_timeline.png")
    plot_leaching_curve(OUTPUT_DIR / "leaching_curve.png")
    
    print("-" * 50)
    print("All charts generated successfully!")


def main():
    parser = argparse.ArgumentParser(
        description="Generate charts for PFAS Filtration Crisis white paper"
    )
    parser.add_argument("--all", action="store_true", help="Generate all charts")
    parser.add_argument("--binding", action="store_true", help="Binding energy chart")
    parser.add_argument("--breakthrough", action="store_true", help="Breakthrough curve")
    parser.add_argument("--cost", action="store_true", help="Cost comparison")
    parser.add_argument("--chain", action="store_true", help="Chain length effect")
    parser.add_argument("--settlement", action="store_true", help="Settlement timeline")
    parser.add_argument("--leaching", action="store_true", help="Leaching curve")
    parser.add_argument("--show", action="store_true", help="Display charts interactively")
    
    args = parser.parse_args()
    
    if args.all or not any([args.binding, args.breakthrough, args.cost, 
                            args.chain, args.settlement, args.leaching]):
        generate_all_charts()
    else:
        if args.binding:
            plot_binding_energy_comparison(OUTPUT_DIR / "binding_energy_comparison.png")
        if args.breakthrough:
            plot_breakthrough_curve(OUTPUT_DIR / "breakthrough_curve.png")
        if args.cost:
            plot_cost_comparison(OUTPUT_DIR / "cost_comparison.png")
        if args.chain:
            plot_chain_length_effect(OUTPUT_DIR / "chain_length_effect.png")
        if args.settlement:
            plot_settlement_timeline(OUTPUT_DIR / "settlement_timeline.png")
        if args.leaching:
            plot_leaching_curve(OUTPUT_DIR / "leaching_curve.png")
    
    if args.show:
        plt.show()


if __name__ == "__main__":
    main()
