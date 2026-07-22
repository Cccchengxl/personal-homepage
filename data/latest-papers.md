# Latest papers for 程旭丽

Updated: 2026-07-22T09:19:39.774256+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Study of ordering in (MoCrTi)$_{100-x}$Al$_x$ refractory high-entropy alloys using machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-20T16:01:06Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn
- Authors: Jiyao Zhang, Klemens Lechner, Markus Maßwohl, Petra Spoerk-Erdely, David Holec
- Link: https://arxiv.org/abs/2607.18099v1
- Score: 17.0
- Match: 标题匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 耐火高熵合金由于其优异的机械性能而成为高温应用的有希望的候选者。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。在这项工作中，通过利用通用机器学习原子间势与混合蒙特卡罗和分子动力学模拟，研究了(MoCrTi)(100-x)Alx系统的温度依赖性热力学和机械性能。 热容和短程有序参数揭示了不同的有序-无序转变行为。虽然 Mo25Cr25Ti25Al25 和 Mo32Cr32Ti32Al4 合金表现出由 B2 型原子对的协同排序主导的单一转变，但 Mo28Cr28Ti28Al16 和 Mo30Cr30Ti30Al10 合金表现出两个单独的转变：由特定对驱动的低温阶段（Mo28Cr28Ti28Al16 中的 Mo-Al；Mo28Cr28Ti28Al16 中的 Al-Al） Mo30Cr30Ti30Al10) 和由其余对控制的高温阶段。 结构分析表明，在低温有序B2相中，Mo和Al共享一个亚晶格，而Cr和Ti共享另一个亚晶格。此外，还确定了排序和机械刚度之间的关系。有序显着增强了弹性常数和模量，并产生非单调的成分依赖性。与随机固溶体不同的是，随机固溶体的刚度随着 Al 含量的减少而单调增加，有序构型表现出非单调趋势，在 Mo30Cr30Ti30Al10 合金中达到峰值。 这种增强归因于强短程有序引起的刚性原子对的优化群体。这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。
**讨论重点：** 这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 2. RuNNer 2.0: A Software Suite for High-Dimensional Neural Network Potentials

- Source: arXiv
- Date: 2026-07-20T14:13:35Z
- Venue: physics.chem-ph, cond-mat.mtrl-sci, physics.comp-ph
- Authors: Alexander L. M. Knoll, Moritz R. Schäfer, K. Nikolas Lausch, Moritz Gubler, Henry Wang, Richard Springborn
- Link: https://arxiv.org/abs/2607.17978v1
- Score: 17.0
- Match: 标题匹配 neural network potential; 最近 3 天发布

**中文摘要：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局部电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。优化的内存管理策略消除了传统上与远程交互相关的训练开销，从而使 4G-HDNNP 能够以与本地对应物相同的效率进行训练。 RuNNer 2.0 采用现代 Fortran（2003/2008 标准）开发，结合​​混合 MPI/OpenMP 并行化方案，旨在在任何 CPU 环境（从经济高效的本地工作站到大规模 HPC 集群）中高效运行。其模块化库架构有助于直接绑定到外部模拟软件； LAMMPS 和原子仿真环境 (ASE) 的本机接口提供对其所有功能的完全访问，包括内置的基于委员会的不确定性量化。 RuNNer 2.0生态系统的高效率和可扩展性通过详细的基准测试得到证明。
**讨论重点：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局部电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 3. ATLAS: A Foundation Neural Sampler for Amorphous Materials

