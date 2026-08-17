# Latest papers for 程旭丽

Updated: 2026-08-17T00:57:14.546794+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Evaluating Electrostatic Embedding MLIP/MM for Relative Binding Free Energy Calculations

- Source: arXiv
- Date: 2026-08-13T15:19:17Z
- Venue: physics.chem-ph, physics.comp-ph
- Authors: Stephen E. Farr, Gianni De Fabritiis
- Link: https://arxiv.org/abs/2608.13355v1
- Score: 11.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 炼金术相对结合自由能 (RBFE) 计算受到经典力场的固定电荷近似的限制。混合机器学习原子间势/分子力学 (MLIP/MM) 方案可以纠正配体应变，但在机械嵌入下仍然描述具有静点电荷的配体-环境静电。已经提出了将机器学习的电荷耦合到 MM 环境的静电嵌入方案，并针对简单系统的 QM/MM 进行了验证，但尚未在生产炼金工作流程中进行测试。 我们采用 Semelak 等人的静电嵌入方案，并在蛋白质-配体 RBFE 上对其进行评估。我们在 AceFF 数据集中的 $10^{6}$ 构象上训练了一个 TensorNet2 模型 \texttt{AceFF-2-RESP-1}，联合预测能量、力和约束静电势 (RESP) 电荷。我们选择 RESP 而不是 MBIS，是因为它与所耦合的 AMBER 系列力场具有可通约性。预测的电荷进入粒子网格 Ewald 和的短程直接空间部分，并使用 Thole 阻尼来防止炼金术变换期间发生极化灾难。 我们在 Wang 等人基准集中的五个目标上测试了该方案，这些目标由先前的研究提前确定，每个边缘和匹配的协议具有三个重复。静电嵌入提高了 TYK2 的每项准确性和相关性指标（$ΔΔG$ RMSE $0.86 \rightarrow 0.45$~kcal/mol 相对于 GAFF2），但与 CDK2、凝血酶、p38 和 JNK1 的经典和机械嵌入基线相当。标准的单分子能量和电荷基准并不能很好地预测这种目标依赖性结果。 TYK2 在薛定谔基准测试中将良好的 $ΔΔG$ 精度与最低的力误差结合在一起，但这种模式并不适用于其他目标。
**讨论重点：** 我们在 Wang 等人基准集中的五个目标上测试了该方案，这些目标由先前的研究提前确定，每个边缘和匹配的协议具有三个重复。我们在 AceFF 数据集中的 $10^{6}$ 构象上训练了一个 TensorNet2 模型 \texttt{AceFF-2-RESP-1}，联合预测能量、力和约束静电势 (RESP) 电荷。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 2. Cross-Geometry Transferability Assessment of Universal Machine Learning Interatomic Potentials: From Bulk Materials to Atomic Nanowires

- Source: arXiv
- Date: 2026-08-07T00:15:49Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.comp-ph
- Authors: Pedro H. M. Zanineli, Bruno Focassio, Gabriel R. Schleder
- Link: https://arxiv.org/abs/2608.06662v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 基础机器学习原子间势（MLIP）能够以比第一原理方法低得多的计算成本进行原子模拟，但它们在结构几何形状上的可靠性仍然没有得到充分的了解。在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。 我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。在没有任何训练的情况下，仅在参考能量对准后，最佳零射击模型（ORB-V3）的能量和力均方根误差分别达到 6 meV/atom 和 197.3 meV/Å，其中颈部和线配置中的力误差最大。然后，我们比较零样本推理、微调和从头开始训练策略。与从头开始训练相比，微调产生的能量和力量误差更低，而两者都需要相当的挂钟时间。 特定于几何形状的微调提高了域内精度，但经常产生向其他结构类别的负转移，而混合几何微调则减少了跨几何误差。对弹性和振动特性、表面能和颈部动力学的评估进一步表明，基于平均能量和力误差的排名并不能普遍预测属性水平的行为。这些结果表明，在将基础 MLIP 应用于低配位（离子）纳米结构时，几何形状多样的目标数据和独立的物理验证是必要的。
**讨论重点：** 在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 3. Ultrafast Nonthermal Lattice Destabilization and Suppression of Polar Optical Scattering in Electronically Excited $α$-SiO$_2$ from First-Principles and Deep Neural Network Potential Modeling

