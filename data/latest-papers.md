# Latest papers for 程旭丽

Updated: 2026-07-21T09:22:55.391727+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Study of ordering in (MoCrTi)$_{100-x}$Al$_x$ refractory high-entropy alloys using machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-20T16:01:06Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn
- Authors: Jiyao Zhang, Klemens Lechner, Markus Maßwohl, Petra Spoerk-Erdely, David Holec
- Link: https://arxiv.org/abs/2607.18099v1
- Score: 18.0
- Match: 标题匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 耐火高熵合金由于其优异的机械性能而成为高温应用的有希望的候选者。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。在这项工作中，通过利用通用机器学习原子间势与混合蒙特卡罗和分子动力学模拟，研究了(MoCrTi)(100-x)Alx系统的温度依赖性热力学和机械性能。 热容和短程有序参数揭示了不同的有序-无序转变行为。虽然 Mo25Cr25Ti25Al25 和 Mo32Cr32Ti32Al4 合金表现出由 B2 型原子对的协同排序主导的单一转变，但 Mo28Cr28Ti28Al16 和 Mo30Cr30Ti30Al10 合金表现出两个单独的转变：由特定对驱动的低温阶段（Mo28Cr28Ti28Al16 中的 Mo-Al；Mo28Cr28Ti28Al16 中的 Al-Al） Mo30Cr30Ti30Al10) 和由其余对控制的高温阶段。 结构分析表明，在低温有序B2相中，Mo和Al共享一个亚晶格，而Cr和Ti共享另一个亚晶格。此外，还确定了排序和机械刚度之间的关系。有序显着增强了弹性常数和模量，并产生非单调的成分依赖性。与随机固溶体不同的是，随机固溶体的刚度随着 Al 含量的减少而单调增加，有序构型表现出非单调趋势，在 Mo30Cr30Ti30Al10 合金中达到峰值。 这种增强归因于强短程有序引起的刚性原子对的优化群体。这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。
**讨论重点：** 这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 2. RuNNer 2.0: A Software Suite for High-Dimensional Neural Network Potentials

- Source: arXiv
- Date: 2026-07-20T14:13:35Z
- Venue: physics.chem-ph, cond-mat.mtrl-sci, physics.comp-ph
- Authors: Alexander L. M. Knoll, Moritz R. Schäfer, K. Nikolas Lausch, Moritz Gubler, Henry Wang, Richard Springborn
- Link: https://arxiv.org/abs/2607.17978v1
- Score: 18.0
- Match: 标题匹配 neural network potential; 最近 3 天发布

**中文摘要：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局部电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。优化的内存管理策略消除了传统上与远程交互相关的训练开销，从而使 4G-HDNNP 能够以与本地对应物相同的效率进行训练。 RuNNer 2.0 采用现代 Fortran（2003/2008 标准）开发，结合​​混合 MPI/OpenMP 并行化方案，旨在在任何 CPU 环境（从经济高效的本地工作站到大规模 HPC 集群）中高效运行。其模块化库架构有助于直接绑定到外部模拟软件； LAMMPS 和原子仿真环境 (ASE) 的本机接口提供对其所有功能的完全访问，包括内置的基于委员会的不确定性量化。 RuNNer 2.0生态系统的高效率和可扩展性通过详细的基准测试得到证明。
**讨论重点：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局部电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 3. Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning

