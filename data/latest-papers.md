# Latest papers for 程旭丽

Updated: 2026-08-06T10:15:43.404531+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. An Exchange-Correlation Functional for Fast and Accurate Modeling of Ferroelectric Perovskites

- Source: arXiv
- Date: 2026-08-05T13:12:10Z
- Venue: cond-mat.mtrl-sci
- Authors: Owain T. Beynon, Chiara Gattinoni
- Link: https://arxiv.org/abs/2608.04806v1
- Score: 14.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 我们提出了一种新颖的交换关联泛函 C09x-PBEc，它将 C09 交换与 PBE 关联相结合，可以准确地模拟钙钛矿的铁电特性，同时保留 GGA 泛函的计算效率。随着人们对开发机器学习原子间势 (MLIP) 来模拟具有技术相关性的大规模铁电系统的兴趣日益浓厚，仔细研究用于计算 MLIP 训练的力、能量和应力的密度泛函理论交换相关函数非常重要。 以典型铁电体钛酸铅、PbTiO3 和钛酸钡、BaTiO3 为例，我们表明许多广泛使用的泛函往往会高估其晶格常数和自发极化。相反，与实验相比，具有 C09 交换的非局域范德华函数可以准确地捕获这些属性，但计算开销比 GGA 等更大。 我们证明，C09x-PBEc 将 C09 交换提供的精度与 GGA 的计算承受能力相结合，使其成为用于铁电钙钛矿 MLIP 训练的绝佳候选者。我们还证明，使用 C09x-PBEc 训练的 MLIP 在实验中准确再现了 PbTiO3 的铁电到顺电相变温度，表明使用 GGA 训练的 MLIP 有了显着的改进。
**讨论重点：** 我们提出了一种新颖的交换关联泛函 C09x-PBEc，它将 C09 交换与 PBE 关联相结合，可以准确地模拟钙钛矿的铁电特性，同时保留 GGA 泛函的计算效率。随着人们对开发机器学习原子间势 (MLIP) 来模拟具有技术相关性的大规模铁电系统的兴趣日益浓厚，仔细研究用于计算 MLIP 训练的力、能量和应力的密度泛函理论交换相关函数非常重要。 结合关键词看，阅读时应重点关注机器学习原子间势相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 2. Ultrafast Nonthermal Lattice Destabilization and Suppression of Polar Optical Scattering in Electronically Excited $α$-SiO$_2$ from First-Principles and Deep Neural Network Potential Modeling

- Source: arXiv
- Date: 2026-07-30T21:04:07Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Iyyappa Rajan Panneerselvam, Mark Yeung, Charlotte Palmer, Brendan Dromey, Lorenzo Stella
- Link: https://arxiv.org/abs/2607.28838v1
- Score: 12.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。使用 DNNP 可以对具有数千个原子的大型 $α$-SiO$_2$ 单元进行接近 DFT 精度的原子建模。 特别是，DNNP 使我们能够获得由电子温度突然升高激发的 $α$-SiO$_2$ 的精确声子能带结构和分子动力学 (MD)。随着电子温度 $T_e$ 的增加，发现 $α$-SiO$_2$ 出现明显的晶格失稳，表现为违反弹性稳定性标准、体积大幅膨胀、体积模量急剧下降以及由于反键态占据而导致 Si-O 键逐渐减弱。 根据电子和声子能带结构，我们估计了 Frohlich 耦合常数，该常数随着 $T_e$ 的增加而减小，表明在电子温度升高时会交叉到 $α$-SiO$_2$ 的非极性相。 Bader 电荷分析证实了这一点。我们还建议在 $T_e > 2$ eV 时应强烈抑制极性光学声子散射。从大单元 DNNP-MD 模拟中，我们表明，在最初的几百飞秒内，并未实现由麦克斯韦-玻尔兹曼分布定义的明确热平衡。 这种行为解释了 $T_e$ 突然上升后动力学温度的非单调平衡。当 $T_e$ 升至 2.6 eV 后，Si 和 O 原子首先在两个不同的温度下分别达到平衡，表明存在原子流体相，这与最近的实验和理论发现一致。
**讨论重点：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 3. PASS: Perturbation augmented space group structure sampling for transferable Fe-O machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-30T10:48:01Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Zixiong Wei, Fei Shuang, Poulumi Dey
- Link: https://arxiv.org/abs/2607.28000v1
- Score: 12.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 铁（Fe）氧化的准确原子建模需要可靠的原子间势，这需要广泛且具有代表性的第一性原理数据集来训练原子间势。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。 我们提出了一种系统方法，基于原子团簇扩展 (ACE) 框架，为 Fe-O 系统开发首个可转移机器学习原子间势 (MLIP)。我们通过体积、表面和界面特性彻底验证了 ACE MLIP 在纯 Fe 和 Fe-O 系统中的准确性和功能。我们展示了使用 ACE MLIP 大规模 Fe 氧化模拟中 FeO 类结构的形成。 这项工作表明，PASS 方法产生了准确且可转移的 MLIP，它能够捕获氧化物生长的反应复杂性，同时保持扩展系统的计算实用性。
**讨论重点：** 在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 4. Extracting Atomic Environments for Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-28T17:28:41Z
- Venue: cond-mat.mtrl-sci
- Authors: Jared C. Stimac, Fei Zhou, Kyle Bushick, Bo Lei, Sebastien Hamel, Amit Samanta
- Link: https://arxiv.org/abs/2607.26018v2
- Score: 10.0
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
- Match: 标题匹配 neural network potential; 近两周发布

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

