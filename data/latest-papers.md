# Latest papers for 程旭丽

Updated: 2026-11-06T04:51:31.074045+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Machine-Learning Molecular Dynamics Reveals Grotthuss Transport in Concentrated Electrolytes

- Source: arXiv
- Date: 2026-11-03T09:24:13Z
- Venue: physics.chem-ph, cond-mat.other
- Authors: Øystein Gullbrekken, Sondre Kvalvåg Schnell
- Link: https://arxiv.org/abs/2611.04558v1
- Score: 12.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 质子转移是酸性或碱性水溶液中异常高电导率的原因。然而，质子转移机制对浓缩水溶液电导率的贡献尚不清楚。在这项工作中，我们使用具有机器学习原子间势（ MLIP ）的分子动力学模拟来计算具有不同浓度的KOH （ aq ）系统的传输特性，其中包括质子转移。 我们量化了质子转移机制对氢氧化物离子和水分子扩散率的贡献，以及电解质的离子电导率和迁移数。在较低的浓度下，这种贡献很大，但在非常高的浓度下会减少。
**讨论重点：** 质子转移是酸性或碱性水溶液中异常高电导率的原因。然而，质子转移机制对浓缩水溶液电导率的贡献尚不清楚。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 2. A Hybrid Message-Passing and Electric-Field Representation for Electrostatic QM/MM Embedding with Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-10-30T10:16:32Z
- Venue: physics.chem-ph, physics.bio-ph, physics.comp-ph
- Authors: Raphael T. Husistein, Shobhit S. Chaturvedi, Thomas Weymuth, Beatriz Piniello, Sélène Forget, Kresten Lindorff-Larsen
- Link: https://arxiv.org/abs/2610.41523v1
- Score: 12.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 3. Does System Size Matter in Uncertainty Quantification for Machine Learning Interatomic Potentials?

- Source: arXiv
- Date: 2026-10-29T14:20:35Z
- Venue: cs.LG, cond-mat.mtrl-sci
- Authors: Chayaphol Lortaraprasert, Nontawat Charoenphakdee, Wenwen Li, Yong-Bin Zhuang, Yuta Tsuboi
- Link: https://arxiv.org/abs/2610.40126v1
- Score: 11.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Machine-learning interatomic potentials (MLIPs) commonly use uncertainty estimates to flag out-of-distribution (OOD) configurations and select structures for active learning. A key question is whether the resulting structure-level uncertainty scores remain comparable across different system sizes. A common practice is to aggregate per-atom uncertainties by their mean or maximum and compare the resulting score against a fixed threshold, implicitly assuming such comparability. We test this assumption across several in-distribution (ID)/OOD pairs by characterizing both aggregations as a function of atom count. The two aggregations exhibit distinct size dependencies. Mean aggregation remains size-independent for homogeneous systems but loses sensitivity to defects in large cells. In contrast, maximum aggregation grows with system size for ID systems while remaining approximately flat for defect-containing systems, narrowing the ID-OOD gap in a manner consistent with extreme-value statistics. Although highly uncertain atoms in large structures may indicate novel local environments, retraining on these structures yields little improvement, in contrast to retraining on OOD structures constructed to lie outside the training distribution. Our results reveal a practical limitation of size-unaware uncertainty criteria and motivate size-aware calibration for more reliable OOD detection in large-scale atomistic simulations.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 4. Distilling Large-Scale Machine Learning Interatomic Potentials to Predict Long-Timescale Electrolyte Transport Properties

- Source: arXiv
- Date: 2026-10-29T07:12:15Z
- Venue: physics.chem-ph, cond-mat.mtrl-sci, cond-mat.soft
- Authors: Ishan Amin, Yue Jian, Nitesh Kumar, Christine Zhang, Jianwei Lai, Casey S. Mezerkor
- Link: https://arxiv.org/abs/2610.39513v1
- Score: 11.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Accurately predicting the transport properties of liquid electrolytes is critical for next-generation battery design and requires force fields that are both quantum-mechanically accurate and fast enough for long-timescale simulation. Recent large-scale pretrained machine learning interatomic potentials (MLIPs) approach density-functional-theory accuracy, but remain too slow to access the necessary timescales to converge transport properties. We provide a knowledge distillation procedure to transfer the accuracy of a large-scale "teacher" MLIP into fast, system-specific "students", without any additional ab initio data. Our distilled models run ~40x faster, reproduce teacher-predicted structural observables, and produce stable 20 ns trajectories in days, rather than the months the teacher would require. Across a diverse set of sodium- and lithium-ion electrolytes, student-predicted self-diffusivities, ionic conductivities, and shear viscosities track experiment and outperform classical force-field predictions, establishing distillation as a practical route to accurate, long-timescale simulations necessary for high-throughput electrolyte screening.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 5. Learning Between the Lines: Interaction Interpolation in a Multi Element Machine Learning Interatomic Potential

