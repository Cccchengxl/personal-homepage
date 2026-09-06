# Latest papers for 程旭丽

Updated: 2026-09-06T02:32:51.050033+00:00
Window: last 14 days

## Notes

- arXiv query failed for 机器学习分子动力学模拟与热力学性质: HTTP Error 429: Unknown Error
- 机器学习分子动力学模拟与热力学性质 kept previous papers because the current query returned 0 results.
- arXiv query failed for 凝聚态物理强关联体系和多铁性质: The read operation timed out
- 凝聚态物理强关联体系和多铁性质 returned 1 papers; target range is 5-10.

## 机器学习分子动力学模拟与热力学性质

### 1. uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks

- Source: arXiv
- Date: 2026-08-28T09:08:23Z
- Venue: cond-mat.mtrl-sci
- Authors: Théo Jaffrelot Inizan, Prathami Divakar Kamath, Alin Marin Elena, Kristin A. Persson
- Link: https://arxiv.org/abs/2608.28100v1
- Score: 15.0
- Match: 标题匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 基础机器学习原子间势（MLIP）以一小部分计算成本提供了近乎从头开始的精度，但它们对金属有机框架（MOF）的承诺在很大程度上仍未实现，因为大型晶胞使得第一性原理训练数据的生成成本昂贵，微调模型稀缺，并且基于实验的基准更加稀缺。我们引入了 uMOF，这是一个解决这一差距的三部分贡献。 首先，我们发布了迄今为止最大、最准确的 MOF 密度泛函理论数据集，在 r$^2$SCAN-D4 理论水平上计算，跨越 19950 个独特框架和 79 个元素的 85524 个配置，涵盖空结构和充气结构、几何优化、状态方程和有限温度分子动力学。 其次，我们发布了一个文献挖掘基准，包含 3986 个经过验证的属性值（3146 个实验值），通过七阶段、检查点多通道大型语言模型管道从 626 篇论文中提取，链接到 650 多个晶体信息文件。第三，我们发布了两个用于 MOF 的通用 MLIP，即 uMOF-MH 和 uMOF-POLAR，它们是根据 uMOF 数据集上两个架构不同的 MACE 基础模型进行微调的。在接近平衡的“Tier-1”属性（体积模量、声子衍生热容）上，uMOF 模型的性能与现有基础和微调基线相当。 在更难的动力学敏感特性（例如通过 Widom 插入和吸附等温线获得的气体吸附焓）方面，uMOF 模型的表现优于我们测试的每个基线，包括在大三个数量级的数据集上训练的 MOF 专用气体捕获模型，将误差减少了 80% 以上，使其处于实验不确定性范围内。我们将这一优势归因于训练数据的物理多样性和理论水平，其中 MD 模拟的一小部分 (1.7%) 对于 MLIP 稳定性至关重要。
**讨论重点：** 我们引入了 uMOF，这是一个解决这一差距的三部分贡献。其次，我们发布了一个文献挖掘基准，包含 3986 个经过验证的属性值（3146 个实验值），通过七阶段、检查点多通道大型语言模型管道从 626 篇论文中提取，链接到 650 多个晶体信息文件。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 2. Cartesian tensor equivariant machine-learning force field for spin-dependent atomistic simulations

- Source: arXiv
- Date: 2026-08-31T06:52:38Z
- Venue: physics.comp-ph
- Authors: Junjie Wang, Yijie Zhu, Zhongwei Zhang, Zhiyue Guo, Xudong Zhu, Lixin He
- Link: https://arxiv.org/abs/2608.30338v1
- Score: 14.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 磁性材料表现出原子结构和自旋自由度之间复杂的耦合，这对跨实验相关长度和时间尺度的原子模拟提出了根本性挑战。在这里，我们介绍 HotPP-Spin，它是 HotPP 的自旋相关扩展，用于磁性机器学习原子间势，建立在笛卡尔张量等变消息传递的基础上。原子磁矩被视为显式轴矢量自由度，而空间反演和时间反演宇称通过张量耦合传播。 这种结构提供了交换主导和自旋轨道引发的相互作用的统一表示，而无需强加预定义的分析相互作用形式。标量自旋相关势能表面通过微分产生能量守恒的原子力和有效磁场。 跨越共线磁性、非共线磁性和自旋轨道耦合引起的磁各向异性的基准表明，HotPP-Spin 在同一通用框架内准确地描述了磁能景观、磁力和磁序相关的能量体积关系。对于 H 相单层 VSe\(_2\)，使用学习的磁有效场进行随机自旋动力学模拟，将有限尺寸磁序交叉点定位在 415--435~K 处，与报告的实验值 \(418.5\pm7.8\)~K 的数值非常一致。 这些结果将笛卡尔张量消息传递确立为将第一原理磁能学与耦合结构和自旋现象的大规模原子模拟连接起来的通用途径。
**讨论重点：** 在这里，我们介绍 HotPP-Spin，它是 HotPP 的自旋相关扩展，用于磁性机器学习原子间势，建立在笛卡尔张量等变消息传递的基础上。跨越共线磁性、非共线磁性和自旋轨道耦合引起的磁各向异性的基准表明，HotPP-Spin 在同一通用框架内准确地描述了磁能景观、磁力和磁序相关的能量体积关系。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 3. Mode-Specific Dynamics of $\text{CO}_2$ Hydrogenation on Copper: The Hidden Role of Molecular Rotation

