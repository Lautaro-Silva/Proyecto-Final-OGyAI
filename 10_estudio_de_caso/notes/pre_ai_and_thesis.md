# Pre-AI research history and thesis/GAP scientific baseline: evidence notes

**Agent scope:** the human research history before the AI period (before 2026-08-29) and the scientific baseline the AI sessions started from. That covers the lab notebook, script evolution, the origin of the `HasStation` requirement, the failed Fast-MC toy model, the GAP-note versions, the thesis claims about the SD inversion, and figures that could be reused in a talk.

**Sources read**
- `Notas  - Latex/Trabajo.tex` (862 lines, read in full) and `Notas  - Latex/Notas Iniciales.tex` (lines 1–100 read; rest grepped).
- Git history of the worktree (`git log --all`, pickaxe `-S HasStation`, `-S GetStationById`, `-S 'sdStation is None'`, `-S 'Corte de Calidad 1'`), plus historical file contents read with `git show`/`git grep` at commits e1aeefe, e9a2737, 41b98be, ce4e0eb and 26ebcf1.
- `Scripts/Procesamiento_ADST_v8-2.py` (l.150–345), `Scripts/Procesamiento_ADST_Campo_v9.py` (l.136–148), `Scripts/Procesamiento_Datos_Campo/readADST_data_v19.py` (l.150–165).
- `Scripts/Intento Toy Model para Inversion Fallido/mc_model_muonic_divergence_v1.ipynb` (5 cells) and `_v2.ipynb` (22 cells): code sources and stdout streams only. Neither notebook has markdown cells, and no `.py` versions exist.
- `GAP_Notes_Latex/[Version_Vieja]GAP_41/main.tex` (350 lines), `GAP_Notes_Latex/GAP2026_041/main.tex` (272 lines) and `GAP_Notes_Latex/[UNFINISHED]GAP_Core_REC/main.tex` (95 lines), all read in full.
- Thesis `Tesis - Latex/capitulos/06_infill.tex` (read in full), `03_fenomenologia.tex` (l.51–102) and `05_anillo_denso.tex` (grepped). Dated with `git blame`.
- Figures viewed: `.../cap6/SD_Desglose_Componentes_vs_UMD.pdf`, `claude_work/presentacion_rafa_2026/figuras/sd_hasstation_antes_despues.pdf`, and `claude_work/reprocesamiento_sd_completo/resultados/SD_sin_corte_vs_UMD_reprocesado_v13.png` and `SD_Desglose_MC_vs_REC_TwinAxes.png`.

**Coverage gaps**
- I did not read the transcripts. That is outside my scope; other agents cover them.
- `Comandos.odt` and `Notas.odt` are binary and were not read.
- The Foundations talk script `Scripts/Presentacion_Foundations/presentacion_feb_2026_v2.py` was only listed, not read.
- Neither GAP file contains a date finer than "August 2026", and neither says who made the edits between the two versions.
- `Notas Iniciales.tex` l.100–156 was only grepped.

---

## 1. Chronological events

All dates come from git commit dates (author TZ −03:00) or from dates the author wrote in `Trabajo.tex`. Git shows "Lautaro Silva"/"Lautaro" as the author of everything before 2026-08-29.

