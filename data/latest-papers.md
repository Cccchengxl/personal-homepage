# Latest papers for 程旭丽

Updated: 2026-08-04T10:22:12.946217+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Ultrafast Nonthermal Lattice Destabilization and Suppression of Polar Optical Scattering in Electronically Excited $α$-SiO$_2$ from First-Principles and Deep Neural Network Potential Modeling

- Source: arXiv
- Date: 2026-07-30T21:04:07Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Iyyappa Rajan Panneerselvam, Mark Yeung, Charlotte Palmer, Brendan Dromey, Lorenzo Stella
- Link: https://arxiv.org/abs/2607.28838v1
- Score: 14.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。使用 DNNP 可以对具有数千个原子的大型 $α$-SiO$_2$ 单元进行接近 DFT 精度的原子建模。 特别是，DNNP 使我们能够获得由电子温度突然升高激发的 $α$-SiO$_2$ 的精确声子能带结构和分子动力学 (MD)。随着电子温度 $T_e$ 的增加，发现 $α$-SiO$_2$ 出现明显的晶格失稳，表现为违反弹性稳定性标准、体积大幅膨胀、体积模量急剧下降以及由于反键态占据而导致 Si-O 键逐渐减弱。 根据电子和声子能带结构，我们估计了 Frohlich 耦合常数，该常数随着 $T_e$ 的增加而减小，表明在电子温度升高时会交叉到 $α$-SiO$_2$ 的非极性相。 Bader 电荷分析证实了这一点。我们还建议，在 $T_e > 2$ eV 时应强烈抑制极性光学声子散射。从大单元 DNNP-MD 模拟中，我们表明，在最初的几百飞秒内，并未实现由麦克斯韦-玻尔兹曼分布定义的明确热平衡。 这种行为解释了 $T_e$ 突然上升后动力学温度的非单调平衡。当 $T_e$ 升至 2.6 eV 后，Si 和 O 原子首先在两个不同的温度下分别达到平衡，表明存在原子流体相，这与最近的实验和理论发现一致。
**讨论重点：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 2. PASS: Perturbation augmented space group structure sampling for transferable Fe-O machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-30T10:48:01Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Zixiong Wei, Fei Shuang, Poulumi Dey
- Link: https://arxiv.org/abs/2607.28000v1
- Score: 14.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 铁（Fe）氧化的准确原子建模需要可靠的原子间势，这需要广泛且具有代表性的第一性原理数据集来训练原子间势。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。 我们提出了一种系统方法，基于原子团簇扩展 (ACE) 框架，为 Fe-O 系统开发首个可转移机器学习原子间势 (MLIP)。我们通过体积、表面和界面特性彻底验证了 ACE MLIP 在纯 Fe 和 Fe-O 系统中的准确性和功能。我们展示了使用 ACE MLIP 大规模 Fe 氧化模拟中 FeO 类结构的形成。 这项工作表明，PASS 方法产生了准确且可转移的 MLIP，它能够捕获氧化物生长的反应复杂性，同时保持扩展系统的计算实用性。
**讨论重点：** 在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 3. Extracting Atomic Environments for Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-28T17:28:41Z
- Venue: cond-mat.mtrl-sci
- Authors: Jared C. Stimac, Fei Zhou, Kyle Bushick, Bo Lei, Sebastien Hamel, Amit Samanta
- Link: https://arxiv.org/abs/2607.26018v2
- Score: 12.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 为了通过原子模拟（例如分子动力学（MD））适当捕获大规模材料特征和突发现象，系统规模可以达到数亿个原子。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 为了计算感兴趣区域中原子上的 DFT 力，例如用于原子间势的主动学习或动态训练，需要从较大的模拟框中提取一小组原子，并且通常使用 DFT 的周期性边界条件。然而，尚未系统地分析选择这组提取的原子的形状和大小以及生成潜在必要的钝化包络的方法。 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。我们使用多种材料系统进行测试，其中包括无定形 $\mathrm{SiO_2}$、具有螺旋位错的 Ta 和熔融 C。我们演示了一种非常简单的程序（我们称为删除的方法），其性能优于一系列替代提取方法。
**讨论重点：** 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 4. Charge-Density-Wave Phase Transitions in Monolayer 1T-TaS2 from Universal Machine Learning Molecular Dynamics