- Source: arXiv
- Date: 2026-08-28T02:39:51Z
- Venue: physics.chem-ph, cond-mat.mtrl-sci
- Authors: Junfan Xia, Zhikai Jiang, Yaolong Zhang, Bo Peng, Hua Guo, Bin Jiang
- Link: https://arxiv.org/abs/2608.27850v2
- Score: 10.0
- Match: 摘要匹配 neural network potential; 近两周发布

**中文摘要：** $\text{CO}_2$ 催化氢化以在铜上形成甲酸盐是 $\text{CO}_2$ 利用的关键基本步骤。先前的实验和理论研究表明，这种反应存在 Eley-Rideal 机制，由弯曲振动激发促进，但仍缺乏直接状态解析的证据。在这里，我们基于精确的全维神经网络势能面提出了 Cu(111) 上 $\text{CO}_2$ 加氢的第一原理动力学预测。 我们的计算近乎定量地再现了测量的反应概率，包括它们的喷嘴温度和入射能量依赖性。我们的状态解析结果表明，虽然弯曲模式的振动激励增强了反应性，但它​​本身并不能解释观察到的反应性随喷嘴温度的增加。相反，旋转激发起着主导作用，这主要归因于 $\text{CO}_2$ 进入过渡态时分子极性方向的各向异性发生显着变化。 这种特定于模式的见解强化了表面反应性中旋转的隐藏作用，为异质催化剂上 $\text{CO}_2$ 加氢的状态选择性控制开辟了新途径。
**讨论重点：** 在这里，我们基于精确的全维神经网络势能面提出了 Cu(111) 上 $\text{CO}_2$ 加氢的第一原理动力学预测。先前的实验和理论研究表明，这种反应存在 Eley-Rideal 机制，由弯曲振动激发促进，但仍缺乏直接状态解析的证据。 结合关键词看，阅读时应重点关注神经网络势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 4. OrbGNN: A Wave function-based Machine Learning Interelectronic Representation

- Source: arXiv
- Date: 2026-08-28T00:47:42Z
- Venue: physics.chem-ph
- Authors: Brody Quebedeaux, Shahzad Akram, Markus Reiher, Konstantinos D. Vogiatzis
- Link: https://arxiv.org/abs/2608.27806v2
- Score: 10.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 机器学习原子间势（MLIP）已成为分子建模和计算化学领域的新兴工具。通过从量子化学数据中学习高维势能表面，MLIP 能够准确有效地预测结构、热力学和动力学特性。然而，由于缺乏电子结构信息，此类模型在预测电子特性和静态电子相关效应方面存在局限性。 这项工作提出了 OrbGNN，一种类似于分子图和 MLIP 框架的电子结构图架构，其中成对轨道相互作用构成了图表示，而轨道纠缠编码了它们之间的连接性。通过将从轨道相关度量得出的信息直接嵌入到图拓扑中，OrbGNN 提供了分子轨道景观和电子相关模式的紧凑表示。对轨道图中特征空间的行为进行分析，以证明模型的鲁棒性。 该模型针对氮的解离和更大的双原子分子数据集进行了评估。最后，将 OrbGNN 模型应用于一组八面体铁 (II) 配合物来预测自旋态能隙。
**讨论重点：** 对轨道图中特征空间的行为进行分析，以证明模型的鲁棒性。通过从量子化学数据中学习高维势能表面，MLIP 能够准确有效地预测结构、热力学和动力学特性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 5. Benchmarking of Fast and Interpretable UF Machine Learning Potentials

