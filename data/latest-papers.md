# Latest papers for 程旭丽

Updated: 2026-08-23T01:04:17.726873+00:00
Window: last 14 days

## Notes

- arXiv query failed for 凝聚态物理强关联体系和多铁性质: HTTP Error 429: Too Many Requests
- 凝聚态物理强关联体系和多铁性质 returned 1 papers; target range is 5-10.

## 机器学习分子动力学模拟与热力学性质

### 1. Unlocking Multi-Component Bulk-Materials Molecular Dynamics with a Small-Footprint Machine Learning Interatomic Potential

- Source: arXiv
- Date: 2026-08-17T09:32:51Z
- Venue: physics.comp-ph
- Authors: Yucheng Ouyang, Xin Chen, Ying Liu, Lifang Wang, Xingyu Gao, Xiawei Du
- Link: https://arxiv.org/abs/2608.16329v1
- Score: 13.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 与纳米材料相反，散装材料需要在大空间尺度（约10 ^ 9个或更多原子）上进行分子动力学（ MD ）模拟，以充分捕捉其原子尺度的物理特性。以前，机器学习原子间势（ MLIP ）的引入已经将MD扩展到这个规模，但即使是单组件批量系统也需要高端超级计算机上的数万个GPU。 QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS
**讨论重点：** 与纳米材料相反，散装材料需要在大空间尺度（约10 ^ 9个或更多原子）上进行分子动力学（ MD ）模拟，以充分捕捉其原子尺度的物理特性。以前，机器学习原子间势（ MLIP ）的引入已经将MD扩展到这个规模，但即使是单组件批量系统也需要高端超级计算机上的数万个GPU。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 2. ChemReporter: A Framework for Curating and Exporting Large-Scale Chemical Datasets for MLIP Training

- Source: arXiv
- Date: 2026-08-17T11:15:35Z
- Venue: physics.chem-ph, physics.atom-ph
- Authors: Marie Bluntzer, Jules Tilly, Christoph Brunken
- Link: https://arxiv.org/abs/2608.16418v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 训练集的质量和多样性是机器学习原子间势（ MLIP ）可靠性的关键决定因素，但完全使用海量数据集通常是不切实际和多余的，因此智能数据选择至关重要。然而，一个主要瓶颈是缺乏统一访问、策划和子采样异构大规模化学数据集的基础设施，这些数据集在结构、元数据和文件格式方面存在很大差异。 我们通过ChemReporter来解决这一差距， ChemReporter是一个模块化的、与方法无关的框架，可将任意分子和材料数据集转换为统一的可查询表示，并将结果直接导出到MLIP就绪的训练数据中。 ChemReporter分为三个解耦阶段：处理，将原始数据集解析为富含结构、物理和化学元数据的分区Apache Parquet存储库；查询，通过CLI或Python API使用任意选择标准过滤和采样此存储库，从简单的物理约束到自定义、用户定义的策略；导出，将所选子集流式传输到HDF5文件中，以便在现代MLIP培训框架中直接使用。 在整个过程中，每个导出的数据点都可以追溯到其原始源条目，并且可以在相同的配置和查询数据库版本下可靠地再现数据集导出。由于数据以可查询的磁盘备份格式存储，因此ChemReporter可以处理远大于可用内存的数据集，使其能够在标准计算基础设施上扩展到十亿结构的数据集。ChemReporter在GitHub和PyPI上以Apache许可证2.0提供。
**讨论重点：** 我们通过ChemReporter来解决这一差距， ChemReporter是一个模块化的、与方法无关的框架，可将任意分子和材料数据集转换为统一的可查询表示，并将结果直接导出到MLIP就绪的训练数据中。然而，一个主要瓶颈是缺乏统一访问、策划和子采样异构大规模化学数据集的基础设施，这些数据集在结构、元数据和文件格式方面存在很大差异。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 3. Cross-Geometry Transferability Assessment of Universal Machine Learning Interatomic Potentials: From Bulk Materials to Atomic Nanowires

