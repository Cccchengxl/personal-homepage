# Latest papers for 程旭丽

Updated: 2026-08-07T05:54:44.133663+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. An Exchange-Correlation Functional for Fast and Accurate Modeling of Ferroelectric Perovskites

- Source: arXiv
- Date: 2026-08-05T13:12:10Z
- Venue: cond-mat.mtrl-sci
- Authors: Owain T. Beynon, Chiara Gattinoni
- Link: https://arxiv.org/abs/2608.04806v1
- Score: 13.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 我们提出了一种新颖的交换关联泛函 C09x-PBEc，它将 C09 交换与 PBE 关联相结合，可以准确地模拟钙钛矿的铁电特性，同时保留 GGA 泛函的计算效率。随着人们对开发机器学习原子间势 (MLIP) 来模拟具有技术相关性的大规模铁电系统的兴趣日益浓厚，仔细研究用于计算 MLIP 训练的力、能量和应力的密度泛函理论交换相关函数非常重要。 以典型铁电体钛酸铅、PbTiO3 和钛酸钡、BaTiO3 为例，我们表明许多广泛使用的泛函往往会高估其晶格常数和自发极化。相反，与实验相比，具有 C09 交换的非局域范德华函数可以准确地捕获这些属性，但计算开销比 GGA 等更大。 我们证明，C09x-PBEc 将 C09 交换提供的精度与 GGA 的计算承受能力相结合，使其成为用于铁电钙钛矿 MLIP 训练的绝佳候选者。我们还证明，使用 C09x-PBEc 训练的 MLIP 在实验中准确再现了 PbTiO3 的铁电到顺电相变温度，表明使用 GGA 训练的 MLIP 有了显着的改进。
**讨论重点：** 我们提出了一种新颖的交换关联泛函 C09x-PBEc，它将 C09 交换与 PBE 关联相结合，可以准确地模拟钙钛矿的铁电特性，同时保留 GGA 泛函的计算效率。随着人们对开发机器学习原子间势 (MLIP) 来模拟具有技术相关性的大规模铁电系统的兴趣日益浓厚，仔细研究用于计算 MLIP 训练的力、能量和应力的密度泛函理论交换相关函数非常重要。 结合关键词看，阅读时应重点关注机器学习原子间势相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 2. Ultrafast Nonthermal Lattice Destabilization and Suppression of Polar Optical Scattering in Electronically Excited $α$-SiO$_2$ from First-Principles and Deep Neural Network Potential Modeling