- Source: arXiv
- Date: 2026-07-20T15:55:37Z
- Venue: cond-mat.mtrl-sci
- Authors: Timo Reents, Marnik Bercx, Giovanni Pizzi
- Link: https://arxiv.org/abs/2607.18092v1
- Score: 14.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 由高通量密度泛函理论计算生成的晶体结构数据库通常作为计算材料发现工作的起点。热力学稳定性数据，例如地层能量和凸包上方的能量，是指导新型材料搜索的重要量，从而能够过滤（亚）稳定结构。在这里，我们展示了完全开源、可重复且以实验为重点的材料云三维晶体数据库 (MC3D) 的热力学稳定性。 我们与其他两个 DFT 数据库（开放量子材料数据库 (OQMD) 和材料项目 (MP)）以及实验形成焓进行比较。然后，我们演示如何利用最近在 r$^2$SCAN 级别训练的基础机器学习原子间势 (MLIP)（具体来说，我们在这里测试 PET-OMATPES）来提高形成能与实验的一致性，相对于 GGA 减少平均绝对误差超过 40%，而不需要任何额外的 DFT 计算。 我们的结果验证了将 PBEsol 几何形状与元 GGA 能量相结合的既定实践，并将其扩展到基础 MLIP 时代。最后，我们训练经典机器学习模型，以进一步纠正 Delta 学习框架中的形成能，其中我们使用基础 MLIP 的信息丰富的潜在特征。这些模型进一步将平均绝对误差降低到 50 meV/原子以下，使其降至与实验不确定性本身相当的值。 值得注意的是，与纯粹的组合特征相比，潜在特征（与仔细调整的正则化相结合）同时减少了预测误差并限制了学习校正对相对相位稳定性的影响。
**讨论重点：** 在这里，我们展示了完全开源、可重复且以实验为重点的材料云三维晶体数据库 (MC3D) 的热力学稳定性。然后，我们演示如何利用最近在 r$^2$SCAN 级别训练的基础机器学习原子间势 (MLIP)（具体来说，我们在这里测试 PET-OMATPES）来提高形成能与实验的一致性，相对于 GGA 减少平均绝对误差超过 40%，而不需要任何额外的 DFT 计算。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 4. Self-organized defect clustering and concentration-dependent vacancy diffusion in MoS$_2$

- Source: arXiv
- Date: 2026-07-16T12:59:35Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Aaron Flötotto, Benjamin Spetzler, Martin Ziegler, Erich Runge, Christian Dreßler
- Link: https://arxiv.org/abs/2607.14951v1
- Score: 10.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 硫空位迁移对电子传输和基于 MoS$_2$ 的器件（例如忆阻器和忆阻器）的功能行为具有至关重要的影响。根据最近的原子模拟，空位迁移通过协同、空位辅助的硫跃迁进行，这意味着缺陷动态密切相关。在这里，我们使用动力学蒙特卡罗模拟研究了 MoS$_2$ 中硫空位簇的集体行为，其转变率源自机器学习原子间势分子动力学模拟。 我们确定了三种传输机制：在低浓度下，空位不动或限制在小簇内，而在高浓度下，观察到具有恒定扩散系数的经典扩散传输，并且空位聚集成各向异性扩展的簇。明确定义的中间状态的特征是簇合并成具有浓度依赖性扩散系数的连接的波动网络。该机制的特点是簇大小分布广泛。 空位扩散系数对平均缺陷浓度的强烈依赖性为在 MoS$_2$ 中观察到的忆阻行为的起源提供了新的见解。
**讨论重点：** 在这里，我们使用动力学蒙特卡罗模拟研究了 MoS$_2$ 中硫空位簇的集体行为，其转变率源自机器学习原子间势分子动力学模拟。根据最近的原子模拟，空位迁移通过协同、空位辅助的硫跃迁进行，这意味着缺陷动态密切相关。 结合关键词看，阅读时应重点关注机器学习原子间势相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 5. Aromatic Molecule Solvation in Liquid Water with Coupled Cluster Accuracy: The Balance of Pi-Interactions and Hydrophobicity

- Source: arXiv
- Date: 2026-07-14T20:52:10Z
- Venue: physics.chem-ph
- Authors: Nore Stolte, Harald Forbert, Yury Lysogorskiy, Ralf Drautz, Dominik Marx
- Link: https://arxiv.org/abs/2607.13261v1
- Score: 8.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 水中的芳香族有机溶质在疏水性溶剂化和定向 O-H$\cdots π$ 氢键之间表现出微妙的平衡，但广泛使用的力场和最先进的密度泛函方法难以提供这些关键相互作用的一致图像。我们引入了一种数据高效的升级策略，以仅使用有限的分子簇来训练基于水性芳香族分子的图原子簇扩展的机器学习原子间势（MLIP），并具有 CCSD(T) 精度进行凝聚相模拟。 我们将我们的方法应用于甲苯水溶液 (C$_6$H$_5$CH$_3$)。由此产生的 CCSD(T) 质量 MLIP 大量再现了耦合的簇能量和力，并揭示了常用的方法无法捕获亲水性和疏水性溶剂化之间的关键平衡，从而扭曲了芳香族分子与其环境的相互作用。代表性的生物分子力场显着影响疏水溶剂化壳的结构，并使界面水定向错误，同时高估$π$-接触，产生不一致的溶剂化平衡。 即使是混合 DFT 和 MP2 也高估了水-$π$氢键断裂的障碍。我们的工作流程为 CCSD(T) 质量的水溶液凝聚相模拟提供了一条实用的通用途径，因此构建的相互作用势现在为对生物分子环境中的 $π$ 接触和疏水效应（例如水环境中蛋白质和 DNA 的溶剂化）进行一致、高精度的基准研究打开了大门。
**讨论重点：** 我们引入了一种数据高效的升级策略，以仅使用有限的分子簇来训练基于水性芳香族分子的图原子簇扩展的机器学习原子间势（MLIP），并具有 CCSD(T) 精度进行凝聚相模拟。 我们的工作流程为 CCSD(T) 质量的水溶液凝聚相模拟提供了一条实用的通用途径，因此构建的相互作用势现在为对生物分子环境中的 $π$ 接触和疏水效应（例如水环境中蛋白质和 DNA 的溶剂化）进行一致、高精度的基准研究打开了大门。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 6. Are Machine Learning Interatomic Potentials Truly Practical? A Benchmark of 23 Mainstream Models

