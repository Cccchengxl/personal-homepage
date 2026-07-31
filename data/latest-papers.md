# Latest papers for 程旭丽

Updated: 2026-07-31T10:07:02.442430+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. PASS: Perturbation augmented space group structure sampling for transferable Fe-O machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-30T10:48:01Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Zixiong Wei, Fei Shuang, Poulumi Dey
- Link: https://arxiv.org/abs/2607.28000v1
- Score: 18.0
- Match: 标题匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 铁（Fe）氧化的准确原子建模需要可靠的原子间势，这需要广泛且具有代表性的第一性原理数据集来训练原子间势。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。 我们提出了一种系统方法，基于原子团簇扩展 (ACE) 框架，为 Fe-O 系统开发首个可转移机器学习原子间势 (MLIP)。我们通过体积、表面和界面特性彻底验证了 ACE MLIP 在纯 Fe 和 Fe-O 系统中的准确性和功能。我们展示了使用 ACE MLIP 大规模 Fe 氧化模拟中 FeO 类结构的形成。 这项工作表明，PASS 方法产生了准确且可转移的 MLIP，它能够捕获氧化物生长的反应复杂性，同时保持扩展系统的计算实用性。
**讨论重点：** 在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 2. Extracting Atomic Environments for Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-28T17:28:41Z
- Venue: cond-mat.mtrl-sci
- Authors: Jared C. Stimac, Fei Zhou, Kyle Bushick, Bo Lei, Sebastien Hamel, Amit Samanta
- Link: https://arxiv.org/abs/2607.26018v1
- Score: 16.0
- Match: 标题匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 为了通过原子模拟（例如分子动力学（MD））适当捕获大规模材料特征和突发现象，系统规模可以达到数亿个原子。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 为了计算感兴趣区域中原子上的 DFT 力，例如用于原子间势的主动学习或动态训练，需要从较大的模拟框中提取一小组原子，并且需要使用 DFT 的周期性边界条件进行典型工作；然而，尚未系统地分析选择这组提取的原子的形状和大小以及生成潜在必要的钝化包络的方法。 在这项工作中，我们提出了各种技术的基准，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。我们使用多种材料系统进行测试，其中包括无定形 $\mathrm{SiO_2}$、具有螺旋位错的 Ta 和熔融 C。我们演示了一种非常简单的程序（我们称为删除的方法），其性能优于一系列替代提取方法。
**讨论重点：** 在这项工作中，我们提出了各种技术的基准，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。我们演示了一个非常简单的过程，我们称之为删除的方法，与一系列替代提取方法相比具有优越的性能。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 3. Charge-Density-Wave Phase Transitions in Monolayer 1T-TaS2 from Universal Machine Learning Molecular Dynamics

- Source: arXiv
- Date: 2026-07-24T13:57:09Z
- Venue: cond-mat.mtrl-sci
- Authors: Valentina Nesterova, Tribhuwan Pandey, Tom Berlijn, Fariborz Kargar, Lucas Lindsay, Konstantin Klyukin
- Link: https://arxiv.org/abs/2607.22316v1
- Score: 12.0
- Match: 标题匹配 machine learning molecular dynamics; 近两周发布

**中文摘要：** 1T 过渡金属二硫属化物中的电荷密度波 (CDW) 相是由强电子声子耦合和伴随的晶格不稳定性产生的。由于需要大型超级电池和广泛的有限温度采样，使用传统的第一原理分子动力学 (MD) 捕获其随温度变化的结构演化仍然具有挑战性。 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。针对 DFT 位移能量的基准测试确定了 UMA-s-1p1 通用机器学习潜力，具有足够的精度用于后续的有限温度模拟。 我们的结果表明，大规模 MD 模拟再现了实验观察到的从低温大卫之星 (SoD) 扭曲结构到高温原始六边形结构的相变序列，通过归因于 SoD 的 Ta 原子数量来量化。加热-冷却循环表现出热滞后，并且在冷却时，系统冻结成多域状态，其中α和\b{eta} CDW手性独立成核并持续到最低温度。 这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。
**讨论重点：** 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。 结合关键词看，阅读时应重点关注机器学习分子动力学相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 4. A high-dimensional neural network potential for finite-temperature phenomena in NiTi martensite