- Source: arXiv
- Date: 2026-07-30T21:04:07Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Iyyappa Rajan Panneerselvam, Mark Yeung, Charlotte Palmer, Brendan Dromey, Lorenzo Stella
- Link: https://arxiv.org/abs/2607.28838v1
- Score: 11.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。使用 DNNP 可以对具有数千个原子的大型 $α$-SiO$_2$ 单元进行接近 DFT 精度的原子建模。 特别是，DNNP 使我们能够获得由电子温度突然升高激发的 $α$-SiO$_2$ 的精确声子能带结构和分子动力学 (MD)。随着电子温度 $T_e$ 的增加，发现 $α$-SiO$_2$ 出现明显的晶格失稳，表现为违反弹性稳定性标准、体积大幅膨胀、体积模量急剧下降以及由于反键态占据而导致 Si-O 键逐渐减弱。 根据电子和声子能带结构，我们估计了 Frohlich 耦合常数，该常数随着 $T_e$ 的增加而减小，表明在电子温度升高时会交叉到 $α$-SiO$_2$ 的非极性相。 Bader 电荷分析证实了这一点。我们还建议在 $T_e > 2$ eV 时应强烈抑制极性光学声子散射。从大单元 DNNP-MD 模拟中，我们表明，在最初的几百飞秒内，并未实现由麦克斯韦-玻尔兹曼分布定义的明确热平衡。 这种行为解释了 $T_e$ 突然上升后动力学温度的非单调平衡。当 $T_e$ 升至 2.6 eV 后，Si 和 O 原子首先在两个不同的温度下分别达到平衡，表明存在原子流体相，这与最近的实验和理论发现一致。
**讨论重点：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 3. PASS: Perturbation augmented space group structure sampling for transferable Fe-O machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-30T10:48:01Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Zixiong Wei, Fei Shuang, Poulumi Dey
- Link: https://arxiv.org/abs/2607.28000v1
- Score: 11.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 铁（Fe）氧化的准确原子建模需要可靠的原子间势，这需要广泛且具有代表性的第一性原理数据集来训练原子间势。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。 我们提出了一种系统方法，基于原子团簇扩展 (ACE) 框架，为 Fe-O 系统开发首个可转移机器学习原子间势 (MLIP)。我们通过体积、表面和界面特性彻底验证了 ACE MLIP 在纯 Fe 和 Fe-O 系统中的准确性和功能。我们展示了使用 ACE MLIP 大规模 Fe 氧化模拟中 FeO 类结构的形成。 这项工作表明，PASS 方法产生了准确且可转移的 MLIP，它能够捕获氧化物生长的反应复杂性，同时保持扩展系统的计算实用性。
**讨论重点：** 在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 4. Extracting Atomic Environments for Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-28T17:28:41Z
- Venue: cond-mat.mtrl-sci
- Authors: Jared C. Stimac, Fei Zhou, Kyle Bushick, Bo Lei, Sebastien Hamel, Amit Samanta
- Link: https://arxiv.org/abs/2607.26018v2
- Score: 9.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 为了通过原子模拟（例如分子动力学（MD））适当捕获大规模材料特征和突发现象，系统规模可以达到数亿个原子。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 为了计算感兴趣区域中原子上的 DFT 力，例如用于原子间势的主动学习或动态训练，需要从较大的模拟框中提取一小组原子，并且通常使用 DFT 的周期性边界条件。然而，尚未系统地分析选择这组提取的原子的形状和大小以及生成潜在必要的钝化包络的方法。 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。我们使用多种材料系统进行测试，其中包括无定形 $\mathrm{SiO_2}$、具有螺旋位错的 Ta 和熔融 C。我们演示了一种非常简单的程序（我们称为删除的方法），其性能优于一系列替代提取方法。
**讨论重点：** 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 5. Charge-Density-Wave Phase Transitions in Monolayer 1T-TaS2 from Universal Machine Learning Molecular Dynamics

- Source: arXiv
- Date: 2026-07-24T13:57:09Z
- Venue: cond-mat.mtrl-sci
- Authors: Valentina Nesterova, Tribhuwan Pandey, Tom Berlijn, Fariborz Kargar, Lucas Lindsay, Konstantin Klyukin
- Link: https://arxiv.org/abs/2607.22316v1
- Score: 8.0
- Match: 标题匹配 machine learning molecular dynamics; 近两周发布

**中文摘要：** 1T 过渡金属二硫属化物中的电荷密度波 (CDW) 相是由强电子声子耦合和伴随的晶格不稳定性产生的。由于需要大型超级电池和广泛的有限温度采样，使用传统的第一原理分子动力学 (MD) 捕获其随温度变化的结构演化仍然具有挑战性。 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。针对 DFT 位移能量的基准测试确定了 UMA-s-1p1 通用机器学习潜力，具有足够的精度用于后续的有限温度模拟。 我们的结果表明，大规模 MD 模拟再现了实验观察到的从低温大卫之星 (SoD) 扭曲结构到高温原始六边形结构的相变序列，通过归因于 SoD 的 Ta 原子数量来量化。加热-冷却循环表现出热滞后，并且在冷却时，系统冻结成多域状态，其中α和\b{eta} CDW手性独立成核并持续到最低温度。 这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。
**讨论重点：** 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。 结合关键词看，阅读时应重点关注机器学习分子动力学相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 6. A high-dimensional neural network potential for finite-temperature phenomena in NiTi martensite

