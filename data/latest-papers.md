# Latest papers for 程旭丽

Updated: 2026-07-30T09:39:09.383662+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Extracting Atomic Environments for Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-28T17:28:41Z
- Venue: cond-mat.mtrl-sci
- Authors: Jared C. Stimac, Fei Zhou, Kyle Bushick, Bo Lei, Sebastien Hamel, Amit Samanta
- Link: https://arxiv.org/abs/2607.26018v1
- Score: 17.0
- Match: 标题匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 为了通过原子模拟（例如分子动力学（MD））适当捕获大规模材料特征和突发现象，系统规模可以达到数亿个原子。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 为了计算感兴趣区域中原子上的 DFT 力，例如用于原子间势的主动学习或动态训练，需要从较大的模拟框中提取一小组原子，并且需要使用 DFT 的周期性边界条件进行典型工作；然而，尚未系统地分析选择这组提取的原子的形状和大小以及生成潜在必要的钝化包络的方法。 在这项工作中，我们提出了各种技术的基准，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。我们使用多种材料系统进行测试，其中包括无定形 $\mathrm{SiO_2}$、具有螺旋位错的 Ta 和熔融 C。我们演示了一种非常简单的程序（我们称为删除的方法），其性能优于一系列替代提取方法。
**讨论重点：** 在这项工作中，我们提出了各种技术的基准，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。我们演示了一个非常简单的过程，我们称之为删除的方法，与一系列替代提取方法相比具有优越的性能。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 2. Charge-Density-Wave Phase Transitions in Monolayer 1T-TaS2 from Universal Machine Learning Molecular Dynamics

- Source: arXiv
- Date: 2026-07-24T13:57:09Z
- Venue: cond-mat.mtrl-sci
- Authors: Valentina Nesterova, Tribhuwan Pandey, Tom Berlijn, Fariborz Kargar, Lucas Lindsay, Konstantin Klyukin
- Link: https://arxiv.org/abs/2607.22316v1
- Score: 13.0
- Match: 标题匹配 machine learning molecular dynamics; 近两周发布

**中文摘要：** 1T 过渡金属二硫属化物中的电荷密度波 (CDW) 相是由强电子声子耦合和伴随的晶格不稳定性产生的。由于需要大型超级电池和广泛的有限温度采样，使用传统的第一原理分子动力学 (MD) 捕获其随温度变化的结构演化仍然具有挑战性。 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。针对 DFT 位移能量的基准测试确定了 UMA-s-1p1 通用机器学习潜力，具有足够的精度用于后续的有限温度模拟。 我们的结果表明，大规模 MD 模拟再现了实验观察到的从低温大卫之星 (SoD) 扭曲结构到高温原始六边形结构的相变序列，通过归因于 SoD 的 Ta 原子数量来量化。加热-冷却循环表现出热滞后，并且在冷却时，系统冻结成多域状态，其中α和\b{eta} CDW手性独立成核并持续到最低温度。 这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。
**讨论重点：** 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。 结合关键词看，阅读时应重点关注机器学习分子动力学相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 3. A high-dimensional neural network potential for finite-temperature phenomena in NiTi martensite

