# Critical Review: BEV Traction Motor Material Composition — Source Cross-Validation and Value Confirmation

*RAWCLIC Project Critical Review / September 2026*

## 1. Review mandate, method and status framework

### 1.1 Scope of the audit

✅ CONFIRMED — This review audits the material, mass, power-density, market-adoption, technology-development and regulatory claims in the original “Practical BEV Traction-Motor Architecture, Weight and Materials Outlook.” The original report is treated only as the claim under review, not as independent corroboration [1].

✅ CONFIRMED — The associated RAWCLIC Deliverable 3.1 models BEV traction-motor composition for permanent-magnet motors, induction motors and electrically excited synchronous machines. Its numerical dataset is intended for vehicle-segment stock-and-flow modelling, and component weights are reported at vehicle level rather than necessarily per individual motor [2].

🔧 ADJUSTED — The central audit question is therefore not whether an original value is plausible, but whether independent evidence confirms the same topology, power rating, duty rating, component boundary and number of motors per vehicle. Values failing any of these boundary tests are retained only as planning assumptions or marked as gaps.

### 1.2 Systematic cross-validation procedure

✅ CONFIRMED — The review applies five sequential tests:

1. **Claim identification:** capture the original Min | Mode | Max and determine whether it concerns a measured product, generalized motor class or constructed scenario [1].
2. **Source independence:** exclude the original report and RAWCLIC workbook as independent confirmation of their own values [2] [1].
3. **Boundary matching:** distinguish motor-only from inverter, gearbox, differential, cooling circuit, retained fluid, e-axle and complete vehicle-level propulsion boundaries.
4. **Rating matching:** distinguish peak or short-duration power from continuous thermally sustainable power.
5. **Triangulation:** require two or three independent eligible sources for every confirmed or adjusted numerical value.

🔧 ADJUSTED — A source does not become independent merely because the same supplier claim is repeated by automotive media. Supplier specifications and reports quoting those specifications remain one originating evidence stream unless separate testing or peer-reviewed characterization is available.

### 1.3 Reliability grading

| Evidence class | Reliability | Audit treatment | Status |
|---|---:|---|---|
| Peer-reviewed literature, EU deliverables and standards | 100% | Highest evidentiary weight; still requires matching system and duty boundaries | ✅ CONFIRMED |
| Industry analysts, national laboratories, JRC and Fraunhofer | 80% | Strong directional or benchmark evidence; proprietary forecast methods remain a limitation | ✅ CONFIRMED |
| OEM or supplier press, white papers and established technical automotive journalism | 60% | Suitable for topology and disclosed specifications; performance remains company-attributed without independent testing | 🔧 ADJUSTED |
| Recognised engineering news and conference presentations | 40% | Corroborative only, especially for prototypes and claimed records | 🔧 ADJUSTED |

✅ CONFIRMED — Sources below 40% are excluded. Wikipedia, Reddit, personal blogs, general market-report aggregators, search snippets and ResearchGate copies are not used as evidence.

### 1.4 Source-boundary controls

| Boundary issue | Required audit treatment | Status |
|---|---|---|
| Motor-only versus e-axle | Do not use an e-axle or drive-unit mass as motor mass unless separable subassembly masses are disclosed | ✅ CONFIRMED |
| Peak versus continuous power | Report the relevant rating explicitly; do not divide peak power by mass and present the result as continuous density | ✅ CONFIRMED |
| One motor versus vehicle total | Preserve both per-motor and per-vehicle values; never normalize a dual-motor vehicle to one motor without disclosure | ✅ CONFIRMED |
| Housing and cooling | State whether the housing, end shields, coolant jacket, pump, hoses and retained fluid are included | ✅ CONFIRMED |
| Axial versus radial flux | Treat flux direction separately from magnet type; most axial-flux traction machines reviewed here are permanent-magnet machines | ✅ CONFIRMED |
| Installed versus marketed share | Do not merge vehicle-model availability, vehicle registrations and installed-motor counts | ✅ CONFIRMED |
| Nominal “150 kW class” | Require evidence that 150 kW refers to the individual motor and identify whether it is peak or continuous | ✅ CONFIRMED |

### 1.5 Status definitions

| Status tag | Meaning | Status |
|---|---|---|
| ✅ CONFIRMED | Independently supported under a materially comparable boundary; numerical findings require two or three independent sources | ✅ CONFIRMED |
| ⚠️ CONTRADICTION | Eligible sources or the original report materially disagree, and the difference cannot be explained fully by boundary control | ⚠️ CONTRADICTION |
| 🔧 ADJUSTED | Direction is supported, but the number, interpretation, attribution or boundary must be changed | 🔧 ADJUSTED |
| ❓ GAP | Public evidence is insufficient to support a numerical value under a comparable boundary | ❓ GAP |

## 2. Evidence-base integrity and principal findings

### 2.1 Overall verdict