- Source: arXiv
- Date: 2026-07-22T19:32:23Z
- Venue: cond-mat.mtrl-sci
- Authors: Petr Jaroš, Petr Sedlák, Petr Šesták, Miroslav Černý, Jörg Behler, Hanuš Seiner
- Link: https://arxiv.org/abs/2607.20681v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 HDNNP 准确地描述了 B19$^\prime$ 和 B33 相的相对稳定性，包括 meV/原子数量级的细微能量差异。预测的堆垛层错能量景观具有强烈的各向异性，并揭示了优先剪切路径，为变形和孪生机制提供了原子学的见解。有限温度分子动力学模拟进一步能够研究作为温度函数的无约束结构演化。 总体而言，开发的 HDNNP 为纳秒时间尺度上包含数十万个原子的马氏体 NiTi 系统的复杂结构和功能行为的原子模拟提供了坚实的基础。
**讨论重点：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 7. Study of ordering in (MoCrTi)$_{100-x}$Al$_x$ refractory high-entropy alloys using machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-20T16:01:06Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn
- Authors: Jiyao Zhang, Klemens Lechner, Markus Maßwohl, Petra Spoerk-Erdely, David Holec
- Link: https://arxiv.org/abs/2607.18099v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 耐火高熵合金由于其优异的机械性能而成为高温应用的有希望的候选者。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。在这项工作中，通过利用通用机器学习原子间势与混合蒙特卡罗和分子动力学模拟，研究了(MoCrTi)(100-x)Alx系统的温度依赖性热力学和机械性能。 热容和短程有序参数揭示了不同的有序-无序转变行为。虽然 Mo25Cr25Ti25Al25 和 Mo32Cr32Ti32Al4 合金表现出由 B2 型原子对的协同排序主导的单一转变，但 Mo28Cr28Ti28Al16 和 Mo30Cr30Ti30Al10 合金表现出两个单独的转变：由特定对驱动的低温阶段（Mo28Cr28Ti28Al16 中的 Mo-Al；Mo28Cr28Ti28Al16 中的 Al-Al） Mo30Cr30Ti30Al10) 和由其余对控制的高温阶段。 结构分析表明，在低温有序B2相中，Mo和Al共享一个亚晶格，而Cr和Ti共享另一个亚晶格。此外，还确定了排序和机械刚度之间的关系。有序显着增强了弹性常数和模量，并产生非单调的成分依赖性。与随机固溶体不同的是，随机固溶体的刚度随着 Al 含量的降低而单调增加，有序构型表现出非单调趋势，在 Mo30Cr30Ti30Al10 合金中达到峰值。 这种增强归因于强短程有序引起的刚性原子对的优化群体。这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。
**讨论重点：** 这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 8. RuNNer 2.0: A Software Suite for High-Dimensional Neural Network Potentials

- Source: arXiv
- Date: 2026-07-20T14:13:35Z
- Venue: physics.chem-ph, cond-mat.mtrl-sci, physics.comp-ph
- Authors: Alexander L. M. Knoll, Moritz R. Schäfer, K. Nikolas Lausch, Moritz Gubler, Henry Wang, Richard Springborn
- Link: https://arxiv.org/abs/2607.17978v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局域电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。优化的内存管理策略消除了传统上与远程交互相关的训练开销，从而使 4G-HDNNP 能够以与本地对应物相同的效率进行训练。 RuNNer 2.0 采用现代 Fortran（2003/2008 标准）开发，结合​​混合 MPI/OpenMP 并行化方案，旨在在任何 CPU 环境（从经济高效的本地工作站到大规模 HPC 集群）中高效运行。其模块化库架构有助于直接绑定到外部模拟软件； LAMMPS 和原子仿真环境 (ASE) 的本机接口提供对其所有功能的完全访问，包括内置的基于委员会的不确定性量化。 RuNNer 2.0生态系统的高效率和可扩展性通过详细的基准测试得到证明。
**讨论重点：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局域电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. Are Machine Learning Interatomic Potentials Truly Practical? A Benchmark of 23 Mainstream Models