- Source: arXiv
- Date: 2026-07-22T19:32:23Z
- Venue: cond-mat.mtrl-sci
- Authors: Petr Jaroš, Petr Sedlák, Petr Šesták, Miroslav Černý, Jörg Behler, Hanuš Seiner
- Link: https://arxiv.org/abs/2607.20681v1
- Score: 11.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 HDNNP 准确地描述了 B19$^\prime$ 和 B33 相的相对稳定性，包括 meV/原子数量级的细微能量差异。预测的堆垛层错能量景观具有强烈的各向异性，并揭示了优先剪切路径，为变形和孪生机制提供了原子学的见解。有限温度分子动力学模拟进一步能够研究作为温度函数的无约束结构演化。 总体而言，开发的 HDNNP 为纳秒时间尺度上包含数十万个原子的马氏体 NiTi 系统的复杂结构和功能行为的原子模拟提供了坚实的基础。
**讨论重点：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 4. Study of ordering in (MoCrTi)$_{100-x}$Al$_x$ refractory high-entropy alloys using machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-20T16:01:06Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn
- Authors: Jiyao Zhang, Klemens Lechner, Markus Maßwohl, Petra Spoerk-Erdely, David Holec
- Link: https://arxiv.org/abs/2607.18099v1
- Score: 9.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 耐火高熵合金由于其优异的机械性能而成为高温应用的有希望的候选者。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。在这项工作中，通过利用通用机器学习原子间势与混合蒙特卡罗和分子动力学模拟，研究了(MoCrTi)(100-x)Alx系统的温度依赖性热力学和机械性能。 热容和短程有序参数揭示了不同的有序-无序转变行为。虽然 Mo25Cr25Ti25Al25 和 Mo32Cr32Ti32Al4 合金表现出由 B2 型原子对的协同排序主导的单一转变，但 Mo28Cr28Ti28Al16 和 Mo30Cr30Ti30Al10 合金表现出两个单独的转变：由特定对驱动的低温阶段（Mo28Cr28Ti28Al16 中的 Mo-Al；Mo28Cr28Ti28Al16 中的 Al-Al） Mo30Cr30Ti30Al10) 和由其余对控制的高温阶段。 结构分析表明，在低温有序B2相中，Mo和Al共享一个亚晶格，而Cr和Ti共享另一个亚晶格。此外，还确定了排序和机械刚度之间的关系。有序显着增强了弹性常数和模量，并产生非单调的成分依赖性。与随机固溶体不同的是，随机固溶体的刚度随着 Al 含量的降低而单调增加，有序构型表现出非单调趋势，在 Mo30Cr30Ti30Al10 合金中达到峰值。 这种增强归因于强短程有序引起的刚性原子对的优化群体。这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。
**讨论重点：** 这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 5. RuNNer 2.0: A Software Suite for High-Dimensional Neural Network Potentials

- Source: arXiv
- Date: 2026-07-20T14:13:35Z
- Venue: physics.chem-ph, cond-mat.mtrl-sci, physics.comp-ph
- Authors: Alexander L. M. Knoll, Moritz R. Schäfer, K. Nikolas Lausch, Moritz Gubler, Henry Wang, Richard Springborn
- Link: https://arxiv.org/abs/2607.17978v1
- Score: 9.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局域电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。优化的内存管理策略消除了传统上与远程交互相关的训练开销，从而使 4G-HDNNP 能够以与本地对应物相同的效率进行训练。 RuNNer 2.0 采用现代 Fortran（2003/2008 标准）开发，结合​​混合 MPI/OpenMP 并行化方案，旨在在任何 CPU 环境（从经济高效的本地工作站到大规模 HPC 集群）中高效运行。其模块化库架构有助于直接绑定到外部模拟软件； LAMMPS 和原子仿真环境 (ASE) 的本机接口提供对其所有功能的完全访问，包括内置的基于委员会的不确定性量化。 RuNNer 2.0生态系统的高效率和可扩展性通过详细的基准测试得到证明。
**讨论重点：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局域电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 6. Are Machine Learning Interatomic Potentials Truly Practical? A Benchmark of 23 Mainstream Models