- Source: arXiv
- Date: 2026-07-22T19:32:23Z
- Venue: cond-mat.mtrl-sci
- Authors: Petr Jaroš, Petr Sedlák, Petr Šesták, Miroslav Černý, Jörg Behler, Hanuš Seiner
- Link: https://arxiv.org/abs/2607.20681v1
- Score: 10.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 HDNNP 准确地描述了 B19$^\prime$ 和 B33 相的相对稳定性，包括 meV/原子数量级的细微能量差异。预测的堆垛层错能量景观具有强烈的各向异性，并揭示了优先剪切路径，为变形和孪生机制提供了原子学的见解。有限温度分子动力学模拟进一步能够研究作为温度函数的无约束结构演化。 总体而言，开发的 HDNNP 为纳秒时间尺度上包含数十万个原子的马氏体 NiTi 系统的复杂结构和功能行为的原子模拟提供了坚实的基础。
**讨论重点：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 5. Study of ordering in (MoCrTi)$_{100-x}$Al$_x$ refractory high-entropy alloys using machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-20T16:01:06Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn
- Authors: Jiyao Zhang, Klemens Lechner, Markus Maßwohl, Petra Spoerk-Erdely, David Holec
- Link: https://arxiv.org/abs/2607.18099v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 耐火高熵合金由于其优异的机械性能而成为高温应用的有希望的候选者。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。在这项工作中，通过利用通用机器学习原子间势与混合蒙特卡罗和分子动力学模拟，研究了(MoCrTi)(100-x)Alx系统的温度依赖性热力学和机械性能。 热容和短程有序参数揭示了不同的有序-无序转变行为。虽然 Mo25Cr25Ti25Al25 和 Mo32Cr32Ti32Al4 合金表现出由 B2 型原子对的协同排序主导的单一转变，但 Mo28Cr28Ti28Al16 和 Mo30Cr30Ti30Al10 合金表现出两个单独的转变：由特定对驱动的低温阶段（Mo28Cr28Ti28Al16 中的 Mo-Al；Mo28Cr28Ti28Al16 中的 Al-Al） Mo30Cr30Ti30Al10) 和由其余对控制的高温阶段。 结构分析表明，在低温有序B2相中，Mo和Al共享一个亚晶格，而Cr和Ti共享另一个亚晶格。此外，还确定了排序和机械刚度之间的关系。有序显着增强了弹性常数和模量，并产生非单调的成分依赖性。与随机固溶体不同的是，随机固溶体的刚度随着 Al 含量的降低而单调增加，有序构型表现出非单调趋势，在 Mo30Cr30Ti30Al10 合金中达到峰值。 这种增强归因于强短程有序引起的刚性原子对的优化群体。这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。
**讨论重点：** 这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 6. RuNNer 2.0: A Software Suite for High-Dimensional Neural Network Potentials

- Source: arXiv
- Date: 2026-07-20T14:13:35Z
- Venue: physics.chem-ph, cond-mat.mtrl-sci, physics.comp-ph
- Authors: Alexander L. M. Knoll, Moritz R. Schäfer, K. Nikolas Lausch, Moritz Gubler, Henry Wang, Richard Springborn
- Link: https://arxiv.org/abs/2607.17978v1
- Score: 8.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局域电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。优化的内存管理策略消除了传统上与远程交互相关的训练开销，从而使 4G-HDNNP 能够以与本地对应物相同的效率进行训练。 RuNNer 2.0 采用现代 Fortran（2003/2008 标准）开发，结合​​混合 MPI/OpenMP 并行化方案，旨在在任何 CPU 环境（从经济高效的本地工作站到大规模 HPC 集群）中高效运行。其模块化库架构有助于直接绑定到外部模拟软件； LAMMPS 和原子仿真环境 (ASE) 的本机接口提供对其所有功能的完全访问，包括内置的基于委员会的不确定性量化。 RuNNer 2.0生态系统的高效率和可扩展性通过详细的基准测试得到证明。
**讨论重点：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局域电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. Are Machine Learning Interatomic Potentials Truly Practical? A Benchmark of 23 Mainstream Models