| Date | Actor | Event | Evidence |
|---|---|---|---|
| 2025-09-01/05 | USER | Repository created; first reading notes on the GAP notes (Pryke 1998, Billoir 2002, Bradfield 2022) | commits e6f0125, a5e43dd, 497486e; `Notas Iniciales.tex` |
| 2025-10-01 | USER (code adapted from colleague "Marina") | First PyROOT reader `Scripts/ejemploPYrootMarina.py`. It calls `sEvent.GetStationById(sdId)` with **no** `HasStation` guard, next to the comment "en simulaciones, el counterId no es el mismo que la station Id" | e1aeefe:`Scripts/ejemploPYrootMarina.py:147` |
| 2025-10-07/09 | USER | `Test_PyRoot_v3/v4/v5`. The guard `sdStation = sEvent.GetStationById(sdId) if sEvent.HasStation(sdId) else None` appears for the first time. At this stage it is only a **null guard**: the counter is still kept and `sdSignal=None` (`sdSignal = sdStation.GetTotalSignal() if sdStation else None`) | e9a2737:`Scripts/Test_PyRoot_v4.ipynb:289–290` |
| 2025-10-09 | USER | Lab notebook starts: 600 ADST files from Marina are being read | `Trabajo.tex:3–5` |
| 2025-10-30 | USER | First parallel pipeline (4 workers) on the "Alexey" production (`Procesamiento_ADST_Alexey`) | `Trabajo.tex:29–63`; 671fd76 |
| 2025-11-04 | USER + colleague "Carmi" | "Deep dive": (1) the old reader iterated over `SDEvent` and silently dropped the Dense-Ring 90k stations; (2) about 1/3 of the modules were flagged `rejected`, deliberately, by the simulation author; (3) a **"Corte Diferido"** policy was adopted: store `is_sd_saturated` as a flag instead of filtering, "así puedo hacer el corte de calidad después en pandas y… comparar los resultados con y sin el corte" | `Trabajo.tex:156–175` |
| 2025-11-05 | USER (probably with a web chatbot, see §3) | The counter loop now iterates over `MDEvent`. **This is the first version in which a missing reconstructed SD partner removes the counter**: `if sdStation is None: counterIterator += 1; continue`, commented "# 1. Seguimos necesitando esto. Sin sdStation, no hay geometría." The very next lines turn saturation into a flag: "# 2. ¡TU IDEA! Creamos el flag en lugar de filtrar." | 41b98be:`Scripts/Procesamiento_ADST_modulos_adaptado.ipynb:154–162` |
| 2025-11-06/11 | USER | First A1 fits. SD and UMD results look null or noisy, and interpretations such as mass sign changes and a geomagnetic "competition" were written down | `Trabajo.tex:227–437` |
| 2025-11-11 | USER + supervisors (Juan, Fede) | **Dense Ring φ double-subtraction bug** found: `phi_rel = sdStation.GetAzimuthSP() - sShower.GetAzimuth()` was applied to 90k stations whose `GetAzimuthSP()` is already shower-relative. Pipeline v7 was created. The earlier "physics" conclusions are recognised as a "error de pipeline, no de física" | `Trabajo.tex:439–470`; the buggy line is visible at 41b98be (`phi_rel = sdStation.GetAzimuthSP() - sShower.GetAzimuth()`) |
| 2025-11-11 | USER | The skip receives its lasting label, "# --- Corte de Calidad 1: Geometría --- / # Si no hay sdStation, no podemos calcular r_core ni phi_plane. / # Ese counter no sirve para el análisis de asimetría." | ce4e0eb:`Scripts/Procesamiento_ADST_v4.ipynb:188–193` |
| 2025-12-02 | USER | Dense Ring analysis "dio perfecto" | bfd981c; `Trabajo.tex:474–531` |
| 2026-01-13 → 01-20 | USER | Infill A1 ≈ 0. The author suspects `GetAzimuthSP()` returns ground angles for Infill and adds a manual 3D Euler rotation (`readADST_surface_v11`) | `Trabajo.tex:533–583` |
| 2026-01-20 | USER | First mention of an "inverted" behaviour, but **near the core**: "Zona Próxima (r < 400 m): Se observó un comportamiento invertido (valle en φ=0) y ruidoso", attributed to PMT saturation and the LDF slope. This is **not** the far-core SD inversion | `Trabajo.tex:588` |
| 2026-02 | USER | Pipeline v12, "La Mariposa/Trompeta" validation plots, SD muon and EM components loaded separately | `Trabajo.tex:594–627`; ea86e4e (2026-02-05) |
| 2026-02 (late) | USER + collaboration (Lorenzo, Juan, Fede, Joaquín, Darko) | Foundations meeting. Feedback: use the true MC core; split SD into EM and µ (Fede); the `GetAzimuthSP` "bug" was *agreed* at the meeting ("Se acordó que la función nativa presenta inconsistencias para el Infill") | `Trabajo.tex:790–862`; commits 2a2030e, 3ab4740 |
| 2026-03-24 | USER | **Euler-fix suspicion retracted** in the commit message: "arreglado de una vez por todas el problema de los angulos. La funcion andaba, los plots esos fueron todos al pedo y finalmente pude ver la asimetria en el infill" | b0f562d |
| 2026-03-30 → 05-16 | USER | Thesis writing starts. Ch. 3 is "pseudoterminado" on 04-13 and Ch. 5 is finished on 05-16 | 70a08a7, 4148250, 8a61ffa |
| 2026-06-03 | USER | Real-data (field) pipeline works | de902b0 |
| 2026-06-07 → 06-12 | USER | Ch. 6 (Infill) is written, including the SD-inversion text: "Esta inversión geométrica no es un artefacto de reconstrucción…" | 7691975…26ebcf1; blame of `06_infill.tex:67` gives 26ebcf16 (2026-06-12) |
| ≤2026-07-13 [dates within this window UNKNOWN] | USER | Fast-MC toy model `mc_model_muonic_divergence_v1/v2.ipynb` built and run on this server (8 cores, 10⁷–10⁸ toy muons) | notebook stdout; the files were committed only later, in 2f92cbc (2026-08-29) |
| 2026-07-13 | USER | Toy model abandoned: "update de que no voy a poder hacer el modelo MC para explicar la discrepancia. faltaria modificar el texto que esta horrible". This commit adds 18 lines to `06_infill.tex` (the future-work roadmap) | 6d6b97b |
| 2026-07-14/17 | USER | Ch. 3 rewritten around "Población A/B" and a Billoir term with a negative sign; Ch. 6 l.80–96 rewritten to invoke it | 42e064d, 1b90b8a (blame of 03:79–101 and 06:80–105) |
| 2026-08-03 | USER | Last pre-AI thesis edit. Ch. 6 l.152–154: the inversion "no es una falla de Monte Carlo, sino un obstáculo experimental empírico" | de463a7 (blame of 06:152,154) |
| "August 2026" (no finer date) | USER + supervisors (per brief) | GAP draft "[Version_Vieja]" (kinematic-divergence story) turned into published GAP-2026-041 (divergence derivation removed, side-wall hypothesis added) | `\date{August 2026}` in both files; both committed only in c915ce7 (2026-08-31) |
| 2026-08-29 | USER / AI | AI period begins: CLAUDE.md is added, and 2f92cbc "updates codigo server" commits the toy-model notebooks | fa012d6, 2f92cbc |
| 2026-09-17 | claude-opus-5 (per commit trailer) | First reprocessing that keeps SD stations with no reconstructed partner. Its commit message states: "The v17 reader skips a UMD counter whenever its SD partner has no reconstructed station (HasStation), so the parquet only ever contained reconstructed SD stations." | 8d4b5a0 (author "Lautaro Silva"; trailer "Co-Authored-By: Claude Opus 5"; it also cites the "Astra" extraction) |

