# Latest papers for 程旭丽

Updated: 2026-07-17T10:14:24.547284+00:00
Window: last 14 days

## Notes

- arXiv query failed for 机器学习分子动力学模拟与热力学性质: The read operation timed out
- 机器学习分子动力学模拟与热力学性质 kept previous papers because the current query returned 0 results.
- arXiv query failed for 凝聚态物理强关联体系和多铁性质: The read operation timed out
- 凝聚态物理强关联体系和多铁性质 kept previous papers because the current query returned 0 results.

## 机器学习分子动力学模拟与热力学性质

### 1. Aromatic Molecule Solvation in Liquid Water with Coupled Cluster Accuracy: The Balance of Pi-Interactions and Hydrophobicity

- Source: arXiv
- Date: 2026-07-14T20:52:10Z
- Venue: physics.chem-ph
- Authors: Nore Stolte, Harald Forbert, Yury Lysogorskiy, Ralf Drautz, Dominik Marx
- Link: https://arxiv.org/abs/2607.13261v1
- Score: 13.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 水中的芳香族有机溶质在疏水性溶剂化和定向 O-H$\cdots π$ 氢键之间表现出微妙的平衡，但广泛使用的力场和最先进的密度泛函方法难以提供这些关键相互作用的一致图像。我们引入了一种数据高效的升级策略，以仅使用有限的分子簇来训练基于水性芳香族分子的图原子簇扩展的机器学习原子间势（MLIP），并具有 CCSD(T) 精度进行凝聚相模拟。 我们将我们的方法应用于甲苯水溶液 (C$_6$H$_5$CH$_3$)。由此产生的 CCSD(T) 质量 MLIP 大量再现了耦合的簇能量和力，并揭示了常用的方法无法捕获亲水性和疏水性溶剂化之间的关键平衡，从而扭曲了芳香族分子与其环境的相互作用。代表性的生物分子力场显着影响疏水溶剂化壳的结构，并使界面水定向错误，同时高估$π$-接触，产生不一致的溶剂化平衡。 即使是混合 DFT 和 MP2 也高估了水-$π$氢键断裂的障碍。我们的工作流程为 CCSD(T) 质量的水溶液凝聚相模拟提供了一条实用的通用途径，因此构建的相互作用势现在为对生物分子环境中的 $π$ 接触和疏水效应（例如水环境中蛋白质和 DNA 的溶剂化）进行一致、高精度的基准研究打开了大门。
**讨论重点：** 我们引入了一种数据高效的升级策略，以仅使用有限的分子簇来训练基于水性芳香族分子的图原子簇扩展的机器学习原子间势（MLIP），并具有 CCSD(T) 精度进行凝聚相模拟。 我们的工作流程为 CCSD(T) 质量的水溶液凝聚相模拟提供了一条实用的通用途径，因此构建的相互作用势现在为对生物分子环境中的 $π$ 接触和疏水效应（例如水环境中蛋白质和 DNA 的溶剂化）进行一致、高精度的基准研究打开了大门。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 2. Transferable Implicit Solvent Machine Learning Potential for Drugs and Proteins Approaching Ab Initio Accuracy

- Source: arXiv
- Date: 2026-07-12T19:29:24Z
- Venue: physics.chem-ph, cs.LG, q-bio.BM
- Authors: Jan Eckwert, Julija Zavadlav
- Link: https://arxiv.org/abs/2607.10887v1
- Score: 11.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 机器学习原子间势 (MLP) 彻底改变了原子建模，提供了取代密度泛函理论 (DFT) 等传统方法的潜力。然而，MLP 的推理时间比经典力场慢几个数量级，阻碍了需要微秒或更长时间时间尺度的生物分子系统的实际应用。隐式溶剂 MLP 可以解决这个问题，但面临着与粗粒度建模相关的数据挑战。 因此，以前的方法依赖于经验力场数据，从而从本质上限制了 MLP 的准确性。在这里，我们介绍了可转移水隐式网络（TWIN），这是一种完全由等变图神经网络参数化的隐式水 MLP，并且仅在从头开始和实验标签上进行训练。 我们证明了 TWIN 在类药物分子、肽和蛋白质之间的可转移性，在从头算和实验晶体学和 NMR 基准上取得了优异的结果，始终优于以前基于机器学习的隐式溶剂或粗粒度模型。此外，TWIN 与基于 DFT 的显式溶剂 MLP 紧密匹配，同时提供两个数量级的更快的时间步长评估，为水环境中生物分子系统的高效从头水平建模铺平了道路。
**讨论重点：** 在这里，我们介绍了可转移水隐式网络（TWIN），这是一种完全由等变图神经网络参数化的隐式水 MLP，并且仅在从头开始和实验标签上进行训练。然而，MLP 的推理时间比经典力场慢几个数量级，阻碍了需要微秒或更长时间时间尺度的生物分子系统的实际应用。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 3. Are Machine Learning Interatomic Potentials Truly Practical? A Benchmark of 23 Mainstream Models