- Source: arXiv
- Date: 2026-07-30T21:04:07Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Iyyappa Rajan Panneerselvam, Mark Yeung, Charlotte Palmer, Brendan Dromey, Lorenzo Stella
- Link: https://arxiv.org/abs/2607.28838v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。使用 DNNP 可以对具有数千个原子的大型 $α$-SiO$_2$ 单元进行接近 DFT 精度的原子建模。 特别是，DNNP 使我们能够获得由电子温度突然升高激发的 $α$-SiO$_2$ 的精确声子能带结构和分子动力学 (MD)。随着电子温度 $T_e$ 的增加，发现 $α$-SiO$_2$ 出现明显的晶格失稳，表现为违反弹性稳定性标准、体积大幅膨胀、体积模量急剧下降以及由于反键态占据而导致 Si-O 键逐渐减弱。 根据电子和声子能带结构，我们估计了 Frohlich 耦合常数，该常数随着 $T_e$ 的增加而减小，表明在电子温度升高时会交叉到 $α$-SiO$_2$ 的非极性相。 Bader 电荷分析证实了这一点。我们还建议，在 $T_e > 2$ eV 时应强烈抑制极性光学声子散射。从大单元 DNNP-MD 模拟中，我们表明，在最初的几百飞秒内，并未实现由麦克斯韦-玻尔兹曼分布定义的明确热平衡。 这种行为解释了 $T_e$ 突然上升后动力学温度的非单调平衡。当 $T_e$ 升至 2.6 eV 后，Si 和 O 原子首先在两个不同的温度下分别达到平衡，表明存在原子流体相，这与最近的实验和理论发现一致。
**讨论重点：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 4. PASS: Perturbation augmented space group structure sampling for transferable Fe-O machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-30T10:48:01Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Zixiong Wei, Fei Shuang, Poulumi Dey
- Link: https://arxiv.org/abs/2607.28000v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 铁（Fe）氧化的准确原子建模需要可靠的原子间势，这需要广泛且具有代表性的第一性原理数据集来训练原子间势。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。 我们提出了一种系统方法，基于原子团簇扩展 (ACE) 框架，为 Fe-O 系统开发首个可转移机器学习原子间势 (MLIP)。我们通过体积、表面和界面特性彻底验证了 ACE MLIP 在纯 Fe 和 Fe-O 系统中的准确性和功能。我们展示了使用 ACE MLIP 大规模 Fe 氧化模拟中 FeO 类结构的形成。 这项工作表明，PASS 方法产生了准确且可转移的 MLIP，它能够捕获氧化物生长的反应复杂性，同时保持扩展系统的计算实用性。
**讨论重点：** 在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 5. Extracting Atomic Environments for Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-28T17:28:41Z
- Venue: cond-mat.mtrl-sci
- Authors: Jared C. Stimac, Fei Zhou, Kyle Bushick, Bo Lei, Sebastien Hamel, Amit Samanta
- Link: https://arxiv.org/abs/2607.26018v2
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 为了通过原子模拟（例如分子动力学（MD））适当捕获大规模材料特征和突发现象，系统规模可以达到数亿个原子。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 为了计算感兴趣区域中原子上的 DFT 力，例如用于原子间势的主动学习或动态训练，需要从较大的模拟框中提取一小组原子，并且通常使用 DFT 的周期性边界条件。然而，尚未系统地分析选择这组提取的原子的形状和大小以及生成潜在必要的钝化包络的方法。 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。我们使用多种材料系统进行测试，其中包括无定形 $\mathrm{SiO_2}$、具有螺旋位错的 Ta 和熔融 C。我们演示了一种非常简单的程序（我们称为删除的方法），其性能优于一系列替代提取方法。
**讨论重点：** 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 6. Charge-Density-Wave Phase Transitions in Monolayer 1T-TaS2 from Universal Machine Learning Molecular Dynamics

- Source: arXiv
- Date: 2026-07-24T13:57:09Z
- Venue: cond-mat.mtrl-sci
- Authors: Valentina Nesterova, Tribhuwan Pandey, Tom Berlijn, Fariborz Kargar, Lucas Lindsay, Konstantin Klyukin
- Link: https://arxiv.org/abs/2607.22316v1
- Score: 8.0
- Match: 标题匹配 machine learning molecular dynamics