- Source: arXiv
- Date: 2026-07-08T17:04:42Z
- Venue: cond-mat.mtrl-sci, cs.CE, physics.comp-ph
- Authors: Hanwen Kang, Tenglong Lu, Sheng Meng, Miao Liu
- Link: https://arxiv.org/abs/2607.07647v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。我们评估三个维度：预测准确性、MD 模拟吞吐量和原子可扩展性。 我们的结果揭示了精确度与效率之间的巨大权衡：大型 SOTA 模型的精确度仅比轻量级模型高出 3-5 meV/atom，但吞吐量却损失了几个数量级——在最坏的情况下，仅比 DFT 本身快一点点。相比之下，轻量级 MLIP 位于帕累托前沿并在适度的硬件上运行。教训是，单维基准会误导该领域，未来的 MLIP 开发应该重视效率和可扩展性以及准确性。
**讨论重点：** 我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. MLIP Studio: An Open Platform for Interactive Benchmarking and Atomistic Simulations Using Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-08T16:23:57Z
- Venue: cond-mat.mtrl-sci
- Authors: Manas Sharma, Sudeep Punnathanam, Ananth Govind Rajan
- Link: https://arxiv.org/abs/2607.07606v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 通用机器学习原子间势（MLIP）是改变原子模拟的基础人工智能模型，但其实际使用仍然受到分散的软件生态系统、依赖性冲突和缺乏可用的基准测试工具的阻碍。这些模型以一小部分计算成本实现了第一原理密度泛函理论 (DFT) 的精度。我们推出了 MLIP Studio（可在 https://mlipstudio.iisc.ac.in 获取），这是一个开放且免费的平台，可将 60 多种通用 MLIP 引入分子和材料的统一交互界面中。 该平台支持端到端 MLIP 驱动的工作流程，包括属性预测、几何优化、振动和状态方程分析、自旋状态确定、自定义模型部署以及针对参考数据的高通量基准测试。自动奇偶图和可排序误差表有助于快速识别元素异常值和有问题的数据点。我们证明基于 MLIP 的预优化可以减少后续 DFT 优化工作约 33$\times$。此外，该应用程序还可以对计算性能进行基准测试。 通过涉及蓝宝石基板上的二维磁性材料 CrCl$_3$ 的综合案例研究，我们展示了各种属性和势能景观的跨模型比较如何指导特定任务的 MLIP 选择。总体而言，MLIP Studio 降低了在计算化学和材料科学的端到端研究工作流程、基准测试和教育中可靠使用基础模型的障碍。
**讨论重点：** 我们推出了 MLIP Studio（可在 https://mlipstudio.iisc.ac.in 获取），这是一个开放且免费的平台，可将 60 多种通用 MLIP 引入分子和材料的统一交互界面中。通过涉及蓝宝石基板上的二维磁性材料 CrCl$_3$ 的综合案例研究，我们展示了各种属性和势能景观的跨模型比较如何指导特定任务的 MLIP 选择。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 8. dpti: An Automated Thermodynamic Integration Workflow for Phase Diagram Calculations with Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-06T12:56:52Z
- Venue: physics.comp-ph, cond-mat.mtrl-sci
- Authors: Fengbo Yuan, Xin Zhong, Donghao Zheng, Jinzhe Zeng, Linfeng Zhang, Han Wang
- Link: https://arxiv.org/abs/2607.05015v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 热力学积分 (TI) 是一种广泛使用的计算自由能和相图的方法。然而，由机器学习原子间势 (MLIP) 驱动的 TI 计算在技术上仍然具有挑战性，因为它们需要仔细设计可逆积分路径以及每个相和状态点的许多密切相关的分子动力学 (MD) 任务。 为了应对这些挑战，我们推出了 dpti，这是一个开源 Python 软件包，可自动执行使用 MLIP 进行相图计算的 TI 工作流程。 dpti 通过可逆积分路径将具有分析已知自由能的参考系统连接到 MLIP 描述的原子和分子固体和液体。给定 JSON 输入文件，dpti 生成并运行所需的 MD 任务，计算自由能贡献，估计误差，并将共存点传播到相边界。 我们通过深势模型驱动的两个示例演示了 dpti 的用法：涉及 β-石英、柯石英和熔体的二氧化硅相图，以及冰 Ih-液态水相边界。 dpti 提供了一个有用的工具，用于自动计算 MLIP 建模的材料的相图。
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