- Source: arXiv
- Date: 2026-10-28T20:45:15Z
- Venue: cond-mat.mtrl-sci
- Authors: Ademola Soyemi, Kipton Barros, Timothy C. Germann, Benjamin T. Nebgen, Brenden W. Hamilton
- Link: https://arxiv.org/abs/2610.38876v1
- Score: 10.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：The continuous development of machine learning inter-atomic potentials (MLIAPs)has greatly accelerated materials research in recent years. However, the need to con- struct custom MLIAPs for each unique problem remains a bottleneck which raises the question of the transferability of MLIAPs. While foundation MLIAPs can achieve transferability due to the broad coverage of chemical space represented in their training sets, their size and computational cost limits their routine use. We address this gap by developing a lightweight general-purpose MLIAP for metal alloys spanning twelve elements (Al, Sc, Ti, V, Cu, Zn, Zr, Nb, Mo, Hf, Ta, W). Here, we utilize a step-wise active learning (AL) approach to develop a compact yet diverse dataset and model that generalizes well by interpolating from previously seen interactions. The resulting potentials transfer effectively to unseen, higher body-order alloys systems, requiring only unary and binary training data to capture ternary and quaternary systems. The model also transfers well to new elements via an alchemical extrapolation within the network, requiring only unary data for the new element and its alloys. These findings suggest that MLIAPs trained on targeted, diversity-driven datasets provide transferability at a relatively low computational cost, offering a practical path toward general-purpose, resource-efficient MLIAPs for materials modeling.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 6. PLUMED-JAX: GPU-native enhanced sampling for atomistic simulations

- Source: arXiv
- Date: 2026-10-31T00:15:58Z
- Venue: physics.chem-ph
- Authors: Venkat Kapil
- Link: https://arxiv.org/abs/2611.00483v1
- Score: 8.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 我们介绍了PLUMED-JAX ，这是一种基于JAX的原子模拟的羽状集体变量、伞形采样和元动力学的人工智能辅助适应，使用gpt-6.1-sol开发，在Codex线束中推理工作量设置为高。与JAX-MD的集成支持编译的分子动力学、批量副本、共享偏差的助行器和跨多个图形处理单元的执行。 我们根据羽状和精确的自由能基准验证了框架，并演示了丁烷、硅结晶和锂输运的应用，使经典力场和机器学习原子间势的计算吞吐量提高了四倍。
**讨论重点：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. Retention-constrained fine-tuning of a pre-trained aluminium MACE potential for non-equilibrium defect dynamics and plasticity

- Source: arXiv
- Date: 2026-10-26T16:00:16Z
- Venue: cond-mat.mtrl-sci
- Authors: Yue Wu, Yuan Tian, Deng Pan, Mingwei Chen
- Link: https://arxiv.org/abs/2610.35653v1
- Score: 8.0
- Match: 标题匹配 MACE potential; 近两周发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注MACE 势函数相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 8. A thermodynamic correction layer for machine learning interatomic potentials

- Source: arXiv
- Date: 2026-10-25T20:26:05Z
- Venue: cond-mat.mtrl-sci
- Authors: Sarath Menon, Braulio Sanchez Ortega, Ralf Drautz
- Link: https://arxiv.org/abs/2610.34551v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Machine learning interatomic potentials enable atomistic simulations with near \textit{ab initio} accuracy over large length and time scales. Foundation models extend this capability across the periodic table but inherit the thermodynamic description of the electronic structure methods used to generate their training data. Small errors in relative phase stability can therefore produce large errors in transformation temperatures. We introduce an additive thermodynamic correction layer that shifts phase free energies towards an assessed reference without retraining or modifying the base potential. A first order thermodynamic construction converts the required phase free energy shifts directly into configuration energy targets, which are fitted using a linear atomic cluster expansion and refined iteratively from measured free energies. We apply the method to melting and solid to solid transformations across elements with different crystal structures using a foundation GRACE model. After the correction, all transformation temperatures lie within the prescribed tolerance of the assessed values, including Ca, Ti, and Zr, where a solid to solid transition and melting are corrected together. Static energy curves, bulk moduli, and liquid structure remain close to those of the base model. Vacancy formation energies, thermal expansion, and liquid density depend on the corrected phase balance and change where the correction is large. The method requires neither retraining, differentiable dynamics, nor access to the parameters of the base potential. It provides a modular route for combining transferable atomistic models with assessed phase thermodynamics.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 9. Scalable long-range machine learning interatomic potentials with electrical response for atomistic material modeling