- Source: arXiv
- Date: 2026-07-24T13:57:09Z
- Venue: cond-mat.mtrl-sci
- Authors: Valentina Nesterova, Tribhuwan Pandey, Tom Berlijn, Fariborz Kargar, Lucas Lindsay, Konstantin Klyukin
- Link: https://arxiv.org/abs/2607.22316v1
- Score: 8.0
- Match: 标题匹配 machine learning molecular dynamics; 近两周发布

**中文摘要：** 1T 过渡金属二硫属化物中的电荷密度波 (CDW) 相是由强电子声子耦合和伴随的晶格不稳定性产生的。由于需要大型超级电池和广泛的有限温度采样，使用传统的第一原理分子动力学 (MD) 捕获其随温度变化的结构演化仍然具有挑战性。 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。针对 DFT 位移能量的基准测试确定了 UMA-s-1p1 通用机器学习潜力，具有足够的精度用于后续的有限温度模拟。 我们的结果表明，大规模 MD 模拟再现了实验观察到的从低温大卫之星 (SoD) 扭曲结构到高温原始六边形结构的相变序列，通过归因于 SoD 的 Ta 原子数量来量化。加热-冷却循环表现出热滞后，并且在冷却时，系统冻结成多域状态，其中α和\b{eta} CDW手性独立成核并持续到最低温度。 这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。
**讨论重点：** 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。 结合关键词看，阅读时应重点关注机器学习分子动力学相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 5. A high-dimensional neural network potential for finite-temperature phenomena in NiTi martensite

- Source: arXiv
- Date: 2026-07-22T19:32:23Z
- Venue: cond-mat.mtrl-sci
- Authors: Petr Jaroš, Petr Sedlák, Petr Šesták, Miroslav Černý, Jörg Behler, Hanuš Seiner
- Link: https://arxiv.org/abs/2607.20681v1
- Score: 8.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 HDNNP 准确地描述了 B19$^\prime$ 和 B33 相的相对稳定性，包括 meV/原子数量级的细微能量差异。预测的堆垛层错能量景观具有强烈的各向异性，并揭示了优先剪切路径，为变形和孪生机制提供了原子学的见解。有限温度分子动力学模拟进一步能够研究作为温度函数的无约束结构演化。 总体而言，开发的 HDNNP 为纳秒时间尺度上包含数十万个原子的马氏体 NiTi 系统的复杂结构和功能行为的原子模拟提供了坚实的基础。
**讨论重点：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 6. Study of ordering in (MoCrTi)$_{100-x}$Al$_x$ refractory high-entropy alloys using machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-20T16:01:06Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn
- Authors: Jiyao Zhang, Klemens Lechner, Markus Maßwohl, Petra Spoerk-Erdely, David Holec
- Link: https://arxiv.org/abs/2607.18099v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 耐火高熵合金由于其优异的机械性能而成为高温应用的有希望的候选者。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。在这项工作中，通过利用通用机器学习原子间势与混合蒙特卡罗和分子动力学模拟，研究了(MoCrTi)(100-x)Alx系统的温度依赖性热力学和机械性能。 热容和短程有序参数揭示了不同的有序-无序转变行为。虽然 Mo25Cr25Ti25Al25 和 Mo32Cr32Ti32Al4 合金表现出由 B2 型原子对的协同排序主导的单一转变，但 Mo28Cr28Ti28Al16 和 Mo30Cr30Ti30Al10 合金表现出两个单独的转变：由特定对驱动的低温阶段（Mo28Cr28Ti28Al16 中的 Mo-Al；Mo28Cr28Ti28Al16 中的 Al-Al） Mo30Cr30Ti30Al10) 和由其余对控制的高温阶段。 结构分析表明，在低温有序B2相中，Mo和Al共享一个亚晶格，而Cr和Ti共享另一个亚晶格。此外，还确定了排序和机械刚度之间的关系。有序显着增强了弹性常数和模量，并产生非单调的成分依赖性。与随机固溶体不同的是，随机固溶体的刚度随着 Al 含量的降低而单调增加，有序构型表现出非单调趋势，在 Mo30Cr30Ti30Al10 合金中达到峰值。 这种增强归因于强短程有序引起的刚性原子对的优化群体。这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。
**讨论重点：** 这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 7. RuNNer 2.0: A Software Suite for High-Dimensional Neural Network Potentials