- Source: arXiv
- Date: 2026-08-07T00:15:49Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.comp-ph
- Authors: Pedro H. M. Zanineli, Bruno Focassio, Gabriel R. Schleder
- Link: https://arxiv.org/abs/2608.06662v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 4. Ultrafast Nonthermal Lattice Destabilization and Suppression of Polar Optical Scattering in Electronically Excited $α$-SiO$_2$ from First-Principles and Deep Neural Network Potential Modeling

- Source: arXiv
- Date: 2026-07-30T21:04:07Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Iyyappa Rajan Panneerselvam, Mark Yeung, Charlotte Palmer, Brendan Dromey, Lorenzo Stella
- Link: https://arxiv.org/abs/2607.28838v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：We present a multiscale first-principles-to-machine-learning approach to investigate ultrafast lattice dynamics in electronically excited $α$-SiO$_2$. Ab initio molecular dynamics (AIMD) based on electronic-temperature-dependent density functional theory (DFT) are used to train electronic-temperature-dependent deep neural network potentials (DNNPs). The use of DNNPs enables atomistic modeling at near-DFT accuracy of large $α$-SiO$_2$ cells with thousands of atoms. In particular, DNNPs allowed us to obtain accurate phonon band structures and molecular dynamics (MD) of $α$-SiO$_2$ excited by a sudden increase in electronic temperature. With increasing electronic temperature, $T_e$, pronounced lattice destabilization of $α$-SiO$_2$ is found, as evidenced by violations of elastic stability criteria, substantial volumetric expansion, a sharp reduction of the bulk modulus, and progressive weakening of Si-O bonding due to antibonding-state occupation. From the electronic and phonon band structures, we estimated the Frohlich coupling constant, which decreases as $T_e$ increases, suggesting a crossover to a nonpolar phase of $α$-SiO$_2$ at elevated electronic temperature. This is corroborated by the Bader charge analysis. We also suggest that polar optical phonon scattering should be strongly suppressed at $T_e > 2$ eV. From large-cell DNNP-MD simulations, we show that a well-defined thermal equilibrium, as defined by the Maxwell-Boltzmann distribution, is not achieved over the first few hundred femtoseconds. This behavior explains the non-monotonic equilibration of the kinetic temperature after a sudden rise of $T_e$. After $T_e$ is raised to 2.6 eV, Si and O atoms first equilibrate separately at two different temperatures, suggesting an atomic fluid phase, in...
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 5. PASS: Perturbation augmented space group structure sampling for transferable Fe-O machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-30T10:48:01Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Zixiong Wei, Fei Shuang, Poulumi Dey
- Link: https://arxiv.org/abs/2607.28000v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 6. Extracting Atomic Environments for Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-28T17:28:41Z
- Venue: cond-mat.mtrl-sci
- Authors: Jared C. Stimac, Fei Zhou, Kyle Bushick, Bo Lei, Sebastien Hamel, Amit Samanta
- Link: https://arxiv.org/abs/2607.26018v2
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：In order to appropriately capture large-scale material features and emergent phenomena via atomistic simulations, such as Molecular Dynamics (MD), the system scale can range up to hundreds of millions of atoms. However, the force-field models that drive those simulations are generally trained with Density Functional Theory (DFT) reference data, limited to relatively small configurations on the order of 100s or 1000s of atoms. To compute DFT forces on atoms in regions of interest, for example for active-learning or on-the-fly training of interatomic potentials, one needs to extract a small set of atoms from the larger simulation box, and typically work with periodic boundary conditions for DFT. However, methods to select the shape and size of this extracted set of atoms, as well as to generate a potentially necessary passivating envelope, have not been systematically analyzed. In this work, we benchmark several techniques, including a generative diffusion-based artificial intelligence (AI) approach, for extracting atomic environments from large, bulk configurations and embedding them into smaller configurations suitable for DFT calculations with periodic boundary conditions. We test with a diverse set of material systems, which includes amorphous $\mathrm{SiO_2}$, Ta with screw dislocations, and molten C. We demonstrated a notably simple procedure, a method we refer to as deletions, yields superior performance over an array of alternative extraction methods.
**讨论重点：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. Charge-Density-Wave Phase Transitions in Monolayer 1T-TaS2 from Universal Machine Learning Molecular Dynamics