**中文摘要：** 1T 过渡金属二硫属化物中的电荷密度波 (CDW) 相是由强电子声子耦合和伴随的晶格不稳定性产生的。由于需要大型超级电池和广泛的有限温度采样，使用传统的第一原理分子动力学 (MD) 捕获其随温度变化的结构演化仍然具有挑战性。 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。针对 DFT 位移能量的基准测试确定了 UMA-s-1p1 通用机器学习潜力，具有足够的精度用于后续的有限温度模拟。 我们的结果表明，大规模 MD 模拟再现了实验观察到的从低温大卫之星 (SoD) 扭曲结构到高温原始六边形结构的相变序列，通过归因于 SoD 的 Ta 原子数量来量化。加热-冷却循环表现出热滞后，并且在冷却时，系统冻结成多域状态，其中α和\b{eta} CDW手性独立成核并持续到最低温度。 这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。
**讨论重点：** 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。 结合关键词看，阅读时应重点关注机器学习分子动力学相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. A high-dimensional neural network potential for finite-temperature phenomena in NiTi martensite

- Source: arXiv
- Date: 2026-07-22T19:32:23Z
- Venue: cond-mat.mtrl-sci
- Authors: Petr Jaroš, Petr Sedlák, Petr Šesták, Miroslav Černý, Jörg Behler, Hanuš Seiner
- Link: https://arxiv.org/abs/2607.20681v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 HDNNP 准确地描述了 B19$^\prime$ 和 B33 相的相对稳定性，包括 meV/原子数量级的细微能量差异。预测的堆垛层错能量景观具有强烈的各向异性，并揭示了优先剪切路径，为变形和孪生机制提供了原子学的见解。有限温度分子动力学模拟进一步能够研究作为温度函数的无约束结构演化。 总体而言，开发的 HDNNP 为纳秒时间尺度上包含数十万个原子的马氏体 NiTi 系统的复杂结构和功能行为的原子模拟提供了坚实的基础。
**讨论重点：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 8. Study of ordering in (MoCrTi)$_{100-x}$Al$_x$ refractory high-entropy alloys using machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-20T16:01:06Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn
- Authors: Jiyao Zhang, Klemens Lechner, Markus Maßwohl, Petra Spoerk-Erdely, David Holec
- Link: https://arxiv.org/abs/2607.18099v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 耐火高熵合金由于其优异的机械性能而成为高温应用的有希望的候选者。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。在这项工作中，通过利用通用机器学习原子间势与混合蒙特卡罗和分子动力学模拟，研究了(MoCrTi)(100-x)Alx系统的温度依赖性热力学和机械性能。 热容和短程有序参数揭示了不同的有序-无序转变行为。虽然 Mo25Cr25Ti25Al25 和 Mo32Cr32Ti32Al4 合金表现出由 B2 型原子对的协同排序主导的单一转变，但 Mo28Cr28Ti28Al16 和 Mo30Cr30Ti30Al10 合金表现出两个单独的转变：由特定对驱动的低温阶段（Mo28Cr28Ti28Al16 中的 Mo-Al；Mo28Cr28Ti28Al16 中的 Al-Al） Mo30Cr30Ti30Al10) 和由其余对控制的高温阶段。 结构分析表明，在低温有序B2相中，Mo和Al共享一个亚晶格，而Cr和Ti共享另一个亚晶格。此外，还确定了排序和机械刚度之间的关系。有序显着增强了弹性常数和模量，并产生非单调的成分依赖性。与随机固溶体不同的是，随机固溶体的刚度随着 Al 含量的降低而单调增加，有序构型表现出非单调趋势，在 Mo30Cr30Ti30Al10 合金中达到峰值。 这种增强归因于强短程有序引起的刚性原子对的优化群体。这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。
**讨论重点：** 这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 9. RuNNer 2.0: A Software Suite for High-Dimensional Neural Network Potentials

- Source: arXiv
- Date: 2026-07-20T14:13:35Z
- Venue: physics.chem-ph, cond-mat.mtrl-sci, physics.comp-ph
- Authors: Alexander L. M. Knoll, Moritz R. Schäfer, K. Nikolas Lausch, Moritz Gubler, Henry Wang, Richard Springborn
- Link: https://arxiv.org/abs/2607.17978v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局域电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。优化的内存管理策略消除了传统上与远程交互相关的训练开销，从而使 4G-HDNNP 能够以与本地对应物相同的效率进行训练。 RuNNer 2.0 采用现代 Fortran（2003/2008 标准）开发，结合​​混合 MPI/OpenMP 并行化方案，旨在在任何 CPU 环境（从经济高效的本地工作站到大规模 HPC 集群）中高效运行。其模块化库架构有助于直接绑定到外部模拟软件； LAMMPS 和原子仿真环境 (ASE) 的本机接口提供对其所有功能的完全访问，包括内置的基于委员会的不确定性量化。 RuNNer 2.0生态系统的高效率和可扩展性通过详细的基准测试得到证明。
**讨论重点：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局域电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 10. Are Machine Learning Interatomic Potentials Truly Practical? A Benchmark of 23 Mainstream Models