- Source: arXiv
- Date: 2026-07-20T14:13:35Z
- Venue: physics.chem-ph, cond-mat.mtrl-sci, physics.comp-ph
- Authors: Alexander L. M. Knoll, Moritz R. Schäfer, K. Nikolas Lausch, Moritz Gubler, Henry Wang, Richard Springborn
- Link: https://arxiv.org/abs/2607.17978v1
- Score: 8.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局域电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。优化的内存管理策略消除了传统上与远程交互相关的训练开销，从而使 4G-HDNNP 能够以与本地对应物相同的效率进行训练。 RuNNer 2.0 采用现代 Fortran（2003/2008 标准）开发，结合​​混合 MPI/OpenMP 并行化方案，旨在在任何 CPU 环境（从经济高效的本地工作站到大规模 HPC 集群）中高效运行。其模块化库架构有助于直接绑定到外部模拟软件； LAMMPS 和原子仿真环境 (ASE) 的本机接口提供对其所有功能的完全访问，包括内置的基于委员会的不确定性量化。 RuNNer 2.0生态系统的高效率和可扩展性通过详细的基准测试得到证明。
**讨论重点：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局域电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 8. Are Machine Learning Interatomic Potentials Truly Practical? A Benchmark of 23 Mainstream Models

- Source: arXiv
- Date: 2026-07-08T17:04:42Z
- Venue: cond-mat.mtrl-sci, cs.CE, physics.comp-ph
- Authors: Hanwen Kang, Tenglong Lu, Sheng Meng, Miao Liu
- Link: https://arxiv.org/abs/2607.07647v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。我们评估三个维度：预测准确性、MD 模拟吞吐量和原子可扩展性。 我们的结果揭示了精确度与效率之间的巨大权衡：大型 SOTA 模型的精确度仅比轻量级模型高出 3-5 meV/atom，但吞吐量却损失了几个数量级——在最坏的情况下，仅比 DFT 本身快一点点。相比之下，轻量级 MLIP 位于帕累托前沿并在适度的硬件上运行。教训是，一维基准会误导该领域，未来的 MLIP 开发应该重视效率和可扩展性以及准确性。
**讨论重点：** 我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. MLIP Studio: An Open Platform for Interactive Benchmarking and Atomistic Simulations Using Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-08T16:23:57Z
- Venue: cond-mat.mtrl-sci
- Authors: Manas Sharma, Sudeep Punnathanam, Ananth Govind Rajan
- Link: https://arxiv.org/abs/2607.07606v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 通用机器学习原子间势（MLIP）是改变原子模拟的基础人工智能模型，但其实际使用仍然受到分散的软件生态系统、依赖性冲突和缺乏可用的基准测试工具的阻碍。这些模型以一小部分计算成本实现了第一原理密度泛函理论 (DFT) 的精度。我们推出了 MLIP Studio（可在 https://mlipstudio.iisc.ac.in 获取），这是一个开放且免费的平台，可将 60 多种通用 MLIP 引入分子和材料的统一交互界面中。 该平台支持端到端 MLIP 驱动的工作流程，包括属性预测、几何优化、振动和状态方程分析、自旋状态确定、自定义模型部署以及针对参考数据的高通量基准测试。自动奇偶图和可排序误差表有助于快速识别元素异常值和有问题的数据点。我们证明基于 MLIP 的预优化可以减少后续 DFT 优化工作约 33$\times$。此外，该应用程序还可以对计算性能进行基准测试。 通过涉及蓝宝石基板上的二维磁性材料 CrCl$_3$ 的综合案例研究，我们展示了各种属性和势能景观的跨模型比较如何指导特定任务的 MLIP 选择。总体而言，MLIP Studio 降低了在计算化学和材料科学的端到端研究工作流程、基准测试和教育中可靠使用基础模型的障碍。
**讨论重点：** 我们推出了 MLIP Studio（可在 https://mlipstudio.iisc.ac.in 获取），这是一个开放且免费的平台，可将 60 多种通用 MLIP 引入分子和材料的统一交互界面中。通过涉及蓝宝石基板上的二维磁性材料 CrCl$_3$ 的综合案例研究，我们展示了各种属性和势能景观的跨模型比较如何指导特定任务的 MLIP 选择。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 10. dpti: An Automated Thermodynamic Integration Workflow for Phase Diagram Calculations with Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-06T12:56:52Z
- Venue: physics.comp-ph, cond-mat.mtrl-sci
- Authors: Fengbo Yuan, Xin Zhong, Donghao Zheng, Jinzhe Zeng, Linfeng Zhang, Han Wang
- Link: https://arxiv.org/abs/2607.05015v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 热力学积分 (TI) 是一种广泛使用的计算自由能和相图的方法。然而，由机器学习原子间势 (MLIP) 驱动的 TI 计算在技术上仍然具有挑战性，因为它们需要仔细设计可逆积分路径以及每个相和状态点的许多密切相关的分子动力学 (MD) 任务。 为了应对这些挑战，我们推出了 dpti，这是一个开源 Python 软件包，可自动执行使用 MLIP 进行相图计算的 TI 工作流程。 dpti 通过可逆积分路径将具有分析已知自由能的参考系统连接到 MLIP 描述的原子和分子固体和液体。给定 JSON 输入文件，dpti 生成并运行所需的 MD 任务，计算自由能贡献，估计误差，并将共存点传播到相边界。 我们通过深势模型驱动的两个示例演示了 dpti 的用法：涉及 β-石英、柯石英和熔体的二氧化硅相图，以及冰 Ih-液态水相边界。 dpti 提供了一个有用的工具，用于自动计算 MLIP 建模的材料的相图。
**讨论重点：** 然而，由机器学习原子间势 (MLIP) 驱动的 TI 计算在技术上仍然具有挑战性，因为它们需要仔细设计可逆积分路径以及每个相和状态点的许多密切相关的分子动力学 (MD) 任务。热力学积分 (TI) 是一种广泛使用的计算自由能和相图的方法。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