- Source: arXiv
- Date: 2026-10-16T15:44:07Z
- Venue: cond-mat.mtrl-sci, cs.LG
- Authors: Yicheng Chen, Xiaoyun Yu, Hyejeong Song, Xintian Wang, Zihui Li, Zixi Xia
- Link: https://arxiv.org/abs/2610.23643v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 10. From Algebraic Completeness to Orbit Separation: Recursive Separating Invariants for Global Neural Network Potential Energy Surfaces

- Source: arXiv
- Date: 2026-10-15T11:20:02Z
- Venue: physics.chem-ph
- Authors: Yiping Hao, Jing Lou, Bina Fu, Dong H. Zhang
- Link: https://arxiv.org/abs/2610.21700v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Majorana corner modes and tunable braiding in an altermagnet-superconductor heterostructure

- Source: arXiv
- Date: 2026-11-05T08:28:17Z
- Venue: cond-mat.supr-con, quant-ph
- Authors: Yingli Gao, Kai Zhang, Ling-Zheng Meng, Junpeng Hou, Ning Li, Ya-Jie Wu
- Link: https://arxiv.org/abs/2611.07645v1
- Score: 24.0
- Match: 摘要匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Non-Perturbative Resolution of Luttinger's Theorem Violations in Strongly Correlated Systems

- Source: arXiv
- Date: 2026-11-05T12:37:27Z
- Venue: cond-mat.str-el
- Authors: Nazzareno Africani, Herbert Eßl, Alessandro Toschi, Michele Fabrizio
- Link: https://arxiv.org/abs/2611.07933v1
- Score: 18.0
- Match: 标题匹配 strongly correlated systems; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Many-body physics faces an apparent paradox concerning violations of Luttinger's theorem in strongly correlated systems. The theorem relates the electron number to the Luttinger count -- the monodromy of the logarithm of the imaginary-frequency Green's function $G(iε)$ -- and, at finite magnetic field, connects the Hall conductivity to the magnetic-field derivative of the Luttinger count via the Streda formula. Here, we provide a non-perturbative solution to this paradox. We demonstrate that the reported violations of Luttinger's theorem do not require a breakdown of the skeleton diagram representation of physical quantities, thereby resolving a long-standing point of contention in many-body theory. Furthermore, we show that the Luttinger integral, which accounts for the mismatch between the particle number and the Luttinger count, is itself a genuine topological invariant directly tied to the Luttinger-Ward functional $Φ[G]$ rather than to the Green's function alone. We demonstrate that this invariant, like the monodromy of $\ln G(iε)$ itself, stems exclusively from the zero-frequency discontinuity of the Matsubara trajectory.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注强关联体系相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 3. Continuum Photonic Axion Insulators

- Source: arXiv
- Date: 2026-11-05T12:13:05Z
- Venue: physics.optics, cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Mario G. Silveirinha
- Link: https://arxiv.org/abs/2611.07893v1
- Score: 17.0
- Match: 摘要匹配 magnetoelectric coupling; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注磁电耦合、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Single-shot ground-state preparation via strongly coupled baths

- Source: arXiv
- Date: 2026-11-04T19:00:05Z
- Venue: quant-ph, cond-mat.str-el
- Authors: Liang-Hong Mo, Jerome Lloyd, Yuxuan Zhang, Dmitry A. Abanin, Biao Lian
- Link: https://arxiv.org/abs/2611.07021v1
- Score: 16.0
- Match: 摘要匹配 Hubbard model; 摘要匹配 quantum many-body; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Preparing ground and thermal states of quantum many-body systems is a central task in quantum simulation. Dissipative protocols have emerged as a promising solution for both near-term and fault-tolerant hardware, but most constructions rely on weak system-bath coupling, leading to slow cooling. Here, we construct cooling protocols at strong system-bath coupling, and demonstrate accurate state preparation within even a single cooling cycle. Our protocols combine dynamically ramped ancilla energy levels with time-dependent couplings to optimize the trade-off between cooling error and physical time. For a general class of free-fermion systems, we reduce the dynamics exactly to a two-level scattering problem: ground-state cooling becomes a control problem of maximizing resonant excitation transfer while suppressing non-adiabatic heating. We then construct a family of ``Möbius-Ingham'' protocols, which reach optimal error scaling for gapless spectra and almost-exponential suppression of the leading heating error for gapped spectra, as a function of the cycle period. In our free-fermion benchmarks, Möbius-Ingham cooling lies on the Pareto frontier between steady-state error and cooling time among the controls tested. We further demonstrate its effectiveness in interacting Ising and $t$-$V$ chains and the two-dimensional Fermi-Hubbard model. Finally, we extend our construction to Gibbs state preparation, showing how free-fermion thermal states can be prepared in a single cycle.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注Hubbard 模型、量子多体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 5. Variational Monte Carlo Study of Superconductivity in a Correlated System with Broken Inversion Symmetry