- Source: arXiv
- Date: 2026-07-08T17:04:42Z
- Venue: cond-mat.mtrl-sci, cs.CE, physics.comp-ph
- Authors: Hanwen Kang, Tenglong Lu, Sheng Meng, Miao Liu
- Link: https://arxiv.org/abs/2607.07647v1
- Score: 11.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。我们评估三个维度：预测准确性、MD 模拟吞吐量和原子可扩展性。 我们的结果揭示了精确度与效率之间的巨大权衡：大型 SOTA 模型的精确度仅比轻量级模型高出 3-5 meV/atom，但吞吐量却损失了几个数量级——在最坏的情况下，仅比 DFT 本身快一点点。相比之下，轻量级 MLIP 位于帕累托前沿并在适度的硬件上运行。教训是，单维基准会误导该领域，未来的 MLIP 开发应该重视效率和可扩展性以及准确性。
**讨论重点：** 我们在低成本 NVIDIA DGX Spark（128 GB 本机内存，上限为 80 GB 以模拟普通实验室硬件）上对 23 个主流开源 MLIP 进行了基准测试，在基于 ASE 的统一管道下使用固定的 192 个原子系统。大多数 MLIP 基准测试奖励静态准确性，而忽略推理效率和硬件可扩展性——导致模型膨胀，现实价值不明确。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 4. MLIP Studio: An Open Platform for Interactive Benchmarking and Atomistic Simulations Using Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-08T16:23:57Z
- Venue: cond-mat.mtrl-sci
- Authors: Manas Sharma, Sudeep Punnathanam, Ananth Govind Rajan
- Link: https://arxiv.org/abs/2607.07606v1
- Score: 11.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 通用机器学习原子间势（MLIP）是改变原子模拟的基础人工智能模型，但其实际使用仍然受到分散的软件生态系统、依赖性冲突和缺乏可用的基准测试工具的阻碍。这些模型以一小部分计算成本实现了第一原理密度泛函理论 (DFT) 的精度。我们推出了 MLIP Studio（可在 https://mlipstudio.iisc.ac.in 获取），这是一个开放且免费的平台，可将 60 多种通用 MLIP 引入分子和材料的统一交互界面中。 该平台支持端到端 MLIP 驱动的工作流程，包括属性预测、几何优化、振动和状态方程分析、自旋状态确定、自定义模型部署以及针对参考数据的高通量基准测试。自动奇偶图和可排序误差表有助于快速识别元素异常值和有问题的数据点。我们证明基于 MLIP 的预优化可以减少后续 DFT 优化工作约 33$\times$。此外，该应用程序还可以对计算性能进行基准测试。 通过涉及蓝宝石基板上的二维磁性材料 CrCl$_3$ 的综合案例研究，我们展示了各种属性和势能景观的跨模型比较如何指导特定任务的 MLIP 选择。总体而言，MLIP Studio 降低了在计算化学和材料科学的端到端研究工作流程、基准测试和教育中可靠使用基础模型的障碍。
**讨论重点：** 我们推出了 MLIP Studio（可在 https://mlipstudio.iisc.ac.in 获取），这是一个开放且免费的平台，可将 60 多种通用 MLIP 引入分子和材料的统一交互界面中。通过涉及蓝宝石基板上的二维磁性材料 CrCl$_3$ 的综合案例研究，我们展示了各种属性和势能景观的跨模型比较如何指导特定任务的 MLIP 选择。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 5. Edge Cluster Expansion with Radial Rotary Attention for Interatomic Potentials

- Source: arXiv
- Date: 2026-07-12T09:17:57Z
- Venue: stat.ML, cond-mat.mtrl-sci, cs.LG
- Authors: Zemin Xu, Wenbo Xie, P. Hu
- Link: https://arxiv.org/abs/2607.10664v1
- Score: 10.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 在本文中，我们对机器学习原子间势 (MLIP) 的 SO(2) 理论进行了系统研究，并确定了传统 SO(2) 线性架构相对于 SO(3) Clebsch-Gordan 张量积 (CGTP) 的局限性。基于这些见解，我们提出了维格纳 D 矩阵的直接笛卡尔构造和递归 Clebsch-Gordan 构造，并引入了两种新颖的交互构建块。 首先，我们提出了基于广义不对称收缩的边缘复积基础，这是一种新的多体展开公式，通过复值等变乘法直接在边缘上构造高阶相互作用。其次，我们引入了径向旋转复合注意力（RRA），它增强了外推性能并超越了现有的注意力向量公式。我们还介绍了原子集群扩展模块的多项改进。 基于这些进步，我们在 OMat24、sAlex 和 MPTrj 上训练模型，并引入 TECE-OAM-RRA-1.0，它在 Matbench Discovery 上实现了最先进的 (SOTA) 性能。
**讨论重点：** 基于这些见解，我们提出了维格纳 D 矩阵的直接笛卡尔构造和递归 Clebsch-Gordan 构造，并引入了两种新颖的交互构建块。首先，我们提出了基于广义不对称收缩的边缘复积基础，这是一种新的多体展开公式，通过复值等变乘法直接在边缘上构造高阶相互作用。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 6. Active rejection enables reliable generalization of universal machine-learning interatomic potentials