**Git verification (item 4):** `git log --all` on `03_fenomenologia.tex`, `05_anillo_denso.tex` and `06_infill.tex` shows **no commits after 2026-08-03 (de463a7)** on any branch. Every thesis sentence quoted in §2 therefore predates the AI period. The AI-era thesis revisions live only in separate draft files, e.g. `870a8f7` (2026-09-03) adds `03_fenomenologia_DRAFT.tex` and `05_anillo_denso_DRAFT.tex` under `claude_work/`. The main checkout also has an untracked `claude_work/borradores_capitulos_3_5_6_integrados_2026_09_24/`, which I did not read.

---

## 2. Physics claims made before the AI period, and what happened to them

### 2.1 The HasStation requirement existed from the start (as a guard) and became a hard cut on 2025-11-05
- **What the code did.** The guard existed from 2025-10-09 (e9a2737). It started excluding counters on 2025-11-05 (41b98be), with the stated reason "Sin sdStation, no hay geometría". On 2025-11-11 (ce4e0eb) it was relabelled "Corte de Calidad 1: Geometría … Ese counter no sirve para el análisis de asimetría". The same construct is still in `Scripts/Procesamiento_ADST_v8-2.py:182–187`, `Scripts/Procesamiento_ADST_Campo_v9.py:141–146` and, for real data, `Scripts/Procesamiento_Datos_Campo/readADST_data_v19.py:157`.
- **Was it ever questioned before the AI period?** **No.** `Trabajo.tex`, `Notas Iniciales.tex`, the thesis chapters and both GAP versions never mention `HasStation`, a reconstructed partner, or selection bias in station choice (grep for `HasStation|selecci|partner|GetStationById` in `Notas  - Latex/*.tex` returns only unrelated "sesgo" hits: the energy bias and the GetAzimuthSP "sesgo"). The only recorded rationale is the geometric one in the code comment.
- **Was that rationale still valid? [INFERENCE, supported by code]** By v8-2 the Infill geometry no longer depends only on the reconstructed station. The Euler/true-core path takes positions from the detector-geometry database (`pos_station = geo.GetStationPosition(sdId)`, `v8-2.py` about l.288–323; `phi_plane_euler_MC_true_core`). The reconstructed station is still used for `GetAzimuthSP`/`GetSPDistance` (l.246, 272–273) and for SD signals. The original justification ("no sdStation, no geometry") had therefore at least partly lapsed for the MC-geometry Infill analysis, but the skip was never revisited.
- **An irony that makes a good talk slide.** The author's own "Corte Diferido" principle, recorded on 2025-11-04 (`Trabajo.tex:167–168`: "no filtrar en el script de procesamiento, sino guardar un nuevo flag … comparar los resultados con y sin el corte"), was applied to saturation (`# 2. ¡TU IDEA! Creamos el flag en lugar de filtrar.`) in the same code block that turned HasStation into a hard `continue`. In the field-data reader the skip is followed immediately by the comment "NO hacemos skip: es el análisis quien decide qué filtrar" (`readADST_data_v19.py:156–163`). That comment refers to the rejection flags, not to HasStation.
- **Precedent for a selection filter creating an artefact.** In Nov 2025 the author had already found that a filter, `rejected`, was hiding the Dense-Ring data (`Trabajo.tex:164–165`, "mi código … los estaba filtrando estúpidamente"). That lesson was not generalised to HasStation.

### 2.2 Claims about the SD inversion's cause