- Source: arXiv
- Date: 2026-08-27T15:53:11Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Pawan Prakash, Sam Dong, Richard G. Hennig
- Link: https://arxiv.org/abs/2608.27277v1
- Score: 10.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 机器学习原子间势 (MLIP) 已成为分子动力学模拟中密度泛函理论 (DFT) 的强大替代方案，以一小部分计算成本提供接近 DFT 的精度。然而，许多最先进的 MLIP 仍然对计算要求很高，并且充当黑匣子，限制了物理可解释性。在这项工作中，我们评估了超快力场 (UF$^3$) 的潜力，它采用三次 B 样条基础的线性回归来表示有效的两体和三体相互作用。 我们表明 UF$^3$ 显示的准确度可与 GAP、MTP、NNP (Behler Parrinello) 和 qSNAP MLIP 等已建立的模型相媲美。我们通过计算六种元素系统的熔点来进一步研究 UF$^3$ 的可转移性，这些元素系统的电势拟合没有任何固液界面配置或有关熔化的明确热力学信息。 该模型再现了简单金属（Ni、Cu、Li）$\sim$6% 范围内的实验熔点，但大大低估了 Mo 和 Si 的熔点，并且未能产生 Ge 的稳定电势，反映出对于具有强角键或共价键的系统，在三体项处截断固定膨胀的局限性。我们进一步说明了 UF$^3$ 基于样条的公式如何允许直接可视化所学习的交互，从而能够识别黑盒方法经常掩盖的非物理行为。
**讨论重点：** 我们通过计算六种元素系统的熔点来进一步研究 UF$^3$ 的可转移性，这些元素系统的电势拟合没有任何固液界面配置或有关熔化的明确热力学信息。该模型再现了简单金属（Ni、Cu、Li）$\sim$6% 范围内的实验熔点，但大大低估了 Mo 和 Si 的熔点，并且未能产生 Ge 的稳定电势，反映出对于具有强角键或共价键的系统，在三体项处截断固定膨胀的局限性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 6. A Hierarchical Synergistic Deep Learning Framework Integrating Composition, Structure, and Ionic Transport for Solid-State Electrolyte Discovery

- Source: arXiv
- Date: 2026-08-26T10:04:42Z
- Venue: cond-mat.mtrl-sci, cs.AI, cs.LG
- Authors: Hongwei Du, Dingyang Lv, Baole Wei, Yongheng Li, Feng Yu, Ziheng Lu
- Link: https://arxiv.org/abs/2608.25592v1
- Score: 9.0
- Match: 摘要匹配 DeepMD; 近两周发布

**中文摘要：** 无机固态电解质必须结合高室温离子电导率、宽电化学窗口、优异的电子绝缘性和良好的机械顺应性。由于训练数据分布不匹配、跨属性数据集异质性和稀缺的动力学传输数据，单一模型难以支持跨广阔化学空间的可靠多目标筛选。 为了克服这些限制，我们开发了一个分层协同深度学习框架，通过四个互补模块依次协调效率、准确性和可靠性。内部开发的 L-G-DCNN 和基于 DenseGNN 的多保真实现分别充当热力学粗筛选和多属性评估的成分和结构专家； MatterSim 和系统特定的 DeePMD 模型提供传输预评估和动力学验证。 系统基准测试表明，每个模块在其任务中均优于主流同行，而回顾性验证则建立了模块级准确性和端到端工作流程可靠性的双闭环验证。该框架应用于 30,364,908 个 Alex/ICSD 衍生候选物，识别出 97 种室温离子电导率为 0.109--59.0 mS/cm 的高性能候选物，包括 94 种卤化物、一种硼氢化物和两种氧化物。与独立实验数据的一致性证实，94 种卤化物中有 76 种属于报道的高电导率结构区域。 分析表明，Li$^{+}$跳跃网络连接性，而不是几何Li位点的数量，是室温离子电导率的核心决定因素。锂缺陷工程有效地增强了氧化物传输，而O$^{2-}$框架的固有刚性表明氧化物电解质性能的潜在上限。
**讨论重点：** 为了克服这些限制，我们开发了一个分层协同深度学习框架，通过四个互补模块依次协调效率、准确性和可靠性。由于训练数据分布不匹配、跨属性数据集异质性和稀缺的动力学传输数据，单一模型难以支持跨广阔化学空间的可靠多目标筛选。 结合关键词看，阅读时应重点关注DeepMD相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. Unlocking Multi-Component Bulk-Materials Molecular Dynamics with a Small-Footprint Machine Learning Interatomic Potential