- Source: arXiv
- Date: 2026-07-08T17:04:42Z
- Venue: cond-mat.mtrl-sci, cs.CE, physics.comp-ph
- Authors: Hanwen Kang, Tenglong Lu, Sheng Meng, Miao Liu
- Link: https://arxiv.org/abs/2607.07647v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。我们评估三个维度：预测准确性、MD 模拟吞吐量和原子可扩展性。 我们的结果揭示了精确度与效率之间的巨大权衡：大型 SOTA 模型的精确度仅比轻量级模型高出 3-5 meV/atom，但吞吐量却损失了几个数量级——在最坏的情况下，仅比 DFT 本身快一点点。相比之下，轻量级 MLIP 位于帕累托前沿并在适度的硬件上运行。教训是，一维基准会误导该领域，未来的 MLIP 开发应该重视效率和可扩展性以及准确性。
**讨论重点：** 我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 10. MLIP Studio: An Open Platform for Interactive Benchmarking and Atomistic Simulations Using Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-08T16:23:57Z
- Venue: cond-mat.mtrl-sci
- Authors: Manas Sharma, Sudeep Punnathanam, Ananth Govind Rajan
- Link: https://arxiv.org/abs/2607.07606v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 通用机器学习原子间势（MLIP）是改变原子模拟的基础人工智能模型，但其实际使用仍然受到分散的软件生态系统、依赖性冲突和缺乏可用的基准测试工具的阻碍。这些模型以一小部分计算成本实现了第一原理密度泛函理论 (DFT) 的精度。我们推出了 MLIP Studio（可在 https://mlipstudio.iisc.ac.in 获取），这是一个开放且免费的平台，可将 60 多种通用 MLIP 引入分子和材料的统一交互界面中。 该平台支持端到端 MLIP 驱动的工作流程，包括属性预测、几何优化、振动和状态方程分析、自旋状态确定、自定义模型部署以及针对参考数据的高通量基准测试。自动奇偶图和可排序误差表有助于快速识别元素异常值和有问题的数据点。我们证明基于 MLIP 的预优化可以减少后续 DFT 优化工作约 33$\times$。此外，该应用程序还可以对计算性能进行基准测试。 通过涉及蓝宝石基板上的二维磁性材料 CrCl$_3$ 的综合案例研究，我们展示了各种属性和势能景观的跨模型比较如何指导特定任务的 MLIP 选择。总体而言，MLIP Studio 降低了在计算化学和材料科学的端到端研究工作流程、基准测试和教育中可靠使用基础模型的障碍。
**讨论重点：** 我们推出了 MLIP Studio（可在 https://mlipstudio.iisc.ac.in 获取），这是一个开放且免费的平台，可将 60 多种通用 MLIP 引入分子和材料的统一交互界面中。通过涉及蓝宝石基板上的二维磁性材料 CrCl$_3$ 的综合案例研究，我们展示了各种属性和势能景观的跨模型比较如何指导特定任务的 MLIP 选择。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Emergent Surface Altermagnetism

- Source: arXiv
- Date: 2026-08-06T02:13:02Z
- Venue: cond-mat.mtrl-sci
- Authors: Yuzhong Hu, Pan Zhou, Baoru Pan, Songmin Liu, Binchang Zhou, Lizhong Sun
- Link: https://arxiv.org/abs/2608.05529v1
- Score: 27.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 迄今为止，交变磁性的研究主要集中在磁性材料中的自旋极化体电子态。在这项工作中，我们通过引入表面交变磁体（SAM）的概念来推进该领域，其中交变磁体自旋极化出现在共线反铁磁体（AFM）或交变磁体（AM）的表面。为了为这种现象奠定理论基础，我们构建了一个彻底的基于对称的框架，该框架系统地将两种类型系统的体自旋群与表面自旋群连接起来。 通过对称性分析，我们确定了所有能够支持 SAM 的对称破缺表面，确定了 35 个 $PT$ 对称 AFM 和 61 个体 AM 的不同情况。此外，我们还表明，203 个共线自旋空间群（包括 100 个不使用 $[C_2 \Vert P]$ 操作的共线自旋空间群和 103 个使用 $[C_2 \Vert P]$ 操作）允许通过分数平移对称性的破缺在 $tT$ 对称 AFM 的表面上出现 SAM。 所提出的框架使用紧束缚模型和第一原理计算进行了验证，并在 NaMnP、LiMnAs 和 CrSb 等代表性化合物中展示了实际材料的实现。我们的研究结果将 SAM 确立为一种强大的、对称保护的磁态，将交变磁现象扩展到材料表面，并为下一代自旋电子技术中先进的无场自旋操纵铺平了道路。
**讨论重点：** 为了为这种现象奠定理论基础，我们构建了一个彻底的基于对称的框架，该框架系统地将两种类型系统的体自旋群与表面自旋群连接起来。在这项工作中，我们通过引入表面交变磁体（SAM）的概念来推进该领域，其中交变磁体自旋极化出现在共线反铁磁体（AFM）或交变磁体（AM）的表面。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Emergence and Detection of Surface altermagnetism in KV$_2$Se$_2$O