- Source: arXiv
- Date: 2026-07-21T15:31:49Z
- Venue: cond-mat.mtrl-sci, cs.LG, physics.comp-ph
- Authors: Mouyang Cheng, Denis Blessing, Botao Yu, Gerhard Neumann, Mingda Li, Carles Domingo-Enrich
- Link: https://arxiv.org/abs/2607.19198v1
- Score: 14.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 非晶材料表现出卓越的机械和功能特性，但其崎岖的能量景观却非常难以采样。在玻璃化转变温度以下，传统的分子动力学和蒙特卡罗变得低效，因为平衡依赖于罕见的跨越障碍事件，而数据驱动的生成模型受到稀缺和有偏见的参考系的限制。在这里，我们介绍 ATLAS，这是一种高效的采样器，它可以学习扩散过程，直接从目标能量函数生成玻尔兹曼分布的非晶结构。 ATLAS 通过等变图神经网络进行参数化，可概括系统大小、温度和组成。通过利用扩散过程的时间反转，它可以有效地估计热力学量并引导目标可观测值。在二维 Kob-Andersen 系统中，ATLAS 再现了平行回火马尔可夫链蒙特卡罗结构分布、自由能和熵，在低温玻璃状态下实现了低于 0.2% 的自由能误差，能量评估减少了 500 倍以上。 在 Cu-Zr 和 Cr-Co-Ni 金属玻璃中，ATLAS 恢复了实验观察到的短程有序趋势，并将结构引导向规定的有序参数和优化的体积模量。此外，成分摊销预训练的性能优于从头开始的特定成分训练，将逆向设计成本降低了数百倍，并且能够使用昂贵的通用机器学习原子间势进行采样。 与大型语言模型代理相结合，ATLAS 在八元素空间中搜索平衡刚度和延展性的高熵金属玻璃，在 480 个预言评估中识别出收敛的帕累托前沿。总之，这些结果将 ATLAS 确立为非晶材料采样、控制和设计的基础模型。
**讨论重点：** 在这里，我们介绍 ATLAS，这是一种高效的采样器，它可以学习扩散过程，直接从目标能量函数生成玻尔兹曼分布的非晶结构。与大型语言模型代理相结合，ATLAS 在八元素空间中搜索平衡刚度和延展性的高熵金属玻璃，在 480 个预言评估中识别出收敛的帕累托前沿。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 4. Data-driven Design of Metal-Organic Frameworks with Tunable Negative Thermal Expansion

- Source: arXiv
- Date: 2026-07-21T00:02:56Z
- Venue: cond-mat.mtrl-sci
- Authors: Prathami Divakar Kamath, Francesco Tavani, Alin Marin Elena, Théo Jaffrelot Inizan, Yen-hsu Lin, Jian Yin
- Link: https://arxiv.org/abs/2607.18594v1
- Score: 13.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 具有负热膨胀 (NTE) 的材料对于需要精确控制热膨胀的应用至关重要。由于其卓越的化学可调性、灵活的结构和低能晶格振动，金属有机框架（MOF）代表了探索 NTE 的丰富平台。然而，在巨大的 MOF 设计空间中揭示控制 NTE 的结构基序仍然在实验上具有挑战性，而且大规模的第一原理声子计算在计算上是令人望而却步的。 在这里，我们利用基于 MACE-MP-MOF0（一种针对 MOF 进行近乎从头精度微调的机器学习原子间势）的高通量工作流程，全面评估影响 MOF 中 NTE 的因素，构建 PhononMOFdb，这是超过 12,000 个 MOF 的声子、非弹性中子散射谱、体积模量和热容的数据库。 该数据库的高通量筛选表明，具有较重、价较低的金属节点的高多孔立方拓扑框架有利于强 NTE，而链接器功能化为调整 NTE 大小和符号而不损害机械稳定性提供了实用的方法。通过对 Ce-UiO-66 MOF 及其溴化变体进行高分辨率温度依赖性同步加速器粉末 X 射线衍射进行的实验验证证实了设计配方，并产生了超越当前记录的体积 NTE 系数。 这项工作为 MOF 中的 NTE 工程建立了数据驱动的策略，展示了机器学习加速发现和有针对性的实验验证如何共同解锁预测材料设计。
**讨论重点：** 然而，在巨大的 MOF 设计空间中揭示控制 NTE 的结构基序仍然在实验上具有挑战性，而且大规模的第一原理声子计算在计算上是令人望而却步的。由于其卓越的化学可调性、灵活的结构和低能晶格振动，金属有机框架（MOF）代表了探索 NTE 的丰富平台。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 5. Towards a universal model for spin-orbit coupled Wannier Hamiltonians