- Source: arXiv
- Date: 2026-08-17T09:32:51Z
- Venue: physics.comp-ph
- Authors: Yucheng Ouyang, Xin Chen, Ying Liu, Lifang Wang, Xingyu Gao, Xiawei Du
- Link: https://arxiv.org/abs/2608.16329v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 与纳米材料相反，块体材料需要在大空间尺度（~10^9 个原子或更多）上进行分子动力学 (MD) 模拟，以充分捕获其原子尺度的物理特性。此前，机器学习原子间势（MLIP）的引入已将MD扩展到如此规模，但即使是单组件批量系统也需要在高端超级计算机上使用数万个GPU。 然而，多组件批量 MD 模拟仍然难以实现，因为现有 MLIP 的 HBM 足迹（对于单组件系统来说已经很大）在多组件场景中呈爆炸性增长。本文提出了一种 HBM 占用空间较小的 MLIP（不到现有 MLIP 的 3%），仅使用数百个 GPU 即可解锁多组件批量 MD。这是通过首先将特征向量和中间张量识别为现有 MLIP 中 HBM 足迹的两个主要贡献者来实现的。 为了解决这两个来源，通过引入物理和化学知识来降低特征向量的维数，并通过积极地将所有内核融合到单个巨型内核中来消除中间张量。在评估中，所提出的MLIP使用了144个NVIDIA A100 GPU对具有1.14x10^9原子的6分量体系统进行MD模拟，而此前这种MD模拟空间尺度仅限于一元系统，通常在配备数万个GPU的高端超级计算机上实现。
**讨论重点：** 与纳米材料相反，块体材料需要在大空间尺度（~10^9 个原子或更多）上进行分子动力学 (MD) 模拟，以充分捕获其原子尺度的物理特性。此前，机器学习原子间势（MLIP）的引入已将MD扩展到如此规模，但即使是单组件批量系统也需要在高端超级计算机上使用数万个GPU。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 8. Cross-Geometry Transferability Assessment of Universal Machine Learning Interatomic Potentials: From Bulk Materials to Atomic Nanowires

- Source: arXiv
- Date: 2026-08-07T00:15:49Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.comp-ph
- Authors: Pedro H. M. Zanineli, Bruno Focassio, Gabriel R. Schleder
- Link: https://arxiv.org/abs/2608.06662v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 基础机器学习原子间势（MLIP）能够以比第一原理方法低得多的计算成本进行原子模拟，但它们在结构几何形状上的可靠性仍然没有得到充分的了解。在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。 我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。在没有任何训练的情况下，仅在参考能量对准后，最佳零射击模型（ORB-V3）的能量和力均方根误差分别达到 6 meV/atom 和 197.3 meV/Å，其中颈部和线配置中的力误差最大。然后，我们比较零样本推理、微调和从头开始训练策略。与从头开始训练相比，微调产生的能量和力量误差更低，而两者都需要相当的挂钟时间。 特定于几何形状的微调提高了域内精度，但经常产生向其他结构类别的负转移，而混合几何微调则减少了跨几何误差。对弹性和振动特性、表面能和颈部动力学的评估进一步表明，基于平均能量和力误差的排名并不能普遍预测属性水平的行为。这些结果表明，在将基础 MLIP 应用于低配位（离子）纳米结构时，几何形状多样化的目标数据和独立的物理验证是必要的。
**讨论重点：** 在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. Ultrafast Nonthermal Lattice Destabilization and Suppression of Polar Optical Scattering in Electronically Excited $α$-SiO$_2$ from First-Principles and Deep Neural Network Potential Modeling