- Source: arXiv
- Date: 2026-07-08T17:04:42Z
- Venue: cond-mat.mtrl-sci, cs.CE, physics.comp-ph
- Authors: Hanwen Kang, Tenglong Lu, Sheng Meng, Miao Liu
- Link: https://arxiv.org/abs/2607.07647v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。我们评估三个维度：预测准确性、MD 模拟吞吐量和原子可扩展性。 我们的结果揭示了精确度与效率之间的巨大权衡：大型 SOTA 模型的精确度仅比轻量级模型高出 3-5 meV/atom，但吞吐量却损失了几个数量级——在最坏的情况下，仅比 DFT 本身快一点点。相比之下，轻量级 MLIP 位于帕累托前沿并在适度的硬件上运行。教训是，一维基准会误导该领域，未来的 MLIP 开发应该重视效率和可扩展性以及准确性。
**讨论重点：** 我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Landau theory and exchange instabilities in Mn$_5$Si$_3$: A case against altermagnetism

- Source: arXiv
- Date: 2026-08-13T17:12:49Z
- Venue: cond-mat.mtrl-sci
- Authors: K. D. Belashchenko
- Link: https://arxiv.org/abs/2608.13483v1
- Score: 25.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 薄膜 Mn$_5$Si$_3$ 因其金属丰度、表现出反常输运特性以及假设的 $d$ 波交换分裂模式而成为研究最多的交变磁候选材料之一，从而实现自旋极化输运和各种自旋电子应用。其假定的交变磁结构具有零传播矢量，这与在 $M$ 星上有序的共线反铁磁体相 (AFM2) 形成鲜明对比。在这项工作中，使用朗道理论、顺磁不稳定性的第一原理计算和蒙特卡洛模拟来分析这两个相。 AFM2 在朗道理论中表现为 $M$ 星单臂处的对称保护反转偶数、排列奇数模式。在$Γ$处，相同的单元内排序模式属于$E_{2g}$排序参数的共线分支。在这两种情况下，相位选择都需要高阶项。对顺磁、无序局部矩状态的第一性原理计算正确地识别了 $M$ 恒星处的主要交换不稳定性，并且由此产生的经典海森堡模型在合理的温度下有序进入单点熵所青睐的正交 $3M$ 相。 $Γ$点$E_{2g}$模式（其朗道理论包含交变磁扇区）明显较弱，并被表现出异常输运的Mn$_5$Si$_3$薄膜代表的外延应变进一步抑制。相同的应变降低了领先的磁交换规模。 这些结果为块体 $M$ 点不稳定性提供了自然的解释，但强烈反对在中等应变的块状 Mn$_5$Si$_3$ 薄膜中假设的传播矢量从 $M$ 到 $Г$ 的重新定位，这表明如果没有额外的物理场，相应的交变磁相不太可能稳定。
**讨论重点：** 对顺磁、无序局部矩状态的第一性原理计算正确地识别了 $M$ 恒星处的主要交换不稳定性，并且由此产生的经典海森堡模型在合理的温度下有序进入单点熵所青睐的正交 $3M$ 相。其假定的交变磁结构具有零传播矢量，这与在 $M$ 星上有序的共线反铁磁体相 (AFM2) 形成鲜明对比。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Two routes to quantum anomalous Hall states in altermagnets

- Source: arXiv
- Date: 2026-08-12T14:42:18Z
- Venue: cond-mat.str-el, cond-mat.mes-hall
- Authors: Makoto Naka, Shuntaro Sumita, Yukitoshi Motome, Hitoshi Seo
- Link: https://arxiv.org/abs/2608.12124v1
- Score: 23.0
- Match: 摘要匹配 Hubbard model; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 摘要匹配 altermagnetic materials