- Source: arXiv
- Date: 2026-08-04T12:23:23Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: Rodrigo Jaeschke-Ubiergo, Xanthe H. Verbeek, Colin Lange, Sergio Rodriguez, Atasi Chakraborty, Alexander Mook
- Link: https://arxiv.org/abs/2608.03551v1
- Score: 26.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们通过 \KVSO 中独特的签名展示了新兴表面交变磁力的最新概念。我们表明，对于块体反铁磁有序 \KVSO，(001) 表面表现出 $d$ 波交变磁性。我们的结果充分解释了最近看似矛盾的实验证据，独立地显示了中子衍射中的反铁磁有序体和光电发射光谱中的 $d$ 波自旋分裂。 为了充分验证这一概念，我们预测作为关键实验特征的大型非线性 Edelstein 响应，该响应位于表面，并遵循 $d$ 波交磁对称性。这些结果不仅与金属和室温磁体 \KVSO 相关，而且还与其他几种利布晶格系统相关。我们的工作扩大了可用于检测反铁磁体表面出现的交变磁性的技术库。
**讨论重点：** 我们通过 \KVSO 中独特的签名展示了新兴表面交变磁力的最新概念。我们表明，对于块体反铁磁有序 \KVSO，(001) 表面表现出 $d$ 波交变磁性。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Correlated topological-polarization surface states in the narrow-gap insulator FeSb2

- Source: arXiv
- Date: 2026-08-06T11:11:43Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: Takahiro Iwagaki, Hideki Matsuoka, Ginta Hoshino, Kanata Watanabe, Shungo Aoyagi, Shunsuke Kitou
- Link: https://arxiv.org/abs/2608.05887v1
- Score: 17.0
- Match: 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 强电子相关性和能带拓扑都产生丰富的量子相，但相互冲突的元素要求在很大程度上使它们分开。拓扑极化提供了一种将它们结合起来的途径，在没有自旋轨道耦合的情况下从键合电荷产生极性表面态，从而将能带拓扑扩展到相关的 3d 过渡金属化合物。在这里，我们证明了窄间隙绝缘体 FeSb2 的外延薄膜具有拓扑极化起源的金属极性表面态，受块体的强相关性控制。 非互易表面传输仅出现在相关驱动的大块 Fe 3d 轨道占据重建的起始温度以下，提供了相关拓扑系统中大块边缘对应的直接证据。此外，静电门控驱动该相关表面通过量子相变进入铁磁态或可能的交磁态。我们的结果将拓扑极化确立为各种材料中相关拓扑相的设计原则。
**讨论重点：** 我们的结果将拓扑极化确立为各种材料中相关拓扑相的设计原则。拓扑极化提供了一种将它们结合起来的途径，在没有自旋轨道耦合的情况下从键合电荷产生极性表面态，从而将能带拓扑扩展到相关的 3d 过渡金属化合物。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Superconducting and charge-ordered phases from Dirac quantum spin liquids on the triangular lattice

- Source: arXiv
- Date: 2026-08-05T18:00:01Z
- Venue: cond-mat.str-el, cond-mat.supr-con
- Authors: Andreas Feuerpfeil, Ronny Thomale, Subir Sachdev, Pietro M. Bonetti
- Link: https://arxiv.org/abs/2608.05277v1
- Score: 17.0
- Match: 标题匹配 quantum spin liquid; 最近 3 天发布

**中文摘要：** 三角晶格量子自旋液体绝缘体被观察到在压力或掺杂下经历超导转变，并在中红外光驱动时表现出增强的太赫兹电导率。我们提出了一个通用理论框架，用于从具有费米子自旋子的 U(1) 狄拉克自旋液体及其带隙 $\mathbb{Z}_2$ 和手性后代中出现超导和电荷有序相。数值研究为这些自旋液体状态提供了实质性证据。 自旋液相具有与新兴规范场耦合的分段狄拉克自旋子，而超导相和电荷有序相是传统的，既没有分段激励，也没有新兴规范动力学。这些相之间的转变是由无自旋电荷 $e$ 玻色子（“双布朗”和“完整子”）的希格斯凝聚驱动的。我们证明，狄拉克自旋子的射影对称群唯一地决定了电荷的对称性和色散，使我们能够在电荷带极小值附近构建有效的低能理论。 chargon 希格斯场的规范不变复合提供了表征相的序参数。所得相图包含丰富多样的有序态，包括 $d+id$ 超导性、电荷密度波、键密度波和对密度波。
**讨论重点：** 我们提出了一个通用理论框架，用于从具有费米子自旋子的 U(1) 狄拉克自旋液体及其带隙 $\mathbb{Z}_2$ 和手性后代中出现超导和电荷有序相。数值研究为这些自旋液体状态提供了实质性证据。 结合关键词看，阅读时应重点关注量子自旋液体相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 5. Lifting the degeneracy of quantum spin liquid phase by uniaxial pressure