| Claim | Where / when | Fate |
|---|---|---|
| "Esta inversión geométrica no es un artefacto de reconstrucción, sino una propiedad física intrínseca de la cascada registrada a nivel del suelo, sugiriendo que el tanque Cherenkov integra poblaciones de partículas con asimetrías diametralmente opuestas." | `06_infill.tex:67`; USER, 2026-06-12 (26ebcf1) | **Contradicted by later evidence.** The inversion appears only with the HasStation requirement (`sd_hasstation_antes_despues.pdf`; 8d4b5a0). In a sense it *is* a reconstruction artefact: a selection on SD reconstruction. The thesis source has not been corrected (no commits after 2026-08-03). |
| The SD tank is flooded by "Población B: muones de baja energía con un momento longitudinal muy bajo (p_z ∼ p_t)" | `06_infill.tex:80`; 2026-07-17 (1b90b8a) | Not supported. The SD-muon A1 without the requirement stays ≈ +0.06–0.07 out to 1275 m (figure below), so no population-driven inversion appears in the unselected MC. |
| "Como fue derivado analíticamente por Billoir, el ensanchamiento espurio de la región tardía está gobernado por el término asimétrico 𝒜_geo…" / "provocando que el factor ⟨p_r / −p_z⟩ explote a grandes distancias radiales con valores negativos" | `06_infill.tex:82,84`; 2026-07-17 | **Internally inconsistent with the author's own GAP notes.** Both GAP versions state that the Billoir term is strictly positive: "the amplitude A_geo is strictly positive … acts additively with atmospheric attenuation" (`[Version_Vieja]GAP_41/main.tex:97`; `GAP2026_041/main.tex:100`). The thesis Ch. 3 says the opposite: "posee signo opuesto necesariamente" (`03_fenomenologia.tex:88`). ⟨p_r/−p_z⟩ with −p_z>0 and p_r≥0 cannot be negative. |
| "…el artefacto de proyección topográfica colapsa matemáticamente a cero (lim_{p_z→∞} 𝒜_geo → 0)" (UMD as a "filtro cinemático") | `06_infill.tex:94–96`; `03_fenomenologia.tex:101`; 2026-07-17 | The mathematical limit is correct, but the explanatory role depends on the inversion being physical. Not supported once the selection bias is known. |
| "…este desglose poblacional demuestra de manera irrefutable que la mera detección de la componente muónica en superficie no es suficiente…" | `06_infill.tex:98`; blame 57c46f5 (2026-07-13) | Overclaim. Contradicted by the no-requirement SD-muon curve, which roughly tracks the UMD (difference compatible with zero in a 95% simultaneous band beyond about 900 m, `SD_sin_corte_vs_UMD_reprocesado_v13.png`, lower panel). |
| "…la inversión observada en el SD Total es el resultado determinista de convolucionar un frente electromagnético asimétrico positivo con este fondo muónico superficial dominado por el efecto geométrico." | `06_infill.tex:84` | Not supported (as above). |
| The inversion survives REC geometry because "la compresión geométrica … es tan masiva…"; "confirmando que este artefacto no es una falla de Monte Carlo, sino un obstáculo experimental empírico" | `06_infill.tex:152–154`; 2026-08-03 (de463a7) | Not supported. The REC-geometry analysis used the same HasStation-filtered parquet, so the persistence of the inversion is expected from the selection itself. [INFERENCE: I did not verify which parquet the REC figures used; the MC pipeline v8-2 has the skip for all rows.] |
| Earlier June wording: low-energy muons "sufren fuertes retrasos cinemáticos y desviaciones. Por efectos de proyección geométrica…"; also a VEM argument ("un único muón pasante deposita ∼240 MeV") | `06_infill.tex` at 26ebcf1, desglose subsection | Superseded in July by the Población A/B text. |
| GAP draft ("Version_Vieja"): "This far-core inversion is driven by a third phenomenon, the kinematic divergence of low-energy muons" (l.43); "This inversion is a genuine, geometric feature of the SD ground signal" (l.278); "the inversion is entirely driven by the divergent muonic component (Population B)" (l.341) | `[Version_Vieja]GAP_41/main.tex` | Removed or softened in GAP-2026-041 (see 2.3). The "genuine" wording survives in the published note. |
| GAP-2026-041: "This inversion is a genuine feature of the SD ground signal and its physical origin is the central puzzle addressed in this note." (l.197). Two "compounding mechanisms": (i) kinematic, low-energy divergent muons ("plausibly generates", l.260); (ii) instrumental, WCD side-wall exposure and track-length/VEM effects following Bertou–Billoir (l.262) | `GAP2026_041/main.tex` | Neither mechanism is needed to explain the far-core MC SD-muon inversion once the requirement is removed. The side-wall/track-length argument might still matter for *VEM* but not for particle *counts* [INFERENCE]. The published GAP carries the "genuine feature" claim. |
| The SD inversion "ya había sido descripto con anterioridad por la Colaboración" | `06_infill.tex:78`; GAP cites Bradfield, Luce ICRC2021 and GAP2000_017 | [UNKNOWN] whether those prior works used an equivalent reconstructed-station selection. This is worth checking, because it bears on whether the literature inversion is physical. |
| Pre-AI mass/sign-change interpretations of Nov 2025 ("competencia compleja … geomagnético"; proton negative vs iron positive) | `Trabajo.tex:385–391` | **Retracted by the USER** the same day: "Mi fracaso anterior era un error de pipeline, no de física" (`Trabajo.tex:470`), after the φ double-subtraction bug. This is a good pre-AI example of a plausible physical story being built on an artefact. |
| Infill `GetAzimuthSP` is buggy; the Euler fix is required; "Confirmación del Bug en Offline (Joaquín/Darko)" | `Trabajo.tex:560, 810–812, 845–848` (Jan–Feb 2026) | **Retracted by the USER** (b0f562d, 2026-03-24: "La funcion andaba, los plots esos fueron todos al pedo"). It is a second pre-AI example of a confident diagnosis, even endorsed at a collaboration meeting, that turned out wrong. |

### 2.3 GAP draft vs published GAP-2026-041: what changed

Diff of `GAP_Notes_Latex/[Version_Vieja]GAP_41/main.tex` against `GAP_Notes_Latex/GAP2026_041/main.tex`:

- **Title.** Old: "A Phenomenological Study of Early--Late Azimuthal Asymmetries of the Muon Density with the UMD". New: "GAP-2026-041 / Azimuthal Asymmetries in Extensive Air Showers: UMD–SD Comparison and Insights into the Surface-Detector Sign Inversion".
- **Abstract.** Old: three mechanisms, "atmospheric attenuation, the geometric effect, and the kinematic projection of muons". The inversion is "driven by the abundant, highly divergent low-energy muon population", and the UMD collapses "the kinematic divergence contribution … to a negligible level". New: no mechanism is asserted. The difference "is consistent with the combined effect of the low-energy muon population and the distinct geometrical response of the two detectors", and it adds the UMD's "approximately planar buried geometry avoids the side-wall exposure and track-length effects".
- **Removed entirely:** §"Kinematic Divergence: Driving the Late Excess" (old l.99–185). It contained the Cazón-based derivation dN/dΩ ∝ cos α·exp(−p_t/Q), the density scaling S(d,α) ∝ d⁻² cos α exp(−sin α E/cQ) (eq. `kinematic_divergence`), the late/early ratio with the claim that the "exponential gain dominates the spatial expansion", the Population A/B definitions, and the "kinematic filter" principle. The `cancel` package was dropped with it. There is even an author TODO inside this section: "%FALTAN COMENTARIOS ACA" (old l.166).
  - The old text justified the dominance of the exponential gain empirically, in a circular way: "Empirically, the fact that this exponential gain dominates the spatial expansion is confirmed by the severe negative asymmetry measured by surface detectors at large radial distances" (old l.173). In other words, the inversion was used as evidence for the mechanism meant to explain it.