### 1. Emergence and Detection of Surface altermagnetism in KV$_2$Se$_2$O

- Source: arXiv
- Date: 2026-08-04T12:23:23Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: Rodrigo Jaeschke-Ubiergo, Xanthe H. Verbeek, Colin Lange, Sergio Rodriguez, Atasi Chakraborty, Alexander Mook
- Link: https://arxiv.org/abs/2608.03551v1
- Score: 27.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们通过 \KVSO 中独特的签名展示了新兴表面交变磁力的最新概念。我们表明，对于块体反铁磁有序 \KVSO，(001) 表面表现出 $d$ 波交变磁性。我们的结果充分解释了最近看似矛盾的实验证据，独立地显示了中子衍射中的反铁磁有序体和光电发射光谱中的 $d$ 波自旋分裂。 为了充分验证这一概念，我们预测作为关键实验特征的大型非线性 Edelstein 响应，该响应位于表面，并遵循 $d$ 波交磁对称性。这些结果不仅与金属和室温磁体 \KVSO 相关，而且还与其他几种利布晶格系统相关。我们的工作扩大了可用于检测反铁磁体表面出现的交变磁性的技术库。
**讨论重点：** 我们通过 \KVSO 中独特的签名展示了新兴表面交变磁力的最新概念。我们表明，对于块体反铁磁有序 \KVSO，(001) 表面表现出 $d$ 波交变磁性。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Magnetically tunable symmetry-enforced nodal lines producing huge anomalous Hall conductivity in altermagnetic $α$-MnTe

- Source: arXiv
- Date: 2026-08-03T15:55:42Z
- Venue: cond-mat.mtrl-sci, cond-mat.other
- Authors: Mathews Benny, Xujia Gong, Amar Fakhredine, Raphaël Salazar, Ashutosh S. Wadge, Juraj Krempaský
- Link: https://arxiv.org/abs/2608.02416v1
- Score: 26.0
- Match: 摘要匹配 ferromagnetism; 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁 $α$-MnTe 在室温下表现出巨大的反常霍尔电导率 (AHC)，以及自旋和轨道极化产生的弱铁磁性。我们通过识别价带中具有 Mn 特征的两组不同的对称强制节点线来澄清 AHC 大值的起源，这些节点线位于 $k_z=0$ 和 $k_z=\fracπ{c}$ 处，分别受到镜像对称 $M_z$ 和滑移对称 $G_z = \{M_z\,|\,0,0,\tfrac{c}{2}\}$ 的保护。 两条节点线均与能量相关，具有近似 C$_6$ 对称性，由于 Néel 矢量的存在，该对称性被简化为精确的 C$_2$ 对称性。最高价带表现出墨西哥帽色散，而第二高价带表现出倒置墨西哥帽色散，在两个能带之间的交叉处具有节点线。在第一原理精度范围内，我们证明这些节点线会产生实验观察到的大 AHC，并表现出与弱铁磁性的强烈相互作用。 我们进一步表明，即使是很小的自旋倾斜也会强烈改变节点线和 AHC，使它们都具有磁性可调。通过解开 AHC 中的交磁和铁磁贡献，交磁贡献在小倾斜角度下占主导地位，而铁磁贡献在较大的角度下变得相当大。利用角度分辨光电子光谱中的线性二色性，我们显示了布里渊区边界处的节点线的特征。
**讨论重点：** 交变磁 $α$-MnTe 在室温下表现出巨大的反常霍尔电导率 (AHC)，以及自旋和轨道极化产生的弱铁磁性。我们通过识别价带中具有 Mn 特征的两组不同的对称强制节点线来澄清 AHC 大值的起源，这些节点线位于 $k_z=0$ 和 $k_z=\fracπ{c}$ 处，分别受到镜像对称 $M_z$ 和滑移对称 $G_z = \{M_z\,|\,0,0,\tfrac{c}{2}\}$ 的保护。 结合关键词看，阅读时应重点关注铁磁性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Symmetry-Guided Computational Screening of Two-Dimensional Altermagnets with ab initio Hubbard Corrections