- Source: arXiv
- Date: 2026-07-10T14:24:47Z
- Venue: cs.LG
- Authors: Mingxiang Luo, Xinnan Mao, Lu Wang, Lei Bai, Feng Ding, Yuqiang Li
- Link: https://arxiv.org/abs/2607.09456v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 通用机器学习原子间势 (uMLIP) 连接了量子力学精度和大规模分子动力学，但 r$^2$SCAN 等高精度计算的成本限制了对相对于开放材料空间仍然较小的数据集的训练。强大的平均基准性能也不能保证对每个结构进行可靠的能量-力预测。我们提出了自适应多教师路由（ATR），它将高保真数据构建重新表述为不确定性下的结构决策问题。 使用一小组真实的 r$^2$SCAN 标签，ATR 校准多个预训练的 uMLIP 教师，并结合结构描述符、教师身份和教师间分歧来估计每个结构-教师对的可靠性。它为伪标签生成选择高置信度预测，并拒绝没有教师足够可靠的结构。由于真实的 r$^2$SCAN 标签仅占候选结构的 0.2\%，ATR 提取了 289 万个可追踪的 r$^2$SCAN 级伪标签用于预训练。 在保留的 r$^2$SCAN 结构和 MP-r$^2$SCAN 基准上，在 ATR 生成的数据集上训练的轻量级 CHGNet 始终优于基线和非路由控制。有限温度分子动力学进一步表明，ATR 提高了多种材料系统的动力学鲁棒性，在基线模拟经历灾难性结构崩溃时保持稳定的轨迹。这些结果确立了主动拒绝作为将多个预训练 uMLIP 转换为可扩展且可靠的高保真 uMLIP 数据构建系统的有效机制。
**讨论重点：** 我们提出了自适应多教师路由（ATR），它将高保真数据构建重新表述为不确定性下的结构决策问题。强大的平均基准性能也不能保证对每个结构进行可靠的能量-力预测。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. dpti: An Automated Thermodynamic Integration Workflow for Phase Diagram Calculations with Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-06T12:56:52Z
- Venue: physics.comp-ph, cond-mat.mtrl-sci
- Authors: Fengbo Yuan, Xin Zhong, Donghao Zheng, Jinzhe Zeng, Linfeng Zhang, Han Wang
- Link: https://arxiv.org/abs/2607.05015v1
- Score: 9.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 热力学积分 (TI) 是一种广泛使用的计算自由能和相图的方法。然而，由机器学习原子间势 (MLIP) 驱动的 TI 计算在技术上仍然具有挑战性，因为它们需要仔细设计可逆积分路径以及每个相和状态点的许多密切相关的分子动力学 (MD) 任务。 为了应对这些挑战，我们推出了 dpti，这是一个开源 Python 软件包，可自动执行使用 MLIP 进行相图计算的 TI 工作流程。 dpti 通过可逆积分路径将具有分析已知自由能的参考系统连接到 MLIP 描述的原子和分子固体和液体。给定 JSON 输入文件，dpti 生成并运行所需的 MD 任务，计算自由能贡献，估计误差，并将共存点传播到相边界。 我们通过深势模型驱动的两个示例演示了 dpti 的用法：涉及 β-石英、柯石英和熔体的二氧化硅相图，以及冰 Ih-液态水相边界。 dpti 提供了一个有用的工具，用于自动计算 MLIP 建模的材料的相图。
**讨论重点：** 然而，由机器学习原子间势 (MLIP) 驱动的 TI 计算在技术上仍然具有挑战性，因为它们需要仔细设计可逆积分路径以及每个相和状态点的许多密切相关的分子动力学 (MD) 任务。热力学积分 (TI) 是一种广泛使用的计算自由能和相图的方法。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 8. Dyna-Mat: End-to-end benchmarking of foundation machine learning interatomic potentials in finite-temperature ensembles