- Source: arXiv
- Date: 2026-07-08T17:04:42Z
- Venue: cond-mat.mtrl-sci, cs.CE, physics.comp-ph
- Authors: Hanwen Kang, Tenglong Lu, Sheng Meng, Miao Liu
- Link: https://arxiv.org/abs/2607.07647v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。我们评估三个维度：预测准确性、MD 模拟吞吐量和原子可扩展性。 我们的结果揭示了精确度与效率之间的巨大权衡：大型 SOTA 模型的精确度仅比轻量级模型高出 3-5 meV/atom，但吞吐量却损失了几个数量级——在最坏的情况下，仅比 DFT 本身快一点点。相比之下，轻量级 MLIP 位于帕累托前沿并在适度的硬件上运行。教训是，一维基准会误导该领域，未来的 MLIP 开发应该重视效率和可扩展性以及准确性。
**讨论重点：** 我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. MLIP Studio: An Open Platform for Interactive Benchmarking and Atomistic Simulations Using Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-08T16:23:57Z
- Venue: cond-mat.mtrl-sci
- Authors: Manas Sharma, Sudeep Punnathanam, Ananth Govind Rajan
- Link: https://arxiv.org/abs/2607.07606v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 通用机器学习原子间势（MLIP）是改变原子模拟的基础人工智能模型，但其实际使用仍然受到分散的软件生态系统、依赖性冲突和缺乏可用的基准测试工具的阻碍。这些模型以计算成本的一小部分达到了第一原理密度泛函理论 (DFT) 的精度。我们推出了 MLIP Studio（可在 https://mlipstudio.iisc.ac.in 获取），这是一个开放且免费的平台，可将 60 多种通用 MLIP 引入分子和材料的统一交互界面中。 该平台支持端到端 MLIP 驱动的工作流程，包括属性预测、几何优化、振动和状态方程分析、自旋状态确定、自定义模型部署以及针对参考数据的高通量基准测试。自动奇偶图和可排序误差表有助于快速识别元素异常值和有问题的数据点。我们证明基于 MLIP 的预优化可以减少后续 DFT 优化工作约 33$\times$。此外，该应用程序还可以对计算性能进行基准测试。 通过涉及蓝宝石基板上的二维磁性材料 CrCl$_3$ 的综合案例研究，我们展示了各种属性和势能景观的跨模型比较如何指导特定任务的 MLIP 选择。总体而言，MLIP Studio 降低了在计算化学和材料科学的端到端研究工作流程、基准测试和教育中可靠使用基础模型的障碍。
**讨论重点：** 我们推出了 MLIP Studio（可在 https://mlipstudio.iisc.ac.in 获取），这是一个开放且免费的平台，可将 60 多种通用 MLIP 引入分子和材料的统一交互界面中。通过涉及蓝宝石基板上的二维磁性材料 CrCl$_3$ 的综合案例研究，我们展示了各种属性和势能景观的跨模型比较如何指导特定任务的 MLIP 选择。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 8. dpti: An Automated Thermodynamic Integration Workflow for Phase Diagram Calculations with Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-06T12:56:52Z
- Venue: physics.comp-ph, cond-mat.mtrl-sci
- Authors: Fengbo Yuan, Xin Zhong, Donghao Zheng, Jinzhe Zeng, Linfeng Zhang, Han Wang
- Link: https://arxiv.org/abs/2607.05015v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 热力学积分 (TI) 是一种广泛使用的计算自由能和相图的方法。然而，由机器学习原子间势 (MLIP) 驱动的 TI 计算在技术上仍然具有挑战性，因为它们需要仔细设计可逆积分路径以及每个相和状态点的许多密切相关的分子动力学 (MD) 任务。 为了应对这些挑战，我们推出了 dpti，这是一个开源 Python 软件包，可自动执行使用 MLIP 进行相图计算的 TI 工作流程。 dpti 通过可逆积分路径将具有分析已知自由能的参考系统连接到 MLIP 描述的原子和分子固体和液体。给定 JSON 输入文件，dpti 生成并运行所需的 MD 任务，计算自由能贡献，估计误差，并将共存点传播到相边界。 我们通过深势模型驱动的两个示例演示了 dpti 的用法：涉及 β-石英、柯石英和熔体的二氧化硅相图，以及冰 Ih-液态水相边界。 dpti 提供了一个有用的工具，用于自动计算由 MLIP 建模的材料的相图。
**讨论重点：** 然而，由机器学习原子间势 (MLIP) 驱动的 TI 计算在技术上仍然具有挑战性，因为它们需要仔细设计可逆积分路径以及每个相和状态点的许多密切相关的分子动力学 (MD) 任务。热力学积分 (TI) 是一种广泛使用的计算自由能和相图的方法。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 9. Dyna-Mat: End-to-end benchmarking of foundation machine learning interatomic potentials in finite-temperature ensembles