- Source: arXiv
- Date: 2026-07-08T17:04:42Z
- Venue: cond-mat.mtrl-sci, cs.CE, physics.comp-ph
- Authors: Hanwen Kang, Tenglong Lu, Sheng Meng, Miao Liu
- Link: https://arxiv.org/abs/2607.07647v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。我们评估三个维度：预测准确性、MD 模拟吞吐量和原子可扩展性。 我们的结果揭示了精确度与效率之间的巨大权衡：大型 SOTA 模型的精确度仅比轻量级模型高出 3-5 meV/atom，但吞吐量却损失了几个数量级——在最坏的情况下，仅比 DFT 本身快一点点。相比之下，轻量级 MLIP 位于帕累托前沿并在适度的硬件上运行。教训是，一维基准会误导该领域，未来的 MLIP 开发应该重视效率和可扩展性以及准确性。
**讨论重点：** 我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 8. MLIP Studio: An Open Platform for Interactive Benchmarking and Atomistic Simulations Using Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-08T16:23:57Z
- Venue: cond-mat.mtrl-sci
- Authors: Manas Sharma, Sudeep Punnathanam, Ananth Govind Rajan
- Link: https://arxiv.org/abs/2607.07606v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 通用机器学习原子间势（MLIP）是改变原子模拟的基础人工智能模型，但其实际使用仍然受到分散的软件生态系统、依赖性冲突和缺乏可用的基准测试工具的阻碍。这些模型以计算成本的一小部分达到了第一原理密度泛函理论 (DFT) 的精度。我们推出了 MLIP Studio（可在 https://mlipstudio.iisc.ac.in 获取），这是一个开放且免费的平台，可将 60 多种通用 MLIP 引入分子和材料的统一交互界面中。 该平台支持端到端 MLIP 驱动的工作流程，包括属性预测、几何优化、振动和状态方程分析、自旋状态确定、自定义模型部署以及针对参考数据的高通量基准测试。自动奇偶图和可排序误差表有助于快速识别元素异常值和有问题的数据点。我们证明基于 MLIP 的预优化可以减少后续 DFT 优化工作约 33$\times$。此外，该应用程序还可以对计算性能进行基准测试。 通过涉及蓝宝石基板上的二维磁性材料 CrCl$_3$ 的综合案例研究，我们展示了各种属性和势能景观的跨模型比较如何指导特定任务的 MLIP 选择。总体而言，MLIP Studio 降低了在计算化学和材料科学的端到端研究工作流程、基准测试和教育中可靠使用基础模型的障碍。
**讨论重点：** 我们推出了 MLIP Studio（可在 https://mlipstudio.iisc.ac.in 获取），这是一个开放且免费的平台，可将 60 多种通用 MLIP 引入分子和材料的统一交互界面中。通过涉及蓝宝石基板上的二维磁性材料 CrCl$_3$ 的综合案例研究，我们展示了各种属性和势能景观的跨模型比较如何指导特定任务的 MLIP 选择。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. dpti: An Automated Thermodynamic Integration Workflow for Phase Diagram Calculations with Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-06T12:56:52Z
- Venue: physics.comp-ph, cond-mat.mtrl-sci
- Authors: Fengbo Yuan, Xin Zhong, Donghao Zheng, Jinzhe Zeng, Linfeng Zhang, Han Wang
- Link: https://arxiv.org/abs/2607.05015v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 热力学积分 (TI) 是一种广泛使用的计算自由能和相图的方法。然而，由机器学习原子间势 (MLIP) 驱动的 TI 计算在技术上仍然具有挑战性，因为它们需要仔细设计可逆积分路径以及每个相和状态点的许多密切相关的分子动力学 (MD) 任务。 为了应对这些挑战，我们推出了 dpti，这是一个开源 Python 软件包，可自动执行使用 MLIP 进行相图计算的 TI 工作流程。 dpti 通过可逆积分路径将具有分析已知自由能的参考系统连接到 MLIP 描述的原子和分子固体和液体。给定 JSON 输入文件，dpti 生成并运行所需的 MD 任务，计算自由能贡献，估计误差，并将共存点传播到相边界。 我们通过深势模型驱动的两个示例演示了 dpti 的用法：涉及 β-石英、柯石英和熔体的二氧化硅相图，以及冰 Ih-液态水相边界。 dpti 提供了一个有用的工具，用于自动计算由 MLIP 建模的材料的相图。
**讨论重点：** 然而，由机器学习原子间势 (MLIP) 驱动的 TI 计算在技术上仍然具有挑战性，因为它们需要仔细设计可逆积分路径以及每个相和状态点的许多密切相关的分子动力学 (MD) 任务。热力学积分 (TI) 是一种广泛使用的计算自由能和相图的方法。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 10. Dyna-Mat: End-to-end benchmarking of foundation machine learning interatomic potentials in finite-temperature ensembles