- Source: arXiv
- Date: 2026-07-24T13:57:09Z
- Venue: cond-mat.mtrl-sci
- Authors: Valentina Nesterova, Tribhuwan Pandey, Tom Berlijn, Fariborz Kargar, Lucas Lindsay, Konstantin Klyukin
- Link: https://arxiv.org/abs/2607.22316v1
- Score: 8.0
- Match: 标题匹配 machine learning molecular dynamics

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Charge-density-wave (CDW) phases in 1T transition-metal dichalcogenides arise from strong electron-phonon coupling and accompanying lattice instabilities. Capturing their temperature-dependent structural evolution using conventional first-principles molecular dynamics (MD) remains challenging because of the large supercells and extensive finite-temperature sampling required. Here, we combine density functional theory (DFT), universal machine-learning interatomic potentials (MLIPs), MD, and temperature-dependent effective potential phonon calculations to investigate the structural and vibrational signatures of CDW transitions in monolayer 1T-TaS2. Benchmarking against DFT displacement energies identifies UMA-s-1p1 universal machine learning potentials with sufficient accuracy for subsequent finite-temperature simulations. Our results show that large-scale MD simulations reproduce the experimentally observed phase transition sequence from the low-temperature Star-of-David (SoD) distorted structure to the high-temperature primitive hexagonal structure, as quantified by the number of Ta atoms attributed to SoDs. Heating-cooling cycles exhibit thermal hysteresis, and upon cooling, the system freezes into a multi-domain state in which α and \b{eta} CDW chiralities nucleate independently and persist to the lowest temperatures. These findings demonstrate that carefully benchmarked universal MLIPs can provide a scalable framework for finite-temperature studies of CDW materials.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注机器学习分子动力学相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 8. A high-dimensional neural network potential for finite-temperature phenomena in NiTi martensite

- Source: arXiv
- Date: 2026-07-22T19:32:23Z
- Venue: cond-mat.mtrl-sci
- Authors: Petr Jaroš, Petr Sedlák, Petr Šesták, Miroslav Černý, Jörg Behler, Hanuš Seiner
- Link: https://arxiv.org/abs/2607.20681v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：We present a high-dimensional neural network potential (HDNNP) for the martensitic phase of the NiTi shape-memory alloy trained to density functional theory (DFT) data. A central aspect of this work is the systematic validation of the potential with respect to the underlying DFT reference method for key properties governing structural evolution, including equilibrium crystal structures, elastic constants, generalized-stacking fault energies, and vibrational spectra. The HDNNP accurately describes the relative stability of the B19$^\prime$ and B33 phases, including subtle energy differences on the order of meV/atom. The predicted stacking-fault energy landscape is strongly anisotropic and reveals a preferential shear pathway, providing atomistic insight into deformation and twinning mechanisms. Finite-temperature molecular dynamics simulations further enable the investigation of unconstrained structural evolution as a function of temperature. Overall, the developed HDNNP provides a robust basis for atomistic simulations of the complex structural and functional behavior of martensitic NiTi systems containing hundreds of thousands of atoms on nanosecond time scales.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 9. Study of ordering in (MoCrTi)$_{100-x}$Al$_x$ refractory high-entropy alloys using machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-20T16:01:06Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn
- Authors: Jiyao Zhang, Klemens Lechner, Markus Maßwohl, Petra Spoerk-Erdely, David Holec
- Link: https://arxiv.org/abs/2607.18099v2
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Refractory high-entropy alloys are promising candidates for high-temperature applications, yet the effects of composition on their chemical-ordering pathways and mechanical properties remain insufficiently understood. Here, a universal MLIP combined with MC and MD simulations is employed to investigate the temperature-dependent thermodynamic and mechanical behavior of (MoCrTi)(100-x)Alx alloys. Atomic configurations, sublattice occupations, and simulated diffraction intensities reveal pronounced B2-type chemical ordering at low temperatures, with Mo and Al occupying one sublattice and Cr and Ti occupying the other. The configurational heat capacities and SRO parameters further reveal a strong composition dependence of the ordering pathway. The Mo25Cr25Ti25Al25 and Mo32Cr32Ti32Al4 alloys exhibit a single dominant ordering stage involving cooperative changes in multiple B2-type pair correlations. By contrast, Mo28Cr28Ti28Al16 and Mo30Cr30Ti30Al10 exhibit two distinct ordering stages. Their low-temperature features are associated primarily with changes in the Mo-Al and Al-Al correlations, respectively, whereas their high-temperature features involve collective changes in the remaining B2-type pair correlations. Chemical ordering also fundamentally alters the composition dependence of mechanical stiffness. Whereas the elastic constants of disordered configurations increase approximately monotonically with decreasing Al content, those of the ordered configurations exhibit a non-monotonic dependence and reach a maximum in Mo30Cr30Ti30Al10. This anomalous enhancement originates from a SRO induced redistribution of atomic pairs, particularly Mo-Cr pairs. These results establish a direct atomistic connection among alloy composition, multistage chemical ordering...
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 10. RuNNer 2.0: A Software Suite for High-Dimensional Neural Network Potentials