- Source: arXiv
- Date: 2026-07-03T15:46:15Z
- Venue: cond-mat.mtrl-sci, physics.chem-ph
- Authors: Mikołaj J. Gawkowski, Nongnuch Artrith, Silvia Bonfanti, Abhijeet Sadashiv Gangan, Hendrik H. Heenen, Joseph Kioseoglou
- Link: https://arxiv.org/abs/2607.03433v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 基础机器学习原子间势 (MLIP) 越来越多地被用作第一性原理计算的直接替代品，从而能够在以前无法实现的长度和时间尺度上模拟材料。然而，由于缺乏地面实况数据，它们在有限热力学系综中结构和动力学可观测值的准确性尚未确定。在这里，我们介绍 Dyna-Mat-v1.0，这是一个凝聚相第一原理分子动力学轨迹的基准数据集，旨在在实际有限温度条件下测试基础 MLIP。 使用该数据集，我们通过比较第一原理配置和从 MLIP 驱动轨迹生成的可观测量的单点能量和力误差，评估了四个模型层的 15 个基础 MLIP。我们发现，具有较低单点力误差的“平均”模型也会产生较低的结构和动力学可观测误差。然而，对于某些单独的系统，低力误差会导致预测结构的定性故障。 大多数模型对压力的描述仍然很差，这表明当前大规模训练数据集中可用的密度泛函理论压力标签存在局限性。最后，我们构建了一个准确性成本帕累托前沿，以确定分子动力学与基础 MLIP 的最佳权衡，发现根据此处考虑的准确性指标，最新一代的交叉训练模型接近帕累托最优。 总体而言，Dyna-Mat-v1.0 表明，端到端有限温度验证对于量化基础 MLIP 的预测行为至关重要，并提供了一种简单、可扩展的途径，用于在与材料设计相关的静态和谐波基准之外对其进行评估。
**讨论重点：** 在这里，我们介绍 Dyna-Mat-v1.0，这是一个凝聚相第一原理分子动力学轨迹的基准数据集，旨在在实际有限温度条件下测试基础 MLIP。使用该数据集，我们通过比较第一原理配置和从 MLIP 驱动轨迹生成的可观测量的单点能量和力误差，评估了四个模型层的 15 个基础 MLIP。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 10. Beyond Adam: SOAP and Muon for Faster, Label-Efficient Training of Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-02T17:57:31Z
- Venue: cs.LG, cs.AI, physics.chem-ph
- Authors: Gil Harari, Yoel Zimmermann, Ola Tangen Kulseng, Laura Zichi, Chuin Wei Tan, Marc L. Descoteaux
- Link: https://arxiv.org/abs/2607.02499v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 机器学习原子间势（MLIP）已成为科学模拟人工智能的标志。虽然在新架构和数据集上的努力导致模型越来越准确和通用，但训练优化器的选择在很大程度上仍未被探索，默认为 Adam 及其在社区中的变体。在这里，我们实现并系统地比较了一类最近提出的矩阵结构优化器，包括 Muon、SOAP 和混合 SOAP-Muon，用于训练 NequIP 和 Allegro MLIP 模型。 我们发现这些优化器在收敛速度和最终精度方面都明显优于 Adam。 SOAP 和 SOAP-Muon 作为稳健且始终如一的强大方法而出现，而 Muon 相对于 Adam 只提供了部分收益。在部分部队监督下，这些改进尤其明显。我们的结果表明，优化器选择是 MLIP 的一个被忽视但有影响力的设计轴。
**讨论重点：** 我们的结果表明，优化器选择是 MLIP 的一个被忽视但有影响力的设计轴。虽然在新架构和数据集上的努力导致模型越来越准确和通用，但训练优化器的选择在很大程度上仍未被探索，默认为 Adam 及其在社区中的变体。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Ferroelectric switchable altermagnetic-like compensated ferrimagnets with charge ordering

- Source: arXiv
- Date: 2026-07-29T14:32:39Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, cond-mat.str-el
- Authors: Xinyu Yang, Shuai Dong
- Link: https://arxiv.org/abs/2607.26971v1
- Score: 28.0
- Match: 摘要匹配 ferroelectricity; 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 磁化强度几乎为零但非相对论性自旋分裂突出的非常规共线磁体，例如交替磁体，可以继承铁磁体和反铁磁体的优点。通过结合更多的自由度，例如铁电性和电荷排序，这些非常规磁体可以变得更加有趣和功能化。根据这一设计原理，预计 Fe$_3$O$_5$ 单层将表现出混合自旋分裂机制，其中交磁状 $k$ 路径交替分裂和亚铁磁体状塞曼分裂相叠加。 受益于基于自旋电荷耦合的隐藏磁电，这种自旋分裂可以通过电场完全切换。其电导率是高度自旋极化的，极化率高于99\%$，与半金属相当，但磁化强度为零。
**讨论重点：** 根据这一设计原理，预计 Fe$_3$O$_5$ 单层将表现出混合自旋分裂机制，其中交磁状 $k$ 路径交替分裂和亚铁磁体状塞曼分裂相叠加。通过结合更多的自由度，例如铁电性和电荷排序，这些非常规磁体可以变得更加有趣和功能化。 结合关键词看，阅读时应重点关注铁电性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Stacking-dependent anisotropic altermagnetism in V$_{1/3}$NbS$_2$