- Source: arXiv
- Date: 2026-08-05T12:49:04Z
- Venue: cond-mat.str-el
- Authors: Shams Sohel Islam, Zurab Guguchia, Orion Gerguri, Petr Král, Maxime Lamotte, Toni Shiroka
- Link: https://arxiv.org/abs/2608.04782v1
- Score: 17.0
- Match: 标题匹配 quantum spin liquid; 最近 3 天发布

**中文摘要：** 我们报告了候选三维（3D）量子自旋液体（QSL）PbCuTe$_2$O$_6$的μ子自旋弛豫/旋转（$μ$SR）测量，其承载$S=1/2$矩，在受控原位[110]单轴压缩下高达$σ_{[110]}=37.7$~MPa。小的方向晶格扰动会显着改变局部磁响应，而在 $σ_{\rm cr}\sim10.8$\,MPa 以上时，弛豫率会大大增强，内场分布也会显着拓宽。这些变化随着局部晶体对称性破缺而发生。 虽然没有观察到传统静态长程磁序的证据，但压缩驱动系统走向结构修改和强相关状态，其中增强的准静态相关性与持续的慢自旋动力学共存。这项工作展示了一种干净且对称选择性的路线，可以控制受挫的​​交换景观并访问 3D QSL 候选物中隐藏的磁不稳定性，从而为调整其他相关系统提供了可能性，其中磁自由度和晶格自由度之间的内在耦合是相关的。
**讨论重点：** 我们报告了候选三维（3D）量子自旋液体（QSL）PbCuTe$_2$O$_6$的μ子自旋弛豫/旋转（$μ$SR）测量，其承载$S=1/2$矩，在受控原位[110]单轴压缩下高达$σ_{[110]}=37.7$~MPa。小的方向晶格扰动会显着改变局部磁响应，而在 $σ_{\rm cr}\sim10.8$\,MPa 以上时，弛豫率会大大增强，内场分布也会显着拓宽。 结合关键词看，阅读时应重点关注量子自旋液体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 6. Pressure-Tunable Electronic and Magnonic Transport in Altermagnet La$_2$O$_3$Mn$_2$Se$_2$

- Source: arXiv
- Date: 2026-08-04T19:41:54Z
- Venue: cond-mat.mtrl-sci
- Authors: Nafise Rezaei, Alireza Qaiumzadeh, Artem R. Oganov, Mojtaba Alaei
- Link: https://arxiv.org/abs/2608.04184v1
- Score: 16.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 静水压力为设计相关绝缘交变磁体 La$_2$O$_3$Mn$_2$Se$_2$ 中的电子和磁子传输提供了一条保持对称性的途径。使用第一性原理计算与自旋哈密尔顿模型相结合，我们发现从 0 到 40 GPa 的压缩显着增强了竞争性第二邻域交换相互作用之间的不等价性，将 $|J_{2a}-J_{2b}|$ 从 1.97 meV 增加到 9.38 meV，同时保留补偿的反铁磁基态。 由此产生的交换各向异性放大了两个手性磁振子分支之间的动量依赖性分裂，使 100 K 时纵向磁振子驱动的自旋塞贝克响应增强了近四倍，从 3.68\times10^{-1}$ 到 1.36$ meV/K。相比之下，静水压力保留了控制反常霍尔效应的磁对称选择规则，同时重新分布电子贝里曲率，在反常霍尔电导率中产生明显的能量相关符号反转。 这些结果将交换各向异性确定为压力增强磁振子响应的微观机制，并将静水压力确定为同时控制绝缘交变磁体中电子和磁子传输的有效手段。
**讨论重点：** 静水压力为设计相关绝缘交变磁体 La$_2$O$_3$Mn$_2$Se$_2$ 中的电子和磁子传输提供了一条保持对称性的途径。使用第一性原理计算与自旋哈密尔顿模型相结合，我们发现从 0 到 40 GPa 的压缩显着增强了竞争性第二邻域交换相互作用之间的不等价性，将 $|J_{2a}-J_{2b}|$ 从 1.97 meV 增加到 9.38 meV，同时保留补偿的反铁磁基态。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 7. Accelerated quantum Monte Carlo simulations of the attractive Hubbard model on the kagome lattice