**中文摘要：** 机器学习原子间势（MLIP）已成为科学模拟人工智能的标志。虽然对新架构和数据集的努力导致了模型越来越准确和通用，但训练优化器的选择在很大程度上仍未被探索，默认为 Adam 及其在社区中的变体。在这里，我们实现并系统地比较了一类最近提出的矩阵结构优化器，包括 Muon、SOAP 和混合 SOAP-Muon，用于训练 NequIP 和 Allegro MLIP 模型。 我们发现这些优化器在收敛速度和最终精度方面都明显优于 Adam。 SOAP 和 SOAP-Muon 作为稳健且始终如一的强大方法而出现，而 Muon 相对于 Adam 只提供了部分收益。在部分部队监督下，这些改进尤其明显。我们的结果表明，优化器选择是 MLIP 的一个被忽视但有影响力的设计轴。
**讨论重点：** 我们的结果表明，优化器选择是 MLIP 的一个被忽视但有影响力的设计轴。虽然对新架构和数据集的努力导致了模型越来越准确和通用，但训练优化器的选择在很大程度上仍未被探索，默认为 Adam 及其在社区中的变体。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Valley polarization, Rashba interaction, and weak altermagnetism in inversion-asymmetric MnPS$_\text{3}|$WS$_\text{2}$ van der Waals heterostructures

- Source: arXiv
- Date: 2026-07-17T18:51:51Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, cond-mat.str-el
- Authors: Purba Dutta, Soumajyoti Bid, Nirmal Ganguli
- Link: https://arxiv.org/abs/2607.16454v1
- Score: 31.0
- Match: 摘要匹配 magnetoelectric coupling; 摘要匹配 ferromagnetism; 标题匹配 altermagnetism; 摘要匹配 altermagnetic

**中文摘要：** 最近，故意破坏反铁磁体中的反演对称性（$\mathcal{P}$）已成为诱导各种特征的有效手段，例如贝里曲率的出现、自旋谷锁定、磁电耦合以及从传统反铁磁性到交替磁性的转变。相反，在非磁性系统中，在存在强自旋轨道相互作用（SOI）的情况下，反演对称性的破坏会通过拉什巴效应产生动量相关的自旋分裂，从而能够通过外部电场实现可调谐的自旋极化。 受二维材料最新进展的推动，我们基于密度泛函理论进行第一性原理计算，以研究由 $\mathcal{P}$ 对称 MnPS$_3$ 单层和 WS$_2$ 单层形成的范德华（vdW）异质结构。我们证明该界面具有丰富的相互作用的涌现现象，包括交变磁相、拉什巴自旋分裂、自旋谷锁定和谷极化。 我们的结果表明，异质结构表现出半导体行为，直接带隙约为 1.65~eV，并且具有 I 型能带排列。值得注意的是，电子结构和能带排列可以通过外部电场和面内双轴应变在 I 型和 II 型区域之间有效调节。此外，场感应调制能够对交变磁相和谷分裂进行强有力的控制。 这些发现确立了所提出的 vdW 异质结构作为一个高度可调的平台，在自旋电子学和谷电子学应用中具有巨大的潜力。
**讨论重点：** 受二维材料最新进展的推动，我们基于密度泛函理论进行第一性原理计算，以研究由 $\mathcal{P}$ 对称 MnPS$_3$ 单层和 WS$_2$ 单层形成的范德华（vdW）异质结构。相反，在非磁性系统中，在存在强自旋轨道相互作用（SOI）的情况下，反演对称性的破坏会通过拉什巴效应产生动量相关的自旋分裂，从而能够通过外部电场实现可调谐的自旋极化。 结合关键词看，阅读时应重点关注磁电耦合、铁磁性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Interface-Engineered Giant Multistate Resistance Switching in Altermagnetic CrSb Multiferroic Tunnel Junctions