- Source: arXiv
- Date: 2026-07-20T18:00:35Z
- Venue: cond-mat.mtrl-sci
- Authors: Alexander C. Tyner
- Link: https://arxiv.org/abs/2607.18403v1
- Score: 13.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 虽然机器学习原子间势 (MLiP) 已经成熟并彻底改变了材料科学，但电子结构的深度学习模型才刚刚开始出现，并且几乎完全局限于非正交基础哈密顿量。我们介绍 G(Wa)NN，这是第一个能够在正交 Wannier 基础上生成固态系统电子哈密顿量的深度学习模型。 G(Wa)NN 在前所未有的多样化数据集上进行训练，该数据集包含超过 111K 个 Wannier Hamiltonian（150M+ 跳跃矩阵），涵盖 69 个元素。 正交哈密顿量的优化推理和线性缩放方法的结合解锁了大规模（10K+原子）的输运模拟。至关重要的是，该框架支持局部微调，允许用户使基本模型适应自定义 Wannier Hamiltonian 数据集。为了将这些预测无缝地转化为物理可观测值，我们引入了 Tailwater，这是一个 Python 包，提供 G(Wa)NN 的 API 接口以及高性能后处理库。 Tailwater 能够将预测的哈密顿量自动投影到任意低能子空间（直接镜像熟悉的 Wannier90 工作流程），并包括一套核多项式方法 (KPM) 函数，这些函数利用正交基础来实现光谱可观测值的严格线性缩放。 Tailwater 生态系统以 G(Wa)NN 模型为核心，旨在帮助弥合深度学习和宏观量子传输模拟之间的差距。
**讨论重点：** 我们介绍 G(Wa)NN，这是第一个能够在正交 Wannier 基础上生成固态系统电子哈密顿量的深度学习模型。 G(Wa)NN 在前所未有的多样化数据集上进行训练，该数据集包含超过 111K 个 Wannier Hamiltonian（150M+ 跳跃矩阵），涵盖 69 个元素。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 6. Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning

- Source: arXiv
- Date: 2026-07-20T15:55:37Z
- Venue: cond-mat.mtrl-sci
- Authors: Timo Reents, Marnik Bercx, Giovanni Pizzi
- Link: https://arxiv.org/abs/2607.18092v1
- Score: 13.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 由高通量密度泛函理论计算生成的晶体结构数据库通常作为计算材料发现工作的起点。热力学稳定性数据，例如地层能量和凸包上方的能量，是指导新型材料搜索的重要量，从而能够过滤（亚）稳定结构。在这里，我们展示了完全开源、可重复且以实验为重点的材料云三维晶体数据库 (MC3D) 的热力学稳定性。 我们与其他两个 DFT 数据库（开放量子材料数据库 (OQMD) 和材料项目 (MP)）以及实验形成焓进行比较。然后，我们演示如何利用最近在 r$^2$SCAN 级别训练的基础机器学习原子间势 (MLIP)（具体来说，我们在这里测试 PET-OMATPES）来提高形成能与实验的一致性，相对于 GGA 减少平均绝对误差超过 40%，而不需要任何额外的 DFT 计算。 我们的结果验证了将 PBEsol 几何形状与元 GGA 能量相结合的既定实践，并将其扩展到基础 MLIP 时代。最后，我们训练经典机器学习模型，以进一步纠正 Delta 学习框架中的形成能，其中我们使用基础 MLIP 的信息丰富的潜在特征。这些模型进一步将平均绝对误差降低到 50 meV/原子以下，使其降至与实验不确定性本身相当的值。 值得注意的是，与纯粹的组合特征相比，潜在特征（与仔细调整的正则化相结合）同时减少了预测误差并限制了学习校正对相对相位稳定性的影响。
**讨论重点：** 在这里，我们展示了完全开源、可重复且以实验为重点的材料云三维晶体数据库 (MC3D) 的热力学稳定性。然后，我们演示如何利用最近在 r$^2$SCAN 级别训练的基础机器学习原子间势 (MLIP)（具体来说，我们在这里测试 PET-OMATPES）来提高形成能与实验的一致性，相对于 GGA 减少平均绝对误差超过 40%，而不需要任何额外的 DFT 计算。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. Self-organized defect clustering and concentration-dependent vacancy diffusion in MoS$_2$