- Source: arXiv
- Date: 2026-08-03T22:24:24Z
- Venue: cond-mat.mtrl-sci
- Authors: Anumita Bose, Nataliia Manko, Marco Gibertini, Antimo Marrazzo
- Link: https://arxiv.org/abs/2608.02925v1
- Score: 25.0
- Match: 摘要匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 摘要匹配 altermagnetic materials

**中文摘要：** 交变磁体将补偿反铁磁序与动量相关的自旋分裂相结合，为自旋电子应用提供了一个有前景的平台，无需宏观磁化或杂散磁场。尽管多种三维 (3D) 材料已被确定为交变磁体，但二维 (2D) 交变磁体仍然相对有限。在这项工作中，我们对 Materials Cloud 2D Crystals (MC2D) 数据库中的 2710 种材料进行了高通量计算搜索。 我们的方法将基于对称性的筛选与第一原理密度泛函理论计算相结合，包括自洽的 Hubbard-$U$ 校正，以可靠地捕获磁基态。通过对磁构型及其能量稳定性的系统探索，我们确定了 42 种材料，它们在至少一个 $U$ 值下表现出交变磁基态，其中 24 种在根据第一原理确定 Hubbard-$U$ 参数后仍然保持稳健，其中包括文献中先前报道的 4 种材料和新预测的 20 种候选材料。 这些包括有前途的单层，例如金属 Fe$_2$Si$_2$SbO$_9$ 和绝缘 CoBrO，自旋分裂分别约为 294 meV 和 330 meV。我们的结果显着扩大了具有良好剥落能量学的潜在二维交替磁体候选库，并为实验工作提供了宝贵的指导。此外，这项工作还建立了一个高通量计算框架，用于可重复地发现和表征互磁材料。
**讨论重点：** 我们的方法将基于对称性的筛选与第一原理密度泛函理论计算相结合，包括自洽的 Hubbard-$U$ 校正，以可靠地捕获磁基态。尽管多种三维 (3D) 材料已被确定为交变磁体，但二维 (2D) 交变磁体仍然相对有限。 结合关键词看，阅读时应重点关注交变磁性、交变磁性材料相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Exotic superconductivity in the doped Kitaev quantum spin liquid

- Source: arXiv
- Date: 2026-08-04T02:13:12Z
- Venue: cond-mat.str-el, cond-mat.supr-con
- Authors: Takahiro Misawa, Kota Ido
- Link: https://arxiv.org/abs/2608.03024v1
- Score: 22.0
- Match: 标题匹配 quantum spin liquid; 摘要匹配 unconventional superconductivity; 摘要匹配 ferromagnetism; 最近 3 天发布

**中文摘要：** 我们通过将多变量变分蒙特卡罗方法应用于空穴掺杂 $t$-$J$ 型 Kitaev 模型来研究掺杂 Kitaev 量子自旋液体中的超导性。使用可以精确表示基塔耶夫量子自旋液体的投影对积​​波函数，我们检查了各向同性二维团簇上超导相的稳定性。 对于铁磁基塔耶夫相互作用，鲁棒的三线态$p$波超导性与低到中度掺杂状态下的铁磁性共存，但当系统接近完全极化的铁磁相时，其受到抑制。对于反铁磁 Kitaev 相互作用，超导性表现出主要配对对称性的变化，从低掺杂的自旋相关三重态 $p$ 波到中等掺杂的单重态 $d+id$。 通过改变固定掺杂下铁磁基塔耶夫相互作用的强度，我们表明三重态超导性与铁磁矩一起增加，并在略低于完全极化的情况下变得最强。我们的研究结果为载流子掺杂基塔耶夫候选材料中非常规超导性的实验研究提供了理论基础，例如与铁磁性共存的三线态超导性。
**讨论重点：** 我们通过将多变量变分蒙特卡罗方法应用于空穴掺杂 $t$-$J$ 型 Kitaev 模型来研究掺杂 Kitaev 量子自旋液体中的超导性。使用可以精确表示基塔耶夫量子自旋液体的投影对积​​波函数，我们检查了各向同性二维团簇上超导相的稳定性。 结合关键词看，阅读时应重点关注量子自旋液体、非常规超导、铁磁性相关的样品制备、实验表征条件、关键观测信号，以及这些信号如何支撑物理机制解释。

