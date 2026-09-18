# Practical BEV Traction-Motor Architecture, Weight and Materials Outlook
*Matthias Roesslein — September 09, 2026*

## Executive Summary

Permanent-magnet synchronous motors remain the practical reference architecture for battery-electric passenger vehicles because they combine high efficiency, compact packaging and high power density. Public sources place permanent-magnet penetration at roughly 85–above 90% of marketed or installed electrified-vehicle applications, depending on vehicle scope and counting method [[1]](https://www.iea.org/reports/the-role-of-critical-minerals-in-clean-energy-transitions/mineral-requirements-for-clean-energy-transitions) [[2]](https://www.idtechex.com/en/research-article/enabling-lower-cost-evs-through-electric-motor-development/31694). This dominance is likely to erode gradually rather than disappear: electrically excited synchronous motors, induction machines and axial-flux designs each solve a specific problem, but none is a universal replacement.

For programme planning, a 150 kW-class radial IPM/PMSM should be treated as a 55–72–90 kg motor-only envelope, corresponding to approximately 1.7–2.1–2.7 kW/kg. A reasonable NdFeB planning allowance is 1.0–1.5–2.0 kg. These are internet-sourced bounded engineering ranges anchored by public OEM, product, drive-unit and technology evidence—not independently weighed OEM bills of material.

Public evidence does not disclose complete, independently weighed component bills of material for Volkswagen MEB/APP550, Hyundai E-GMP, BYD e-Platform 3.0, the Tesla Model 3 rear motor and Renault traction motors. Published drive-unit masses also cannot be treated as motor masses because boundaries may include the inverter, gearbox, differential, lubrication hardware and controls. The component tables in this report therefore support early sourcing, cost and material-risk work, not final design release.

Three practical scenarios emerge:

- **Scenario A—improved radial IPM:** Retain the dominant architecture while reducing steel, copper, magnet and housing intensity. At constant 150 kW-class output, motor mass could move from 55–72–90 kg in the 2025 planning row toward 44–57–72 kg in the 2040 row.
- **Scenario B—EESM substitution:** Eliminate traction-magnet exposure but accept an estimated 4–8–15 kg motor-mass increase, 3–6–10 kg of additional rotor-winding copper and a highway-speed efficiency difference spanning −1.5–−0.5–+0.5 percentage points relative to a comparable IPM. The range crosses zero because published comparisons do not agree on the high-speed winner [[3]](https://mdpi.com/1996-1073/19/17/3960) [[4]](https://mdpi.com/1996-1073/18/14/3673).
- **Scenario C—axial flux:** Pursue a potential 10–20–30% motor-weight saving, equivalent to approximately 7–14–24 kg at the 150 kW class. Commercial potential is credible, but production scale, thermal boundaries and manufacturing complexity make adoption more uncertain than radial-IPM improvement [[5]](https://www.sciencedirect.com/science/article/pii/S0306261923018603) [[6]](https://www.sciencedirect.com/science/article/pii/S2773186324000963) [[7]](https://www.sciencedirect.com/science/article/pii/S1110016821004300).

The decision is therefore not “which motor wins globally?” It is “which architecture best fits each vehicle’s efficiency duty, package, material-risk and manufacturing boundary?” Radial IPM remains the lowest-disruption baseline; EESM is the clearest rare-earth hedge; axial flux is the higher-upside, higher-execution-risk option.

## Introductory Method Note

Every engineering, material and market result is expressed as **Min | Typical | Max**. In prose, the same triplets use en-dash syntax—for example, 55–72–90 kg. The middle value is a planning centre, not a measured universal average.

The ranges reflect variation across OEM designs, peak versus continuous duty ratings, cooling systems, voltage and speed boundaries, motor-only versus drive-unit definitions, vehicle segments, manufacturing maturity and analyst projections. They are intended to expose uncertainty rather than create false precision.

Three evidence classes are used:

1. **Direct public facts:** OEM architecture descriptions, published product characteristics and explicitly reported market direction.
2. **Internet-derived bounded engineering ranges:** Report estimates anchored by public motor, drive-unit, materials and system evidence where complete component measurements are unavailable.
3. **Report scenario bands:** Transparent low–base–high planning cases bounded by published technology direction. They are not represented as analyst consensus.

Component minima and maxima are not mechanically summed to create motor totals. Lightweight choices in one component can require heavier cooling or structure elsewhere, while maximum assumptions may be mutually incompatible. Total-motor ranges are therefore independent system-level envelopes.

## 1. Architecture Mix

### 1.1 Current Market Position

The IEA reports permanent-magnet synchronous motors in more than 90% of currently marketed EVs, while IDTechEx places PM motors at approximately 85% of the battery-electric and plug-in-hybrid car market in its stated scope [[1]](https://www.iea.org/reports/the-role-of-critical-minerals-in-clean-energy-transitions/mineral-requirements-for-clean-energy-transitions) [[2]](https://www.idtechex.com/en/research-article/enabling-lower-cost-evs-through-electric-motor-development/31694). The difference is better understood as a boundary and classification issue than a direct contradiction.

The following table converts that public evidence into a mutually exclusive primary-motor classification. Axial-flux motors are counted separately even when they use permanent magnets; this prevents double counting with radial IPM.

| Primary architecture | Min share | Typical share | Max share |
|---|---:|---:|---:|
| Radial IPM/PMSM | 78% | 85% | 92% |
| EESM/WRSM | 4% | 7% | 10% |
| Induction | 3% | 6% | 10% |
| Axial flux | 0% | 1% | 2% |

The individual limits are uncertainty bands and need not sum to the same total. The typical column is normalized approximately, while the minima and maxima represent alternative classification and market-scope boundaries.

### 1.2 Architecture Scenario Bands

Public architecture-by-installed-motor datasets are incomplete, and long-horizon forecasts rarely provide directly comparable shares for IPM, EESM, induction and axial flux. The bands below are therefore report scenarios bounded by published direction, including continued PM dominance, expanding magnet-free designs and gradual axial-flux commercialization [[2]](https://www.idtechex.com/en/research-article/enabling-lower-cost-evs-through-electric-motor-development/31694) [[8]](https://www.idtechex.com/en/research-article/the-evolution-of-modern-electric-motor-market-for-electric-vehicles/29506) [[9]](https://www.idtechex.com/en/research-article/emerging-electric-motor-technologies-for-the-ev-market/24839).

| Year | Architecture | Min share | Typical share | Max share |
|---|---|---:|---:|---:|
| 2030 | Radial IPM/PMSM | 70% | 78% | 86% |
| 2030 | EESM/WRSM | 8% | 12% | 18% |
| 2030 | Induction | 4% | 7% | 11% |
| 2030 | Axial flux | 1% | 3% | 6% |
| 2035 | Radial IPM/PMSM | 55% | 68% | 78% |
| 2035 | EESM/WRSM | 14% | 20% | 27% |
| 2035 | Induction | 4% | 6% | 10% |
| 2035 | Axial flux | 2% | 6% | 12% |
| 2040 | Radial IPM/PMSM | 45% | 61% | 73% |
| 2040 | EESM/WRSM | 17% | 24% | 33% |
| 2040 | Induction | 3% | 6% | 10% |
| 2040 | Axial flux | 3% | 9% | 18% |

IDTechEx’s published direction places magnet-free automotive motors moving from approximately 9% in 2023 toward approximately 30% in 2035 [[2]](https://www.idtechex.com/en/research-article/enabling-lower-cost-evs-through-electric-motor-development/31694). The EESM and induction bands are consistent with that direction but should not be interpreted as a restatement of the source’s proprietary forecast.

## 2. Weight Reality

### 2.1 What Public OEM Evidence Does—and Does Not—Show

Volkswagen’s APP550 evidence establishes a higher-output permanent-magnet drive within the preceding package envelope, supported by revised windings, stronger magnets and pump-less oil distribution. It does not publish a complete motor-only bill of material.

Hyundai E-GMP integrates the motor, inverter and reduction gear and uses compact winding and cooling arrangements [[10]](https://chargedevs.com/features/a-closer-look-at-axial-flux-motors/). BYD emphasizes highly integrated electric-drive assemblies rather than independently weighed motor components [[11]](https://www.byd.com/en). The Tesla Model 3 rear drive unit has been reported at just under approximately 90 kg, but that boundary includes more than the bare motor [[12]](https://electrek.co/2025/12/02/yasa-record-setting-axial-flux-motor-in-wheel-powertrain-1000-bhp/). Renault publicly supports electrically excited motor development, but the supplied evidence does not provide a complete independently weighed production bill of material [[13]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[14]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/e7a-the-next-gen-electric-motor-developed-by-renault-and-valeo/).

Consequently, no named OEM product should be assigned the component values below as if they were direct teardown measurements.

### 2.2 150 kW-Class Radial IPM/PMSM Component Envelope

These values are internet-sourced bounded engineering ranges anchored by public OEM/product/system evidence and broader evidence on electrical steel, copper windings, NdFeB magnets, cooling and bearings [[15]](https://www.emobility-engineering.com/axial-flux-motors/) [[16]](https://www.emobility-engineering.com/motor-materials-electric-vehicles/). They do not claim direct teardowns where those are absent.

| Component or result | Unit | Min | Typical | Max |
|---|---|---:|---:|---:|
| Stator laminations | kg | 18.0 | 23.0 | 28.0 |
| Stator copper | kg | 8.0 | 11.0 | 14.0 |
| Rotor laminations | kg | 10.0 | 14.0 | 18.0 |
| NdFeB magnets | kg | 1.0 | 1.5 | 2.0 |
| Shaft | kg | 3.0 | 4.5 | 6.0 |
| Housing and end shields | kg | 8.0 | 12.0 | 17.0 |
| Bearings and seals | kg | 1.0 | 1.7 | 2.5 |
| Cooling hardware and retained fluid | kg | 2.0 | 4.0 | 7.0 |
| Sensors and resolver | kg | 0.3 | 0.7 | 1.2 |
| Total motor weight | kg | 55 | 72 | 90 |
| Motor power density | kW/kg | 1.7 | 2.1 | 2.7 |

Thin insulated electrical-steel laminations reduce eddy-current losses, while copper remains the reference winding material because its conductivity supports compact packaging [[15]](https://www.emobility-engineering.com/axial-flux-motors/) [[16]](https://www.emobility-engineering.com/motor-materials-electric-vehicles/). Oil spray, water jackets and hollow-shaft approaches create materially different cooling masses and continuous-duty capability. That variability is one reason a single universal motor weight is misleading.

### 2.3 NdFeB Allowance by Power Class

Public evidence supports approximately 1–2 kg of NdFeB for common 100–150 kW passenger-vehicle motors and approximately 3–4 kg for some higher-performance or dual-motor applications. The wider planning bands below include topology and torque-density variation.

| Power class | Unit | Min | Typical | Max |
|---|---|---:|---:|---:|
| 75 kW | kg NdFeB | 0.4 | 0.7 | 1.0 |
| 150 kW | kg NdFeB | 1.0 | 1.5 | 2.0 |
| 250–400 kW | kg NdFeB | 2.0 | 3.5 | 5.0 |

The upper end of the 250–400 kW row is a planning extrapolation, not a disclosed production-motor measurement. High-speed designs, reluctance torque contribution and cooling can reduce magnet intensity; high-torque or dual-motor configurations can increase total installed magnet mass.

## 3. Three Practical Scenarios

### 3.1 Scenario A—Improved Radial IPM

Scenario A assumes continued radial-IPM development through thinner laminations, improved winding fill, better thermal paths, reduced heavy-rare-earth content and structural integration. It is the least disruptive route because it retains the dominant electromagnetic architecture.

| Year | Result | Unit | Min | Typical | Max |
|---|---|---|---:|---:|---:|
| 2025 | Stator laminations | kg | 18.0 | 23.0 | 28.0 |
| 2025 | Stator copper | kg | 8.0 | 11.0 | 14.0 |
| 2025 | Rotor laminations | kg | 10.0 | 14.0 | 18.0 |
| 2025 | NdFeB | kg | 1.0 | 1.5 | 2.0 |
| 2025 | Mechanical and housing | kg | 20.0 | 29.7 | 43.0 |
| 2025 | Cooling and sensing | kg | 2.3 | 4.7 | 8.2 |
| 2025 | Total motor weight | kg | 55 | 72 | 90 |
| 2025 | Power density | kW/kg | 1.7 | 2.1 | 2.7 |
| 2030 | Stator laminations | kg | 17.0 | 21.5 | 26.0 |
| 2030 | Stator copper | kg | 7.5 | 10.0 | 13.0 |
| 2030 | Rotor laminations | kg | 9.5 | 13.0 | 17.0 |
| 2030 | NdFeB | kg | 0.8 | 1.3 | 1.8 |
| 2030 | Mechanical and housing | kg | 18.0 | 26.8 | 38.5 |
| 2030 | Cooling and sensing | kg | 2.1 | 4.1 | 7.0 |
| 2030 | Total motor weight | kg | 51 | 66 | 83 |
| 2030 | Power density | kW/kg | 1.8 | 2.3 | 2.9 |
| 2035 | Stator laminations | kg | 16.0 | 20.0 | 24.5 |
| 2035 | Stator copper | kg | 7.0 | 9.3 | 12.0 |
| 2035 | Rotor laminations | kg | 9.0 | 12.0 | 15.5 |
| 2035 | NdFeB | kg | 0.7 | 1.1 | 1.6 |
| 2035 | Mechanical and housing | kg | 16.5 | 24.5 | 35.0 |
| 2035 | Cooling and sensing | kg | 1.9 | 3.7 | 6.3 |
| 2035 | Total motor weight | kg | 47 | 61 | 77 |
| 2035 | Power density | kW/kg | 1.9 | 2.5 | 3.2 |
| 2040 | Stator laminations | kg | 15.0 | 18.8 | 23.0 |
| 2040 | Stator copper | kg | 6.5 | 8.7 | 11.0 |
| 2040 | Rotor laminations | kg | 8.5 | 11.2 | 14.5 |
| 2040 | NdFeB | kg | 0.6 | 1.0 | 1.5 |
| 2040 | Mechanical and housing | kg | 15.0 | 22.5 | 32.5 |
| 2040 | Cooling and sensing | kg | 1.7 | 3.3 | 5.8 |
| 2040 | Total motor weight | kg | 44 | 57 | 72 |
| 2040 | Power density | kW/kg | 2.1 | 2.6 | 3.4 |

The scenario is not a forecast that every component improves simultaneously. Thermal durability, noise, rotor containment and manufacturing yield may constrain the lower-weight combinations.

### 3.2 Scenario B—EESM Versus IPM

EESM removes the permanent magnets and adds an actively excited rotor. Published studies agree on the rare-earth benefit but disagree on relative efficiency: optimized IPM generally leads in power density, while some EESM studies show competitive or superior high-speed operation [[17]](https://www.mdpi.com/1996-1073/11/10/2601) [[18]](https://mdpi.com/1996-1073/16/3/1306) [[3]](https://mdpi.com/1996-1073/19/17/3960) [[4]](https://mdpi.com/1996-1073/18/14/3673) [[19]](https://mdpi.com/1996-1073/16/4/1657).

| EESM result relative to comparable IPM | Unit | Min | Typical | Max |
|---|---|---:|---:|---:|
| Motor-mass difference | kg | +4 | +8 | +15 |
| Additional rotor-winding copper | kg | 3 | 6 | 10 |
| Highway-speed efficiency difference | percentage points | −1.5 | −0.5 | +0.5 |
| NdFeB reduction | kg | 1.0 | 1.5 | 2.0 |

| Year | EESM market share | Min | Typical | Max |
|---|---|---:|---:|---:|
| 2030 | Share | 8% | 12% | 18% |
| 2035 | Share | 14% | 20% | 27% |
| 2040 | Share | 17% | 24% | 33% |

EESM should be evaluated on total vehicle value, not magnet avoidance alone. Rotor excitation, cooling, controls and manufacturing complexity can offset part of the material-risk advantage [[20]](https://mdpi.com/2079-9292/9/7/1096/htm) [[17]](https://www.mdpi.com/1996-1073/11/10/2601) [[19]](https://mdpi.com/1996-1073/16/4/1657).

### 3.3 Scenario C—Axial Flux Versus Radial Flux

Axial-flux machines offer a short axial package and potentially higher torque and power density, especially in dual-rotor arrangements. Literature supports the directional advantage but also identifies topology, air-gap and mechanical-design dependence [[5]](https://www.sciencedirect.com/science/article/pii/S0306261923018603) [[6]](https://www.sciencedirect.com/science/article/pii/S2773186324000963) [[7]](https://www.sciencedirect.com/science/article/pii/S1110016821004300) [[21]](https://www.sciencedirect.com/science/article/pii/S1000936125006685).

| Axial-flux result relative to radial motor | Unit | Min | Typical | Max |
|---|---|---:|---:|---:|
| Weight saving | % | 10% | 20% | 30% |
| Weight saving at 150 kW class | kg | 7 | 14 | 24 |
| Production-oriented axial power density | kW/kg | 3.0 | 5.0 | 8.0 |
| Production-oriented radial power density | kW/kg | 1.7 | 2.1 | 2.7 |

| Year | Axial-flux market share | Min | Typical | Max |
|---|---|---:|---:|---:|
| 2030 | Share | 1% | 3% | 6% |
| 2035 | Share | 2% | 6% | 12% |
| 2040 | Share | 3% | 9% | 18% |

The density comparison is boundary-sensitive. Published prototype or supplier claims should not be compared with a fully validated radial production motor unless cooling, inverter, gearbox, continuous duty and housing boundaries match [[22]](https://yasa.com/technology/) [[23]](https://www.magnax.com/) [[24]](https://yasa.com/) [[25]](https://www.magnax.com/magnax-blog/a-new-generation-of-axial-flux-ev-motors).

## 4. Constant-Output Evolution and Scaling

Power does not scale linearly with motor mass. Torque requirement, speed, cooling, electromagnetic loading and durability boundaries alter the result. The table provides a radial-IPM planning envelope rather than a sizing equation.

| Rated power identifier | Result | Unit | Min | Typical | Max |
|---|---|---|---:|---:|---:|
| 75 kW | Total motor weight | kg | 35 | 45 | 58 |
| 75 kW | Power density | kW/kg | 1.3 | 1.7 | 2.1 |
| 75 kW | NdFeB | kg | 0.4 | 0.7 | 1.0 |
| 100 kW | Total motor weight | kg | 42 | 54 | 68 |
| 100 kW | Power density | kW/kg | 1.5 | 1.9 | 2.4 |
| 100 kW | NdFeB | kg | 0.7 | 1.1 | 1.5 |
| 150 kW | Total motor weight | kg | 55 | 72 | 90 |
| 150 kW | Power density | kW/kg | 1.7 | 2.1 | 2.7 |
| 150 kW | NdFeB | kg | 1.0 | 1.5 | 2.0 |
| 200 kW | Total motor weight | kg | 68 | 88 | 110 |
| 200 kW | Power density | kW/kg | 1.8 | 2.3 | 2.9 |
| 200 kW | NdFeB | kg | 1.4 | 2.1 | 2.8 |
| 250 kW | Total motor weight | kg | 80 | 105 | 132 |
| 250 kW | Power density | kW/kg | 1.9 | 2.4 | 3.1 |
| 250 kW | NdFeB | kg | 1.8 | 2.7 | 3.6 |
| 350 kW | Total motor weight | kg | 105 | 142 | 185 |
| 350 kW | Power density | kW/kg | 1.9 | 2.5 | 3.3 |
| 350 kW | NdFeB | kg | 2.5 | 3.8 | 5.0 |
| 400 kW | Total motor weight | kg | 118 | 160 | 210 |
| 400 kW | Power density | kW/kg | 1.9 | 2.5 | 3.4 |
| 400 kW | NdFeB | kg | 2.8 | 4.3 | 5.8 |

The higher-power rows are increasingly sensitive to whether output comes from one machine or multiple motors. They should not be used to infer a disclosed magnet mass for any named product.

## 5. Material Dependency

### 5.1 Heavy Rare Earths and Grain-Boundary Diffusion

NdFeB provides high magnetic energy density, but coercivity falls as temperature rises. Dy and Tb can improve high-temperature resistance to demagnetization. Traditional heavy-rare-earth additions span approximately 2–8 wt.% and can extend toward approximately 8–11 wt.% in demanding designs, while grain-boundary diffusion concentrates heavy rare earths near grain boundaries rather than through the entire magnet [[26]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8183520/) [[27]](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/adem.202400234).

| Magnet-chemistry parameter | Unit | Min | Typical | Max |
|---|---|---:|---:|---:|
| Dy content of magnet weight | % | 0.5% | 3.0% | 8.0% |
| Tb content of magnet weight | % | 0.0% | 0.5% | 2.0% |
| 2030 GBD Dy-reduction versus bulk-alloy route | % | 50% | 60% | 70% |

The 2030 row is a report planning range based on published GBD heavy-rare-earth savings of approximately 50–70%, not a guaranteed industry-wide Dy outcome [[27]](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/adem.202400234) [[28]](https://www.sciencedirect.com/science/article/pii/S0304885323011253). Diffusion depth and magnet dimensions limit applicability.

### 5.2 Critical Materials for a 150 kW-Class IPM

The rare-earth rows represent elemental mass within the magnet allowance; they are not additional to NdFeB magnet mass. Copper includes stator conductors and connections. Silicon is the alloying element represented within electrical steel, while aluminum is concentrated in housings and thermal structures.

| Critical material | Unit | Min | Typical | Max |
|---|---|---:|---:|---:|
| Neodymium, Nd | kg | 0.25 | 0.38 | 0.55 |
| Praseodymium, Pr | kg | 0.03 | 0.08 | 0.15 |
| Dysprosium, Dy | kg | 0.01 | 0.05 | 0.12 |
| Terbium, Tb | kg | 0.00 | 0.01 | 0.03 |
| Copper, Cu | kg | 8.0 | 11.0 | 14.0 |
| Silicon, Si | kg | 0.5 | 1.0 | 1.8 |
| Aluminum, Al | kg | 8.0 | 12.0 | 17.0 |

The key sourcing distinction is concentration, not only mass. Copper, silicon and aluminum occur in larger quantities, but Dy and Tb may create disproportionate exposure because they are specialized additions to already supply-sensitive permanent magnets [[29]](https://www.iea.org/reports/the-role-of-critical-minerals-in-clean-energy-transitions/executive-summary) [[1]](https://www.iea.org/reports/the-role-of-critical-minerals-in-clean-energy-transitions/mineral-requirements-for-clean-energy-transitions).

## 6. OEM Strategy Implications

### 6.1 Radial-IPM Development Remains Active

Volkswagen’s APP550 direction demonstrates that radial permanent-magnet systems still have substantial development room through winding, magnet, inverter and cooling changes without requiring a new package. Hyundai E-GMP similarly emphasizes an integrated motor, inverter and reduction gear with compact windings and thermal management [[10]](https://chargedevs.com/features/a-closer-look-at-axial-flux-motors/).

Tesla’s Model 3 rear architecture confirms the production relevance of IPM combined with integrated oil cooling, while its reported drive-unit mass must not be substituted for motor-only mass [[12]](https://electrek.co/2025/12/02/yasa-record-setting-axial-flux-motor-in-wheel-powertrain-1000-bhp/). BYD’s e-Platform strategy emphasizes multi-function integration and system efficiency rather than publication of a separately weighed traction motor [[11]](https://www.byd.com/en).

### 6.2 EESM Is a Strategic Supply-Chain Choice

Renault public material supports electrically excited traction-machine development [[13]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[14]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/e7a-the-next-gen-electric-motor-developed-by-renault-and-valeo/). BMW public communications likewise support current-excited synchronous-machine strategy [[30]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en) [[31]](https://www.bmwgroup.com/en/company/neue-klasse/details-antrieb-der-6--generation.html). These choices show that magnet-free propulsion is a production strategy rather than only a research concept.

The trade is not free: EESM replaces permanent-magnet exposure with rotor copper, excitation hardware, thermal demand and manufacturing complexity. It is most compelling where rare-earth resilience, adjustable field control or high-speed operation outweigh the mass and complexity penalty [[3]](https://mdpi.com/1996-1073/19/17/3960) [[4]](https://mdpi.com/1996-1073/18/14/3673) [[19]](https://mdpi.com/1996-1073/16/4/1657).

### 6.3 Axial Flux Is a Targeted Packaging and Density Bet

IDTechEx identifies axial flux as a growing but currently small segment, especially relevant to high-performance and hybrid applications [[8]](https://www.idtechex.com/en/research-article/the-evolution-of-modern-electric-motor-market-for-electric-vehicles/29506) [[9]](https://www.idtechex.com/en/research-article/emerging-electric-motor-technologies-for-the-ev-market/24839). Mercedes-Benz’s relationship with YASA provides a visible OEM pathway for industrialization [[32]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) [[33]](https://yasa.com/news/concept-amg-gt-xx-a-new-dimension-of-performance/).

Axial flux should initially be treated as a targeted platform option rather than a universal radial replacement. Its value is highest where package thickness, mass and torque density justify manufacturing and validation risk.

## 7. Composite Outlook to 2050

The long-term outlook should remain conservative. Evidence supports diversification away from near-total PM dominance, but it does not justify assuming rapid elimination of radial IPM or unrestricted axial-flux growth. The 2050 bands are deliberately broad because public long-horizon architecture forecasts are incomplete.

| Year | Architecture | Min share | Typical share | Max share |
|---|---|---:|---:|---:|
| 2040 | Radial IPM/PMSM | 45% | 61% | 73% |
| 2040 | EESM/WRSM | 17% | 24% | 33% |
| 2040 | Induction | 3% | 6% | 10% |
| 2040 | Axial flux | 3% | 9% | 18% |
| 2045 | Radial IPM/PMSM | 41% | 57% | 70% |
| 2045 | EESM/WRSM | 18% | 26% | 36% |
| 2045 | Induction | 3% | 6% | 10% |
| 2045 | Axial flux | 4% | 11% | 21% |
| 2050 | Radial IPM/PMSM | 38% | 54% | 68% |
| 2050 | EESM/WRSM | 18% | 27% | 38% |
| 2050 | Induction | 3% | 6% | 10% |
| 2050 | Axial flux | 5% | 13% | 24% |

The bands are architecture scenarios, not analyst consensus. They assume continued radial-IPM competitiveness, measured expansion of EESM, a durable but bounded induction niche and gradual axial-flux scaling. Faster rare-earth diversification would push outcomes toward the lower IPM and higher EESM limits; superior magnet processing and recycling would support the higher IPM limits.

## Data Confidence and Use in Excel

### Evidence Confidence

| Data group | Confidence | Min interpretation | Typical interpretation | Max interpretation |
|---|---|---|---|---|
| Public OEM architecture | High | Confirmed topology | Confirmed system direction | Confirmed qualitative strategy |
| Named-product component masses | Low | Sparse public disclosure | Engineering reconstruction | Boundary-sensitive estimate |
| 150 kW motor total mass | Medium | Aggressive lightweight design | Mainstream planning case | Conservative duty/package case |
| NdFeB mass | Medium | Magnet-efficient design | Common IPM allowance | High-torque or conservative allowance |
| EESM comparison | Medium | Optimized EESM case | Programme-planning case | Cooling and complexity penalty |
| Axial-flux comparison | Low–medium | Production-constrained case | Scaled supplier case | High-performance boundary |
| Current architecture share | Medium | Narrow classification | Central market scope | Broad marketed-vehicle scope |
| 2030–2050 shares | Low | Low-adoption scenario | Base scenario | High-adoption scenario |

### Excel Handling Rules

Each table should be imported with separate Min, Typical and Max fields. Do not replace the triplets with an unlabelled average.

For component costing, multiply each mass column by a matching low, central or high material-price assumption. Do not combine minimum mass with maximum performance unless the design basis explicitly supports that combination.

For sensitivity analysis:

- Use **Typical** for the programme baseline.
- Use **Min** for an aggressive mass or material-intensity case.
- Use **Max** for a conservative thermal, structural or sourcing case.
- Keep motor-only and drive-unit boundaries in separate worksheets.
- Flag OEM-product rows as public facts or bounded estimates.
- Treat market-share bands as independent scenarios rather than statistical confidence intervals.
- Preserve zero-valued material minima where an element can be intentionally omitted.
- Avoid summing independent component maxima into a claimed physical motor unless compatibility has been checked.

## Decision-Oriented Takeaway

Use improved radial IPM as the baseline for near-term mainstream BEV programmes. It has the strongest production evidence, the lowest architecture disruption and the clearest route to incremental weight and efficiency gains.

Maintain an EESM derivative or validated sourcing option where rare-earth exposure is strategically material. Its 4–8–15 kg estimated mass penalty and 3–6–10 kg additional rotor-copper requirement should be evaluated against magnet-price volatility, supply security and duty-cycle efficiency.

Fund axial-flux work selectively where packaging or vehicle-level mass has high value. Do not book the full 10–20–30% potential weight saving until continuous-duty cooling, manufacturing yield and system boundaries have been demonstrated.

For a 150 kW-class radial IPM programme, begin planning with 55–72–90 kg total motor mass, 1.7–2.1–2.7 kW/kg power density and 1.0–1.5–2.0 kg NdFeB. Carry the full range through sourcing, cost, thermal and vehicle simulations until measured supplier data replaces the bounded engineering assumptions.

---

## References

1. <https://www.iea.org/reports/the-role-of-critical-minerals-in-clean-energy-transitions/mineral-requirements-for-clean-energy-transitions>
2. <https://www.idtechex.com/en/research-article/enabling-lower-cost-evs-through-electric-motor-development/31694>
3. <https://mdpi.com/1996-1073/19/17/3960>
4. <https://mdpi.com/1996-1073/18/14/3673>
5. <https://www.sciencedirect.com/science/article/pii/S0306261923018603>
6. <https://www.sciencedirect.com/science/article/pii/S2773186324000963>
7. <https://www.sciencedirect.com/science/article/pii/S1110016821004300>
8. <https://www.idtechex.com/en/research-article/the-evolution-of-modern-electric-motor-market-for-electric-vehicles/29506>
9. <https://www.idtechex.com/en/research-article/emerging-electric-motor-technologies-for-the-ev-market/24839>
10. <https://chargedevs.com/features/a-closer-look-at-axial-flux-motors/>
11. <https://www.byd.com/en>
12. <https://electrek.co/2025/12/02/yasa-record-setting-axial-flux-motor-in-wheel-powertrain-1000-bhp/>
13. <https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/>
14. <https://www.renaultgroup.com/en/magazine/energy-and-powertrains/e7a-the-next-gen-electric-motor-developed-by-renault-and-valeo/>
15. <https://www.emobility-engineering.com/axial-flux-motors/>
16. <https://www.emobility-engineering.com/motor-materials-electric-vehicles/>
17. <https://www.mdpi.com/1996-1073/11/10/2601>
18. <https://mdpi.com/1996-1073/16/3/1306>
19. <https://mdpi.com/1996-1073/16/4/1657>
20. <https://mdpi.com/2079-9292/9/7/1096/htm>
21. <https://www.sciencedirect.com/science/article/pii/S1000936125006685>
22. <https://yasa.com/technology/>
23. <https://www.magnax.com/>
24. <https://yasa.com/>
25. <https://www.magnax.com/magnax-blog/a-new-generation-of-axial-flux-ev-motors>
26. <https://pmc.ncbi.nlm.nih.gov/articles/PMC8183520/>
27. <https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/adem.202400234>
28. <https://www.sciencedirect.com/science/article/pii/S0304885323011253>
29. <https://www.iea.org/reports/the-role-of-critical-minerals-in-clean-energy-transitions/executive-summary>
30. <https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en>
31. <https://www.bmwgroup.com/en/company/neue-klasse/details-antrieb-der-6--generation.html>
32. <https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html>
33. <https://yasa.com/news/concept-amg-gt-xx-a-new-dimension-of-performance/>