- **Replaced by:** §"Beyond Attenuation and Geometry" (new l.102–105). It notes that the two established mechanisms are strictly positive, so "at least one additional effect, either intrinsic to the shower physics or associated with the specific response of the detector, must be operative", with discussion deferred to the conclusions.
- **Introduction.** Old l.43, "driven by a third phenomenon, the kinematic divergence", was removed. New l.46 adds "through a three-dimensional water volume with non-negligible side-wall exposure". The Cazón model is no longer promised as the interpretation (old l.45 vs new l.48).
- **Scope.** The old version said "proton and iron initiated showers" (l.47); the new one says "proton-initiated showers" (l.50).
- **Results.** Old "in quantitative agreement" became "in qualitative agreement" (l.278 → 197). "genuine, geometric feature" became "genuine feature … central puzzle". The subsection "Signal Dissection and the Kinematic Filter Mechanism" was renamed "Signal Dissection: EM vs. Muonic Contributions". The new version adds a caveat that N^MC_µ,sup counts particles crossing the 3D tank boundary, so "its sign inversion already encapsulates detector-specific geometric biases, such as the differential exposure of the tank's side walls" (new l.231). It also adds the two "structural differences" (energy threshold and detector geometry, l.233).
- **Conclusions.** Old: "the inversion is entirely driven by the divergent muonic component (Population B)" and "the exponential term … collapses to zero" (l.341–343). New: "two compounding mechanisms: a primary physical driver … and a severe instrumental bias associated with the detector's volumetric geometry" (l.258–262), with the Bertou–Billoir side-wall cross-term ∝ (p_z/p_r) cos Φ sin 2θ and a track-length (1/cos θ_local) VEM enhancement. New l.264 hedges: "Regardless of the relative quantitative weight of the kinematic and instrumental effects…". It also adds mass-composition outlook text and Acknowledgements (Prague group, CC IoP, DIRAC).
- **Unchanged:** Table `tab:a1_summary` (SD-EM +0.40/+0.45/+0.44; SD-Muon +0.05/+0.04/−0.10; SD Total +0.11/+0.09/−0.08; UMD N^MC +0.10/+0.12/+0.11 at 450/800/1200 m) and all figures (byte-identical sizes).
- **What neither version mentions:** station selection, the HasStation requirement, or any reconstructed-station cut.
- **Who removed the divergence section:** [UNKNOWN from the files]. The brief says the supervisor did. Nothing in either file or in git attributes it, since both folders arrived together in c915ce7 (2026-08-31).

### 2.4 `[UNFINISHED]GAP_Core_REC/main.tex` ("A study on core reconstruction bias and how it attenuates the early-late asymmetry", `\date{August, 2026}`)

This is a skeleton only: every section is commented narrative threads, and the abstract is empty. Its argument:
- (i) The reconstructed UMD A1 is damped compared with MC truth.
- (ii) A bootstrap "directional counting bias" toy model (the successful Ch. 5 toy) reproduces the damping for θ ≤ 35° but not for θ ≥ 35°.
- (iii) So a spatial error is proposed: fitting a symmetric LDF to an asymmetric footprint "systematically dragging the reconstructed core toward the late region".
- (iv) That core shift produces azimuthal smearing and "non-linear feedback" in UMD counting.

It inherits the divergence premise: "Highly inclined showers feature a late-region density excess due to low-energy, highly divergent muons" (l.40) and "The Underground Muon Detector (UMD) acts as a kinematic filter" (l.41). It mirrors Ch. 5's discussion (`05_anillo_denso.tex:125–145`). [INFERENCE] If the late excess is a selection artefact, the motivation in l.40 needs rewriting. The core-shift/LDF hypothesis itself is independent and remains open.

### 2.5 The failed Fast-MC toy model (`Scripts/Intento Toy Model para Inversion Fallido/`)

**What it assumed** (v1 cells 0–1; v2 cells 0–1, 7, 18):
- Muons are generated independently of any shower.
  - Production height z ~ Gamma(k=10, scale=300 m). In v2's "coupled" version the scale grows with log E.
  - φ is uniform in [−180°, 180°].
  - E follows a power law E^−2.6 on [0.1, 50] GeV.
  - p_T ~ N(p_T_mean, 0.05) clipped at ≥ 0.1 GeV. p_T_mean is 0.3 in v1 and 0.03 in v2, so in v2 the clip dominates and almost every p_T is 0.1 [INFERENCE from the code].
- The radius is purely kinematic, r = z·p_T/E. There is **no lateral shower development and no multiple scattering**. θ is fixed at 45°.
- The density enters through weights, "(Basado en L. Cazón)":
  - geometric weight `w_geo = 1 − (r/z)·tanθ·cosφ` ("Falsa asimetría negativa por mapeo al Ground Plane", v1 docstring);
  - decay weight `w_decay = exp(−l/(γ cτ))`.