## 凝聚态物理强关联体系和多铁性质

### 1. Magnetically tunable symmetry-enforced nodal lines producing huge anomalous Hall conductivity in altermagnetic $α$-MnTe

- Source: arXiv
- Date: 2026-08-03T15:55:42Z
- Venue: cond-mat.mtrl-sci, cond-mat.other
- Authors: Mathews Benny, Xujia Gong, Amar Fakhredine, Raphaël Salazar, Ashutosh S. Wadge, Juraj Krempaský
- Link: https://arxiv.org/abs/2608.02416v1
- Score: 28.0
- Match: 摘要匹配 ferromagnetism; 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁 $α$-MnTe 在室温下表现出巨大的反常霍尔电导率 (AHC)，以及自旋和轨道极化产生的弱铁磁性。我们通过识别价带中具有 Mn 特征的两组不同的对称强制节点线来澄清 AHC 大值的起源，这些节点线位于 $k_z=0$ 和 $k_z=\fracπ{c}$ 处，分别受到镜像对称 $M_z$ 和滑移对称 $G_z = \{M_z\,|\,0,0,\tfrac{c}{2}\}$ 的保护。 两条节点线均与能量相关，具有近似 C$_6$ 对称性，由于 Néel 矢量的存在，该对称性被简化为精确的 C$_2$ 对称性。最高价带表现出墨西哥帽色散，而第二高价带表现出倒置墨西哥帽色散，在两个能带之间的交叉处具有节点线。在第一原理精度范围内，我们证明这些节点线会产生实验观察到的大 AHC，并表现出与弱铁磁性的强烈相互作用。 我们进一步表明，即使是很小的自旋倾斜也会强烈改变节点线和 AHC，使它们都具有磁性可调。通过解开 AHC 中的交磁和铁磁贡献，交磁贡献在小倾斜角度下占主导地位，而铁磁贡献在较大的角度下变得相当大。利用角度分辨光电子光谱中的线性二色性，我们显示了布里渊区边界处的节点线的特征。
**讨论重点：** 交变磁 $α$-MnTe 在室温下表现出巨大的反常霍尔电导率 (AHC)，以及自旋和轨道极化产生的弱铁磁性。我们通过识别价带中具有 Mn 特征的两组不同的对称强制节点线来澄清 AHC 大值的起源，这些节点线位于 $k_z=0$ 和 $k_z=\fracπ{c}$ 处，分别受到镜像对称 $M_z$ 和滑移对称 $G_z = \{M_z\,|\,0,0,\tfrac{c}{2}\}$ 的保护。 结合关键词看，阅读时应重点关注铁磁性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Study of the Anomalous Hall effect by tuning the spin orientation in the Altermagnetic material CrSb