- Source: arXiv
- Date: 2026-07-17T08:05:43Z
- Venue: cond-mat.mtrl-sci
- Authors: Zhi Yan, Yuwen Hua, Yueting Li, Xujin Zhang, Jianhua Xiao, Xiaohong Xu
- Link: https://arxiv.org/abs/2607.15728v1
- Score: 28.0
- Match: 标题匹配 multiferroic; 标题匹配 altermagnetic; 标题匹配 altermagnet; 近两周发布

**中文摘要：** 交变磁体能够在没有杂散磁场的情况下实现自旋分裂传输，但将其动量相关的自旋分裂转换为强隧道结响应需要界面选择的隧道通道。在这里，利用密度泛函理论与非平衡格林函数计算相结合，我们证明了 CrSb/$α$-In$_2$Se$_3$ 交变磁性多铁性隧道结中的巨大多态电阻切换。 响应不仅仅由 CrSb 的体自旋分裂控制，而是由对称选择的界面机制控制，其中 Cr/Sb 终端和 \textit{h}-BN 或石墨烯插入层决定自旋通道匹配，而铁电极化重塑静电势垒。对称和不对称终端反转了平行/反平行 Néel 矢量配置和高/低电阻状态之间的对应关系，表明界面 Cr 矩的实际排列选择了主要的隧道通道。 单层In$_2$Se$_3$结表现出四种非易失性电阻状态，隧道磁阻（TMR）和隧道电阻（TER）分别达到1626\%和2206\%，在费米能级位移时增加到9576\%和4144\%。有限偏置计算进一步揭示了强大的自旋过滤和可调自旋极化电流。将势垒扩展到双层 In$_2$Se$_3$ 引入了层间偏振耦合，从而实现了八种电阻态，最大 TMR 和 TER 值分别为 $3.77\times10^{4}\%$ 和 $4.18\times10^{5}\%$。 这些结果确立了界面对称、自旋通道匹配和铁电势垒重建作为无杂散场多态自旋电子隧道器件的设计原则。
**讨论重点：** 这些结果确立了界面对称、自旋通道匹配和铁电势垒重建作为无杂散场多态自旋电子隧道器件的设计原则。在这里，利用密度泛函理论与非平衡格林函数计算相结合，我们证明了 CrSb/$α$-In$_2$Se$_3$ 交变磁性多铁性隧道结中的巨大多态电阻切换。 结合关键词看，阅读时应重点关注多铁性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Electrical Control of Altermagnetism in a Quasi-1D Magnet

- Source: arXiv
- Date: 2026-07-18T15:44:13Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall
- Authors: Alberto M. Ruiz, Cuiju Yu, Diego López-Alcalá, Jose L. Lado, Adolfo O. Fumega, José J. Baldoví
- Link: https://arxiv.org/abs/2607.16856v1
- Score: 26.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交替磁性是一种共线磁态，其特征是完全补偿材料中动量相关的自旋分裂。虽然在三维或二维交换相互作用控制的系统中得到了广泛的研究，但它向准一维磁体的扩展几乎仍未被探索。重点关注实验建立的 AgCrP$_2$S$_6$ 范德华磁体，我们证明嵌入二维晶格中的反铁磁链提供了交变磁性的一般途径。 结合第一性原理计算和自旋空间群分析，我们证明面外对称性破缺可以产生非相对论性 d 波自旋分裂。外部平面外电场验证了这种机制，其中感应分裂随场强线性增加，并随场方向反转符号。我们通过构建有效的紧束缚模型来合理化这种行为，该模型将交变磁响应与各向异性第三邻居链间跳跃联系起来。 此外，我们还表明，Janus 取代还会引起 d 波自旋织构，而与 CuInP$_2$S$_6$ 的铁电界面能够在完全补偿的亚铁磁状态下实现偏振控制的自旋分裂带。我们的结果将准一维反铁磁体建立为交变磁性的基础。
**讨论重点：** 我们通过构建有效的紧束缚模型来合理化这种行为，该模型将交变磁响应与各向异性第三邻居链间跳跃联系起来。虽然在三维或二维交换相互作用控制的系统中得到了广泛的研究，但它向准一维磁体的扩展几乎仍未被探索。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Stripe-Order Altermagnetism