- Source: arXiv
- Date: 2026-07-20T14:13:35Z
- Venue: physics.chem-ph, cond-mat.mtrl-sci, physics.comp-ph
- Authors: Alexander L. M. Knoll, Moritz R. Schäfer, K. Nikolas Lausch, Moritz Gubler, Henry Wang, Richard Springborn
- Link: https://arxiv.org/abs/2607.17978v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：We present RuNNer 2.0, the "Ruhr University Neural Network energy representation", a highly optimized software suite for training and evaluating high-dimensional neural network potentials (HDNNPs) of the second, third, and fourth generation. Long-range electrostatics and charge equilibration (QEq) for the description of non-local charge transfer in fourth-generation (4G) HDNNPs are accelerated by quasi-linear-scaling plane-wave methods, reducing QEq computational complexity from $\mathcal{O}(N^3)$ to $\mathcal{O}(N\log^2 N)$ such that linear or quasi-linear scaling is achieved across all HDNNP generations. An optimized memory management strategy eliminates the training overhead traditionally associated with long-range interactions, allowing 4G-HDNNPs to be trained with the same efficiency as their local counterparts. Developed in modern Fortran (2003/2008 standards), combined with a hybrid MPI/OpenMP parallelization scheme, RuNNer 2.0 has been designed to run efficiently in any CPU environment, from cost-effective local workstations to massive HPC clusters. Its modular library architecture facilitates straightforward binding to external simulation software; native interfaces to LAMMPS and the Atomic Simulation Environment (ASE) provide full access to all its features, including built-in committee-based uncertainty quantification. The high efficiency and scalability of the RuNNer 2.0 ecosystem are demonstrated through detailed benchmarks.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Efficient quantum implementation of dynamical mean field theory for correlated materials

- Source: Journal
- Date: 2026-08-17
- Venue: npj Computational Materials
- Authors: Norman Hogan, Efekan Kökcü, Thomas Steckmann, Liam P. Doak, Carlos Mejuto-Zaera, Daan Camps
- Link: https://doi.org/10.1038/s41524-026-02289-2
- Score: 11.0
- Match: 标题匹配 dynamical mean field theory; 近两周发布

**中文摘要：** 当前元数据未提供原文摘要。论文题目为“Efficient quantum implementation of dynamical mean field theory for correlated materials”。
**讨论重点：** 结合关键词看，阅读时应重点关注动力学平均场理论相关的研究对象、方法假设、关键参数、数据来源，以及结果能否迁移到相邻材料或物理体系。