### 5. Lifting the degeneracy of quantum spin liquid phase by uniaxial pressure

- Source: arXiv
- Date: 2026-08-05T12:49:04Z
- Venue: cond-mat.str-el
- Authors: Shams Sohel Islam, Zurab Guguchia, Orion Gerguri, Petr Král, Maxime Lamotte, Toni Shiroka
- Link: https://arxiv.org/abs/2608.04782v1
- Score: 18.0
- Match: 标题匹配 quantum spin liquid; 最近 3 天发布

**中文摘要：** 我们报告了候选三维（3D）量子自旋液体（QSL）PbCuTe$_2$O$_6$的μ子自旋弛豫/旋转（$μ$SR）测量，其承载$S=1/2$矩，在受控原位[110]单轴压缩下高达$σ_{[110]}=37.7$~MPa。小的方向晶格扰动会显着改变局部磁响应，而在 $σ_{\rm cr}\sim10.8$\,MPa 以上时，弛豫率会大大增强，内场分布也会显着拓宽。这些变化随着局部晶体对称性破缺而发生。 虽然没有观察到传统静态长程磁序的证据，但压缩驱动系统走向结构修改和强相关状态，其中增强的准静态相关性与持续的慢自旋动力学共存。这项工作展示了一种干净且对称选择性的路线，可以控制受挫的​​交换景观并访问 3D QSL 候选物中隐藏的磁不稳定性，从而为调整其他相关系统提供了可能性，其中磁自由度和晶格自由度之间的内在耦合是相关的。
**讨论重点：** 我们报告了候选三维（3D）量子自旋液体（QSL）PbCuTe$_2$O$_6$的μ子自旋弛豫/旋转（$μ$SR）测量，其承载$S=1/2$矩，在受控原位[110]单轴压缩下高达$σ_{[110]}=37.7$~MPa。小的方向晶格扰动会显着改变局部磁响应，而在 $σ_{\rm cr}\sim10.8$\,MPa 以上时，弛豫率会大大增强，内场分布也会显着拓宽。 结合关键词看，阅读时应重点关注量子自旋液体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 6. Pressure-Tunable Electronic and Magnonic Transport in Altermagnet La$_2$O$_3$Mn$_2$Se$_2$

- Source: arXiv
- Date: 2026-08-04T19:41:54Z
- Venue: cond-mat.mtrl-sci
- Authors: Nafise Rezaei, Alireza Qaiumzadeh, Artem R. Oganov, Mojtaba Alaei
- Link: https://arxiv.org/abs/2608.04184v1
- Score: 17.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 静水压力为设计相关绝缘交变磁体 La$_2$O$_3$Mn$_2$Se$_2$ 中的电子和磁子传输提供了一条保持对称性的途径。使用第一性原理计算与自旋哈密尔顿模型相结合，我们发现从 0 到 40 GPa 的压缩显着增强了竞争性第二邻域交换相互作用之间的不等价性，将 $|J_{2a}-J_{2b}|$ 从 1.97 meV 增加到 9.38 meV，同时保留补偿的反铁磁基态。 由此产生的交换各向异性放大了两个手性磁振子分支之间的动量依赖性分裂，使 100 K 时纵向磁振子驱动的自旋塞贝克响应增强了近四倍，从 3.68\times10^{-1}$ 到 1.36$ meV/K。相比之下，静水压力保留了控制反常霍尔效应的磁对称选择规则，同时重新分布电子贝里曲率，在反常霍尔电导率中产生明显的能量相关符号反转。 这些结果将交换各向异性确定为压力增强磁振子响应的微观机制，并将静水压力确定为同时控制绝缘交变磁体中电子和磁子传输的有效手段。
**讨论重点：** 静水压力为设计相关绝缘交变磁体 La$_2$O$_3$Mn$_2$Se$_2$ 中的电子和磁子传输提供了一条保持对称性的途径。使用第一性原理计算与自旋哈密尔顿模型相结合，我们发现从 0 到 40 GPa 的压缩显着增强了竞争性第二邻域交换相互作用之间的不等价性，将 $|J_{2a}-J_{2b}|$ 从 1.97 meV 增加到 9.38 meV，同时保留补偿的反铁磁基态。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 7. Accelerated quantum Monte Carlo simulations of the attractive Hubbard model on the kagome lattice