- Source: arXiv
- Date: 2026-07-31T17:23:31Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: Sreedevi Chintalapudi, Upasana Agrawal, Suvadip Das
- Link: https://arxiv.org/abs/2607.29646v1
- Score: 25.0
- Match: 摘要匹配 altermagnetism; 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁性领域的最新发展以及对反常霍尔效应应用的需求不断增加，开创了材料中新型量子相的新时代。以前预计可以科学预测的量子材料已经展现出新颖的特性，使它们成为人们关注的焦点。这些表现使我们根据物质的拓扑非平凡相重新思考对磁性材料现有分类的理解以及关于反常霍尔效应的现有概念。 最近的一项进展在于具有量子计算前景的新型变磁材料。在本文中，我们描述了自旋和轨道分辨电子谱、模式分解声子色散关系、几何浆果曲率和拓扑表面态及其对有前景的互磁化合物 CrSb 中反常霍尔电导率的影响。 我们进一步利用第一性原理计算，结合交流磁体众多磁性配置的计算效率最大局部万尼尔态来模拟外部场的影响，并阐明反常霍尔电导率与磁化强度的线性行为并不一定适用于所有磁性类别（例如交流磁体）。
**讨论重点：** 交变磁性领域的最新发展以及对反常霍尔效应应用的需求不断增加，开创了材料中新型量子相的新时代。以前预计可以科学预测的量子材料已经展现出新颖的特性，使它们成为人们关注的焦点。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Twist-induced magnetic topological phase transition in stacked altermagnetic CrO

- Source: arXiv
- Date: 2026-08-02T13:42:16Z
- Venue: cond-mat.mtrl-sci
- Authors: Zi-Hao Ding, Ze-Feng Gao, Xiang-Hua Kong, Peng-Jie Guo, Zhong-Yi Lu
- Link: https://arxiv.org/abs/2608.01235v1
- Score: 24.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 层间扭曲提供了控制电子状态的几何途径，但它是否可以同时重建磁对称性和能带拓扑仍不清楚。在这里，基于对称性分析和第一性原理计算，我们表明相应的扭曲驱动堆叠双层 CrO 中的磁拓扑相变。特别是，它将反铁磁狄拉克半金属转变为 $d$ 波交磁双极化韦尔半金属或非常规补偿磁性韦尔半金属。 一个关键结果是 $d$ 波交磁相中的 Weyl 点位于布里渊区中的通用 $k$ 点，并受到自旋对称性 $\left\{ C_2 T||C_{2z} T\right\}$ 的保护。这与传统的二维韦尔半金属形成鲜明对比，在传统的二维韦尔半金属中，韦尔点通常受到镜像或旋转对称性的保护，因此固定在高对称线上。我们进一步证明，相应的扭曲保留了自旋对称性$\left\{ C_2 T||C_{2z} T\right\}$，使得Weyl相成为扭曲的鲁棒结果，而不是特定角度的微调特征。 我们的工作建立了一种基于对称的途径来设计扭曲二维材料中的磁拓扑相。
**讨论重点：** 层间扭曲提供了控制电子状态的几何途径，但它是否可以同时重建磁对称性和能带拓扑仍不清楚。在这里，基于对称性分析和第一性原理计算，我们表明相应的扭曲驱动堆叠双层 CrO 中的磁拓扑相变。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Band topology and symmetry-driven magneto-optical response in two-dimensional d-wave altermagnets with staggered spin-orbit coupling

- Source: arXiv
- Date: 2026-08-03T12:36:30Z
- Venue: cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Meysam Bagheri Tagani Carmine Autieri, Wojciech Brzezicki
- Link: https://arxiv.org/abs/2608.02155v1
- Score: 21.0
- Match: 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁体将补偿共线磁序与动量相关的自旋分裂相结合，提供了一种在没有净铁磁矩的情况下横向电子和光学响应的​​途径。我们为二维 d 波交替磁体开发了严格周期性的四能带紧束缚模型，并区分了三个自旋轨道耦合 (SOC) 通道的作用：均匀 Rashba SOC、亚晶格交错 Rashba 相互作用和键交错 SOC。 在没有 SOC 的情况下，d 波动力学各向异性在正交布里渊区边界上产生自旋极化狄拉克点，与交磁四重自旋群对称性相关。均匀 Rashba SOC 混合自旋扇区并移动这些节点，但保留了禁止集成霍尔响应的反酉对称性。亚晶格交错的 Rashba 项打破了这种对称性并激活横向光学响应，而键交错的 SOC 提供了使边界节点间隙的质量。 它们的组合作用会产生强烈的贝里曲率热点，并在狭窄的参数窗口内产生陈数 C=-2 的孤立的下两带流形。对于这里考虑的代表性参数，可以稳定陈绝缘体相。使用协变速度 Kubo 计算，我们表明大光学霍尔电导率和圆二色性远远超出非零陈区域，并受到 SOC 引起的避免交叉和对称性破缺的控制。 我们进一步发现，载流子掺杂通过泡利阻塞和贝里曲率热点的占据强烈改变了谐振和直流霍尔响应，从而实现了栅极控制的符号反转。这些结果确定了不同界面 SOC 机制在补偿二维磁体中产生拓扑和可调谐磁光活动方面的互补作用。
**讨论重点：** 我们为二维 d 波交替磁体开发了严格周期性的四能带紧束缚模型，并区分了三个自旋轨道耦合 (SOC) 通道的作用：均匀 Rashba SOC、亚晶格交错 Rashba 相互作用和键交错 SOC。在没有 SOC 的情况下，d 波动力学各向异性在正交布里渊区边界上产生自旋极化狄拉克点，与交磁四重自旋群对称性相关。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 5. Transient Ferromagnetism in Ultrafast Phase Transitions in Perovskites under XUV Irradiation: A Comparative Study of SrTiO3 and KTaO3