- Source: arXiv
- Date: 2026-07-03T15:46:15Z
- Venue: cond-mat.mtrl-sci, physics.chem-ph
- Authors: Mikołaj J. Gawkowski, Nongnuch Artrith, Silvia Bonfanti, Abhijeet Sadashiv Gangan, Hendrik H. Heenen, Joseph Kioseoglou
- Link: https://arxiv.org/abs/2607.03433v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 基础机器学习原子间势 (MLIP) 越来越多地被用作第一性原理计算的直接替代品，从而能够在以前无法实现的长度和时间尺度上模拟材料。然而，由于缺乏地面实况数据，它们在有限热力学系综中结构和动力学可观测值的准确性尚未确定。在这里，我们介绍 Dyna-Mat-v1.0，这是一个凝聚相第一原理分子动力学轨迹的基准数据集，旨在在实际有限温度条件下测试基础 MLIP。 使用该数据集，我们通过比较第一原理配置和从 MLIP 驱动轨迹生成的可观测量的单点能量和力误差，评估了四个模型层的 15 个基础 MLIP。我们发现，具有较低单点力误差的“平均”模型也会产生较低的结构和动力学可观测误差。然而，对于某些单独的系统，低力误差会导致预测结构的定性故障。 大多数模型对压力的描述仍然很差，这表明当前大规模训练数据集中可用的密度泛函理论压力标签存在局限性。最后，我们构建了一个准确性成本帕累托前沿，以确定分子动力学与基础 MLIP 的最佳权衡，发现根据此处考虑的准确性指标，最新一代的交叉训练模型接近帕累托最优。 总体而言，Dyna-Mat-v1.0 表明，端到端有限温度验证对于量化基础 MLIP 的预测行为至关重要，并提供了一种简单、可扩展的途径，用于在与材料设计相关的静态和谐波基准之外对其进行评估。
**讨论重点：** 在这里，我们介绍 Dyna-Mat-v1.0，这是一个凝聚相第一原理分子动力学轨迹的基准数据集，旨在在实际有限温度条件下测试基础 MLIP。使用该数据集，我们通过比较第一原理配置和从 MLIP 驱动轨迹生成的可观测量的单点能量和力误差，评估了四个模型层的 15 个基础 MLIP。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. Beyond Adam: SOAP and Muon for Faster, Label-Efficient Training of Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-02T17:57:31Z
- Venue: cs.LG, cs.AI, physics.chem-ph
- Authors: Gil Harari, Yoel Zimmermann, Ola Tangen Kulseng, Laura Zichi, Chuin Wei Tan, Marc L. Descoteaux
- Link: https://arxiv.org/abs/2607.02499v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 机器学习原子间势（MLIP）已成为科学模拟人工智能的标志。虽然对新架构和数据集的努力导致了模型越来越准确和通用，但训练优化器的选择在很大程度上仍未被探索，默认为 Adam 及其在社区中的变体。在这里，我们实现并系统地比较了一类最近提出的矩阵结构优化器，包括 Muon、SOAP 和混合 SOAP-Muon，用于训练 NequIP 和 Allegro MLIP 模型。 我们发现这些优化器在收敛速度和最终精度方面都明显优于 Adam。 SOAP 和 SOAP-Muon 作为稳健且始终如一的强大方法而出现，而 Muon 相对于 Adam 只提供了部分收益。在部分部队监督下，这些改进尤其明显。我们的结果表明，优化器选择是 MLIP 的一个被忽视但有影响力的设计轴。
**讨论重点：** 我们的结果表明，优化器选择是 MLIP 的一个被忽视但有影响力的设计轴。虽然对新架构和数据集的努力导致了模型越来越准确和通用，但训练优化器的选择在很大程度上仍未被探索，默认为 Adam 及其在社区中的变体。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 10. Enerzyme: A Framework for Efficient Training of Reactive Neural Network Potentials for Enzyme Catalysis with Application to Methyltransferases

- Source: arXiv
- Date: 2026-07-01T18:24:10Z
- Venue: physics.chem-ph, cs.LG, q-bio.BM
- Authors: Weiliang Luo, Heather J. Kulik
- Link: https://arxiv.org/abs/2607.01362v1
- Score: 8.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 量子力学 (QM) 簇模型为酶反应的机理研究提供了有效的框架，但计算量仍然很高。神经网络电位（NNP）提供了一种降低成本的有前景的途径，但酶带来了小分子以外的挑战，包括大系统尺寸、隐式溶剂环境、大量极化和电荷转移。 在这里，我们提出了一个集成的软件框架，用于对酶的机理研究进行有效的 NNP 训练，并在 S-腺苷-L-甲硫氨酸依赖性甲基转移酶 (MTase) 的 QM 集群模型上进行了演示。我们的 Enerzyme 代码引入了模块化静电感知 NNP 架构，并将自动化 QM 集群构建与反应式数据集生成相结合。 Enerzymette 子包可在 NNP 和 DFT 水平上自动探索反应路径。 我们表明，与传统数据集指标相比，迭代灵活扫描和微调弹性带计算对 NNP 提出了更严格的要求。尽管如此，NNP 在不到 1,000 个系统特定数据点上进行训练，以接近化学的精度再现了包含多达 545 个原子的 MTase 簇的反应能量和过渡态结构。 原子电荷的直接监控和一致的介电屏蔽极大地提高了模拟的稳定性和准确性，而多任务学习的原子电荷捕获电荷转移和极化趋势，并提供具有化学意义的反应性描述符。最后，跨化学多样化的儿茶酚 O-甲基转移酶底物的可转移性表明，随着训练数据在多种酶上扩展，NNP 可以学习通用的反应模式。
**讨论重点：** 神经网络电位（NNP）提供了一种降低成本的有前景的途径，但酶带来了小分子以外的挑战，包括大系统尺寸、隐式溶剂环境、大量极化和电荷转移。量子力学 (QM) 簇模型为酶反应的机理研究提供了有效的框架，但计算量仍然很高。 结合关键词看，阅读时应重点关注神经网络势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