- Source: arXiv
- Date: 2026-08-04T16:26:51Z
- Venue: cond-mat.str-el
- Authors: Jie Zhang, Xiang Li, Yu Wang
- Link: https://arxiv.org/abs/2608.03894v1
- Score: 17.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 最近发现的几个 kagome 材料家族和光学 kagome 晶格的实验实现刺激了对 kagome 晶格上相互作用驱动的相关态的数值研究。在可用的数值方法中，行列式量子蒙特卡罗 (DQMC) 是研究此类强相关态的强大方法。然而，现有 DQMC 模拟的可访问系统规模仍然有限，无法进行可靠的有限规模缩放分析。 在这里，我们开发了一种基于快速傅立叶变换 (FFT) 的通用加速方案，用于复合晶格上的传播器乘法，并将其与延迟更新算法相结合，能够对两倍于之前 DQMC 研究的系统尺寸进行仿真，从而能够对有吸引力的 kagome-lattice Hubbard 模型进行可靠的有限尺寸缩放分析。我们的大规模模拟揭示了狄拉克填充时相互作用驱动的零温超流体量子临界性，并提供了相关临界指数的可靠估计。 此外，我们没有发现任何证据表明先前提出的三角规则电荷密度波阶在热力学极限下仍然存在，这表明它可能是有限尺寸效应。此外，对于当前二维光学晶格实验中可访问的系统尺寸，组合的 FFT 和延迟更新方案表现出有效的计算成本缩放为 $N^{2.49}$，大大低于传统 DQMC 模拟的 $\mathcal{O}(N^3)$ 计算成本。
**讨论重点：** 在这里，我们开发了一种基于快速傅立叶变换 (FFT) 的通用加速方案，用于复合晶格上的传播器乘法，并将其与延迟更新算法相结合，能够对两倍于之前 DQMC 研究的系统尺寸进行仿真，从而能够对有吸引力的 kagome-lattice Hubbard 模型进行可靠的有限尺寸缩放分析。在可用的数值方法中，行列式量子蒙特卡罗 (DQMC) 是研究此类强相关态的强大方法。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 8. A table-top few-femtosecond broadband extreme-ultraviolet absorption spectrometer with cryogenic cooling

- Source: arXiv
- Date: 2026-08-04T17:20:42Z
- Venue: physics.ins-det, cond-mat.mtrl-sci
- Authors: Sheng-Chih Lin, Alfred Zong, Emma Berger, Bailey R. Nebgen, Marcus Hui, Shuaiwei Pan
- Link: https://arxiv.org/abs/2608.03955v1
- Score: 16.0
- Match: 摘要匹配 strongly correlated systems; 摘要匹配 multiferroic; 最近 3 天发布

**中文摘要：** 我们提出了一种台式低温超快宽带 XUV 吸收光谱 (c-UBXAS) 光束线，专为量子材料的温度依赖性和时间分辨研究而设计。该仪器将跨越 22-73 eV 的宽带高次谐波发生源与自动图像配准和低至 20 K 的低温样品控制相结合，从而能够在平衡和非平衡条件下进行元素特定测量。 该光束线提供低于 50 meV 的能量分辨率和低于 10 fs 的仪器响应函数，同时保持适合扩展、超灵敏测量的长期稳定性。 NiI$_2$（一种范德华多铁性材料）的基准实验揭示了其磁相变中与温度相关的光谱演化，证明了识别特定元素对基态的贡献及其在飞秒范围内瞬态响应的能力。 该仪器提供了解开固态材料在光与物质相互作用过程中的第一个响应的机会，为理解强相关系统中非平衡动力学和涌现状态的复杂相空间铺平了道路，在这些系统中，几飞秒的电子响应已经避开了大多数其他类型的时间分辨技术。
**讨论重点：** 我们提出了一种台式低温超快宽带 XUV 吸收光谱 (c-UBXAS) 光束线，专为量子材料的温度依赖性和时间分辨研究而设计。 NiI$_2$（一种范德华多铁性材料）的基准实验揭示了其磁相变中与温度相关的光谱演化，证明了识别特定元素对基态的贡献及其在飞秒范围内瞬态响应的能力。 结合关键词看，阅读时应重点关注强关联体系、多铁性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 9. Antisymmetric Dynamical Spin Correlations: Spin-Space-Group Constraints and Frequency-Moment Sum Rules