- Detector response is a hard energy threshold: SD E ≥ 0.3 GeV (v1) or 0.001 GeV (v2); UMD E ≥ 1 GeV. Output is the A1 per r-bin, or raw azimuthal histograms at r = 400 and 1000 m (v2).
- The path length has **opposite signs in v1 and v2**: v1 uses `l_path = z + r tanθ cosφ`, while v2 uses `l_path = z − r tanθ cosφ` with the comment "early (φ=0): l_path es MENOR". v2 cell 7 switches off the geometric weight ("APAGADO PARA DEBUGGING FENOMENOLÓGICO: Forzamos w_geo = 1.0"), which shows the author was isolating terms.
- Cost: 10⁸ toy muons over 8 cores (v1) and 10⁷ (v2, about 10 s per run), written to `toy_model_data/` parquet chunks.

**Why it failed:**
- The author's commit (6d6b97b, 2026-07-13) says only that he would not be able to build the model.
- The thesis text (`06_infill.tex:105`, 2026-07-17) says: "La limitación intrínseca de este estudio radica en que las simulaciones utilizadas entregan la huella final de la lluvia a nivel del suelo, careciendo de la granularidad necesaria para rastrear la cinemática de producción individual (p_z, p_t y altura de decaimiento z)…". The fix is framed as future work (4 steps, l.107–119).
- [INFERENCE] Three structural points follow from the code:
  - The sign of A1 is set by hand-chosen weights. `w_geo` is *defined* to give a negative (late) contribution, so the model can only reproduce whichever sign its weights encode.
  - The weights use a single fixed θ with no shower-plane/ground geometry.
  - Most importantly for the later story, the toy contains **no station selection**. It was searching for a physical mechanism for an effect that later turned out to come from the reconstruction selection.
- No output figures were inspected (per instructions, outputs were not printed), so whether the toy's plotted A1 was positive, negative or null is [UNKNOWN]. v2's stdout confirms runs at r = 400 ± 50/200 m and 1000 ± 50/200 m.

---

## 3. AI workflow techniques observed (pre-AI baseline only)

- **Evidence of chatbot-assisted code before Claude Code or Codex [INFERENCE].** The Nov 2025 reader contains conversational, second-person comments typical of a web-chat LLM answer:
  - "# --- ❗️ CAMBIO DE LÓGICA ❗️ ---", "# 2. ¡TU IDEA! Creamos el flag en lugar de filtrar." (41b98be, `Procesamiento_ADST_modulos_adaptado.ipynb:156–163`);
  - in v8-2, "print(\"Librerías cargadas correctamente. ¡Listo para trabajar! 🚀\")" (l.59), "# ❗️ 3. CAMBIO CRÍTICO: imap_unordered + chunksize=1 ❗️" (l.731), "# [OPTIMIZACIÓN v17]…", and "# Usamos los métodos que el Hunter encontró como NO NULOS" (l.207).

  The HasStation hard skip was introduced in that same edit. Which tool and model were used is [UNKNOWN]; this should be asked (§7). If confirmed, the selection bias was *introduced* during an earlier, unlogged AI-assisted session and *found* in the logged AI sessions, which is a notable framing point for the report.
- **Human review gates were already part of the method:** supervisor and colleague debugging caught the φ double subtraction (`Trabajo.tex:441`, "tuve una larga discusión con mis directores") and the `rejected` filter ("Hablé con Carmi", `Trabajo.tex:158`). Collaboration-meeting feedback set the SD EM/µ split (`Trabajo.tex:839–843`), which produced the key desglose figure.
- **Explicit null-test planning** (isotropy in φ_in, energy invariance; `Trabajo.tex:640–647`). These tests check detector isotropy, not station-selection effects.

---

## 4. Failures, errors, corrections before the AI period

1. **Dense Ring φ double subtraction** (introduced by Nov 2025, 41b98be; found 2025-11-11 by the USER with supervisors Juan and Fede). It had produced spurious "physics" conclusions (mass-dependent sign flips) that were written up and then retracted (`Trabajo.tex:385–391` vs `439–470`).
2. **`rejected` filter hid the Dense Ring** (found 2025-11-04 with Carmi; `Trabajo.tex:161–165`).
3. **Infill GetAzimuthSP "bug"** (Jan–Feb 2026). The Euler workaround was built and presented at the Foundations meeting, and colleagues "confirmed" the bug. The USER retracted it on 2026-03-24 (b0f562d).
4. **HasStation hard cut** (introduced 2025-11-05, 41b98be). It was never questioned before the AI period and later shown to create the far-core SD inversion (8d4b5a0; figures in §5).
5. **The "genuine/physical inversion" narrative** was built on (4). It lives in the thesis (Ch. 3 l.79–101, Ch. 6 l.67–98, 152–154) and in GAP-2026-041 (l.197, 256–264).
6. **Sign inconsistency for the Billoir term:** Ch. 3 l.88 and Ch. 6 l.84 (negative) vs GAP l.97/100 (strictly positive).
7. **Fast-MC toy abandoned** (2026-07-13). The v1/v2 path-length sign flip and the dominance of the p_T clip in v2 are latent issues [INFERENCE].
8. **Personal document in the repo.** `GAP_Notes_Latex/GAP2026_041/SILVA_lautaro.pdf` is the author's UBA academic transcript, with national ID number, issued for CONICET. It is committed in git (c915ce7) and unrelated to the GAP. Contents are deliberately not reproduced here; the author should decide whether it belongs in the repo.