- Source: arXiv
- Date: 2026-07-03T15:46:15Z
- Venue: cond-mat.mtrl-sci, physics.chem-ph
- Authors: Mikołaj J. Gawkowski, Nongnuch Artrith, Silvia Bonfanti, Abhijeet Sadashiv Gangan, Hendrik H. Heenen, Joseph Kioseoglou
- Link: https://arxiv.org/abs/2607.03433v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 基础机器学习原子间势 (MLIP) 越来越多地被用作第一性原理计算的直接替代品，从而能够在以前无法实现的长度和时间尺度上模拟材料。然而，由于缺乏地面实况数据，它们在有限热力学系综中结构和动力学可观测值的准确性尚未确定。在这里，我们介绍 Dyna-Mat-v1.0，这是一个凝聚相第一原理分子动力学轨迹的基准数据集，旨在在实际有限温度条件下测试基础 MLIP。 使用该数据集，我们通过比较第一原理配置和从 MLIP 驱动轨迹生成的可观测量的单点能量和力误差，评估了四个模型层的 15 个基础 MLIP。我们发现，具有较低单点力误差的“平均”模型也会产生较低的结构和动力学可观测误差。然而，对于某些单独的系统，低力误差会导致预测结构的定性故障。 大多数模型对压力的描述仍然很差，这表明当前大规模训练数据集中可用的密度泛函理论压力标签存在局限性。最后，我们构建了一个准确性成本帕累托前沿，以确定分子动力学与基础 MLIP 的最佳权衡，发现根据此处考虑的准确性指标，最新一代的交叉训练模型接近帕累托最优。 总体而言，Dyna-Mat-v1.0 表明，端到端有限温度验证对于量化基础 MLIP 的预测行为至关重要，并提供了一种简单、可扩展的途径，用于在与材料设计相关的静态和谐波基准之外对其进行评估。
**讨论重点：** 在这里，我们介绍 Dyna-Mat-v1.0，这是一个凝聚相第一原理分子动力学轨迹的基准数据集，旨在在实际有限温度条件下测试基础 MLIP。使用该数据集，我们通过比较第一原理配置和从 MLIP 驱动轨迹生成的可观测量的单点能量和力误差，评估了四个模型层的 15 个基础 MLIP。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Altermagnetism from a Cu-Fe Lieb Lattice in FeSe/Cuprate Heterostructures

- Source: arXiv
- Date: 2026-07-29T18:00:04Z
- Venue: cond-mat.str-el, cond-mat.supr-con
- Authors: Ying Li, Augustin Davignon, Peng Rao, Runhan Li, Maia G. Vergniory, Roser Valentí
- Link: https://arxiv.org/abs/2607.27331v1
- Score: 30.0
- Match: 摘要匹配 unconventional superconductivity; 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet

**中文摘要：** 在基于铜酸盐的高$T_c$系统中实现交变磁性将为在没有净磁化强度的情况下研究自旋分裂电子​​带并研究它们与非常规超导性的相互作用提供直接途径。在这里，我们提出 FeSe/铜酸盐异质结构提供了这样一个平台，其中 Cu 和 Fe 层的 45$^\circ$ 扭曲创建了一个有效的 CuFe$_2$ Lieb 晶格，其中 Fe 磁序和通过配体的 Cu-Fe 杂化诱导了交磁 $d$ 波自旋分裂。最小紧束缚模型表明该机制是通用的。 此外，FeSe 中两个 Se 位点的基质引起的不等价性提供了第二条途径，其中交变磁性起源于 Fe 层，并通过邻近转移到铜酸盐层。 FeSe/Bi$_2$Sr$_2$CuO$_6$ 异质结构的密度泛函理论计算证实了两种机制的可行性，并揭示了增强自旋分裂的方法。这些结果确立了超导铜酸盐/过渡金属硫属化物异质结构作为工程交流磁学和研究其与非常规超导耦合的有前途的环境。
**讨论重点：** 在这里，我们提出 FeSe/铜酸盐异质结构提供了这样一个平台，其中 Cu 和 Fe 层的 45$^\circ$ 扭曲创建了一个有效的 CuFe$_2$ Lieb 晶格，其中 Fe 磁序和通过配体的 Cu-Fe 杂化诱导了交磁 $d$ 波自旋分裂。在基于铜酸盐的高$T_c$系统中实现交变磁性将为在没有净磁化强度的情况下研究自旋分裂电子​​带并研究它们与非常规超导性的相互作用提供直接途径。 结合关键词看，阅读时应重点关注非常规超导、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Coupled Spin-Density-Wave and Bond-Order Driven Metal-Insulator Transition in Altermagnetic CsCr$_2$S$_2$O