**中文摘要：** 我们从理论上提出了在交变磁材料中实现量子反常霍尔态的两种可能途径。我们考虑具有与斜方晶体结构相关的反对称自旋轨道耦合的最小方格哈伯德模型，该模型支持拓扑平凡的交变磁态。通过结合 Rashba 型自旋轨道耦合和外部扰动，我们证明了这种平凡的状态可以通过两种不同的方式转变为拓扑交磁相。 第一条路线由交错电势驱动，该电势打破了连接晶体等效子晶格的对称性，从而产生以量子化霍尔电导率 $\left| 为特征的拓扑交变磁基态。 σ_{xy} \right|=e^2/h$ 和陈数 $C=1$。第二条路线是通过施加垂直于二维平面的磁场来实现的。由此产生的拓扑状态在磁滞回线中显示为亚稳态，表现出量子化霍尔电导率 $\left| σ_{xy} \right|=2e^2/h$ 与陈数 $C=2$ 相关。 我们表明，这些拓扑转变伴随着布里渊区边界处的特征间隙闭合，间隙闭合点的数量决定了陈数。带状几何计算揭示了与体拓扑不变量一致的手性边缘态，并证明了 $C=1$ 和 $C=2$ 态之间不同的自旋极化。我们的结果建立了实验上可行的途径来实现交流磁体中的量化异常霍尔响应。
**讨论重点：** 我们从理论上提出了在交变磁材料中实现量子反常霍尔态的两种可能途径。我们考虑具有与斜方晶体结构相关的反对称自旋轨道耦合的最小方格哈伯德模型，该模型支持拓扑平凡的交变磁态。 结合关键词看，阅读时应重点关注Hubbard 模型、交变磁性、交变磁性材料相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Competition between local magnetic disorder and altermagnetism in doped FeSb$_2$

- Source: arXiv
- Date: 2026-08-11T15:57:19Z
- Venue: cond-mat.mtrl-sci
- Authors: Enrico Di Lucente, Michele Simoncelli
- Link: https://arxiv.org/abs/2608.11089v1
- Score: 23.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 近两周发布

**中文摘要：** 最近的实验报告表明，窄带隙非磁性半导体FeSb$_2$可以通过Co掺杂（Co$_{0.15}$Fe$_{0.85}$Sb$_2$）转变为交磁金属，或者通过Cr掺杂转变为磁无序或短程有序状态（Cr$_{0.15}$Fe$_{0.85}$Sb$_2$）。在这里，我们依靠哈伯德增强密度泛函理论（DFT+U）结合罗密欧基态搜索算法，从第一原理探索这些掺杂系统的能量景观和磁态。 在已建立的虚拟晶体近似（VCA）中，我们表明 \texttt{Romeo} 发现了几个不平凡的磁态，这些磁态为超级晶胞中掺杂的有针对性的显式模拟提供了信息。我们依靠这些发现来讨论 VCA-Romeo 方法与显式掺杂超级细胞方法的优点和局限性，以及如何协同使用它们。 总体而言，我们的模拟表明，Cr 掺杂系统的基态是局域无序自旋补偿 (LDSC) 配置，形式上与 Néel 的 L 型完全补偿亚铁磁性兼容，而 Co 掺杂系统的基态被发现是交变磁性 (AFMo)。这项工作展示了磁性合金的近似和显式模拟如何能够相互提供信息，并建立了研究候选金属交替磁体的协议。
**讨论重点：** 在这里，我们依靠哈伯德增强密度泛函理论（DFT+U）结合罗密欧基态搜索算法，从第一原理探索这些掺杂系统的能量景观和磁态。我们依靠这些发现来讨论 VCA-Romeo 方法与显式掺杂超级细胞方法的优点和局限性，以及如何协同使用它们。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Topological Superconductors in Doubly-Coupled Nanowires with Altermagnetism

- Source: arXiv
- Date: 2026-08-13T14:04:23Z
- Venue: cond-mat.mes-hall
- Authors: Hongfa Pan, Haoyang Wang, Wenguang Zhu, Zhenhua Qiao
- Link: https://arxiv.org/abs/2608.13265v1
- Score: 22.0
- Match: 标题匹配 altermagnetism; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们从理论上研究了在双耦合纳米线中集成邻近感应超导性和交变磁性的工程拓扑超导性的可能性。通过调整实验上可访问的参数，我们发现了四种不同的拓扑超导相：D类、BDI类，以及每端有两个马约拉纳零模式的两个相，分别受到自旋群和磁点群对称性的保护。 除了继承交变磁感应拓扑超导的优点之外，我们的系统还提供多个调谐旋钮（例如，超导相位差和线间耦合）来控制拓扑特性。
**讨论重点：** 我们从理论上研究了在双耦合纳米线中集成邻近感应超导性和交变磁性的工程拓扑超导性的可能性。通过调整实验上可访问的参数，我们发现了四种不同的拓扑超导相：D类、BDI类，以及每端有两个马约拉纳零模式的两个相，分别受到自旋群和磁点群对称性的保护。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 5. Superconductivity in the $t$-$t'$ Hubbard Model from Symmetry-Preserving Neural-Network Quantum States