---

## 5. Human-in-the-loop moments and reusable figures

### 5a. Quotes that show the author steering
- "Esto no lo logré, lo cual es una cagada y no me queda claro si estoy haciendo algo mal, o por qué no se ve lo que espero." (`Trabajo.tex:94`, 2025-11-04)
- "Mi fracaso anterior era un **error de pipeline, no de física**." (`Trabajo.tex:470`, 2025-11-11)
- "La mejor metodología es no filtrar en el script de procesamiento, sino guardar un nuevo flag…" (`Trabajo.tex:168`)
- "La funcion andaba, los plots esos fueron todos al pedo" (b0f562d, 2026-03-24)
- "no voy a poder hacer el modelo MC para explicar la discrepancia. faltaria modificar el texto que esta horrible" (6d6b97b, 2026-07-13)
- In the draft chapter's own to-do list: "Y HABRIA QUE VER SI SE PUEDE METER ALGO DE LA JUSTIFICAICON DE LA INVERSION DE ASIMETRIA EN EL SD … UNA EXPLCAICION, UN TOY MODEL O ALGO ASI" (`06_infill.tex:179`)

### 5b. Figures reusable for a talk

| Path | What it shows | Pre/post-AI |
|---|---|---|
| `Tesis - Latex/capitulos/imagenes_capitulos/cap6/UMD_vs_SD_Total_Asymmetry.pdf` (also `GAP_Notes_Latex/*/UMD_vs_SD_Total_Asymmetry.pdf`, `claude_work/presentacion_rafa_2026/figuras/umd_vs_sd_total_asymmetry.pdf`) | A1 vs r_MC, 30–40°, proton SIB2.3e, true MC geometry: UMD N_µ^REC positive and flat; SD Total (VEM) peaks near 700 m and inverts beyond about 1050 m. The "puzzle" figure. | pre-AI |
| `.../cap6/SD_Desglose_Componentes_vs_UMD.pdf` (and GAP copies, `presentacion_rafa_2026/figuras/sd_desglose_componentes_vs_umd.pdf`) | Four components on twin axes: UMD N_µ^MC (≈0.06→0.11, positive), SD EM N^MC (0.28→0.46, positive), SD surface muons N^MC_µ,sup (+0.06, turning negative near 950 m, −0.12 at 1275 m), SD Total VEM (+0.13 at 675 m → −0.10 at 1275 m). All **with** the HasStation requirement, which the figure does not say. | pre-AI |
| `.../cap6/Global_A1_vs_R_Theta_MC.pdf` (`presentacion_rafa_2026/figuras/global_a1_vs_r_theta_mc.pdf`) | UMD A1(r) for all θ bins, MC geometry: growth with r and θ | pre-AI |
| `.../cap6/UMD_Asymmetry_MC_vs_REC.pdf` | UMD N^MC vs N^REC at 40–50°: REC damped, same shape | pre-AI |
| `.../cap5/Evolucion_Asimetria_vs_Theta.pdf` (`GAP_Notes_Latex/*/`, `presentacion_rafa_2026/figuras/evolucion_asimetria_vs_theta.pdf`) | Dense Ring (450 m) A1 vs θ for UMD REC, UMD MC and SD: SD > UMD at moderate θ, hierarchy inverts at high θ | pre-AI |
| `GAP_Notes_Latex/*/Ajuste_UMD_MC_Bin9.pdf`; `.../cap5/Ajuste_UMD_REC_Bin9.pdf` | Example harmonic fit (A1 = 0.083 ± 0.005, UMD MC) | pre-AI |
| `.../cap5/Mass_Discrimination_MF.pdf`, `toy_model.pdf`, `directional_bias.pdf`, `muon_counting_validation.pdf`, `DenseRing_Systematics_*.pdf`, `Hadronic_Uncertainty_Helium.pdf` | Ch. 5 results (MF ≈ 2.5, bootstrap toy, directional counting bias, null tests) | pre-AI |
| `.../cap3/efecto_geo_luce_icrc2021.png`, `divergencia_angular.png`, `esquema_lluvia.png` | Geometry schematics (early/late, emission angles, from Luce ICRC2021) | pre-AI |
| `claude_work/presentacion_rafa_2026/figuras/sd_hasstation_antes_despues.pdf` | **The key before/after figure.** Two panels, same bins, weighted fit, one row per SD station and event, proton SIB2.3e, 30–40°, true MC geometry. **SD muonic count:** before HasStation, A1 ≈ +0.03 → +0.06–0.07, flat to 1275 m; with HasStation=True, identical up to 675 m, then +0.040 (825 m), −0.016 (975), −0.064 (1125), −0.124 (1275). **SD EM count:** before, 0.46 → 0.52 rising; with the requirement, a plateau at ≈0.45 (the "plateau" noted in `06_infill.tex:76` is also a selection effect [INFERENCE]). | AI era (Sept 2026) |
| `claude_work/reprocesamiento_sd_completo/resultados/SD_sin_corte_vs_UMD_reprocesado_v13.png/.pdf` | Top: UMD (selected), SD µ before and after HasStation. Bottom: A1(SD) − A1(UMD) with a 95% simultaneous band. "Before" is compatible with the UMD difference band; "after" drops to about −0.2. | AI era (8d4b5a0 / 0ecae20) |
| `claude_work/reprocesamiento_sd_completo/resultados/SD_Desglose_MC_vs_REC_TwinAxes.png/.pdf` | The four-component figure redrawn with solid lines for "sólo MC" (no requirement) and dashed lines for "con SD REC". A direct before/after version of the thesis desglose figure. | AI era (c332ab8) |
| `claude_work/reprocesamiento_sd_completo/resultados/SD_sin_corte_vs_UMD_insumos_astra.png/.pdf` | Same comparison computed from gpt-6-astra's inputs (cross-check) | AI era |