## 凝聚态物理强关联体系和多铁性质

### 1. Strain-Tunable Shift Current and Magneto-Optical Kerr Effect in Multiferroic Altermagnet Fe2Mo3O8

- Source: arXiv
- Date: 2026-07-14T14:14:24Z
- Venue: cond-mat.mtrl-sci
- Authors: Shengqiao Wang, Bo Zhao, Harish K. Singh, Jiahao Xie, Fu Li, Hongbin Zhang
- Link: https://arxiv.org/abs/2607.12799v1
- Score: 30.0
- Match: 标题匹配 multiferroic; 摘要匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet

**中文摘要：** 交变磁学最近已成为自旋电子学领域的一个引人注目的前沿领域，它将铁磁体的敏捷可调性与反铁磁体的标志优点无缝地融合在一起。作为一种具有独特交变磁性的典型极性多铁性材料，Fe2Mo3O8 为探索铁电极化、交变磁序和自旋相关响应之间复杂的相互作用提供了理想的场所。在这里，我们采用第一性原理计算，系统地研究了 Fe2Mo3O8 中偏振、自旋分裂、位移电流和磁光响应之间的耦合。 我们的研究结果表明，改变铁电极化不仅反转了位移电流的符号，而且还全面重塑了动量空间自旋分裂结构。此外，位移电流和磁光光谱在机械应变下表现出很强的可调谐性。值得注意的是，a 轴单轴应变的应用打破了晶体对称性，从而激活了有限磁光克尔效应，而这种效应在原始相中是被禁止的。
**讨论重点：** 在这里，我们采用第一性原理计算，系统地研究了 Fe2Mo3O8 中偏振、自旋分裂、位移电流和磁光响应之间的耦合。作为一种具有独特交变磁性的典型极性多铁性材料，Fe2Mo3O8 为探索铁电极化、交变磁序和自旋相关响应之间复杂的相互作用提供了理想的场所。 结合关键词看，阅读时应重点关注多铁性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Dirac topology, anomalous Hall response, and giant magnetoresistance in carrier-compensated altermagnetic semimetal NiS

- Source: arXiv
- Date: 2026-07-15T02:53:13Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: Shovan Gayen, Sk. Soyeb Ali, S K Panda
- Link: https://arxiv.org/abs/2607.13400v1
- Score: 27.0
- Match: 摘要匹配 altermagnetism; 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们结合第一原理密度泛函理论、贝里曲率分析、半经典玻尔兹曼输运和原子自旋动力学，将六方 NiS 建立为补偿的 3d 交变磁半金属，其中拓扑、磁性和晶格动力学本质上交织在一起。 NiAs 晶格的旋转陪集对称性产生了交变磁性的动量依赖性自旋分裂特性。通过自旋轨道耦合，带隙的狄拉克式交叉产生强烈的贝里曲率热点和几乎补偿的电子空穴袋。 这导致了与几种 4d、5d 金属相当的大且各向异性的本征自旋霍尔电导率、尽管净磁化强度为零但对称性允许的反常霍尔响应以及超过 10000% 的非饱和磁阻。在磁性方面，交换张量的第一性原理测定揭示了占主导地位的长程超交换和相当大的各向异性相互作用，定量地再现了实验尼尔温度。 我们的结果将 NiS 确定为一个模型 3D 平台，其中载流子补偿、交磁对称、贝里曲率驱动的传输和晶格敏感磁性在单一对称框架内共存，为相关过渡金属化合物中的多功能量子响应提供了设计原理。
**讨论重点：** 我们的结果将 NiS 确定为一个模型 3D 平台，其中载流子补偿、交磁对称、贝里曲率驱动的传输和晶格敏感磁性在单一对称框架内共存，为相关过渡金属化合物中的多功能量子响应提供了设计原理。 NiAs 晶格的旋转陪集对称性产生了交变磁性的动量依赖性自旋分裂特性。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Second-order topological insulator induced by compensated altermagnetism without bulk spin splitting