- Source: arXiv
- Date: 2026-07-28T02:39:07Z
- Venue: cond-mat.str-el
- Authors: Chris J. Lygouras, Nathan Prouse, Jack H. Drouin, Youzhe Chen, Laura Garcia-Gassull, Zili Feng
- Link: https://arxiv.org/abs/2607.25213v1
- Score: 26.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们报告了插入范德华材料 NbS$_2$ 层之间的磁性过渡金属离子三角形晶格的堆叠顺序的深远影响。利用单晶 X 射线和中子衍射以及输运和磁化强度测量，我们发现 $\rm V_{1/3}NbS_2$ 有两种不同的多型体，具有不同的易磁化轴和不同的反常霍尔响应。 非弹性中子散射数据的自洽分析为振荡 RKKY 相互作用提供了证据，该相互作用延伸至 1 nm，并稳定了两种多型体中的准共线 A 型交变磁序，尽管具有垂直的易轴。块体多型晶体的详细堆叠顺序极大地影响其宏观异常霍尔响应和磁性，这为设计层状三维固体的块体特性提供了一条新途径。
**讨论重点：** 我们报告了插入范德华材料 NbS$_2$ 层之间的磁性过渡金属离子三角形晶格的堆叠顺序的深远影响。利用单晶 X 射线和中子衍射以及输运和磁化强度测量，我们发现 $\rm V_{1/3}NbS_2$ 有两种不同的多型体，具有不同的易磁化轴和不同的反常霍尔响应。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Nanoscale Imaging of Strain-Controlled Altermagnetic Domains in α-MnTe

- Source: arXiv
- Date: 2026-07-29T05:42:39Z
- Venue: cond-mat.mtrl-sci
- Authors: Alex L. Melendez, Sijie Xu, Liangbo Liang, An-Ping Li, Pengcheng Dai, Hu Miao
- Link: https://arxiv.org/abs/2607.26495v1
- Score: 24.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交替磁体将补偿磁序与动量相关的自旋分裂相结合，提供了一种实现自旋电子功能的途径，而无需传统铁磁体的杂散场。机械应变提供了一种控制奈尔级的有前途的方法，但应变重组交变磁结构的微观途径仍未解决。在这里，我们将压电驱动的单轴应变单元与扫描氮空位磁力测量相结合，对室温下原位压缩过程中块体 α-MnTe 的磁畴进行成像。 我们发现压缩通过磁畴合并重新组织磁性纹理，增加最大连通磁畴的尺寸，同时降低磁畴壁密度。然而，卸载后，应变形成的域网络不会沿着加载路径返回。相反，大的连接区域分裂成新的亚稳态配置，在最大域尺寸和杂散场分布中产生明显的滞后。这些结果将域连接性和拓扑结构确定为应变诱导磁记忆的关键载体。 我们的工作揭示了磁域聚结和磁滞碎裂作为 α-MnTe 中应变控制的微观途径，并为应变可编程交变磁织构和可重构自旋电子器件建立了一条途径。
**讨论重点：** 交替磁体将补偿磁序与动量相关的自旋分裂相结合，提供了一种实现自旋电子功能的途径，而无需传统铁磁体的杂散场。机械应变提供了一种控制奈尔级的有前途的方法，但应变重组交变磁结构的微观途径仍未解决。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Direct minimization versus iterative embedding in the ghost-Gutzwiller method: a comparative study of magnetism in Mott insulators

- Source: arXiv
- Date: 2026-07-29T17:34:11Z
- Venue: cond-mat.str-el
- Authors: Antonio Maria Tagliente, Ivan Pasqua, Michele Fabrizio
- Link: https://arxiv.org/abs/2607.27156v1
- Score: 21.0
- Match: 摘要匹配 Hubbard model; 标题匹配 Mott insulator; 最近 3 天发布