- Source: arXiv
- Date: 2026-07-16T12:59:35Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Aaron Flötotto, Benjamin Spetzler, Martin Ziegler, Erich Runge, Christian Dreßler
- Link: https://arxiv.org/abs/2607.14951v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 硫空位迁移对电子传输和基于 MoS$_2$ 的器件（例如忆阻器和忆阻器）的功能行为具有至关重要的影响。根据最近的原子模拟，空位迁移通过协同、空位辅助的硫跃迁进行，这意味着缺陷动态密切相关。在这里，我们使用动力学蒙特卡罗模拟研究了 MoS$_2$ 中硫空位簇的集体行为，其转变率源自机器学习原子间势分子动力学模拟。 我们确定了三种传输机制：在低浓度下，空位不动或限制在小簇内，而在高浓度下，观察到具有恒定扩散系数的经典扩散传输，并且空位聚集成各向异性扩展的簇。明确定义的中间状态的特征是簇合并成具有浓度依赖性扩散系数的连接的波动网络。该机制的特点是簇大小分布广泛。 空位扩散系数对平均缺陷浓度的强烈依赖性为在 MoS$_2$ 中观察到的忆阻行为的起源提供了新的见解。
**讨论重点：** 在这里，我们使用动力学蒙特卡罗模拟研究了 MoS$_2$ 中硫空位簇的集体行为，其转变率源自机器学习原子间势分子动力学模拟。根据最近的原子模拟，空位迁移通过协同、空位辅助的硫跃迁进行，这意味着缺陷动态密切相关。 结合关键词看，阅读时应重点关注机器学习原子间势相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 8. Are Machine Learning Interatomic Potentials Truly Practical? A Benchmark of 23 Mainstream Models

- Source: arXiv
- Date: 2026-07-08T17:04:42Z
- Venue: cond-mat.mtrl-sci, cs.CE, physics.comp-ph
- Authors: Hanwen Kang, Tenglong Lu, Sheng Meng, Miao Liu
- Link: https://arxiv.org/abs/2607.07647v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。我们评估三个维度：预测准确性、MD 模拟吞吐量和原子可扩展性。 我们的结果揭示了精确度与效率之间的巨大权衡：大型 SOTA 模型的精确度仅比轻量级模型高出 3-5 meV/atom，但吞吐量却损失了几个数量级——在最坏的情况下，仅比 DFT 本身快一点点。相比之下，轻量级 MLIP 位于帕累托前沿并在适度的硬件上运行。教训是，单维基准会误导该领域，未来的 MLIP 开发应该重视效率和可扩展性以及准确性。
**讨论重点：** 我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. MLIP Studio: An Open Platform for Interactive Benchmarking and Atomistic Simulations Using Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-08T16:23:57Z
- Venue: cond-mat.mtrl-sci
- Authors: Manas Sharma, Sudeep Punnathanam, Ananth Govind Rajan
- Link: https://arxiv.org/abs/2607.07606v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

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

### 1. Valley polarization, Rashba interaction, and weak altermagnetism in inversion-asymmetric MnPS$_\text{3}|$WS$_\text{2}$ van der Waals heterostructures

- Source: arXiv
- Date: 2026-07-17T18:51:51Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, cond-mat.str-el
- Authors: Purba Dutta, Soumajyoti Bid, Nirmal Ganguli
- Link: https://arxiv.org/abs/2607.16454v1
- Score: 30.0
- Match: 摘要匹配 magnetoelectric coupling; 摘要匹配 ferromagnetism; 标题匹配 altermagnetism; 摘要匹配 altermagnetic