- Source: arXiv
- Date: 2026-07-30T14:58:50Z
- Venue: cond-mat.str-el
- Authors: Chenchao Xu, Wansheng Bai, Guo-Xiang Zhi, Yi Liu, Xiaoqun Wang, Jianhui Dai
- Link: https://arxiv.org/abs/2607.28329v1
- Score: 28.0
- Match: 摘要匹配 altermagnetism; 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 在 CsCr$_2$S$_2$O 中发现了由键序 (BO) 与次级自旋密度波 (SDW) 耦合驱动的金属-绝缘体转变 (MIT)。这种耦合是由于预先存在的 C 型反铁磁 (C-AFM) 阶次而导致时间反转对称性被破坏而实现的。第一性原理计算揭示了轨道选择物理现象，即 Cr-$d_{yz}$ 轨道形成局部矩并建立交变磁序，而 Cr-$d_{xz}$ 轨道保持金属性并与 S-$p_z$ 杂化。因此，低能物理由 Cr-$d_{xz}$ 和 S-$p_z$ 轨道控制。 然后，现场相互作用增强了流动 $d_{xz}$ 电子的次级 SDW ($s$SDW) 不稳定性，该电子与 Cr-$d_{xz}$-S-$p_z$ 键序耦合。由此产生的耦合 $s$SDW-BO 同时产生实验观察到的结构变形、电荷歧化、局部 Cr 矩调制和间隙打开。我们的研究结果建立了一种轨道选择机制，在该机制上预先存在的交变磁力和电子相关性合作驱动结构性 MIT。
**讨论重点：** 在 CsCr$_2$S$_2$O 中发现了由键序 (BO) 与次级自旋密度波 (SDW) 耦合驱动的金属-绝缘体转变 (MIT)。这种耦合是由于预先存在的 C 型反铁磁 (C-AFM) 阶次而导致时间反转对称性被破坏而实现的。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. A Universal Crystal-Field Design Principle for Orbital-Order-Driven Altermagnetism

- Source: arXiv
- Date: 2026-07-30T05:26:18Z
- Venue: cond-mat.mtrl-sci
- Authors: Shantanu Pathak, Saswata Bhattacharya
- Link: https://arxiv.org/abs/2607.27693v1
- Score: 27.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁体将共线反铁磁序与非相对论自旋分裂相结合，无需依赖自旋轨道耦合即可实现自旋电子功能。虽然交错轨道排序最近已成为交流磁学的替代途径，但其普遍性仍未得到探索。在这里，我们建立了轨道序驱动交变磁力的通用晶体场设计原理。 我们表明，结构弛豫一致地重建了晶体场景观，激活了一个共同的 $d_{xz}/d_{yz}$ 轨道流形，该轨道流形驱动自发交错轨道排序和跨越电子填充从 $d^1$ 到 $d^7$ 的过渡金属化合物的鲁棒 $d$ 波非相对论自旋分裂。通过引入基于层相关磁和轨道序参数的统一对称框架，我们演示了层间堆叠如何决定系统是否实现体交变磁态或全局补偿的反交变磁相。 此外，我们发现这种对称保护的自旋分裂纹理会产生高度各向异性的自旋极化电导率。我们的结果将晶体场工程确立为发现和工程轨道序驱动交替磁体的预测设计策略。
**讨论重点：** 在这里，我们建立了轨道序驱动交变磁力的通用晶体场设计原理。通过引入基于层相关磁和轨道序参数的统一对称框架，我们演示了层间堆叠如何决定系统是否实现体交变磁态或全局补偿的反交变磁相。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Ferroelectric switchable altermagnetic-like compensated ferrimagnets with charge ordering