- Source: arXiv
- Date: 2026-11-04T05:00:56Z
- Venue: cond-mat.supr-con
- Authors: Tsuyoshi Imazu, Katsunori Kubo
- Link: https://arxiv.org/abs/2611.05964v1
- Score: 16.0
- Match: 摘要匹配 Hubbard model; 摘要匹配 unconventional superconductivity; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注Hubbard 模型、非常规超导相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 6. Interplay between Spin Stripes and Pairing Crossover in the Bilayer Hubbard Model

- Source: arXiv
- Date: 2026-11-04T02:27:52Z
- Venue: cond-mat.str-el
- Authors: Zixuan Jia, Xuelei Sui, Shijie Hu, Tianxing Ma, Haiqing Lin, Bing Huang
- Link: https://arxiv.org/abs/2611.05840v1
- Score: 16.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Whether $d$-wave or $s_\pm$-wave pairing prevails in the bilayer nickelate \ce{La3Ni2O7} remains unresolved, and how its observed spin order and magnetic excitations relate to the pairing mechanism is unclear. Here, we use finite-temperature determinant quantum Monte Carlo simulations of a minimal bilayer Hubbard model to investigate pairing competition at strong interlayer coupling, where intralayer and interlayer antiferromagnetic correlations have comparable strengths. We find that spin stripes develop spontaneously with increasing hole doping, accompanied by a crossover of the dominant pairing symmetry from $d$-wave to $s_\pm$-wave. The crossover tracks the changing relative strengths of the spin correlations, with the interlayer correlations overtaking their intralayer counterparts in magnitude. Concomitantly, the dynamical spin structure factor exhibits a momentum-dependent reorganization of the magnetic excitations, consistent with fluctuating spin stripes. Our results identify the structure of spin fluctuations as a key link between spin stripes and pairing competition, offering a minimal-model perspective for understanding \ce{La3Ni2O7}.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 7. Ferroelectricity and Peierls transition in MOI$_2$ (M=Ta, Nb): a first-principle analysis

- Source: arXiv
- Date: 2026-11-04T02:24:50Z
- Venue: cond-mat.mtrl-sci
- Authors: Carmel Dansou, Charles Paillard, Laurent Bellaiche
- Link: https://arxiv.org/abs/2611.05836v1
- Score: 16.0
- Match: 标题匹配 ferroelectricity; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：The van der Waals ferroelectric NbOI$_2$ hosts a polar distortion that is commonly attributed to the Peierls dimerization of its Nb chains. Here we show, using first-principles calculations and a Landau-type energy, that the polar instability is in fact a distinct order parameter that does not stem from the Peierls mode condensation and that three main distinct modes are important in the whole MOI$_2$ family. They are a polar mode $P$, an antipolar mode $η$, and a Peierls mode $δ$, whose stabilities and couplings strongly depend on the nature of the $M$ metal element, as evidenced by the fact that the isostructural, TaOI$_2$ system is not polar while possessing Peirls distortions.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注铁电性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 8. Dualities in one-dimensional quantum lattice models: Lie groups, Schur-Weyl duality and symmetry breaking

- Source: arXiv
- Date: 2026-11-05T16:55:32Z
- Venue: quant-ph, cond-mat.str-el, math-ph
- Authors: Dante Bosgoed, Frank Verstraete, Laurens Lootens
- Link: https://arxiv.org/abs/2611.08293v1
- Score: 14.0
- Match: 摘要匹配 tensor network; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：We present a systematic framework for gauging continuous symmetries, and show that the Schur-Weyl duality arises naturally as a realization of this construction with open boundary conditions. Restricting to compact Lie group symmetries, we construct dual models for one-dimensional quantum lattice models exhibiting those symmetries. We demonstrate that matrix product operators enable the explicit construction of intertwiners between the dual theories and their (non-invertible) symmetries. With closed boundary conditions, we can relate the full spectrum of these dual theories by considering all possible twisted boundary conditions.We illustrate how the Peter-Weyl transform appears when the duality acts on the boundary Hilbert space of a $G$-symmetric model. The presented framework generalizes previous work on dualities for unitary fusion category symmetric models. It exemplifies how dualities for both finite and continuous symmetries rely on the relation between a bond algebra and a representation of the symmetry in the lattice as double centralizers. We argue that dual non-invertible spontaneous symmetry breaking is the mechanism that underlies symmetric tensor network algorithms. We illustrate these results for $U(1)$- and $SU(2)$-symmetric quantum lattice models.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注张量网络相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 9. Microscopic Origin and Josephson Signatures of $d$-Wave Superconductivity in Monolayer FeSe