**中文摘要：** 最近，故意破坏反铁磁体中的反演对称性（$\mathcal{P}$）已成为诱导各种特征的有效手段，例如贝里曲率的出现、自旋谷锁定、磁电耦合以及从传统反铁磁性到交替磁性的转变。相反，在非磁性系统中，在存在强自旋轨道相互作用（SOI）的情况下，反演对称性的破坏会通过拉什巴效应产生动量相关的自旋分裂，从而能够通过外部电场实现可调谐的自旋极化。 受二维材料最新进展的推动，我们基于密度泛函理论进行第一性原理计算，以研究由 $\mathcal{P}$ 对称 MnPS$_3$ 单层和 WS$_2$ 单层形成的范德华（vdW）异质结构。我们证明该界面具有丰富的相互作用的涌现现象，包括交变磁相、拉什巴自旋分裂、自旋谷锁定和谷极化。 我们的结果表明，异质结构表现出半导体行为，直接带隙约为 1.65~eV，并且具有 I 型能带排列。值得注意的是，电子结构和能带排列可以通过外部电场和面内双轴应变在 I 型和 II 型区域之间有效调节。此外，场感应调制能够对交变磁相和谷分裂进行强有力的控制。 这些发现确立了所提出的 vdW 异质结构作为一个高度可调的平台，在自旋电子学和谷电子学应用中具有巨大的潜力。
**讨论重点：** 受二维材料最新进展的推动，我们基于密度泛函理论进行第一性原理计算，以研究由 $\mathcal{P}$ 对称 MnPS$_3$ 单层和 WS$_2$ 单层形成的范德华（vdW）异质结构。相反，在非磁性系统中，在存在强自旋轨道相互作用（SOI）的情况下，反演对称性的破坏会通过拉什巴效应产生动量相关的自旋分裂，从而能够通过外部电场实现可调谐的自旋极化。 结合关键词看，阅读时应重点关注磁电耦合、铁磁性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Pure Spin Bulk Photovoltaic Effect in an Altermagnetic Higher-Order Topological Insulator

- Source: arXiv
- Date: 2026-07-21T12:02:22Z
- Venue: cond-mat.mes-hall, cond-mat.str-el, cond-mat.supr-con
- Authors: Sibgat Ulah, Ankan Bhattacharyya, Manisha Thakurathi
- Link: https://arxiv.org/abs/2607.19018v1
- Score: 25.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们研究了 $PT$ 对称二维异质结构中的体光伏效应 (BPVE)，该异质结构由与 $d$ 波交变磁体耦合的拓扑绝缘体组成。为了描述该系统的对称强制简并能带，我们开发了自旋 BPVE 的非阿贝尔公式，将传统理论从孤立的非简并能带扩展到 $PT$ 简并流形。我们表明，尼尔矢量的方向控制着拓扑相位和非线性光学响应的​​特征。 当 Néel 矢量位于 $xy$ 平面时，异质结构实现了受 $C_{4z}T$ 对称性保护的二阶拓扑绝缘体 (SOTI)。该系统还保留了$C_{2z}$对称性，完全抑制了二阶电荷光电流，同时允许有限的自旋光电流。结果，BPVE 成为本质上纯的自旋光伏效应，产生直流自旋电流，而不伴随充电电流。我们发现线偏振光驱动自旋位移电流，而圆偏振光产生自旋注入电流。 每当局部狄拉克质量改变符号时，两种响应都会经历符号反转。当尼尔矢量向 $z$ 轴旋转时，SOTI 相转变为一阶拓扑绝缘相，导致电荷和自旋光电流共存。我们的结果建立了 $PT$ 对称交变磁拓扑绝缘体异质结构作为生成和控制纯自旋光电流的通用平台，并揭示了非线性自旋输运作为拓扑和磁对称性的敏感探针。
**讨论重点：** 为了描述该系统的对称强制简并能带，我们开发了自旋 BPVE 的非阿贝尔公式，将传统理论从孤立的非简并能带扩展到 $PT$ 简并流形。我们研究了 $PT$ 对称二维异质结构中的体光伏效应 (BPVE)，该异质结构由与 $d$ 波交变磁体耦合的拓扑绝缘体组成。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Electrical Control of Altermagnetism in a Quasi-1D Magnet

- Source: arXiv
- Date: 2026-07-18T15:44:13Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall
- Authors: Alberto M. Ruiz, Cuiju Yu, Diego López-Alcalá, Jose L. Lado, Adolfo O. Fumega, José J. Baldoví
- Link: https://arxiv.org/abs/2607.16856v1
- Score: 25.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交替磁性是一种共线磁态，其特征是完全补偿材料中动量相关的自旋分裂。虽然在三维或二维交换相互作用控制的系统中得到了广泛的研究，但它向准一维磁体的扩展几乎仍未被探索。重点关注实验建立的 AgCrP$_2$S$_6$ 范德华磁体，我们证明嵌入二维晶格中的反铁磁链提供了交变磁性的一般途径。 结合第一性原理计算和自旋空间群分析，我们证明面外对称性破缺可以产生非相对论性 d 波自旋分裂。外部平面外电场验证了这种机制，其中感应分裂随场强线性增加，并随场方向反转符号。我们通过构建有效的紧束缚模型来合理化这种行为，该模型将交变磁响应与各向异性第三邻居链间跳跃联系起来。 此外，我们还表明，Janus 取代还会引起 d 波自旋织构，而与 CuInP$_2$S$_6$ 的铁电界面能够在完全补偿的亚铁磁状态下实现偏振控制的自旋分裂带。我们的结果将准一维反铁磁体建立为交变磁性的基础。
**讨论重点：** 我们通过构建有效的紧束缚模型来合理化这种行为，该模型将交变磁响应与各向异性第三邻居链间跳跃联系起来。虽然在三维或二维交换相互作用控制的系统中得到了广泛的研究，但它向准一维磁体的扩展几乎仍未被探索。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Coherent Magnons Driven by Photomodulated Anisotropy in Altermagnetic MnTe