- Source: arXiv
- Date: 2026-07-29T14:32:39Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, cond-mat.str-el
- Authors: Xinyu Yang, Shuai Dong
- Link: https://arxiv.org/abs/2607.26971v1
- Score: 27.0
- Match: 摘要匹配 ferroelectricity; 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 磁化强度几乎为零但非相对论性自旋分裂突出的非常规共线磁体，例如交替磁体，可以继承铁磁体和反铁磁体的优点。通过结合更多的自由度，例如铁电性和电荷排序，这些非常规磁体可以变得更加有趣和功能化。根据这一设计原理，预计 Fe$_3$O$_5$ 单层将表现出混合自旋分裂机制，其中交磁状 $k$ 路径交替分裂和亚铁磁体状塞曼分裂相叠加。 受益于基于自旋电荷耦合的隐藏磁电，这种自旋分裂可以通过电场完全切换。其电导率是高度自旋极化的，极化率高于99\%$，与半金属相当，但磁化强度为零。
**讨论重点：** 根据这一设计原理，预计 Fe$_3$O$_5$ 单层将表现出混合自旋分裂机制，其中交磁状 $k$ 路径交替分裂和亚铁磁体状塞曼分裂相叠加。通过结合更多的自由度，例如铁电性和电荷排序，这些非常规磁体可以变得更加有趣和功能化。 结合关键词看，阅读时应重点关注铁电性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 5. Transport Evidence of Magnetic Polarization in the Altermagnetic Candidate MnTe

- Source: arXiv
- Date: 2026-07-30T16:14:10Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall
- Authors: Younes Ghorbani, Nayana Devaraj, Joshua Maile, Samuel Poage, Qihua Zhang, Maria Hilse
- Link: https://arxiv.org/abs/2607.28441v1
- Score: 25.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 精确控制磁特性的能力是未来自旋电子学发展的核心。在这项工作中，我们报告了使用分子束外延在 InP(111) 衬底上成功生长外延 α-MnTe 薄膜。低温下的磁输运测量揭示了明显的迟滞蝶形纵向磁阻以及非线性横向磁阻响应，表明薄膜中存在有限的净磁极化。 为了了解这种行为的起源，进行了密度泛函理论 (DFT) 计算。虽然原始块体 MnTe 是一种补偿反铁磁体，但我们的计算结果表明，薄膜几何形状中可以通过多种途径出现有限磁化，包括界面引起的对称性破缺和点缺陷。这些发现证明了在薄膜中设计磁响应的外延途径。
**讨论重点：** 精确控制磁特性的能力是未来自旋电子学发展的核心。在这项工作中，我们报告了使用分子束外延在 InP(111) 衬底上成功生长外延 α-MnTe 薄膜。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 6. Orbital-Selective Mott Transition and Correlation-Amplified Charge Ordering in the Altermagnet CsCr$_2$S$_2$O

- Source: arXiv
- Date: 2026-07-30T11:14:59Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: Xiuhua Chen, Yilin Wang
- Link: https://arxiv.org/abs/2607.28029v1
- Score: 24.0
- Match: 摘要匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** Altermagnet CsCr$_2$S$_2$O 经历由晶格畸变和 Cr 子晶格上的条带电荷顺序驱动的 Verwey 型金属到绝缘体转变 (MIT)，让人想起 Fe$_3$O$_4$ 中的物理现象。然而，原子畸变仅发生在配体位点而不是 Cr 位点。因此，是什么导致了 Cr 位点之间如此明显的电荷不平衡仍然是一个谜。利用 DFT+DMFT 计算，我们确定了轨道选择性莫特跃迁，这使得相关金属 $d_{yz}$ 轨道控制着低能物理。 我们证明，S 位点畸变通过 Cr-$d_{yz}$ 和 S-$p$ 轨道杂化触发 Cr 位点之间初始的微小电荷不对称性。至关重要的是，这种不对称性被动态电子相关性显着放大，导致不同 Cr 位点之间 Cr-$d_{yz}$ 轨道的电荷和电子相关性存在巨大差异。这进一步引起了交变磁态下局部自旋极化的显着差异，最终推动了 MIT 的发展。 相反，我们预测用 Te 代替 S 会削弱这种相关放大效应，并且由于电子相关性较弱而无法诱导 MIT。我们的研究结果表明，多体效应可以极大地放大配体不稳定性，从而重塑交变磁体的电子结构，这凸显了配体工程对于实现稳健的金属交变磁性至关重要。
**讨论重点：** Altermagnet CsCr$_2$S$_2$O 经历由晶格畸变和 Cr 子晶格上的条带电荷顺序驱动的 Verwey 型金属到绝缘体转变 (MIT)，让人想起 Fe$_3$O$_4$ 中的物理现象。然而，原子畸变仅发生在配体位点而不是 Cr 位点。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 7. Nanoscale Imaging of Strain-Controlled Altermagnetic Domains in α-MnTe