🔧 ADJUSTED — The original report is strongest on qualitative architecture direction and weakest on 150 kW-normalized bills of material. Public evidence supports PMSM importance, rare-earth supply exposure, production use of EESM, specialized axial-flux commercialization and the central importance of thermal boundaries, but it does not validate most component-level Min | Mode | Max triplets [[3]](https://www.iea.org/reports/rare-earth-elements/executive-summary) [[4]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140892/JRC140892_01.pdf) [[5]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142055/JRC142055_01.pdf) [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) [[7]](https://www.idtechex.com/en/research-article/permanent-magnet-and-wrsm-idtechex-explores-ev-motors/32181).

❓ GAP — No supplied independent evidence provides a complete, independently weighed, motor-only bill of material for a representative 150 kW radial IPM/PMSM with matched peak or continuous rating. Consequently, the original stator, copper, rotor, magnet, shaft, housing, bearing, cooling and sensor masses cannot be called confirmed [2] [1].

🔧 ADJUSTED — RAWCLIC’s torque-regression method is appropriate for scenario modelling only if the input component observations and vehicle-level motor-count boundary are visible. A regression confidence interval quantifies uncertainty around the fitted relationship; it does not correct source-boundary errors or convert sparse product observations into directly measured 150 kW bills of material [2].

### 2.2 Evidence streams retained

| Evidence stream | Audit use | Principal eligible source base | Status |
|---|---|---|---|
| Rare-earth demand and motor dependence | Direction, supply concentration and substitution pressure | IEA, JRC and EU sources [[3]](https://www.iea.org/reports/rare-earth-elements/executive-summary) [[8]](https://www.iea.org/reports/the-role-of-critical-minerals-in-clean-energy-transitions/executive-summary) [[4]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140892/JRC140892_01.pdf) [[9]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC122671/jrc122671_the_role_of_rare_earth_elements_in_wind_energy_and_electric_mobility_2.pdf) [[10]](https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/innovative-requirements-could-boost-circular-economy-plastics-and-critical-raw-materials-vehicles-2023-07-13_en) [[11]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC141759/JRC141759_01.pdf) [[12]](https://single-market-economy.ec.europa.eu/sectors/raw-materials/areas-specific-interest/rare-earth-elements-permanent-magnets-and-motors_en) [[13]](https://www.iea.org/topics/critical-minerals) [[14]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC120312/policyreport_assessment_of_magnetic_fields_in_electrified_vehicles_final2.pdf) [[5]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142055/JRC142055_01.pdf) | ✅ CONFIRMED |
| Production topology | OEM confirmation of EESM, axial-flux and integrated drive strategies | Renault, BMW, Mercedes-Benz and supplier sources [[15]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en) [[16]](https://www.press.bmwgroup.com/usa/article/detail/T0443395EN_US/the-all-new-2025-bmw-m5) [[17]](https://www.press.bmwgroup.com/usa/article/attachment/T0443395EN_US/618783) [[18]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[19]](https://media.renault.com/all-new-megane-e-tech-electric-delving-into-the-heart-of-innovation-episode-3/) [[20]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/e7a-the-next-gen-electric-motor-developed-by-renault-and-valeo/) [[21]](https://www.valeo.com/en/renault-group-valeo-and-valeo-siemens-eautomotive-join-forces-to-develop-and-manufacture-a-new-generation-automotive-electric-motor-in-france/) [[22]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) [[23]](https://media.mercedes-benz.com/en/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf) [[24]](https://group.mercedes-benz.com/company/strategy/mercedes-benz-strategy-update-electric-drive.html) | ✅ CONFIRMED |
| Motor research and benchmarking | Topology, thermal limits, recycling and design trade-offs | Peer-reviewed and national-laboratory sources [[25]](https://info.ornl.gov/sites/publications/Files/Pub57320.pdf) [[26]](https://www.osti.gov/servlets/purl/1825650) [[27]](https://www.sciencedirect.com/science/article/pii/S1364032126007021) [[28]](https://www.sciencedirect.com/science/article/pii/S0306261923018603) [[29]](https://www.mdpi.com/2032-6653/13/4/65) [[30]](https://www.mdpi.com/1996-1073/19/18/4316) [[31]](https://www.mdpi.com/1996-1073/18/9/2274) [[32]](https://pubs.aip.org/aip/adv/article/10/2/025105/1021639/Performance-verification-of-DR-PMSM-for-traction) [[33]](https://www.sciencedirect.com/science/article/pii/S2773153722000123) [[34]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10890235/) [[35]](https://www.sciencedirect.com/science/article/pii/S2590123026013034) [[36]](https://link.springer.com/article/10.1007/s11837-022-05594-5) | ✅ CONFIRMED |
| Axial-flux performance | Product specifications plus independent technical literature | YASA, IEEE and peer-reviewed sources [[37]](https://yasa.com/) [[38]](https://yasa.com/technology/) [[39]](https://yasa.com/about/) [[40]](https://yasa.com/yasa-mercedes-benz/) [[41]](https://yasa.com/automotive/) [[42]](https://ieeexplore.ieee.org/document/10360216/) [[43]](https://www.sciencedirect.com/science/article/pii/S1000936125006685) [[44]](https://www.sciencedirect.com/science/article/pii/S2352484722014767) [[45]](https://www.mdpi.com/2075-1702/13/10/954) [[46]](https://cjme.springeropen.com/articles/10.1186/s10033-023-00868-8) | 🔧 ADJUSTED |
| Circularity and secondary magnets | Policy obligations, recycling routes and life-cycle effects | EU, JRC and peer-reviewed sources [[47]](https://single-market-economy.ec.europa.eu/sectors/raw-materials/areas-specific-interest/critical-raw-materials/critical-raw-materials-act_en) [[48]](https://commission.europa.eu/topics/competitiveness/green-deal-industrial-plan/european-critical-raw-materials-act_en) [[49]](https://www.mdpi.com/2075-4701/14/6/658) [[50]](https://link.springer.com/article/10.1007/s11837-023-06235-1) [[51]](https://www.sciencedirect.com/science/article/abs/pii/S1383586623004355) [[52]](https://www.sciencedirect.com/science/article/abs/pii/S2452223624000051) [[53]](https://www.sciencedirect.com/science/article/abs/pii/S1383586625033003) [[54]](https://www.sciencedirect.com/science/article/pii/S0304885323011253) [[55]](https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng) [[56]](https://eur-lex.europa.eu/EN/legal-content/summary/a-secure-and-sustainable-supply-of-critical-raw-materials.html) | ✅ CONFIRMED |
| Long-term architecture adoption | Direction only; scenario values require explicit labelling | IEA, IDTechEx and JRC [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[3]](https://www.iea.org/reports/rare-earth-elements/executive-summary) [[4]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140892/JRC140892_01.pdf) [[5]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142055/JRC142055_01.pdf) [[7]](https://www.idtechex.com/en/research-article/permanent-magnet-and-wrsm-idtechex-explores-ev-motors/32181) [[58]](https://www.idtechex.com/en/research-article/the-ev-market-doubles-down-on-permanent-magnets-despite-material-costs/28314) [[59]](https://www.idtechex.com/en/research-article/the-evolution-of-modern-electric-motor-market-for-electric-vehicles/29506) [[60]](https://www.idtechex.com/en/research-article/axial-flux-traction-motor-with-15-advantage/9643) | 🔧 ADJUSTED |

### 2.3 Values that survive cross-validation

✅ CONFIRMED — NdFeB traction magnets contain Nd and Pr as principal magnet rare earths, with Dy or Tb potentially used to improve coercivity and high-temperature performance [[34]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10890235/) [[9]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC122671/jrc122671_the_role_of_rare_earth_elements_in_wind_energy_and_electric_mobility_2.pdf) [[61]](https://pubs.aip.org/aip/adv/article/15/7/075206/3351613/Microstructure-and-super-high-coercivity-of-Tb).

✅ CONFIRMED — EESM and induction architectures eliminate rare-earth permanent magnets from the rotor, although they do not eliminate copper, electrical steel, housing, insulation or thermal-system requirements [[4]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140892/JRC140892_01.pdf) [[5]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142055/JRC142055_01.pdf) [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html).

🔧 ADJUSTED — PM traction motors are dominant, but the original mutually exclusive 78% | 85% | 92% radial-IPM share is not directly supported. The eligible evidence supports PM motor share above 75% since 2015 and separate estimates around 85% or above 90%, depending on vehicle, geography and counting scope [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[62]](https://www.iea.org/reports/global-ev-outlook-2026/trends-in-electric-cars) [[3]](https://www.iea.org/reports/rare-earth-elements/executive-summary) [[7]](https://www.idtechex.com/en/research-article/permanent-magnet-and-wrsm-idtechex-explores-ev-motors/32181).

✅ CONFIRMED — Axial-flux machines can provide a short axial package and high torque or power density, but performance depends on topology, cooling, mechanical containment and whether peak or continuous power is used [[63]](https://www.sciencedirect.com/science/article/pii/S2773186324000963) [[64]](https://www.hub-edrive.de/fileadmin/media/Publikation/Comprehensive_Review_and_Systemization_of_the_Product_Features_of_Axial_Flux_Machines.pdf) [[65]](https://www.mdpi.com/2227-7390/12/19/2981) [[66]](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/elp2.12218) [[43]](https://www.sciencedirect.com/science/article/pii/S1000936125006685).

🔧 ADJUSTED — A YASA P400-class value around 160 kW and 24–28.2 kg supports a peak motor-only density of approximately 5.7–6.7 kW/kg, not the original generic 3 | 5 | 8 kW/kg “production-oriented” band and not a continuous-density conclusion [[42]](https://ieeexplore.ieee.org/document/10360216/) [[67]](https://yasa.com/media/2021/05/yasa-p400rdatasheet-rev-14.pdf) [[68]](http://vialidad.usb.ve/materias/ec5136/Motores_axiales/YASA_P400_Product_Sheet.pdf).

✅ CONFIRMED — DeepDrive is independently identified through Technical University of Munich sources as a TUM spin-off [[69]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/german-entrepreneurship-award-for-tum-spin-off-deepdrive) [[70]](https://www.mec.ed.tum.de/fileadmin/w00cbp/am/_my_direct_uploads/2023_ECAM_Slimak.pdf) [[71]](https://www.ie.mgt.tum.de/en/ent/tum-start-up-incubator/) [[72]](https://www.tum.de/en/innovation/) [[73]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/presidential-award-for-space-start-up) [[74]](https://www.mgt.tum.de/unlock-the-brain-tum-startup-develops-neurotechnology-based-playtesting/).

🔧 ADJUSTED — DeepDrive’s motor is a dual-rotor radial-flux topology, with a stator between inner and outer rotors; it is not an axial-flux architecture. Quantitative savings in magnet mass, iron, cost or efficiency remain company-attributed unless independently tested [[75]](https://chargedevs.com/newswire/deepdrive-unveils-new-dual-rotor-radial-flux-drive-unit-for-evs/) [[76]](https://www.deepdrive.tech/news/unleashing-efficiency-revolutionizing-electric-vehicle-technologydeepdrive-deepdive-part-2) [[73]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/presidential-award-for-space-start-up) [[77]](https://www.deepdrive.tech/technology).

## 3. Architecture mix and adoption claims

### 3.1 Current market position

| Architecture claim | Original Min | Original Mode | Original Max | Revised Min | Revised Mode | Revised Max | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| Radial IPM/PMSM current share | 78% | 85% | 92% | — | — | — | ❓ GAP |
| EESM/WRSM current share | 4% | 7% | 10% | — | — | — | ❓ GAP |
| Induction current share | 3% | 6% | 10% | — | — | — | ❓ GAP |
| Axial-flux current share | 0% | 1% | 2% | — | — | — | ❓ GAP |
| PM-motor market direction | Not separately stated | Approximately 85% to above 90% | Not separately stated | >75% | approximately 85% | >90% under broader scope | 🔧 ADJUSTED |

🔧 ADJUSTED — Evidence supports continued PM-motor dominance, but “PM motor” is not synonymous with “radial IPM.” Axial-flux PM machines and PM-assisted reluctance machines may fall inside a PM total while being separated in the original architecture table [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[4]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140892/JRC140892_01.pdf) [[5]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142055/JRC142055_01.pdf) [[7]](https://www.idtechex.com/en/research-article/permanent-magnet-and-wrsm-idtechex-explores-ev-motors/32181).

⚠️ CONTRADICTION — The original architecture table describes its typical column as approximately normalized, but 85% + 7% + 6% + 1% equals 99%, while the individual uncertainty ranges overlap and use different classification concepts. The larger issue is that axial flux describes flux orientation whereas PMSM describes excitation, so the categories are not naturally mutually exclusive [1] [[63]](https://www.sciencedirect.com/science/article/pii/S2773186324000963) [[64]](https://www.hub-edrive.de/fileadmin/media/Publikation/Comprehensive_Review_and_Systemization_of_the_Product_Features_of_Axial_Flux_Machines.pdf).

### 3.2 2030–2040 scenarios

❓ GAP — The original 2030, 2035 and 2040 architecture shares are scenario construction rather than confirmed forecasts. The supplied analyst evidence supports continuing PM dominance through 2035 and increased interest in magnet-free, axial-flux and in-wheel technologies, but it does not independently reproduce the report’s topology-specific triplets [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[78]](https://www.idtechex.com/en/research-report/electric-motors-for-electric-vehicles/1131) [[79]](https://www.idtechex.com/en/research-article/new-idtechex-report-electric-motors-for-electric-vehicles-2026-2036/33926) [[7]](https://www.idtechex.com/en/research-article/permanent-magnet-and-wrsm-idtechex-explores-ev-motors/32181) [[58]](https://www.idtechex.com/en/research-article/the-ev-market-doubles-down-on-permanent-magnets-despite-material-costs/28314) [[59]](https://www.idtechex.com/en/research-article/the-evolution-of-modern-electric-motor-market-for-electric-vehicles/29506).

🔧 ADJUSTED — The only defensible quantitative trajectory in the supplied material is that one analyst direction places magnet-free automotive motors at approximately 9% in 2023 and approximately 30% in 2035. This does not determine the separate EESM and induction shares and must not be reallocated between them without the underlying dataset [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[7]](https://www.idtechex.com/en/research-article/permanent-magnet-and-wrsm-idtechex-explores-ev-motors/32181) [[59]](https://www.idtechex.com/en/research-article/the-evolution-of-modern-electric-motor-market-for-electric-vehicles/29506).

| Horizon | Original interpretation | Revised interpretation | Status |
|---|---|---|---|
| 2025/current | Four mutually exclusive topology shares | PM dominance supported; topology-specific installed shares unresolved | 🔧 ADJUSTED |
| 2030 | Near-term share forecast | Scenario only; direction supported, exact shares unconfirmed | ❓ GAP |
| 2035 | EESM and axial-flux expansion | Diversification supported; allocation by topology unconfirmed | 🔧 ADJUSTED |
| 2040 | Radial IPM mode falls to 61% | Speculative scenario without independent topology forecast | ❓ GAP |

### 3.3 2050–2070 scenarios

❓ GAP — The original 2045 and 2050 architecture shares are not independently corroborated. No supplied eligible source provides a comparable global or European installed-motor forecast dividing radial IPM, EESM, induction and axial flux through 2050 [1] [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[3]](https://www.iea.org/reports/rare-earth-elements/executive-summary).

❓ GAP — The evidence on high-temperature superconducting motors concerns specialized aerospace, marine or heavy-duty research and cryogenic-system challenges. It does not support assigning passenger-BEV market shares for 2050–2070 [[80]](https://www.sciencedirect.com/science/article/pii/S2352484722025628) [[81]](https://global-sei.com/technology/tr/bn75/pdf/75-11.pdf) [[82]](https://ieeexplore.ieee.org/document/182730) [[83]](https://technology.nasa.gov/patent/LEW-TOPS-140) [[84]](https://global-sei.com/technology/tr/bn67/pdf/67-05.pdf).

🔧 ADJUSTED — The evidence-supported long-term statement is limited to likely diversification under rare-earth supply pressure, continuing improvement in PM technology, and uncertain commercialization of alternative topologies. Numerical passenger-car shares beyond 2040 remain speculative scenario inputs [[3]](https://www.iea.org/reports/rare-earth-elements/executive-summary) [[4]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140892/JRC140892_01.pdf) [[5]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142055/JRC142055_01.pdf) [[59]](https://www.idtechex.com/en/research-article/the-evolution-of-modern-electric-motor-market-for-electric-vehicles/29506).

## 4. Motor mass, material composition and power density

### 4.1 The 150 kW radial IPM/PMSM bill of material

| Component | Original Min | Original Mode | Original Max | Independently revised Min | Mode | Max | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| Stator laminations | 18.0 kg | 23.0 kg | 28.0 kg | — | — | — | ❓ GAP |
| Stator copper | 8.0 kg | 11.0 kg | 14.0 kg | — | — | — | ❓ GAP |
| Rotor laminations | 10.0 kg | 14.0 kg | 18.0 kg | — | — | — | ❓ GAP |
| NdFeB magnets | 1.0 kg | 1.5 kg | 2.0 kg | — | — | — | ❓ GAP |
| Shaft | 3.0 kg | 4.5 kg | 6.0 kg | — | — | — | ❓ GAP |
| Housing and end shields | 8.0 kg | 12.0 kg | 17.0 kg | — | — | — | ❓ GAP |
| Bearings and seals | 1.0 kg | 1.7 kg | 2.5 kg | — | — | — | ❓ GAP |
| Cooling hardware and fluid | 2.0 kg | 4.0 kg | 7.0 kg | — | — | — | ❓ GAP |
| Sensors and resolver | 0.3 kg | 0.7 kg | 1.2 kg | — | — | — | ❓ GAP |
| Total motor weight | 55 kg | 72 kg | 90 kg | — | — | — | ❓ GAP |
| Motor power density | 1.7 kW/kg | 2.1 kW/kg | 2.7 kW/kg | — | — | — | ❓ GAP |

❓ GAP — Peer-reviewed sources confirm the physical material structure—electrical-steel stator and rotor cores, copper windings, permanent magnets where applicable, shaft, housing, insulation and bearings—but do not validate the original component masses for a matched 150 kW production motor [[25]](https://info.ornl.gov/sites/publications/Files/Pub57320.pdf) [[27]](https://www.sciencedirect.com/science/article/pii/S1364032126007021) [[28]](https://www.sciencedirect.com/science/article/pii/S0306261923018603) [[29]](https://www.mdpi.com/2032-6653/13/4/65) [[85]](https://link.springer.com/article/10.1007/s43939-026-00679-3) [[86]](https://www.sciencedirect.com/topics/engineering/permanent-magnet-synchronous-motor) [[87]](https://doi.org/10.3390/vehicles8030066).

🔧 ADJUSTED — The original report’s 55 | 72 | 90 kg total corresponds arithmetically to 2.73 | 2.08 | 1.67 kW/kg at 150 kW, but this relationship does not validate either the mass or the power rating. The reported order of 1.7 | 2.1 | 2.7 kW/kg reverses the associated mass order and should be treated as a separately constructed range [1].

⚠️ CONTRADICTION — Recognised engineering evidence places contemporary motor-level power-density benchmarks materially above 1.7–2.7 kW/kg in some production and demonstrator contexts, while integrated-system values can be much lower. The disagreement cannot be resolved without knowing whether the original 150 kW is continuous, peak or vehicle-system power [[88]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) [[89]](https://docs.nrel.gov/docs/fy21osti/75994.pdf) [[90]](https://www.borgwarner.com/technologies/electric-drive-motors).

### 4.2 Magnet allowance and elemental composition

🔧 ADJUSTED — Independent evidence supports a broad traction-motor magnet range of approximately 0.5–3 kg, but not a power-normalized 1.0 | 1.5 | 2.0 kg range specifically for a 150 kW motor. The original value is plausible as a planning band but remains unconfirmed [[9]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC122671/jrc122671_the_role_of_rare_earth_elements_in_wind_energy_and_electric_mobility_2.pdf) [[91]](https://www.sciencedirect.com/science/article/pii/S0921344924005573) [[92]](https://www.benchmarkminerals.com/glossary/what-are-rare-earths).

| Magnet parameter | Original Min | Original Mode | Original Max | Revised result | Status |
|---|---:|---:|---:|---|---|
| NdFeB in a 150 kW IPM | 1.0 kg | 1.5 kg | 2.0 kg | No matched 150 kW triplet; broad traction evidence approximately 0.5–3 kg | 🔧 ADJUSTED |
| Nd in motor | 0.25 kg | 0.38 kg | 0.55 kg | No verified 150 kW elemental BOM | ❓ GAP |
| Pr in motor | 0.03 kg | 0.08 kg | 0.15 kg | No verified 150 kW elemental BOM | ❓ GAP |
| Dy in motor | 0.01 kg | 0.05 kg | 0.12 kg | No verified 150 kW elemental BOM | ❓ GAP |
| Tb in motor | 0.00 kg | 0.01 kg | 0.03 kg | No verified 150 kW elemental BOM | ❓ GAP |

✅ CONFIRMED — Published magnet evidence supports NdFeB compositions containing approximately 29–32% Nd and approximately 1–2% boron, with iron forming most of the balance and optional Dy, Tb or other additions. This chemistry does not determine motor-level elemental masses until magnet mass and grade are known [[34]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10890235/) [[61]](https://pubs.aip.org/aip/adv/article/15/7/075206/3351613/Microstructure-and-super-high-coercivity-of-Tb) [[49]](https://www.mdpi.com/2075-4701/14/6/658).

🔧 ADJUSTED — The original Dy range of 0.5% | 3% | 8% and Tb range of 0% | 0.5% | 2% are better interpreted as broad magnet-grade chemistry assumptions than as a confirmed representative 2025 traction-magnet distribution [[34]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10890235/) [[36]](https://link.springer.com/article/10.1007/s11837-022-05594-5) [[61]](https://pubs.aip.org/aip/adv/article/15/7/075206/3351613/Microstructure-and-super-high-coercivity-of-Tb).

🔧 ADJUSTED — Grain-boundary diffusion can reduce heavy-rare-earth use by concentrating Dy or Tb near grain boundaries, but the supplied evidence supports reductions around 50% or a broader 50–70% process range—not an independently validated 2030 industry-wide 50% | 60% | 70% outcome [[34]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10890235/) [[93]](https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119792918.ch14) [[94]](https://www.sciencedirect.com/science/article/abs/pii/S0956053X18306809).

### 4.3 Scaling from 75 to 400 kW

❓ GAP — The original motor-mass and magnet-mass rows for 75, 100, 200, 250, 350 and 400 kW are not supported by matched public measurements. Motor mass does not scale uniquely with rated power because speed, torque, duration, cooling, topology and integration change simultaneously [1] [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) [[95]](https://www.ifam.fraunhofer.de/en/magazine/electric-drives.html).

⚠️ CONTRADICTION — The original report cautions that power does not scale linearly with mass, yet provides a complete ladder of smooth mass and magnet triplets without a disclosed sizing model or matched empirical dataset. The caution is valid; the numerical ladder is not independently reproducible [1].

## 5. EESM, induction, ferrite and synchronous-reluctance alternatives

### 5.1 EESM comparison

✅ CONFIRMED — Renault and BMW public material confirms that current-excited or electrically excited synchronous traction machines are production strategies rather than purely academic alternatives [[15]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en) [[16]](https://www.press.bmwgroup.com/usa/article/detail/T0443395EN_US/the-all-new-2025-bmw-m5) [[18]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[19]](https://media.renault.com/all-new-megane-e-tech-electric-delving-into-the-heart-of-innovation-episode-3/) [[20]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/e7a-the-next-gen-electric-motor-developed-by-renault-and-valeo/).

✅ CONFIRMED — EESM eliminates the traction permanent magnet but adds rotor excitation, rotor conductors and associated control and thermal requirements [[29]](https://www.mdpi.com/2032-6653/13/4/65) [[30]](https://www.mdpi.com/1996-1073/19/18/4316) [[31]](https://www.mdpi.com/1996-1073/18/9/2274) [[5]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142055/JRC142055_01.pdf) [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html).

| EESM parameter relative to IPM | Original Min | Original Mode | Original Max | Revised value | Status |
|---|---:|---:|---:|---|---|
| Motor-mass difference | +4 kg | +8 kg | +15 kg | No comparable public triplet | ❓ GAP |
| Additional rotor copper | 3 kg | 6 kg | 10 kg | No comparable public triplet | ❓ GAP |
| Highway efficiency difference | −1.5 pp | −0.5 pp | +0.5 pp | Direction depends on operating point; no universal triplet | ❓ GAP |
| NdFeB reduction | 1.0 kg | 1.5 kg | 2.0 kg | Magnet eliminated relative to the selected IPM baseline; absolute amount unresolved | 🔧 ADJUSTED |

⚠️ CONTRADICTION — Comparative studies do not establish a universal highway-speed efficiency penalty for EESM. Results vary with motor optimization, field excitation, speed, load and cooling, so a single cross-vehicle triplet can cross zero without providing a decision-useful central estimate [[29]](https://www.mdpi.com/2032-6653/13/4/65) [[30]](https://www.mdpi.com/1996-1073/19/18/4316) [[96]](https://www.mdpi.com/2032-6653/16/11/633) [[97]](https://www.mdpi.com/2075-1702/12/6/361).

### 5.2 Induction machines

✅ CONFIRMED — Induction motors avoid permanent magnets and therefore avoid Nd, Pr, Dy and Tb in the rotor magnet system, while retaining substantial electrical-steel, conductor and cooling requirements [[4]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140892/JRC140892_01.pdf) [[5]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142055/JRC142055_01.pdf) [[95]](https://www.ifam.fraunhofer.de/en/magazine/electric-drives.html).

❓ GAP — The original current and future induction shares are not confirmed because evidence mixes primary traction motors, secondary axle motors, vehicle models and installed motors [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[7]](https://www.idtechex.com/en/research-article/permanent-magnet-and-wrsm-idtechex-explores-ev-motors/32181) [[59]](https://www.idtechex.com/en/research-article/the-evolution-of-modern-electric-motor-market-for-electric-vehicles/29506).

### 5.3 Ferrite and synchronous-reluctance alternatives

✅ CONFIRMED — Ferrite-assisted synchronous-reluctance machines are an active rare-earth-free or rare-earth-reduced research route. Ferrite can improve power factor and torque relative to a pure synchronous-reluctance rotor, but its lower magnetic performance requires topology and volume compensation [[27]](https://www.sciencedirect.com/science/article/pii/S1364032126007021) [[87]](https://doi.org/10.3390/vehicles8030066) [[98]](https://ieeexplore.ieee.org/document/7542569/) [[99]](https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/iet-epa.2018.5891).

✅ CONFIRMED — The ReFreeDrive evidence includes a 200 kW peak synchronous-reluctance design and a 75 kW peak scaled version, demonstrating technical development at traction-relevant power rather than proving mass-market adoption [[100]](https://www.refreedrive.eu/wp-content/downloads/2018_Coiltech_ReFreeDrive_UnivLAquila_SynchronousReluctanceMotorForTractionApplications.pdf) [[101]](https://www.electricmotorengineering.com/synchronous-reluctance-motor-a-rare-earth-free-solution-for-electric-vehicles/).

❓ GAP — No supplied evidence supports a 150 kW ferrite-assisted motor-only BOM, magnet mass, continuous power density or production-market share. A numeric substitution scenario would therefore be manufactured.

## 6. Axial flux, YASA, DeepDrive and in-wheel systems

### 6.1 Axial-flux weight and density claims

| Axial-flux parameter | Original Min | Original Mode | Original Max | Revised Min | Revised Mode | Revised Max | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| Weight saving versus radial motor | 10% | 20% | 30% | — | — | — | ❓ GAP |
| Saving at 150 kW | 7 kg | 14 kg | 24 kg | — | — | — | ❓ GAP |
| “Production-oriented” density | 3 kW/kg | 5 kW/kg | 8 kW/kg | — | — | — | ❓ GAP |
| YASA P400-class peak density | Not separated | Not separated | Not separated | 5.7 kW/kg | approximately 6.0 kW/kg | 6.7 kW/kg | 🔧 ADJUSTED |

🔧 ADJUSTED — Academic reviews support a directional axial-flux advantage in torque density and axial package length, but do not validate a universal 10% | 20% | 30% mass saving against an unspecified radial comparator [[63]](https://www.sciencedirect.com/science/article/pii/S2773186324000963) [[64]](https://www.hub-edrive.de/fileadmin/media/Publikation/Comprehensive_Review_and_Systemization_of_the_Product_Features_of_Axial_Flux_Machines.pdf) [[65]](https://www.mdpi.com/2227-7390/12/19/2981) [[66]](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/elp2.12218).

🔧 ADJUSTED — A 7 | 14 | 24 kg saving is derived from applying percentage assumptions to the unconfirmed 55 | 72 | 90 kg radial baseline. It is therefore a second-order scenario calculation, not independent product evidence [1].

### 6.2 YASA continuous-versus-peak caveat

✅ CONFIRMED — The YASA P400 family is an axial-flux, permanent-magnet, yokeless and segmented-armature topology [[38]](https://yasa.com/technology/) [[42]](https://ieeexplore.ieee.org/document/10360216/) [[68]](http://vialidad.usb.ve/materias/ec5136/Motores_axiales/YASA_P400_Product_Sheet.pdf).

🔧 ADJUSTED — Public specifications support approximately 160 kW peak and dry mass around 24–28.2 kg for P400 variants, but continuous output varies substantially by version and cooling configuration. The peak ratio must not be described as continuous power density [[102]](https://yasa.com/yasa-p400-r/) [[67]](https://yasa.com/media/2021/05/yasa-p400rdatasheet-rev-14.pdf) [[68]](http://vialidad.usb.ve/materias/ec5136/Motores_axiales/YASA_P400_Product_Sheet.pdf).

⚠️ CONTRADICTION — The original report presents 3 | 5 | 8 kW/kg as a production-oriented axial-flux range without tying it to duty duration. The P400 evidence demonstrates why this is unsafe: approximately 160 kW peak divided by variant mass produces a high peak density while cited continuous outputs span approximately 20–100 kW [[103]](https://www.scribd.com/document/480141531/YASA-P400-Product-Sheet-pdf) [[67]](https://yasa.com/media/2021/05/yasa-p400rdatasheet-rev-14.pdf) [[68]](http://vialidad.usb.ve/materias/ec5136/Motores_axiales/YASA_P400_Product_Sheet.pdf).

🔧 ADJUSTED — Later YASA prototype records remain company-attributed short-duration claims unless independent test data establish rating duration, coolant conditions, inverter boundary and repeatability [[37]](https://yasa.com/) [[104]](https://electrek.co/2025/10/22/yasa-record-power-density-axial-flux-motor/) [[39]](https://yasa.com/about/) [[40]](https://yasa.com/yasa-mercedes-benz/).

### 6.3 DeepDrive verification

✅ CONFIRMED — TUM sources identify DeepDrive as a Technical University of Munich spin-off [[69]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/german-entrepreneurship-award-for-tum-spin-off-deepdrive) [[70]](https://www.mec.ed.tum.de/fileadmin/w00cbp/am/_my_direct_uploads/2023_ECAM_Slimak.pdf) [[71]](https://www.ie.mgt.tum.de/en/ent/tum-start-up-incubator/) [[72]](https://www.tum.de/en/innovation/) [[73]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/presidential-award-for-space-start-up) [[74]](https://www.mgt.tum.de/unlock-the-brain-tum-startup-develops-neurotechnology-based-playtesting/).

✅ CONFIRMED — Independent technical and company descriptions identify the core topology as a dual-rotor radial-flux machine with a stator located between inner and outer rotors [[75]](https://chargedevs.com/newswire/deepdrive-unveils-new-dual-rotor-radial-flux-drive-unit-for-evs/) [[76]](https://www.deepdrive.tech/news/unleashing-efficiency-revolutionizing-electric-vehicle-technologydeepdrive-deepdive-part-2) [[73]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/presidential-award-for-space-start-up) [[77]](https://www.deepdrive.tech/technology).

🔧 ADJUSTED — Claims of approximately 50% less magnet material, 80% less iron, broad efficiency above 96% or cost reductions above 70% remain company-attributed in the supplied evidence. Media repetition does not constitute independent experimental validation [[105]](https://www.electrive.com/2023/08/21/deepdrive-announces-dual-rotor-radial-flux-central-drive/) [[75]](https://chargedevs.com/newswire/deepdrive-unveils-new-dual-rotor-radial-flux-drive-unit-for-evs/) [[76]](https://www.deepdrive.tech/news/unleashing-efficiency-revolutionizing-electric-vehicle-technologydeepdrive-deepdive-part-2) [[77]](https://www.deepdrive.tech/technology).

🔧 ADJUSTED — DeepDrive offers central-drive and in-wheel development routes, but its 150 kW, 24 kg MG 250 is described as a motor-generator for a range extender. It is not evidence for a 150 kW BEV traction-motor BOM [[106]](https://www.electrive.com/2025/08/07/deepdrive-presents-dual-rotor-radial-flow-generator-for-range-extenders/).

### 6.4 In-wheel systems

✅ CONFIRMED — In-wheel motors can remove conventional central driveline elements and enable direct wheel control, but they create distinct unsprung-mass, sealing, impact, braking, thermal and service boundaries [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[107]](https://www.beyondmotors.io/research/axial-flux-motors-explained-the-essential-engineering-guide-to-topology-design-and-performance-metrics) [[108]](https://www.emobility-engineering.com/challenge-of-power-torque-density/) [[109]](https://www.beyondmotors.io/research/axial-flux-motors-vs-traditional-radial-motors-comparison).

❓ GAP — No supplied source supports an installed passenger-BEV in-wheel architecture share for 2025, 2030, 2040 or later horizons.

🔧 ADJUSTED — DeepDrive and Continental development activity demonstrates technical and OEM interest, not confirmed high-volume adoption [[110]](https://newatlas.com/deepdrive-dual-rotor-e-motor/) [[76]](https://www.deepdrive.tech/news/unleashing-efficiency-revolutionizing-electric-vehicle-technologydeepdrive-deepdive-part-2) [[77]](https://www.deepdrive.tech/technology).

## 7. Circularity, life, scrap and EU policy

### 7.1 Recycled and secondary NdFeB

✅ CONFIRMED — The EU Critical Raw Materials Act is Regulation (EU) 2024/1252 and establishes a 2030 benchmark under which at least 25% of annual EU consumption of strategic raw materials should come from EU recycling capacity [[47]](https://single-market-economy.ec.europa.eu/sectors/raw-materials/areas-specific-interest/critical-raw-materials/critical-raw-materials-act_en) [[48]](https://commission.europa.eu/topics/competitiveness/green-deal-industrial-plan/european-critical-raw-materials-act_en) [[55]](https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng) [[111]](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A52023SC0161).

🔧 ADJUSTED — The 25% CRMA benchmark applies to strategic raw materials collectively; it is not a guarantee that 25% of every traction motor’s NdFeB magnet mass will be recycled content in 2030 [[47]](https://single-market-economy.ec.europa.eu/sectors/raw-materials/areas-specific-interest/critical-raw-materials/critical-raw-materials-act_en) [[48]](https://commission.europa.eu/topics/competitiveness/green-deal-industrial-plan/european-critical-raw-materials-act_en) [[55]](https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng).

✅ CONFIRMED — The CRMA introduces information obligations concerning permanent magnets, including presence, recyclability and recycled-content information for covered products [[56]](https://eur-lex.europa.eu/EN/legal-content/summary/a-secure-and-sustainable-supply-of-critical-raw-materials.html) [[112]](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=COM%3A2023%3A160%3AFIN) [[113]](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A52023PC0160) [[114]](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401252) [[115]](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1252).

✅ CONFIRMED — EU and JRC evidence describes current rare-earth permanent-magnet recycling as below 1%, establishing a low starting point for secondary supply [[12]](https://single-market-economy.ec.europa.eu/sectors/raw-materials/areas-specific-interest/rare-earth-elements-permanent-magnets-and-motors_en) [[116]](https://eitrawmaterials.eu/sites/default/files/2024-11/2021_07-13_REE%20Cluster%20Report.pdf) [[117]](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52025DC0945) [[118]](https://www.eit.europa.eu/sites/default/files/2021_09-24_ree_cluster_report2.pdf).

🔧 ADJUSTED — Recycling can reduce primary-material dependence, but the contribution of end-of-life EV motors remains constrained by vehicle lifetime, collection, dismantling, magnet identification, feedstock quality and processing capacity [[50]](https://link.springer.com/article/10.1007/s11837-023-06235-1) [[51]](https://www.sciencedirect.com/science/article/abs/pii/S1383586623004355) [[53]](https://www.sciencedirect.com/science/article/abs/pii/S1383586625033003) [[119]](https://circulareconomy.europa.eu/platform/sites/default/files/2023-01/Developing%20a%20supply%20chain%20for%20recycled%20rare%20earth%20permanent%20magnets%20in%20the%20EU.pdf) [[120]](https://cordis.europa.eu/project/id/101138767).

### 7.2 Magnet manufacturing scrap

✅ CONFIRMED — NdFeB manufacturing generates clean scrap, machining swarf and sludge that are generally easier to collect than dispersed end-of-life magnets [[121]](https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2022.1094055/xml) [[91]](https://www.sciencedirect.com/science/article/pii/S0921344924005573) [[52]](https://www.sciencedirect.com/science/article/abs/pii/S2452223624000051) [[53]](https://www.sciencedirect.com/science/article/abs/pii/S1383586625033003).

🔧 ADJUSTED — Evidence indicates manufacturing scrap can represent approximately 20–30% of raw-material input in some sintered-magnet processes. This is a process-input or gross-scrap range, not necessarily unrecovered net waste [[121]](https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2022.1094055/xml) [[91]](https://www.sciencedirect.com/science/article/pii/S0921344924005573) [[53]](https://www.sciencedirect.com/science/article/abs/pii/S1383586625033003).

✅ CONFIRMED — Hydrogen processing is suited particularly to clean magnet scrap, while hydrometallurgical routes can process oxidized or contaminated feedstocks and may achieve high rare-earth recovery under specified laboratory or process conditions [[50]](https://link.springer.com/article/10.1007/s11837-023-06235-1) [[51]](https://www.sciencedirect.com/science/article/abs/pii/S1383586623004355) [[52]](https://www.sciencedirect.com/science/article/abs/pii/S2452223624000051) [[53]](https://www.sciencedirect.com/science/article/abs/pii/S1383586625033003) [[122]](https://pubs.acs.org/acsodf/article/8/20/17431/407376/Review-on-the-Parameters-of-Recycling-NdFeB).

❓ GAP — The original report contains no explicit manufacturing-yield or recycled-swarf assumption in its 150 kW material table. Gross motor BOM, purchased magnet input and net virgin-material demand therefore cannot be reconciled.

### 7.3 Motor life and end-of-life flows

✅ CONFIRMED — Traction-motor life depends on thermal cycling, winding-insulation degradation, bearings, lubrication, electrical stresses, rotor integrity and, for PM motors, demagnetization risk [[123]](https://www.iee.fraunhofer.de/de/anwendungsfelder/energiesystemtechnik/leistungselektronik-elektrische-antriebssysteme/elektrische-maschinen.html) [[124]](https://www.ifam.fraunhofer.de/en/technologies/test-bench-for-e-machines.html) [[125]](https://ieeexplore.ieee.org/document/9242951/) [[126]](https://www.researchgate.net/publication/252033360_Life_expectancy_calculation_for_electric_vehicle_traction_motors_regarding_dynamic_temperature_and_driving_cycles) [[127]](https://www.mdpi.com/2071-1050/13/17/9668).

✅ CONFIRMED — Reuse, remanufacturing and recycling are distinct end-of-life routes; functional disassembly and condition diagnosis determine whether material recycling is preferable to retaining component value [[128]](https://www.sciencedirect.com/science/article/pii/S0921344924001769) [[129]](https://www.sciencedirect.com/science/article/pii/S2212827126006104) [[130]](https://www.nist.gov/publications/optimizing-electric-traction-motor-design-analyzing-benefits-circular-economy) [[131]](https://research.birmingham.ac.uk/en/publications/recycling-of-ndfeb-magnets-from-hard-disc-drive-scrap-using-hpms-/) [[132]](https://link.springer.com/article/10.1007/s10163-025-02162-2).

❓ GAP — No supplied evidence provides a representative passenger-BEV traction-motor lifetime distribution by topology, vehicle segment, climate or duty cycle. A single lifetime in years or kilometres would be unsupported.

❓ GAP — No supplied evidence provides EU annual retirement flows of PM, induction and EESM motors with recoverable magnet, copper, steel and aluminium masses. Stock-and-flow modelling therefore requires sensitivity cases rather than a confirmed end-of-life curve.

### 7.4 Environmental interpretation

✅ CONFIRMED — Life-cycle evidence identifies NdFeB production as an important environmental and supply-risk contributor, while copper, electrical steel and aluminium also contribute materially to traction-motor impacts [[65]](https://www.mdpi.com/2227-7390/12/19/2981) [[133]](https://www.mdpi.com/2075-1702/10/12/1178) [[134]](https://www.mdpi.com/1996-1073/15/10/3542) [[49]](https://www.mdpi.com/2075-4701/14/6/658) [[135]](https://doi.org/10.3390/wevj17050249).

🔧 ADJUSTED — Magnet-to-magnet recycling can reduce impacts relative to virgin magnet production, but reported reductions depend on feedstock, process, electricity and allocation boundaries. They should not be applied directly to the entire motor mass [[65]](https://www.mdpi.com/2227-7390/12/19/2981) [[134]](https://www.mdpi.com/1996-1073/15/10/3542) [[50]](https://link.springer.com/article/10.1007/s11837-023-06235-1).

## 8. Vehicle configuration, e-axle boundaries, thermal duty and regulation

### 8.1 Single- versus dual-motor vehicles

✅ CONFIRMED — RAWCLIC reports component masses at vehicle level, which is suitable for material-flow accounting only if the number and type of installed motors are represented correctly [2].

⚠️ CONTRADICTION — The original practical report moves between motor-level 150 kW values, vehicle-level dual-motor applications and higher-power classes without a consistent installed-motor boundary. A 300 kW dual-motor vehicle is not materially equivalent to one 300 kW motor [1].

❓ GAP — Eligible public evidence in the supplied data does not provide an EU registration-weighted distribution of single-, dual- and multi-motor BEVs by segment and year.

🔧 ADJUSTED — Material-demand modelling should use installed motors per vehicle, allocating front and rear machines separately where topology or rating differs. Vehicle nameplate power alone is insufficient.

### 8.2 E-axle and drive-unit boundaries

✅ CONFIRMED — Modern electric drive systems frequently integrate the motor, inverter, reduction gear, differential and cooling functions. Published drive-unit mass must therefore not be assigned to the bare motor without disassembly evidence [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) [[136]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/inverters/projects_inverters.html) [[137]](https://www.izm.fraunhofer.de/en/business_units/power_electronics/electricdrivetechnology.html) [[123]](https://www.iee.fraunhofer.de/de/anwendungsfelder/energiesystemtechnik/leistungselektronik-elektrische-antriebssysteme/elektrische-maschinen.html).

⚠️ CONTRADICTION — The original report correctly warns against using e-axle masses as motor masses, yet its 55 | 72 | 90 kg motor range is said to be anchored partly by product and drive-unit evidence. That evidence cannot confirm the motor-only range unless the non-motor content is removed [1].

❓ GAP — The supplied evidence does not provide separable masses for Volkswagen APP550, Hyundai E-GMP, BYD e-Platform 3.0 or the Tesla Model 3 rear motor under one consistent boundary.

### 8.3 Thermal continuous-versus-peak duty

✅ CONFIRMED — Continuous output is constrained principally by losses, heat transfer and allowable temperatures, whereas peak output can be sustained only for a specified duration and initial thermal condition [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) [[95]](https://www.ifam.fraunhofer.de/en/magazine/electric-drives.html) [[138]](https://www.ict.fraunhofer.de/en/topics/electric-mobility.html) [[123]](https://www.iee.fraunhofer.de/de/anwendungsfelder/energiesystemtechnik/leistungselektronik-elektrische-antriebssysteme/elektrische-maschinen.html).

⚠️ CONTRADICTION — Any density claim using an unspecified “150 kW” numerator is indeterminate. The original radial and axial density tables do not consistently identify whether 150 kW is peak or continuous [1].

🔧 ADJUSTED — Cooling hardware cannot be treated merely as parasitic mass. More capable cooling may increase motor assembly mass while enabling a much higher continuous rating, thereby improving continuous power density at system level [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) [[95]](https://www.ifam.fraunhofer.de/en/magazine/electric-drives.html) [[138]](https://www.ict.fraunhofer.de/en/topics/electric-mobility.html).

❓ GAP — No original mass scenario specifies coolant inlet temperature, flow rate, maximum winding temperature, magnet temperature, duty duration or steady-state criterion. The 2030–2040 mass reductions therefore lack a thermal acceptance basis.

### 8.4 Euro 7 and passenger-car power limits

✅ CONFIRMED — Euro 7 introduces requirements addressing non-exhaust emissions, including brake-particle emissions, alongside broader vehicle-emissions and durability provisions [[139]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32023R1804) [[140]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52025DC0260) [[141]](https://eur-lex.europa.eu/EN/legal-content/summary/deployment-of-alternative-fuels-infrastructure.html) [[142]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A42023X0401) [[143]](https://eur-lex.europa.eu/EN/legal-content/summary/road-safety-driving-licences.html) [[144]](https://eur-lex.europa.eu/EN/legal-content/summary/two-or-three-wheeled-motor-vehicles-maximum-design-speed.html).

⚠️ CONTRADICTION — No supplied EU legislation establishes a general passenger-car traction-motor power limit in kW, and the original evidence does not justify one [[139]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32023R1804) [[140]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52025DC0260) [[141]](https://eur-lex.europa.eu/EN/legal-content/summary/deployment-of-alternative-fuels-infrastructure.html) [[142]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A42023X0401).

⚠️ CONTRADICTION — Brake-particle limits do not establish a causal regulatory rule reducing or capping BEV motor power. Motor kW must not be projected from Euro 7 brake-particle provisions [[139]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32023R1804) [[140]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52025DC0260) [[141]](https://eur-lex.europa.eu/EN/legal-content/summary/deployment-of-alternative-fuels-infrastructure.html) [[143]](https://eur-lex.europa.eu/EN/legal-content/summary/road-safety-driving-licences.html).

🔧 ADJUSTED — Regenerative braking may change friction-brake use, but any effect on brake particles depends on vehicle control, battery acceptance, brake blending, brake design and driving conditions. The supplied evidence does not quantify a motor-power relationship.

## 9. Dedicated contradictions and gaps

### 9.1 Contradictions

**C-1 — Architecture classification**

⚠️ CONTRADICTION — The original report treats radial IPM/PMSM and axial flux as mutually exclusive primary architectures [1], while axial flux describes flux orientation and can also use permanent-magnet synchronous excitation [[63]](https://www.sciencedirect.com/science/article/pii/S2773186324000963) [[64]](https://www.hub-edrive.de/fileadmin/media/Publikation/Comprehensive_Review_and_Systemization_of_the_Product_Features_of_Axial_Flux_Machines.pdf). Resolution: use two dimensions—flux orientation and excitation type—rather than one exclusive list.

**C-2 — PMSM share versus radial-IPM share**

⚠️ CONTRADICTION — IEA and analyst evidence supports high PM-motor penetration [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[3]](https://www.iea.org/reports/rare-earth-elements/executive-summary) [[7]](https://www.idtechex.com/en/research-article/permanent-magnet-and-wrsm-idtechex-explores-ev-motors/32181), but the original report converts that evidence into a radial-IPM share of 78% | 85% | 92% [1]. Resolution: retain PM dominance as directional evidence; withdraw the radial-IPM triplet.

**C-3 — Motor-only mass versus integrated-drive evidence**

⚠️ CONTRADICTION — The original report warns that integrated drive-unit masses cannot be treated as motor masses but uses drive-unit evidence to anchor a 55 | 72 | 90 kg motor-only envelope [1]. Fraunhofer evidence confirms that motor, inverter and gearbox integration is widespread [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) [[136]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/inverters/projects_inverters.html). Resolution: mark the 150 kW motor-only mass as a gap.

**C-4 — Radial power-density benchmark**

⚠️ CONTRADICTION — The original 1.7 | 2.1 | 2.7 kW/kg radial range [1] is materially below some published motor-level production benchmarks and above some integrated-system values [[88]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) [[89]](https://docs.nrel.gov/docs/fy21osti/75994.pdf) [[90]](https://www.borgwarner.com/technologies/electric-drive-motors). Resolution: no revised triplet until rating duration and denominator are matched.

**C-5 — YASA peak and continuous density**

⚠️ CONTRADICTION — The original report presents a generic 3 | 5 | 8 kW/kg axial-flux range [1], while YASA P400 evidence distinguishes approximately 160 kW peak from much lower and configuration-dependent continuous power [[103]](https://www.scribd.com/document/480141531/YASA-P400-Product-Sheet-pdf) [[67]](https://yasa.com/media/2021/05/yasa-p400rdatasheet-rev-14.pdf) [[68]](http://vialidad.usb.ve/materias/ec5136/Motores_axiales/YASA_P400_Product_Sheet.pdf). Resolution: report peak and continuous densities separately.

**C-6 — EESM efficiency penalty**

⚠️ CONTRADICTION — The original −1.5 | −0.5 | +0.5 percentage-point highway difference [1] implies a transferable comparison, while peer-reviewed comparisons vary by operating point and optimization [[29]](https://www.mdpi.com/2032-6653/13/4/65) [[30]](https://www.mdpi.com/1996-1073/19/18/4316) [[96]](https://www.mdpi.com/2032-6653/16/11/633) [[97]](https://www.mdpi.com/2075-1702/12/6/361). Resolution: retain qualitative duty-cycle dependence and withdraw the universal triplet.

**C-7 — Future shares represented numerically**

⚠️ CONTRADICTION — The original report calls the 2030–2050 values scenarios but presents complete topology tables with forecast-like precision [1]. Analyst evidence supports diversification without confirming those allocations [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[7]](https://www.idtechex.com/en/research-article/permanent-magnet-and-wrsm-idtechex-explores-ev-motors/32181) [[59]](https://www.idtechex.com/en/research-article/the-evolution-of-modern-electric-motor-market-for-electric-vehicles/29506). Resolution: separate evidence-supported direction from explicit scenario construction.

**C-8 — Scaling warning versus scaling table**

⚠️ CONTRADICTION — The report states that power does not scale linearly with mass, yet supplies smooth 75–400 kW mass and magnet ladders without a disclosed physical model [1]. Resolution: remove the ladder from confirmed-value use.

**C-9 — DeepDrive topology**

⚠️ CONTRADICTION — Secondary descriptions can associate DeepDrive with wheel-integrated concepts, but TUM, technical and company evidence identifies a dual-rotor radial-flux machine rather than an axial-flux machine [[75]](https://chargedevs.com/newswire/deepdrive-unveils-new-dual-rotor-radial-flux-drive-unit-for-evs/) [[76]](https://www.deepdrive.tech/news/unleashing-efficiency-revolutionizing-electric-vehicle-technologydeepdrive-deepdive-part-2) [[73]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/presidential-award-for-space-start-up) [[77]](https://www.deepdrive.tech/technology). Resolution: classify it as dual-rotor radial flux.

**C-10 — Euro 7 and motor power**

⚠️ CONTRADICTION — Euro 7 brake-particle provisions are regulatory emissions requirements [[139]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32023R1804) [[140]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52025DC0260) [[141]](https://eur-lex.europa.eu/EN/legal-content/summary/deployment-of-alternative-fuels-infrastructure.html), not an EU passenger-car traction-power cap. Resolution: exclude any motor-kW limit or causal forecast derived from brake-particle rules.

### 9.2 Gaps

**G-1 — Recycled and secondary NdFeB**

❓ GAP — No evidence quantifies recycled NdFeB content in a representative 150 kW motor by 2025, 2030 or 2040. Fill method: obtain supplier declarations using CRMA-compatible recycled-content methodology and distinguish pre-consumer magnet scrap from post-consumer end-of-life material [[55]](https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng) [[56]](https://eur-lex.europa.eu/EN/legal-content/summary/a-secure-and-sustainable-supply-of-critical-raw-materials.html) [[114]](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401252).

**G-2 — Motor life and end-of-life**

❓ GAP — No topology-specific survival curve is available. Fill method: combine warranty returns, dismantler observations, odometer-at-retirement data and thermal-duty models, then validate separate reuse, remanufacture and recycling probabilities [[125]](https://ieeexplore.ieee.org/document/9242951/) [[126]](https://www.researchgate.net/publication/252033360_Life_expectancy_calculation_for_electric_vehicle_traction_motors_regarding_dynamic_temperature_and_driving_cycles) [[130]](https://www.nist.gov/publications/optimizing-electric-traction-motor-design-analyzing-benefits-circular-economy).

**G-3 — Ferrite alternatives**

❓ GAP — No 150 kW ferrite-assisted production BOM or continuous density is disclosed. Fill method: require a matched IPM/ferrite demonstrator comparison using the same stator outer diameter, cooling, voltage, peak duration and continuous thermal limit [[98]](https://ieeexplore.ieee.org/document/7542569/) [[99]](https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/iet-epa.2018.5891).

**G-4 — Manufacturing scrap**

❓ GAP — The gross 20–30% magnet-process scrap range does not reveal internal recycling, external recycling or net virgin-material loss. Fill method: collect mass-balance data from alloy input through sintering, machining, rejected magnets and recovered swarf [[121]](https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2022.1094055/xml) [[91]](https://www.sciencedirect.com/science/article/pii/S0921344924005573) [[53]](https://www.sciencedirect.com/science/article/abs/pii/S1383586625033003).

**G-5 — Dual- versus single-motor vehicles**

❓ GAP — Registration data do not identify installed motor count and topology consistently. Fill method: map vehicle variants and axle configurations to registrations, retaining separate front and rear motor records [2].

**G-6 — In-wheel adoption**

❓ GAP — Demonstrators and supplier programmes do not establish market penetration. Fill method: count homologated series-production vehicles and installed wheel motors rather than announcements, prototypes or funding rounds [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[77]](https://www.deepdrive.tech/technology).

**G-7 — E-axle boundary**

❓ GAP — Public product specifications rarely disaggregate motor, inverter, gearbox, differential, oil and housing masses. Fill method: use controlled teardowns with a boundary protocol and photographically traceable weighing of each cleaned subassembly [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) [[136]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/inverters/projects_inverters.html).

**G-8 — Thermal peak and continuous duty**

❓ GAP — Original density values lack duration and coolant conditions. Fill method: report at least peak power and duration, continuous steady-state power, coolant inlet temperature, flow rate, winding limit, magnet limit and included cooling mass [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) [[95]](https://www.ifam.fraunhofer.de/en/magazine/electric-drives.html) [[138]](https://www.ict.fraunhofer.de/en/topics/electric-mobility.html).

## 10. Master confirmed-value table

| Motor type | Parameter | Original value | Confirmed Min | Confirmed Mode | Confirmed Max | Status | Key confirming/contradicting source |
|---|---|---:|---:|---:|---:|---|---|
| Radial IPM/PMSM | Current architecture share | 78% \| 85% \| 92% | — | — | — | ❓ GAP | PM evidence does not isolate radial IPM [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[3]](https://www.iea.org/reports/rare-earth-elements/executive-summary) [[7]](https://www.idtechex.com/en/research-article/permanent-magnet-and-wrsm-idtechex-explores-ev-motors/32181) |
| PM motors, all relevant excitation/orientation classes | Current market direction | Approximately 85% to >90% | >75% | approximately 85% | >90% under broader scope | 🔧 ADJUSTED | Scope-dependent PM estimates [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[62]](https://www.iea.org/reports/global-ev-outlook-2026/trends-in-electric-cars) [[3]](https://www.iea.org/reports/rare-earth-elements/executive-summary) |
| EESM/WRSM | Current architecture share | 4% \| 7% \| 10% | — | — | — | ❓ GAP | Production use confirmed, share not confirmed [[15]](https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en) [[18]](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) [[4]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140892/JRC140892_01.pdf) |
| Induction | Current architecture share | 3% \| 6% \| 10% | — | — | — | ❓ GAP | Architecture confirmed, installed share unresolved [[4]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140892/JRC140892_01.pdf) [[5]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142055/JRC142055_01.pdf) [[95]](https://www.ifam.fraunhofer.de/en/magazine/electric-drives.html) |
| Axial flux | Current architecture share | 0% \| 1% \| 2% | — | — | — | ❓ GAP | Commercial activity does not establish share [[22]](https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html) [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[59]](https://www.idtechex.com/en/research-article/the-evolution-of-modern-electric-motor-market-for-electric-vehicles/29506) |
| Radial IPM/PMSM, 150 kW class | Total motor mass | 55 \| 72 \| 90 kg | — | — | — | ❓ GAP | No matched motor-only public BOM [1] [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) [[136]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/inverters/projects_inverters.html) |
| Radial IPM/PMSM, 150 kW class | Power density | 1.7 \| 2.1 \| 2.7 kW/kg | — | — | — | ❓ GAP | Peak/continuous and denominator unresolved [[88]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) [[89]](https://docs.nrel.gov/docs/fy21osti/75994.pdf) [[90]](https://www.borgwarner.com/technologies/electric-drive-motors) |
| Radial IPM/PMSM, 150 kW class | Stator laminations | 18 \| 23 \| 28 kg | — | — | — | ❓ GAP | Material presence confirmed, mass not confirmed [[25]](https://info.ornl.gov/sites/publications/Files/Pub57320.pdf) [[28]](https://www.sciencedirect.com/science/article/pii/S0306261923018603) [[86]](https://www.sciencedirect.com/topics/engineering/permanent-magnet-synchronous-motor) |
| Radial IPM/PMSM, 150 kW class | Stator copper | 8 \| 11 \| 14 kg | — | — | — | ❓ GAP | No independently weighed 150 kW value [[25]](https://info.ornl.gov/sites/publications/Files/Pub57320.pdf) [[85]](https://link.springer.com/article/10.1007/s43939-026-00679-3) [[87]](https://doi.org/10.3390/vehicles8030066) |
| Radial IPM/PMSM, 150 kW class | Rotor laminations | 10 \| 14 \| 18 kg | — | — | — | ❓ GAP | No comparable public component weighing [[25]](https://info.ornl.gov/sites/publications/Files/Pub57320.pdf) [[28]](https://www.sciencedirect.com/science/article/pii/S0306261923018603) [[86]](https://www.sciencedirect.com/topics/engineering/permanent-magnet-synchronous-motor) |
| Radial IPM/PMSM, 150 kW class | NdFeB magnets | 1.0 \| 1.5 \| 2.0 kg | 0.5 kg broad traction range | — | 3.0 kg broad traction range | 🔧 ADJUSTED | Not normalized to 150 kW [[9]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC122671/jrc122671_the_role_of_rare_earth_elements_in_wind_energy_and_electric_mobility_2.pdf) [[91]](https://www.sciencedirect.com/science/article/pii/S0921344924005573) [[92]](https://www.benchmarkminerals.com/glossary/what-are-rare-earths) |
| Radial IPM/PMSM, 150 kW class | Shaft | 3.0 \| 4.5 \| 6.0 kg | — | — | — | ❓ GAP | No public component evidence |
| Radial IPM/PMSM, 150 kW class | Housing and end shields | 8 \| 12 \| 17 kg | — | — | — | ❓ GAP | Housing boundary varies with e-axle integration [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) [[136]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/inverters/projects_inverters.html) |
| Radial IPM/PMSM, 150 kW class | Bearings and seals | 1.0 \| 1.7 \| 2.5 kg | — | — | — | ❓ GAP | No independently weighed range |
| Radial IPM/PMSM, 150 kW class | Cooling hardware and fluid | 2 \| 4 \| 7 kg | — | — | — | ❓ GAP | Cooling-system boundary unspecified [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) [[95]](https://www.ifam.fraunhofer.de/en/magazine/electric-drives.html) [[138]](https://www.ict.fraunhofer.de/en/topics/electric-mobility.html) |
| Radial IPM/PMSM, 150 kW class | Sensors and resolver | 0.3 \| 0.7 \| 1.2 kg | — | — | — | ❓ GAP | No comparable public component evidence |
| NdFeB magnet | Nd content | Motor-level 0.25 \| 0.38 \| 0.55 kg | 29% of magnet mass | approximately 30% | 32% | 🔧 ADJUSTED | Chemistry confirmed; motor mass unresolved [[34]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10890235/) [[61]](https://pubs.aip.org/aip/adv/article/15/7/075206/3351613/Microstructure-and-super-high-coercivity-of-Tb) [[49]](https://www.mdpi.com/2075-4701/14/6/658) |
| NdFeB magnet | Dy content | 0.5% \| 3% \| 8% | — | — | — | ❓ GAP | Grade- and process-dependent [[34]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10890235/) [[36]](https://link.springer.com/article/10.1007/s11837-022-05594-5) [[61]](https://pubs.aip.org/aip/adv/article/15/7/075206/3351613/Microstructure-and-super-high-coercivity-of-Tb) |
| NdFeB magnet | Tb content | 0% \| 0.5% \| 2% | — | — | — | ❓ GAP | Grade- and process-dependent [[34]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10890235/) [[36]](https://link.springer.com/article/10.1007/s11837-022-05594-5) [[61]](https://pubs.aip.org/aip/adv/article/15/7/075206/3351613/Microstructure-and-super-high-coercivity-of-Tb) |
| NdFeB magnet | GBD heavy-rare-earth reduction | 50% \| 60% \| 70% by 2030 | approximately 50% | — | approximately 70% process range | 🔧 ADJUSTED | Process potential, not industry-wide outcome [[34]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10890235/) [[93]](https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119792918.ch14) [[94]](https://www.sciencedirect.com/science/article/abs/pii/S0956053X18306809) |
| EESM | Motor-mass difference versus IPM | +4 \| +8 \| +15 kg | — | — | — | ❓ GAP | No matched production comparison [[29]](https://www.mdpi.com/2032-6653/13/4/65) [[30]](https://www.mdpi.com/1996-1073/19/18/4316) [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) |
| EESM | Additional rotor copper | 3 \| 6 \| 10 kg | — | — | — | ❓ GAP | Rotor copper direction confirmed, mass not confirmed [[31]](https://www.mdpi.com/1996-1073/18/9/2274) [[5]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142055/JRC142055_01.pdf) [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) |
| EESM | Highway efficiency difference | −1.5 \| −0.5 \| +0.5 pp | — | — | — | ❓ GAP | Operating-point comparisons disagree [[29]](https://www.mdpi.com/2032-6653/13/4/65) [[30]](https://www.mdpi.com/1996-1073/19/18/4316) [[96]](https://www.mdpi.com/2032-6653/16/11/633) |
| EESM | Magnet elimination | 1.0 \| 1.5 \| 2.0 kg reduction | Full elimination of selected IPM magnet mass | Same | Same | 🔧 ADJUSTED | Absolute reduction depends on comparator [[4]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140892/JRC140892_01.pdf) [[5]](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142055/JRC142055_01.pdf) [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) |
| Ferrite PMa-SynRM | 150 kW BOM and density | Not provided | — | — | — | ❓ GAP | Traction research exists without matched 150 kW production BOM [[87]](https://doi.org/10.3390/vehicles8030066) [[98]](https://ieeexplore.ieee.org/document/7542569/) [[99]](https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/iet-epa.2018.5891) |
| Pure SynRM | Demonstrated traction power class | Not provided | 75 kW peak scaled design | — | 200 kW peak design | 🔧 ADJUSTED | Demonstrator evidence, not adoption evidence [[100]](https://www.refreedrive.eu/wp-content/downloads/2018_Coiltech_ReFreeDrive_UnivLAquila_SynchronousReluctanceMotorForTractionApplications.pdf) [[101]](https://www.electricmotorengineering.com/synchronous-reluctance-motor-a-rare-earth-free-solution-for-electric-vehicles/) |
| Axial-flux PM | Weight saving versus radial | 10% \| 20% \| 30% | — | — | — | ❓ GAP | Comparator and duty not matched [[63]](https://www.sciencedirect.com/science/article/pii/S2773186324000963) [[64]](https://www.hub-edrive.de/fileadmin/media/Publikation/Comprehensive_Review_and_Systemization_of_the_Product_Features_of_Axial_Flux_Machines.pdf) [[65]](https://www.mdpi.com/2227-7390/12/19/2981) |
| Axial-flux PM | Weight saving at 150 kW | 7 \| 14 \| 24 kg | — | — | — | ❓ GAP | Derived from two unconfirmed ranges [1] |
| Axial-flux PM | Generic production density | 3 \| 5 \| 8 kW/kg | — | — | — | ❓ GAP | Peak/continuous ambiguity [[63]](https://www.sciencedirect.com/science/article/pii/S2773186324000963) [[66]](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/elp2.12218) [[43]](https://www.sciencedirect.com/science/article/pii/S1000936125006685) |
| YASA P400-class axial flux | Peak power | Approximately 160 kW | 160 kW | 160 kW | 160 kW | ✅ CONFIRMED | Supplier specification and technical characterization [[42]](https://ieeexplore.ieee.org/document/10360216/) [[67]](https://yasa.com/media/2021/05/yasa-p400rdatasheet-rev-14.pdf) [[68]](http://vialidad.usb.ve/materias/ec5136/Motores_axiales/YASA_P400_Product_Sheet.pdf) |
| YASA P400-class axial flux | Dry motor mass | Approximately 24 kg | 24 kg | — | 28.2 kg | 🔧 ADJUSTED | Variant-dependent [[103]](https://www.scribd.com/document/480141531/YASA-P400-Product-Sheet-pdf) [[67]](https://yasa.com/media/2021/05/yasa-p400rdatasheet-rev-14.pdf) [[68]](http://vialidad.usb.ve/materias/ec5136/Motores_axiales/YASA_P400_Product_Sheet.pdf) |
| YASA P400-class axial flux | Peak power density | Not separated | 5.7 kW/kg | approximately 6.0 kW/kg | 6.7 kW/kg | 🔧 ADJUSTED | Computed from disclosed peak power and variant mass [[42]](https://ieeexplore.ieee.org/document/10360216/) [[67]](https://yasa.com/media/2021/05/yasa-p400rdatasheet-rev-14.pdf) [[68]](http://vialidad.usb.ve/materias/ec5136/Motores_axiales/YASA_P400_Product_Sheet.pdf) |
| YASA P400-class axial flux | Continuous power | Not separated | approximately 20 kW | — | approximately 100 kW | 🔧 ADJUSTED | Cooling- and variant-dependent [[103]](https://www.scribd.com/document/480141531/YASA-P400-Product-Sheet-pdf) [[67]](https://yasa.com/media/2021/05/yasa-p400rdatasheet-rev-14.pdf) [[68]](http://vialidad.usb.ve/materias/ec5136/Motores_axiales/YASA_P400_Product_Sheet.pdf) |
| DeepDrive dual-rotor radial flux | TUM spin-off identity | Not explicitly verified | Yes | Yes | Yes | ✅ CONFIRMED | TUM institutional sources [[69]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/german-entrepreneurship-award-for-tum-spin-off-deepdrive) [[70]](https://www.mec.ed.tum.de/fileadmin/w00cbp/am/_my_direct_uploads/2023_ECAM_Slimak.pdf) [[71]](https://www.ie.mgt.tum.de/en/ent/tum-start-up-incubator/) [[73]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/presidential-award-for-space-start-up) |
| DeepDrive dual-rotor radial flux | Topology | Ambiguous in secondary discussion | Dual rotor | Stator between rotors | Radial flux | ✅ CONFIRMED | Technical and company descriptions [[75]](https://chargedevs.com/newswire/deepdrive-unveils-new-dual-rotor-radial-flux-drive-unit-for-evs/) [[76]](https://www.deepdrive.tech/news/unleashing-efficiency-revolutionizing-electric-vehicle-technologydeepdrive-deepdive-part-2) [[73]](https://www.tum.de/en/news-and-events/all-news/press-releases/details/presidential-award-for-space-start-up) |
| DeepDrive dual-rotor radial flux | Magnet saving | Approximately 50% claim | — | — | — | 🔧 ADJUSTED | Company-attributed, not independently tested [[75]](https://chargedevs.com/newswire/deepdrive-unveils-new-dual-rotor-radial-flux-drive-unit-for-evs/) [[76]](https://www.deepdrive.tech/news/unleashing-efficiency-revolutionizing-electric-vehicle-technologydeepdrive-deepdive-part-2) [[77]](https://www.deepdrive.tech/technology) |
| DeepDrive dual-rotor radial flux | Iron saving | Approximately 80% claim | — | — | — | 🔧 ADJUSTED | Company-attributed, not independently tested [[75]](https://chargedevs.com/newswire/deepdrive-unveils-new-dual-rotor-radial-flux-drive-unit-for-evs/) [[76]](https://www.deepdrive.tech/news/unleashing-efficiency-revolutionizing-electric-vehicle-technologydeepdrive-deepdive-part-2) [[77]](https://www.deepdrive.tech/technology) |
| DeepDrive MG 250 | 150 kW and 24 kg | Potentially comparable 150 kW evidence | — | — | — | 🔧 ADJUSTED | Range-extender motor-generator, not BEV traction BOM [[88]](https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/) |
| All architectures | 2030 topology shares | Complete original triplets | — | — | — | ❓ GAP | Direction supported, exact allocation unconfirmed [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[7]](https://www.idtechex.com/en/research-article/permanent-magnet-and-wrsm-idtechex-explores-ev-motors/32181) [[59]](https://www.idtechex.com/en/research-article/the-evolution-of-modern-electric-motor-market-for-electric-vehicles/29506) |
| All architectures | 2035 topology shares | Complete original triplets | — | — | — | ❓ GAP | Magnet-free growth direction does not allocate topology [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[7]](https://www.idtechex.com/en/research-article/permanent-magnet-and-wrsm-idtechex-explores-ev-motors/32181) |
| All architectures | 2040 topology shares | Complete original triplets | — | — | — | ❓ GAP | Scenario construction only [1] [[59]](https://www.idtechex.com/en/research-article/the-evolution-of-modern-electric-motor-market-for-electric-vehicles/29506) |
| All architectures | 2050 topology shares | Complete original triplets | — | — | — | ❓ GAP | No comparable long-horizon dataset [1] [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[3]](https://www.iea.org/reports/rare-earth-elements/executive-summary) |
| Passenger-BEV motors | EU power limit | Implicit policy concern | — | — | — | ⚠️ CONTRADICTION | No general motor-kW cap identified in Euro 7 [[139]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32023R1804) [[140]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52025DC0260) [[141]](https://eur-lex.europa.eu/EN/legal-content/summary/deployment-of-alternative-fuels-infrastructure.html) |
| Passenger-BEV motors | Brake-particle rule causes lower motor kW | Potential causal inference | — | — | — | ⚠️ CONTRADICTION | Euro 7 brake requirements do not establish such causation [[139]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32023R1804) [[141]](https://eur-lex.europa.eu/EN/legal-content/summary/deployment-of-alternative-fuels-infrastructure.html) [[143]](https://eur-lex.europa.eu/EN/legal-content/summary/road-safety-driving-licences.html) |
| Strategic raw materials | EU recycling benchmark for 2030 | Not integrated into motor scenarios | 25% | 25% | 25% | ✅ CONFIRMED | EU-wide strategic-material recycling-capacity benchmark [[47]](https://single-market-economy.ec.europa.eu/sectors/raw-materials/areas-specific-interest/critical-raw-materials/critical-raw-materials-act_en) [[48]](https://commission.europa.eu/topics/competitiveness/green-deal-industrial-plan/european-critical-raw-materials-act_en) [[55]](https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng) |
| NdFeB magnets | 2030 motor-level recycled content | Not provided | — | — | — | ❓ GAP | CRMA benchmark is not a per-motor content mandate [[55]](https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng) [[56]](https://eur-lex.europa.eu/EN/legal-content/summary/a-secure-and-sustainable-supply-of-critical-raw-materials.html) [[114]](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401252) |
| NdFeB manufacture | Gross scrap or swarf generation | Not provided | 20% | — | 30% | 🔧 ADJUSTED | Process-input range, not net unrecovered loss [[121]](https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2022.1094055/xml) [[91]](https://www.sciencedirect.com/science/article/pii/S0921344924005573) [[53]](https://www.sciencedirect.com/science/article/abs/pii/S1383586625033003) |
| Traction motors | Service-life distribution | Not provided | — | — | — | ❓ GAP | Thermal and failure evidence lacks representative survival curve [[123]](https://www.iee.fraunhofer.de/de/anwendungsfelder/energiesystemtechnik/leistungselektronik-elektrische-antriebssysteme/elektrische-maschinen.html) [[125]](https://ieeexplore.ieee.org/document/9242951/) [[126]](https://www.researchgate.net/publication/252033360_Life_expectancy_calculation_for_electric_vehicle_traction_motors_regarding_dynamic_temperature_and_driving_cycles) |
| Traction motors | End-of-life route shares | Not provided | — | — | — | ❓ GAP | Reuse, remanufacture and recycling shares not quantified [[128]](https://www.sciencedirect.com/science/article/pii/S0921344924001769) [[129]](https://www.sciencedirect.com/science/article/pii/S2212827126006104) [[130]](https://www.nist.gov/publications/optimizing-electric-traction-motor-design-analyzing-benefits-circular-economy) |
| Vehicle-level propulsion | Single- versus dual-motor distribution | Not consistently controlled | — | — | — | ❓ GAP | Registration-weighted installed-motor data unavailable [2] |
| In-wheel motors | Passenger-BEV adoption share | Not provided | — | — | — | ❓ GAP | Demonstrators do not establish market share [[57]](https://www.idtechex.com/en/research-report/electric-motors/1031) [[77]](https://www.deepdrive.tech/technology) |
| Integrated e-axles | Motor-only mass disaggregation | Treated cautiously but used as anchor | — | — | — | ❓ GAP | Motor, inverter and gearbox masses not separable [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) [[136]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/inverters/projects_inverters.html) [[123]](https://www.iee.fraunhofer.de/de/anwendungsfelder/energiesystemtechnik/leistungselektronik-elektrische-antriebssysteme/elektrische-maschinen.html) |
| All motor types | Continuous/peak density conversion | Often unspecified | — | — | — | ❓ GAP | Requires duration, coolant and temperature limits [[6]](https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html) [[95]](https://www.ifam.fraunhofer.de/en/magazine/electric-drives.html) [[138]](https://www.ict.fraunhofer.de/en/topics/electric-mobility.html) |

---

## References

1. BEV_Motors_Practical_Report_v2.md (uploaded document)
2. RAWCLIC_BEV_motor_consolidated_data_description-V1.pdf (uploaded document)
3. <https://www.iea.org/reports/rare-earth-elements/executive-summary>
4. <https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140892/JRC140892_01.pdf>
5. <https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142055/JRC142055_01.pdf>
6. <https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/e_machines.html>
7. <https://www.idtechex.com/en/research-article/permanent-magnet-and-wrsm-idtechex-explores-ev-motors/32181>
8. <https://www.iea.org/reports/the-role-of-critical-minerals-in-clean-energy-transitions/executive-summary>
9. <https://publications.jrc.ec.europa.eu/repository/bitstream/JRC122671/jrc122671_the_role_of_rare_earth_elements_in_wind_energy_and_electric_mobility_2.pdf>
10. <https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/innovative-requirements-could-boost-circular-economy-plastics-and-critical-raw-materials-vehicles-2023-07-13_en>
11. <https://publications.jrc.ec.europa.eu/repository/bitstream/JRC141759/JRC141759_01.pdf>
12. <https://single-market-economy.ec.europa.eu/sectors/raw-materials/areas-specific-interest/rare-earth-elements-permanent-magnets-and-motors_en>
13. <https://www.iea.org/topics/critical-minerals>
14. <https://publications.jrc.ec.europa.eu/repository/bitstream/JRC120312/policyreport_assessment_of_magnetic_fields_in_electrified_vehicles_final2.pdf>
15. <https://www.press.bmwgroup.com/canada/article/detail/T0440602EN/bmw%E2%80%99s-5th-generation-electric-drive-system-wins-2024-ajac-best-green-innovation-award?language=en>
16. <https://www.press.bmwgroup.com/usa/article/detail/T0443395EN_US/the-all-new-2025-bmw-m5>
17. <https://www.press.bmwgroup.com/usa/article/attachment/T0443395EN_US/618783>
18. <https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/>
19. <https://media.renault.com/all-new-megane-e-tech-electric-delving-into-the-heart-of-innovation-episode-3/>
20. <https://www.renaultgroup.com/en/magazine/energy-and-powertrains/e7a-the-next-gen-electric-motor-developed-by-renault-and-valeo/>
21. <https://www.valeo.com/en/renault-group-valeo-and-valeo-siemens-eautomotive-join-forces-to-develop-and-manufacture-a-new-generation-automotive-electric-motor-in-france/>
22. <https://group.mercedes-benz.com/company/production/news/axial-flux-motor-berlin.html>
23. <https://media.mercedes-benz.com/en/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf>
24. <https://group.mercedes-benz.com/company/strategy/mercedes-benz-strategy-update-electric-drive.html>
25. <https://info.ornl.gov/sites/publications/Files/Pub57320.pdf>
26. <https://www.osti.gov/servlets/purl/1825650>
27. <https://www.sciencedirect.com/science/article/pii/S1364032126007021>
28. <https://www.sciencedirect.com/science/article/pii/S0306261923018603>
29. <https://www.mdpi.com/2032-6653/13/4/65>
30. <https://www.mdpi.com/1996-1073/19/18/4316>
31. <https://www.mdpi.com/1996-1073/18/9/2274>
32. <https://pubs.aip.org/aip/adv/article/10/2/025105/1021639/Performance-verification-of-DR-PMSM-for-traction>
33. <https://www.sciencedirect.com/science/article/pii/S2773153722000123>
34. <https://pmc.ncbi.nlm.nih.gov/articles/PMC10890235/>
35. <https://www.sciencedirect.com/science/article/pii/S2590123026013034>
36. <https://link.springer.com/article/10.1007/s11837-022-05594-5>
37. <https://yasa.com/>
38. <https://yasa.com/technology/>
39. <https://yasa.com/about/>
40. <https://yasa.com/yasa-mercedes-benz/>
41. <https://yasa.com/automotive/>
42. <https://ieeexplore.ieee.org/document/10360216/>
43. <https://www.sciencedirect.com/science/article/pii/S1000936125006685>
44. <https://www.sciencedirect.com/science/article/pii/S2352484722014767>
45. <https://www.mdpi.com/2075-1702/13/10/954>
46. <https://cjme.springeropen.com/articles/10.1186/s10033-023-00868-8>
47. <https://single-market-economy.ec.europa.eu/sectors/raw-materials/areas-specific-interest/critical-raw-materials/critical-raw-materials-act_en>
48. <https://commission.europa.eu/topics/competitiveness/green-deal-industrial-plan/european-critical-raw-materials-act_en>
49. <https://www.mdpi.com/2075-4701/14/6/658>
50. <https://link.springer.com/article/10.1007/s11837-023-06235-1>
51. <https://www.sciencedirect.com/science/article/abs/pii/S1383586623004355>
52. <https://www.sciencedirect.com/science/article/abs/pii/S2452223624000051>
53. <https://www.sciencedirect.com/science/article/abs/pii/S1383586625033003>
54. <https://www.sciencedirect.com/science/article/pii/S0304885323011253>
55. <https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng>
56. <https://eur-lex.europa.eu/EN/legal-content/summary/a-secure-and-sustainable-supply-of-critical-raw-materials.html>
57. <https://www.idtechex.com/en/research-report/electric-motors/1031>
58. <https://www.idtechex.com/en/research-article/the-ev-market-doubles-down-on-permanent-magnets-despite-material-costs/28314>
59. <https://www.idtechex.com/en/research-article/the-evolution-of-modern-electric-motor-market-for-electric-vehicles/29506>
60. <https://www.idtechex.com/en/research-article/axial-flux-traction-motor-with-15-advantage/9643>
61. <https://pubs.aip.org/aip/adv/article/15/7/075206/3351613/Microstructure-and-super-high-coercivity-of-Tb>
62. <https://www.iea.org/reports/global-ev-outlook-2026/trends-in-electric-cars>
63. <https://www.sciencedirect.com/science/article/pii/S2773186324000963>
64. <https://www.hub-edrive.de/fileadmin/media/Publikation/Comprehensive_Review_and_Systemization_of_the_Product_Features_of_Axial_Flux_Machines.pdf>
65. <https://www.mdpi.com/2227-7390/12/19/2981>
66. <https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/elp2.12218>
67. <https://yasa.com/media/2021/05/yasa-p400rdatasheet-rev-14.pdf>
68. <http://vialidad.usb.ve/materias/ec5136/Motores_axiales/YASA_P400_Product_Sheet.pdf>
69. <https://www.tum.de/en/news-and-events/all-news/press-releases/details/german-entrepreneurship-award-for-tum-spin-off-deepdrive>
70. <https://www.mec.ed.tum.de/fileadmin/w00cbp/am/_my_direct_uploads/2023_ECAM_Slimak.pdf>
71. <https://www.ie.mgt.tum.de/en/ent/tum-start-up-incubator/>
72. <https://www.tum.de/en/innovation/>
73. <https://www.tum.de/en/news-and-events/all-news/press-releases/details/presidential-award-for-space-start-up>
74. <https://www.mgt.tum.de/unlock-the-brain-tum-startup-develops-neurotechnology-based-playtesting/>
75. <https://chargedevs.com/newswire/deepdrive-unveils-new-dual-rotor-radial-flux-drive-unit-for-evs/>
76. <https://www.deepdrive.tech/news/unleashing-efficiency-revolutionizing-electric-vehicle-technologydeepdrive-deepdive-part-2>
77. <https://www.deepdrive.tech/technology>
78. <https://www.idtechex.com/en/research-report/electric-motors-for-electric-vehicles/1131>
79. <https://www.idtechex.com/en/research-article/new-idtechex-report-electric-motors-for-electric-vehicles-2026-2036/33926>
80. <https://www.sciencedirect.com/science/article/pii/S2352484722025628>
81. <https://global-sei.com/technology/tr/bn75/pdf/75-11.pdf>
82. <https://ieeexplore.ieee.org/document/182730>
83. <https://technology.nasa.gov/patent/LEW-TOPS-140>
84. <https://global-sei.com/technology/tr/bn67/pdf/67-05.pdf>
85. <https://link.springer.com/article/10.1007/s43939-026-00679-3>
86. <https://www.sciencedirect.com/topics/engineering/permanent-magnet-synchronous-motor>
87. <https://doi.org/10.3390/vehicles8030066>
88. <https://auto-tech-news.com/2026/05/26/what-is-a-high-power-density-electric-motor-engineers-guide/>
89. <https://docs.nrel.gov/docs/fy21osti/75994.pdf>
90. <https://www.borgwarner.com/technologies/electric-drive-motors>
91. <https://www.sciencedirect.com/science/article/pii/S0921344924005573>
92. <https://www.benchmarkminerals.com/glossary/what-are-rare-earths>
93. <https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119792918.ch14>
94. <https://www.sciencedirect.com/science/article/abs/pii/S0956053X18306809>
95. <https://www.ifam.fraunhofer.de/en/magazine/electric-drives.html>
96. <https://www.mdpi.com/2032-6653/16/11/633>
97. <https://www.mdpi.com/2075-1702/12/6/361>
98. <https://ieeexplore.ieee.org/document/7542569/>
99. <https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/iet-epa.2018.5891>
100. <https://www.refreedrive.eu/wp-content/downloads/2018_Coiltech_ReFreeDrive_UnivLAquila_SynchronousReluctanceMotorForTractionApplications.pdf>
101. <https://www.electricmotorengineering.com/synchronous-reluctance-motor-a-rare-earth-free-solution-for-electric-vehicles/>
102. <https://yasa.com/yasa-p400-r/>
103. <https://www.scribd.com/document/480141531/YASA-P400-Product-Sheet-pdf>
104. <https://electrek.co/2025/10/22/yasa-record-power-density-axial-flux-motor/>
105. <https://www.electrive.com/2023/08/21/deepdrive-announces-dual-rotor-radial-flux-central-drive/>
106. <https://www.electrive.com/2025/08/07/deepdrive-presents-dual-rotor-radial-flow-generator-for-range-extenders/>
107. <https://www.beyondmotors.io/research/axial-flux-motors-explained-the-essential-engineering-guide-to-topology-design-and-performance-metrics>
108. <https://www.emobility-engineering.com/challenge-of-power-torque-density/>
109. <https://www.beyondmotors.io/research/axial-flux-motors-vs-traditional-radial-motors-comparison>
110. <https://newatlas.com/deepdrive-dual-rotor-e-motor/>
111. <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A52023SC0161>
112. <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=COM%3A2023%3A160%3AFIN>
113. <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A52023PC0160>
114. <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401252>
115. <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1252>
116. <https://eitrawmaterials.eu/sites/default/files/2024-11/2021_07-13_REE%20Cluster%20Report.pdf>
117. <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52025DC0945>
118. <https://www.eit.europa.eu/sites/default/files/2021_09-24_ree_cluster_report2.pdf>
119. <https://circulareconomy.europa.eu/platform/sites/default/files/2023-01/Developing%20a%20supply%20chain%20for%20recycled%20rare%20earth%20permanent%20magnets%20in%20the%20EU.pdf>
120. <https://cordis.europa.eu/project/id/101138767>
121. <https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2022.1094055/xml>
122. <https://pubs.acs.org/acsodf/article/8/20/17431/407376/Review-on-the-Parameters-of-Recycling-NdFeB>
123. <https://www.iee.fraunhofer.de/de/anwendungsfelder/energiesystemtechnik/leistungselektronik-elektrische-antriebssysteme/elektrische-maschinen.html>
124. <https://www.ifam.fraunhofer.de/en/technologies/test-bench-for-e-machines.html>
125. <https://ieeexplore.ieee.org/document/9242951/>
126. <https://www.researchgate.net/publication/252033360_Life_expectancy_calculation_for_electric_vehicle_traction_motors_regarding_dynamic_temperature_and_driving_cycles>
127. <https://www.mdpi.com/2071-1050/13/17/9668>
128. <https://www.sciencedirect.com/science/article/pii/S0921344924001769>
129. <https://www.sciencedirect.com/science/article/pii/S2212827126006104>
130. <https://www.nist.gov/publications/optimizing-electric-traction-motor-design-analyzing-benefits-circular-economy>
131. <https://research.birmingham.ac.uk/en/publications/recycling-of-ndfeb-magnets-from-hard-disc-drive-scrap-using-hpms-/>
132. <https://link.springer.com/article/10.1007/s10163-025-02162-2>
133. <https://www.mdpi.com/2075-1702/10/12/1178>
134. <https://www.mdpi.com/1996-1073/15/10/3542>
135. <https://doi.org/10.3390/wevj17050249>
136. <https://www.iisb.fraunhofer.de/en/research_areas/power_electronics/inverters/projects_inverters.html>
137. <https://www.izm.fraunhofer.de/en/business_units/power_electronics/electricdrivetechnology.html>
138. <https://www.ict.fraunhofer.de/en/topics/electric-mobility.html>
139. <https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32023R1804>
140. <https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52025DC0260>
141. <https://eur-lex.europa.eu/EN/legal-content/summary/deployment-of-alternative-fuels-infrastructure.html>
142. <https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A42023X0401>
143. <https://eur-lex.europa.eu/EN/legal-content/summary/road-safety-driving-licences.html>
144. <https://eur-lex.europa.eu/EN/legal-content/summary/two-or-three-wheeled-motor-vehicles-maximum-design-speed.html>