- Source: arXiv
- Date: 2026-07-14T04:04:02Z
- Venue: cond-mat.mes-hall
- Authors: Lizhou Liu, Qing-Feng Sun, Ying-Tao Zhang
- Link: https://arxiv.org/abs/2607.12323v1
- Score: 26.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们从理论上证明了二维拓扑绝缘体薄膜中由补偿交变磁性引起的二阶拓扑绝缘相，同时保持体间隙不变。通过引入在顶层和底层具有相反符号的层解析面外$d$波交变磁项，系统保留了$\mathcal{PT}$对称性并保持体能带中的自旋简并性，同时使螺旋边缘态产生间隙并生成局部角态。 由此产生的高阶相的特征是非零镜像分级缠绕数，有效边缘理论表明角态源自狄拉克质量域壁。我们进一步通过分析确定相边界并构建相应的拓扑相图，建立了一种无需批量自旋分裂即可实现高阶拓扑的稳健路线。
**讨论重点：** 我们进一步通过分析确定相边界并构建相应的拓扑相图，建立了一种无需批量自旋分裂即可实现高阶拓扑的稳健路线。通过引入在顶层和底层具有相反符号的层解析面外$d$波交变磁项，系统保留了$\mathcal{PT}$对称性并保持体能带中的自旋简并性，同时使螺旋边缘态产生间隙并生成局部角态。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Quantum anomalous Hall effect with tunable Chern numbers induced by d-wave sublattice-staggered altermagnetism

- Source: arXiv
- Date: 2026-07-14T03:58:39Z
- Venue: cond-mat.mes-hall
- Authors: Lizhou Liu, Qing-Feng Sun
- Link: https://arxiv.org/abs/2607.12320v1
- Score: 23.0
- Match: 标题匹配 altermagnetism; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们在方晶格上构建了一个最小自旋紧束缚模型，其中 $d$ 波亚晶格交错交替磁性驱动量子反常霍尔效应。这里，交换场在两个子晶格之间交错，在泡利矩阵 $τ_z$ 描述的 $A$ 和 $B$ 上具有相反的符号。由此产生的绝缘相具有可调陈数 $\mathcal{C}=\pm1$ 和 $\mathcal{C}=\pm2$，由交错交换强度和亚晶格交错电势控制。 我们确定了完整的相图，识别了布里渊区 $X$ 和 $Y$ 点处的谷分辨能带反转，并演示了手性边缘态以及量化的两端电导平台。我们的工作提供了一种简单的途径，通过 $d$ 波亚晶格交错交错磁性在补偿磁体中实现量子反常霍尔效应。
**讨论重点：** 我们在方晶格上构建了一个最小自旋紧束缚模型，其中 $d$ 波亚晶格交错交替磁性驱动量子反常霍尔效应。这里，交换场在两个子晶格之间交错，在泡利矩阵 $τ_z$ 描述的 $A$ 和 $B$ 上具有相反的符号。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 5. Phase-Controlled Epitaxy and Anisotropic Antiferromagnetism of Polar Wurtzite MnTe

- Source: arXiv
- Date: 2026-07-13T22:19:38Z
- Venue: cond-mat.mtrl-sci
- Authors: Janusz Sadowski, Jaroslaw Z. Domagala, Piotr Dziawa, Anna Kaleta, Sania Dad, Maciej Wójcik
- Link: https://arxiv.org/abs/2607.12191v2
- Score: 22.0
- Match: 标题匹配 ferromagnetism; 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁自旋电子学需要能够将补偿磁序、对称控制电子响应和外延可调谐性结合在实验上可实现的薄膜中的材料。 MnTe 是这方面的关键材料，但实验研究主要集中在稳定的 NiAs 型多晶型物上，而极性纤锌矿相仍未得到探索。 在这里，我们展示了分子束外延生长并研究了直接沉积在 GaAs(111)B 上的近相纯纤锌矿 MnTe 的特性，并表明生长条件的微小变化强烈改变了相组成，从嵌入纤锌矿 MnTe 基体中的内轴 NiAs 型夹杂物的多相状态到几乎单相极性纤锌矿层。
**讨论重点：** 在这里，我们展示了分子束外延生长并研究了直接沉积在 GaAs(111)B 上的近相纯纤锌矿 MnTe 的特性，并表明生长条件的微小变化强烈改变了相组成，从嵌入纤锌矿 MnTe 基体中的内轴 NiAs 型夹杂物的多相状态到几乎单相极性纤锌矿层。 MnTe 是这方面的关键材料，但实验研究主要集中在稳定的 NiAs 型多晶型物上，而极性纤锌矿相仍未得到探索。 结合关键词看，阅读时应重点关注铁磁性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 6. Ultrafast altermagnetophononics

