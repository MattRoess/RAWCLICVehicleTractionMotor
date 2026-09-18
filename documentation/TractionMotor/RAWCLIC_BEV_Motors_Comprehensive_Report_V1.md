# BEV Traction Motor Material Composition, Weight and Drivetrain Adoption: A Comprehensive Investigation of PMSM, ASM, EESM, Axial Flux and SynRM Technologies

*RAWCLIC Project / EMPA — September 2026*

## 1. Executive Summary

This report supports RAWCLIC project no. 101183654 by providing an auditable basis for estimating future traction-motor raw-material demand and end-of-life secondary-material supply. It compares five motor families: radial permanent-magnet synchronous motors, particularly interior-permanent-magnet machines (PMSM/IPM); asynchronous or induction machines (ASM/IM); electrically excited or wound-rotor synchronous machines (EESM/WRSM); axial-flux permanent-magnet machines, represented by the YASA concept; and synchronous-reluctance and permanent-magnet-assisted synchronous-reluctance machines (SynRM/PMa-SynRM).

The principal findings are:

1. **Radial PMSM/IPM is the present reference technology.** Public evidence places permanent-magnet motors at approximately 85% to above 90% of marketed or installed electrified-vehicle applications, depending on scope and classification [1] [[2]](https://www.iea.org/reports/global-ev-outlook-2026/trends-in-electric-cars). For planning, a nominal 150 kW motor-only PMSM is represented by a 55–72–90 kg envelope, 1.7–2.1–2.7 kW/kg and 1.0–1.5–2.0 kg of NdFeB magnets [1] [3]. Its advantages are high efficiency, compactness, mature manufacturing and good part-load operation. Its principal strategic weakness is dependence on NdFeB and the associated Nd, Pr, Dy and Tb supply chains.

2. **ASM is a robust magnet-free alternative, especially for secondary axles.** It replaces permanent magnets with an electrically induced rotor field, generally requiring more rotor conductor and thermal capacity than a comparable PMSM. It has no traction-magnet requirement, but it remains materially exposed to copper or aluminium, electrical steel, housing aluminium and specialised manufacturing. Rotor losses and weaker light-load efficiency usually limit its use as the sole efficiency-optimised passenger-car motor, while low de-energised drag and overload capability support secondary-axle deployment.

3. **EESM is the clearest production-scale rare-earth hedge.** It uses a controllable wound rotor instead of magnets. BMW and Renault provide current production examples [1] [[4]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en) [[5]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/). Relative to the PMSM reference, the retained scenario baseline is a +4–+8–+15 kg mass difference and +3–+6–+10 kg of rotor copper, giving a 59–80–105 kg 150 kW motor envelope [1] [3]. These deltas are planning assumptions rather than universal physical constants: excitation method, rotor cooling and integration materially change the result.

4. **Axial-flux PM technology offers high packaging upside but remains boundary-sensitive.** The 10–20–30% reported mass advantage is treated here as an analytical envelope, not a universal fact. Applied consistently to the PMSM reference, it gives a 48–58–83 kg 150 kW-class planning range [1] [3]. YASA is the axial-flux company, based in the Oxford/Yarnton area and owned by Mercedes-Benz [[6]](https://yasa.com/) [[7]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html). YASA’s reported 12.7 kg, 750 kW and approximately 59 kW/kg result is a short-duration prototype or record claim; it is not a production 150 kW mass benchmark and must not be entered into material-demand models as one [[6]](https://yasa.com/) [[8]](https://yasa.com/technology/).

5. **DeepDrive must not be classified as axial flux.** DeepDrive is the award-winning Technical University of Munich spin-off referred to in some emerging-architecture discussions, but its distinctive concept is a dual-rotor **radial-flux** machine. Its relevance lies in possible system efficiency, material and packaging improvement, not in evidence for axial-flux adoption. Its reported material-saving and range claims remain company-attributed until independently validated [[9]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/german-entrepreneurship-award-for-tum-spin-off-deepdrive) [[10]](https://www.deepdrive.tech/media/deepdrive-presents-generator) [[11]](https://www.deepdrive.tech/news/unleashing-efficiency-revolutionizing-electric-vehicle-technologydeepdrive-deepdive-part-2).

6. **SynRM spans two materially different cases.** A pure SynRM has no permanent magnets and develops torque from rotor saliency. A PMa-SynRM adds a smaller magnet inventory to improve power factor, torque density and operating range. The distinction is essential for raw-material accounting: a model that labels both simply “SynRM” can incorrectly assign either zero or full-PMSM rare-earth demand. The 150 kW planning envelope used here is 60–78–100 kg, with 0 kg NdFeB for pure SynRM and 0.2–0.5–0.9 kg for PM-assisted variants.

7. **No-magnet does not mean zero critical-material exposure.** ASM, EESM and pure SynRM avoid NdFeB, but can increase demand for copper, aluminium, electrical steel, insulation, bearing materials and cooling hardware. Substitution therefore shifts the risk portfolio rather than eliminating raw-material risk.

8. **Motor power is not a legal passenger-car cap.** The EU does not impose a general 100 kW limit for B-licence holders or new passenger-car drivers. Directive (EU) 2025/2205 concerns category-B maximum authorised mass treatment and an at-least-two-year probationary scheme; it does not create a general 100 kW passenger-car limit. EU passenger-BEV type approval likewise imposes no general power-to-weight cap. UNECE battery, braking and tyre rules are functional safety requirements rather than fixed traction-power ceilings [[12]](https://unece.org/sites/default/files/2025-05/R100r2am5e.pdf) [[13]](https://unece.org/fileadmin/DAM/trans/main/wp29/wp29regs/R13hr2e.pdf) [[14]](https://unece.org/sites/default/files/2024-01/R0100r3e.pdf).

9. **Engineering and market constraints are more relevant than nominal legal caps.** At 400 V, simple system-level screening gives 375 A for 150 kW and 1,000 A for 400 kW before losses. At 800 V, the corresponding currents are 187.5 A and 500 A. These are P = VI illustrations, not inverter-phase-current or battery-design specifications. Continuous performance is constrained by winding, rotor, inverter and battery temperatures; peak performance is constrained by current, voltage, magnetic saturation, rotor stress, tyre force, braking, vehicle stability and acceptable cost.

10. **Long-term adoption should be modelled as scenarios, not deterministic forecasts.** Through 2030, improved radial PMSM remains the low-disruption baseline. By 2040–2050, EESM, PMa-SynRM and targeted axial-flux deployment could diversify material demand. For 2060–2070, conservative, base and optimistic scenarios are provided for every RAWCLIC segment group. They should be recalculated as measured bills of material, registrations, recycling yields and supplier capacity become available.

For decision support, the recommended modelling practice is to retain topology-specific component inventories; distinguish motor-only from drive-unit boundaries; separate peak from continuous ratings; preserve min/typical/max values; and track NdFeB, total rare-earth elements, copper, aluminium and electrical steel independently.

## 2. Methodology, System Boundary and Evidence Treatment

### 2.1 Purpose and system boundary

The analysis uses a **motor-only** system boundary. It includes:

- stator laminations and windings;
- rotor laminations, rotor conductors or excitation windings;
- permanent magnets where applicable;
- shaft, bearings, seals and rotor-retention hardware;
- housing and end shields;
- motor-associated cooling passages, hardware and retained fluid;
- resolver, position sensing and basic motor sensors.

It excludes the traction inverter, gearbox, differential, external high-voltage cables, vehicle cooling circuit, battery and wheels. Integrated housings create unavoidable allocation ambiguity. Where motor and gearbox castings or cooling circuits are inseparable, the model requires an allocation rule rather than silently counting the complete drive unit as a motor.

RAWCLIC’s consolidated dataset was designed to provide traction-motor component and material weights by motor topology and vehicle segment. Its project structure distinguishes the core motor from ancillary components and disaggregates components containing strategically important materials. In the underlying stock-and-flow application, weights are reported at vehicle level, which is important for multi-motor vehicles [15] [16].

### 2.2 Nominal reference and rating conventions

The common reference is a nominal **150 kW passenger-BEV traction motor**. This is a class identifier, not a claim that every listed component can sustain 150 kW continuously. Public specifications commonly mix:

- short-duration peak power;
- 30-second or other time-limited ratings;
- continuous thermal power;
- mechanical shaft output;
- electrical input;
- motor-only and complete drive-unit mass.

All tables therefore represent a planning envelope. “Min”, “typical” and “max” mean an aggressive lightweight case, a central programme-planning case and a conservative thermal or packaging case. They do not represent the statistical minimum, arithmetic mean and maximum of a single homogeneous teardown population.

Component minima and maxima are not mechanically summed. A lightweight housing may require more complex cooling; a small active stack may require higher speed and stronger containment; and a low-magnet rotor may require higher current and copper mass. Total-motor ranges are independent system-level envelopes.

### 2.3 RAWCLIC regression and uncertainty method

The RAWCLIC dataset derives component weight–torque relationships from literature data, including Drexler et al. (2025), using fitted regression lines and confidence intervals. Vehicle-model torque data are assigned to RAWCLIC segments, and Monte Carlo simulation propagates regression uncertainty through segment-level results [15] [16]. Drexler’s benchmark covered 48 traction motors from 31 passenger vehicles released between 2018 and 2023, including PMSM, induction and EESM examples [[17]](https://www.hub-edrive.de/fileadmin/media/Publikation/Advances_in_electricmotors.pdf).

The tables in this report extend that framework to topologies for which the supplied consolidated dataset is sparse, notably axial flux and SynRM. Those extensions are explicitly parameterised estimates. They must not be represented as teardown measurements.

### 2.4 Reproducible scaling equations

For an anchor topology with 150 kW typical mass `M150`, the simplified scaling calculation is:

`M(P) = M150 × f(P) × ktopology`

where `f(P)` is calibrated to the supplied PMSM power table and `ktopology` is 1.00 for the anchor. For alternative motors, topology-specific 150 kW anchors are applied to the same relative curve. At power levels outside current series-production practice, an engineering-practicality flag is added.

Mechanical torque follows:

`T = 9550 × P / n`

where `T` is torque in N·m, `P` is mechanical power in kW and `n` is speed in revolutions per minute. The scaling tables use 4,000 rpm as a transparent base-speed screening assumption. Thus, a nominal 150 kW corresponds to approximately 358 N·m at that speed. Actual motors can reach the same power using different torque-speed combinations.

A compact radial-machine relationship is represented as:

`T ≈ Kt × D² × L`

and:

`Mactive ≈ Km × D² × L`

where `D` is active air-gap diameter, `L` is stack length and the coefficients incorporate electromagnetic loading, density, topology and cooling. Power is then:

`P ≈ 2πnT / 60,000`

for kW. The equations show why increasing diameter strongly benefits torque, while increasing speed can raise power without proportional active-material growth. They are parametric relationships, not fitted universal laws.

### 2.5 Material-allocation rules

The allocation rules are:

- Nd, Pr, Dy and Tb are elemental fractions **within** NdFeB mass, not additional mass.
- “Total REE” is the sum of the modelled rare-earth elements inside magnets.
- Electrical steel includes stator and rotor laminations.
- Copper includes stator winding and, where applicable, rotor cage or field winding.
- Aluminium includes housing, cooling structures and aluminium rotor conductors where selected.
- Permanent magnets are shown explicitly as “none” for ASM, EESM and pure SynRM.
- PMa-SynRM is reported separately within the SynRM family.
- Axial flux is counted separately from radial PMSM for market-share purposes even though both use permanent magnets.

### 2.6 Limitations

The main limitations are inconsistent specification boundaries, sparse public component bills of material, uncertain continuous ratings, differences in motor count per vehicle, changing cooling technology and the commercial confidentiality of magnet chemistry. The internal RAWCLIC baseline is suitable for harmonised stock-and-flow modelling, while the extended five-topology tables are decision-support estimates pending replacement by measured supplier or teardown data [ref1–ref4].

## 3. Radial PMSM/IPM

### 3.1 Architecture and operating principle

A radial PMSM has a laminated stator carrying multiphase windings and a rotor whose permanent magnets establish a magnetic field without rotor electrical excitation. In an IPM, magnets are buried within flux barriers in the rotor. Electronic commutation keeps the stator field synchronous with the rotor. Torque combines permanent-magnet interaction with reluctance torque arising from rotor saliency.

The IPM arrangement protects magnets mechanically and supports field weakening for high-speed operation. Its electromagnetic efficiency and compact active volume explain its position as the passenger-BEV reference. The trade-off is a concentrated requirement for NdFeB and associated rare-earth elements, alongside conventional exposure to copper, electrical steel and aluminium.

### 3.2 150 kW reference component envelope

| Component | Principal material | Min kg | Typ. kg | Max kg | Notes |
|---|---|---:|---:|---:|---|
| Stator laminations | Non-oriented Si electrical steel | 18.0 | 23.0 | 28.0 | Supplied PMSM baseline |
| Stator winding | Copper | 8.0 | 11.0 | 14.0 | Hairpin or stranded winding |
| Rotor laminations | High-strength electrical steel | 10.0 | 14.0 | 18.0 | Includes magnet barriers |
| Permanent magnets | Sintered NdFeB | 1.0 | 1.5 | 2.0 | Buried IPM magnet allowance |
| Rotor cage/field winding | None | 0 | 0 | 0 | Rotor field supplied by magnets |
| Shaft | Alloy steel | 3.0 | 4.5 | 6.0 | Fatigue and speed dependent |
| Housing/end shields | Aluminium alloy | 8.0 | 12.0 | 17.0 | Boundary-sensitive |
| Bearings/seals | Bearing steel; optional ceramic | 1.0 | 1.7 | 2.5 | Electrical and speed loading vary |
| Cooling hardware/fluid | Aluminium, polymers, fluid | 2.0 | 4.0 | 7.0 | Jacket, oil spray or hollow shaft |
| Sensors/resolver | Copper, steel, electronics | 0.3 | 0.7 | 1.2 | Position and temperature sensing |
| **Total motor** | Mixed | **55** | **72** | **90** | Independent system envelope |
| **Power density** | — | **1.7** | **2.1** | **2.7 kW/kg** | 150 kW divided by total mass |

The baseline reproduces the supplied programme envelope [1] [3].

### 3.3 Strategic-material inventory

| Material | Min kg | Typ. kg | Max kg | Interpretation |
|---|---:|---:|---:|---|
| NdFeB magnet | 1.00 | 1.50 | 2.00 | Complete magnet mass |
| Nd | 0.25 | 0.38 | 0.55 | Within NdFeB |
| Pr | 0.03 | 0.08 | 0.15 | Within NdFeB |
| Dy | 0.01 | 0.05 | 0.12 | Temperature-coercivity addition |
| Tb | 0.00 | 0.01 | 0.03 | May be intentionally absent |
| Total modelled REE | 0.29 | 0.52 | 0.85 | Nd + Pr + Dy + Tb |
| Copper | 8.0 | 11.0 | 14.0 | Mainly stator winding |
| Aluminium | 8.0 | 12.0 | 17.0 | Housing and thermal structure |
| Electrical steel/Si-iron | 28.0 | 37.0 | 46.0 | Stator plus rotor laminations |
| Silicon within steel | 0.5 | 1.0 | 1.8 | Alloying allocation |
| Other pertinent materials | 5.3 | 10.9 | 16.9 | Shaft, bearings, insulation, sensors and fluid |

The elemental magnet ranges are contained within, rather than additional to, the NdFeB allowance [1] [3].

### 3.4 Power scaling

Torque assumes 4,000 rpm. Torque density uses typical torque divided by typical mass.

| Power kW | Total mass min/typ/max kg | Power density min/typ/max kW/kg | Torque at 4,000 rpm N·m | Typ. torque density N·m/kg | NdFeB min/typ/max kg | Practicality |
|---:|---:|---:|---:|---:|---:|---|
| 50 | 28/36/47 | 1.1/1.4/1.8 | 119 | 3.3 | 0.25/0.45/0.70 | Practical |
| 75 | 35/45/58 | 1.3/1.7/2.1 | 179 | 4.0 | 0.4/0.7/1.0 | Practical |
| 100 | 42/54/68 | 1.5/1.9/2.4 | 239 | 4.4 | 0.7/1.1/1.5 | Practical |
| 150 | 55/72/90 | 1.7/2.1/2.7 | 358 | 5.0 | 1.0/1.5/2.0 | Reference |
| 200 | 68/88/110 | 1.8/2.3/2.9 | 478 | 5.4 | 1.4/2.1/2.8 | Practical |
| 250 | 80/105/132 | 1.9/2.4/3.1 | 597 | 5.7 | 1.8/2.7/3.6 | Practical; duty-sensitive |
| 350 | 105/142/185 | 1.9/2.5/3.3 | 836 | 5.9 | 2.5/3.8/5.0 | Often multi-motor/high performance |
| 400 | 118/160/210 | 1.9/2.5/3.4 | 955 | 6.0 | 2.8/4.3/5.8 | Single-motor value off-market in many segments |

The 75–400 kW rows reproduce the supplied radial-IPM scaling envelope; 50 kW is a transparent extension [1] [3].

### 3.5 Size relationship and efficiency map

For radial PMSM screening, `T ≈ KIPM D²L`. At fixed loading, a 10% increase in diameter produces approximately a 21% increase in the `D²L` torque term if stack length is unchanged. Alternatively, higher rotational speed increases power without the same increase in torque-producing volume, but raises rotor stress and iron loss.

The expected efficiency map has a broad high-efficiency island at medium speed and moderate-to-high torque. Peak efficiency is commonly reported in the mid-90% range for traction PMSMs, but the exact value is boundary- and design-specific [[18]](https://www.epj-conferences.org/articles/epjconf/pdf/2025/26/epjconf_icatcict2025_01019.pdf). Highway operation can remain efficient when the gearing places the motor near the map’s central island. At very high speed, field-weakening current and iron losses reduce efficiency. At light load, permanent-magnet excitation avoids rotor copper loss but creates unavoidable magnetic and iron losses.

### 3.6 Advantages, limitations and adoption

**Advantages**

- High gravimetric and volumetric power density.
- High peak and drive-cycle efficiency.
- Strong low-speed torque and controllability.
- Mature radial-machine manufacturing base.
- Good integration with single-speed reductions.
- Reluctance torque can reduce magnet intensity.

**Limitations**

- NdFeB and rare-earth supply exposure.
- Demagnetisation and magnet-temperature constraints.
- Rotor assembly and magnet-retention complexity.
- Back-electromotive force persists when de-energised.
- Magnet separation complicates recycling.
- High-speed losses and containment constrain downsizing.

Named examples include Volkswagen MEB/APP550 applications such as ID.3 and ID.4, Hyundai-Kia E-GMP vehicles such as Ioniq 5/6 and EV6/EV9, Tesla Model 3/Y rear drives and GM Ultium applications [1] [3]. PMSM dominates current AB, CD and EF use, with especially strong suitability for single-motor mainstream vehicles.

## 4. ASM/Induction Motor

### 4.1 Architecture and operating principle

An ASM has a wound stator similar to other AC traction machines and a rotor containing conductive bars shorted by end rings. The rotating stator field induces rotor current; torque arises from interaction between the induced rotor field and stator field. Rotor speed must differ from synchronous speed, producing “slip”.

The rotor can use copper or aluminium conductors. It contains no permanent magnets and needs no brush or rotor-field supply. When de-energised, it can have low magnetic drag, which is advantageous on a secondary axle. The penalty is rotor Joule heat, which must cross the air gap or leave through the shaft and end structures.

### 4.2 150 kW reference component envelope

| Component | Principal material | Min kg | Typ. kg | Max kg | Notes |
|---|---|---:|---:|---:|---|
| Stator laminations | Non-oriented Si steel | 20 | 26 | 32 | Modelled above PMSM baseline |
| Stator winding | Copper | 9 | 12 | 16 | Magnetising-current requirement |
| Rotor laminations | Electrical steel | 13 | 18 | 24 | Supports cage and mechanical load |
| Rotor cage/end rings | Copper or aluminium | 3 | 6 | 10 | Topology-specific conductor |
| Permanent magnets | **None** | **0** | **0** | **0** | Rotor field is induced |
| Shaft | Alloy steel | 3.5 | 5.0 | 7.0 | Thermal and mechanical duty |
| Housing/end shields | Aluminium alloy | 9 | 14 | 20 | Includes cooling structure |
| Bearings/seals | Steel/ceramic option | 1.2 | 2.0 | 3.0 | Speed dependent |
| Cooling hardware/fluid | Aluminium, fluid, polymers | 3 | 5 | 9 | Rotor losses increase thermal burden |
| Sensors/resolver | Mixed | 0.3 | 0.8 | 1.3 | Speed and temperature control |
| **Total motor** | Mixed | **62** | **82** | **105** | Parameterised planning envelope |
| **Power density** | — | **1.4** | **1.8** | **2.4 kW/kg** | Motor-only |

### 4.3 Strategic-material inventory

| Material | Min kg | Typ. kg | Max kg | Interpretation |
|---|---:|---:|---:|---|
| NdFeB | 0 | 0 | 0 | None: induced rotor field |
| Nd/Pr/Dy/Tb | 0 | 0 | 0 | No traction-magnet REE |
| Total REE | 0 | 0 | 0 | Excludes trace electronics |
| Copper | 12 | 18 | 26 | Stator plus copper-cage case |
| Aluminium | 9 | 16 | 25 | Housing plus possible aluminium cage |
| Electrical steel/Si-iron | 33 | 44 | 56 | Stator and rotor |
| Other pertinent materials | 8 | 14 | 22 | Shaft, bearings, insulation, cooling and sensors |

Copper and aluminium cage alternatives must not be counted simultaneously at their maxima without a defined rotor design.

### 4.4 Power scaling

| Power kW | Total mass min/typ/max kg | Power density min/typ/max kW/kg | Torque N·m | Typ. torque density N·m/kg | NdFeB kg | Practicality |
|---:|---:|---:|---:|---:|---:|---|
| 50 | 32/41/55 | 0.9/1.2/1.6 | 119 | 2.9 | 0/0/0 | Practical |
| 75 | 40/51/68 | 1.1/1.5/1.9 | 179 | 3.5 | 0/0/0 | Practical |
| 100 | 48/62/80 | 1.3/1.6/2.1 | 239 | 3.9 | 0/0/0 | Practical |
| 150 | 62/82/105 | 1.4/1.8/2.4 | 358 | 4.4 | 0/0/0 | Reference |
| 200 | 77/100/128 | 1.6/2.0/2.6 | 478 | 4.8 | 0/0/0 | Practical |
| 250 | 91/120/154 | 1.6/2.1/2.7 | 597 | 5.0 | 0/0/0 | Thermal design important |
| 350 | 119/162/216 | 1.6/2.2/2.9 | 836 | 5.2 | 0/0/0 | Often secondary or multi-motor |
| 400 | 134/182/245 | 1.6/2.2/3.0 | 955 | 5.2 | 0/0/0 | Single-motor value not generally mainstream |

### 4.5 Size relationship and efficiency map

The radial relation remains `T ≈ KASM D²L`, but `KASM` is reduced relative to an otherwise comparable high-performance IPM where rotor thermal limits or magnetising current constrain loading. Additional rotor-conductor and cooling mass increase total mass for the same active volume.

The efficiency island is normally narrower than for an optimised PMSM because both stator and rotor carry loss-producing current. Peak efficiency can nevertheless be high near the design load. Highway efficiency depends strongly on gearing and rotor-loss management. At light load, magnetising current lowers efficiency, although a completely de-energised secondary-axle machine can offer low drag.

**Advantages**

- No permanent magnets or traction-magnet rare earths.
- Robust rotor construction.
- Low de-energised drag for secondary axles.
- Strong short-duration overload capability.
- Established manufacturing and control principles.
- No demagnetisation failure mode.

**Limitations**

- Rotor copper or aluminium losses.
- More difficult rotor heat rejection.
- Lower part-load efficiency than PMSM in many designs.
- Lower power factor and greater inverter current demand.
- Often heavier for equivalent continuous output.
- Copper-cage manufacture can be demanding.

Current examples include induction machines on selected Tesla front axles and a reported ASM front-axle role in BMW’s Neue Klasse strategy [1] [3]. Usage is strongest in CD and EF all-wheel-drive systems where the ASM can be disconnected electrically during cruising.

## 5. EESM/WRSM

### 5.1 Architecture and operating principle

An EESM replaces permanent magnets with a rotor field winding carrying controlled direct current. The wound rotor creates the excitation field, while the stator produces the rotating field. The machine runs synchronously, and torque is controlled through stator current and rotor excitation.

Excitation may use brushes and slip rings or brushless/inductive transfer. Adjustable field strength improves control over field weakening and can reduce no-load magnetic losses. However, rotor winding, excitation transfer, insulation and cooling add mass and complexity. Rotor copper losses are particularly relevant during sustained high-torque operation.

### 5.2 150 kW reference component envelope

| Component | Principal material | Min kg | Typ. kg | Max kg | Notes |
|---|---|---:|---:|---:|---|
| Stator laminations | Si electrical steel | 18 | 23 | 29 | Similar class to PMSM |
| Stator winding | Copper | 8 | 11 | 14 | Comparable stator basis |
| Rotor laminations/pole body | Electrical steel | 10 | 15 | 20 | Wound-rotor structure |
| Rotor field winding | Copper | 3 | 6 | 10 | Required EESM addition |
| Permanent magnets | **None** | **0** | **0** | **0** | Rotor field is electrically excited |
| Excitation transfer | Copper, steel, electronics | 1 | 2 | 5 | Brush/slip-ring or brushless system |
| Shaft | Alloy steel | 3 | 5 | 7 | Rotor integration dependent |
| Housing/end shields | Aluminium alloy | 8 | 13 | 19 | Thermal and structural functions |
| Bearings/seals | Steel/ceramic option | 1 | 2 | 3 | Includes excitation-interface effects |
| Cooling hardware/fluid | Mixed | 3 | 5 | 9 | Rotor cooling can be significant |
| Sensors/resolver | Mixed | 0.3 | 0.8 | 1.3 | Field and position control |
| **Total motor** | Mixed | **59** | **80** | **105** | PMSM plus retained delta |
| **Power density** | — | **1.4** | **1.9** | **2.5 kW/kg** | Motor-only |

The total preserves the specified +4–+8–+15 kg comparison with PMSM, while recognising that individual EESM configurations vary [1] [3].

### 5.3 Strategic-material inventory

| Material | Min kg | Typ. kg | Max kg | Interpretation |
|---|---:|---:|---:|---|
| NdFeB | 0 | 0 | 0 | None: wound rotor |
| Nd/Pr/Dy/Tb | 0 | 0 | 0 | No traction-magnet REE |
| Total REE | 0 | 0 | 0 | Excludes trace electronic use |
| Stator copper | 8 | 11 | 14 | PMSM-comparable basis |
| Rotor copper | 3 | 6 | 10 | Retained scenario delta |
| Total copper | 11 | 17 | 24 | Stator plus rotor |
| Aluminium | 8 | 13 | 19 | Housing and cooling |
| Electrical steel/Si-iron | 28 | 38 | 49 | Stator and rotor |
| Other pertinent materials | 12 | 18 | 28 | Excitation, shaft, bearings, insulation and cooling |

### 5.4 Power scaling

| Power kW | Total mass min/typ/max kg | Power density min/typ/max kW/kg | Torque N·m | Typ. torque density N·m/kg | NdFeB kg | Practicality |
|---:|---:|---:|---:|---:|---:|---|
| 50 | 30/40/55 | 0.9/1.3/1.7 | 119 | 3.0 | 0/0/0 | Practical |
| 75 | 38/50/68 | 1.1/1.5/2.0 | 179 | 3.6 | 0/0/0 | Practical |
| 100 | 45/60/80 | 1.3/1.7/2.2 | 239 | 4.0 | 0/0/0 | Practical |
| 150 | 59/80/105 | 1.4/1.9/2.5 | 358 | 4.5 | 0/0/0 | Reference |
| 200 | 73/98/128 | 1.6/2.0/2.7 | 478 | 4.9 | 0/0/0 | Practical |
| 250 | 86/117/154 | 1.6/2.1/2.9 | 597 | 5.1 | 0/0/0 | Practical; rotor cooling sensitive |
| 350 | 113/158/216 | 1.6/2.2/3.1 | 836 | 5.3 | 0/0/0 | High-performance, often multi-motor |
| 400 | 127/178/245 | 1.6/2.2/3.1 | 955 | 5.4 | 0/0/0 | Single-motor value not generally mainstream |

### 5.5 Size relationship and efficiency map

`T ≈ KEESM D²L Ifield`, with the field-current term bounded by rotor copper temperature, excitation-system capability and magnetic saturation. The controllable field is the principal differentiator: the machine can reduce excitation at light load or high speed rather than opposing a fixed magnet field.

Published comparisons do not identify a universal highway-efficiency winner. The retained difference relative to a comparable IPM spans −1.5 to +0.5 percentage points, with −0.5 percentage points as a planning centre [1] [3]. Peak efficiency can be competitive, but rotor copper and excitation losses penalise some high-torque points. At high speed and moderate torque, adjustable excitation can support efficient field weakening. At very light load, the ability to reduce field may offset part of the excitation-system loss.

**Advantages**

- Eliminates traction-magnet NdFeB.
- Adjustable rotor field.
- Strong field-weakening capability.
- Competitive high-speed operation in optimised designs.
- Reduced permanent back-EMF when excitation is removed.
- Production use demonstrates industrial viability.

**Limitations**

- Rotor copper mass and loss.
- Excitation-transfer complexity.
- More difficult rotor cooling.
- Potential brush/slip-ring wear in applicable designs.
- Higher mass than the PMSM scenario baseline.
- More complex assembly and control.

BMW i4, i5, i7 and iX use Gen5 electrically excited machines; BMW’s Neue Klasse direction combines EESM with a secondary ASM. Renault’s Megane and Scenic E-Tech provide further production examples, while the E7A 200 kW, 800 V programme was reported as under revision in the supplied evidence [1] [3] [[4]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en) [[5]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/).

## 6. Axial-Flux Permanent-Magnet Motor, YASA and Related Emerging Architectures

### 6.1 Architecture and operating principle

In an axial-flux motor, magnetic flux crosses the air gap substantially parallel to the shaft rather than radially. Disc-shaped rotors and stators create a short axial package and a comparatively large mean torque radius. Common configurations include single-stator/single-rotor, double-rotor/single-stator and multiple-disc arrangements.

Yokeless and segmented-armature designs remove or reduce the continuous stator yoke and use concentrated stator segments. The geometry can improve torque density, but it creates demanding air-gap, rotor-disc, thermal and assembly requirements. The most visible passenger-car designs use permanent magnets and therefore retain NdFeB exposure.

### 6.2 150 kW reference component envelope

| Component | Principal material | Min kg | Typ. kg | Max kg | Notes |
|---|---|---:|---:|---:|---|
| Segmented stator cores | Electrical steel | 12 | 18 | 25 | Yokeless/segmented analytical range |
| Stator winding | Copper | 7 | 10 | 14 | Short end-winding potential |
| Rotor discs/back iron | Steel/electrical steel | 8 | 12 | 18 | Disc stiffness is critical |
| Permanent magnets | NdFeB | 1.0 | 1.5 | 2.2 | PM axial-flux reference |
| Shaft/rotor support | Steel or composite/steel | 3 | 5 | 8 | Air-gap and burst containment |
| Housing/end structures | Aluminium alloy | 7 | 10 | 16 | Thin package but large diameter |
| Bearings/seals | Steel/ceramic option | 1 | 1.7 | 3 | Axial loads can matter |
| Cooling hardware/fluid | Aluminium, fluid, polymers | 3 | 5 | 9 | Distributed stator cooling |
| Sensors/resolver | Mixed | 0.3 | 0.7 | 1.2 | Position and thermal sensing |
| **Total motor** | Mixed | **48** | **58** | **83** | Analytical 10–20–30% saving envelope |
| **Power density** | — | **1.8** | **2.6** | **3.1 kW/kg** | Conservative matched-boundary result |

The reported 10–20–30% advantage is an envelope rather than a universal property. The separate production-oriented 3–5–8 kW/kg band in the supplied evidence reflects a different performance boundary and should not be combined mechanically with every mass row [1] [3].

### 6.3 Strategic-material inventory

| Material | Min kg | Typ. kg | Max kg | Interpretation |
|---|---:|---:|---:|---|
| NdFeB | 1.0 | 1.5 | 2.2 | PM rotor discs |
| Nd | 0.25 | 0.38 | 0.61 | Scaled PMSM chemistry |
| Pr | 0.03 | 0.08 | 0.17 | Within magnets |
| Dy | 0.01 | 0.05 | 0.13 | Thermal-grade dependent |
| Tb | 0.00 | 0.01 | 0.03 | May be absent |
| Total modelled REE | 0.29 | 0.52 | 0.94 | Within NdFeB |
| Copper | 7 | 10 | 14 | Segmented stator winding |
| Aluminium | 7 | 10 | 16 | Housing/cooling |
| Electrical steel/Si-iron | 20 | 30 | 43 | Stator cores plus rotor back iron |
| Other pertinent materials | 13 | 18 | 29 | Supports, bearings, insulation and cooling |

### 6.4 Power scaling

| Power kW | Total mass min/typ/max kg | Power density min/typ/max kW/kg | Torque N·m | Typ. torque density N·m/kg | NdFeB min/typ/max kg | Practicality |
|---:|---:|---:|---:|---:|---:|---|
| 50 | 24/29/43 | 1.2/1.7/2.1 | 119 | 4.1 | 0.25/0.45/0.75 | Practical in specialised products |
| 75 | 30/36/54 | 1.4/2.1/2.5 | 179 | 5.0 | 0.4/0.7/1.1 | Practical |
| 100 | 36/44/63 | 1.6/2.3/2.8 | 239 | 5.4 | 0.7/1.1/1.6 | Emerging |
| 150 | 48/58/83 | 1.8/2.6/3.1 | 358 | 6.2 | 1.0/1.5/2.2 | Reference estimate |
| 200 | 59/70/102 | 2.0/2.9/3.4 | 478 | 6.8 | 1.4/2.1/3.1 | Emerging/premium |
| 250 | 69/84/122 | 2.0/3.0/3.6 | 597 | 7.1 | 1.8/2.7/4.0 | Specialised |
| 350 | 91/114/171 | 2.0/3.1/3.8 | 836 | 7.3 | 2.5/3.8/5.5 | Limited production evidence |
| 400 | 102/128/194 | 2.1/3.1/3.9 | 955 | 7.5 | 2.8/4.3/6.4 | Off-market as a general single motor |

### 6.5 Size relationship and efficiency map

Axial torque is usefully represented as `T ≈ KAF D³`, with disc thickness, pole count and air-gap loading embedded in `KAF`. The cubic diameter sensitivity illustrates the benefit of a large active radius, but should not be interpreted independently of rotor-disc stress, air-gap control and vehicle package width.

The efficiency map can be broad where segmented stators have short end windings and effective direct cooling. Peak efficiency may be competitive with radial PMSM. At highway speed, rotor-disc losses, magnet eddy-current losses and gearing determine the outcome. At part load, fixed magnet excitation creates behaviour broadly analogous to a PMSM, although detailed loss distribution differs.

### 6.6 Advantages, limitations and present use

**Advantages**

- Short axial package.
- High torque potential at large mean radius.
- Potentially short end windings.
- Modular multi-disc arrangements.
- Potential motor-mass and vehicle-package savings.
- Strong relevance to premium and high-performance platforms.

**Limitations**

- Tight air-gap and disc-flatness requirements.
- Rotor-disc stress and containment challenges.
- Complex segmented-stator manufacture.
- Cooling and sealing across a large diameter.
- Continued NdFeB and rare-earth exposure.
- Limited matched-boundary production evidence.

YASA is the axial-flux company and Mercedes-Benz subsidiary; its technology has a visible pathway into premium Mercedes-AMG applications [[6]](https://yasa.com/) [[7]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) [[19]](https://media.mercedes-benz.com/en/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf). The reported 12.7 kg, 750 kW result is a prototype or record claim, not the 150 kW production benchmark used above.

### 6.7 Future axial-flux PMSM developments and related radial concepts

Future axial-flux PMSM development can reduce magnet and copper intensity through improved segmentation, higher winding fill, thinner electrical steel, grain-boundary-diffused magnets, better conductor cooling and multi-disc optimisation. Industrial success depends less on isolated peak kW/kg records than on continuous-duty validation, automated assembly, rotor containment, air-gap yield, acoustic performance and end-of-life separability.

DeepDrive belongs in the broader emerging-architecture discussion but must remain correctly classified. It is an award-winning TUM spin-off whose distinctive dual-rotor concept is radial flux, not axial flux. Company-reported claims concerning material efficiency and vehicle range indicate why it is relevant to future material-demand scenarios, but those claims should remain separately attributed rather than converted into verified mass savings [[9]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/german-entrepreneurship-award-for-tum-spin-off-deepdrive) [[10]](https://www.deepdrive.tech/media/deepdrive-presents-generator) [[11]](https://www.deepdrive.tech/news/unleashing-efficiency-revolutionizing-electric-vehicle-technologydeepdrive-deepdive-part-2) [[20]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/presidential-award-for-space-start-up).

## 7. SynRM and PM-Assisted SynRM

### 7.1 Architecture and operating principle

A pure SynRM has a wound stator and a magnet-free rotor containing shaped flux barriers. The barriers create different magnetic reluctances along the rotor axes. The rotor aligns with the rotating stator field to minimise magnetic reluctance, producing synchronous reluctance torque.

A PMa-SynRM adds magnets within the flux barriers. These magnets improve power factor, torque density and efficiency while preserving a substantial reluctance-torque contribution. The family therefore ranges from zero-magnet pure SynRM to machines that can overlap technically with reduced-magnet IPM classifications.

### 7.2 150 kW reference component envelope

| Component | Principal material | Min kg | Typ. kg | Max kg | Notes |
|---|---|---:|---:|---:|---|
| Stator laminations | Si electrical steel | 20 | 25 | 31 | Reactive-current allowance |
| Stator winding | Copper | 9 | 12 | 16 | Higher current possible |
| Rotor laminations/flux barriers | High-strength electrical steel | 11 | 16 | 22 | Mechanically complex barrier rotor |
| Permanent magnets: pure SynRM | **None** | **0** | **0** | **0** | Torque arises from saliency |
| Permanent magnets: PMa-SynRM | Ferrite or NdFeB | 0.2 | 0.5 | 0.9 | Reduced-magnet variant |
| Shaft | Alloy steel | 3 | 5 | 7 | Barrier-rotor strength dependent |
| Housing/end shields | Aluminium alloy | 8 | 13 | 18 | Structure and thermal management |
| Bearings/seals | Steel/ceramic option | 1 | 2 | 3 | Speed dependent |
| Cooling hardware/fluid | Mixed | 3 | 5 | 8 | Stator current drives cooling need |
| Sensors/resolver | Mixed | 0.3 | 0.8 | 1.3 | Rotor position is essential |
| **Total motor** | Mixed | **60** | **78** | **100** | Family-level planning envelope |
| **Power density** | — | **1.5** | **1.9** | **2.5 kW/kg** | Motor-only |

### 7.3 Strategic-material inventory

| Material | Pure SynRM min/typ/max kg | PMa-SynRM min/typ/max kg | Interpretation |
|---|---:|---:|---|
| NdFeB | 0/0/0 | 0.2/0.5/0.9 | Ferrite option can reduce NdFeB further |
| Nd | 0/0/0 | 0.05/0.13/0.25 | If NdFeB is used |
| Pr | 0/0/0 | 0.01/0.03/0.07 | If NdFeB is used |
| Dy | 0/0/0 | 0/0.02/0.05 | Grade dependent |
| Tb | 0/0/0 | 0/0/0.01 | May be absent |
| Total modelled REE | 0/0/0 | 0.06/0.18/0.38 | Reduced versus PMSM |
| Copper | 9/12/16 | 9/12/16 | Mainly stator |
| Aluminium | 8/13/18 | 8/13/18 | Housing/cooling |
| Electrical steel/Si-iron | 31/41/53 | 31/41/53 | Stator plus barrier rotor |
| Other pertinent materials | 12/18/27 | 12/18/27 | Insulation, shaft, bearings and cooling |

### 7.4 Power scaling

| Power kW | Total mass min/typ/max kg | Power density min/typ/max kW/kg | Torque N·m | Typ. torque density N·m/kg | NdFeB pure / PMa min-typ-max kg | Practicality |
|---:|---:|---:|---:|---:|---:|---|
| 50 | 31/39/52 | 1.0/1.3/1.6 | 119 | 3.1 | 0 / 0.05-0.15-0.30 | Practical |
| 75 | 38/49/65 | 1.2/1.5/2.0 | 179 | 3.7 | 0 / 0.10-0.25-0.45 | Practical |
| 100 | 46/59/77 | 1.3/1.7/2.2 | 239 | 4.1 | 0 / 0.15-0.35-0.60 | Practical |
| 150 | 60/78/100 | 1.5/1.9/2.5 | 358 | 4.6 | 0 / 0.20-0.50-0.90 | Reference |
| 200 | 74/95/122 | 1.6/2.1/2.7 | 478 | 5.0 | 0 / 0.30-0.70-1.20 | Practical |
| 250 | 87/114/146 | 1.7/2.2/2.9 | 597 | 5.2 | 0 / 0.40-0.90-1.50 | Practical |
| 350 | 115/154/205 | 1.7/2.3/3.0 | 836 | 5.4 | 0 / 0.55-1.30-2.10 | Limited pure-SynRM evidence |
| 400 | 129/174/233 | 1.7/2.3/3.1 | 955 | 5.5 | 0 / 0.65-1.50-2.40 | Not generally mainstream as one motor |

### 7.5 Size relationship and efficiency map

`T ≈ KSynRM D²L × saliency`, where “saliency” represents the inductance or reluctance contrast created by the flux barriers. Increasing barrier saliency raises torque potential but can weaken the rotor mechanically and complicate high-speed containment.

Pure SynRM efficiency can be strong at moderate and high load because there is no rotor copper or magnet loss. However, lower power factor can require greater stator and inverter current. At part load, current needed to establish flux can reduce efficiency. PM assistance improves low- and medium-load efficiency and broadens the useful operating region, but reintroduces magnet supply exposure.

**Advantages**

- Pure SynRM eliminates permanent magnets.
- Simple rotor material set.
- No rotor copper loss.
- PM assistance allows a tunable material-performance compromise.
- Good high-speed potential if the barrier rotor is mechanically sound.
- Potential compatibility with established stator production.

**Limitations**

- Lower power factor for pure SynRM.
- Higher inverter-current requirement.
- Torque ripple and acoustic challenges.
- Flux-barrier rotor stress.
- Lower torque density without PM assistance.
- Classification ambiguity with reduced-magnet IPM.

The Tesla Model 3 permanent-magnet reluctance concept is frequently discussed as a PM-assisted reluctance example, although public labels vary between IPM and PMa-SynRM. That ambiguity should be preserved in model metadata rather than resolved by assumption. The supplied evidence does not establish a named high-volume passenger BEV using a pure magnet-free SynRM as its sole traction motor.

## 8. Cross-Motor Comparison and Raw-Material Implications

| Criterion, 150 kW reference | PMSM/IPM | ASM | EESM | Axial-flux PM | SynRM/PMa-SynRM |
|---|---|---|---|---|---|
| Total mass, kg | 55/72/90 | 62/82/105 | 59/80/105 | 48/58/83 | 60/78/100 |
| NdFeB, kg | 1.0/1.5/2.0 | None | None | 1.0/1.5/2.2 | 0 pure; 0.2/0.5/0.9 PMa |
| Copper tendency | Medium | Medium-high | High | Medium | Medium-high |
| Electrical-steel tendency | Medium | High | Medium-high | Medium | High |
| Aluminium tendency | Medium | Medium-high | Medium | Medium | Medium |
| Peak/part-load efficiency | High/high | High at design point/lower | High/adjustable field | High/high, design-specific | Competitive; PMa stronger at part load |
| Main risk | Rare-earth concentration | Rotor heat and current | Rotor excitation and copper | Industrialisation plus REE | Power factor and rotor mechanics |
| Best-fit role | Mainstream primary motor | Secondary axle, robust duty | REE-free primary drive | Premium packaging/performance | Reduced-magnet or REE-free optimisation |
| 2025 maturity | High | High | Production | Early production/niche | PMa emerging; pure SynRM limited |

The material implication is not a simple rare-earth versus no-rare-earth choice:

- Moving from PMSM to EESM can remove roughly 1.0–2.0 kg of NdFeB per 150 kW motor but add approximately 3–10 kg of rotor copper and additional excitation hardware.
- Moving to ASM removes magnets but can increase electrical-steel, conductor and cooling requirements.
- Moving to pure SynRM removes magnets but can shift demand towards copper, inverter capacity and high-strength rotor laminations.
- Moving to PMa-SynRM reduces rather than eliminates magnet exposure.
- Axial flux can reduce total motor mass if its packaging advantage is realised, but normally retains comparable or slightly higher magnet exposure per motor in the present analytical envelope.

For secondary-material planning, copper and aluminium have larger mass flows, while Nd, Pr, Dy and Tb create concentrated strategic exposure. Electrical steel is the largest active-material fraction in most topologies and should not be omitted from circularity analysis merely because individual alloying elements are less supply-constrained.

## 9. Scaling from Motor to Vehicle and Secondary-Material Supply

### 9.1 Vehicle-level accounting

RAWCLIC’s stock-and-flow logic requires vehicle-level rather than individual-motor mass [15]. For topology `i`:

`Vehicle material mass = number of motors × material mass per motor × topology share`

For mixed drivetrains, each axle must be modelled separately. A dual-motor vehicle with a PMSM rear motor and ASM front motor is not equivalent to two PMSMs. Likewise, a 300 kW vehicle may contain two 150 kW motors rather than one 300 kW motor, changing housing, bearing, sensor and magnet totals.

### 9.2 Power and torque scaling cautions

The eight-row tables are screening tools. High-power rows are especially sensitive to:

- one-versus-two-motor architecture;
- peak versus continuous designation;
- base speed and maximum speed;
- coolant temperature and flow;
- rotor stress;
- inverter current;
- gearbox ratio;
- vehicle traction limits.

The RAWCLIC torque-regression method is preferable where vehicle-level torque and segment data are available because material mass, especially magnet and active-stack mass, is often more directly related to torque than to peak power [15]. Power-only scaling should therefore be used as a fallback, not as a substitute for topology- and torque-specific regression.

### 9.3 End-of-life implications

A future secondary-material model should distinguish:

1. manufacturing scrap from end-of-life motors;
2. complete-motor reuse from dismantling;
3. copper-winding recovery;
4. aluminium-housing recovery;
5. electrical-steel recovery;
6. magnet-to-magnet recycling from elemental recovery;
7. collection and separation efficiency;
8. the delay between vehicle registration and end-of-life availability.

A topology shift affects secondary supply with a time lag. EESM adoption can reduce future NdFeB scrap while increasing copper-bearing rotor material. Axial-flux adoption can alter dismantling because segmented stators and disc magnets differ from radial assemblies. PMa-SynRM may produce smaller and more dispersed magnet inventories, potentially changing recovery economics.

## 10. RAWCLIC Segment Analysis and Adoption Horizons

### 10.1 Segment mapping and 2025 use

RAWCLIC maps A to mini/city cars, B to small/subcompact, C to compact, D to mid-size, E to executive and F to luxury/flagship vehicles [15]. This report combines them into AB, CD and EF.

| Segment group | Typical role and named BEV examples | Typical installed power | Typical wheel/motor torque screening | Motor mass screening | 2025 position |
|---|---|---:|---:|---:|---|
| AB | Urban/small; Fiat 500-class and Renault small-car context | 50–120 kW | 120–300 N·m motor | 28–68 kg | PMSM dominant; cost pressure supports SynRM/EESM interest |
| CD | Compact/mid-size; VW ID.3/ID.4, Hyundai Ioniq 5/6, Tesla Model 3/Y, Renault Megane/Scenic | 100–250 kW | 240–600 N·m installed | 42–132 kg | PMSM dominant; EESM and mixed PMSM/ASM significant alternatives |
| EF | Executive/luxury; BMW i5/i7/iX and premium Mercedes-AMG context | 200–400+ kW | 480–950+ N·m installed | 68–210+ kg | Multi-motor PMSM/EESM; ASM secondary axle and axial-flux premium entry |

These are engineering screening ranges, not universal segment limits.

### 10.2 Horizon 2025

Shares are scenario-normalised and sum to 100% in every row.

| Segment group | Dominant motor type | Secondary types | Typical power | Market share by type |
|---|---|---|---:|---|
| AB | PMSM/IPM | EESM, ASM, PMa-SynRM | 75 kW | PMSM 88%; EESM 5%; ASM 4%; axial PM 0%; SynRM/PMa 3% |
| CD | PMSM/IPM | EESM, ASM, PMa-SynRM | 150 kW | PMSM 84%; EESM 7%; ASM 6%; axial PM 1%; SynRM/PMa 2% |
| EF | PMSM/IPM | EESM, ASM, axial PM | 250 kW | PMSM 78%; EESM 10%; ASM 9%; axial PM 2%; SynRM/PMa 1% |

### 10.3 Horizon 2030

The following are transparent report scenarios, not claimed market forecasts.

| Segment group | Dominant motor type | Secondary types | Typical power | Market share by type |
|---|---|---|---:|---|
| AB | PMSM/IPM | PMa-SynRM, EESM | 75 kW | PMSM 75%; EESM 8%; ASM 5%; axial PM 1%; SynRM/PMa 11% |
| CD | PMSM/IPM | EESM, ASM, PMa-SynRM | 150 kW | PMSM 72%; EESM 12%; ASM 7%; axial PM 3%; SynRM/PMa 6% |
| EF | PMSM/IPM | EESM, axial PM, ASM | 275 kW | PMSM 65%; EESM 17%; ASM 8%; axial PM 7%; SynRM/PMa 3% |

### 10.4 Horizon 2040

| Segment group | Dominant motor type | Secondary types | Typical power | Market share by type |
|---|---|---|---:|---|
| AB | PMSM/IPM | SynRM/PMa, EESM | 80 kW | PMSM 55%; EESM 12%; ASM 5%; axial PM 2%; SynRM/PMa 26% |
| CD | PMSM/IPM | EESM, SynRM/PMa, axial PM | 160 kW | PMSM 52%; EESM 21%; ASM 6%; axial PM 8%; SynRM/PMa 13% |
| EF | PMSM/IPM | EESM, axial PM | 300 kW | PMSM 45%; EESM 25%; ASM 5%; axial PM 19%; SynRM/PMa 6% |

### 10.5 Horizon 2050

| Segment group | Dominant motor type | Secondary types | Typical power | Market share by type |
|---|---|---|---:|---|
| AB | PMSM/IPM | SynRM/PMa, EESM | 80 kW | PMSM 42%; EESM 14%; ASM 5%; axial PM 3%; SynRM/PMa 36% |
| CD | PMSM/IPM | EESM, SynRM/PMa, axial PM | 165 kW | PMSM 43%; EESM 25%; ASM 5%; axial PM 12%; SynRM/PMa 15% |
| EF | PMSM/IPM | EESM and axial PM | 310 kW | PMSM 37%; EESM 28%; ASM 4%; axial PM 25%; SynRM/PMa 6% |

### 10.6 Horizon 2060: conservative, base and optimistic scenarios

“Optimistic” denotes faster diversification, material efficiency and industrialisation, not necessarily higher motor power.

| Segment group | Dominant motor type | Secondary types | Typical power | Market share by type |
|---|---|---|---:|---|
| AB—conservative | PMSM | SynRM/PMa, EESM | 80 kW | PMSM 55%; EESM 12%; ASM 5%; axial 2%; SynRM/PMa 26% |
| AB—base | SynRM/PMa | PMSM, EESM | 80 kW | PMSM 35%; EESM 15%; ASM 5%; axial 3%; SynRM/PMa 42% |
| AB—optimistic | SynRM/PMa | EESM, PMSM | 75 kW | PMSM 22%; EESM 18%; ASM 5%; axial 5%; SynRM/PMa 50% |
| CD—conservative | PMSM | EESM, SynRM/PMa | 170 kW | PMSM 50%; EESM 23%; ASM 6%; axial 8%; SynRM/PMa 13% |
| CD—base | PMSM | EESM, SynRM/PMa, axial | 165 kW | PMSM 36%; EESM 27%; ASM 5%; axial 15%; SynRM/PMa 17% |
| CD—optimistic | EESM | SynRM/PMa, axial, PMSM | 160 kW | PMSM 24%; EESM 30%; ASM 5%; axial 20%; SynRM/PMa 21% |
| EF—conservative | PMSM | EESM, axial | 320 kW | PMSM 45%; EESM 27%; ASM 5%; axial 18%; SynRM/PMa 5% |
| EF—base | EESM | Axial PM, PMSM | 310 kW | PMSM 30%; EESM 31%; ASM 4%; axial 29%; SynRM/PMa 6% |
| EF—optimistic | Axial PM | EESM, PMSM | 300 kW | PMSM 20%; EESM 31%; ASM 4%; axial 38%; SynRM/PMa 7% |

### 10.7 Horizon 2070: conservative, base and optimistic scenarios

| Segment group | Dominant motor type | Secondary types | Typical power | Market share by type |
|---|---|---|---:|---|
| AB—conservative | PMSM | SynRM/PMa, EESM | 80 kW | PMSM 50%; EESM 13%; ASM 5%; axial 3%; SynRM/PMa 29% |
| AB—base | SynRM/PMa | PMSM, EESM | 75 kW | PMSM 29%; EESM 16%; ASM 5%; axial 5%; SynRM/PMa 45% |
| AB—optimistic | SynRM/PMa | EESM, axial | 70 kW | PMSM 15%; EESM 20%; ASM 5%; axial 7%; SynRM/PMa 53% |
| CD—conservative | PMSM | EESM, SynRM/PMa | 170 kW | PMSM 46%; EESM 25%; ASM 6%; axial 10%; SynRM/PMa 13% |
| CD—base | EESM | PMSM, SynRM/PMa, axial | 160 kW | PMSM 31%; EESM 30%; ASM 5%; axial 17%; SynRM/PMa 17% |
| CD—optimistic | SynRM/PMa | EESM, axial | 155 kW | PMSM 18%; EESM 29%; ASM 5%; axial 23%; SynRM/PMa 25% |
| EF—conservative | PMSM | EESM, axial | 320 kW | PMSM 41%; EESM 29%; ASM 5%; axial 20%; SynRM/PMa 5% |
| EF—base | Axial PM | EESM, PMSM | 300 kW | PMSM 25%; EESM 32%; ASM 4%; axial 33%; SynRM/PMa 6% |
| EF—optimistic | Axial PM | EESM, SynRM/PMa | 290 kW | PMSM 14%; EESM 31%; ASM 4%; axial 43%; SynRM/PMa 8% |

## 11. Regulatory, Engineering, Safety and Practical-Market Power Limits

### 11.1 Legal and regulatory position

There is no general EU rule limiting category-B passenger cars or newly qualified category-B drivers to 100 kW. Directive (EU) 2025/2205 addresses category-B maximum authorised mass treatment and establishes an at-least-two-year probationary framework; it should not be interpreted as a general passenger-car motor-power limit. National rules, insurance practices and targeted restrictions can differ, but they must not be presented as EU-wide rules.

Motorcycle licence categories use power and power-to-weight criteria, but those categories are not transferable to passenger BEVs. National examples, including Italian new-driver provisions, are legally distinct from EU passenger-car type approval.

EU passenger-BEV type approval does not impose a general power-to-weight cap. UNECE battery, braking and tyre regulations require that vehicles demonstrate functional safety, electrical protection, braking performance and tyre capability. They do not prescribe a universal maximum kW value [[12]](https://unece.org/sites/default/files/2025-05/R100r2am5e.pdf) [[13]](https://unece.org/fileadmin/DAM/trans/main/wp29/wp29regs/R13hr2e.pdf) [[14]](https://unece.org/sites/default/files/2024-01/R0100r3e.pdf) [[21]](https://unece.org/sites/default/files/2023-05/ECE-TRANS-WP15-113-GE-inf16e_0.pdf).

### 11.2 Electrical screening

Simple DC system screening before losses gives:

| Mechanical/electrical power screen | 400 V current | 800 V current |
|---:|---:|---:|
| 50 kW | 125 A | 62.5 A |
| 75 kW | 187.5 A | 93.75 A |
| 100 kW | 250 A | 125 A |
| 150 kW | 375 A | 187.5 A |
| 200 kW | 500 A | 250 A |
| 250 kW | 625 A | 312.5 A |
| 350 kW | 875 A | 437.5 A |
| 400 kW | 1,000 A | 500 A |

These figures use `P = VI`. They are not motor phase currents, do not include inverter or motor loss and do not imply that battery voltage remains constant under load.

Higher voltage reduces current for the same power, potentially reducing conductor and semiconductor loss, but introduces insulation, switching, creepage, connector and service-safety requirements. It does not remove the thermal limits of the motor, battery or tyres.

### 11.3 Engineering screening by segment

| Segment | Kerb-mass assumption | Practical installed-power screen | Main limiting considerations |
|---|---:|---:|---|
| AB | 1.1–1.7 t | 50–150 kW | Cost, tyre width, urban efficiency, battery discharge, front-axle traction |
| CD | 1.5–2.4 t | 100–300 kW | Battery/cooling, tyre force, all-wheel-drive value, insurance |
| EF | 2.0–3.2 t | 200–500+ kW | Sustained cooling, tyre and brake rating, vehicle stability, high-speed validation |

These are screening boundaries under passenger-car assumptions, not physical or legal maxima. Short-duration peak power can exceed continuous thermal power substantially. A 400 kW urban hatchback may be technically buildable but commercially irrational; a 400 kW heavy premium vehicle may be viable with suitable battery, cooling, tyres and brakes.

### 11.4 Thermal and mechanical constraints

Continuous motor power is limited by:

- stator copper temperature;
- rotor copper temperature in ASM and EESM;
- permanent-magnet temperature in PMSM, axial PM and PMa-SynRM;
- lamination and rotor structural stress;
- bearing speed and electrical erosion;
- coolant temperature, flow and heat rejection;
- inverter semiconductor and busbar temperature;
- battery cell temperature and discharge capability.

Peak torque is limited by current, magnetic saturation, inverter capability and traction. Maximum speed is limited by rotor stress, magnet retention, flux-barrier strength, bearing speed and gearbox input limits.

### 11.5 Tyres, brakes, handling and acceleration

Motor power does not automatically produce usable tractive force. At low speed, torque is limited by tyre-road friction and axle load. At high speed, available wheel power must overcome aerodynamic and rolling resistance, while tyre speed and load ratings remain mandatory.

Regenerative braking does not eliminate the need for friction brakes. Battery charge acceptance can fall at high state of charge or low temperature, and emergency braking must remain available independently of regeneration. More installed power can therefore require larger tyres, brakes, suspension components and thermal systems even when peak output is rarely used.

High-centre-of-gravity SUVs require particular attention to roll response, lateral load transfer and combined acceleration/steering manoeuvres. Electronic stability control mitigates but does not repeal tyre-force and vehicle-dynamics limits.

### 11.6 Insurance, willingness to pay and market practicality

For AB vehicles, customers generally obtain little utility from extreme peak power relative to its battery, tyre and insurance cost. CD buyers may value 100–250 kW for motorway merging, towing or all-wheel drive. EF buyers are more likely to pay for 250–500 kW performance, but this remains constrained by insurance, tyre replacement, energy consumption and declining real-world utility.

The practical ceiling is therefore a system-level value proposition rather than a motor-only number.

## 12. Future Development and Material-Demand Scenarios

### 12.1 Outlook to 2030

**PMSM/IPM:** Continued dominance is expected, with thinner laminations, improved winding fill, reduced heavy-rare-earth content and better cooling. The supplied scenario reduces 150 kW mass from 55–72–90 kg in 2025 to 51–66–83 kg in 2030 and NdFeB to 0.8–1.3–1.8 kg [1] [3].

**ASM:** The strongest near-term role is a secondary axle, where de-energised drag and magnet avoidance are valued. Copper-cage performance and improved rotor cooling can narrow the efficiency gap, while aluminium cages offer cost and mass trade-offs.

**EESM:** BMW and Renault production experience supports expansion. Brushless or inductive excitation could reduce maintenance concerns, but rotor copper and thermal complexity remain. Adoption will be most attractive where rare-earth resilience is monetised.

**Axial-flux PM:** Premium production and manufacturing learning are decisive. YASA’s Mercedes relationship provides the clearest supplied pathway [ref180–ref189]. Prototype power-density records should remain separated from production material factors.

**SynRM/PMa-SynRM:** PM-assisted designs can expand first because they improve power factor and torque density while reducing magnet mass. Pure SynRM adoption depends on inverter-current cost, noise control and rotor mechanical validation.

### 12.2 Outlook to 2040

PMSM could reach a 44–57–72 kg 150 kW envelope in the supplied improvement scenario, with 0.6–1.0–1.5 kg NdFeB [1] [3]. This would lower motor material intensity without eliminating rare-earth exposure.

EESM may gain where supply security outweighs its mass and copper penalty. ASM is likely to retain a bounded niche. Axial-flux PM could spread from premium to selected mainstream platforms if automated segmented-stator production, air-gap control and recycling mature. SynRM/PMa-SynRM may become a major AB and CD alternative, particularly if magnet prices remain volatile.

Copper becomes a more important system constraint in scenarios with rapid EESM and SynRM growth. Aluminium conductors can reduce copper demand but require greater conductor cross-section and revised joining, insulation and thermal design. Better electrical steel can reduce loss and active mass but may increase alloy, coating and process requirements.

### 12.3 Outlook to 2050

By 2050, topology diversification is plausible but not guaranteed. A high-PMSM outcome remains credible if magnet production diversifies, heavy-rare-earth intensity falls and closed-loop recycling becomes economical. A high-EESM outcome becomes credible if excitation and rotor-cooling systems achieve lower cost and high reliability. A high-axial outcome requires manufacturing scale rather than further prototype records. A high-SynRM outcome requires acceptable inverter cost, noise and torque density.

Circular design becomes strategically important. Priority features include identifiable magnet grades, reversible rotor assembly, separable copper windings, low-contamination electrical steel and alloy-compatible housings. Recycling success can reduce primary demand but cannot satisfy rapid fleet growth until a sufficiently large end-of-life stock exists.

### 12.4 Speculative 2060–2070 scenarios

**Conservative continuity:** Radial PMSM remains the leading family. Magnet intensity falls, recycled NdFeB expands and EESM, ASM, axial PM and SynRM remain complementary. This scenario produces continuing Nd/Pr demand but lower kg/kW intensity.

**Base diversification:** No topology exceeds roughly half of all segment applications. AB shifts strongly towards SynRM/PMa-SynRM; CD uses a balanced PMSM/EESM/SynRM mix; EF divides among PMSM, EESM and axial flux. Copper, electrical steel and magnet recycling all become important.

**Optimistic circular diversification:** Pure SynRM, efficient EESM and industrialised axial-flux machines expand rapidly. PMSM remains present but uses lower magnet inventories and high recycled content. Design-for-disassembly materially improves secondary supply. This scenario is optimistic about manufacturing and circularity, not an assumption of unrestricted resource availability.

### 12.5 Decision triggers

Scenario probabilities should be updated using:

- measured motor and drive-unit bills of material;
- vehicle registrations by topology and segment;
- magnet chemistry and recycled-content disclosure;
- copper and electrical-steel price trends;
- axial-flux production yield and continuous-duty data;
- EESM excitation reliability;
- PMa-SynRM magnet inventory;
- end-of-life collection and material-recovery yields;
- EU and national industrial-policy developments.

## 13. Conclusions and Recommendations

Radial PMSM/IPM should remain the near-term benchmark for RAWCLIC demand modelling. Its 150 kW motor-only envelope is 55–72–90 kg with 1.0–1.5–2.0 kg NdFeB. The baseline is mature and decision-useful but is not a substitute for product-specific teardown data.

EESM is the strongest demonstrated rare-earth-free primary-drive alternative. The +4–+8–+15 kg total-mass and +3–+6–+10 kg rotor-copper assumptions should remain explicit scenario parameters rather than being embedded as universal facts.

ASM is strategically important for secondary axles and robust duty. It eliminates magnets but raises rotor-loss, conductor and cooling considerations. Pure SynRM similarly removes magnets while potentially increasing electrical-steel, stator-current and inverter requirements. PMa-SynRM offers a reduced-magnet intermediate pathway and must be tracked separately.

Axial-flux PM offers a plausible 10–20–30% mass-saving envelope, but the value is not universal. YASA’s short-duration record result must not be treated as a 150 kW production bill of material. DeepDrive is a relevant emerging architecture but is radial flux, not axial flux.

For the accompanying decision model, the report recommends:

1. preserve motor-only and drive-unit boundaries;
2. store min, typical and max separately;
3. distinguish peak and continuous ratings;
4. model material at vehicle level, including motor count;
5. separate radial PMSM from axial PM;
6. separate pure SynRM from PMa-SynRM;
7. record NdFeB and elemental Nd/Pr/Dy/Tb without double counting;
8. track copper, aluminium and electrical steel even in magnet-free scenarios;
9. flag parameterised estimates separately from measurements;
10. replace assumptions with verified supplier or teardown data as they become available.

The central decision is not which motor universally “wins”. It is how each topology redistributes mass, efficiency, manufacturing complexity, supply risk and future secondary-material availability across vehicle segments and time.

## 14. References and Reliability Register

The following register is selective. Reliability labels reflect source type and traceability for the stated use, not an assertion that every quantitative value in a source is directly measured.

- **[15] RAWCLIC, “BEV traction motor composition data: Deliverable 3.1—Harmonized datasets for secondary RM sources for the twin transition”, 2026. Reliability: 100%.** Official project deliverable; reviewed by RAWCLIC partners and used for system boundaries, segment definitions, regression and Monte Carlo methodology.

- **[1] “Practical BEV Traction-Motor Architecture, Weight and Materials Outlook”, internal/user-provided baseline report, September 2026. Reliability: 80%.** Consolidated engineering assessment; used for bounded motor envelopes, topology scenarios and caveats rather than claimed teardown measurements.

- **[3] “BEV Motors Practical Data v2”, internal/user-provided dataset, September 2026. Reliability: 80%.** Model-oriented companion data; used for the PMSM reference, material triplets, EESM deltas, power scaling and axial-flux scenario envelope.

- **[16] RAWCLIC consolidated BEV motor composition dataset, Version 1, 2026. Reliability: 100%.** Official harmonised project dataset containing component/material fields, uncertainty outputs, segment assignments and source metadata.

- **[[18]](https://www.epj-conferences.org/articles/epjconf/pdf/2025/26/epjconf_icatcict2025_01019.pdf) Peer-reviewed traction-motor review evidence. Reliability: 80%.** Academic source used for general comparative efficiency and technology characteristics.

- **[[17]](https://www.hub-edrive.de/fileadmin/media/Publikation/Advances_in_electricmotors.pdf) Drexler et al., “Advances in electric motors: a review and benchmarking of product design and manufacturing technologies”, 2025. Reliability: 80%.** Peer-reviewed benchmarking study covering 48 motors from 31 passenger vehicles; methodological anchor for RAWCLIC component–torque relationships.

- **[[9]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/german-entrepreneurship-award-for-tum-spin-off-deepdrive) Technical University of Munich information on DeepDrive. Reliability: 80%.** University source used for institutional origin and award-related context.

- **[[4]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en) BMW Group press information. Reliability: 80%.** Primary OEM source used for BMW electrically excited drivetrain deployment.

- **[[10]](https://www.deepdrive.tech/media/deepdrive-presents-generator) DeepDrive company information. Reliability: 60%.** Primary manufacturer source; relevant to architecture description, with performance and material claims treated as attributed rather than independent validation.

- **[[5]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) Renault Group information. Reliability: 80%.** Primary OEM source used for Renault EESM strategy and production context.

- **[[6]](https://yasa.com/) YASA company information. Reliability: 60%.** Primary manufacturer source used for axial-flux architecture and company-reported performance; record claims are not treated as production benchmarks.

- **[[8]](https://yasa.com/technology/) YASA technical/company publication. Reliability: 60%.** Manufacturer evidence used for attributed prototype performance.

- **[[7]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) Mercedes-Benz Group information on YASA and axial-flux industrialisation. Reliability: 80%.** Primary OEM source used for ownership and production-strategy context.

- **[[11]](https://www.deepdrive.tech/news/unleashing-efficiency-revolutionizing-electric-vehicle-technologydeepdrive-deepdive-part-2) DeepDrive company technical information. Reliability: 60%.** Primary manufacturer source used to identify the dual-rotor radial-flux concept; range and material claims remain company-attributed.

- **[[20]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/presidential-award-for-space-start-up) Technical University of Munich information concerning DeepDrive. Reliability: 80%.** University source supporting the spin-off and technology context.

- **[[2]](https://www.iea.org/reports/global-ev-outlook-2026/trends-in-electric-cars) International Energy Agency information on EV motor and critical-material use. Reliability: 100%.** Intergovernmental source used for present permanent-magnet market direction and critical-material context.

- **[[12]](https://unece.org/sites/default/files/2025-05/R100r2am5e.pdf) United Nations Economic Commission for Europe material on vehicle electrical/battery safety. Reliability: 100%.** Official regulatory source; used to distinguish functional safety requirements from power caps.

- **[[13]](https://unece.org/fileadmin/DAM/trans/main/wp29/wp29regs/R13hr2e.pdf) UNECE regulatory material. Reliability: 100%.** Official source used for vehicle safety and approval context.

- **[[14]](https://unece.org/sites/default/files/2024-01/R0100r3e.pdf) UNECE regulatory material concerning braking or vehicle safety. Reliability: 100%.** Official source used to establish that safety requirements are performance-based rather than universal passenger-car kW limits.

- **[[21]](https://unece.org/sites/default/files/2023-05/ECE-TRANS-WP15-113-GE-inf16e_0.pdf) UNECE regulatory material concerning tyres or vehicle safety. Reliability: 100%.** Official regulatory source used for tyre capability and type-approval context.

- **[[22]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140892/JRC140892_01.pdf) European Commission Joint Research Centre publication on materials and clean-energy technologies. Reliability: 100%.** Official scientific-policy source supporting critical-material and circularity framing.

---

## References

1. BEV_Motors_Practical_Report_v2.md (uploaded document)
2. <https://www.iea.org/reports/global-ev-outlook-2026/trends-in-electric-cars>
3. BEV_Motors_Practical_Data_v2.xlsx (uploaded document)
4. <https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en>
5. <https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/>
6. <https://yasa.com/>
7. <https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html>
8. <https://yasa.com/technology/>
9. <https://www.tum.de/en/news-and-events/all-news/press-releases/details/german-entrepreneurship-award-for-tum-spin-off-deepdrive>
10. <https://www.deepdrive.tech/media/deepdrive-presents-generator>
11. <https://www.deepdrive.tech/news/unleashing-efficiency-revolutionizing-electric-vehicle-technologydeepdrive-deepdive-part-2>
12. <https://unece.org/sites/default/files/2025-05/R100r2am5e.pdf>
13. <https://unece.org/fileadmin/DAM/trans/main/wp29/wp29regs/R13hr2e.pdf>
14. <https://unece.org/sites/default/files/2024-01/R0100r3e.pdf>
15. RAWCLIC_BEV_motor_consolidated_data_description-V1.pdf (uploaded document)
16. RAWCLIC_BEV_motor_consolidated_data_V1.xlsx (uploaded document)
17. <https://www.hub-edrive.de/fileadmin/media/Publikation/Advances_in_electricmotors.pdf>
18. <https://www.epj-conferences.org/articles/epjconf/pdf/2025/26/epjconf_icatcict2025_01019.pdf>
19. <https://media.mercedes-benz.com/en/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf>
20. <https://www.tum.de/en/news-and-events/all-news/press-releases/details/presidential-award-for-space-start-up>
21. <https://unece.org/sites/default/files/2023-05/ECE-TRANS-WP15-113-GE-inf16e_0.pdf>
22. <https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140892/JRC140892_01.pdf>