- Source: arXiv
- Date: 2026-07-20T14:30:09Z
- Venue: cond-mat.mes-hall, cond-mat.mtrl-sci, cond-mat.str-el
- Authors: Zheng-Yang Zhuang, Zhongbo Yan
- Link: https://arxiv.org/abs/2607.17997v1
- Score: 25.0
- Match: 标题匹配 altermagnetism; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁学将补偿磁序与非相对论性自旋分裂相结合，但已建立的机制主要依赖于尼尔级反铁磁体中的自旋反转。在这里，我们建立了由自旋反转镜控制的条序交变磁力，将其置于通常的基于旋转的 $l$ 波分类之外。使用双轨道模型，我们表明条纹自旋和轨道顺序的相互作用产生两个阶段：具有镜像选择向列自旋分裂的条纹交变磁体和具有自旋简并带的条纹反交变磁体。 后者可以支持在合适的屈曲结构中对自旋分裂进行类似铁电的电控制。随机相位近似（RPA）计算表明，在强跳跃各向异性下，接近半填充时，带状交变磁性更受青睐。自旋反转镜还对平行或垂直于镜面的电场施加纯横向自旋电流，从而提供直接传输诊断。
**讨论重点：** 交变磁学将补偿磁序与非相对论性自旋分裂相结合，但已建立的机制主要依赖于尼尔级反铁磁体中的自旋反转。在这里，我们建立了由自旋反转镜控制的条序交变磁力，将其置于通常的基于旋转的 $l$ 波分类之外。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 5. Altermagnetism without a long-range order

- Source: arXiv
- Date: 2026-07-17T13:42:06Z
- Venue: cond-mat.str-el
- Authors: V. E. Valiulin, A. V. Mikheyenkov, K. I. Kugel
- Link: https://arxiv.org/abs/2607.15954v1
- Score: 25.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** Kugel-Khomskii 自旋-赝自旋模型最初是为具有轨道自由度的过渡金属化合物而开发的，最近在交变磁性的背景下得到了重新解释。在这项工作中，我们从理论上研究了在没有长程磁序或轨道序的情况下交变磁行为的出现。使用旋转不变格林函数方法来构建方晶格和线性链上的 SU(2) x SU(2) 对称模型，我们分析了自旋-自旋和自旋-赝自旋相关函数、激发光谱、热容和磁化率。 我们表明，除了关键的子系统间交换 Kc(T) 之外，即使每个位点的平均自旋和赝自旋为零，也会出现具有非零自旋-赝自旋相关性的复合态。激发谱分为声学和光学分支，节点线沿 qx = qy - 交变磁对称的直接特征。在相界处观察到热容量的峰值和磁化率的跳跃。在一维中，相界是非单调的并且表现出重入转变。 这些结果建立了“交变顺磁体”或“交变磁液体”的概念，没有长程有序，与低维和强波动系统相关。
**讨论重点：** 在这项工作中，我们从理论上研究了在没有长程磁序或轨道序的情况下交变磁行为的出现。 Kugel-Khomskii 自旋-赝自旋模型最初是为具有轨道自由度的过渡金属化合物而开发的，最近在交变磁性的背景下得到了重新解释。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 6. Altermagnetic spin textures coupled to superconductors: Domain wall spin-triplet superconductivity and supercurrent-induced torques

- Source: arXiv
- Date: 2026-07-16T17:46:41Z
- Venue: cond-mat.supr-con, cond-mat.mes-hall
- Authors: Yasir Dar, Mathias S. Scheurer, Constantin Schrade
- Link: https://arxiv.org/abs/2607.15249v1
- Score: 24.0
- Match: 摘要匹配 altermagnetism; 标题匹配 altermagnetic; 标题匹配 altermagnet; 近两周发布