- Source: arXiv
- Date: 2026-07-30T21:04:07Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Iyyappa Rajan Panneerselvam, Mark Yeung, Charlotte Palmer, Brendan Dromey, Lorenzo Stella
- Link: https://arxiv.org/abs/2607.28838v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。使用 DNNP 可以对具有数千个原子的大型 $α$-SiO$_2$ 单元进行接近 DFT 精度的原子建模。 特别是，DNNP 使我们能够获得由电子温度突然升高激发的 $α$-SiO$_2$ 的精确声子能带结构和分子动力学 (MD)。随着电子温度 $T_e$ 的增加，发现 $α$-SiO$_2$ 出现明显的晶格失稳，表现为违反弹性稳定性标准、体积大幅膨胀、体积模量急剧下降以及由于反键态占据而导致 Si-O 键逐渐减弱。 根据电子和声子能带结构，我们估计了 Frohlich 耦合常数，该常数随着 $T_e$ 的增加而减小，表明在电子温度升高时会交叉到 $α$-SiO$_2$ 的非极性相。 Bader 电荷分析证实了这一点。我们还建议，在 $T_e > 2$ eV 时应强烈抑制极性光学声子散射。从大单元 DNNP-MD 模拟中，我们表明，在最初的几百飞秒内，并未实现由麦克斯韦-玻尔兹曼分布定义的明确热平衡。 这种行为解释了 $T_e$ 突然上升后动力学温度的非单调平衡。当 $T_e$ 升至 2.6 eV 后，Si 和 O 原子首先在两个不同的温度下分别达到平衡，表明存在原子流体相，这与最近的实验和理论发现一致。
**讨论重点：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 10. PASS: Perturbation augmented space group structure sampling for transferable Fe-O machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-30T10:48:01Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Zixiong Wei, Fei Shuang, Poulumi Dey
- Link: https://arxiv.org/abs/2607.28000v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 铁（Fe）氧化的准确原子建模需要可靠的原子间势，这需要广泛且具有代表性的第一性原理数据集来训练原子间势。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。 我们提出了一种系统方法，基于原子团簇扩展 (ACE) 框架，为 Fe-O 系统开发首个可转移机器学习原子间势 (MLIP)。我们通过体积、表面和界面特性彻底验证了 ACE MLIP 在纯 Fe 和 Fe-O 系统中的准确性和功能。我们展示了使用 ACE MLIP 大规模 Fe 氧化模拟中 FeO 类结构的形成。 这项工作表明，PASS 方法产生了准确且可转移的 MLIP，它能够捕获氧化物生长的反应复杂性，同时保持扩展系统的计算实用性。
**讨论重点：** 在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

## 凝聚态物理强关联体系和多铁性质

### 1. Calculation of NMR Shieldings for Strongly Correlated Molecules Using the Density Matrix Renormalization Group Self-Consistent-Field Method with Large Active Spaces

- Source: Journal
- Date: 2026-09-02
- Venue: Journal of Chemical Theory and Computation
- Authors: Jiaao Su, Wei Huang, Yinxuan Song, Haibo Ma
- Link: https://doi.org/10.1021/acs.jctc.6c01230
- Score: 16.0
- Match: 摘要匹配 strongly correlated systems; 标题匹配 density matrix renormalization group; 近两周发布

**中文摘要：** 摘要 准确预测强相关系统的核磁共振 (NMR) 屏蔽常数仍然具有挑战性。在这种情况下，我们提出了一种密度矩阵重整化群自洽场 (DMRG-SCF) 实现，用于具有大活动空间的 NMR 屏蔽计算。在包含规范的原子轨道 DMRG-SCF (GIAO–DMRG-SCF) 框架内，我们使用局域有效哈密顿量制定并求解耦合扰动 DMRG-SCF (CP-DMRG-SCF) 方程。 这种方法可以直接评估波函数对外部磁场的响应。在小活动空间的限制下，计算的 NMR 屏蔽与传统的完整活动空间自洽场 (CASSCF) 结果一致，而本方法自然可以扩展到标准多配置方法无法访问的更大活动空间。对一系列分子系统，特别是强相关的过渡金属配合物的应用表明，所提出的实现既可靠又准确。
**讨论重点：** 在这种情况下，我们提出了一种密度矩阵重整化群自洽场 (DMRG-SCF) 实现，用于具有大活动空间的 NMR 屏蔽计算。在包含规范的原子轨道 DMRG-SCF (GIAO–DMRG-SCF) 框架内，我们使用局域有效哈密顿量制定并求解耦合扰动 DMRG-SCF (CP-DMRG-SCF) 方程。 结合关键词看，阅读时应重点关注强关联体系、密度矩阵重整化群相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。