**中文摘要：** 准确描述假设的对称不变莫特绝缘体是迭代量子嵌入方法中长期存在的挑战。我们在 Ghost-Gutzwiller 方法中解决了这个问题，该方法可以通过类似于动态平均场理论的迭代嵌入方案来解决，或者通过直接最小化其变分能量泛函来解决。 在单带哈伯德模型的莫特转变中，这些形式上等效的方法表现得非常不同：迭代方案计算效率高但脆弱，需要莫特阶段的临时配方，但在塞曼场中失败，导致不连续能量和虚假的全极化绝缘体。直接最小化可以避免这些伪影，从而稳定真正的顺磁解决方案。 相反，当允许对称性破缺时，如在反铁磁相中，迭代方案会产生正确的解，与动态平均场理论密切相关。我们的研究结果描述了迭代嵌入可以被信任的条件以及何时需要直接最小化。
**讨论重点：** 我们在 Ghost-Gutzwiller 方法中解决了这个问题，该方法可以通过类似于动态平均场理论的迭代嵌入方案来解决，或者通过直接最小化其变分能量泛函来解决。在单带哈伯德模型的莫特转变中，这些形式上等效的方法表现得非常不同：迭代方案计算效率高但脆弱，需要莫特阶段的临时配方，但在塞曼场中失败，导致不连续能量和虚假的全极化绝缘体。 结合关键词看，阅读时应重点关注Hubbard 模型、Mott 绝缘体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 5. Isolation of spin-valley locked nodal-line fermions in $d$-wave $\mathrm{AV_2X_2O}$ altermagnets

- Source: arXiv
- Date: 2026-07-28T18:00:39Z
- Venue: cond-mat.mtrl-sci
- Authors: Pritesh Srivastava, Rahul Verma, Bahadur Singh
- Link: https://arxiv.org/abs/2607.26150v1
- Score: 17.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 晶体对称性稳定了具有独特电子特性的拓扑态，而交流磁体则表现出动量相关的自旋分裂，而没有净磁化。在这里，我们将第一原理计算与最小紧束缚模型相结合，以在$d$波交替磁体$\mathrm{AV_2X_2O}$（A = Rb、Cs或K；X = Te、Se或S）中实现$C$配对的自旋谷锁定节点线费米子。低能电子结构在费米能级附近的$C_{4z}$配对谷周围存在共存的自旋简并和自旋极化节点线。 自旋极化节点线受到面外镜对称性 $\mathcal{M}_z$ 的保护，并且对自旋轨道耦合保持鲁棒性。最小模型揭示了它们的微观起源，并为它们的隔离建立了一般设计原则。层工程和电子相关性充当材料特定的旋钮，用于实现费米能级附近的这些孤立的自旋谷锁定节点线。我们的结果将 $\mathrm{AV_2X_2O}$ 系列确立为探索 $d$ 波交流磁体中的拓扑自旋谷锁定的多功能平台。
**讨论重点：** 最小模型揭示了它们的微观起源，并为它们的隔离建立了一般设计原则。在这里，我们将第一原理计算与最小紧束缚模型相结合，以在$d$波交替磁体$\mathrm{AV_2X_2O}$（A = Rb、Cs或K；X = Te、Se或S）中实现$C$配对的自旋谷锁定节点线费米子。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 6. Superfluidity without charge order in the attractive Hubbard model on the kagome lattice

- Source: arXiv
- Date: 2026-07-28T17:05:04Z
- Venue: cond-mat.str-el
- Authors: Xiaodong Jin, Yingping Mou, Rubem Mondaini
- Link: https://arxiv.org/abs/2607.25983v1
- Score: 17.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 使用辅助场量子蒙特卡罗模拟，我们研究了各种相关电子填充下 kagome 晶格的零温吸引哈伯德模型。 $2/3$密度的低能物理受到费米能狄拉克点的影响，其中我们揭示了临界吸引相互作用$U_c/t=-4.58(3)$处的超流体转变，属于手性-XY普适性类别。 在用硬核玻色子进行描述变得越来越合适的情况下，即使对于相当大的相互作用强度，这种 U(1) 对称性破缺也不会伴随电荷序。对后者的研究表明，$1/3$ 填充的电荷排序仅发生在比原始费米子模型映射对应的相互作用强度大得多的情况下。 此外，对于在非相互作用态密度中表现出范霍夫奇点的密度，我们的结果表明，任何吸引相互作用都会产生超流性，但又没有电荷排序，这与最近采用平均场理论的研究相反。
**讨论重点：** 使用辅助场量子蒙特卡罗模拟，我们研究了各种相关电子填充下 kagome 晶格的零温吸引哈伯德模型。 $2/3$密度的低能物理受到费米能狄拉克点的影响，其中我们揭示了临界吸引相互作用$U_c/t=-4.58(3)$处的超流体转变，属于手性-XY普适性类别。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 7. Ferroelectricity and antiferroelectricity in the BaS-PbS system with the rocksalt structure