- Source: arXiv
- Date: 2026-07-20T18:11:04Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: Dingbin Huang, Jonathon Kruppe, Resham Babu Regmi, Nirmal J. Ghimire, James Analytis, Joseph Orenstein
- Link: https://arxiv.org/abs/2607.18421v1
- Score: 24.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 碲化锰 ($\text{MnTe}$) 最近作为一种典型的 $g$ 波交变磁体出现，为研究交变磁序的非平衡激发提供了一个理想的平台。在这里，我们报告了尼尔矢量局部平衡方向 $\varphi_L(\mathbf{r})$ 的同步空间映射，以及光激发自旋波的振幅 $Δ\varphi(\mathbf{r},t)$ 和频率 $Ω(\mathbf{r})$。基于这些测量，我们在由本征各向异性引起的自旋波间隙上设置了一个非常低的上限 $\approx 60~μ\text{eV}$ (0.7 K)。 这种异常弱的六方各向异性 ($K_6$) 使得交变磁序非常容易受到光学调谐的影响，从而允许相干自旋波由 $K_6$ 的光致增强驱动。在阈值泵注量以上，我们的空间图显示，这种光调制表现为 $Δ\varphi$ 对 $\varphi_L$ 的六重对称锯齿依赖性以及 $Ω$ 的类摆线调制。 最终，$\text{MnTe}$中尼尔矢量的近各向同性使得能够对电子能带结构中自旋分裂的方向进行光学和机械控制，为交磁自旋电子学提供了新的途径。
**讨论重点：** 碲化锰 ($\text{MnTe}$) 最近作为一种典型的 $g$ 波交变磁体出现，为研究交变磁序的非平衡激发提供了一个理想的平台。在这里，我们报告了尼尔矢量局部平衡方向 $\varphi_L(\mathbf{r})$ 的同步空间映射，以及光激发自旋波的振幅 $Δ\varphi(\mathbf{r},t)$ 和频率 $Ω(\mathbf{r})$。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 5. Stripe-Order Altermagnetism

- Source: arXiv
- Date: 2026-07-20T14:30:09Z
- Venue: cond-mat.mes-hall, cond-mat.mtrl-sci, cond-mat.str-el
- Authors: Zheng-Yang Zhuang, Zhongbo Yan
- Link: https://arxiv.org/abs/2607.17997v1
- Score: 24.0
- Match: 标题匹配 altermagnetism; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁学将补偿磁序与非相对论性自旋分裂相结合，但已建立的机制主要依赖于尼尔级反铁磁体中的自旋反转。在这里，我们建立了由自旋反转镜控制的条序交变磁力，将其置于通常的基于旋转的 $l$ 波分类之外。使用双轨道模型，我们表明条纹自旋和轨道顺序的相互作用产生两个阶段：具有镜像选择向列自旋分裂的条纹交变磁体和具有自旋简并带的条纹反交变磁体。 后者可以支持在合适的屈曲结构中对自旋分裂进行类似铁电的电控制。随机相位近似（RPA）计算表明，在强跳跃各向异性下，接近半填充时，带状交变磁性更受青睐。自旋反转镜还对平行或垂直于镜面的电场施加纯横向自旋电流，从而提供直接传输诊断。
**讨论重点：** 交变磁学将补偿磁序与非相对论性自旋分裂相结合，但已建立的机制主要依赖于尼尔级反铁磁体中的自旋反转。在这里，我们建立了由自旋反转镜控制的条序交变磁力，将其置于通常的基于旋转的 $l$ 波分类之外。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 6. Altermagnetism without a long-range order