- Source: arXiv
- Date: 2026-11-05T13:54:03Z
- Venue: cond-mat.supr-con, cond-mat.mtrl-sci, cond-mat.str-el
- Authors: Jiong Mei, Lili Wang, Yu-Jie Sun, Kun Jiang
- Link: https://arxiv.org/abs/2611.08037v1
- Score: 14.0
- Match: 摘要匹配 high-temperature superconductivity; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Monolayer FeSe on SrTiO$_3$ exhibits high-temperature superconductivity with an electron-only Fermi surface, raising fundamental questions about its unconventional pairing mechanism. Motivated by recent Josephson scanning tunneling microscopy evidence for nodeless $d$-wave superconductivity, we investigate the microscopic role of the Fe $d_{xy}$ orbital using an experimentally constrained multiorbital theory. A tight-binding model fitted to quasiparticle interference and angle-resolved photoemission spectroscopy reveals substantial $d_{xy}$ character near the Fermi level and dominant nearest-neighbor hopping, in contrast to the conventional kinetic-frustration picture of iron-based superconductors. Both itinerant spin-fluctuation calculations and strong-coupling exchange approaches favor a robust $d$-wave pairing state, whose interband pairing components allow a fully gapped quasiparticle spectrum. We further establish a symmetry-based selection rule for spatial Josephson tunneling, revealing characteristic bond-centered maxima and mirror-enforced interference zeros that distinguish $d$-wave pairing from competing $s$-wave states. These symmetry-enforced nodal lines survive near Fe-site impurities, while a pronounced contrast between the $d$- and $s$-wave Josephson patterns persists around vortices despite the loss of mirror protection. Our results connect the unconventional $d_{xy}$ electronic structure to nodeless $d$-wave superconductivity and demonstrate the power of spatial Josephson interference for resolving pairing symmetry in multiorbital superconductors.
**讨论重点：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 结合关键词看，阅读时应重点关注高温超导相关的样品制备、实验表征条件、关键观测信号，以及这些信号如何支撑物理机制解释。

### 10. Observable-Based Learning of Effective Entanglement Hamiltonians

- Source: arXiv
- Date: 2026-11-05T02:43:38Z
- Venue: cond-mat.str-el, cond-mat.stat-mech, quant-ph
- Authors: Siyi Yang, Yuzhi Liu, Yi-Ming Ding, Zheng Yan
- Link: https://arxiv.org/abs/2611.07353v1
- Score: 13.0
- Match: 摘要匹配 quantum many-body; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Determining the entanglement Hamiltonian (EH) of an interacting quantum many-body system remains a fundamental challenge beyond special analytically tractable cases. Here we develop an observable-matching framework for learning effective EHs, which we demonstrate using response estimates from quantum Monte Carlo. As applications of this framework, we first calibrate the overall prefactor of the lattice Bisognano--Wichmann (LBW) construction using equal-time correlations and then learn spatially resolved couplings beyond its prescribed profile, without assuming a specific functional form for their spatial dependence. Trained solely on local correlations, the learned EHs reproduce benchmarked von Neumann and second Rényi entropies in $1$D and second Rényi entropies in $2$D. For a strong-bond cut associated with special surface criticality at the $(2+1)$D $O(3)$ Wilson--Fisher critical point, free-form learning outperforms the calibrated LBW ansatz in predicting the second Rényi entropy and reveals spatially nonuniform coupling renormalizations. Importantly, the learned EH also provides access to the von Neumann entropy in this setting, revealing a negative subleading correction and extending previous Rényi entropy findings to the von Neumann case. Directly evaluating the von Neumann entropy in such $(2+1)$D interacting quantum many-body systems remains challenging for conventional numerical methods. These results establish observable-based learning as a route to constructing effective entanglement Hamiltonians beyond prescribed spatial profiles in higher-dimensional interacting systems.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注量子多体相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。