- Source: arXiv
- Date: 2026-07-28T11:22:32Z
- Venue: cond-mat.mtrl-sci
- Authors: Alexander I. Lebedev
- Link: https://arxiv.org/abs/2607.25591v1
- Score: 17.0
- Match: 标题匹配 ferroelectricity; 最近 3 天发布

**中文摘要：** 使用密度泛函理论中的第一性原理计算，发现并研究了具有 NaCl 结构的 BaS--PbS 体系中超结构、超晶格、量子线和无序固溶体中的铁电不稳定性。这些结构中铁电性的出现与线性-Pb--S--Pb--S--链中TO声子的不稳定性有关，这是由于引入大的钡原子时结构拉伸而产生的。 此外，人们还发现，除了铁电相之外，该结构还表现出稳定的、竞争的反铁电相以及具有混合铁电-反铁电排序的相（铁电极化的一维Pb-S链在垂直方向上以有序或无序的方式排列）。这些相通常成为所研究系统的基态。 铁电态、反铁电态和混合态能量的接近表明出现了多重最小电势，其中无限数量的阱被构型空间中的势垒隔开。这表明低温下结构中可能出现非遍历性。
**讨论重点：** 使用密度泛函理论中的第一性原理计算，发现并研究了具有 NaCl 结构的 BaS--PbS 体系中超结构、超晶格、量子线和无序固溶体中的铁电不稳定性。这些结构中铁电性的出现与线性-Pb--S--Pb--S--链中TO声子的不稳定性有关，这是由于引入大的钡原子时结构拉伸而产生的。 结合关键词看，阅读时应重点关注铁电性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 8. Charge-6e superconductivity from doping SU(3) spin liquids

- Source: arXiv
- Date: 2026-07-28T16:02:19Z
- Venue: cond-mat.str-el, cond-mat.mes-hall, cond-mat.supr-con
- Authors: Yan-Qi Wang, Boran Zhou, Hui Yang, Zhi-Qiang Gao
- Link: https://arxiv.org/abs/2607.25909v1
- Score: 16.0
- Match: 摘要匹配 Hubbard model; 摘要匹配 quantum spin liquid; 最近 3 天发布

**中文摘要：** 我们建议掺杂 $SU(3)$ 对称自旋液体作为实现电荷 $6e$ 超导的途径。这概括了从掺杂 $SU(4)$ 对称相构造电荷 $4e$ 超导性的想法。作为一个具体的平台，我们研究了具有$SU(3)$自旋对称性和层间反铁磁交换的双层三角晶格哈伯德模型。使用互补部分子结构，我们分析了掺杂的 $\mathbb{Z}_3$ 量子自旋液体和 $SU(3)$ 相关的手性自旋液体。 掺杂 $\mathbb{Z}_3$ 量子自旋液体可以产生具有规范不变费米电荷面的正交金属 - $3e$ 费米子三重子。将这些三重子配对得到时间反转对称电荷$6e$超导体。掺杂阿贝尔 $SU(3)_1$ 和 $SU(6)_1$ 手性自旋液体分别产生具有和不具有残余阿贝尔拓扑序的手性电荷 $6e$ 超导体。 掺杂非阿贝尔$SU(3)_2$手性自旋液体会产生非阿贝尔手性电荷-$6e$超导体，与$SO(3)_{-3}$拓扑顺序交织在一起，并支持非阿贝尔$h/(6e)$超导涡旋。我们还确定了其他几个相，包括 $\mathbb{Z}_3$ 正交金属、由 $\mathbb{Z}_3$ 或 $\mathbb{Z}_2$ 拓扑顺序富集的量子反常霍尔（晶体）相、$SU(3)$-破坏电荷-$2e$ 超导体、与非阿贝尔规范场耦合的复合费米液体以及后代手性自旋液体。 我们的结果将掺杂的 $SU(3)$ 自旋液体确定为一种自然环境，其中对称性、分​​式化和拓扑结构协同作用以产生电荷 $6e$ 超导性。
**讨论重点：** 我们建议掺杂 $SU(3)$ 对称自旋液体作为实现电荷 $6e$ 超导的途径。作为一个具体的平台，我们研究了具有$SU(3)$自旋对称性和层间反铁磁交换的双层三角晶格哈伯德模型。 结合关键词看，阅读时应重点关注Hubbard 模型、量子自旋液体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 9. Momentum-Selective Two-Component Excitations in Electron-Doped Mott Insulators