Numbers for the brief: the table `claude_work/revision_asimetrias_sd_umd/02_notebooks/03_sd_vs_umd/RESULTADO.md:15–16` gives, for the SD µ before and after the requirement, +0.0683 and −0.0641 at 1050–1200 m, and +0.0689 and −0.1240 at 1200–1350 m. The brief's "−0.095" is roughly the mean of the two far bins [INFERENCE]; I did not find the value −0.095 itself. The direction in the corrected brief is **confirmed**: the inversion appears only **with** HasStation.

---

## 6. The selection-bias thread (pre-AI part)

- **First appearance of the code:**
  - 2025-10-01: `GetStationById` with no guard (e1aeefe).
  - 2025-10-09: guard as null-check only (e9a2737).
  - **2025-11-05: hard skip** (41b98be), with the rationale "Sin sdStation, no hay geometría".
  - 2025-11-11: labelled "Corte de Calidad 1: Geometría" (ce4e0eb).
  - It is carried unchanged through v5, v6, v7, v8, v8-2 (2026-03-24, b0f562d), the field-data v9 and `readADST_data_v19`.
- **Pre-AI discussion: none.** There is no mention in the lab notebook (Oct 2025 – Feb 2026), the thesis chapters (up to 2026-08-03), or either GAP version. The inversion was always attributed to physics (divergence, Population B, Billoir term) or to the detector (WCD side walls, track length).
- **Was a selection explanation ever hinted at?** The closest pre-AI statements are `06_infill.tex:67` ("no es un artefacto de reconstrucción"), which explicitly *rules out* reconstruction, and the GAP-2026-041 caveat that N^MC_µ,sup "already encapsulates detector-specific geometric biases" (l.231), which points to detector geometry, not selection.
- **Later AI-era handling (for context only; other agents cover the details):**
  - 114fd52 (2026-09-17): "Fill slide 23 with preliminary HasStation selection-bias finding".
  - 8d4b5a0 (2026-09-17, Co-Authored-By Claude Opus 5): reprocess keeping non-reconstructed stations. Its commit message credits "Astra" for extractions (`adst_counts_fast.csv`, `comparacion_directa.csv`) and says Astra's "or not simCounter" variant "discarded 63747 valid rows".
  - c332ab8 and 0ecae20 (2026-09-24): the figures above.
- **Mechanism consistency check [INFERENCE].** HasStation requires the SD partner to be part of the reconstructed event, which in practice means triggered and not removed. Far from the core, triggering probability depends on the station's own signal, which is azimuthally modulated by the large positive EM asymmetry (+0.45 to +0.52). Late-side stations then pass the cut only when their signal fluctuates up, including their muon count. That would bias the *surviving* stations' muon counts toward the late side and depress the EM plateau, which is qualitatively what `sd_hasstation_antes_despues.pdf` shows. The UMD curve in the same figures is also "seleccionado" yet stays positive, which fits the idea that UMD counts are only weakly correlated with the SD trigger. This deserves a proper test, not an assertion.

---

## 7. Open questions for the author

1. Which tool wrote the Nov 2025 reader code with "¡TU IDEA!", "❗️ CAMBIO DE LÓGICA ❗️" and "el Hunter encontró"? Was it a web chatbot (ChatGPT, Gemini, Claude.ai)? Did you or it propose `if sdStation is None: continue`? (41b98be)
2. After the Euler/`geo.GetStationPosition` path existed, did you consider dropping the HasStation skip, given that its only stated reason ("sin sdStation, no hay geometría") no longer fully applied?
3. Who removed the kinematic-divergence section from the GAP draft, when, and with what comment? Is there an email or review record? The files carry no finer date than "August 2026".
4. Do the Bradfield/Luce ICRC2021/Bertou–Billoir SD inversions come from analyses with an equivalent "reconstructed/triggered station" requirement? That decides whether the literature inversion is physical.
5. The thesis Ch. 3 l.88 says the Billoir term has the opposite sign to attenuation, while the GAP says it is strictly positive. Which one do you stand by? Ch. 3 and Ch. 6 need rewriting either way.
6. Did the REC-geometry Infill figures (Ch. 6 §"geometría reconstruida", l.121–154) use the same HasStation-filtered parquet? If so, l.152–154 should be revisited.
7. Is GAP-2026-041 already distributed within the collaboration? If yes, does "This inversion is a genuine feature of the SD ground signal" (l.197) need an erratum or follow-up note?
8. Should `GAP_Notes_Latex/GAP2026_041/SILVA_lautaro.pdf` (a personal academic transcript with an ID number) stay in the git history?
9. What did the Fast-MC toy's plots actually show (A1 sign at 1000 m for SD and UMD), and was the v1→v2 sign flip in `l_path` a deliberate correction?