- Source: arXiv
- Date: 2026-08-04T16:26:51Z
- Venue: cond-mat.str-el
- Authors: Jie Zhang, Xiang Li, Yu Wang
- Link: https://arxiv.org/abs/2608.03894v1
- Score: 16.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 最近发现的几个 kagome 材料家族和光学 kagome 晶格的实验实现刺激了对 kagome 晶格上相互作用驱动的相关态的数值研究。在可用的数值方法中，行列式量子蒙特卡罗 (DQMC) 是研究此类强相关态的强大方法。然而，现有 DQMC 模拟的可访问系统规模仍然有限，无法进行可靠的有限规模缩放分析。 在这里，我们开发了一种基于快速傅立叶变换 (FFT) 的通用加速方案，用于复合晶格上的传播器乘法，并将其与延迟更新算法相结合，能够对两倍于之前 DQMC 研究的系统尺寸进行仿真，从而能够对有吸引力的 kagome-lattice Hubbard 模型进行可靠的有限尺寸缩放分析。我们的大规模模拟揭示了狄拉克填充时相互作用驱动的零温超流体量子临界性，并提供了相关临界指数的可靠估计。 此外，我们没有发现任何证据表明先前提出的三角规则电荷密度波阶在热力学极限下仍然存在，这表明它可能是有限尺寸效应。此外，对于当前二维光学晶格实验中可访问的系统尺寸，组合的 FFT 和延迟更新方案表现出有效的计算成本缩放为 $N^{2.49}$，大大低于传统 DQMC 模拟的 $\mathcal{O}(N^3)$ 计算成本。
**讨论重点：** 在这里，我们开发了一种基于快速傅立叶变换 (FFT) 的通用加速方案，用于复合晶格上的传播器乘法，并将其与延迟更新算法相结合，能够对两倍于之前 DQMC 研究的系统尺寸进行仿真，从而能够对有吸引力的 kagome-lattice Hubbard 模型进行可靠的有限尺寸缩放分析。在可用的数值方法中，行列式量子蒙特卡罗 (DQMC) 是研究此类强相关态的强大方法。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 8. A table-top few-femtosecond broadband extreme-ultraviolet absorption spectrometer with cryogenic cooling

- Source: arXiv
- Date: 2026-08-04T17:20:42Z
- Venue: physics.ins-det, cond-mat.mtrl-sci
- Authors: Sheng-Chih Lin, Alfred Zong, Emma Berger, Bailey R. Nebgen, Marcus Hui, Shuaiwei Pan
- Link: https://arxiv.org/abs/2608.03955v1
- Score: 15.0
- Match: 摘要匹配 strongly correlated systems; 摘要匹配 multiferroic; 最近 3 天发布

**中文摘要：** 我们提出了一种台式低温超快宽带 XUV 吸收光谱 (c-UBXAS) 光束线，专为量子材料的温度依赖性和时间分辨研究而设计。该仪器将跨越 22-73 eV 的宽带高次谐波发生源与自动图像配准和低至 20 K 的低温样品控制相结合，从而能够在平衡和非平衡条件下进行元素特定测量。 该光束线提供低于 50 meV 的能量分辨率和低于 10 fs 的仪器响应函数，同时保持适合扩展、超灵敏测量的长期稳定性。 NiI$_2$（一种范德华多铁性材料）的基准实验揭示了其磁相变中与温度相关的光谱演化，证明了识别特定元素对基态的贡献及其在飞秒范围内瞬态响应的能力。 该仪器提供了解开固态材料在光与物质相互作用过程中的第一个响应的机会，为理解强相关系统中非平衡动力学和涌现状态的复杂相空间铺平了道路，在这些系统中，几飞秒的电子响应已经避开了大多数其他类型的时间分辨技术。
**讨论重点：** 我们提出了一种台式低温超快宽带 XUV 吸收光谱 (c-UBXAS) 光束线，专为量子材料的温度依赖性和时间分辨研究而设计。 NiI$_2$（一种范德华多铁性材料）的基准实验揭示了其磁相变中与温度相关的光谱演化，证明了识别特定元素对基态的贡献及其在飞秒范围内瞬态响应的能力。 结合关键词看，阅读时应重点关注强关联体系、多铁性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 9. Antisymmetric Dynamical Spin Correlations: Spin-Space-Group Constraints and Frequency-Moment Sum Rules