- Source: arXiv
- Date: 2026-08-04T15:05:04Z
- Venue: cond-mat.str-el
- Authors: Tsutomu Momoi
- Link: https://arxiv.org/abs/2608.03786v1
- Score: 16.0
- Match: 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 偏振非弹性中子散射通过动态自旋结构因子张量的自旋分量反对称部分探测磁激发的旋向性。我们推导了磁空间群和自旋空间群的酉和反酉剩余运算下的对称约束。这些约束决定了允许的张量分量、它们在动量反转下的奇偶性以及强制对称的节点。然后，我们引入相应的反对称换向器谱函数，并推导出其频率矩的精确零温和规则。 零阶矩由均匀磁化固定。对于海森堡或 XXZ 交换哈密顿量，$xy$ 分量的一阶矩由动量加权静态矢量手性固定。对于补偿共线反铁磁体，当反演或平移涉及相反自旋子晶格时，反对称动态结构因子被禁止。然而，在与旋转相关的交流磁体中，即使在动量反转的情况下，通用波矢量也允许存在 $xy$ 分量。 因此，有限反对称谱权可以与换向器谱函数的零阶矩和一阶矩消失共存。相比之下，在平面螺旋中，残余反酉自旋空间群对称性使得动量反转下允许的 $xy$ 分量为奇数。它的一阶矩通常不为零，并且通过一阶矩和规则由动量加权静态矢量手性固定。代表性交变磁模型和螺旋模型的线性自旋波计算明确地实现了这些对称性和求和规则约束。
**讨论重点：** 然后，我们引入相应的反对称换向器谱函数，并推导出其频率矩的精确零温和规则。我们推导了磁空间群和自旋空间群的酉和反酉剩余运算下的对称约束。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 10. Large scale neural quantum states reveal the interplay between superconductivity and quantum criticality in the Hofstadter-Hubbard model

- Source: arXiv
- Date: 2026-08-03T18:01:16Z
- Venue: cond-mat.str-el, cond-mat.dis-nn, cond-mat.supr-con
- Authors: Christopher Roth, Andrew Millis, Tomohiro Soejima
- Link: https://arxiv.org/abs/2608.02753v1
- Score: 16.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 了解母体绝缘态如何塑造掺杂后出现的超导性是一个长期存在的问题，可以追溯到安德森的共振价键提议。每个小板具有 $π/2$ 通量的三角晶格 Hofstadter-Hubbard 模型为这个问题提供了一个理想的设置：在半填充时，它拥有两个不同的母态——弱耦合时的整数量子霍尔绝缘体和中间耦合时的手性自旋液体——通过拓扑相变分开。 在高达 432$ 的环面上使用神经量子态，我们提供了强有力的证据，证明过渡是连续的，$2e$ 电荷间隙和临界电荷波动消失。掺杂后，我们发现了一种具有非对角长程有序的拓扑超导体，与过渡两侧的 $d+id$ 配对一致。 超导性的两个组成部分，对形成和相位相干性，以截然不同的方式响应母态：虽然配对顺序参数在整个转变过程中几乎保持不变，但超流体刚度在临界点附近强烈增强。因此，超导体的能级不是由掺杂的母态决定的，而是由它们之间的过渡的接近程度决定的。我们的研究结果将神经量子态确立为理解长程电子相关性和超导性之间微妙相互作用的强大工具。
**讨论重点：** 在高达 432$ 的环面上使用神经量子态，我们提供了强有力的证据，证明过渡是连续的，$2e$ 电荷间隙和临界电荷波动消失。每个小板具有 $π/2$ 通量的三角晶格 Hofstadter-Hubbard 模型为这个问题提供了一个理想的设置：在半填充时，它拥有两个不同的母态——弱耦合时的整数量子霍尔绝缘体和中间耦合时的手性自旋液体——通过拓扑相变分开。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。