- Source: arXiv
- Date: 2026-07-15T14:07:37Z
- Venue: cond-mat.mtrl-sci
- Authors: Chenyu Wang, Yaxian Wang, Sheng Meng
- Link: https://arxiv.org/abs/2607.13863v1
- Score: 21.0
- Match: 摘要匹配 altermagnetism; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁体在电子结构中具有对称性决定的非平凡自旋分裂，有望用于下一代自旋电子学，但其超快动态操纵在很大程度上仍未得到探索。在这里，我们将交替磁声学建立为通过相干声子引起的选择性对称破缺进行磁控制的有效途径。 以原型交流磁体 $α$-MnTe 为例，我们证明了 B$_{1g}$ 模式的定向激励选择性地解除了保护交流磁体 (AM) 的对称性约束，驱动超快过渡到瞬态补偿亚铁磁 (cFiM) 相，其特征是全局自旋分裂，没有净磁化。此外，我们通过展示多模式对称性破缺路径以及在金属 CrSb 中实现具有可逆磁矩的亚铁磁序，表明所提出的机制具有广泛的适用性。 这些发现阐明了通过对自旋分裂进行相干声子控制而在交变磁体中获得理想的非平衡特性的潜力。
**讨论重点：** 交变磁体在电子结构中具有对称性决定的非平凡自旋分裂，有望用于下一代自旋电子学，但其超快动态操纵在很大程度上仍未得到探索。在这里，我们将交替磁声学建立为通过相干声子引起的选择性对称破缺进行磁控制的有效途径。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 7. Phase-shifted multicomponent spin-charge nematicity in an altermagnet

- Source: arXiv
- Date: 2026-07-14T14:37:28Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: Christopher Candelora, Siyu Cheng, Muxian Xu, Keyu Zeng, Hengxin Tan, Younghun Hwang
- Link: https://arxiv.org/abs/2607.12824v1
- Score: 20.0
- Match: 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁体具有自旋分裂费米表面，没有净磁化。这种本质上的多组分电子设置提高了熟悉的相关电子相获得非常规自旋电荷结构的可能性。在这里，我们报告了 Co0.25NbSe2 中交磁向列性的发现。使用光谱成像扫描隧道显微镜和自旋偏振扫描隧道显微镜，我们发现在电荷和自旋敏感隧道通道中，三个名义上与 C3 相关的方向在零场状态下失去了旋转等效性。 引人注目的是，主要的自旋敏感成分相对于主要的电荷成分移动了一个 C3 扇区，揭示了相移的自旋电荷向列响应。现象学理论表明，交变磁序有利于电荷和自旋敏感向列成分之间的有限相对相位——C3 晶格钉扎会抑制这种首选偏移并选择观察到的锁相。 这些结果将交变磁向列性确立为多组分电子液晶有序的一种新形式，并指出了交变磁体可以将传统相关相转化为对称设计的自旋电荷有序的潜在通用途径。
**讨论重点：** 交变磁体具有自旋分裂费米表面，没有净磁化。这种本质上的多组分电子设置提高了熟悉的相关电子相获得非常规自旋电荷结构的可能性。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 8. Angular momentum splitter effect of $d$-wave axial phonons in orbital altermagnets

- Source: arXiv
- Date: 2026-07-15T15:01:42Z
- Venue: cond-mat.str-el
- Authors: Dimos Chatzichrysafis, Alexander Mook
- Link: https://arxiv.org/abs/2607.13923v1
- Score: 18.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们从理论上证明，在没有自旋轨道耦合的情况下，轴向声子（携带有限角动量的晶格振动量子）可以在轨道交变磁体中承载 $d$ 波角动量纹理。我们考虑一个具有 $d$ 波环路电流顺序的最小电子紧束缚模型，它打破了时间反转对称性。 在玻恩-奥本海默近似中，我们通过分子贝里曲率结合了电子-声子耦合，并表明电子态的潜在 $d$ 波轨道磁矩纹理转移到声子，而不需要相对论自旋轨道耦合。我们的研究结果扩大了可用于工程轴向声子的平台范围，并指出了 $d$ 波纹理的独特功能，包括角动量塞贝克和分束效应，对应于由温度梯度驱动的纵向和横向角动量电流。
**讨论重点：** 我们考虑一个具有 $d$ 波环路电流顺序的最小电子紧束缚模型，它打破了时间反转对称性。在玻恩-奥本海默近似中，我们通过分子贝里曲率结合了电子-声子耦合，并表明电子态的潜在 $d$ 波轨道磁矩纹理转移到声子，而不需要相对论自旋轨道耦合。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 9. Magnetic field-driven phase switching in the antiferromagnetic Mott insulator Ca$_3$(Ru$_{0.99}$Ti$_{0.01}$)$_2$O$_7$