- Source: arXiv
- Date: 2026-08-04T15:05:04Z
- Venue: cond-mat.str-el
- Authors: Tsutomu Momoi
- Link: https://arxiv.org/abs/2608.03786v1
- Score: 15.0
- Match: 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 偏振非弹性中子散射通过动态自旋结构因子张量的自旋分量反对称部分探测磁激发的旋向性。我们推导了磁空间群和自旋空间群的酉和反酉剩余运算下的对称约束。这些约束决定了允许的张量分量、它们在动量反转下的奇偶性以及强制对称的节点。然后，我们引入相应的反对称换向器谱函数，并推导出其频率矩的精确零温和规则。 零阶矩由均匀磁化固定。对于海森堡或 XXZ 交换哈密顿量，$xy$ 分量的一阶矩由动量加权静态矢量手性固定。对于补偿共线反铁磁体，当反演或平移涉及相反自旋子晶格时，反对称动态结构因子被禁止。然而，在与旋转相关的交流磁体中，即使在动量反转的情况下，通用波矢量也允许存在 $xy$ 分量。 因此，有限反对称谱权可以与换向器谱函数的零阶矩和一阶矩消失共存。相比之下，在平面螺旋中，残余反酉自旋空间群对称性使得动量反转下允许的 $xy$ 分量为奇数。它的一阶矩通常不为零，并且通过一阶矩和规则由动量加权静态矢量手性固定。代表性交变磁模型和螺旋模型的线性自旋波计算明确地实现了这些对称性和求和规则约束。
**讨论重点：** 然后，我们引入相应的反对称换向器谱函数，并推导出其频率矩的精确零温和规则。我们推导了磁空间群和自旋空间群的酉和反酉剩余运算下的对称约束。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 10. Phonon spectral functions of low-density polaron metals

- Source: arXiv
- Date: 2026-08-06T17:55:23Z
- Venue: cond-mat.str-el
- Authors: Luis Walther, Alberto Nocera, Mona Berciu
- Link: https://arxiv.org/abs/2608.06357v1
- Score: 14.0
- Match: 摘要匹配 density matrix renormalization group; 最近 3 天发布

**中文摘要：** 我们使用密度矩阵重正化群 (DMRG) 来计算掺杂有低但有限载流子浓度 $x \leq 0.15$ 的一维无自旋荷斯坦模型的声子谱函数，作为电子声子耦合 $λ$ 的函数。据我们所知，这是该机制中的第一个此类结果，补充了单极化子水平（$x\to 0$）的广泛先前工作。 我们发现显着的声子谱权重转移到下面，一直向下到 $ω=0$，以及裸声子能量 $Ω$ 之上，与 Migdal 极限中预期的 Kohn 异常现象形成鲜明对比，其中权重仍然集中在 $Ω$ 附近，并在 $q=2k_F$ 处扭结。我们的结果中没有出现此 $2k_F$ 问题的签名。 这种行为可以通过随机相位近似 (RPA) 定性地捕获，而可以通过“修饰的 RPA”方案以可忽略的额外计算成本进行半定量捕获，其中使用低密度电子极化子的动量平均 (MA) 近似对电子加法传播器进行重新归一化。相比之下，向该修饰方案添加最低阶顶点校正会产生非物理负谱权重，这表明一旦传播器被非扰动地修饰，则必须一致地处理顶点和传播器修饰。 我们的结果为低密度极化子金属的声子谱函数提供了有效的近似，该函数与弱掺杂绝缘体相关。
**讨论重点：** 我们使用密度矩阵重正化群 (DMRG) 来计算掺杂有低但有限载流子浓度 $x \leq 0.15$ 的一维无自旋荷斯坦模型的声子谱函数，作为电子声子耦合 $λ$ 的函数。据我们所知，这是该机制中的第一个此类结果，补充了单极化子水平（$x\to 0$）的广泛先前工作。 结合关键词看，阅读时应重点关注密度矩阵重整化群相关的研究对象、方法假设、关键参数、数据来源，以及结果能否迁移到相邻材料或物理体系。