- Source: arXiv
- Date: 2026-07-29T05:42:39Z
- Venue: cond-mat.mtrl-sci
- Authors: Alex L. Melendez, Sijie Xu, Liangbo Liang, An-Ping Li, Pengcheng Dai, Hu Miao
- Link: https://arxiv.org/abs/2607.26495v1
- Score: 23.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交替磁体将补偿磁序与动量相关的自旋分裂相结合，提供了一种实现自旋电子功能的途径，而无需传统铁磁体的杂散场。机械应变提供了一种控制奈尔级的有前途的方法，但应变重组交变磁结构的微观途径仍未解决。在这里，我们将压电驱动的单轴应变单元与扫描氮空位磁力测量相结合，对室温下原位压缩过程中块体 α-MnTe 的磁畴进行成像。 我们发现压缩通过磁畴合并重新组织磁性纹理，增加最大连通磁畴的尺寸，同时降低磁畴壁密度。然而，卸载后，应变形成的域网络不会沿着加载路径返回。相反，大的连接区域分裂成新的亚稳态配置，在最大域尺寸和杂散场分布中产生明显的滞后。这些结果将域连接性和拓扑结构确定为应变诱导磁记忆的关键载体。 我们的工作揭示了磁域聚结和磁滞碎裂作为 α-MnTe 中应变控制的微观途径，并为应变可编程交变磁织构和可重构自旋电子器件建立了一条途径。
**讨论重点：** 交替磁体将补偿磁序与动量相关的自旋分裂相结合，提供了一种实现自旋电子功能的途径，而无需传统铁磁体的杂散场。机械应变提供了一种控制奈尔级的有前途的方法，但应变重组交变磁结构的微观途径仍未解决。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 8. Thermal spin transport in easy-planar $d$-wave altermagnets controlled by magnetic field

- Source: arXiv
- Date: 2026-07-30T11:53:34Z
- Venue: cond-mat.str-el
- Authors: Yuliia I. Gusieva, Kostiantyn V. Yershov, Jeroen van den Brink, Volodymyr P. Kravchuk
- Link: https://arxiv.org/abs/2607.28085v1
- Score: 21.0
- Match: 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁体构成了一类新型共线自旋补偿材料，其中磁振子分支即使在非相对论极限下也是自旋分裂的。后者是连接两个子晶格的更复杂的对称运算（与传统反铁磁体相比）的结果。交变磁分裂强烈影响磁振子输运特性，特别是导致易轴向 $d$ 波交变磁体中的热磁振子分裂效应。 这种效应是否也出现在易平面系统中尚不明显，因为在这种情况下磁振子分支不携带恒定磁矩。在这里，我们考虑金红石型的简单平面 $d$ 波交变磁体，例如 NiF$_2$，并证明交变磁体产生的磁振子磁矩的出现，该磁矩与动量相关并具有 $d$ 波对称性。这然后导致自旋分裂效应，即响应于所施加的温度梯度而出现磁振子驱动的自旋流（磁矩流）。 我们还证明，可以通过垂直于易平面的外部磁场有效地调节相应的热自旋电导率。
**讨论重点：** 交变磁体构成了一类新型共线自旋补偿材料，其中磁振子分支即使在非相对论极限下也是自旋分裂的。后者是连接两个子晶格的更复杂的对称运算（与传统反铁磁体相比）的结果。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 9. Direct minimization versus iterative embedding in the ghost-Gutzwiller method: a comparative study of magnetism in Mott insulators