- Source: arXiv
- Date: 2026-07-17T13:42:06Z
- Venue: cond-mat.str-el
- Authors: V. E. Valiulin, A. V. Mikheyenkov, K. I. Kugel
- Link: https://arxiv.org/abs/2607.15954v1
- Score: 24.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 近两周发布

**中文摘要：** Kugel-Khomskii 自旋-赝自旋模型最初是为具有轨道自由度的过渡金属化合物而开发的，最近在交变磁性的背景下得到了重新解释。在这项工作中，我们从理论上研究了在没有长程磁序或轨道序的情况下交变磁行为的出现。使用旋转不变格林函数方法来构建方晶格和线性链上的 SU(2) x SU(2) 对称模型，我们分析了自旋-自旋和自旋-赝自旋相关函数、激发光谱、热容和磁化率。 我们表明，除了关键的子系统间交换 Kc(T) 之外，即使每个位点的平均自旋和赝自旋为零，也会出现具有非零自旋-赝自旋相关性的复合态。激发谱分为声学和光学分支，节点线沿 qx = qy - 交变磁对称的直接特征。在相界处观察到热容量的峰值和磁化率的跳跃。在一维中，相界是非单调的并且表现出重入转变。 这些结果建立了“交变顺磁体”或“交变磁液体”的概念，没有长程有序，与低维和强波动系统相关。
**讨论重点：** 在这项工作中，我们从理论上研究了在没有长程磁序或轨道序的情况下交变磁行为的出现。 Kugel-Khomskii 自旋-赝自旋模型最初是为具有轨道自由度的过渡金属化合物而开发的，最近在交变磁性的背景下得到了重新解释。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 7. Lower Bounds on Spectral Gaps of Parent Hamiltonians via Tensor Networks

- Source: arXiv
- Date: 2026-07-21T13:10:20Z
- Venue: quant-ph, cond-mat.str-el
- Authors: Milán Ádám Rozmán, András Molnár, Norbert Schuch
- Link: https://arxiv.org/abs/2607.19078v1
- Score: 21.0
- Match: 标题匹配 tensor network; 摘要匹配 quantum many-body; 最近 3 天发布

**中文摘要：** 证明地面空间上方的光谱间隙是量子多体物理学的一个中心问题。然而，找到差距的下限是出了名的困难。我们重新审视最初由 Fannes、Nachtergaele 和 Werner [Fannes '92, Nachtergaele '96] 开发的鞅方法，以证明矩阵积状态 (MPS) 的父哈密顿量的谱间隙的存在，并对该方法的不同步骤进行改进。 最重要的是，我们设计了一种新技术，可以准确有效地计算鞅方法中的关键量——局部地面空间的重叠。这使得该方法得到了明显的改进，使其能够超越其他现有技术来降低边界差距，我们通过对多个模型进行基准测试来证明这一点。值得注意的是，我们的——数值驱动的——方法同时也产生了一个显着简化的证明，证明任何（表现良好的）MPS 的父哈密顿量总是有缺口的。
**讨论重点：** 我们重新审视最初由 Fannes、Nachtergaele 和 Werner [Fannes '92, Nachtergaele '96] 开发的鞅方法，以证明矩阵积状态 (MPS) 的父哈密顿量的谱间隙的存在，并对该方法的不同步骤进行改进。然而，找到差距的下限是出了名的困难。 结合关键词看，阅读时应重点关注张量网络、量子多体相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 8. $J_{1} - J_{2} - δ$ model on a square lattice: From Altermagnet to Columnar antiferromagnet via quantum disordered phase

- Source: arXiv
- Date: 2026-07-17T18:06:05Z
- Venue: cond-mat.str-el
- Authors: Subharthi Paul, Darshan G. Joshi
- Link: https://arxiv.org/abs/2607.16415v1
- Score: 17.0
- Match: 摘要匹配 altermagnetism; 标题匹配 altermagnet; 近两周发布