- Source: arXiv
- Date: 2026-07-14T13:09:26Z
- Venue: cond-mat.str-el
- Authors: Ksenia S. Rabinovich, Tim Priessnitz, Nils Gross, George Jackeli, Maximilian J. Krautloher, Pascal Reiss
- Link: https://arxiv.org/abs/2607.12737v1
- Score: 17.0
- Match: 标题匹配 Mott insulator; 最近 3 天发布

**中文摘要：** Ca$_3$(Ru$_{1-x}$Ti$_x$)$_2$O$_7$ 中带宽控制的反铁磁莫特绝缘相是通过 Ru 位点的等价取代实现的。对于仅含 1% Ti 的稀释替代，莫特绝缘体基态仍然接近简并，原始 Ca$_3$Ru$_2$O$_7$ 的基态，其中 Ru 矩在以反铁磁方式堆叠的金属 RuO$_2$ 双层内铁磁排列。这种掺杂化合物的异常浅的自由能景观是由交织的电子-电子和电子-晶格相互作用产生的。 这使得它的磁性和传输特性对外部扰动高度敏感。我们系统地研究了 Ca$_3$(Ru$_{0.99}$Ti$_{0.01}$)$_2$O$_7$ 中磁场引起的相变，以探索其磁性 $H$-$T$ 相图。当沿易 $b$ 轴施加与反铁磁矩平行的场时，磁化强度在 $\approx $6 T 处表现出一阶自旋随角跃迁，表明 Ru 矩垂直于场的重新定向。 该转变伴随着电阻的减小，但自旋翻转阶段保持绝缘。在 10.5 T 以上，所有 Ru 力矩均与 $b$ 轴对齐，从而产生强制铁磁金属相。相比之下，当沿 $a$ 轴施加磁场时，在 14 T 以内，都观察不到自旋翻转和受迫铁磁相。 虽然电子动能和电子晶格耦合有助于该系统的自由能平衡，但所得的 $H$-$T$ 相图非常简单，并且与规范各向异性反铁磁体的相图非常相似，尽管具有基本重整化的临界场。
**讨论重点：** 我们系统地研究了 Ca$_3$(Ru$_{0.99}$Ti$_{0.01}$)$_2$O$_7$ 中磁场引起的相变，以探索其磁性 $H$-$T$ 相图。对于仅含 1% Ti 的稀释替代，莫特绝缘体基态仍然接近简并，原始 Ca$_3$Ru$_2$O$_7$ 的基态，其中 Ru 矩在以反铁磁方式堆叠的金属 RuO$_2$ 双层内铁磁排列。 结合关键词看，阅读时应重点关注Mott 绝缘体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 10. Halogen control of magnetic competition in Kitaev candidate Ru$X_3$ ($X =$ Cl, Br)

- Source: arXiv
- Date: 2026-07-14T10:13:10Z
- Venue: cond-mat.str-el
- Authors: Ryuta Iwazaki, Shinnosuke Koyama, Takashi Koretsune, Shintaro Hoshino, Joji Nasu
- Link: https://arxiv.org/abs/2607.12595v1
- Score: 15.0
- Match: 摘要匹配 Hubbard model; 摘要匹配 Mott insulator; 最近 3 天发布

**中文摘要：** 自旋轨道莫特绝缘体 Ru$X_3$ ($X =$ Cl, Br) 作为实现基塔耶夫自旋液体的有前景的候选材料引起了相当大的关注。在本研究中，我们根据第一性原理计算得出的多轨道哈伯德模型构建了有效的赝自旋模型，并研究了 RuCl$_3$ 和 RuBr$_3$ 的磁态。从构建的有效模型中，我们发现RuBr$_3$比RuCl$_3$具有更扩展的Wannier轨道和更强的层间交换相互作用。 这些相互作用增强了三维相关性，与实验推断的 RuBr$_3$ 更强的反铁磁性趋势一致。轨道相关的库仑各向异性进一步减小了铁磁态和锯齿态之间的能量差。我们的结果阐明了卤素取代如何通过层间交换相互作用和轨道依赖库仑相互作用的影响来控制 Ru$X_3$ 中的磁竞争。
**讨论重点：** 在本研究中，我们根据第一性原理计算得出的多轨道哈伯德模型构建了有效的赝自旋模型，并研究了 RuCl$_3$ 和 RuBr$_3$ 的磁态。从构建的有效模型中，我们发现RuBr$_3$比RuCl$_3$具有更扩展的Wannier轨道和更强的层间交换相互作用。 结合关键词看，阅读时应重点关注Hubbard 模型、Mott 绝缘体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。