- Source: arXiv
- Date: 2026-08-03T12:06:28Z
- Venue: cond-mat.mtrl-sci
- Authors: Aldo Artimez Pena, Nikita Medvedev
- Link: https://arxiv.org/abs/2608.02106v1
- Score: 18.0
- Match: 标题匹配 ferromagnetism; 最近 3 天发布

**中文摘要：** 我们使用 XTANT3 多尺度代码研究钛酸锶和钽酸钾对强飞秒辐照的超快结构和电子响应。研究发现，在 STO 中的阈值剂量为 0.7 eVatom 和 KTO 中的阈值剂量为 0.9 eVatom 时，超离子态会随着氧子系统的选择性熔化而热形成，同时金属亚晶格仍保持有序。这种状态持续到 1.6 eVatom STO 和 1.5 eVatom KTO，超过此值就会发生完全紊乱。 对瞬态电子密度的分析表明，B位d轨道控制着两种材料的发散行为：STO中紧凑的Ti 3d轨道产生窄导带和大原子内交换参数，在1 ps时间尺度上驱动瞬态铁磁不稳定性，而KTO中更空间扩展的Ta 5d轨道产生更宽的导带和更小的交换参数，保持KTO顺磁性。 这些结果表明d轨道空间范围作为影响相变序列和极端电子激发下磁响应的结构参数，对基于钙钛矿的光电器件中电子和磁特性的超快光学控制具有影响。 Landau Devonshire 分析表明，0.3 eVatom 的辐照瞬时加深了无应变和应变 STO 和 KTO 中的极性势阱，相对于无应变情况，在应变 STO 中该效应放大了约 2 倍，在应变 KTO 中放大了 6 倍。
**讨论重点：** 我们使用 XTANT3 多尺度代码研究钛酸锶和钽酸钾对强飞秒辐照的超快结构和电子响应。研究发现，在 STO 中的阈值剂量为 0.7 eVatom 和 KTO 中的阈值剂量为 0.9 eVatom 时，超离子态会随着氧子系统的选择性熔化而热形成，同时金属亚晶格仍保持有序。 结合关键词看，阅读时应重点关注铁磁性相关的研究对象、方法假设、关键参数、数据来源，以及结果能否迁移到相邻材料或物理体系。

### 6. Second-Harmonic Imaging of Magnetic Domains in Thin Film Hematite

- Source: arXiv
- Date: 2026-08-03T14:07:20Z
- Venue: cond-mat.mtrl-sci
- Authors: Holger Mirkes, Johannes Schmuck, Katharina Müller, János Papp, Paul Seifert, Matthias Althammer
- Link: https://arxiv.org/abs/2608.02263v1
- Score: 17.0
- Match: 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 赤铁矿是一种反铁磁氧化物和候选交磁绝缘体，其尼尔阶在莫林转变处从易轴重新定向到易平面相。解释交磁输运和对称敏感光学响应需要了解相对于晶轴的尼尔矢量方向以及被探测器件内的磁畴结构。在这里，我们展示了偏振分辨二次谐波发生（SHG）显微镜可以解析外延（0001）取向赤铁矿薄膜中的磁对称性和磁畴。 在整个莫林温度范围内，SHG 偏振各向异性从与易轴方向一致的大约六重模式演变为与易平面方向一致的明显双重模式。基于磁偶极子和电四极子贡献的对称性分析再现了这种演变。重要的是，在磁序反转的情况下，奇数和偶数倍频振幅之间的干涉使得相反的尼尔矢量方向在光学上可区分。 一致地，在我们的实验中，所施加的面内磁场的相反方向会产生不同的倍频响应。利用这种磁性对比，我们对微米级磁域、它们在莫林转变期间的重组以及它们在磁和热循环下的重新配置进行成像，包括通过自旋翻转转变循环后的剩余变化。这些结果确立了倍频显微镜作为赤铁矿薄膜中磁对称性、尼尔矢量取向和磁畴演化的局部探针。
**讨论重点：** 赤铁矿是一种反铁磁氧化物和候选交磁绝缘体，其尼尔阶在莫林转变处从易轴重新定向到易平面相。解释交磁输运和对称敏感光学响应需要了解相对于晶轴的尼尔矢量方向以及被探测器件内的磁畴结构。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 7. Emergent modular Luttinger liquid from spin-partitioned entanglement in the one-dimensional Hubbard model

