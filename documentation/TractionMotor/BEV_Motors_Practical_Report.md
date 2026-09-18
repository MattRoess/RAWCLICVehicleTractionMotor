# BEV Traction Motors: Current Dominance, Weight Reality & Pragmatic Development Scenarios to 2050
*Matthias Roesslein — September 09, 2026*

## Executive Summary

Interior permanent-magnet synchronous motors— including permanent-magnet-assisted reluctance variants—remain the default passenger-BEV traction architecture. Public market studies indicate that permanent-magnet motors maintained more than 75% share during 2015–2024, but no public source provides a complete global passenger-BEV architecture-by-installed-unit dataset [[1]](https://www.idtechex.com/en/research-report/electric-motors-for-electric-vehicles/1131) [[2]](https://www.idtechex.com/en/research-report/electric-motors/1031). This report therefore estimates the 2025 installed-motor mix at **78% radial IPM/PMSR, 10% EESM/WRSM, 10% induction, 0.5% axial flux and 1.5% SRM/other**. These are triangulated estimates, not reported market statistics.

IPM dominates because it combines magnetic and reluctance torque, high efficiency and high power density in a compact package [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) [[4]](https://www.mdpi.com/1996-1073/17/23/5861). It is established across Tesla rear axles, Volkswagen MEB, Hyundai E-GMP and GM Ultium applications [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/). Its strategic weakness is dependence on NdFeB magnets: China accounted for 94% of global sintered permanent-magnet production in 2024, while magnet-rare-earth demand is projected to rise by approximately one-third by 2030 [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary). Reducing heavy rare earths, qualifying diversified magnet supply and designing recoverable rotors are therefore immediate priorities.

A representative **150 kW radial IPM motor-only** model weighs **25.0 kg**, equivalent to **6.0 kW/kg**. This sits within the cited 5–8 kW/kg range for contemporary production-oriented traction motors [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/). Because available public evidence does not disclose a complete component-by-component production bill of materials, the report’s row-level allocation is explicitly an engineering model: 10.8 kg electrical steel, 5.5 kg copper, 1.5 kg NdFeB magnets and 7.2 kg housing, shaft, bearings, insulation and cooling-related motor hardware. It excludes inverter, gearbox, differential, external cables and drive-unit fluids.

Three pragmatic pathways are evaluated:

- **Scenario A—optimized radial IPM:** lowest industrial disruption and the likely volume path. The model reduces a constant-output 150 kW motor from 25.0 kg in 2025 to 22.3 kg in 2030 and 19.7 kg in 2040, while cutting NdFeB from 1.50 kg to 1.00 kg.
- **Scenario B—EESM/WRSM rise:** strongest hedge against magnet concentration. BMW already uses rare-earth-free electrically excited synchronous motors, while Renault has a long production history with wound-rotor machines [[6]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[7]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en) [[8]](https://www.press.bmwgroup.com/usa/article/detail/T0327877EN_US/the-bmw-ix-xdrive50-5th-generation-edrive-and-sustainability?language=en_US). Added rotor copper and excitation hardware constrain mass and manufacturing simplicity.
- **Scenario C—axial flux:** credible for premium, packaging-constrained and high-performance applications, but not yet a universal radial-motor replacement. Mercedes-Benz began large-scale production of YASA-derived axial-flux motors in Berlin in June 2026 for the Mercedes-AMG GT 4-Door programme [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) [[10]](https://media.mercedes-benz.com/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf). The 98-step manufacturing process illustrates both the architecture’s potential and its industrial complexity [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html).

The report’s pragmatic composite forecast keeps IPM largest through 2050, but its share declines from 78% in 2025 to 54% in 2050. EESM rises to 27%, axial flux to 10%, and induction/SRM/other collectively remain near 9%. These are strategic planning assumptions—not external forecasts.

**Decision implication:** protect the radial-IPM core programme, establish an EESM industrial option where magnet exposure is strategically unacceptable, and restrict axial-flux investment to applications where packaging or performance value can absorb specialized manufacturing cost.

---

## 1. Current Passenger-BEV Motor Architecture Mix

### 1.1 Scope and estimation method

The unit of analysis is an **installed passenger-BEV traction motor**, not a vehicle. A dual-motor vehicle therefore contributes two installed machines, potentially of different architectures. Integrated drive-unit market values are not used as substitutes for motor-unit shares.

No identified public source reports a complete 2023–2025 global passenger-BEV architecture-by-installed-unit dataset. Available evidence instead establishes that permanent-magnet machines exceeded 75% of the broader EV traction-motor market through 2024 and identifies production applications for the principal alternatives [[1]](https://www.idtechex.com/en/research-report/electric-motors-for-electric-vehicles/1131) [[2]](https://www.idtechex.com/en/research-report/electric-motors/1031). The estimates below triangulate that market evidence with documented vehicle and axle applications. They should be used as rounded planning values.

**Table 1. Triangulated 2025 global passenger-BEV installed-motor mix**

| Motor architecture | 2025 share of installed motors | Estimate status | Production position |
|---|---:|---|---|
| Radial IPM/PMSM/PMSR | 78.0% | Triangulated estimate | Volume default |
| EESM/WRSM | 10.0% | Triangulated estimate | Established minority |
| Induction/asynchronous | 10.0% | Triangulated estimate | Mainly selected axles and mixed-topology AWD |
| Axial-flux PM | 0.5% | Triangulated estimate | Pre-volume niche in 2025 |
| SRM and other | 1.5% | Triangulated estimate | Marginal passenger-BEV role |
| **Total** | **100.0%** |  |  |

*Basis: PM motors held more than 75% share during 2015–2024; BMW and Renault provide established EESM production evidence, while axial flux and SRM remained niches [[1]](https://www.idtechex.com/en/research-report/electric-motors-for-electric-vehicles/1131) [[2]](https://www.idtechex.com/en/research-report/electric-motors/1031). Percentages are report estimates, not source-reported shares.*

### 1.2 Architecture position and real applications

**Table 2. Production status and credible passenger-BEV examples**

| Architecture | Why OEMs use it | Credible production passenger-BEV examples |
|---|---|---|
| Radial IPM/PMSM/PMSR | High efficiency and power density; combines magnetic and reluctance torque | Tesla Model 3 rear motor; Volkswagen MEB/APP550 applications; Hyundai E-GMP applications; GM Ultium applications [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) |
| EESM/WRSM | No permanent magnets; controllable rotor field; reduced exposure to Nd, Pr, Dy and Tb | BMW i4, i5, i7 and iX families; Renault Mégane E-Tech and Scénic E-Tech [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) [[6]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[7]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en) [[8]](https://www.press.bmwgroup.com/usa/article/detail/T0327877EN_US/the-bmw-ix-xdrive50-5th-generation-edrive-and-sustainability?language=en_US) |
| Induction/asynchronous | Magnet-free rotor; can be de-energized without permanent-magnet drag | Tesla front axle in certain dual-motor configurations [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/). Fewer current passenger-BEV examples are credibly established in the evidence; BMW Gen6 front-axle ASM is a future programme, not a 2025 example [[11]](https://www.press.bmwgroup.com/global/article/detail/T0448099EN/charge-faster-drive-further:-bmw-group-reveals-revolutionary-electric-drive-concept-with-800v-technology-for-the-neue-klasse?language=en) [[12]](https://www.press.bmwgroup.com/united-kingdom/article/detail/T0452406EN_GB/the-start-of-a-new-era-the-new-bmw-ix3?language=en_GB) |
| Axial-flux PM | Short axial package and high structural torque density | No credible 2023–2025 series passenger-BEV example is established in the evidence. McLaren Artura and Ferrari SF90 are hybrid applications and are therefore excluded [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/). Mercedes-AMG production begins in 2026 [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) |
| SRM | Magnet-free and no rotor winding; rugged rotor | No widespread series passenger-BEV application is established. Passenger-car use remains marginal because torque ripple, noise and control requirements offset rotor simplicity [[13]](https://chargedevs.com/features/a-closer-look-at-axial-flux-motors/) [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) |

Vehicle and axle classifications must not be conflated. Tesla, for example, may combine a permanent-magnet rear machine with an induction front machine in a dual-motor vehicle [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/). BMW’s forthcoming Gen6 strategy similarly combines an EESM with an asynchronous front motor in AWD configurations [[11]](https://www.press.bmwgroup.com/global/article/detail/T0448099EN/charge-faster-drive-further:-bmw-group-reveals-revolutionary-electric-drive-concept-with-800v-technology-for-the-neue-klasse?language=en) [[12]](https://www.press.bmwgroup.com/united-kingdom/article/detail/T0452406EN_GB/the-start-of-a-new-era-the-new-bmw-ix3?language=en_GB).

### 1.3 Why IPM remains dominant

IPM machines provide high torque and power density while exploiting both permanent-magnet and reluctance torque [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/). Their established tooling, supplier base and deployment across major global platforms lower industrialization risk relative to newer architectures.

The limiting strategic issue is not basic motor performance but magnet exposure. NdFeB enables a strong field in a small rotor volume, but the associated supply chain is highly concentrated [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary). Heavy-rare-earth grain-boundary diffusion can preserve high-temperature coercivity while reducing total Dy/Tb use [[14]](https://www.emobility-engineering.com/emotor-materials/).

### 1.4 Why induction is declining—and SRM is not replacing it

Induction motors avoid permanent magnets and can be attractive as a secondary axle that is frequently de-energized. However, lower power density and rotor losses make them less compelling than IPM for the primary high-utilization axle [[13]](https://chargedevs.com/features/a-closer-look-at-axial-flux-motors/) [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/). BMW’s planned use of an asynchronous motor on the Gen6 front axle illustrates a targeted supporting role rather than a wholesale return to induction [[11]](https://www.press.bmwgroup.com/global/article/detail/T0448099EN/charge-faster-drive-further:-bmw-group-reveals-revolutionary-electric-drive-concept-with-800v-technology-for-the-neue-klasse?language=en) [[12]](https://www.press.bmwgroup.com/united-kingdom/article/detail/T0452406EN_GB/the-start-of-a-new-era-the-new-bmw-ix3?language=en_GB).

SRM has an even smaller passenger-BEV position. Its magnet-free, winding-free rotor is simple, but torque ripple, acoustic noise and control complexity remain material passenger-car constraints [[13]](https://chargedevs.com/features/a-closer-look-at-axial-flux-motors/) [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/). The available evidence supports describing SRM as a strategic option under evaluation—not an established volume competitor.

---

## 2. The Weight Reality of a 125–150 kW Radial IPM Motor

### 2.1 Boundary and total-mass anchor

The reference machine is a **150 kW radial IPM traction motor only**. It excludes the inverter, reduction gearbox, differential, external high-voltage cables and drive-unit fluids.

Production-oriented traction motors are reported in a broad 5–8 kW/kg range [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/). A central **6.0 kW/kg** planning point gives a 25.0 kg reference motor:

**150 kW ÷ 25.0 kg = 6.0 kW/kg.**

The evidence reviewed does not provide a complete teardown with separately weighed laminations, copper, magnets, housing, shaft, bearings and insulation for one 125–150 kW production motor. The following is therefore a transparent, mass-balanced engineering allocation anchored to the cited total power-density range. It is not presented as a single OEM bill of materials.

### 2.2 Component mass allocation

**Table 3. Representative 150 kW radial IPM motor-only mass allocation**

| Component/material group | Mass, kg | Share of motor mass |
|---|---:|---:|
| Stator electrical-steel laminations | 7.00 | 28.0% |
| Rotor electrical-steel laminations | 3.80 | 15.2% |
| Stator copper windings and internal connections | 5.50 | 22.0% |
| NdFeB permanent magnets | 1.50 | 6.0% |
| Shaft and bearings | 2.20 | 8.8% |
| Housing and end shields | 4.00 | 16.0% |
| Insulation, resin, terminals and motor cooling sleeve/hardware | 1.00 | 4.0% |
| **Total motor only** | **25.00** | **100.0%** |

*Model basis: 6.0 kW/kg within the cited 5–8 kW/kg production-oriented range [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/). Hairpin windings, thinner electrical steel and improved cooling are established levers for power density, but the row values above are report allocations rather than disclosed OEM weights [[15]](https://www.mdpi.com/1996-1073/15/15/5431) [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/).*

Electrical steel represents the largest mass block, while copper dominates the non-ferrous active material. Magnet mass is strategically important despite being only 6% of the modeled motor because the Nd/Pr/Dy/Tb supply chain is highly concentrated [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary).

### 2.3 Reference-magnet composition

The 1.50 kg magnet allocation is modeled as sintered NdFeB containing:

- **29.0% Nd + Pr**
- **1.0% Dy + Tb**
- **70.0% Fe + B and minor balance**

This is a report composition basis, not a measured production magnet recipe. It reflects the identified use of Nd, Pr, Dy and Tb in high-performance permanent magnets and the industry direction toward localized heavy-rare-earth diffusion [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary) [[14]](https://www.emobility-engineering.com/emotor-materials/).

**Table 4. Modeled 2025 magnet composition in the reference IPM motor**

| Magnet constituent | Composition basis | Mass, kg |
|---|---:|---:|
| Nd + Pr | 29.0% | 0.435 |
| Dy + Tb | 1.0% | 0.015 |
| Fe + B and minor balance | 70.0% | 1.050 |
| **Total NdFeB magnet** | **100.0%** | **1.500** |

The report’s engineering target reduces Dy/Tb from **1.0% of magnet mass in 2025 to 0.3% in 2030**, primarily through magnet-temperature control, rotor optimization and grain-boundary diffusion. The target is a scenario assumption; the supporting industry direction is reduced heavy-rare-earth intensity rather than one universal composition specification [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary) [[14]](https://www.emobility-engineering.com/emotor-materials/).

### 2.4 Power-to-mass scaling points

Motor mass does not scale perfectly linearly: housing, bearing, cooling and rotor-speed requirements create architecture-specific discontinuities. The following points are normalized at the reference 6.0 kW/kg solely for early programme comparison.

**Table 5. Normalized radial-IPM motor-only scaling points**

| Peak motor output, kW | Status | Assumed power density, kW/kg | Calculated motor mass, kg |
|---:|---|---:|---:|
| 75 | Normalized representative point | 6.0 | 12.5 |
| 100 | Normalized representative point | 6.0 | 16.7 |
| 150 | Reference engineering point | 6.0 | 25.0 |
| 250 | Normalized representative point | 6.0 | 41.7 |
| 400 | Normalized representative point | 6.0 | 66.7 |

*All five rows are normalized report points, not actual vehicle teardown measurements. The common 6.0 kW/kg assumption lies within the cited 5–8 kW/kg production-oriented range [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/).*

For comparison, Renault’s E7A development target is 200 kW and 400 Nm, but no motor-only mass is disclosed in the available evidence; a kW/kg calculation would therefore be inappropriate [[6]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/). YASA has reported prototypes at 13.1 kg and 42 kW/kg and at 12.7 kg and 59 kW/kg, but these are prototype test figures rather than representative mass-production passenger-BEV anchors [[16]](https://yasa.com/) [[17]](https://carbuzz.com/yasa-axial-flux-motor-incredible-power-density/) [[18]](https://www.automotivemanufacturingsolutions.com/powertrain/yasa-industrialises-axial-flux-motor-production-under-mercedes-benz/2703254).

---

## 3. Three Pragmatic Development Scenarios

The following are **alternative report scenarios**, not external market forecasts. Every scenario begins from the same triangulated 2025 mix.

### 3.1 Scenario A—optimized radial IPM remains the volume core

Scenario A assumes OEMs prioritize existing manufacturing assets, vehicle efficiency and compact packaging while progressively reducing magnet intensity. Thin laminations, improved winding fill, direct oil cooling and higher-speed designs support mass reduction, although thermal durability and rotor mechanical stress remain constraints [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) [[14]](https://www.emobility-engineering.com/emotor-materials/).

**Table 6. Scenario A architecture shares, % of installed passenger-BEV motors**

| Year | IPM/PMSR | EESM/WRSM | Induction | Axial flux | SRM/other | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 2025 | 78 | 10 | 10 | 0.5 | 1.5 | 100 |
| 2030 | 78 | 12 | 7 | 1.5 | 1.5 | 100 |
| 2035 | 76 | 14 | 6 | 2.5 | 1.5 | 100 |
| 2040 | 73 | 16 | 5 | 4.0 | 2.0 | 100 |

*Report assumptions based on established PM dominance, continuing rare-earth-intensity reduction and the industrial maturity of radial machines [[1]](https://www.idtechex.com/en/research-report/electric-motors-for-electric-vehicles/1131) [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary) [[2]](https://www.idtechex.com/en/research-report/electric-motors/1031).*

**Conditions and milestones**

- By 2030: NdFeB mass falls from 1.50 kg to 1.25 kg per reference motor.
- By 2030: Dy/Tb target falls to 0.3% of magnet mass.
- By 2040: radial-IPM motor mass reaches 19.7 kg at constant 150 kW.
- Failure condition: sustained magnet unavailability or price volatility outweighs the cost of retooling for magnet-free architectures.

### 3.2 Scenario B—EESM/WRSM gains strategic scale

EESM replaces permanent magnets with an electrically excited rotor winding. The controllable field provides another efficiency-calibration variable but introduces rotor copper loss and excitation hardware [[13]](https://chargedevs.com/features/a-closer-look-at-axial-flux-motors/) [[6]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/). BMW Gen5 uses electrically excited synchronous motors without rare-earth magnets, and BMW Gen6 retains EESM while adding an asynchronous front machine in AWD vehicles [[7]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en) [[8]](https://www.press.bmwgroup.com/usa/article/detail/T0327877EN_US/the-bmw-ix-xdrive50-5th-generation-edrive-and-sustainability?language=en_US) [[11]](https://www.press.bmwgroup.com/global/article/detail/T0448099EN/charge-faster-drive-further:-bmw-group-reveals-revolutionary-electric-drive-concept-with-800v-technology-for-the-neue-klasse?language=en). Renault’s Mégane E-Tech, Scénic E-Tech and Alpine A290 use its second-generation EESM family [[6]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[19]](https://techplanet.today/post/renaults-rare-earth-free-electric-motors-a-strategic-shift-in-ev-technology-and-supply-chain-independence).

Renault’s official programme described E7A as a 200 kW, 800 V, 30%-more-compact third-generation motor planned for 2027 production [[6]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[20]](https://renaultgroup.com/en/magazine/energy-and-motorization/e7a-the-next-gen-electric-motor-developed-by-renault-and-valeo). Later reporting indicated that Renault ended part of the Valeo co-development arrangement and was evaluating alternative stator sourcing [[21]](https://www.reuters.com/business/autos-transportation/renault-seeking-chinese-rare-earth-free-motor-supplier-sources-say-2025-11-10/). The official specification is therefore best treated as a development intention whose sourcing and launch configuration require reconfirmation—not as an unconditional production commitment.

**Table 7. Scenario B architecture shares, % of installed passenger-BEV motors**

| Year | IPM/PMSR | EESM/WRSM | Induction | Axial flux | SRM/other | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 2025 | 78 | 10 | 10 | 0.5 | 1.5 | 100 |
| 2030 | 65 | 25 | 7 | 1.5 | 1.5 | 100 |
| 2035 | 52 | 36 | 7 | 3.0 | 2.0 | 100 |
| 2040 | 43 | 44 | 6 | 4.0 | 3.0 | 100 |

*Report assumptions based on demonstrated BMW and Renault production capability and concentrated magnet supply [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary) [[6]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[7]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en).*

In the mass model, a 2030 EESM contains **7.0 kg copper**, versus 5.1 kg in the optimized 2030 IPM, and weighs 25.3 kg versus 22.3 kg. The precise copper penalty depends on rotor excitation, cooling and power-transfer design. EESM has zero magnet procurement cost, but total motor-cost superiority cannot be asserted: savings vary with NdFeB prices, while added copper, rotor winding, excitation components and assembly complexity offset them. The evidence does not support a stable dollar-per-motor comparison.

**Conditions and milestones**

- Reliable high-volume rotor-winding and excitation processes.
- Rotor thermal management without unacceptable efficiency loss.
- Copper-price exposure managed alongside avoided magnet exposure.
- Platform-level efficiency remains competitive over representative duty cycles.

### 3.3 Scenario C—axial flux expands from premium applications

Axial-flux machines arrange the magnetic circuit in a disc-shaped layout, with two rotors surrounding a stator in the Mercedes/YASA design [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html). Their short axial length can create valuable packaging freedom, but precise air-gap control, cooling and specialized assembly complicate volume production [[22]](https://www.emobility-engineering.com/axial-flux-motors/) [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html).

Mercedes-Benz acquired YASA in 2021 and started large-scale production of axial-flux motors at Berlin-Marienfelde on June 9, 2026 for the Mercedes-AMG GT 4-Door programme [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) [[10]](https://media.mercedes-benz.com/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf). The plant uses approximately 30,000 m² across three halls and seven lines; production requires 98 process steps, including 65 new to Mercedes-Benz and 35 described as new worldwide [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) [[23]](https://group.mercedes-benz.com/company/production/production-network/mbdfc-humanoid-robots.html).

Mercedes states that its axial-flux design can use one-third of the space and weigh one-third as much as a conventional motor of equal output [[24]](https://group.mercedes-benz.com/technology/innovation/vision/vision-oneeleven.html). YASA separately describes motors up to 50% smaller and lighter than radial counterparts [[16]](https://yasa.com/) [[25]](https://yasa.com/news/concept-amg-gt-xx-a-new-dimension-of-performance/). These are supplier/OEM comparisons under their chosen boundaries—not a universal 30–50% industry rule. Prototype records of 42 and 59 kW/kg must not be applied directly to mass-production continuous-duty motors [[16]](https://yasa.com/) [[17]](https://carbuzz.com/yasa-axial-flux-motor-incredible-power-density/) [[18]](https://www.automotivemanufacturingsolutions.com/powertrain/yasa-industrialises-axial-flux-motor-production-under-mercedes-benz/2703254).

**Table 8. Scenario C architecture shares, % of installed passenger-BEV motors**

| Year | IPM/PMSR | EESM/WRSM | Induction | Axial flux | SRM/other | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 2025 | 78 | 10 | 10 | 0.5 | 1.5 | 100 |
| 2030 | 68 | 13 | 7 | 10 | 2 | 100 |
| 2035 | 55 | 15 | 6 | 21 | 3 | 100 |
| 2040 | 45 | 16 | 5 | 30 | 4 | 100 |

*Report assumptions. The high-share case requires manufacturing learning beyond the documented Mercedes-AMG premium programme [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html).*

Scenario C is conditional on automated stator manufacture, repeatable sub-0.1 mm assembly control, economical magnet use and demonstrated high-volume durability. A supplier agreement, minority investment or pilot line is not counted as a vehicle-production launch.

### 3.4 Correction of disputed application premises

The evidence supports BMW Gen5 as EESM technology and includes the iX family among BMW’s EESM applications [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) [[7]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en) [[8]](https://www.press.bmwgroup.com/usa/article/detail/T0327877EN_US/the-bmw-ix-xdrive50-5th-generation-edrive-and-sustainability?language=en_US). It does not provide sufficient axle-specific evidence to independently classify every iX front motor; that claim should not be generalized across all variants.

The available Mercedes evidence does not establish the EQS 450 rear motor as EESM. Consequently, this report does not use the EQS 450 as an EESM example. Mercedes’ confirmed axial-flux application is the later Mercedes-AMG GT 4-Door programme [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) [[10]](https://media.mercedes-benz.com/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf). No Audi PPE or SSP EESM decision is confirmed in the evidence and none is assumed.

---

## 4. Constant-Output Motor Weight Evolution

**Table 9. Mass-balanced 150 kW motor-only scenario model**

| Component or metric | 2025 IPM baseline | 2030 A: optimized IPM | 2040 A: optimized IPM | 2030 B: EESM | 2040 B: EESM | 2030 C: axial flux | 2040 C: axial flux |
|---|---:|---:|---:|---:|---:|---:|---:|
| Stator electrical steel, kg | 7.00 | 6.20 | 5.40 | 6.50 | 5.80 | 5.20 | 4.50 |
| Rotor electrical steel, kg | 3.80 | 3.40 | 3.00 | 4.40 | 4.00 | 2.80 | 2.40 |
| Total copper, kg | 5.50 | 5.10 | 4.70 | 7.00 | 6.50 | 5.20 | 4.80 |
| NdFeB magnets, kg | 1.50 | 1.25 | 1.00 | 0.00 | 0.00 | 1.80 | 1.50 |
| Housing and end shields, kg | 4.00 | 3.50 | 3.00 | 3.80 | 3.30 | 3.40 | 2.80 |
| Shaft, bearings and miscellaneous steel, kg | 2.20 | 2.05 | 1.90 | 2.40 | 2.20 | 1.80 | 1.60 |
| Insulation, resin, terminals and internal cooling hardware, kg | 1.00 | 0.80 | 0.70 | 1.20 | 1.00 | 1.00 | 0.80 |
| **Total motor mass, kg** | **25.00** | **22.30** | **19.70** | **25.30** | **22.80** | **21.20** | **18.40** |
| **Power density, kW/kg** | **6.00** | **6.73** | **7.61** | **5.93** | **6.58** | **7.08** | **8.15** |

*This is a report scenario model. Every architecture-year column is internally mass-balanced, uses a constant 150 kW output and applies the same motor-only boundary. Unlisted fasteners and minor ferrous parts are included in “shaft, bearings and miscellaneous steel.” EESM magnet mass is 0.00 kg by definition. The baseline is anchored to the cited 5–8 kW/kg production-oriented range [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/); future values are assumptions, not external forecasts.*

The modeled EESM remains heavier because replacing rotor magnets requires field copper and excitation-related structure. Axial flux receives a more conservative mass advantage than the strongest supplier claims because production boundaries and continuous ratings are not directly comparable [[16]](https://yasa.com/) [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) [[24]](https://group.mercedes-benz.com/technology/innovation/vision/vision-oneeleven.html).

---

## 5. Magnet and Material Dependency

### 5.1 Rare-earth intensity by scenario

**Table 10. Modeled magnet-material intensity per constant-output 150 kW motor**

| Scenario/year | NdFeB total, kg | Nd + Pr, kg | Dy + Tb, kg | Fe + B and balance, kg |
|---|---:|---:|---:|---:|
| A—IPM 2025 | 1.500 | 0.435 | 0.0150 | 1.050 |
| A—IPM 2030 | 1.250 | 0.363 | 0.0038 | 0.884 |
| A—IPM 2040 | 1.000 | 0.280 | 0.0010 | 0.719 |
| B—EESM 2025 | 0.000 | 0.000 | 0.0000 | 0.000 |
| B—EESM 2030 | 0.000 | 0.000 | 0.0000 | 0.000 |
| B—EESM 2040 | 0.000 | 0.000 | 0.0000 | 0.000 |
| C—axial flux 2025 representative | 2.000 | 0.580 | 0.0200 | 1.400 |
| C—axial flux 2030 | 1.800 | 0.522 | 0.0054 | 1.273 |
| C—axial flux 2040 | 1.500 | 0.420 | 0.0015 | 1.079 |

*Report model: 2025 composition is 29% Nd/Pr, 1% Dy/Tb and 70% balance; 2030 uses 29%, 0.3% and 70.7%; 2040 uses 28%, 0.1% and 71.9%. Totals may show 0.001 kg rounding differences. The direction—lower heavy-rare-earth intensity and alternative magnet-free motors—is consistent with the IEA’s demand-side risk-mitigation options [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary).*

Scenario B eliminates NdFeB but shifts material intensity toward copper. In the 2030 weight model, EESM uses 7.0 kg total copper against 5.1 kg for IPM. This 1.9 kg difference is a report assumption, not a universal architecture constant; the actual increment depends on excitation design, rotor current density and cooling.

### 5.2 Traffic-light dependency assessment

**Table 11. Material dependency and supply risk**

| Material | IPM | EESM | Axial flux PM | Supply-risk indication | Engineering response |
|---|---|---|---|---|---|
| Nd/Pr | Red | Green | Red | High concentration in permanent-magnet supply [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary) | Reduce magnet volume; dual-source magnets; recycling-ready rotor |
| Dy/Tb | Red | Green | Red | Very high strategic sensitivity despite low mass [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary) | Grain-boundary diffusion; lower magnet temperature [[14]](https://www.emobility-engineering.com/emotor-materials/) |
| Copper | Amber | Red | Amber | EESM adds rotor copper to stator copper | Optimize current density, winding fill and recovery |
| Electrical steel | Amber | Amber | Amber | Large mass fraction across radial architectures | Thin laminations and scrap-yield control |
| Specialized manufacturing | Green | Amber | Red | Axial-flux assembly requires new precision processes [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) | Pilot process capability before platform commitment |

*Colour words indicate relative architecture dependency and programme risk, not commodity-price forecasts.*

China’s 94% share of 2024 sintered permanent-magnet production makes supply qualification a board-level continuity issue, not merely a purchasing optimization [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary). Recycling could reduce primary rare-earth supply requirements by up to 35% by 2050, but meaningful end-of-life motor volumes emerge too late to replace near-term diversification [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary).

---

## 6. OEM Strategy Snapshot

**Table 12. Confirmed evidence and 2027–2030 direction**

| OEM | Current Motor Type | 2027–2030 Direction | Scenario Path | Key Programme |
|---|---|---|---|---|
| VW Group | IPM/PMSM on MEB applications | Next topology not publicly confirmed in the evidence | A | MEB APP550 [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) |
| Stellantis | Not publicly confirmed in the evidence | Not publicly confirmed | Not assigned | Not publicly disclosed |
| Renault-Nissan | Renault EESM/WRSM; Nissan classification not sufficiently confirmed | Renault officially targeted an 800 V, 200 kW E7A, but sourcing and partnership changes require reconfirmation | B | Mégane E-Tech, Scénic E-Tech; E7A development [[6]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[21]](https://www.reuters.com/business/autos-transportation/renault-seeking-chinese-rare-earth-free-motor-supplier-sources-say-2025-11-10/) [[20]](https://renaultgroup.com/en/magazine/energy-and-motorization/e7a-the-next-gen-electric-motor-developed-by-renault-and-valeo) |
| GM | IPM/PMSM represented in Ultium applications | Next topology not publicly confirmed | A | Ultium traction applications [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) |
| Ford | Not publicly confirmed in the evidence | Not publicly confirmed | Not assigned | Not publicly disclosed |
| Toyota | Not publicly confirmed in the evidence | Not publicly confirmed | Not assigned | Not publicly disclosed |
| Hyundai-Kia | IPM/PMSM represented on E-GMP | Next topology not publicly confirmed | A | E-GMP traction applications [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) |
| Mercedes | Current mainstream topology not sufficiently confirmed; axial flux entered production in 2026 for AMG | Scale YASA-derived axial flux in a premium performance programme | C | Mercedes-AMG GT 4-Door; Berlin-Marienfelde axial-flux production [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) [[10]](https://media.mercedes-benz.com/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf) |
| BMW | Gen5 EESM/WRSM | Gen6 EESM plus asynchronous front motor for AWD | B | Neue Klasse Gen6 eDrive [[7]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en) [[8]](https://www.press.bmwgroup.com/usa/article/detail/T0327877EN_US/the-bmw-ix-xdrive50-5th-generation-edrive-and-sustainability?language=en_US) [[11]](https://www.press.bmwgroup.com/global/article/detail/T0448099EN/charge-faster-drive-further:-bmw-group-reveals-revolutionary-electric-drive-concept-with-800v-technology-for-the-neue-klasse?language=en) [[12]](https://www.press.bmwgroup.com/united-kingdom/article/detail/T0452406EN_GB/the-start-of-a-new-era-the-new-bmw-ix3?language=en_GB) |
| BYD | Not publicly confirmed in the supplied evidence | Not publicly confirmed | Not assigned | Not publicly disclosed |
| Tesla | PM-assisted reluctance/IPM rear; induction on certain front axles | Rare-earth-free PM direction has been discussed, but a specific series application is not confirmed in the evidence | A with secondary induction | Model 3 rear motor and selected dual-motor front axle [[3]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) [[1]](https://www.idtechex.com/en/research-report/electric-motors-for-electric-vehicles/1131) [[26]](https://www.idtechex.com/en/research-report/electric-motors-for-evs/941) |

No motor-relevant OEM volume target is included because the available programme evidence does not provide sufficiently specific, comparable passenger-BEV motor-unit commitments. “Not publicly confirmed” is preferable to inferring architecture from a platform name, supplier agreement or general electrification target.

BMW offers the clearest confirmed mixed-topology strategy: EESM remains the high-utilization synchronous machine while asynchronous technology serves the front axle of Gen6 AWD configurations [[11]](https://www.press.bmwgroup.com/global/article/detail/T0448099EN/charge-faster-drive-further:-bmw-group-reveals-revolutionary-electric-drive-concept-with-800v-technology-for-the-neue-klasse?language=en) [[12]](https://www.press.bmwgroup.com/united-kingdom/article/detail/T0452406EN_GB/the-start-of-a-new-era-the-new-bmw-ix3?language=en_GB). Renault provides the longest documented EESM progression, but its E7A schedule and sourcing should be treated as a programme under revision because official development statements and subsequent reporting differ [[6]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[21]](https://www.reuters.com/business/autos-transportation/renault-seeking-chinese-rare-earth-free-motor-supplier-sources-say-2025-11-10/).

Mercedes provides the strongest confirmed axial-flux industrialization evidence. Its programme nevertheless begins in a high-performance AMG application with a specialized 98-step production process, not a mass-market compact BEV [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html).

---

## 7. Pragmatic Composite Outlook to 2050

The three preceding scenarios are alternatives intended to expose strategic choices. The following is the report’s **base/pragmatic composite forecast**: radial IPM remains largest, EESM gains steadily, axial flux scales selectively, and induction/SRM retain supporting niches.

**Table 13. Pragmatic global passenger-BEV installed-motor mix, 2025–2050**

| Year | IPM/PMSR | EESM/WRSM | Axial flux | Other: induction, SRM and remaining types | Total |
|---:|---:|---:|---:|---:|---:|
| 2025 | 78% | 10% | 0.5% | 11.5% | 100% |
| 2027 | 77% | 12% | 1% | 10% | 100% |
| 2030 | 73% | 16% | 2% | 9% | 100% |
| 2033 | 69% | 19% | 3% | 9% | 100% |
| 2035 | 66% | 21% | 4% | 9% | 100% |
| 2040 | 61% | 24% | 6% | 9% | 100% |
| 2045 | 57% | 26% | 8% | 9% | 100% |
| 2050 | 54% | 27% | 10% | 9% | 100% |

*Rounded report assumptions; intermediate years are directional milestones rather than claims of forecast precision. The basis is current PM share above 75%, demonstrated BMW/Renault EESM production, Mercedes axial-flux industrialization and continued rare-earth supply concentration [[1]](https://www.idtechex.com/en/research-report/electric-motors-for-electric-vehicles/1131) [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary) [[6]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) [[2]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[7]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en).*

### 7.1 Milestone interpretation

**2025–2030:** IPM optimization is the lowest-risk route. EESM adoption broadens where magnet avoidance is worth additional copper and rotor complexity. Axial flux remains concentrated in premium programmes.

**2030–2040:** architecture selection becomes more regional and application-specific. EESM is most competitive where magnet security carries a high strategic premium. Axial flux expands only if manufacturing yield, air-gap control and thermal durability move beyond specialized lines.

**2040–2050:** IPM still leads because efficiency, compactness and accumulated manufacturing knowledge remain valuable. Recycling and diversified supply reduce—but do not eliminate—magnet risk. The IEA estimates recycling could reduce primary rare-earth supply requirements by up to 35% by 2050 [[5]](https://www.iea.org/reports/rare-earth-elements/executive-summary).

---

## Data Confidence and Use in Excel

| Table | Data classification | Recommended workbook treatment |
|---|---|---|
| Table 1—2025 architecture mix | Triangulated report estimate | Use as a rounded baseline; retain an “estimate” flag |
| Table 2—production examples | Sourced programme/application evidence | Use for architecture validation; preserve axle and vehicle notes |
| Tables 3–4—reference IPM mass and magnet composition | Transparent engineering allocation | Use for scenario calculations, not OEM teardown benchmarking |
| Table 5—power scaling | Normalized calculation at 6.0 kW/kg | Use only for preliminary sizing; do not label as actual product data |
| Tables 6–8—alternative scenario shares | Report scenario assumptions | Keep as separate A/B/C cases; do not average automatically |
| Table 9—weight evolution | Internally mass-balanced scenario model | Suitable for sensitivity analysis with fixed motor-only boundaries |
| Table 10—magnet intensity | Report material model | Link composition percentages explicitly; retain sufficient decimals |
| Table 11—traffic-light risk | Qualitative decision model supported by supply evidence | Store colours as text categories, not numerical probabilities |
| Table 12—OEM snapshot | Sourced facts plus explicit evidence gaps | Treat “not publicly confirmed” as unknown, not zero |
| Table 13—composite forecast | Rounded pragmatic forecast assumption | Use as the base case, with A/B/C retained as alternatives |

Direct product datapoints include Renault E7A’s stated 200 kW and 400 Nm development target and YASA’s 13.1 kg/42 kW/kg and 12.7 kg/59 kW/kg prototype results [[6]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[16]](https://yasa.com/) [[17]](https://carbuzz.com/yasa-axial-flux-motor-incredible-power-density/). The latter must remain labeled as prototype figures. The Mercedes production date, plant footprint and process counts are direct programme evidence [[9]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) [[10]](https://media.mercedes-benz.com/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf). No table in this report should be represented as a complete production teardown bill of materials.

## Decision-Oriented Takeaway

1. **Fund the IPM roadmap first:** it remains the most credible volume architecture through 2050.
2. **Reduce exposure, not only magnet mass:** qualify diversified NdFeB sources, lower Dy/Tb intensity and design for magnet recovery.
3. **Maintain an EESM industrial option:** it is the most mature magnet-free synchronous alternative, but requires explicit copper, rotor-loss and excitation-system targets.
4. **Gate axial flux by application value:** proceed where packaging and performance justify specialized production; do not apply prototype power-density claims to mainstream duty cycles.
5. **Keep architecture accounting axle-specific:** mixed-topology AWD vehicles make vehicle-level labels inadequate for sourcing, cost and material forecasts.

---

## References

1. <https://www.idtechex.com/en/research-report/electric-motors-for-electric-vehicles/1131>
2. <https://www.idtechex.com/en/research-report/electric-motors/1031>
3. <https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/>
4. <https://www.mdpi.com/1996-1073/17/23/5861>
5. <https://www.iea.org/reports/rare-earth-elements/executive-summary>
6. <https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/>
7. <https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en>
8. <https://www.press.bmwgroup.com/usa/article/detail/T0327877EN_US/the-bmw-ix-xdrive50-5th-generation-edrive-and-sustainability?language=en_US>
9. <https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html>
10. <https://media.mercedes-benz.com/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf>
11. <https://www.press.bmwgroup.com/global/article/detail/T0448099EN/charge-faster-drive-further:-bmw-group-reveals-revolutionary-electric-drive-concept-with-800v-technology-for-the-neue-klasse?language=en>
12. <https://www.press.bmwgroup.com/united-kingdom/article/detail/T0452406EN_GB/the-start-of-a-new-era-the-new-bmw-ix3?language=en_GB>
13. <https://chargedevs.com/features/a-closer-look-at-axial-flux-motors/>
14. <https://www.emobility-engineering.com/emotor-materials/>
15. <https://www.mdpi.com/1996-1073/15/15/5431>
16. <https://yasa.com/>
17. <https://carbuzz.com/yasa-axial-flux-motor-incredible-power-density/>
18. <https://www.automotivemanufacturingsolutions.com/powertrain/yasa-industrialises-axial-flux-motor-production-under-mercedes-benz/2703254>
19. <https://techplanet.today/post/renaults-rare-earth-free-electric-motors-a-strategic-shift-in-ev-technology-and-supply-chain-independence>
20. <https://renaultgroup.com/en/magazine/energy-and-motorization/e7a-the-next-gen-electric-motor-developed-by-renault-and-valeo>
21. <https://www.reuters.com/business/autos-transportation/renault-seeking-chinese-rare-earth-free-motor-supplier-sources-say-2025-11-10/>
22. <https://www.emobility-engineering.com/axial-flux-motors/>
23. <https://group.mercedes-benz.com/company/production/production-network/mbdfc-humanoid-robots.html>
24. <https://group.mercedes-benz.com/technology/innovation/vision/vision-oneeleven.html>
25. <https://yasa.com/news/concept-amg-gt-xx-a-new-dimension-of-performance/>
26. <https://www.idtechex.com/en/research-report/electric-motors-for-evs/941>