- Source: arXiv
- Date: 2026-07-27T18:00:07Z
- Venue: cond-mat.str-el, cond-mat.supr-con
- Authors: Zeyu Han, Can Cui, Jia-Xin Zhang, Zheng-Yu Weng
- Link: https://arxiv.org/abs/2607.24936v1
- Score: 16.0
- Match: 标题匹配 Mott insulator; 最近 3 天发布

**中文摘要：** 实验研究揭示了电子和空穴掺杂铜酸盐之间低能单粒子激发的惊人不对称性。电子掺杂铜酸盐表现出一种重要的二分性：类费米液体行为（表明电子相关性较弱）与空穴掺杂系统典型的相关驱动特征共存。这种双重性质对掺杂莫特绝缘体框架内的统一描述提出了挑战。 目前的工作通过建立 $t$-$t'$-$J$ 模型的基态波函数通常具有双分量结构来解决这个问题，包括相干准粒子和非相干复合分量。动能由相干准粒子的固有传播和这些组件之间的共振产生。在单孔水平上使用变分蒙特卡罗，我们表明对于空穴掺杂（$t'<0$），组件之间的这种共振在低能量下占主导地位并集中在节点区域。 这种由共振引起的新兴传播可以在物理上解释为源自分数化自由度的重组，这驱动了与强相关性相关的各种现象。相反，对于电子掺杂（$t'>0$），表现出费米液体传统特性的相干准粒子传播在低能量下在波腹区域选择性增强。 这会在电子掺杂系统的动量空间中产生分离：低能量下的波腹谱权由相干准粒子控制，从根本上不同于节点区域，节点区域仍然由非相干复合成分主导。受这种结构的启发并以实验观察为指导，我们提出了有限掺杂下的唯象格林函数，产生与实验一致的光谱特征。
**讨论重点：** 目前的工作通过建立 $t$-$t'$-$J$ 模型的基态波函数通常具有双分量结构来解决这个问题，包括相干准粒子和非相干复合分量。这种双重性质对掺杂莫特绝缘体框架内的统一描述提出了挑战。 结合关键词看，阅读时应重点关注Mott 绝缘体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 10. Chiral Magnons: Mechanisms and Research Progress

- Source: arXiv
- Date: 2026-07-27T18:13:11Z
- Venue: cond-mat.str-el
- Authors: Wanxing Lin, Hanchen Deng, Bao-Tian Wang, Dao-Xin Yao
- Link: https://arxiv.org/abs/2607.24963v1
- Score: 15.0
- Match: 摘要匹配 altermagnetism; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 手性磁振子是磁有序系统中独特的集体自旋激发，其色散关系打破了动量反演对称性 $ω(\boldsymbol{k}) \neq ω(-\boldsymbol{k})$，导致本质上的非互易自旋波传播。这种内置的方向性为自旋信息传递、热自旋互变和低耗散非互易微波器件提供了新的机会，它们补充了拓扑磁振子学，但又有所不同。 近年来，交变磁学的提出和快速发展拓宽了手性磁子的物理起源和研究框架，使其成为凝聚态物理的研究前沿。这篇综述提出了手性磁振子的统一框架，涵盖对称性破缺机制、材料实现、实验表征、输运响应和多体非厄米动力学，并评估了通往室温和设备相关平台的路线。 讨论基于对称分析、模型哈密顿量和自旋波理论，结合第一性原理计算以及最近的光谱（例如非弹性和偏振中子散射、布里渊光散射）和输运测量。本综述进一步总结了体能隙和贝里曲率引起的手性磁振子边缘态、通过手性自旋泵浦和腔磁振子混合体增强非互易性，以及多粒子阻尼和增益损失竞争产生的非厄米特征。 该综述为阐明手性磁振子的基本机制、推进新型材料的合成和实验表征以及指导下一代非互易磁振子器件的设计提供了全面的参考。
**讨论重点：** 该综述为阐明手性磁振子的基本机制、推进新型材料的合成和实验表征以及指导下一代非互易磁振子器件的设计提供了全面的参考。近年来，交变磁学的提出和快速发展拓宽了手性磁子的物理起源和研究框架，使其成为凝聚态物理的研究前沿。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。