- Source: arXiv
- Date: 2026-08-03T07:26:51Z
- Venue: cond-mat.str-el, cond-mat.quant-gas
- Authors: Ádám Bácsi, Catalin Pascu Moca, Balázs Dóra
- Link: https://arxiv.org/abs/2608.01817v1
- Score: 17.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 我们研究一维排斥哈伯德模型的自旋分配纠缠哈密顿量。通过将玻色子化与精确对角化相结合，我们证明追踪一个自旋物种会产生一种模块化的卢廷格液体，其性质与物理系统的性质根本不同。虽然模谱是完全无色散的并且具有与动量无关的纠缠间隙，但其本征态表现出由单个有效卢廷格参数控制的代数相关性，该有效卢廷格参数等于电荷和自旋卢廷格参数的几何平均值。 由此产生的纠缠谱显示出通用的分支层次结构，与精确的对角化非常一致。我们进一步证明，模块化基态与无旋转的卢廷格液体几乎相同。这些结果揭示了相互作用的一维费米子系统中的通用模块化结构。
**讨论重点：** 我们研究一维排斥哈伯德模型的自旋分配纠缠哈密顿量。通过将玻色子化与精确对角化相结合，我们证明追踪一个自旋物种会产生一种模块化的卢廷格液体，其性质与物理系统的性质根本不同。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 8. Electron-like high-temperature superconductivity induced by compressive strain in La2PrNi2O7 thin films

- Source: arXiv
- Date: 2026-08-02T15:05:34Z
- Venue: cond-mat.supr-con, cond-mat.mtrl-sci, cond-mat.str-el
- Authors: Zhiwei Wang, Zhengjie Wang, Huiyu Wang, Mingyi Zhu, Mengzu Shi, Zongyao Huang
- Link: https://arxiv.org/abs/2608.01295v1
- Score: 17.0
- Match: 标题匹配 high-temperature superconductivity; 最近 3 天发布

**中文摘要：** 在外延压缩应变下双层镍酸盐中实现高温超导被广泛解释为模仿高静水压力的影响。为了测试这些机制的等效性，我们研究了从压缩 (-2.14%) 到拉伸 (+0.91%) 的综合应变连续体。至关重要的是，通过臭氧辅助原子层外延，我们在 NdAlO3 基底上生长的 La2PrNi2O7 薄膜中实现了高温超导性，这在该材料系统中引起了最极端的压缩应变。 在极端压缩（-2.14%）下，这些薄膜表现出 60 K 的 Tc_onset、33 K 的零电阻和 20 K 的抗磁响应，磁输运测量证实了准二维超导性质。将我们的相图与报道的数据进行比较，揭示了不同的晶格响应：与加压晶体不同，外延膜中的超导窗口在面外参数 c（或 c/ap 比率）方面显着发散，但在面内参数 ap 方面与本体保持一致。 至关重要的是，虽然两个系统中的超导性都是通过抑制自旋密度波（SDW）而产生的，但霍尔测量揭示了基本的电子二分法：最佳超导薄膜本质上是类电子的（表现出负霍尔系数），与高压块状晶体和非超导拉伸薄膜的类空穴性质（正霍尔系数）形成鲜明对比。 最终，两种调谐策略都有效地调节了潜在的相关景观（超导性的真正驱动力），超越了特定费米表面拓扑的限制。这项工作为探索镍酸盐的多轨道物理建立了宏观平台，为研究高温超导性提供了新的维度。
**讨论重点：** 在外延压缩应变下双层镍酸盐中实现高温超导被广泛解释为模仿高静水压力的影响。为了测试这些机制的等效性，我们研究了从压缩 (-2.14%) 到拉伸 (+0.91%) 的综合应变连续体。 结合关键词看，阅读时应重点关注高温超导相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 9. Magnetic circular dichroism of THz modes and selection rules of Raman-active optical phonons in the polar altermagnet candidate \ce{Mn2Mo3O8}