- Source: arXiv
- Date: 2026-08-12T18:00:02Z
- Venue: cond-mat.str-el, cond-mat.dis-nn, cond-mat.supr-con
- Authors: Riccardo Rende, Luciano Loris Viteritti, Antoine Georges
- Link: https://arxiv.org/abs/2608.12465v1
- Score: 17.0
- Match: 摘要匹配 strongly correlated electrons; 标题匹配 Hubbard model; 近两周发布

**中文摘要：** 尽管二维掺杂哈伯德模型的基态性质在强相关电子理论中具有根本重要性，但其本质仍然存在激烈争论。变分方法为解决该问题提供了有力的途径，但其结论可能敏感地取决于所选的波函数参数化、平均场初始化或用于指导优化的钉扎场以及边界条件。 这可能有利于一种对称性打破另一种对称性，从而难以区分相互交织或竞争的顺序的真正相互作用与变分参数化引起的偏差。在这里，我们介绍了保对称回流配对 (SBP) ansatz，这是一种神经网络波函数，它通过构造尊重平移对称性，从而避免了这些破缺对称性最小值。 SBP ansatz 在 $t$-$t'$ Hubbard 模型上达到了最先进的变分能量，其晶格高达 $24\times24$，电子数为 $504$，低于竞争的纯条纹解决方案。通过推断热力学极限，我们找到了 $d$ 波超导序的有力证据，解决了有关 $t'/t=-0.2$ 和 $U/t=8.0$ 的 $1/8$ 掺杂模型的长期问题。 SBP 波函数建立在对称性和局域性的一般原理之上，为具有挑战性的相互作用费米子系统提供了广泛适用的变分表示。
**讨论重点：** 在这里，我们介绍了保对称回流配对 (SBP) ansatz，这是一种神经网络波函数，它通过构造尊重平移对称性，从而避免了这些破缺对称性最小值。尽管二维掺杂哈伯德模型的基态性质在强相关电子理论中具有根本重要性，但其本质仍然存在激烈争论。 结合关键词看，阅读时应重点关注强关联电子、Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 6. Dimensional crossover and local strain induced deflection of the spin spiral state in multiferroic NiI2

- Source: arXiv
- Date: 2026-08-12T11:32:08Z
- Venue: cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Tianxing Jiang, Lianchuang Li, Haiyan Zhu, Hongyu Wang, Junchao Tian, Wenzhao Wang
- Link: https://arxiv.org/abs/2608.11944v1
- Score: 17.0
- Match: 标题匹配 multiferroic; 摘要匹配 ferroelectricity; 近两周发布

**中文摘要：** 低维多铁性材料对于集成磁电器件具有广阔的前景。最近，自旋螺旋态已被证明可以在单层范德华 (vdW) 材料 NiI2 中诱导铁电性。然而，这种状态如何演化以及如何调整至二维极限仍不清楚。在这里，我们结合自旋偏振扫描隧道显微镜、逐层薄膜生长和多尺度理论模型来研究 NiI2 薄膜中的自旋螺旋。 随着薄膜厚度从 1 单层增加到 7 个单层，我们观察到自旋螺旋波长不断增加，波矢量从近 [110] 方向旋转到 [1-10] 方向，这证明了主要由增强的层间交换能驱动的维度交叉。此外，我们发现薄膜皱纹会引起自旋螺旋波矢的偏转，这是由交换相互作用的局部曲率引起的修改引起的。 我们的研究结果将厚度和局部应变确定为工程非共线螺旋磁性和 vdW 多铁性材料中伴随电极化的两种调谐方法。
**讨论重点：** 在这里，我们结合自旋偏振扫描隧道显微镜、逐层薄膜生长和多尺度理论模型来研究 NiI2 薄膜中的自旋螺旋。最近，自旋螺旋态已被证明可以在单层范德华 (vdW) 材料 NiI2 中诱导铁电性。 结合关键词看，阅读时应重点关注多铁性、铁电性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 7. Magnetic reconstruction of the altermagnet α-MnTe(0001) surface driven by ligand holes