**中文摘要：** 由于不存在相当大的杂散场以及最近发现的交变磁织构对流动电子的非常重要的影响，我们在这里研究与传统$s$波超导体耦合的空间变化交变磁体中的库珀对的形式。由于交变磁性对自旋单重态配对的有害影响以及磁序参数中的纹理引起的局部对称性降低，我们表明超导性主要影响交变磁域之间的区域。 着眼于具体的平面径向磁畴壁，我们证明了涌现的塞曼场和自旋轨道场产生了空间上分离的三重态热点以及节点和全间隙超导区域之间的过渡，其结构由磁畴壁和交变磁序参数决定。我们还确定了一种交互效应，其中超电流产生准粒子介导的四极扭矩，该扭矩继承了交变磁序的对称性。 我们的结果表明，考虑交变磁序参数的空间不均匀性对于理解超导邻近效应至关重要，并表明交变磁织构和超导体的混合系统为库珀对的局部工程和检测交变磁序提供了独特的机会。
**讨论重点：** 由于不存在相当大的杂散场以及最近发现的交变磁织构对流动电子的非常重要的影响，我们在这里研究与传统$s$波超导体耦合的空间变化交变磁体中的库珀对的形式。由于交变磁性对自旋单重态配对的有害影响以及磁序参数中的纹理引起的局部对称性降低，我们表明超导性主要影响交变磁域之间的区域。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 7. Emergent d-wave altermagnetism in chlorine-adsorbed FeSe monolayer

- Source: arXiv
- Date: 2026-07-16T16:57:03Z
- Venue: cond-mat.mtrl-sci
- Authors: Zi-Hao Ding, Ze-Feng Gao, Kai Liu, Peng-Jie Guo, Zhong-Yi Lu
- Link: https://arxiv.org/abs/2607.15197v1
- Score: 24.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 近两周发布

**中文摘要：** 最近出现的交变磁学开辟了凝聚态物理的新领域，但能够同时具有内在交变磁序和超导性的材料平台仍然极其罕见。在这里，基于对称性分析和第一性原理计算，我们提出了一种在单层 FeSe（一种典型的铁基超导体）中设计鲁棒交变磁性的现实途径。通过单侧 Cl 吸附设计化学计量的 Fe2Se2Cl 结构并引入栅极可调空穴掺杂，我们实现了高度稳定的交变磁基态。 我们的计算揭示了一种协同机制：空穴掺杂牢固地稳定了棋盘磁序，而不对称配体环境本质上打破了面外空间反演对称性。因此，这种相互作用会引发高达 620 meV 的巨大交变自旋分裂。至关重要的是，我们证明了这种交变磁态及其巨大的自旋分裂具有高度弹性，即使在精确模拟体积极限的 10 层板模型中也能持续存在。 通过将交变磁性引入成熟的 FeSe 基超导家族，我们的研究结果表明 Fe2Se2Cl 是自旋电子应用的一个有前途的平台，并激发了未来对交变磁性和超导之间可能相互作用的研究。
**讨论重点：** 在这里，基于对称性分析和第一性原理计算，我们提出了一种在单层 FeSe（一种典型的铁基超导体）中设计鲁棒交变磁性的现实途径。至关重要的是，我们证明了这种交变磁态及其巨大的自旋分裂具有高度弹性，即使在精确模拟体积极限的 10 层板模型中也能持续存在。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 8. First-Order Topological FFLO Transition and Superconducting Diode Sign Reversal in Altermagnetic Nanowires

- Source: arXiv
- Date: 2026-07-17T07:55:36Z
- Venue: cond-mat.supr-con
- Authors: Bo Fu, Kaizhi Bai, Chang-An Li, Shun-Qing Shen
- Link: https://arxiv.org/abs/2607.15720v1
- Score: 21.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 近两周发布