- Source: arXiv
- Date: 2026-08-02T07:54:50Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: F. Schilberth, K. Vasin, M. Knauft, M. Kondákor, M. Vuckovic, N. Herrmann
- Link: https://arxiv.org/abs/2608.01062v1
- Score: 16.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们通过温度相关拉曼散射和磁光太赫兹时域透射光谱研究了共线交替磁体候选 ce{Mn2Mo3O8} 中的磁和振动激发。通过与精确捕获振动本征模式的本征频率的 \textit{ab initio} 计算进行比较，我们识别了所有光学声子，包括 $A_1​​$ 和 $E_2$ 类型的最低拉曼模式，这在之前的拉曼研究中仍然难以捉摸。 此外，我们比较了 ce{Mn2Mo3O8} 的顺磁相和磁有序相中光学活性声子的选择规则，并分析了关于赝角动量守恒的拉曼选择规则。没有证据表明简并顺磁 $E_2$ 光学声子在磁排序时分裂成圆偏振模式的问题可以得到解决，这可能是由于 Mn$^{2+}$ 典型的弱自旋轨道耦合所致。 相比之下，我们在宽太赫兹激发带上观察到强磁圆二色性，以磁有序状态出现。该带可能源自双磁振子激发，仅具有电偶极子活性，并且具有场相关的双组分精细结构。其磁圆二色性在 4~T 的自旋翻转跃迁之上消失。
**讨论重点：** 通过与精确捕获振动本征模式的本征频率的 \textit{ab initio} 计算进行比较，我们识别了所有光学声子，包括 $A_1​​$ 和 $E_2$ 类型的最低拉曼模式，这在之前的拉曼研究中仍然难以捉摸。此外，我们比较了 ce{Mn2Mo3O8} 的顺磁相和磁有序相中光学活性声子的选择规则，并分析了关于赝角动量守恒的拉曼选择规则。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 10. Non-relativistic spin splitting in a triangular metal-excess magnet Fe$_{1+δ}$Sb

- Source: arXiv
- Date: 2026-08-01T21:14:06Z
- Venue: cond-mat.mtrl-sci
- Authors: Chao-Chun Wei, Xiaojuan Ni, Sophia Adams, Jacob Kjeldahl Jensen, Jue Liu, Qiang Zhang
- Link: https://arxiv.org/abs/2608.00871v1
- Score: 15.0
- Match: 摘要匹配 ferromagnetism; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 非相对论自旋分裂（NRSS）​​反铁磁体最近成为一类重要的磁性材料，它将补偿磁性与动量相关的自旋分裂结合起来，为自旋电子学应用提供了新的机会。在这里，我们利用中子衍射、对分布函数、磁力测量和密度泛函理论计算研究了 NiAs 型 Fe$_{1+δ}$Sb 系列 ($δ= 0.17$-0.30)。 中子衍射确定 Fe$_{1+δ}$Sb 采用 $120^\circ$ 共面补偿磁序，传播矢量 $\mathbf{k}=(1/3,\,1/3,\,0)$。正如对分布函数精修所揭示的那样，增加间隙 Fe 会抑制有序磁矩，同时引起局部对称性降低。密度泛函理论预测动量相关的自旋分裂，主要是具有奇宇称 f 波对称性的面外自旋极化，从而将该材料确立为非共线 NRSS 反铁磁体。 受 Fe$_{1+δ}$Sb 和已知的交流磁体 CrSb 结构相似性的启发，我们进一步研究了它们的固溶体，发现中等浓度的 Cr 取代会产生铁磁成分和团簇自旋玻璃行为。这些结果将 Fe$_{1+δ}$Sb 确立为非共线 NRSS 反铁磁性的新平台，并证明金属填隙和替代是调节磁序和性能的有效参数。
**讨论重点：** 在这里，我们利用中子衍射、对分布函数、磁力测量和密度泛函理论计算研究了 NiAs 型 Fe$_{1+δ}$Sb 系列 ($δ= 0.17$-0.30)。中子衍射确定 Fe$_{1+δ}$Sb 采用 $120^\circ$ 共面补偿磁序，传播矢量 $\mathbf{k}=(1/3,\,1/3,\,0)$。 结合关键词看，阅读时应重点关注铁磁性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。