- Source: arXiv
- Date: 2026-08-13T06:43:56Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall
- Authors: Tomonori Tanaka, Yoshihiro Gohda
- Link: https://arxiv.org/abs/2608.12878v1
- Score: 15.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们从第一原理出发证明，交变磁体 α-MnTe 在 (0001) 表面重建其磁序，与铁磁最外层 Mn 双层堆叠，其能量低于整体连续双层。干净的终止在 Te 悬空键中留下配体孔。驱动逆转的原因是到达 Te 的空穴部分介导 Mn 双层内的交换。计算出的恒定能量轮廓与光电发射图一致。因此，薄膜上的传输和光谱对非本体磁序的表面磁序敏感。
**讨论重点：** 我们从第一原理出发证明，交变磁体 α-MnTe 在 (0001) 表面重建其磁序，与铁磁最外层 Mn 双层堆叠，其能量低于整体连续双层。干净的终止在 Te 悬空键中留下配体孔。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 8. Dissipationless Photovoltaic Spin Hall Effect from Spin-current Vorticity

- Source: arXiv
- Date: 2026-08-13T08:49:54Z
- Venue: cond-mat.mtrl-sci
- Authors: Longjun Xiang, Jian Wang
- Link: https://arxiv.org/abs/2608.12968v1
- Score: 14.0
- Match: 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 自旋流涡度（SCV）可以产生线性磁自旋霍尔效应[\href{https://doi.org/10.1038/s41586-018-0853-0}{Nature \textbf{565}, 627 (2019)}]，但其在非线性自旋霍尔传输中的作用却很少被探索。在这里，我们证明，在直流电场下，SCV 可以偏转光激发电子以驱动无耗散的光伏自旋霍尔效应（PSHE），其中圆偏振光和线偏振光的光激发分别由贝里曲率和量子度量控制。 由于贝里曲率是 $\mathcal{T}$-奇数，而量子度量是 $\mathcal{T}$-偶数，因此它们各自与 $\mathcal{T}$-奇数 SCV 的组合产生 $\mathcal{T}$-偶数和 $\mathcal{T}$-奇数 PSHE，其中 $\mathcal{T}$ 表示时间反转对称性。值得注意的是，我们发现 $\mathcal{T}$-均匀 PSHE 的自旋电流可以通过切换光螺旋性来逆转，如单层 WTe$_2$ 所示。相比之下，交变磁体中的 $\mathcal{T}$ 奇数 PSHE 在尼尔矢量反转时改变符号，如 $d$ 波交变磁体模型所示。 除了 PSHE 之外，我们还表明 SCV 偶极子控制着最近提出的德鲁德效应和固有非线性自旋霍尔效应。我们的结果揭示了两种可切换的自旋霍尔机制，并将 SCV 确立为理解无耗散非线性自旋霍尔传输的统一概念。
**讨论重点：** 相比之下，交变磁体中的 $\mathcal{T}$ 奇数 PSHE 在尼尔矢量反转时改变符号，如 $d$ 波交变磁体模型所示。在这里，我们证明，在直流电场下，SCV 可以偏转光激发电子以驱动无耗散的光伏自旋霍尔效应（PSHE），其中圆偏振光和线偏振光的光激发分别由贝里曲率和量子度量控制。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 9. Pulse Engineering of Quantum Many-Body Dynamics: Emergent Scar States, Entanglement, and Nonstabilizerness

- Source: arXiv
- Date: 2026-08-12T19:51:24Z
- Venue: quant-ph, cond-mat.str-el
- Authors: Prasant Mallik, Arkaprava Sil, Sudipto Singha Roy
- Link: https://arxiv.org/abs/2608.12559v1
- Score: 14.0
- Match: 标题匹配 quantum many-body; 近两周发布

**中文摘要：** 理解和连贯地控制相互作用的量子多体系统的特性是非平衡量子物理学的一个核心挑战。虽然在过去的几十年里，人们广泛引入了多体哈密顿量来研究量子混沌、非典型本征态和量子资源，但在单个微观模型中系统地设计和不断调整这些特性仍然很大程度上未被探索。 在这里，我们采用脉冲工程方案来构建有效的哈密顿量，该哈密顿量在具有局部杂质的混沌海森堡（XXX）链和 ZX 哈密顿量之间连续插值。沿着这种插值，我们识别出嵌入激发态光谱中的几个可分析处理的非典型本征态家族，具有独特的纠缠和非稳定特性。在 XXX 极限下，这些态在纠缠和稳定器 Rényi 熵方面都表现出精确的平台，并且对应于长程价键固体 (VBS) 态的相干叠加。 随着脉冲强度的增加，有效哈密顿量在低能谱中表现出一组新的近似纠缠平台的层次结构。有趣的是，在完全脉冲设计的 ZX 极限中，我们发现了一对独特的长程纠缠稳定剂本征态，对应于彩虹疤痕态。我们进一步表明，脉冲工程保留了原始模型的独特混沌和非混沌状态，而这在纠缠和非稳定器的动态生成中很大程度上不存在。 脉冲工程模型在两种状态下生成几乎相同的量子资源，揭示了量子混沌和量子资源生成之间的部分解耦。我们的结果将脉冲工程确立为一种通用框架，用于生成具有结构化本征态和可调量子资源的多体哈密顿量。
**讨论重点：** 在这里，我们采用脉冲工程方案来构建有效的哈密顿量，该哈密顿量在具有局部杂质的混沌海森堡（XXX）链和 ZX 哈密顿量之间连续插值。虽然在过去的几十年里，人们广泛引入了多体哈密顿量来研究量子混沌、非典型本征态和量子资源，但在单个微观模型中系统地设计和不断调整这些特性仍然很大程度上未被探索。 结合关键词看，阅读时应重点关注量子多体相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 10. Emergent heavy fermion and superconductivity near Mott transition in twisted bilayer graphene

- Source: arXiv
- Date: 2026-08-12T17:59:59Z
- Venue: cond-mat.str-el
- Authors: Ya-Hui Zhang
- Link: https://arxiv.org/abs/2608.12319v1
- Score: 14.0
- Match: 标题匹配 heavy fermion; 近两周发布

**中文摘要：** 在带宽调谐莫特跃迁附近，金属的费米速度 $v_F$ 和准粒子残留 $Z$ 通常消失。在这里，我们展示了在整数填充时扭曲双层石墨烯（TBG）中出现的类似现象，并且可以通过投影有源带限制内的新兴重费米子框架捕获。与包含远程带的模型不同，我们有效的重费米子描述来自于 \textit{混合价莫特} 物理通过解耦电荷和局部矩扇区。 在电荷区域，活跃能带 $c(\mathbf{k})$ 与新兴的 \emph{正交费米子} $ψ(\mathbf{k})$ 杂交，在 $|\mathbf{k}| 处打开一个大的莫特能隙。 > k_*$ （$k_*$ 设置动量补丁大小）和中性点 ($ν=0$) 附近 $\mathbf{k}=0$ 附近的二次能带接触半金属。正交费米子是双克隆和完整子激励的线性组合，可以写为 $ψ_i \sim (δn^f_i+\frac{1}{2})^{-1} f_i$。 $ψ$ 和局部矩 $ψ'$ 之间的新兴近藤耦合 $J_K \sim U$（$U$ 是局部哈伯德相互作用）将莫特转变框架为近藤屏蔽转变，并通过扭转角 $θ$ 进行调整。远离魔角，近藤筛选的重半金属在 $T_K$（近藤温度）以下发展，$Z$ 消失。引入反亨德耦合 $J_A$ 即使在 $ν=0$ 时也会在莫特边界附近产生完全带隙或向列型、节点带隙的 s 波超导穹顶。 在其他整数填充 $ν= \pm 1, \pm 2$ 时，增加带宽首先将小能隙莫特态驱动为中间二次能带接触半金属，然后进入具有大费米表面的重费米液体。我们的结果为新兴的重费米子物理建立了一个统一的框架，其中包括来自 $f$ 轨道的巡回载流子和局部矩。
**讨论重点：** 在这里，我们展示了在整数填充时扭曲双层石墨烯（TBG）中出现的类似现象，并且可以通过投影有源带限制内的新兴重费米子框架捕获。与包含远程带的模型不同，我们有效的重费米子描述来自于 \textit{混合价莫特} 物理通过解耦电荷和局部矩扇区。 结合关键词看，阅读时应重点关注重费米子相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。
