# Latest papers for 程旭丽

Updated: 2026-08-18T00:56:55.475097+00:00
Window: last 14 days

## Notes

- arXiv query failed for 机器学习分子动力学模拟与热力学性质: HTTP Error 429: Unknown Error
- 机器学习分子动力学模拟与热力学性质 kept previous papers because the current query returned 0 results.
- arXiv query failed for 凝聚态物理强关联体系和多铁性质: The read operation timed out
- 凝聚态物理强关联体系和多铁性质 returned 1 papers; target range is 5-10.

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

### 1. Efficient quantum implementation of dynamical mean field theory for correlated materials

- Source: Journal
- Date: 2026-08-17
- Venue: npj Computational Materials
- Authors: Norman Hogan, Efekan Kökcü, Thomas Steckmann, Liam P. Doak, Carlos Mejuto-Zaera, Daan Camps
- Link: https://doi.org/10.1038/s41524-026-02289-2
- Score: 16.0
- Match: 标题匹配 dynamical mean field theory; 最近 3 天发布

**中文摘要：** 当前元数据未提供原文摘要。论文题目为“Efficient quantum implementation of dynamical mean field theory for correlated materials”。
**讨论重点：** 结合关键词看，阅读时应重点关注动力学平均场理论相关的研究对象、方法假设、关键参数、数据来源，以及结果能否迁移到相邻材料或物理体系。