**中文摘要：** 局部矩磁体的交变磁性的特征是在没有任何自旋各向异性相互作用或外部场的情况下，零净磁化强度和相反手性磁振子带的分裂。在这项工作中，我们研究了交流磁体对磁挫败引起的量子涨落的鲁棒性。我们考虑方形晶格上的海森堡模型，除了最近邻相互作用之外，还具有两种不同类型的第二邻域相互作用（如棋盘图案）。 该模型在方格上的 $J_{1}-J_{2}$ 海森堡模型和棋盘格上的海森堡模型之间连续插值。对于较弱的第二邻域相互作用，实现了尼尔型交变磁体相。另一方面，为了增强第二邻域相互作用，出现了柱状反铁磁体。利用线性自旋波理论，我们计算了两个磁相的磁振子色散、有序参数、静态和动态结构因子。 此外，我们还表明存在一个中间量子无序相将两个磁相分开，该相与 $J_{1}-J_{2}$ 模型中实现的相相关。当我们向棋盘晶格极限调整时，量子无序区域进一步稳定。
**讨论重点：** 在这项工作中，我们研究了交流磁体对磁挫败引起的量子涨落的鲁棒性。我们考虑方形晶格上的海森堡模型，除了最近邻相互作用之外，还具有两种不同类型的第二邻域相互作用（如棋盘图案）。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 9. Exotic Electronic Order in a Parabolic Kagome Semimetal

- Source: arXiv
- Date: 2026-07-20T18:00:03Z
- Venue: cond-mat.str-el
- Authors: C. Alexander Baum, Jonas Issing, Sarbajit Mazumdar, Matteo Dürrnagel, Michael Klett, Ronny Thomale
- Link: https://arxiv.org/abs/2607.18389v1
- Score: 16.0
- Match: 摘要匹配 altermagnetism; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们研究了二次能带接触半金属在 2/3 填充下的相互作用戈薇晶格实现，并具有现场和最近邻排斥相互作用。结合功能重正化群和从玻色子方法，我们将其相图从中间耦合映射到强耦合，并揭示了非常规电子顺序的层次结构。主要的不稳定性包括环路电流有序、由自旋波美兰丘克不稳定性引起的自发交变磁力以及具有独特且很大程度上未经探索的特性的自旋环路电流有序。 我们演示了能带运动学、电子相互作用和量子几何的相互作用如何控制这些相的选择。我们的研究结果确立了二次带接触半金属作为非常规对称性破缺的有前景的平台，并提出了其他抛物线半金属中的类似现象。
**讨论重点：** 我们研究了二次能带接触半金属在 2/3 填充下的相互作用戈薇晶格实现，并具有现场和最近邻排斥相互作用。结合功能重正化群和从玻色子方法，我们将其相图从中间耦合映射到强耦合，并揭示了非常规电子顺序的层次结构。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 10. Quantum-metric-driven light-induced ferrovalley state in d-wave altermagnets

- Source: arXiv
- Date: 2026-07-19T03:26:26Z
- Venue: cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Shihao Zhang
- Link: https://arxiv.org/abs/2607.17049v1
- Score: 15.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 将量子度量与贝里曲率分离仍然是量子材料中的一个核心挑战，因为这两个几何量几乎总是共存，并且它们的贡献很难分开。我们证明，d 波交替磁体构成了克服这一障碍的理想平台，其真正的哈密顿量具有严格消失的贝里曲率。 使用马格努斯展开式和精确的 Floquet 对角化，我们证明了线性偏振非共振光通过纯粹的量子度量介导的带隙重正化驱动轨道选择性铁谷相，在任何阶次都没有贝里曲率贡献。轨道选择性源于跳跃各向异性，它在 $d_{xz}$ 和 $d_{yz}$ 轨道之间产生明显的度量各向异性，并且间隙减小以量子度量的形式解析表示。 由此产生的谷间隙差异提供了量子度量的直接定量测量，可用于自旋分辨 ARPES 和光学泵浦探针光谱。这将 d 波交替磁体建立为一个原始的可调谐平台，其中可以隔离量子度量效应，通过光偏振控制，并通过谷偏振读出。
**讨论重点：** 由此产生的谷间隙差异提供了量子度量的直接定量测量，可用于自旋分辨 ARPES 和光学泵浦探针光谱。我们证明，d 波交替磁体构成了克服这一障碍的理想平台，其真正的哈密顿量具有严格消失的贝里曲率。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。