**中文摘要：** Fulde-Ferrell-Larkin-Ovchinnikov (FFLO) 态通常通过有限磁化驱动的二阶相变出现。在这里，我们表明，接近$d$波交替磁体的自旋轨道耦合纳米线（净磁化强度为零）可以通过一阶跃迁实现拓扑FFLO状态，其特征是尖锐的符号反转超导二极管效应。交变磁场产生带分辨的竞争配对通道，从而产生双谷自由能景观，其全局最小值不连续地切换。 因此，它会导致一阶拓扑 FFLO 跃迁，同时库珀配对振幅和有限质心动量发生跳跃。值得注意的是，这种不连续的拓扑重新配置大大提高了二极管效率，并在过渡期间驱动特征性的尖锐符号反转。金兹堡-朗道理论捕捉到了这种奇异现象的机制。我们的结果为拓扑 FFLO 状态提供了一条无场交变磁路线，并识别了它们的直接传输指纹。
**讨论重点：** Fulde-Ferrell-Larkin-Ovchinnikov (FFLO) 态通常通过有限磁化驱动的二阶相变出现。在这里，我们表明，接近$d$波交替磁体的自旋轨道耦合纳米线（净磁化强度为零）可以通过一阶跃迁实现拓扑FFLO状态，其特征是尖锐的符号反转超导二极管效应。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 9. $J_{1} - J_{2} - δ$ model on a square lattice: From Altermagnet to Columnar antiferromagnet via quantum disordered phase

- Source: arXiv
- Date: 2026-07-17T18:06:05Z
- Venue: cond-mat.str-el
- Authors: Subharthi Paul, Darshan G. Joshi
- Link: https://arxiv.org/abs/2607.16415v1
- Score: 18.0
- Match: 摘要匹配 altermagnetism; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 局部矩磁体的交变磁性的特征是在没有任何自旋各向异性相互作用或外部场的情况下，零净磁化强度和相反手性磁振子带的分裂。在这项工作中，我们研究了交流磁体对磁挫败引起的量子涨落的鲁棒性。我们考虑方形晶格上的海森堡模型，除了最近邻相互作用之外，还具有两种不同类型的第二邻域相互作用（如棋盘图案）。 该模型在方格上的 $J_{1}-J_{2}$ 海森堡模型和棋盘格上的海森堡模型之间连续插值。对于较弱的第二邻域相互作用，实现了尼尔型交变磁体相。另一方面，为了增强第二邻域相互作用，出现了柱状反铁磁体。利用线性自旋波理论，我们计算了两个磁相的磁振子色散、有序参数、静态和动态结构因子。 此外，我们还表明存在一个中间量子无序相将两个磁相分开，该相与 $J_{1}-J_{2}$ 模型中实现的相相关。当我们向棋盘晶格极限调整时，量子无序区域进一步稳定。
**讨论重点：** 在这项工作中，我们研究了交流磁体对磁挫败引起的量子涨落的鲁棒性。我们考虑方形晶格上的海森堡模型，除了最近邻相互作用之外，还具有两种不同类型的第二邻域相互作用（如棋盘图案）。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 10. Quantum-metric-driven light-induced ferrovalley state in d-wave altermagnets

- Source: arXiv
- Date: 2026-07-19T03:26:26Z
- Venue: cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Shihao Zhang
- Link: https://arxiv.org/abs/2607.17049v1
- Score: 16.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 将量子度量与贝里曲率分离仍然是量子材料中的一个核心挑战，因为这两个几何量几乎总是共存，并且它们的贡献很难分开。我们证明，d 波交替磁体构成了克服这一障碍的理想平台，其真正的哈密顿量具有严格消失的贝里曲率。 使用马格努斯展开式和精确的 Floquet 对角化，我们证明了线性偏振非共振光通过纯粹的量子度量介导的带隙重正化驱动轨道选择性铁谷相，在任何阶次都没有贝里曲率贡献。轨道选择性源于跳跃各向异性，它在 $d_{xz}$ 和 $d_{yz}$ 轨道之间产生明显的度量各向异性，并且间隙减小以量子度量的形式解析表示。 由此产生的谷间隙差异提供了量子度量的直接定量测量，可用于自旋分辨 ARPES 和光学泵浦探针光谱。这将 d 波交替磁体建立为一个原始的可调谐平台，其中可以隔离量子度量效应，通过光偏振控制，并通过谷偏振读出。
**讨论重点：** 由此产生的谷间隙差异提供了量子度量的直接定量测量，可用于自旋分辨 ARPES 和光学泵浦探针光谱。我们证明，d 波交替磁体构成了克服这一障碍的理想平台，其真正的哈密顿量具有严格消失的贝里曲率。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。