- Source: arXiv
- Date: 2026-07-29T17:34:11Z
- Venue: cond-mat.str-el
- Authors: Antonio Maria Tagliente, Ivan Pasqua, Michele Fabrizio
- Link: https://arxiv.org/abs/2607.27156v1
- Score: 20.0
- Match: 摘要匹配 Hubbard model; 标题匹配 Mott insulator; 最近 3 天发布

**中文摘要：** 准确描述假设的对称不变莫特绝缘体是迭代量子嵌入方法中长期存在的挑战。我们在 Ghost-Gutzwiller 方法中解决了这个问题，该方法可以通过类似于动态平均场理论的迭代嵌入方案来解决，或者通过直接最小化其变分能量泛函来解决。 在单带哈伯德模型的莫特转变中，这些形式上等效的方法表现得非常不同：迭代方案计算效率高但脆弱，需要莫特阶段的临时配方，但在塞曼场中失败，导致不连续能量和虚假的全极化绝缘体。直接最小化可以避免这些伪影，从而稳定真正的顺磁解决方案。 相反，当允许对称性破缺时，如在反铁磁相中，迭代方案会产生正确的解，与动态平均场理论密切相关。我们的研究结果描述了迭代嵌入可以被信任的条件以及何时需要直接最小化。
**讨论重点：** 我们在 Ghost-Gutzwiller 方法中解决了这个问题，该方法可以通过类似于动态平均场理论的迭代嵌入方案来解决，或者通过直接最小化其变分能量泛函来解决。在单带哈伯德模型的莫特转变中，这些形式上等效的方法表现得非常不同：迭代方案计算效率高但脆弱，需要莫特阶段的临时配方，但在塞曼场中失败，导致不连续能量和虚假的全极化绝缘体。 结合关键词看，阅读时应重点关注Hubbard 模型、Mott 绝缘体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 10. Finite-size effects and interaction-driven crossovers in quarter-filled attractive Hubbard model: Exact diagonalization, DMRG and machine-learning analysis

- Source: arXiv
- Date: 2026-07-30T09:30:00Z
- Venue: cond-mat.str-el, cond-mat.supr-con
- Authors: Md Fahad Equbal, Satoru Hayami
- Link: https://arxiv.org/abs/2607.27916v1
- Score: 17.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 我们使用精确对角化 (ED)、密度矩阵重正化群 (DMRG) 和基于无监督机器学习的技术研​​究有限宽度圆柱晶格上的四分之一填充有吸引力的哈伯德模型。对基态能量、局部可观测量和相关函数的分析揭示了从弱相关费米子到由紧密束缚单重态对主导的状态的连续相互作用驱动的交叉。 这种交叉源于动能驱动的费米子行程和相互作用驱动的现场对形成之间的竞争，并表现出与热力学极限下的 BCS-BEC 交叉一致的行为。空穴结合能计算为对形成提供了直接的能量证据：两孔结合能在整个吸引力范围内保持负值，而三孔结合仅在足够强的吸引力下出现，并表现出明显的有限尺寸依赖性。 为了获得相关景观的无偏表征，我们将主成分分析（PCA）和均匀流形逼近和投影（UMAP）应用于真实空间相关矩阵。 PCA 揭示了相关方差的系统性重新分布，而 UMAP 则确定了弱配对机制和强配对机制之间的明显分离。 两种基于机器学习的方法都独立地识别从传统可观测值推断出的相同交叉区域，同时提供多体相关性的底层重组的独立于顺序参数的表征。配对结构因子和主要 PCA 方差比的有限尺寸缩放分析表明，随着系统尺寸的增加，这些特征仍然保持稳健。
**讨论重点：** 我们使用精确对角化 (ED)、密度矩阵重正化群 (DMRG) 和基于无监督机器学习的技术研​​究有限宽度圆柱晶格上的四分之一填充有吸引力的哈伯德模型。对基态能量、局部可观测量和相关函数的分析揭示了从弱相关费米子到由紧密束缚单重态对主导的状态的连续相互作用驱动的交叉。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。
